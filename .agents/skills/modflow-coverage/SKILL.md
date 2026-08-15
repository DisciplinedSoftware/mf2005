---
name: modflow-coverage
description: "Use when measuring native Fortran/C coverage for MODFLOW-2005 with Pixi, Meson, and gcovr."
---

# MODFLOW-2005 Coverage Workflow

Use the repository root as the working directory:

```bash
cd /home/pluck/Documents/DisciplinedSoftware/Modernization/Code/mf2005
```

## Coverage model

Coverage is selected by the same variant dimensions as the builds:

- Precision: `single` or `double` (default: `single`)
- Meson build type: `release`, `debug`, `debugoptimized`, `plain`, `minsize`, or `custom` (default: `debug` for coverage)

Coverage instrumentation is enabled by `--coverage`. The generated gcovr HTML
report includes per-source details, decision coverage, call coverage, and
uncovered-code sorting. A JSON summary is generated beside the HTML report.

## Coverage execution

Build, run tests, and create an HTML native Fortran/C coverage report in one step:

```bash
pixi run coverage single
pixi run coverage double --buildtype debugoptimized
pixi run coverage double --buildtype release --output coverage-double.html
```

Coverage defaults to the `release` Meson build type and uses `gcovr`. The
report filters source files under `src/`. The generated HTML report, JSON
summary, and GCC `.gcda`/`.gcno` files are ignored by Git.

## Direct Meson fallback

If Pixi is unavailable, use the equivalent explicit Meson command:

```bash
meson setup --wipe . builds/build-debug-single \
  --prefix="$(pwd)/builds" --bindir=bin \
  --buildtype=debug -Ddouble=false -Db_coverage=true
meson compile -C builds/build-debug-single
meson install -C builds/build-debug-single
```

Prefer the Pixi task because it keeps build directory naming and executable selection consistent.

## Validation expectations

After changing coverage scripts or configuration:

1. Run `python -m py_compile scripts/coverage.py`.
2. Run `pixi run coverage --help`.
3. Build the requested coverage variant.
4. Confirm the HTML report is created and inspect the gcovr summary.
