mf2005
======

[![mf2005 checks](https://github.com/MODFLOW-USGS/mf2005/actions/workflows/ci.yml/badge.svg)](https://github.com/MODFLOW-USGS/mf2005/actions/workflows/ci.yml)

Official MODFLOW-2005 version

## Build, test, and coverage

The Pixi tasks accept `single` or `double`; `single` is the default. Build
tasks also accept the Meson build types `release`, `debug`,
`debugoptimized`, `plain`, `minsize`, and `custom`.

```bash
pixi install
pixi run build-solution single
pixi run build-solution double
pixi run test-solution single
pixi run coverage single
pixi run coverage double --output coverage-double.html
pixi run build-solution double --buildtype debug
pixi run test-solution double --buildtype debug
pixi run coverage double --buildtype debugoptimized
```

The coverage task defaults to the `release` build type, adds GCC coverage
instrumentation, runs the selected executable through the autotests, and
writes a detailed HTML report plus a JSON summary for the Fortran and C
sources. The HTML report includes source details, decision coverage, call
coverage, and uncovered-code sorting. Use `--coverage` with `test-solution`
when testing a previously built coverage variant.

The code audit defaults to GCC across all build types and precisions. Select a
specific warning-audit configuration with `--build-type` and `--precision`, or
use `--compiler all` to include every compiler. Coverage is independent and
opt-in with `pixi run code-audit --coverage`; use
`--coverage-build-type` and `--coverage-precision` to select its configuration.
Coverage uses GCC/gcovr; audit-generated HTML coverage reports are written
alongside the audit HTML report.
