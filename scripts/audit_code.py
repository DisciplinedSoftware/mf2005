import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path

try:
    import code_statistics
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import code_statistics


ROOT = Path(__file__).resolve().parents[1]
BUILD_TYPES = ("release", "debug", "debugoptimized", "plain", "minsize", "custom")
PRECISIONS = ("single", "double")

# Category label, followed by the case-insensitive pattern that identifies a
# compiler diagnostic message as belonging to that category.
CATEGORIES = (
    ("obsolescent", "Obsolescent", re.compile(r"obsolescent", re.I)),
    ("implicit_interface", "Implicit interface", re.compile(r"implicit interface|explicit type", re.I)),
    ("conversion", "Conversion", re.compile(r"possible change of value", re.I)),
    ("real_comparison", "Real comparison", re.compile(r"comparison for real", re.I)),
    ("unused", "Unused", re.compile(r"unused|not used", re.I)),
    ("tabs", "Tabs", re.compile(r"nonconforming tab", re.I)),
    ("c_sign_conversion", "C sign conversion", re.compile(r"change the sign", re.I)),
    ("c_float_conversion", "C float conversion", re.compile(r"may change value", re.I)),
)

# Extra CSS/JS appended to code_statistics.TABLE_CSS/TABLE_JS to support the
# clickable tag chips used to filter the unique-warnings table by config.
TAG_CHIP_CSS = """
    #unique-warnings-table { max-width: none; }

  .tag-chip { display: inline-block; margin: .15rem .3rem .15rem 0; padding: .15rem .55rem;
    border: 1px solid #d0d7de; border-radius: 999px; background: #f6f8fa; font-size: .85rem;
    cursor: pointer; }
  .tag-chip.active { background: #0969da; color: #fff; border-color: #0969da; }
"""

TAG_CHIP_JS = """
document.querySelectorAll(".tag-chip").forEach(chip => {
  chip.addEventListener("click", () => {
    const input = document.getElementById(chip.dataset.filterInput);
    if (!input) return;
    const selecting = input.value !== chip.dataset.tag;
    input.value = selecting ? chip.dataset.tag : "";
    input.dispatchEvent(new Event("input"));
    document.querySelectorAll(`.tag-chip[data-filter-input="${chip.dataset.filterInput}"]`)
      .forEach(c => c.classList.remove("active"));
    if (selecting) chip.classList.add("active");
  });
});
"""

# Matches a Fortran-style diagnostic block: "<file>:<line>:<col>:", a blank
# line, source context, then the "Warning:"/"Error:" message.
FORTRAN_DIAGNOSTIC_BLOCK = re.compile(
    r"(?P<file>[\w./\\-]+\.(?:f90|f|F90|F)):(?P<line>\d+):\d+:\s*\n"
    r"\s*\n"
    r"(?P<context>(?:.*\n){1,6}?)"
    r"(?P<severity>Warning|Error):\s*(?P<message>.+)"
)

# Matches a GCC-style C diagnostic: "<file>:<line>:<col>: warning: <message>"
# on one line, followed immediately by the source context.
C_DIAGNOSTIC_BLOCK = re.compile(
    r"(?P<file>[\w./\\-]+\.(?:c|h|C)):(?P<line>\d+):\d+:\s*(?P<severity>warning|error):\s*(?P<message>.+)\n"
    r"(?P<context>(?:.*\n){1,4}?)(?=\n|\Z)"
)


@dataclass(frozen=True)
class Compiler:
    name: str
    fortran: str
    c: str


COMPILERS = {
    "gcc": Compiler("gcc", "gfortran", "gcc"),
    "intel": Compiler("intel", "ifx", "icx"),
}


