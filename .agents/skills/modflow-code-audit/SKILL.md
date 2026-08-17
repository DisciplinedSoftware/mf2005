---
name: modflow-code-audit
description: "Use when auditing MODFLOW-2005 source with all warning checks across GCC or Intel LLVM, both precision modes, and all Meson build types."
---

# MODFLOW-2005 Code Audit

This workflow treats the compiler as the code auditor. It configures Meson with
`-Dwarning_audit=true`, builds every requested matrix variant, preserves the
compiler output, and generates a self-contained HTML report.

## Audit matrix

The script supports these independent dimensions:

- Compiler: GCC or Intel LLVM (`ifx`/`icx`)
- Precision: single or double
- Build type: `release`, `debug`, `debugoptimized`, `plain`, `minsize`, or `custom`

The default command audits GCC across every build type and precision. Use
`--compiler all` to audit every compiler; `--build-type` and `--precision`
select the independent audit dimensions. Coverage is opt-in and independent:
pass `--coverage` to build, test, and report coverage for the configurations
selected by `--coverage-compiler`, `--coverage-build-type`, and
`--coverage-precision`. Coverage uses GCC/gcovr.

## Run the audit

GCC, all build types and precisions:

```bash
pixi run code-audit --compiler gcc
```

One warning-audit variant explicitly:

```bash
pixi run code-audit --compiler gcc --build-type release --precision single
```

Intel only:

```bash
source /opt/intel/oneapi/setvars.sh
pixi run code-audit --compiler intel
```

All available compilers:

```bash
source /opt/intel/oneapi/setvars.sh
pixi run code-audit --compiler all
```

One coverage configuration:

```bash
pixi run code-audit --coverage --coverage-build-type release --coverage-precision single
```

Coverage for every GCC build type and precision:

```bash
pixi run code-audit --coverage
```

The Intel environment must be initialized before running the script because
`ifx` and `icx` are not normally on `PATH`.

## Outputs

Raw logs are written to a unique run directory under `builds/build-logs/code-audit/`
and are not committed. The HTML report is written to
`doc/reports/code-audit-report.html` by default. When `--coverage` is enabled
without an explicit `--report`, it is written to
`doc/reports/coverage_{datetime}/coverage_{datetime}.html`, where `{datetime}` uses the format
`%Y-%m-%d_%Hh%Mm%S` (for example,
`doc/reports/coverage_2026-08-16_14h05m09/coverage_2026-08-16_14h05m09.html`). The
Each variant coverage report is stored in its own
`<compiler>-<configuration>-<precision>` subfolder under the timestamped
folder, for example
`doc/reports/coverage_2026-08-16_14h05m09/gcc-release-single/coverage-gcc-release-single.html`.
An explicit `--report` path always takes precedence. The report is a
self-contained modernization status snapshot:

- Embedded dynamic source statistics (source size, program structure, complexity
  summary, top 10 cyclomatic/cognitive complexity procedures, and a
  sortable/filterable collapsible full procedure list)
- A pass/fail matrix by build type and compiler/precision
- A warning-category count table (obsolescent, implicit interface, conversion,
  real comparison, unused, tabs, C sign conversion, C float conversion)
- The warning flags enabled per compiler
- A representative log snippet and source context for each category with
  occurrences
- An overall assessment paragraph

Use `--output` to choose a stable raw-log directory and `--report` to choose a
different HTML report path. Do not run two audits against the same explicit
output directory at the same time.

The script creates isolated `builds/build-code-audit-*` directories and does not edit
source files. A nonzero exit code means at least one requested variant failed.

Run the script directly when Pixi is unavailable:

```bash
python scripts/audit_code.py --compiler gcc
```

## Interpretation

Warning counts are occurrences in compiler logs, not unique source locations.
Use the file and line noted in each representative snippet to inspect the
source path reported by the
compiler. Compiler diagnostic names differ, so compare warning categories by
message meaning rather than expecting GCC `[-W...]` identifiers from Intel.