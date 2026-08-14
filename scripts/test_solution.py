import argparse
import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description="Run MODFLOW-2005 autotests.")
    parser.add_argument("precision", nargs="?", choices=("single", "double"), default="single")
    parser.add_argument(
        "--buildtype",
        choices=("release", "debug", "debugoptimized", "plain", "minsize", "custom"),
        default="release",
        help="Meson build type used to build the executable (default: release).",
    )
    parser.add_argument("--coverage", action="store_true", help="Use the coverage-instrumented build.")
    args, pytest_args = parser.parse_known_args()

    environment = os.environ.copy()
    coverage_name = "-coverage" if args.coverage else ""
    build_dir = ROOT / f"build-{args.buildtype}-{args.precision}{coverage_name}"
    executable_name = "mf2005dbl" if args.precision == "double" else "mf2005"
    executable = build_dir / "src" / executable_name
    if not executable.exists():
        raise SystemExit(f"Executable not found: {executable}. Build this variant first.")
    environment["MF2005_EXECUTABLE"] = str(executable)
    subprocess.run(["pytest", "-v", "./autotest", *pytest_args], cwd=ROOT, env=environment, check=True)


if __name__ == "__main__":
    main()