class Progress:
    """Print a live one-line-per-stage progress indicator for a fixed-size run.

    Builds/coverage runs redirect their subprocess output to log files, so
    without this the audit goes silent for minutes at a time. On a tty, each
    update overwrites the previous line; otherwise (e.g. CI logs) every
    update is printed as its own line.
    """

    def __init__(self, total, label="Progress"):
        self.total = total
        self.label = label
        self.done = 0
        self.start_time = time.monotonic()
        self.tty = sys.stdout.isatty()

    def _bar(self, width=24):
        filled = width if self.total == 0 else int(width * self.done / self.total)
        return "#" * filled + "." * (width - filled)

    def _write(self, name, stage, final):
        elapsed = time.monotonic() - self.start_time
        line = f"[{self._bar()}] {self.done}/{self.total} ({elapsed:6.1f}s) {self.label}: {name}: {stage}"
        if self.tty:
            width = shutil.get_terminal_size((100, 20)).columns
            sys.stdout.write("\r" + line[:width].ljust(width))
            if final:
                sys.stdout.write("\n")
            sys.stdout.flush()
        else:
            print(line)

    def step(self, name, stage):
        self._write(name, stage, final=False)

    def finish(self, name, stage):
        self.done += 1
        self._write(name, stage, final=True)


def run(command, environment, log_file):
    with log_file.open("w", encoding="utf-8") as stream:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            stdout=stream,
            stderr=subprocess.STDOUT,
            check=False,
        )
    return completed.returncode


def iter_diagnostic_records(log_file):
    """Yield compiler diagnostics with their file, line, severity, and category."""
    if not log_file.exists():
        return []
    text = log_file.read_text(encoding="utf-8", errors="replace")
    records = []
    for match in (*FORTRAN_DIAGNOSTIC_BLOCK.finditer(text), *C_DIAGNOSTIC_BLOCK.finditer(text)):
        severity = match.group("severity").title()
        message = match.group("message").strip()
        category = next((key for key, _, pattern in CATEGORIES if pattern.search(message)), None)
        records.append({
            "file": match.group("file"),
            "line": match.group("line"),
            "severity": severity,
            "message": message,
            "category": category,
        })
    return records


def warning_counts(log_file):
    counts = {"warnings": 0, "errors": 0}
    counts.update({key: 0 for key, _, _ in CATEGORIES})
    if not log_file.exists():
        return counts
    for record in iter_diagnostic_records(log_file):
        if record["severity"] == "Warning":
            counts["warnings"] += 1
        elif record["severity"] == "Error":
            counts["errors"] += 1
        if record["category"] is not None:
            counts[record["category"]] += 1
    return counts


def summarize_coverage(summary):
    """Return a compact coverage summary from gcovr JSON output."""
    if not summary:
        return {}
    payload = {
        "line_covered": summary.get("line_covered", 0),
        "line_total": summary.get("line_total", 0),
        "line_percent": summary.get("line_percent", 0.0),
        "branch_covered": summary.get("branch_covered", 0),
        "branch_total": summary.get("branch_total", 0),
        "branch_percent": summary.get("branch_percent", 0.0),
        "function_covered": summary.get("function_covered", 0),
        "function_total": summary.get("function_total", 0),
        "function_percent": summary.get("function_percent", 0.0),
    }
    return payload


