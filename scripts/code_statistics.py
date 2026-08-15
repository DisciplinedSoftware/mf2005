"""Lexical static-analysis statistics for the MF2005 production source.

Scans src/* fixed-form and free-form Fortran source plus C source files -- not
the hydprograms/ utility program, generated code, or test sources -- and
reports size, structure, preprocessing, and complexity metrics. This is a
lexical scanner, not a full parser; treat the complexity numbers as
comparative, not audit-grade.
"""
import argparse
import html
import re
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Fixed-form: .f/.for/.ftn are never preprocessed; .fpp is fixed-form with
# C-preprocessing (gfortran/ifort convention). Free-form: .f90/.f95/.f03/
# .f08/.f18, with or without preprocessing. C sources and headers are also
# counted in the production-source pass.
FIXED_FORM_EXTENSIONS = {".f", ".for", ".ftn", ".fpp"}
FREE_FORM_EXTENSIONS = {".f90", ".f95", ".f03", ".f08", ".f18"}
C_EXTENSIONS = {".c", ".h"}
SOURCE_EXTENSIONS = tuple(FIXED_FORM_EXTENSIONS | FREE_FORM_EXTENSIONS | C_EXTENSIONS)

DECISION_KEYWORDS = re.compile(
    r"^(ELSE\s*IF|IF)\s*\(|^DO\b|^SELECT\s*CASE\b|^CASE\b|^WHERE\b|^FORALL\b",
    re.IGNORECASE,
)
BLOCK_OPEN = re.compile(r"^(IF)\s*\(.*\)\s*THEN\b|^DO\b|^SELECT\s*CASE\b|^WHERE\b|^FORALL\b", re.IGNORECASE)
BLOCK_CLOSE = re.compile(r"^END\s*(IF|DO|SELECT|WHERE|FORALL)\b", re.IGNORECASE)

PROC_START = re.compile(r"\b(SUBROUTINE|FUNCTION)\s+(\w+)", re.IGNORECASE)
PROC_END = re.compile(r"^END\s*(SUBROUTINE|FUNCTION)?\s*\w*\s*$", re.IGNORECASE)
MODULE_START = re.compile(r"^MODULE\s+(\w+)\b(?!\s*PROCEDURE)", re.IGNORECASE)
MODULE_END = re.compile(r"^END\s*MODULE\b", re.IGNORECASE)
INTERFACE_START = re.compile(r"^INTERFACE\b", re.IGNORECASE)
INTERFACE_END = re.compile(r"^END\s*INTERFACE\b", re.IGNORECASE)
COMMON_STATEMENT = re.compile(r"^COMMON\s*/", re.IGNORECASE)
COMMON_NAME = re.compile(r"/(\w+)/")
INCLUDE_STATEMENT = re.compile(r"^INCLUDE\s+", re.IGNORECASE)

PREPROCESSOR_DIRECTIVES = (
    "define", "if", "ifdef", "ifndef", "elif", "else", "endif", "include", "pragma",
)

# Intel/DEC compiler-directive comments: the comment marker immediately
# followed by DEC$ or DIR$ (no space) turns an ordinary Fortran comment line
# into a directive the compiler acts on (e.g. attribute or vectorization
# hints). Lexically indistinguishable from a plain comment except for this
# prefix, so they must be pulled out before falling into comment_lines.
FORTRAN_COMPILER_DIRECTIVES = ("dec$", "dir$")


def is_comment(line, free_form, is_c_file=False):
    if is_c_file:
        stripped = line.lstrip()
        return stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*")
    if free_form:
        return line.lstrip().startswith("!")
    return bool(line) and line[0] in "Cc*"


def fortran_directive_comment(line, free_form):
    """Return the DEC$/DIR$ keyword if this comment line is actually an
    Intel/DEC compiler directive, else None. Assumes is_comment() is True.
    """
    body = line.lstrip()[1:] if free_form else line[1:]
    body = body.lower()
    for keyword in FORTRAN_COMPILER_DIRECTIVES:
        if body.startswith(keyword):
            return keyword
    return None


