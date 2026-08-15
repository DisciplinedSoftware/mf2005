---
name: modflow-build
description: "Use when building MODFLOW-2005 with Pixi and Meson. Supports GCC or Intel LLVM compilers, single or double precision, release/debug/debugoptimized/plain/minsize/custom build types, and the optional strict warning audit."
---

# MODFLOW-2005 Build Workflow

Use the repository root as the working directory:

```bash
cd /home/pluck/Documents/DisciplinedSoftware/Modernization/Code/mf2005
```

## Variant model

Every native build is selected by these independent dimensions:

- Compiler: GCC (default environment) or Intel LLVM (`ifx`/`icx`)
- Precision: `single` or `double` (default: `single`)
- Meson build type: `release`, `debug`, `debugoptimized`, `plain`, `minsize`, or `custom` (default: `release`)
- Warning audit: `false` (default) or `true` for strict compiler warnings and Fortran runtime checks

The single-precision executable is `mf2005`; double precision is `mf2005dbl`.
Use a distinct combination for each build. The task scripts create variant-specific build directories under a common `builds/` folder and install the executable to `builds/bin/` while avoiding collisions.

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

The Pixi build task does not currently expose `warning_audit`; use the direct Meson workflow below for an audit build.

## Direct Meson fallback

If Pixi is unavailable, use the equivalent explicit Meson command:

```bash
meson setup --wipe . builds/build-debug-single \
  --prefix="$(pwd)/builds" --bindir=bin \
  --buildtype=debug -Ddouble=false
meson compile -C builds/build-debug-single
meson install -C builds/build-debug-single
```

Build the strict warning-audit configuration:

```bash
meson setup --wipe . builds/build-warning-audit \
  --prefix="$(pwd)/builds" --bindir=bin \
  --buildtype=debug -Ddouble=false -Dwarning_audit=true
meson compile -C builds/build-warning-audit
```

The audit option can be combined with the existing precision and build-type dimensions. For example, a double-precision release audit uses `-Ddouble=true -Dwarning_audit=true --buildtype=release` and should use its own build directory.

Build with Intel oneAPI on Linux:

```bash
source /opt/intel/oneapi/setvars.sh
FC=ifx CC=icx meson setup --wipe . builds/build-warning-audit-intel-debug-single \
  --prefix="$(pwd)/builds" --bindir=bin \
  --buildtype=debug -Ddouble=false -Dwarning_audit=true
FC=ifx CC=icx meson compile -C builds/build-warning-audit-intel-debug-single
```

The Intel audit matrix uses the same six Meson build types and both precision modes as the GCC matrix. Use a distinct `builds/build-warning-audit-intel-<buildtype>-<precision>` directory for each combination. Intel diagnostics are recorded under `builds/build-logs/warning-audit-intel/`.

Prefer the Pixi tasks because they keep build directory naming and executable selection consistent.

## Validation expectations

After changing task scripts or build configuration:

1. Run `python -m py_compile scripts/build_solution.py`.
2. Run `pixi run build-solution --help`.
3. Build the requested variant.