def coverage_summary(build_dir):
    """Run gcovr and summarize a coverage build if it exists."""
    if not build_dir.exists():
        return None
    completed = subprocess.run(
        [
            "gcovr",
            "--root",
            ".",
            "--object-directory",
            str(build_dir),
            "--filter",
            "src/",
            "--json-summary",
            # Same known-gcov-bug tolerance as scripts/coverage.py; without it
            # gcovr exits 64 and the report silently loses its coverage table.
            "--gcov-ignore-parse-errors",
            "suspicious_hits.warn_once_per_file",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        return None
    try:
        payload = __import__("json").loads(completed.stdout)
    except ValueError:
        return None
    return summarize_coverage(payload)


def parse_diagnostics(log_file):
    """Extract (file, line, message, category) for every diagnostic block in a log.

    Line number is kept only for display; it is not part of the dedup key
    used elsewhere, since the same warning can appear at different lines
    across precision/#ifdef variants of the same source file.
    """
    diagnostics = []
    for record in iter_diagnostic_records(log_file):
        diagnostics.append((record["file"], record["line"], record["message"], record["category"]))
    return diagnostics


def unique_warning_counts(log_files):
    """Count distinct (file, message) warnings across a set of logs.

    This collapses duplicates that arise from auditing the same source across
    multiple build types/precisions/compilers, so a warning present in every
    variant is only counted once instead of once per variant.
    """
    seen = set()
    counts = {key: 0 for key, _, _ in CATEGORIES}
    counts["warnings"] = 0
    for log_file in log_files:
        for file_name, _, message, category in parse_diagnostics(log_file):
            key = (file_name, message)
            if key in seen:
                continue
            seen.add(key)
            counts["warnings"] += 1
            if category is not None:
                counts[category] += 1
    return counts


def build_category_rows(results, compiler_names=None, precisions=None):
    """Return rows for the per-category warning summary table.

    Each row includes the compiler, precision, total warning count, and one count
    for every warning category.
    """
    names = sorted({compiler_names} if isinstance(compiler_names, str) else set(compiler_names or {r["compiler"] for r in results}))
    selected_precisions = tuple(precisions or PRECISIONS)
    rows = []
    for compiler_name in names:
        for precision in selected_precisions:
            matches = [r for r in results if r["compiler"] == compiler_name and r["precision"] == precision]
            rows.append(
                (
                    compiler_name,
                    precision,
                    sum(r["counts"]["warnings"] for r in matches),
                    *(sum(r["counts"][key] for r in matches) for key, _, _ in CATEGORIES),
                )
            )
    return rows


def collect_unique_warnings(results):
    """Build one entry per distinct (file, message) warning, tagged with every
    compiler, build type, and precision that produces it.
    """
    entries = {}
    for r in results:
        tags = {
            f"compiler:{r['compiler']}",
            f"build-type:{r['build_type']}",
            f"precision:{r['precision']}",
        }
        for file_name, line, message, category in parse_diagnostics(r["log_file"]):
            key = (file_name, message)
            entry = entries.setdefault(
                key, {"file": file_name, "line": line, "message": message, "category": category, "tags": set()}
            )
            entry["tags"].update(tags)
    return sorted(entries.values(), key=lambda e: (e["file"], int(e["line"]), e["message"]))


def find_examples(log_files):
    """Find the first representative diagnostic block for each warning category."""
    examples = {key: None for key, _, _ in CATEGORIES}
    for log_file in log_files:
        if all(examples.values()) or not log_file.exists():
            continue
        text = log_file.read_text(encoding="utf-8", errors="replace")
        matches = sorted(
            (*FORTRAN_DIAGNOSTIC_BLOCK.finditer(text), *C_DIAGNOSTIC_BLOCK.finditer(text)),
            key=lambda m: m.start(),
        )
        for match in matches:
            message = match.group("message").strip()
            for key, _, pattern in CATEGORIES:
                if examples[key] is None and pattern.search(message):
                    examples[key] = {
                        "file": match.group("file"),
                        "line": match.group("line"),
                        "message": message,
                        "context": match.group("context").rstrip("\n"),
                    }
    return examples


def available_compilers(requested):
    names = tuple(COMPILERS) if requested == "all" else (requested,)
    result = []
    missing = []
    for name in names:
        compiler = COMPILERS[name]
        if shutil.which(compiler.fortran) and shutil.which(compiler.c):
            result.append(compiler)
        else:
            missing.append(name)
    if missing:
        missing_tools = ", ".join(
            f"{name} ({COMPILERS[name].fortran}/{COMPILERS[name].c})" for name in missing
        )
        raise RuntimeError(
            f"Compiler(s) unavailable: {missing_tools}. "
            "For Intel, source /opt/intel/oneapi/setvars.sh first."
        )
    return result


def run_coverage(compiler, build_types, precisions, log_dir, report_dir):
    """Build, test, and report coverage for each selected configuration."""
    coverage_codes = []
    environment = os.environ.copy()
    environment.update({"FC": compiler.fortran, "CC": compiler.c})
    progress = Progress(len(build_types) * len(precisions), label="Coverage")
    for build_type in build_types:
        for precision in precisions:
            variant = f"{compiler.name}-{build_type}-{precision}"
            progress.step(variant, "running")
            log_file = log_dir / f"{variant}-coverage.log"
            coverage_report = report_dir / f"coverage-{variant}.html"
            command = [
                sys.executable,
                "scripts/coverage.py",
                precision,
                "--buildtype",
                build_type,
                "--output",
                str(coverage_report),
            ]
            with log_file.open("w", encoding="utf-8") as stream:
                stream.write("$ " + " ".join(command) + "\n")
                stream.flush()  # else the buffered header lands after the child's output
                completed = subprocess.run(
                    command,
                    cwd=ROOT,
                    env=environment,
                    stdout=stream,
                    stderr=subprocess.STDOUT,
                    check=False,
                )
            status = "PASS" if completed.returncode == 0 else f"FAIL ({completed.returncode})"
            progress.finish(variant, status)
            coverage_codes.append((variant, completed.returncode))
    return coverage_codes


def main():
    parser = argparse.ArgumentParser(
        description="Build every warning-audit configuration and generate a code-audit report."
    )
    parser.add_argument(
        "--compiler",
        choices=("gcc", "intel", "all"),
        default="all",
        help="Compiler(s) to audit (default: all); use all for every compiler.",
    )
    parser.add_argument(
        "--build-type",
        choices=(*BUILD_TYPES, "all"),
        default="all",
        help="Meson build type to audit (default: all).",
    )
    parser.add_argument(
        "--precision",
        choices=(*PRECISIONS, "all"),
        default="all",
        help="Precision to audit (default: all).",
    )
    parser.add_argument(
        "--coverage-compiler",
        choices=("gcc",),
        default="gcc",
        help="Compiler for coverage (default: gcc).",
    )
    parser.add_argument(
        "--coverage-build-type",
        choices=(*BUILD_TYPES, "all"),
        default="release",
        help="Meson build type for coverage (default: release).",
    )
    parser.add_argument(
        "--coverage-precision",
        choices=(*PRECISIONS, "all"),
        default="single",
        help="Precision for coverage (default: single).",
    )
    parser.add_argument(
        "--coverage",
        action="store_true",
        help="Build, test, and include coverage summaries for the selected coverage configuration.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "builds" / "build-logs" / "code-audit",
        help="Directory for raw logs and the generated report.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=ROOT / "doc" / "reports" / "code-audit-report.html",
        help="HTML report path (default: doc/reports/code-audit-report.html).",
    )
    args = parser.parse_args()

    compilers = available_compilers(args.compiler)
    build_types = BUILD_TYPES if args.build_type == "all" else (args.build_type,)
    precisions = PRECISIONS if args.precision == "all" else (args.precision,)
    coverage_build_types = (
        BUILD_TYPES if args.coverage_build_type == "all" else (args.coverage_build_type,)
    )
    coverage_precisions = (
        PRECISIONS if args.coverage_precision == "all" else (args.coverage_precision,)
    )
    if args.output == ROOT / "builds" / "build-logs" / "code-audit":
        run_name = f"{args.compiler}-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{os.getpid()}"
        output = args.output / run_name
    else:
        output = args.output if args.output.is_absolute() else ROOT / args.output
    output.mkdir(parents=True, exist_ok=True)
    results = []

    progress = Progress(len(compilers) * len(build_types) * len(precisions), label="Audit")
    for compiler in compilers:
        for build_type in build_types:
            for precision in precisions:
                variant = f"{compiler.name}-{build_type}-{precision}"
                progress.step(variant, "setup")
                build_dir = ROOT / "builds" / f"build-code-audit-{variant}"
                log_file = output / f"{variant}.log"
                environment = os.environ.copy()
                environment.update({"FC": compiler.fortran, "CC": compiler.c})
                setup = [
                    "meson",
                    "setup",
                    "--wipe",
                    str(build_dir),
                    str(ROOT),
                    f"--buildtype={build_type}",
                    f"-Ddouble={'true' if precision == 'double' else 'false'}",
                    "-Dwarning_audit=true",
                ]
                compile_command = ["meson", "compile", "-C", str(build_dir), "-j1"]
                setup_code = run(setup, environment, log_file)
                compile_code = None
                if setup_code == 0:
                    progress.step(variant, "compile")
                    with log_file.open("a", encoding="utf-8") as stream:
                        stream.write("\n$ " + " ".join(compile_command) + "\n")
                    with log_file.open("a", encoding="utf-8") as stream:
                        compile_code = subprocess.run(
                            compile_command,
                            cwd=ROOT,
                            env=environment,
                            stdout=stream,
                            stderr=subprocess.STDOUT,
                            check=False,
                        ).returncode
                counts = warning_counts(log_file)
                status = "PASS" if setup_code == 0 and compile_code == 0 else "FAIL"
                progress.finish(variant, status)
                results.append(
                    {
                        "compiler": compiler.name,
                        "build_type": build_type,
                        "precision": precision,
                        "setup_code": setup_code,
                        "compile_code": compile_code,
                        "counts": counts,
                        "log_file": log_file,
                    }
                )

    report = args.report if args.report.is_absolute() else ROOT / args.report
    report.parent.mkdir(parents=True, exist_ok=True)
    coverage_codes = []
    if args.coverage:
        coverage_compiler = COMPILERS[args.coverage_compiler]
        coverage_codes = run_coverage(
            coverage_compiler,
            coverage_build_types,
            coverage_precisions,
            output,
            report.parent,
        )

    write_report(
        report,
        results,
        compilers,
        output,
        build_types,
        precisions,
        args.coverage,
        coverage_build_types,
        coverage_precisions,
    )

    failed = [r for r in results if r["setup_code"] != 0 or r["compile_code"] != 0]
    failed_coverage = [variant for variant, code in coverage_codes if code != 0]
    print(f"Audit report: {report}")
    print(f"Variants: {len(results)}, passed: {len(results) - len(failed)}, failed: {len(failed)}")
    if failed_coverage:
        print(f"Coverage failed: {', '.join(failed_coverage)}")
    return 1 if failed or failed_coverage else 0


def write_report(
    report,
    results,
    compilers,
    log_dir,
    build_types,
    precisions,
    include_coverage=False,
    coverage_build_types=BUILD_TYPES,
    coverage_precisions=PRECISIONS,
):
    passed = [r for r in results if r["setup_code"] == 0 and r["compile_code"] == 0]
    columns = [(c.name, p) for c in compilers for p in precisions]

    def cell(compiler_name, build_type, precision):
        match = next(
            (r for r in results if r["compiler"] == compiler_name
             and r["build_type"] == build_type and r["precision"] == precision),
            None,
        )
        if match is None:
            return "n/a"
        ok = match["setup_code"] == 0 and match["compile_code"] == 0
        return "PASS" if ok else f"FAIL (setup={match['setup_code']}, compile={match['compile_code']})"

    matrix_rows = [
        (build_type, *(cell(name, build_type, precision) for name, precision in columns))
        for build_type in build_types
    ]
    matrix_table = code_statistics.html_table(
        ["Build type", *(f"{name} {precision}" for name, precision in columns)],
        matrix_rows,
        sortable=False,
    )

    category_rows = build_category_rows(
        results,
        {compiler_name for compiler_name, _ in columns},
        precisions,
    )
    category_table = code_statistics.html_table(
        ["Compiler", "Precision", "Total", *(label for _, label, _ in CATEGORIES)],
        category_rows,
        numeric_columns=tuple(range(2, len(CATEGORIES) + 3)),
        sortable=False,
    )

    dedup_rows = []
    for compiler_name in {c.name for c in compilers}:
        compiler_logs = [r["log_file"] for r in results if r["compiler"] == compiler_name]
        unique_counts = unique_warning_counts(compiler_logs)
        dedup_rows.append(
            (compiler_name, unique_counts["warnings"], *(unique_counts[key] for key, _, _ in CATEGORIES))
        )
    dedup_table = code_statistics.html_table(
        ["Compiler", "Unique warnings", *(label for _, label, _ in CATEGORIES)],
        dedup_rows,
        numeric_columns=tuple(range(1, len(CATEGORIES) + 2)),
        sortable=False,
    )

    def source_path(file_name):
        normalized = file_name.replace("\\", "/")
        if "/src/" in normalized:
            return "src/" + normalized.split("/src/", 1)[1]
        if normalized.startswith("src/"):
            return normalized
        return normalized

    examples = find_examples([r["log_file"] for r in results])
    totals = {key: sum(r["counts"][key] for r in results) for key, _, _ in CATEGORIES}
    highlights = []
    for key, label, _ in CATEGORIES:
        if totals[key] == 0:
            continue
        example = examples.get(key)
        if example is None:
            highlights.append(
                f"<h3>{html.escape(label)} ({totals[key]} occurrences)</h3>"
                "<p>No representative log snippet was captured for this category.</p>"
            )
        else:
            highlights.append(
                f"<h3>{html.escape(label)} ({totals[key]} occurrences)</h3>"
                f"<p>Example log output:</p><pre>{html.escape(example['message'])}</pre>"
                f"<p>Representative source snippet from <code>{html.escape(source_path(example['file']))}:"
                f"{html.escape(example['line'])}</code>:</p><pre>{html.escape(example['context'])}</pre>"
            )

    coverage_rows = []
    if include_coverage:
        for build_type in coverage_build_types:
            for precision in coverage_precisions:
                build_dir = ROOT / "builds" / f"build-{build_type}-{precision}-coverage"
                summary = coverage_summary(build_dir)
                if summary:
                    coverage_rows.append(
                        (
                            build_type,
                            precision,
                            summary["line_percent"],
                            summary["branch_percent"],
                            summary["function_percent"],
                        )
                    )
    if coverage_rows:
        coverage_table = code_statistics.html_table(
            ["Build type", "Precision", "Line coverage %", "Branch coverage %", "Function coverage %"],
            coverage_rows,
            numeric_columns=(2, 3, 4),
            sortable=False,
        )
        coverage_section = (
            "<h2>3. Coverage Summary</h2>"
            f"{coverage_table}"
        )
    elif include_coverage:
        coverage_section = (
            "<h2>3. Coverage Summary</h2>"
            "<p>No coverage build was found. Generate one with <code>python scripts/coverage.py</code> "
            "or <code>pixi run coverage</code> before reviewing coverage metrics.</p>"
        )
    else:
        coverage_section = ""

    total_warnings = sum(r["counts"]["warnings"] for r in results)
    total_errors = sum(r["counts"]["errors"] for r in results)
    if len(passed) == len(results):
        assessment = (
            f"All {len(results)} warning-audit variants compiled successfully with a combined "
            f"{total_warnings} warnings and {total_errors} errors across logs. The build is healthy; "
            "the diagnostics below are modernization backlog items, not build blockers."
        )
    else:
        assessment = (
            f"{len(results) - len(passed)} of {len(results)} warning-audit variants failed to build. "
            "Investigate the failing variants before treating the warning counts below as "
            "representative of the current codebase."
        )

    category_label = {key: label for key, label, _ in CATEGORIES}
    unique_warnings = collect_unique_warnings(results)
    warning_rows = [
        (source_path(w["file"]), w["line"], category_label.get(w["category"], "Other"), w["message"], ", ".join(sorted(w["tags"])))
        for w in unique_warnings
    ]
    warning_table = code_statistics.html_table(
        ["File", "Line", "Category", "Message", "Tags"],
        warning_rows,
        numeric_columns=(1,),
        table_id="unique-warnings-table",
    )
    all_tags = sorted({tag for w in unique_warnings for tag in w["tags"]})
    tag_chips = "".join(
        f'<button type="button" class="tag-chip" data-filter-input="unique-warnings-filter" '
        f'data-tag="{html.escape(tag)}">{html.escape(tag)}</button>'
        for tag in all_tags
    )

    assessment_summary = html.escape(assessment)
    body = (
        "<h1>MF2005 Code Audit Report</h1>"
        f"<p class=\"muted\">Generated on {datetime.now().strftime('%Y-%m-%d')}. "
        "This is a modernization status snapshot; rerun the audit to refresh it.</p>"
        f"<p class=\"muted\">{code_statistics.git_status_line()}</p>"
        f"<p>{assessment_summary}</p>"
        f"{code_statistics.render_statistics_body(code_statistics.compute_statistics(), 2, '1. Code Statistics')}"
        "<h2>2. Matrix Result</h2>"
        f"{matrix_table}<p>Total: {len(passed)} of {len(results)} warning-audit builds passed.</p>"
        f"{coverage_section}"
        "<h2>4. Warning Audit</h2>"
        "<h3>4a. Warning Flags Enabled</h3>"
        f"{warning_flags_html(compilers)}"
        "<h3>4b. Warning Category Counts</h3>"
        "<p>Counts are total occurrences across all build type and precision variants for each "
        "compiler/precision combination.</p>"
        f"{category_table}"
        "<h3>4c. Deduplicated Warning Counts</h3>"
        "<p>This table counts each distinct "
        "<code>(file, message)</code> warning once per compiler, merged across all build types and "
        "precisions. Line number is deliberately excluded from the dedup key, since the same warning "
        "can shift lines between precision-conditional (<code>#ifdef</code>) branches of a file.</p>"
        f"{dedup_table}"
        "<h2>5. Warning Highlights</h2>"
        f"{''.join(highlights)}"
        "<h2>6. All Unique Warnings</h2>"
        "<p>Every distinct <code>(file, message)</code> warning, tagged independently by compiler, build type, "
        "and precision. Click a tag to filter the table to warnings reproducible with that value, or type in the "
        "box to filter by any text.</p>"
        "<details><summary>"
        f"Unique warnings ({len(unique_warnings)})</summary>"
        f"<p>{tag_chips}</p>"
        '<input class="filter" id="unique-warnings-filter" data-target="unique-warnings-table" '
        'type="text" placeholder="Filter by file, message, or config...">'
        f"{warning_table}</details>"
    )
    report.write_text(
        "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        "<title>MF2005 Code Audit Report</title>"
        f"<style>{code_statistics.TABLE_CSS}{TAG_CHIP_CSS}</style></head><body>{body}"
        f"<script>{code_statistics.TABLE_JS}{TAG_CHIP_JS}</script></body></html>",
        encoding="utf-8",
    )


def warning_flags_html(compilers):
    return "".join(
        f"<p>{html.escape(line.replace('`', ''))}</p>"
        for line in warning_flags_text(compilers).splitlines()
        if line.strip()
    )


def warning_flags_text(compilers):
    lines = []
    names = {c.name for c in compilers}
    if "gcc" in names:
        lines.append(
            "GCC (Fortran): `-Wall`, `-Wextra`, `-Wpedantic`, `-Wimplicit-interface`, `-Wtabs`, "
            "`-Wsurprising`, `-Wconversion`, `-fcheck=all`, `-fbacktrace`\n\n"
        )
        lines.append("GCC (C): `-Wall`, `-Wextra`, `-Wpedantic`, `-Wshadow`, `-Wconversion`\n\n")
    if "intel" in names:
        lines.append("Intel LLVM (Fortran): `-warn all`, `-stand f18`, `-check all`\n\n")
        lines.append("Intel LLVM (C): `-Wall`, `-Wextra`, `-Wpedantic`, `-Wshadow`, `-Wconversion`\n\n")
    return "".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())