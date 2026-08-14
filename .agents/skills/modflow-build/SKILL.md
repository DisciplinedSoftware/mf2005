---
name: modflow-build
description: "Use when building, testing, or measuring code coverage for MODFLOW-2005 with Pixi and Meson. Supports single or double precision, release/debug/debugoptimized/plain/minsize/custom build types, coverage instrumentation, autotests, and gcovr reports."
---

# MODFLOW-2005 Build Workflow

Use the repository root as the working directory:

```bash
cd /home/pluck/Documents/DisciplinedSoftware/Modernization/Code/mf2005
```

## Variant model

Every native build is selected by these independent dimensions:

- Precision: `single` or `double` (default: `single`)
- Meson build type: `release`, `debug`, `debugoptimized`, `plain`, `minsize`, or `custom` (default: `release` for builds and tests)
- Coverage: normal or instrumented (enabled by `--coverage`)

The single-precision executable is `mf2005`; double precision is `mf2005dbl`.
Use a distinct combination for each build. The task scripts create variant-specific build directories and tests run the executable from the selected build directory, avoiding collisions in `bin/`.

## Build

Build a normal release variant:

```bash
pixi run build-solution single
pixi run build-solution double
```

Build another Meson configuration:

```bash
pixi run build-solution single --buildtype debug
pixi run build-solution double --buildtype debugoptimized
pixi run build-solution single --buildtype plain
pixi run build-solution double --buildtype minsize
pixi run build-solution single --buildtype custom
```

The task runs Meson setup, compile, and install. It uses `-Ddouble=true` only for the double-precision variant.

## Tests

Run the full MODFLOW-2005 autotest suite against a built variant:

```bash
pixi run test-solution single
pixi run test-solution double --buildtype debug
```

For a coverage-instrumented build, pass `--coverage` to select the matching executable:

```bash
pixi run test-solution single --buildtype debug --coverage
```

The test task uses `pytest -v ./autotest`. Add normal pytest arguments after the task options, for example:

```bash
pixi run test-solution single --buildtype debug -k sfr
pixi run test-solution double --buildtype release --collect-only -q
```

If the selected executable has not been built, build the same precision, build type, and coverage combination first. The task reports the expected executable path when it is missing.

## Coverage

Build, run tests, and create an HTML native Fortran/C coverage report in one step:

```bash
pixi run coverage single
pixi run coverage double --buildtype debugoptimized
pixi run coverage double --buildtype release --output coverage-double.html
```

Coverage defaults to the `debug` Meson build type and uses `gcovr`. The report filters source files under `src/`. The generated HTML report and GCC `.gcda`/`.gcno` files are ignored by Git.

## Direct Meson fallback

If Pixi is unavailable, use the equivalent explicit Meson command:

```bash
meson setup --wipe . build-debug-single \
  --prefix="$(pwd)" --bindir=bin \
  --buildtype=debug -Ddouble=false -Db_coverage=true
meson compile -C build-debug-single
meson install -C build-debug-single
```

Prefer the Pixi tasks because they keep build directory naming and executable selection consistent.

## Validation expectations

After changing task scripts or build configuration:

1. Run `python -m py_compile scripts/build_solution.py scripts/test_solution.py scripts/coverage.py`.
2. Run the relevant task with `--help`.
3. Build the requested variant.
4. Run `pixi run test-solution ... --collect-only -q` before the full suite when checking task routing.
5. For coverage, confirm the HTML report is created and inspect the gcovr summary.