def strip_inline_comment(statement):
    index = statement.find("!")
    return statement if index < 0 else statement[:index]


def git_info():
    """Return the current commit sha and whether the working tree has local modifications."""
    try:
        sha = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout.strip()
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {"sha": "unknown", "dirty": None}
    return {"sha": sha, "dirty": bool(status.strip())}


def source_files():
    return sorted(p for p in ROOT.joinpath("src").glob("*") if p.suffix.lower() in SOURCE_EXTENSIONS)


def scan_file(path, stats):
    suffix = path.suffix.lower()
    is_c_file = suffix in C_EXTENSIONS
    free_form = suffix in FREE_FORM_EXTENSIONS
    if is_c_file:
        form = stats["by_form"]["c"]
    else:
        form = stats["by_form"]["free" if free_form else "fixed"]
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    stats["physical_lines"] += len(lines)
    form["files"] += 1
    form["physical_lines"] += len(lines)

    in_interface = False
    procedure = None  # {name, file, cyclomatic, cognitive, _nesting}

    for raw_line in lines:
        if not raw_line.strip():
            stats["blank_lines"] += 1
            form["blank_lines"] += 1
            continue
        if is_comment(raw_line, free_form, is_c_file=is_c_file):
            stats["comment_lines"] += 1
            form["comment_lines"] += 1
            if not is_c_file:
                keyword = fortran_directive_comment(raw_line, free_form)
                if keyword is not None:
                    stats["directives"]["fortran"][keyword] += 1
            continue

        stripped = raw_line.strip()
        if stripped.startswith("#"):
            directive = stripped[1:].strip().split()[0].lower() if len(stripped) > 1 else ""
            directive_counts = stats["directives"]["c" if is_c_file else "fortran"]
            if directive in PREPROCESSOR_DIRECTIVES:
                directive_counts[directive] += 1
            else:
                directive_counts["other"] += 1
            continue

        if is_c_file:
            continue

        statement = strip_inline_comment(stripped).strip()
        if not statement:
            continue

        if INTERFACE_START.match(statement):
            in_interface = True
            continue
        if INTERFACE_END.match(statement):
            in_interface = False
            continue

        if MODULE_START.match(statement):
            stats["modules"] += 1
            continue
        if MODULE_END.match(statement):
            continue

        if COMMON_STATEMENT.match(statement):
            stats["common_statements"] += 1
            name_match = COMMON_NAME.search(statement)
            if name_match:
                stats["common_names"].add(name_match.group(1).upper())
            continue

        if INCLUDE_STATEMENT.match(statement):
            stats["includes"] += 1
            continue

        proc_match = PROC_START.search(statement) if not in_interface else None
        if proc_match and not statement.upper().startswith("END"):
            procedure = {
                "name": proc_match.group(2),
                "file": path.name,
                "cyclomatic": 1,
                "cognitive": 1,
                "_nesting": 0,
            }
            stats["procedures"].append(procedure)
            continue

        if procedure is not None and PROC_END.match(statement):
            procedure = None
            continue

        if procedure is None:
            continue

        if DECISION_KEYWORDS.match(statement):
            procedure["cyclomatic"] += 1
            procedure["cognitive"] += 1 + procedure["_nesting"]
        if BLOCK_OPEN.match(statement):
            procedure["_nesting"] += 1
        elif BLOCK_CLOSE.match(statement):
            procedure["_nesting"] = max(0, procedure["_nesting"] - 1)


def compute_statistics():
    stats = {
        "physical_lines": 0,
        "blank_lines": 0,
        "comment_lines": 0,
        "modules": 0,
        "common_statements": 0,
        "common_names": set(),
        "includes": 0,
        "procedures": [],
        "directives": {
            "fortran": {directive: 0 for directive in PREPROCESSOR_DIRECTIVES}
            | {directive: 0 for directive in FORTRAN_COMPILER_DIRECTIVES}
            | {"other": 0},
            "c": {directive: 0 for directive in PREPROCESSOR_DIRECTIVES} | {"other": 0},
        },
        "by_form": {
            "fixed": {"files": 0, "physical_lines": 0, "blank_lines": 0, "comment_lines": 0},
            "free": {"files": 0, "physical_lines": 0, "blank_lines": 0, "comment_lines": 0},
            "c": {"files": 0, "physical_lines": 0, "blank_lines": 0, "comment_lines": 0},
        },
    }
    files = source_files()
    for path in files:
        scan_file(path, stats)
    stats["files"] = files
    return stats


