import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(command):
    subprocess.run(command, cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description="Build, test, and report MODFLOW-2005 coverage.")
    parser.add_argument("precision", nargs="?", choices=("single", "double"), default="single")
    parser.add_argument(
        "--buildtype",
        choices=("release", "debug", "debugoptimized", "plain", "minsize", "custom"),
        default="debug",
        help="Meson build type (default: debug).",
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
    build_dir = ROOT / f"build-{args.buildtype}-{args.precision}-coverage"
    run([
        "gcovr", "--root", ".", "--object-directory", str(build_dir),
        "--filter", "src/", "--html-details", args.output,
    ])
    print(f"Wrote {ROOT / args.output}")


if __name__ == "__main__":
    main()