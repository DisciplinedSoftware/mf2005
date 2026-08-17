import argparse
import datetime
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# gcov miscounts hot lines in gwf2swr7.f (SSWR_LININT and the SWR reach-group
# loops), emitting hit counts in the billions. gcovr treats any count above its
# suspicious-hits threshold as a parse error and aborts with exit 64, which
# fails the whole coverage run over a known gcov defect:
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=68080
# Downgrade it to one warning per affected file so the report is still produced.
GCOV_PARSE_FLAGS = ("--gcov-ignore-parse-errors", "suspicious_hits.warn_once_per_file")


def run(command):
    subprocess.run(command, cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description="Build, test, and report MODFLOW-2005 C/Fortran coverage.")
    parser.add_argument("precision", nargs="?", choices=("single", "double"), default="single")
    parser.add_argument(
        "--buildtype",
        choices=("release", "debug", "debugoptimized", "plain", "minsize", "custom"),
        default="release",
        help="Meson build type (default: release).",
    )
    parser.add_argument("--output", default="coverage.html", help="HTML report path relative to the repository.")
    args = parser.parse_args()

    run([
        "python", "scripts/build_solution.py", args.precision,
        "--buildtype", args.buildtype, "--coverage",
    ])
    run([
        "python", "scripts/test_solution.py", args.precision,
        "--buildtype", args.buildtype, "--coverage",
    ])
    build_dir = ROOT / "builds" / f"build-{args.buildtype}-{args.precision}-coverage"
    report = Path(args.output)
    if not report.is_absolute():
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%Hh%Mm%S")
        report = ROOT / "doc" / "reports" / f"coverage_{timestamp}" 
    report.parent.mkdir(parents=True, exist_ok=True)
    summary = report.with_suffix(".json")
    run([
        "gcovr", "--root", ".", "--object-directory", str(build_dir),
        "--filter", "src/", "--html-details", str(report),
        "--decisions", "--calls", "--sort", "uncovered-percent",
        "--html-title", f"MF2005 Coverage - {args.buildtype} {args.precision}",
        "--json-summary", str(summary), "--print-summary",
        *GCOV_PARSE_FLAGS,
    ])
    print(f"Wrote {report}")
    print(f"Wrote {summary}")


if __name__ == "__main__":
    main()