def top_n(procedures, key, n=10):
    return sorted(procedures, key=lambda p: p[key], reverse=True)[:n]


# Shared page assets: any HTML report embedding a "sortable-table" or a
# "filter" input reuses these instead of each report shipping its own.
TABLE_CSS = """
  body { font-family: -apple-system, Segoe UI, Helvetica, Arial, sans-serif; margin: 2rem; color: #1b1f24; }
  h1, h2, h3 { border-bottom: 1px solid #d0d7de; padding-bottom: .3rem; }
  table { border-collapse: collapse; margin: 0.5rem 0 1.5rem; width: 100%; max-width: 900px; }
  th, td { border: 1px solid #d0d7de; padding: .35rem .6rem; text-align: right; }
  th:first-child, td:first-child { text-align: left; }
  th { background: #f6f8fa; cursor: pointer; user-select: none; }
  th.sortable::after { content: " \\2195"; color: #999; }
  tr:nth-child(even) { background: #fafbfc; }
  details { margin: 1rem 0; }
  summary { cursor: pointer; font-weight: 600; padding: .4rem 0; }
  input.filter { padding: .3rem .5rem; width: 100%; max-width: 400px; margin-bottom: .5rem; }
  pre { background: #f6f8fa; padding: .6rem; overflow-x: auto; border: 1px solid #d0d7de; }
  .muted { color: #57606a; }
"""

TABLE_JS = """
function sortTable(table, columnIndex, numeric) {
  const tbody = table.tBodies[0];
  const rows = Array.from(tbody.rows);
  const asc = table.dataset.sortCol == columnIndex && table.dataset.sortDir !== "asc";
  rows.sort((a, b) => {
    let x = a.cells[columnIndex].textContent.trim();
    let y = b.cells[columnIndex].textContent.trim();
    if (numeric) { x = parseFloat(x.replace(/,/g, "")) || 0; y = parseFloat(y.replace(/,/g, "")) || 0; }
    if (x < y) return asc ? -1 : 1;
    if (x > y) return asc ? 1 : -1;
    return 0;
  });
  rows.forEach(r => tbody.appendChild(r));
  table.dataset.sortCol = columnIndex;
  table.dataset.sortDir = asc ? "asc" : "desc";
}

document.querySelectorAll("table.sortable-table").forEach(table => {
  table.querySelectorAll("th").forEach((th, index) => {
    th.classList.add("sortable");
    const numeric = th.dataset.numeric === "1";
    th.addEventListener("click", () => sortTable(table, index, numeric));
  });
});

document.querySelectorAll("input.filter").forEach(input => {
  input.addEventListener("input", () => {
    const term = input.value.toLowerCase();
    document.querySelectorAll(`#${input.dataset.target} tbody tr`).forEach(row => {
      row.style.display = row.textContent.toLowerCase().includes(term) ? "" : "none";
    });
  });
});
"""


def html_table(headers, rows, numeric_columns=(), table_id="", sortable=True):
    classes = "sortable-table" if sortable else ""
    id_attr = f' id="{table_id}"' if table_id else ""
    parts = [f'<table class="{classes}"{id_attr}>', "<thead><tr>"]
    for index, header in enumerate(headers):
        numeric = "1" if index in numeric_columns else "0"
        parts.append(f'<th data-numeric="{numeric}">{html.escape(header)}</th>')
    parts.append("</tr></thead><tbody>")
    for row in rows:
        parts.append("<tr>" + "".join(f"<td>{html.escape(str(cell))}</td>" for cell in row) + "</tr>")
    parts.append("</tbody></table>")
    return "".join(parts)


