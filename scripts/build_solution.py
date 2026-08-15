import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(command):
    subprocess.run(command, cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description="Build MODFLOW-2005.")
    parser.add_argument("precision", nargs="?", choices=("single", "double"), default="single")
    parser.add_argument(
        "--buildtype",
        choices=("release", "debug", "debugoptimized", "plain", "minsize", "custom"),
        default="release",
        help="Meson build type (default: release).",
    )
    parser.add_argument("--coverage", action="store_true", help="Enable GCC coverage instrumentation.")
    args = parser.parse_args()

    coverage_name = "-coverage" if args.coverage else ""
    build_dir = ROOT / "builds" / f"build-{args.buildtype}-{args.precision}{coverage_name}"
    double_option = "true" if args.precision == "double" else "false"
    executable = ROOT / "builds" / "bin" / ("mf2005dbl" if args.precision == "double" else "mf2005")

    setup = [
        "meson", "setup", "--wipe", ".", str(build_dir),
        f"--prefix={ROOT / 'builds'}", "--bindir=bin", f"--buildtype={args.buildtype}",
        f"-Ddouble={double_option}",
    ]
    if args.coverage:
        setup.append("-Db_coverage=true")

    run(setup)
    run(["meson", "compile", "-C", str(build_dir)])
    run(["meson", "install", "-C", str(build_dir)])
    print(f"Built {executable}")


if __name__ == "__main__":
    main()