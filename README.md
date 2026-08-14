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

The coverage task defaults to the `debug` build type, adds GCC coverage
instrumentation, runs the selected executable through the autotests, and
writes an HTML report for the Fortran and C sources. Use `--coverage` with
`test-solution` when testing a previously built coverage variant.