def render_statistics_body(stats, heading_level=2, title="Code Statistics"):
    """Render the code-statistics section as an HTML fragment, embeddable in any report page."""
    h, hh = f"h{heading_level}", f"h{heading_level + 1}"
    fixed = sum(1 for f in stats["files"] if f.suffix.lower() in FIXED_FORM_EXTENSIONS)
    free = sum(1 for f in stats["files"] if f.suffix.lower() in FREE_FORM_EXTENSIONS)
    c_files = sum(1 for f in stats["files"] if f.suffix.lower() in C_EXTENSIONS)
    code_lines = stats["physical_lines"] - stats["blank_lines"] - stats["comment_lines"]
    procedures = stats["procedures"]
    total_cyclomatic = sum(p["cyclomatic"] for p in procedures)
    total_cognitive = sum(p["cognitive"] for p in procedures)
    per_procedure_cyclomatic = total_cyclomatic / len(procedures) if procedures else 0
    per_procedure_cognitive = total_cognitive / len(procedures) if procedures else 0
    highest = max(procedures, key=lambda p: p["cyclomatic"], default=None)
    highest_note = (
        f"The highest observed cyclomatic complexity is {highest['cyclomatic']} in {highest['name']}."
        if highest is not None else ""
    )

    source_size_table = html_table(
        ["Metric", "Count"],
        [
            ("Source files", len(stats["files"])),
            ("Physical lines", f"{stats['physical_lines']:,}"),
            ("Blank lines", f"{stats['blank_lines']:,}"),
            ("Comment lines", f"{stats['comment_lines']:,}"),
            ("Code lines (nonblank, noncomment physical lines)", f"{code_lines:,}"),
        ],
        numeric_columns=(1,),
        sortable=False,
    )

    by_form_rows = []
    for form_key, label in (("fixed", "Fortran (Fixed-form)"), ("free", "Fortran (Free-form)"), ("c", "C")):
        form = stats["by_form"][form_key]
        form_code_lines = form["physical_lines"] - form["blank_lines"] - form["comment_lines"]
        by_form_rows.append((label, form["files"], f"{form['physical_lines']:,}", f"{form_code_lines:,}"))
    by_form_table = html_table(
        ["Form", "Files", "Physical lines", "Code lines"], by_form_rows, numeric_columns=(1, 2, 3), sortable=False
    )

    structure_table = html_table(
        ["Metric", "Count"],
        [
            ("Procedures (SUBROUTINE and FUNCTION)", len(procedures)),
            ("Fortran modules", stats["modules"]),
            ("COMMON declarations", stats["common_statements"]),
            ("Distinct named COMMON blocks", len(stats["common_names"])),
            ("Fortran INCLUDE statements", stats["includes"]),
        ],
        numeric_columns=(1,),
        sortable=False,
    )

    directive_rows = []
    for directive in (*PREPROCESSOR_DIRECTIVES, "other"):
        directive_rows.append(
            (directive, stats["directives"]["fortran"][directive], stats["directives"]["c"][directive])
        )
    for directive in FORTRAN_COMPILER_DIRECTIVES:
        directive_rows.append((f"{directive} (compiler directive)", stats["directives"]["fortran"][directive], 0))
    directive_table = html_table(
        ["Directive", "Fortran", "C"], directive_rows, numeric_columns=(1, 2), sortable=False
    )

    complexity_table = html_table(
        ["Metric", "Total", "Per procedure"],
        [
            ("Cyclomatic complexity", f"{total_cyclomatic:,}", f"{per_procedure_cyclomatic:.2f}"),
            ("Cognitive complexity", f"{total_cognitive:,}", f"{per_procedure_cognitive:.2f}"),
        ],
        numeric_columns=(1, 2),
        sortable=False,
    )

    top_cyclomatic_table = html_table(
        ["Procedure", "File", "Cyclomatic"],
        [(p["name"], p["file"], p["cyclomatic"]) for p in top_n(procedures, "cyclomatic")],
        numeric_columns=(2,),
    )
    top_cognitive_table = html_table(
        ["Procedure", "File", "Cognitive"],
        [(p["name"], p["file"], p["cognitive"]) for p in top_n(procedures, "cognitive")],
        numeric_columns=(2,),
    )
    full_table = html_table(
        ["Procedure", "File", "Cyclomatic", "Cognitive"],
        [
            (p["name"], p["file"], p["cyclomatic"], p["cognitive"])
            for p in sorted(procedures, key=lambda p: p["cyclomatic"], reverse=True)
        ],
        numeric_columns=(2, 3),
        table_id="full-procedure-table",
    )

    return (
        f"<{h}>{html.escape(title)}</{h}>"
        f"<p>Production source in <code>src/</code> is included: {fixed} fixed-form files, "
        f"{free} free-form files, and {c_files} C files. Tests, build directories, "
        "distributions, Python tooling, and generated files are excluded.</p>"
        f"<{hh}>Source Size</{hh}>{source_size_table}"
        f"<{hh}>Source Size by Form</{hh}>{by_form_table}"
        f"<{hh}>Program Structure</{hh}>{structure_table}"
        f"<{hh}>Preprocessor Directives</{hh}>"
        "<p>The two \"compiler directive\" rows are Fortran comments that the Intel/DEC "
        "convention (comment marker immediately followed by <code>DEC$</code> or "
        "<code>DIR$</code>, no space) turns into compiler directives rather than prose; "
        "they have no C equivalent, so their C column is always 0.</p>"
        f"{directive_table}"
        f"<{hh}>Complexity</{hh}>{complexity_table}<p>{html.escape(highest_note)}</p>"
        f"<{hh}>Top 10 Cyclomatic Complexity</{hh}>{top_cyclomatic_table}"
        f"<{hh}>Top 10 Cognitive Complexity</{hh}>{top_cognitive_table}"
        "<details><summary>Full procedure list "
        f"({len(procedures)} procedures)</summary>"
        '<input class="filter" data-target="full-procedure-table" type="text" '
        'placeholder="Filter by name or file...">'
        f"{full_table}</details>"
        '<p class="muted">These are lexical static-analysis metrics, calculated from physical source '
        "lines. Cyclomatic complexity starts each procedure at 1 and adds decisions for IF, ELSE IF, "
        "DO, SELECT CASE, CASE, WHERE, and FORALL. Cognitive complexity uses the same decisions with "
        "a nesting penalty. Because it is not a full Fortran parser, use the complexity values for "
        "comparative analysis; compiler-aware tooling is required for audit-grade results.</p>"
    )


