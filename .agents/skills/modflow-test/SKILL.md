---
name: modflow-test
description: "Use when running MODFLOW-2005 autotests against a built variant with Pixi and pytest."
---

# MODFLOW-2005 Test Workflow

Use the repository root as the working directory:

```bash
cd /home/pluck/Documents/DisciplinedSoftware/Modernization/Code/mf2005
```

## Variant model

Every test run targets a built executable selected by these independent dimensions:

- Precision: `single` or `double` (default: `single`)
- Meson build type: `release`, `debug`, `debugoptimized`, `plain`, `minsize`, or `custom` (default: `release`)
- Coverage: normal or instrumented (enabled by `--coverage`)

The single-precision executable is `mf2005`; double precision is `mf2005dbl`.
The task scripts create variant-specific build directories and run the selected executable from the matching build output, avoiding collisions in `bin/`.

## Test execution

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

## Validation expectations

After changing task scripts or test routing:

1. Run `python -m py_compile scripts/test_solution.py`.
2. Run `pixi run test-solution --help`.
3. Run `pixi run test-solution ... --collect-only -q` before the full suite when checking task routing.
4. Execute the full autotest suite when validating a real test run.