def git_status_line():
    info = git_info()
    if info["sha"] == "unknown":
        return "Commit: unknown (not a git repository or git unavailable)."
    state = "with local modifications" if info["dirty"] else "clean working tree"
    return f"Commit {html.escape(info['sha'])} ({state})."


def render_html(stats):
    """Render the standalone MF2005 Code Statistics HTML report."""
    body = render_statistics_body(stats, heading_level=1, title="MF2005 Code Statistics")
    generated = datetime.now().strftime("%Y-%m-%d")
    return (
        "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>MF2005 Code Statistics</title><style>{TABLE_CSS}</style></head><body>"
        f'<p class="muted">Generated on {generated} from the current working tree. '
        f"{git_status_line()}</p>"
        f"{body}<script>{TABLE_JS}</script></body></html>"
    )


def main():
    parser = argparse.ArgumentParser(description="Compute MF2005 production source code statistics.")
    parser.add_argument(
        "--report",
        type=Path,
        default=ROOT / "doc" / "reports" / "code-statistics.html",
        help="HTML report path (default: doc/reports/code-statistics.html).",
    )
    args = parser.parse_args()

    stats = compute_statistics()
    report = args.report if args.report.is_absolute() else ROOT / args.report
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(render_html(stats), encoding="utf-8")
    print(f"Wrote {report}")


if __name__ == "__main__":
    main()
