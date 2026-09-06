# Undefined behavior report

Generated 2026-09-05T20:06:48-04:00 at commit aa43e20 for mf2005.

## Summary

| Metric | Count |
| --- | ---: |
| Source files | 54 |
| Program units analyzed | 793 |
| Program units skipped | 0 |
| Findings (all detectors) | 1,538 |
| — Uninitialized reads | 1,507 |
| — Argument aliasing and constant modification | 30 |
| — Interface mismatches | 0 |
| — Out-of-bounds subscripts (constant) | 0 |
| — Storage association (COMMON layout) | 0 |
| — Pointer association misuse | 0 |
| — FORMAT descriptors vs data-transfer items | 1 |

## Detectors

### Uninitialized reads

Definite assignment analysis: forward MUST/MAY dataflow over each unit's control-flow graph flags every read a path can reach before the variable is assigned.

- **always** (0) — no path defines the variable before this read
- **conditional** (321) — some paths define it, others reach the read without
- **loop-guarded** (1163) — every definition sits inside a possibly zero-trip loop
- **call-assumed** (22) — only 'definition' is an argument to a call with unknown intent
- **result-unset** (1) — function result possibly never assigned before RETURN

### Argument aliasing and constant modification

Cross-checks every call site against the callee's inferred argument usage: overlapping actuals where the callee writes, module variables passed into procedures that also assign them, and constants bound to written dummies.

- **aliasing** (22) — two actuals share storage and the callee writes one of them
- **aliasing-possible** (0) — two actuals share storage; the callee only passes them onward to calls with unknown intent
- **global-aliasing** (8) — an actual is a module variable the callee also writes by USE association
- **constant-modification** (0) — a literal or PARAMETER actual is written by the callee
- **constant-modification-possible** (0) — a literal or PARAMETER actual is passed onward by the callee to calls with unknown intent

### Interface mismatches

Checks every call site against the called procedure's definition elsewhere in the tree: argument counts, type classes, precision, and rank.

- **argument-count** (0) — call passes a different number of arguments than the procedure declares
- **argument-type** (0) — actual and dummy are of incompatible type classes
- **argument-precision** (0) — REAL actual bound to DOUBLE PRECISION dummy or vice versa (mismatched except under promoting flags such as -fdefault-real-8)
- **argument-rank** (0) — a scalar actual is bound to an array dummy, or a whole array to a scalar dummy
- **argument-rank-character** (0) — a CHARACTER scalar is bound to a CHARACTER array dummy: legal sequence association only while the actual is at least as long as the dummy elements the callee reaches

### Out-of-bounds subscripts (constant)

Every compile-time-constant subscript is checked against the declared constant bounds of local and COMMON arrays.

- **constant-subscript** (0) — a constant subscript falls outside the declared constant bounds

### Storage association (COMMON layout)

Compares every named COMMON block's layout across the program units that declare it; differing layouts alias storage under different names and types.

- **common-layout** (0) — a named COMMON block has different layouts across program units

### Pointer association misuse

Per-unit dataflow over ALLOCATE/DEALLOCATE/NULLIFY/pointer-assignment: flags references reachable while the variable may be deallocated or disassociated.

- **use-after-dealloc** (0) — a path reaches this reference after DEALLOCATE/NULLIFY without re-association

### FORMAT descriptors vs data-transfer items

Every WRITE/READ/PRINT with a FORMAT label or literal format is walked in format-control order (repeats, groups, unlimited groups, reversion) and each data edit descriptor is checked against the type of the item it transfers.

- **format-type** (1) — a data edit descriptor meets an item whose type it cannot transfer
- **format-count** (0) — items remain when the format has no data edit descriptors to consume them (endless format reversion)

## Findings

### de47.f90 (2)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 489 | de47ap | uninitialized | loop-guarded | ieq | defined at 426, 436, 444, 452, 460, 468, 476 | `L = IEQ(M)` |
| 493 | de47ap | uninitialized | loop-guarded | cnd | defined at 435, 443, 451, 459, 467, 475 | `AU(N, IR) = CND(M)` |

### gwf2bas7.f90 (1)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 2077 | sgwf2bas7l | uninitialized | conditional | layer | defined at 2061 | `WRITE(IOUT, 112) LABEL, (LAYER(M), M = 1, NSET)` |

### gwf2bcf7.f90 (45)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 384 | gwf2bcf7fm | uninitialized | conditional | tled | defined at 358 | `RHO = SC1(J, I, K) * TLED` |
| 399 | gwf2bcf7fm | uninitialized | conditional | tled | defined at 358 | `RHO2 = SC2(J, I, KT) * TLED` |
| 400 | gwf2bcf7fm | uninitialized | conditional | tled | defined at 358 | `RHO1 = SC1(J, I, K) * TLED` |
| 932 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 908, 924, 967, 1009, 1010 | `DO 310 K = K1, K2` |
| 932 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 909, 925, 968, 1011, 1024 | `DO 310 K = K1, K2` |
| 933 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 910, 926, 969, 970, 1012 | `DO 310 I = I1, I2` |
| 933 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 911, 927, 971, 982, 1013 | `DO 310 I = I1, I2` |
| 934 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 912, 928, 929, 972, 1014 | `DO 310 J = J1, J2` |
| 934 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 913, 930, 939, 973, 1015 | `DO 310 J = J1, J2` |
| 939 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 913, 930, 939, 973, 1015 | `IF (J2 .EQ. NCOL) J2 = J2 - 1` |
| 940 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 908, 924, 967, 1009, 1010 | `DO 400 K = K1, K2` |
| 940 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 909, 925, 968, 1011, 1024 | `DO 400 K = K1, K2` |
| 941 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 910, 926, 969, 970, 1012 | `DO 400 I = I1, I2` |
| 941 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 911, 927, 971, 982, 1013 | `DO 400 I = I1, I2` |
| 942 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 912, 928, 929, 972, 1014 | `DO 400 J = J1, J2` |
| 942 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 913, 930, 939, 973, 1015 | `DO 400 J = J1, J2` |
| 975 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 908, 924, 967, 1009, 1010 | `DO 410 K = K1, K2` |
| 975 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 909, 925, 968, 1011, 1024 | `DO 410 K = K1, K2` |
| 976 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 910, 926, 969, 970, 1012 | `DO 410 I = I1, I2` |
| 976 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 911, 927, 971, 982, 1013 | `DO 410 I = I1, I2` |
| 977 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 912, 928, 929, 972, 1014 | `DO 410 J = J1, J2` |
| 977 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 913, 930, 939, 973, 1015 | `DO 410 J = J1, J2` |
| 982 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 911, 927, 971, 982, 1013 | `IF (I2 .EQ. NROW) I2 = I2 - 1` |
| 983 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 908, 924, 967, 1009, 1010 | `DO 500 K = K1, K2` |
| 983 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 909, 925, 968, 1011, 1024 | `DO 500 K = K1, K2` |
| 984 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 910, 926, 969, 970, 1012 | `DO 500 I = I1, I2` |
| 984 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 911, 927, 971, 982, 1013 | `DO 500 I = I1, I2` |
| 985 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 912, 928, 929, 972, 1014 | `DO 500 J = J1, J2` |
| 985 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 913, 930, 939, 973, 1015 | `DO 500 J = J1, J2` |
| 1017 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 908, 924, 967, 1009, 1010 | `DO 510 K = K1, K2` |
| 1017 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 909, 925, 968, 1011, 1024 | `DO 510 K = K1, K2` |
| 1018 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 910, 926, 969, 970, 1012 | `DO 510 I = I1, I2` |
| 1018 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 911, 927, 971, 982, 1013 | `DO 510 I = I1, I2` |
| 1019 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 912, 928, 929, 972, 1014 | `DO 510 J = J1, J2` |
| 1019 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 913, 930, 939, 973, 1015 | `DO 510 J = J1, J2` |
| 1024 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 909, 925, 968, 1011, 1024 | `IF (K2 .EQ. NLAY) K2 = K2 - 1` |
| 1025 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 909, 925, 968, 1011, 1024 | `DO 600 K = 1, K2` |
| 1026 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 908, 924, 967, 1009, 1010 | `IF (K .LT. K1) GO TO 600` |
| 1027 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 910, 926, 969, 970, 1012 | `DO 590 I = I1, I2` |
| 1027 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 911, 927, 971, 982, 1013 | `DO 590 I = I1, I2` |
| 1028 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 912, 928, 929, 972, 1014 | `DO 590 J = J1, J2` |
| 1028 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 913, 930, 939, 973, 1015 | `DO 590 J = J1, J2` |
| 1279 | sgwf2bcf7h | uninitialized | loop-guarded | acnvrt | defined at 1210, 1253 | `WRITE(IOUT, 18) (ACNVRT(L), ICNVRT(L), JCNVRT(L), L = 1, NCNVRT)` |
| 1279 | sgwf2bcf7h | uninitialized | loop-guarded | icnvrt | defined at 1208, 1251 | `WRITE(IOUT, 18) (ACNVRT(L), ICNVRT(L), JCNVRT(L), L = 1, NCNVRT)` |
| 1279 | sgwf2bcf7h | uninitialized | loop-guarded | jcnvrt | defined at 1209, 1252 | `WRITE(IOUT, 18) (ACNVRT(L), ICNVRT(L), JCNVRT(L), L = 1, NCNVRT)` |

### gwf2drt7.f90 (10)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 470 | gwf2drt7bd | uninitialized | loop-guarded | icr | defined at 448, 504 | `IF (ILR .NE. 0 .AND. IBOUND(ICR, IRR, ILR) .GT. 0) THEN` |
| 470 | gwf2drt7bd | uninitialized | loop-guarded | irr | defined at 447, 504 | `IF (ILR .NE. 0 .AND. IBOUND(ICR, IRR, ILR) .GT. 0) THEN` |
| 487 | gwf2drt7bd | uninitialized | loop-guarded | icr | defined at 448, 504 | `WRITE(IOUT, 550) L, ILR, IRR, ICR, QIN` |
| 487 | gwf2drt7bd | uninitialized | loop-guarded | irr | defined at 447, 504 | `WRITE(IOUT, 550) L, ILR, IRR, ICR, QIN` |
| 487 | gwf2drt7bd | uninitialized | loop-guarded | qin | defined at 444, 473, 504 | `WRITE(IOUT, 550) L, ILR, IRR, ICR, QIN` |
| 496 | gwf2drt7bd | uninitialized | loop-guarded | icr | defined at 448, 504 | `BUFF(ICR, IRR, ILR) = BUFF(ICR, IRR, ILR) + QIN` |
| 496 | gwf2drt7bd | uninitialized | loop-guarded | irr | defined at 447, 504 | `BUFF(ICR, IRR, ILR) = BUFF(ICR, IRR, ILR) + QIN` |
| 496 | gwf2drt7bd | uninitialized | loop-guarded | qin | defined at 444, 473, 504 | `BUFF(ICR, IRR, ILR) = BUFF(ICR, IRR, ILR) + QIN` |
| 509 | gwf2drt7bd | uninitialized | loop-guarded | qin | defined at 444, 473, 504 | `DRTF(NDRTVL - 1, L) = QIN` |
| 998 | sgwf2drt7ls | uninitialized | loop-guarded | nlst | defined at 915, 920 | `DO 140 II = NDRTCL - NLST + 1, NDRTCL` |

### gwf2ets7.f90 (11)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 276 | gwf2ets7rp | uninitialized | conditional | iniets | defined at 199, 201, 206, 208 | `IF (INIETS .LT. 0) THEN` |
| 288 | gwf2ets7rp | uninitialized | conditional | insgdf | defined at 199, 201 | `IF (INSGDF .LT. 0) THEN` |
| 364 | gwf2ets7fm | uninitialized | loop-guarded | il | defined at 347, 350, 354, 357 | `IF (IBOUND(IC, IR, IL) .GT. 0) THEN` |
| 368 | gwf2ets7fm | uninitialized | loop-guarded | il | defined at 347, 350, 354, 357 | `HH = HNEW(IC, IR, IL)` |
| 374 | gwf2ets7fm | uninitialized | loop-guarded | il | defined at 347, 350, 354, 357 | `RHS(IC, IR, IL) = RHS(IC, IR, IL) + C` |
| 413 | gwf2ets7fm | uninitialized | loop-guarded | petm2 | defined at 396, 399 | `THCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |
| 413 | gwf2ets7fm | uninitialized | loop-guarded | pxdp2 | defined at 395, 398 | `THCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |
| 421 | gwf2ets7fm | uninitialized | loop-guarded | il | defined at 347, 350, 354, 357 | `RHS(IC, IR, IL) = RHS(IC, IR, IL) + TRHS` |
| 422 | gwf2ets7fm | uninitialized | loop-guarded | il | defined at 347, 350, 354, 357 | `HCOF(IC, IR, IL) = HCOF(IC, IR, IL) + THCOF` |
| 564 | gwf2ets7bd | uninitialized | loop-guarded | petm2 | defined at 547, 550 | `HHCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |
| 564 | gwf2ets7bd | uninitialized | loop-guarded | pxdp2 | defined at 546, 549 | `HHCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |

### gwf2evt7.f90 (1)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 231 | gwf2evt7rp | uninitialized | conditional | inievt | defined at 153, 155 | `IF (INIEVT .LT. 0) THEN` |

### gwf2fhb7.f90 (3)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 304 | gwf2fhb7ar | uninitialized | conditional | nd | defined at 237, 274, 331 | `WRITE(IOUT, 54) (DSH1, M = 1, ND)` |
| 373 | gwf2fhb7ar | uninitialized | conditional | nd | defined at 237, 274, 331 | `WRITE(IOUT, 54) (DSH1, M = 1, ND)` |
| 737 | gwf2fhb7bd | format | format-type | kper | item 2 KPER (integer) against A4: non-standard; gfortran transfers the raw bytes; item 3 KSTP (integer) against A4: non-standard; gfortran transfers the raw bytes; item 4 L (integer) against A4: non-standard; gfortran transfers the raw bytes; item 8 Q (real) against I3: gfortran aborts the transfer at runtime | `WRITE(IOUT, 900) TEXT, KPER, KSTP, L, IL, IR, IC, Q` |

### gwf2gag7.f90 (4)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 1010 | sgwf2gag7so | uninitialized | loop-guarded | pmxdvrt | defined at 968, 969, 970 | `WRITE(IG3, 270) GAGETM, STRM(15, II), PMXDVRT, STRM(10, II), UPSTRFLW` |
| 1010 | sgwf2gag7so | uninitialized | loop-guarded | upstrflw | defined at 967 | `WRITE(IG3, 270) GAGETM, STRM(15, II), PMXDVRT, STRM(10, II), UPSTRFLW` |
| 1082 | sgwf2gag7so | uninitialized | loop-guarded | pmxdvrt | defined at 968, 969, 970 | `WRITE(IG3, LFRMAT) GAGETM, STRM(15, II), PMXDVRT, STRM(10, II), UPSTRFLW, (COUT(II, ISOL), CLOAD(...` |
| 1082 | sgwf2gag7so | uninitialized | loop-guarded | upstrflw | defined at 967 | `WRITE(IG3, LFRMAT) GAGETM, STRM(15, II), PMXDVRT, STRM(10, II), UPSTRFLW, (COUT(II, ISOL), CLOAD(...` |

### gwf2huf7.f90 (57)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 582 | gwf2huf7ar | uninitialized | conditional | iflg | defined at 551, 558, 559, 560, 562, 563, 567, 569, 571, 573, 575 | `IHGUFLG(I, NU) = IFLG(I)` |
| 588 | gwf2huf7ar | uninitialized | conditional | iflg | defined at 551, 558, 559, 560, 562, 563, 567, 569, 571, 573, 575 | `IHGUFLG(I, IU) = IFLG(I)` |
| 3003 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2979, 2995, 3046, 3097, 3098 | `DO 310 K = K1, K2` |
| 3003 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2980, 2996, 3047, 3099, 3112 | `DO 310 K = K1, K2` |
| 3004 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2981, 2997, 3048, 3049, 3100 | `DO 310 I = I1, I2` |
| 3004 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2982, 2998, 3050, 3061, 3101 | `DO 310 I = I1, I2` |
| 3005 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2983, 2999, 3000, 3051, 3102 | `DO 310 J = J1, J2` |
| 3005 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2984, 3001, 3010, 3052, 3103 | `DO 310 J = J1, J2` |
| 3010 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2984, 3001, 3010, 3052, 3103 | `IF (J2 .EQ. NCOL) J2 = J2 - 1` |
| 3011 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2979, 2995, 3046, 3097, 3098 | `DO 400 K = K1, K2` |
| 3011 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2980, 2996, 3047, 3099, 3112 | `DO 400 K = K1, K2` |
| 3012 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2981, 2997, 3048, 3049, 3100 | `DO 400 I = I1, I2` |
| 3012 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2982, 2998, 3050, 3061, 3101 | `DO 400 I = I1, I2` |
| 3013 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2983, 2999, 3000, 3051, 3102 | `DO 400 J = J1, J2` |
| 3013 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2984, 3001, 3010, 3052, 3103 | `DO 400 J = J1, J2` |
| 3054 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2979, 2995, 3046, 3097, 3098 | `DO 410 K = K1, K2` |
| 3054 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2980, 2996, 3047, 3099, 3112 | `DO 410 K = K1, K2` |
| 3055 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2981, 2997, 3048, 3049, 3100 | `DO 410 I = I1, I2` |
| 3055 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2982, 2998, 3050, 3061, 3101 | `DO 410 I = I1, I2` |
| 3056 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2983, 2999, 3000, 3051, 3102 | `DO 410 J = J1, J2` |
| 3056 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2984, 3001, 3010, 3052, 3103 | `DO 410 J = J1, J2` |
| 3061 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2982, 2998, 3050, 3061, 3101 | `IF (I2 .EQ. NROW) I2 = I2 - 1` |
| 3062 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2979, 2995, 3046, 3097, 3098 | `DO 500 K = K1, K2` |
| 3062 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2980, 2996, 3047, 3099, 3112 | `DO 500 K = K1, K2` |
| 3063 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2981, 2997, 3048, 3049, 3100 | `DO 500 I = I1, I2` |
| 3063 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2982, 2998, 3050, 3061, 3101 | `DO 500 I = I1, I2` |
| 3064 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2983, 2999, 3000, 3051, 3102 | `DO 500 J = J1, J2` |
| 3064 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2984, 3001, 3010, 3052, 3103 | `DO 500 J = J1, J2` |
| 3105 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2979, 2995, 3046, 3097, 3098 | `DO 510 K = K1, K2` |
| 3105 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2980, 2996, 3047, 3099, 3112 | `DO 510 K = K1, K2` |
| 3106 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2981, 2997, 3048, 3049, 3100 | `DO 510 I = I1, I2` |
| 3106 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2982, 2998, 3050, 3061, 3101 | `DO 510 I = I1, I2` |
| 3107 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2983, 2999, 3000, 3051, 3102 | `DO 510 J = J1, J2` |
| 3107 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2984, 3001, 3010, 3052, 3103 | `DO 510 J = J1, J2` |
| 3112 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2980, 2996, 3047, 3099, 3112 | `IF (K2 .EQ. NLAY) K2 = K2 - 1` |
| 3113 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2980, 2996, 3047, 3099, 3112 | `DO 600 K = 1, K2` |
| 3114 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2979, 2995, 3046, 3097, 3098 | `IF (K .LT. K1) GO TO 600` |
| 3115 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2981, 2997, 3048, 3049, 3100 | `DO 590 I = I1, I2` |
| 3115 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2982, 2998, 3050, 3061, 3101 | `DO 590 I = I1, I2` |
| 3116 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2983, 2999, 3000, 3051, 3102 | `DO 590 J = J1, J2` |
| 3116 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2984, 3001, 3010, 3052, 3103 | `DO 590 J = J1, J2` |
| 3273 | gwf2huf7bdch | uninitialized | call-assumed | dfl | defined at 3257 | `CHCH1 = - DFL` |
| 3293 | gwf2huf7bdch | uninitialized | call-assumed | dfr | defined at 3257 | `CHCH2 = DFR` |
| 3311 | gwf2huf7bdch | uninitialized | call-assumed | dft | defined at 3257 | `CHCH3 = - DFT` |
| 3329 | gwf2huf7bdch | uninitialized | call-assumed | dfb | defined at 3257 | `CHCH4 = DFB` |
| 3646 | sgwf2huf7flot | uninitialized | loop-guarded | hxr | defined at 3640 | `DHXR = H0 - HXR` |
| 3658 | sgwf2huf7flot | uninitialized | loop-guarded | hyb | defined at 3652 | `DHYB = H0 - HYB` |
| 4310 | sgwf2huf7c | uninitialized | loop-guarded | tr0 | defined at 4306 | `IF (TR0 .EQ. 0.0 .AND. TR1 .EQ. 0.0) THEN` |
| 4313 | sgwf2huf7c | uninitialized | loop-guarded | tr0 | defined at 4306 | `CRL = 2. * TR1 * TR0 * DELC(I) / (TR1 * DELR(J + 1) + TR0 * DELR(J))` |
| 4317 | sgwf2huf7c | uninitialized | loop-guarded | tr0 | defined at 4306 | `IF (TR0 .EQ. 0.0 .AND. TR1 .EQ. 0.0) THEN` |
| 4320 | sgwf2huf7c | uninitialized | loop-guarded | tr0 | defined at 4306 | `CRR = 2. * TR1 * TR0 * DELC(I) / (TR1 * DELR(J - 1) + TR0 * DELR(J))` |
| 4324 | sgwf2huf7c | uninitialized | loop-guarded | tc0 | defined at 4307 | `IF (TC0 .EQ. 0.0 .AND. TC1 .EQ. 0.0) THEN` |
| 4327 | sgwf2huf7c | uninitialized | loop-guarded | tc0 | defined at 4307 | `CCT = 2. * TC1 * TC0 * DELR(J) / (TC1 * DELC(I + 1) + TC0 * DELC(I))` |
| 4331 | sgwf2huf7c | uninitialized | loop-guarded | tc0 | defined at 4307 | `IF (TC0 .EQ. 0.0 .AND. TC1 .EQ. 0.0) THEN` |
| 4334 | sgwf2huf7c | uninitialized | loop-guarded | tc0 | defined at 4307 | `CCB = 2. * TC1 * TC0 * DELR(J) / (TC1 * DELC(I - 1) + TC0 * DELC(I))` |
| 4393 | sgwf2huf7ind | uninitialized | conditional | istack | defined at 4438, 4439, 4442, 4443 | `ir = istack(jstack)` |
| 4394 | sgwf2huf7ind | uninitialized | conditional | istack | defined at 4438, 4439, 4442, 4443 | `l = istack(jstack - 1)` |

### gwf2hydmod7.f90 (25)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 241 | gwf2hyd7bas7ar | uninitialized | conditional | hydbaslbl | defined at 250 | `WRITE(HYDBASLBL(1 : 2), FMT = '(A2)') HYDBASARR(NHYDBAS)` |
| 244 | gwf2hyd7bas7ar | uninitialized | conditional | hydbaslbl | defined at 250 | `WRITE(HYDBASLBL(3 : 3), FMT = '(A1)') LINE(ISTART : ISTOP)` |
| 249 | gwf2hyd7bas7ar | uninitialized | conditional | hydbaslbl | defined at 250 | `WRITE(HYDBASLBL(4 : 6), FMT = '(I3.3)') KLAY` |
| 330 | gwf2hyd7bas7ar | uninitialized | call-assumed | w1 | defined at 299 | `HYDBASSTRT(NHYDBAS) = H1 * W1 + H2 * W2 + H3 * W3 + H4 * W4` |
| 330 | gwf2hyd7bas7ar | uninitialized | call-assumed | w2 | defined at 299 | `HYDBASSTRT(NHYDBAS) = H1 * W1 + H2 * W2 + H3 * W3 + H4 * W4` |
| 330 | gwf2hyd7bas7ar | uninitialized | call-assumed | w3 | defined at 299 | `HYDBASSTRT(NHYDBAS) = H1 * W1 + H2 * W2 + H3 * W3 + H4 * W4` |
| 330 | gwf2hyd7bas7ar | uninitialized | call-assumed | w4 | defined at 299 | `HYDBASSTRT(NHYDBAS) = H1 * W1 + H2 * W2 + H3 * W3 + H4 * W4` |
| 439 | gwf2hyd7ibs7ar | uninitialized | conditional | hydibslbl | defined at 448 | `WRITE(HYDIBSLBL(1 : 2), FMT = '(A2)') ARR` |
| 442 | gwf2hyd7ibs7ar | uninitialized | conditional | hydibslbl | defined at 448 | `WRITE(HYDIBSLBL(3 : 3), FMT = '(A1)') INTYP` |
| 447 | gwf2hyd7ibs7ar | uninitialized | conditional | hydibslbl | defined at 448 | `WRITE(HYDIBSLBL(4 : 6), FMT = '(I3.3)') KLAY` |
| 627 | gwf2hyd7sub7ar | uninitialized | conditional | hydsublbl | defined at 636 | `WRITE(HYDSUBLBL(1 : 2), FMT = '(A2)') ARR` |
| 630 | gwf2hyd7sub7ar | uninitialized | conditional | hydsublbl | defined at 636 | `WRITE(HYDSUBLBL(3 : 3), FMT = '(A1)') INTYP` |
| 635 | gwf2hyd7sub7ar | uninitialized | conditional | hydsublbl | defined at 636 | `WRITE(HYDSUBLBL(4 : 6), FMT = '(I3.3)') KLAY` |
| 831 | gwf2hyd7str7rp | uninitialized | conditional | hydstrlbl | defined at 840 | `WRITE(HYDSTRLBL(1 : 2), FMT = '(A2)') HYDSTRARR(NUMSTR)` |
| 838 | gwf2hyd7str7rp | uninitialized | conditional | hydstrlbl | defined at 840 | `WRITE(HYDSTRLBL(3 : 5), FMT = '(I3.3)') INT(XL)` |
| 839 | gwf2hyd7str7rp | uninitialized | conditional | hydstrlbl | defined at 840 | `WRITE(HYDSTRLBL(6 : 8), FMT = '(I3.3)') INT(YL)` |
| 1002 | gwf2hyd7sfr7rp | uninitialized | conditional | hydsfrlbl | defined at 1011 | `WRITE(HYDSFRLBL(1 : 2), FMT = '(A2)') HYDSFRARR(NUMSFR)` |
| 1009 | gwf2hyd7sfr7rp | uninitialized | conditional | hydsfrlbl | defined at 1011 | `WRITE(HYDSFRLBL(3 : 5), FMT = '(I3.3)') INT(XL)` |
| 1010 | gwf2hyd7sfr7rp | uninitialized | conditional | hydsfrlbl | defined at 1011 | `WRITE(HYDSFRLBL(6 : 8), FMT = '(I3.3)') INT(YL)` |
| 1122 | gwf2hyd7bas7se | uninitialized | loop-guarded | ibfact | defined at 1111, 1116 | `IF (IBHYDBAS(N) .AND. IBFACT .EQ. 0) THEN` |
| 1130 | gwf2hyd7bas7se | uninitialized | loop-guarded | ibfact | defined at 1111, 1116 | `IF (IBHYDBAS(N) .AND. IBFACT .EQ. 0) THEN` |
| 1201 | gwf2hyd7ibs7se | uninitialized | loop-guarded | ibfact | defined at 1190, 1195 | `IF (IBHYDIBS(N) .AND. IBFACT .EQ. 0) THEN` |
| 1217 | gwf2hyd7ibs7se | uninitialized | loop-guarded | ibfact | defined at 1190, 1195 | `IF (IBHYDIBS(N) .AND. IBFACT .EQ. 0) THEN` |
| 1317 | gwf2hyd7sub7se | uninitialized | loop-guarded | ibfact | defined at 1306, 1311 | `IF (IBHYDSUB(N) .AND. IBFACT .EQ. 0) THEN` |
| 1337 | gwf2hyd7sub7se | uninitialized | loop-guarded | ibfact | defined at 1306, 1311 | `IF (IBHYDSUB(N) .AND. IBFACT .EQ. 0) THEN` |

### gwf2lak7.f90 (20)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 736 | gwf2lak7rp | uninitialized | loop-guarded | lid | defined at 725, 727, 731, 733 | `ILAKE(4, M) = LID` |
| 744 | gwf2lak7rp | uninitialized | loop-guarded | lid | defined at 725, 727, 731, 733 | `BGAREA(LID) = BGAREA(LID) + DELC(J) * DELR(I)` |
| 1643 | gwf2lak7fm | uninitialized | loop-guarded | thck | defined at 1640, 1641 | `IF (STGON .GT. BOTCL .OR. THCK .GT. 0.0) THEN` |
| 2511 | gwf2lak7bd | uninitialized | loop-guarded | jcls | defined at 2496, 2511, 2520, 2528, 2549, 2558 | `IF (JCLS(IC4, IC5) .EQ. 1) JCLS(IC4, IC5) = 2` |
| 2514 | gwf2lak7bd | uninitialized | loop-guarded | jcls | defined at 2496, 2511, 2520, 2528, 2549, 2558 | `IF (JCLS(ICL, 1) .GE. 2) GO TO 1300` |
| 2750 | gwf2lak7bd | uninitialized | loop-guarded | tvolm | defined at 2706, 2724 | `TV = TVOLM / 1000000.` |
| 2768 | gwf2lak7bd | uninitialized | loop-guarded | botlk | defined at 2198, 2200, 2203, 2239, 2765, 2766, 3176, 3189 | `IF (STGNEW(LAKE) .LE. BOTLK) THEN` |
| 2794 | gwf2lak7bd | uninitialized | loop-guarded | icb | defined at 2788 | `WRITE(IOUT, 876) (ILB(I), IRB(I), ICB(I), I = 1, LDR1)` |
| 2794 | gwf2lak7bd | uninitialized | loop-guarded | ilb | defined at 2786 | `WRITE(IOUT, 876) (ILB(I), IRB(I), ICB(I), I = 1, LDR1)` |
| 2794 | gwf2lak7bd | uninitialized | loop-guarded | irb | defined at 2787 | `WRITE(IOUT, 876) (ILB(I), IRB(I), ICB(I), I = 1, LDR1)` |
| 3430 | sgwf2lak7bcf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3383, 3387, 3428, 3429 | `IF (CNDFC1 .GT. 0.0 .AND. CNDFC2 .GT. 0.0) CNDFCT(II) = 1.0 / (1.0 / CNDFC2 + 1.0 / CNDFC1)` |
| 3430 | sgwf2lak7bcf7rps | uninitialized | loop-guarded | cndfc2 | defined at 3426, 3427 | `IF (CNDFC1 .GT. 0.0 .AND. CNDFC2 .GT. 0.0) CNDFCT(II) = 1.0 / (1.0 / CNDFC2 + 1.0 / CNDFC1)` |
| 3432 | sgwf2lak7bcf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3383, 3387, 3428, 3429 | `WRITE(IOUT, 7325) (ILAKE(I1, II), I1 = 1, 5), DELC(J), DELR(I), BEDLAK(II), CNDFC1, CNDFC2, CNDFC...` |
| 3432 | sgwf2lak7bcf7rps | uninitialized | loop-guarded | cndfc2 | defined at 3426, 3427 | `WRITE(IOUT, 7325) (ILAKE(I1, II), I1 = 1, 5), DELC(J), DELR(I), BEDLAK(II), CNDFC1, CNDFC2, CNDFC...` |
| 3560 | sgwf2lak7lpf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3515, 3518, 3558, 3559 | `IF (CNDFC1 .GT. 0.0 .AND. CNDFC2 .GT. 0.0) CNDFCT(II) = 1.0 / (1.0 / CNDFC2 + 1.0 / CNDFC1)` |
| 3560 | sgwf2lak7lpf7rps | uninitialized | loop-guarded | cndfc2 | defined at 3548, 3553, 3555 | `IF (CNDFC1 .GT. 0.0 .AND. CNDFC2 .GT. 0.0) CNDFCT(II) = 1.0 / (1.0 / CNDFC2 + 1.0 / CNDFC1)` |
| 3562 | sgwf2lak7lpf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3515, 3518, 3558, 3559 | `WRITE(IOUT, 7325) (ILAKE(I1, II), I1 = 1, 5), DELC(J), DELR(I), BEDLAK(II), CNDFC1, CNDFC2, CNDFC...` |
| 3562 | sgwf2lak7lpf7rps | uninitialized | loop-guarded | cndfc2 | defined at 3548, 3553, 3555 | `WRITE(IOUT, 7325) (ILAKE(I1, II), I1 = 1, 5), DELC(J), DELR(I), BEDLAK(II), CNDFC1, CNDFC2, CNDFC...` |
| 3671 | sgwf2lak7huf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3629, 3632, 3666, 3667 | `CNDFCT(II) = CNDFC1` |
| 3672 | sgwf2lak7huf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3629, 3632, 3666, 3667 | `WRITE(IOUT, 7325) (ILAKE(I1, II), I1 = 1, 5), DELC(J), DELR(I), BEDLAK(II), CNDFC1, CNDFCT(II)` |

### gwf2lpf7.f90 (39)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 944 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 920, 936, 979, 1021, 1022 | `DO 310 K = K1, K2` |
| 944 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 921, 937, 980, 1023, 1036 | `DO 310 K = K1, K2` |
| 945 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 922, 938, 981, 982, 1024 | `DO 310 I = I1, I2` |
| 945 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 923, 939, 983, 994, 1025 | `DO 310 I = I1, I2` |
| 946 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 924, 940, 941, 984, 1026 | `DO 310 J = J1, J2` |
| 946 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 925, 942, 951, 985, 1027 | `DO 310 J = J1, J2` |
| 951 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 925, 942, 951, 985, 1027 | `IF (J2 .EQ. NCOL) J2 = J2 - 1` |
| 952 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 920, 936, 979, 1021, 1022 | `DO 400 K = K1, K2` |
| 952 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 921, 937, 980, 1023, 1036 | `DO 400 K = K1, K2` |
| 953 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 922, 938, 981, 982, 1024 | `DO 400 I = I1, I2` |
| 953 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 923, 939, 983, 994, 1025 | `DO 400 I = I1, I2` |
| 954 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 924, 940, 941, 984, 1026 | `DO 400 J = J1, J2` |
| 954 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 925, 942, 951, 985, 1027 | `DO 400 J = J1, J2` |
| 987 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 920, 936, 979, 1021, 1022 | `DO 410 K = K1, K2` |
| 987 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 921, 937, 980, 1023, 1036 | `DO 410 K = K1, K2` |
| 988 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 922, 938, 981, 982, 1024 | `DO 410 I = I1, I2` |
| 988 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 923, 939, 983, 994, 1025 | `DO 410 I = I1, I2` |
| 989 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 924, 940, 941, 984, 1026 | `DO 410 J = J1, J2` |
| 989 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 925, 942, 951, 985, 1027 | `DO 410 J = J1, J2` |
| 994 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 923, 939, 983, 994, 1025 | `IF (I2 .EQ. NROW) I2 = I2 - 1` |
| 995 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 920, 936, 979, 1021, 1022 | `DO 500 K = K1, K2` |
| 995 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 921, 937, 980, 1023, 1036 | `DO 500 K = K1, K2` |
| 996 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 922, 938, 981, 982, 1024 | `DO 500 I = I1, I2` |
| 996 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 923, 939, 983, 994, 1025 | `DO 500 I = I1, I2` |
| 997 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 924, 940, 941, 984, 1026 | `DO 500 J = J1, J2` |
| 997 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 925, 942, 951, 985, 1027 | `DO 500 J = J1, J2` |
| 1029 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 920, 936, 979, 1021, 1022 | `DO 510 K = K1, K2` |
| 1029 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 921, 937, 980, 1023, 1036 | `DO 510 K = K1, K2` |
| 1030 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 922, 938, 981, 982, 1024 | `DO 510 I = I1, I2` |
| 1030 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 923, 939, 983, 994, 1025 | `DO 510 I = I1, I2` |
| 1031 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 924, 940, 941, 984, 1026 | `DO 510 J = J1, J2` |
| 1031 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 925, 942, 951, 985, 1027 | `DO 510 J = J1, J2` |
| 1036 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 921, 937, 980, 1023, 1036 | `IF (K2 .EQ. NLAY) K2 = K2 - 1` |
| 1037 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 921, 937, 980, 1023, 1036 | `DO 600 K = 1, K2` |
| 1038 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 920, 936, 979, 1021, 1022 | `IF (K .LT. K1) GO TO 600` |
| 1039 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 922, 938, 981, 982, 1024 | `DO 590 I = I1, I2` |
| 1039 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 923, 939, 983, 994, 1025 | `DO 590 I = I1, I2` |
| 1040 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 924, 940, 941, 984, 1026 | `DO 590 J = J1, J2` |
| 1040 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 925, 942, 951, 985, 1027 | `DO 590 J = J1, J2` |

### gwf2mnw17.f90 (19)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 742 | gwf2mnw17rp | uninitialized | loop-guarded | cond | defined at 734, 739, 740, 741, 742 | `cond = cond * 1.0D3` |
| 744 | gwf2mnw17rp | uninitialized | loop-guarded | cond | defined at 734, 739, 740, 741, 742 | `WELL2(11, m) = cond` |
| 755 | gwf2mnw17rp | uninitialized | loop-guarded | hlim | defined at 647, 748, 752 | `WRITE(IOUT, 9004) m, k, j, i, (WELL2(ii, m), ii = 3, 6), hlim, hrfw, WELL2(16, m), igrp, WELL2(11...` |
| 755 | gwf2mnw17rp | uninitialized | loop-guarded | hrfw | defined at 648, 749, 753 | `WRITE(IOUT, 9004) m, k, j, i, (WELL2(ii, m), ii = 3, 6), hlim, hrfw, WELL2(16, m), igrp, WELL2(11...` |
| 874 | gwf2mnw17ad | uninitialized | loop-guarded | cond | defined at 866, 871, 872, 873, 874, 932, 939 | `cond = cond * 1.0D3` |
| 876 | gwf2mnw17ad | uninitialized | loop-guarded | cond | defined at 866, 871, 872, 873, 874, 932, 939 | `WELL2(11, m) = cond` |
| 917 | gwf2mnw17ad | uninitialized | loop-guarded | i | defined at 861, 871, 872, 873, 904, 938 | `hwell = HNEW(i, j, k)` |
| 917 | gwf2mnw17ad | uninitialized | loop-guarded | j | defined at 860, 871, 872, 873, 903, 937 | `hwell = HNEW(i, j, k)` |
| 917 | gwf2mnw17ad | uninitialized | loop-guarded | k | defined at 859, 871, 872, 873, 902, 936 | `hwell = HNEW(i, j, k)` |
| 1053 | gwf2mnw17fm | uninitialized | loop-guarded | cond | defined at 1045, 1050, 1051, 1052, 1053, 1144 | `cond = cond * 1.0D3` |
| 1055 | gwf2mnw17fm | uninitialized | loop-guarded | cond | defined at 1045, 1050, 1051, 1052, 1053, 1144 | `WELL2(11, m) = cond` |
| 1089 | gwf2mnw17fm | uninitialized | loop-guarded | i | defined at 1040, 1050, 1051, 1052, 1077, 1123, 1139 | `hwell = HNEW(i, j, k)` |
| 1089 | gwf2mnw17fm | uninitialized | loop-guarded | j | defined at 1039, 1050, 1051, 1052, 1076, 1122, 1138 | `hwell = HNEW(i, j, k)` |
| 1089 | gwf2mnw17fm | uninitialized | loop-guarded | k | defined at 1038, 1050, 1051, 1052, 1075, 1121, 1137 | `hwell = HNEW(i, j, k)` |
| 1112 | gwf2mnw17fm | uninitialized | loop-guarded | i | defined at 1040, 1050, 1051, 1052, 1077, 1123, 1139 | `hwell = HNEW(i, j, k)` |
| 1112 | gwf2mnw17fm | uninitialized | loop-guarded | j | defined at 1039, 1050, 1051, 1052, 1076, 1122, 1138 | `hwell = HNEW(i, j, k)` |
| 1112 | gwf2mnw17fm | uninitialized | loop-guarded | k | defined at 1038, 1050, 1051, 1052, 1075, 1121, 1137 | `hwell = HNEW(i, j, k)` |
| 1376 | gwf2mnw17bd | uninitialized | loop-guarded | href | defined at 1368, 1372, 1456 | `dd = hwell - href` |
| 1399 | gwf2mnw17bd | uninitialized | loop-guarded | href | defined at 1368, 1372, 1456 | `WRITE(IOWELL2(1), '(i9,2i10,1X,g11.4,1X,i10,2x,6g11.4)') k, j, i, q, 0, qd, hwell, HNEW(i, j, k),...` |

### gwf2mnw27.f90 (389)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 511 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `IF (Rw .GT. 0.0) THEN` |
| 514 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 524 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `IF (Rw .GT. 0.0) THEN` |
| 525 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `IF (Rskin .GT. 0.0) THEN` |
| 526 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 528 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 529 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 530 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 533 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 534 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 538 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 540 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 541 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 544 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 549 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `IF (Rskin .GT. 0.0) THEN` |
| 550 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 552 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 553 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 556 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 560 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 562 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 575 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `IF (Rw .GT. 0.0) THEN` |
| 576 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `IF (B .GE. 0.0) THEN` |
| 577 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 578 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 580 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 581 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 582 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 583 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 586 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 587 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 588 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 592 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 594 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 595 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 596 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 599 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 600 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 605 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 606 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 608 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 609 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 610 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 613 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 614 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 618 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 620 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 621 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 624 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 630 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `IF (B .GE. 0.0) THEN` |
| 631 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 632 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 634 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 635 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 636 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 639 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 640 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 644 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 646 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 647 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 650 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 655 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 656 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 658 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 659 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 662 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 666 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 668 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 683 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 476 | `IF (CWC .GT. 0.0) THEN` |
| 685 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 476 | `CWCNode = CWC` |
| 701 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `IF (Rw .GT. 0.0) THEN` |
| 704 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 714 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `IF (Rw .GT. 0.0) THEN` |
| 715 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `IF (Rskin .GT. 0.0) THEN` |
| 716 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 718 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 719 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 720 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 723 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 724 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 728 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 730 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 731 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 734 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 739 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `IF (Rskin .GT. 0.0) THEN` |
| 740 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 742 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 743 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 746 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 750 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 752 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 765 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `IF (Rw .GT. 0.0) THEN` |
| 766 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `IF (B .GE. 0.0) THEN` |
| 767 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 768 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 770 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 771 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 772 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 773 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 776 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 777 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 778 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 782 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 784 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 785 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 786 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 789 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 790 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 795 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 796 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 798 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 799 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 800 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 803 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 804 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 808 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 810 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 811 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 814 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 820 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `IF (B .GE. 0.0) THEN` |
| 821 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 822 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 824 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 825 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 826 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 829 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 830 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 834 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 836 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 837 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 840 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 845 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 846 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 848 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 849 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 852 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 856 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 858 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 873 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 476 | `IF (CWC .GT. 0.0) THEN` |
| 875 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 476 | `CWCNode = CWC` |
| 883 | gwf2mnw27rp | uninitialized | loop-guarded | il | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 1161, 1262, 1568, 1603, 1623 | `MNWNOD(1, NODNUM + INODE - 1) = IL` |
| 884 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `MNWNOD(2, NODNUM + INODE - 1) = IR` |
| 885 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `MNWNOD(3, NODNUM + INODE - 1) = IC` |
| 890 | gwf2mnw27rp | uninitialized | loop-guarded | pp | defined at 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 888 | `MNWNOD(19, NODNUM + INODE - 1) = PP` |
| 893 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `IRlast = IR` |
| 894 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `IClast = IC` |
| 897 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 897 | gwf2mnw27rp | uninitialized | loop-guarded | iclast | defined at 894, 1145 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 897 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 897 | gwf2mnw27rp | uninitialized | loop-guarded | irlast | defined at 893, 1144 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 905 | gwf2mnw27rp | uninitialized | loop-guarded | pp | defined at 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 888 | `IF (pp .NE. 0.D0) MNWNOD(20, NODNUM + INODE - 1) = 1D30` |
| 934 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `IF (Rw .GT. 0.0) THEN` |
| 937 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 947 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `IF (Rw .GT. 0.0) THEN` |
| 948 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `IF (Rskin .GT. 0.0) THEN` |
| 949 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 951 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 952 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 953 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 956 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 957 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 961 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 963 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 964 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 967 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 972 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `IF (Rskin .GT. 0.0) THEN` |
| 973 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 975 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 976 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 979 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 452 | `RskinNode = Rskin` |
| 983 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `IF (Kskin .GT. 0.0) THEN` |
| 985 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 452 | `KskinNode = Kskin` |
| 999 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `IF (Rw .GT. 0.0) THEN` |
| 1000 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `IF (B .GE. 0.0) THEN` |
| 1001 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 1002 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 1004 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 1005 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 1006 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 1007 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 1010 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 1011 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 1012 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 1016 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 1018 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 1019 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 1020 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 1023 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 1024 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 1029 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 1030 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 1032 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 1033 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 1034 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 1037 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 1038 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 1042 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 1044 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 1045 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 1048 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 445, 452, 466 | `RwNode = Rw` |
| 1054 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `IF (B .GE. 0.0) THEN` |
| 1055 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 1056 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 1058 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 1059 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 1060 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 1063 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 1064 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 1068 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 1070 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 1071 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 1074 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 466 | `BNode = B` |
| 1079 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `IF (C .GE. 0.0) THEN` |
| 1080 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 1082 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 1083 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 1086 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 466 | `CNode = C` |
| 1090 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `IF (P .GE. 0.0) THEN` |
| 1092 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 466 | `PNode = P` |
| 1108 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 476 | `IF (CWC .GT. 0.0) THEN` |
| 1110 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 476 | `CWCNode = CWC` |
| 1118 | gwf2mnw27rp | uninitialized | loop-guarded | ztop | defined at 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112 | `MNWINT(1, INTNUM + IINT - 1) = Ztop` |
| 1119 | gwf2mnw27rp | uninitialized | loop-guarded | zbotm | defined at 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112 | `MNWINT(2, INTNUM + IINT - 1) = Zbotm` |
| 1120 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `MNWINT(3, INTNUM + IINT - 1) = IR` |
| 1121 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `MNWINT(4, INTNUM + IINT - 1) = IC` |
| 1125 | gwf2mnw27rp | uninitialized | loop-guarded | zbotmlast | defined at 1134 | `IF (Ztop .GT. Zbotmlast) THEN` |
| 1125 | gwf2mnw27rp | uninitialized | loop-guarded | ztop | defined at 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112 | `IF (Ztop .GT. Zbotmlast) THEN` |
| 1134 | gwf2mnw27rp | uninitialized | loop-guarded | zbotm | defined at 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112 | `Zbotmlast = Zbotm` |
| 1144 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `IRlast = IR` |
| 1145 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `IClast = IC` |
| 1147 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 1147 | gwf2mnw27rp | uninitialized | loop-guarded | iclast | defined at 894, 1145 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 1147 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 1147 | gwf2mnw27rp | uninitialized | loop-guarded | irlast | defined at 893, 1144 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 1157 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `DO WHILE (Ztop .LE. BOTM(IC, IR, LBOTM(K)))` |
| 1157 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `DO WHILE (Ztop .LE. BOTM(IC, IR, LBOTM(K)))` |
| 1157 | gwf2mnw27rp | uninitialized | loop-guarded | ztop | defined at 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112 | `DO WHILE (Ztop .LE. BOTM(IC, IR, LBOTM(K)))` |
| 1172 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `IF (IBOUND(IC, IR, IL) .NE. 0) THEN` |
| 1172 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `IF (IBOUND(IC, IR, IL) .NE. 0) THEN` |
| 1191 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `MNWNOD(2, NODNUM) = IR` |
| 1192 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `MNWNOD(3, NODNUM) = IC` |
| 1209 | gwf2mnw27rp | uninitialized | loop-guarded | nodnum | defined at 489, 1175, 1218, 1263 | `IF (MNWNOD(1, NODNUM) .EQ. IL) THEN` |
| 1212 | gwf2mnw27rp | uninitialized | loop-guarded | nodnum | defined at 489, 1175, 1218, 1263 | `MNWNOD(13, NODNUM) = INTNUM + IINT - 1` |
| 1217 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `IF (IBOUND(IC, IR, IL) .NE. 0) THEN` |
| 1217 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `IF (IBOUND(IC, IR, IL) .NE. 0) THEN` |
| 1218 | gwf2mnw27rp | uninitialized | loop-guarded | nodnum | defined at 489, 1175, 1218, 1263 | `NODNUM = NODNUM + 1` |
| 1231 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `MNWNOD(2, NODNUM) = IR` |
| 1232 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `MNWNOD(3, NODNUM) = IC` |
| 1259 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `DO WHILE (Zbotm .LT. BOTM(IC, IR, LBOTM(K)) .AND. ((K + 1) .LE. NLAY))` |
| 1259 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `DO WHILE (Zbotm .LT. BOTM(IC, IR, LBOTM(K)) .AND. ((K + 1) .LE. NLAY))` |
| 1259 | gwf2mnw27rp | uninitialized | loop-guarded | zbotm | defined at 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112 | `DO WHILE (Zbotm .LT. BOTM(IC, IR, LBOTM(K)) .AND. ((K + 1) .LE. NLAY))` |
| 1263 | gwf2mnw27rp | uninitialized | loop-guarded | nodnum | defined at 489, 1175, 1218, 1263 | `NODNUM = NODNUM + 1` |
| 1276 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `MNWNOD(2, NODNUM) = IR` |
| 1277 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `MNWNOD(3, NODNUM) = IC` |
| 1604 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1570, 1607, 1625 | `IF (Zpump .LT. BOTM(IC, IR, LBOTM(IL) - 1) .AND. Zpump .GT. BOTM(IC, IR, LBOTM(IL))) THEN` |
| 1604 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 507, 512, 517, 527, 532, 539, 543, 551, 555, 561, 564, 579, 585, 593, 598, 607, 612, 619, 623, 633, 638, 645, 649, 657, 661, 667, 670, 684, 687, 697, 702, 707, 717, 722, 729, 733, 741, 745, 751, 754, 769, 775, 783, 788, 797, 802, 809, 813, 823, 828, 835, 839, 847, 851, 857, 860, 874, 877, 930, 935, 940, 950, 955, 962, 966, 974, 978, 984, 987, 1003, 1009, 1017, 1022, 1031, 1036, 1043, 1047, 1057, 1062, 1069, 1073, 1081, 1085, 1091, 1094, 1109, 1112, 1569, 1606, 1624 | `IF (Zpump .LT. BOTM(IC, IR, LBOTM(IL) - 1) .AND. Zpump .GT. BOTM(IC, IR, LBOTM(IL))) THEN` |
| 1893 | gwf2mnw27rp | uninitialized | loop-guarded | cprime | defined at 1795, 1809 | `MNW2(12, MNWID) = Cprime` |
| 1914 | gwf2mnw27rp | uninitialized | loop-guarded | capmult | defined at 1804, 1809, 1812 | `MNW2(24, MNWID) = CapMult` |
| 1918 | gwf2mnw27rp | uninitialized | loop-guarded | capmult | defined at 1804, 1809, 1812 | `WRITE(iout, 1113) CapMult` |
| 1926 | gwf2mnw27rp | uninitialized | loop-guarded | capmult | defined at 1804, 1809, 1812 | `IF (CapMult .EQ. 0.D0) THEN` |
| 2118 | gwf2mnw27ad | uninitialized | loop-guarded | ic | defined at 2091, 2148 | `hhnew = hnew(ic, ir, il)` |
| 2118 | gwf2mnw27ad | uninitialized | loop-guarded | il | defined at 2089, 2146 | `hhnew = hnew(ic, ir, il)` |
| 2118 | gwf2mnw27ad | uninitialized | loop-guarded | ir | defined at 2090, 2147 | `hhnew = hnew(ic, ir, il)` |
| 2186 | gwf2mnw27ad | uninitialized | loop-guarded | qpot | defined at 2132, 2160, 2189 | `ratio = qpot / qdes` |
| 2194 | gwf2mnw27ad | uninitialized | loop-guarded | qoff | defined at 2048, 2051, 2056, 2059 | `IF (ratio .LT. Qoff) THEN` |
| 2201 | gwf2mnw27ad | uninitialized | loop-guarded | qon | defined at 2049, 2052, 2057, 2060 | `ELSE IF (ratio .GT. Qon .AND. (ABS(qact) .LT. Qsmall)) THEN` |
| 2203 | gwf2mnw27ad | uninitialized | loop-guarded | qpot | defined at 2132, 2160, 2189 | `mnw2(30, iw) = Qpot` |
| 2204 | gwf2mnw27ad | uninitialized | loop-guarded | qpot | defined at 2132, 2160, 2189 | `MNWNOD(4, firstnode) = Qpot` |
| 2210 | gwf2mnw27ad | uninitialized | loop-guarded | qcut | defined at 2047 | `IF (QCUT .EQ. 0 .AND. ratio .GT. 0.D0) THEN` |
| 2212 | gwf2mnw27ad | uninitialized | loop-guarded | qpot | defined at 2132, 2160, 2189 | `mnw2(30, iw) = Qpot` |
| 2213 | gwf2mnw27ad | uninitialized | loop-guarded | qpot | defined at 2132, 2160, 2189 | `MNWNOD(4, firstnode) = Qpot` |
| 2422 | gwf2mnw27fm | uninitialized | loop-guarded | lasth | defined at 2316 | `htemp = ABS(lastH - hwell)` |
| 2426 | gwf2mnw27fm | uninitialized | call-assumed | qactcap | defined at 2319 | `mnw2(29, iw) = qactCap` |
| 2436 | gwf2mnw27fm | uninitialized | call-assumed | qactcap | defined at 2319 | `WRITE(iout, *) ' with Pump-Capacity Q = ', qactCap` |
| 2523 | gwf2mnw27fm | uninitialized | loop-guarded | hlim | defined at 2509 | `qact = (hlim - hhnew) * cond` |
| 2525 | gwf2mnw27fm | uninitialized | loop-guarded | hlim | defined at 2509 | `rhs(ic, ir, il) = rhs(ic, ir, il) - cond * hlim` |
| 2739 | gwf2mnw27bd | uninitialized | loop-guarded | iweldry | defined at 2669, 2676 | `IF (MNWPRNT .GT. 1 .AND. iweldry .EQ. 1) THEN` |
| 2797 | gwf2mnw27bd | uninitialized | loop-guarded | hwell | defined at 2700, 2853 | `IF (MNWNOD(15, INODE) .NE. hwell .AND. MNWNOD(15, INODE) .NE. Hdry .AND. numnddel .NE. 0) THEN` |
| 3674 | smnw2cond | uninitialized | loop-guarded | zbotm | defined at 3590, 3608 | `alpha2 = hwell - zbotm` |
| 3686 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3582, 3615, 3756 | `IF (totlength .GT. 0D0) THEN` |
| 3687 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3582, 3615, 3756 | `alpha3 = alpha2 / totlength` |
| 3733 | smnw2cond | uninitialized | loop-guarded | firstint | defined at 3579 | `IF (firstint .EQ. lastint) THEN` |
| 3733 | smnw2cond | uninitialized | loop-guarded | lastint | defined at 3580 | `IF (firstint .EQ. lastint) THEN` |
| 3734 | smnw2cond | uninitialized | loop-guarded | ztop | defined at 3589, 3607 | `topscreen = ztop` |
| 3735 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3582, 3615, 3756 | `bottomscreen = ztop - totlength` |
| 3735 | smnw2cond | uninitialized | loop-guarded | ztop | defined at 3589, 3607 | `bottomscreen = ztop - totlength` |
| 3740 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3582, 3615, 3756 | `topscreen = top - ((thck - totlength) / 2)` |
| 3741 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3582, 3615, 3756 | `bottomscreen = topscreen - totlength` |
| 3745 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3582, 3615, 3756 | `topscreen = zbotm + totlength` |
| 3745 | smnw2cond | uninitialized | loop-guarded | zbotm | defined at 3590, 3608 | `topscreen = zbotm + totlength` |
| 3746 | smnw2cond | uninitialized | loop-guarded | zbotm | defined at 3590, 3608 | `bottomscreen = zbotm` |
| 3810 | smnw2cond | uninitialized | call-assumed | isolnflag | defined at 3796 | `IF (ISOLNFLAG .EQ. 0 .AND. ITFLAG .GT. 0 .AND. QQ .NE. 0.D0) THEN` |
| 3838 | smnw2cond | uninitialized | loop-guarded | dhp | defined at 3714, 3796, 3802, 3834 | `MNWNOD(18, INODE) = dhp` |
| 3844 | smnw2cond | uninitialized | loop-guarded | bottomscreen | defined at 3735, 3741, 3746, 3760, 3764, 3773, 3904 | `ratio = (topscreen - bottomscreen) / thck` |
| 3844 | smnw2cond | uninitialized | loop-guarded | topscreen | defined at 3734, 3740, 3745, 3759, 3763, 3772, 3901 | `ratio = (topscreen - bottomscreen) / thck` |
| 3852 | smnw2cond | uninitialized | loop-guarded | dhp | defined at 3714, 3796, 3802, 3834 | `IF (ITFLAG .EQ. 1. .AND. (Qact .LT. 0.D0 .AND. dhp .GE. 0.D0) .OR. (Qact .GT. 0.D0 .AND. dhp .LE....` |
| 3858 | smnw2cond | uninitialized | loop-guarded | dhp | defined at 3714, 3796, 3802, 3834 | `dpp = dhp / (Qact * (- 1.D0))` |
| 3866 | smnw2cond | uninitialized | loop-guarded | dhp | defined at 3714, 3796, 3802, 3834 | `WRITE(iout, *) '***WARNING*** Partial penetration term (dpp) set to 0.0 due to misalignment of dh...` |
| 3900 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `IF (topscreen .GT. top) THEN` |
| 3900 | smnw2cond | uninitialized | loop-guarded | topscreen | defined at 3734, 3740, 3745, 3759, 3763, 3772, 3901 | `IF (topscreen .GT. top) THEN` |
| 3901 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `topscreen = top` |
| 3903 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `IF (mnwnod(21, inode) .LT. bot) THEN` |
| 3904 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `bottomscreen = bot` |
| 3909 | smnw2cond | uninitialized | loop-guarded | b | defined at 3549, 3553, 3631, 3635 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3909 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3909 | smnw2cond | uninitialized | loop-guarded | bottomscreen | defined at 3735, 3741, 3746, 3760, 3764, 3773, 3904 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3909 | smnw2cond | uninitialized | call-assumed | skin | defined at 3553, 3635 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3909 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3909 | smnw2cond | uninitialized | loop-guarded | topscreen | defined at 3734, 3740, 3745, 3759, 3763, 3772, 3901 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3915 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `WRITE(iout, '(A15,I3,1PG12.4,1x,5G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, topscreen,...` |
| 3915 | smnw2cond | uninitialized | loop-guarded | bottomscreen | defined at 3735, 3741, 3746, 3760, 3764, 3773, 3904 | `WRITE(iout, '(A15,I3,1PG12.4,1x,5G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, topscreen,...` |
| 3915 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `WRITE(iout, '(A15,I3,1PG12.4,1x,5G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, topscreen,...` |
| 3915 | smnw2cond | uninitialized | loop-guarded | topscreen | defined at 3734, 3740, 3745, 3759, 3763, 3772, 3901 | `WRITE(iout, '(A15,I3,1PG12.4,1x,5G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, topscreen,...` |
| 3926 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `t1 = top` |
| 3927 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `t2 = bot` |
| 3929 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `IF (mnwnod(20, inode) .GT. top) THEN` |
| 3930 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `t1 = top` |
| 3934 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `IF (mnwnod(21, inode) .LT. bot) THEN` |
| 3935 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `t2 = bot` |
| 3939 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `IF (mnwnod(21, inode) .GT. top) THEN` |
| 3947 | smnw2cond | uninitialized | loop-guarded | b | defined at 3549, 3553, 3631, 3635 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, alpha, S...` |
| 3947 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, alpha, S...` |
| 3947 | smnw2cond | uninitialized | call-assumed | skin | defined at 3553, 3635 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, alpha, S...` |
| 3947 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, alpha, S...` |
| 3954 | smnw2cond | uninitialized | loop-guarded | b | defined at 3549, 3553, 3631, 3635 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, alpha, Ski...` |
| 3954 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, alpha, Ski...` |
| 3954 | smnw2cond | uninitialized | call-assumed | skin | defined at 3553, 3635 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, alpha, Ski...` |
| 3954 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, alpha, Ski...` |
| 3962 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ' N/A ',...` |
| 3962 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ' N/A ',...` |
| 3966 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, ' N/A ', '...` |
| 3966 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, ' N/A ', '...` |
| 3979 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ...` |
| 3979 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ...` |
| 3984 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ...` |
| 3984 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ...` |
| 3993 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, al...` |
| 3993 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, al...` |
| 3998 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3530 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, ' ...` |
| 3998 | smnw2cond | uninitialized | loop-guarded | top | defined at 3524, 3526, 3527 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, ' ...` |
| 4154 | cel2wel2 | uninitialized | conditional | c | defined at 4137, 4141, 4143, 4147, 4152 | `cel2wel2 = A + B + C` |
| 4279 | smnw2seep | uninitialized | loop-guarded | ic | defined at 4266, 4411, 4504 | `hwell = hnew(ic, ir, il)` |
| 4279 | smnw2seep | uninitialized | loop-guarded | il | defined at 4264, 4409, 4502 | `hwell = hnew(ic, ir, il)` |
| 4279 | smnw2seep | uninitialized | loop-guarded | ir | defined at 4265, 4410, 4503 | `hwell = hnew(ic, ir, il)` |
| 4299 | smnw2seep | uninitialized | conditional | qpot | defined at 4292, 4302 | `ratio = qpot / qdes` |
| 4327 | smnw2seep | uninitialized | conditional | qpot | defined at 4292, 4302 | `mnw2(30, iw) = Qpot` |
| 4428 | smnw2seep | uninitialized | conditional | hwell | defined at 4262, 4277, 4279, 4290, 4458, 4460, 4472, 4483, 4485 | `IF (kSeep .GT. 1 .AND. hwell .LT. Bottom) THEN` |
| 4460 | smnw2seep | uninitialized | loop-guarded | ic | defined at 4266, 4411, 4504 | `hwell = hnew(ic, ir, il)` |
| 4460 | smnw2seep | uninitialized | loop-guarded | il | defined at 4264, 4409, 4502 | `hwell = hnew(ic, ir, il)` |
| 4460 | smnw2seep | uninitialized | loop-guarded | ir | defined at 4265, 4410, 4503 | `hwell = hnew(ic, ir, il)` |
| 4485 | smnw2seep | uninitialized | loop-guarded | ic | defined at 4266, 4411, 4504 | `hwell = hnew(ic, ir, il)` |
| 4485 | smnw2seep | uninitialized | loop-guarded | il | defined at 4264, 4409, 4502 | `hwell = hnew(ic, ir, il)` |
| 4485 | smnw2seep | uninitialized | loop-guarded | ir | defined at 4265, 4410, 4503 | `hwell = hnew(ic, ir, il)` |
| 4501 | smnw2seep | uninitialized | conditional | firstnode | defined at 4260, 4405 | `DO INODE = firstnode, lastnode` |
| 4501 | smnw2seep | uninitialized | conditional | lastnode | defined at 4261, 4406 | `DO INODE = firstnode, lastnode` |
| 4510 | smnw2seep | uninitialized | conditional | hwell | defined at 4262, 4277, 4279, 4290, 4458, 4460, 4472, 4483, 4485 | `qact = (hwell - hnew(ic, ir, il)) * MNWNOD(14, INODE)` |
| 4512 | smnw2seep | uninitialized | conditional | hwell | defined at 4262, 4277, 4279, 4290, 4458, 4460, 4472, 4483, 4485 | `MNWNOD(15, INODE) = hwell` |
| 4523 | smnw2seep | uninitialized | loop-guarded | qseep | defined at 4404, 4432 | `IF (ABS(seepchk) .LT. ABS(MNW2(18, IW)) .AND. qseep .NE. 0.0) LIMQ(3, IW) = 1` |
| 4595 | smnw2seep | uninitialized | conditional | hwell | defined at 4262, 4277, 4279, 4290, 4458, 4460, 4472, 4483, 4485 | `MNW2(17, iw) = hwell` |
| 4681 | gwf2mnw27bh | uninitialized | conditional | nodepump | defined at 4641, 4658 | `IF (nodepump .EQ. firstnode) THEN` |
| 4692 | gwf2mnw27bh | uninitialized | conditional | nodepump | defined at 4641, 4658 | `IF (nodepump .EQ. inode .AND. inode .NE. lastnode) THEN` |
| 5085 | mnw2horiz | uninitialized | loop-guarded | xi | defined at 5078, 5098, 5123, 5282, 5293, 5309 | `IF (x2face .EQ. xi) THEN` |
| 5086 | mnw2horiz | uninitialized | loop-guarded | xi | defined at 5078, 5098, 5123, 5282, 5293, 5309 | `lxf = SQRT(((x2 - xi) ** 2) + ((y2 - yi) ** 2) + ((z2 - zi) ** 2))` |
| 5110 | mnw2horiz | uninitialized | loop-guarded | yi | defined at 5073, 5103, 5124, 5277, 5298, 5310 | `IF (y2face .EQ. yi) THEN` |
| 5111 | mnw2horiz | uninitialized | loop-guarded | yi | defined at 5073, 5103, 5124, 5277, 5298, 5310 | `lyf = SQRT(((x2 - xi) ** 2) + ((y2 - yi) ** 2) + ((z2 - zi) ** 2))` |
| 5135 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 5074, 5099, 5128, 5278, 5294, 5314 | `IF (z2face .EQ. zi) THEN` |
| 5136 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 5074, 5099, 5128, 5278, 5294, 5314 | `lzf = SQRT(((x2 - xi) ** 2) + ((y2 - yi) ** 2) + ((z2 - zi) ** 2))` |
| 5204 | mnw2horiz | uninitialized | loop-guarded | xi | defined at 5078, 5098, 5123, 5282, 5293, 5309 | `IF (xi .EQ. xi2) THEN` |
| 5204 | mnw2horiz | uninitialized | loop-guarded | xi2 | defined at 5156, 5167, 5183 | `IF (xi .EQ. xi2) THEN` |
| 5208 | mnw2horiz | uninitialized | loop-guarded | xi | defined at 5078, 5098, 5123, 5282, 5293, 5309 | `xa = xi` |
| 5209 | mnw2horiz | uninitialized | loop-guarded | xi2 | defined at 5156, 5167, 5183 | `xb = xi2` |
| 5216 | mnw2horiz | uninitialized | loop-guarded | yi | defined at 5073, 5103, 5124, 5277, 5298, 5310 | `IF (yi .EQ. yi2) THEN` |
| 5216 | mnw2horiz | uninitialized | loop-guarded | yi2 | defined at 5151, 5172, 5184 | `IF (yi .EQ. yi2) THEN` |
| 5220 | mnw2horiz | uninitialized | loop-guarded | yi | defined at 5073, 5103, 5124, 5277, 5298, 5310 | `ya = yi` |
| 5221 | mnw2horiz | uninitialized | loop-guarded | yi2 | defined at 5151, 5172, 5184 | `yb = yi2` |
| 5228 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 5074, 5099, 5128, 5278, 5294, 5314 | `IF (zi .EQ. zi2) THEN` |
| 5228 | mnw2horiz | uninitialized | loop-guarded | zi2 | defined at 5152, 5168, 5188 | `IF (zi .EQ. zi2) THEN` |
| 5232 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 5074, 5099, 5128, 5278, 5294, 5314 | `za = zi` |
| 5233 | mnw2horiz | uninitialized | loop-guarded | zi2 | defined at 5152, 5168, 5188 | `zb = zi2` |
| 5245 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 5074, 5099, 5128, 5278, 5294, 5314 | `zseg2(inode) = zi` |
| 5246 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 5074, 5099, 5128, 5278, 5294, 5314 | `zseg1(inode + 1) = zi` |
| 5325 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 5074, 5099, 5128, 5278, 5294, 5314 | `zseg2(inode + 1) = zi` |
| 5706 | cel2wel2seg | uninitialized | conditional | omega0 | defined at 5588 | `IF (omega0 .GT. 90.0) omega = 180.0 - omega` |
| 5798 | mnw2capacity | uninitialized | loop-guarded | ifirstl | defined at 5778 | `L1 = CapTable(iw, ifirstL, 1)` |
| 5799 | mnw2capacity | uninitialized | loop-guarded | isecondl | defined at 5779 | `L2 = CapTable(iw, isecondL, 1)` |
| 5800 | mnw2capacity | uninitialized | loop-guarded | ifirstl | defined at 5778 | `Q1 = CapTable(iw, ifirstL, 2)` |
| 5801 | mnw2capacity | uninitialized | loop-guarded | isecondl | defined at 5779 | `Q2 = CapTable(iw, isecondL, 2)` |
| 6471 | ltst2 | uninitialized | loop-guarded | sume | defined at 6391, 6448 | `E = SUME` |
| 6485 | ltst2 | uninitialized | loop-guarded | pdl | defined at 6469, 6472, 6475, 6480 | `XP = XP + V(I) * PDL` |

### gwf2mnw2i7.f90 (9)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 377 | gwf2mnw2i7ot | uninitialized | loop-guarded | seepflg | defined at 365, 471 | `IF (SEEPFLG .EQ. hwell .OR. SEEPFLG .EQ. Hdry) THEN` |
| 385 | gwf2mnw2i7ot | uninitialized | loop-guarded | cond | defined at 366, 472 | `hwell = HCELL + (q / COND)` |
| 385 | gwf2mnw2i7ot | uninitialized | loop-guarded | hcell | defined at 364, 418, 470 | `hwell = HCELL + (q / COND)` |
| 385 | gwf2mnw2i7ot | uninitialized | loop-guarded | q | defined at 320, 322, 362, 417, 475 | `hwell = HCELL + (q / COND)` |
| 486 | gwf2mnw2i7ot | uninitialized | loop-guarded | seepflg | defined at 365, 471 | `IF (SEEPFLG .NE. hwell .AND. SEEPFLG .NE. Hdry) THEN` |
| 490 | gwf2mnw2i7ot | uninitialized | loop-guarded | cond | defined at 366, 472 | `hwell = HCELL + (q / COND)` |
| 490 | gwf2mnw2i7ot | uninitialized | loop-guarded | hcell | defined at 364, 418, 470 | `hwell = HCELL + (q / COND)` |
| 490 | gwf2mnw2i7ot | uninitialized | loop-guarded | q | defined at 320, 322, 362, 417, 475 | `hwell = HCELL + (q / COND)` |
| 555 | gwf2mnw2i7ot | uninitialized | loop-guarded | sftest | defined at 485, 491 | `IF (sftest .LT. 1.0) THEN` |

### gwf2rch7.f90 (1)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 194 | gwf2rch7rp | uninitialized | conditional | inirch | defined at 140, 142 | `IF (INIRCH .LT. 0) THEN` |

### gwf2res7.f90 (4)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 496 | gwf2res7bd | uninitialized | loop-guarded | rate | defined at 490, 493 | `BUFF(IC, IR, IL) = BUFF(IC, IR, IL) + RATE` |
| 499 | gwf2res7bd | uninitialized | loop-guarded | rate | defined at 490, 493 | `IF (RATE) 94, 190, 96` |
| 503 | gwf2res7bd | uninitialized | loop-guarded | rate | defined at 490, 493 | `RATOUT = RATOUT - RATE` |
| 508 | gwf2res7bd | uninitialized | loop-guarded | rate | defined at 490, 493 | `RATIN = RATIN + RATE` |

### gwf2sfr7.f90 (372)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 617 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `IF (IBOUND(jrch, irch, krch) .LE. 0) WRITE(IOUT, 9018) ireach, jseg` |
| 617 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9018) ireach, jseg` |
| 617 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `IF (IBOUND(jrch, irch, krch) .LE. 0) WRITE(IOUT, 9018) ireach, jseg` |
| 617 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9018) ireach, jseg` |
| 617 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `IF (IBOUND(jrch, irch, krch) .LE. 0) WRITE(IOUT, 9018) ireach, jseg` |
| 634 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `THTR(ii) = THTS(ii) - SC2LPF(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 634 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `THTR(ii) = THTS(ii) - SC2LPF(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 634 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `THTR(ii) = THTS(ii) - SC2LPF(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 637 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `IF (LAYCON(krch) .LT. 2) THEN` |
| 638 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `THTR(ii) = THTS(ii) - SC1(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 638 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `THTR(ii) = THTS(ii) - SC1(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 638 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `THTR(ii) = THTS(ii) - SC1(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 642 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `DO k = 1, krch` |
| 645 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `THTR(ii) = THTS(ii) - SC2(jrch, irch, kkrch) / (DELR(jrch) * DELC(irch))` |
| 645 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `THTR(ii) = THTS(ii) - SC2(jrch, irch, kkrch) / (DELR(jrch) * DELC(irch))` |
| 649 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `THTR(ii) = THTS(ii) - SC2HUF(jrch, irch)` |
| 649 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `THTR(ii) = THTS(ii) - SC2HUF(jrch, irch)` |
| 658 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 658 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 658 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 658 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 658 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 661 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 661 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 661 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 661 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 661 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 666 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 666 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 666 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 666 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 666 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 670 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 670 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 670 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 670 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 670 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 676 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 676 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 676 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 676 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 676 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 681 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 681 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 681 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 681 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 681 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 688 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 688 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 688 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 688 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 688 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 694 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 694 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 694 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 694 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 694 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 701 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 701 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 701 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 701 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 701 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 704 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 704 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 704 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 704 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 704 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 717 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `IF (jseg .LE. 0 .OR. jseg .GT. NSS) THEN` |
| 721 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `IF (jseg .NE. nseg) THEN` |
| 724 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `IF (jseg .NE. nseg) THEN` |
| 730 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `IF (ireach .NE. nreach) THEN` |
| 738 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `ISTRM(1, ii) = krch` |
| 739 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613, 769, 849 | `ISTRM(2, ii) = irch` |
| 740 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `ISTRM(3, ii) = jrch` |
| 741 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `ISTRM(4, ii) = jseg` |
| 742 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `ISTRM(5, ii) = ireach` |
| 745 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `ISEG(4, jseg) = ireach` |
| 745 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `ISEG(4, jseg) = ireach` |
| 747 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `uzfar_check % ltype = LAYHDT(krch)` |
| 793 | gwf2sfr7ar | uninitialized | loop-guarded | thsslpe | defined at 778 | `THTS(irch) = SEG(18, nseg) - (thsslpe * dist)` |
| 794 | gwf2sfr7ar | uninitialized | loop-guarded | thislpe | defined at 779 | `THTI(irch) = SEG(19, nseg) - (thislpe * dist)` |
| 795 | gwf2sfr7ar | uninitialized | loop-guarded | epsslpe | defined at 780 | `EPS(irch) = SEG(20, nseg) - (epsslpe * dist)` |
| 796 | gwf2sfr7ar | uninitialized | loop-guarded | uhcslpe | defined at 781 | `UHC(irch) = SEG(21, nseg) - (uhcslpe * dist)` |
| 814 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 552, 555, 560, 564, 576, 581, 593, 598, 610, 613 | `DO k = 1, krch` |
| 1176 | parsesfroptions | uninitialized | conditional | iostat | defined at 1058 | `IF (Iostat .NE. 0) THEN` |
| 1652 | gwf2sfr7rp | uninitialized | loop-guarded | hcslpe | defined at 1641 | `avhc = SEG(6, nseg) - (hcslpe * dist)` |
| 1653 | gwf2sfr7rp | uninitialized | loop-guarded | thkslpe | defined at 1642 | `avthk = SEG(7, nseg) - (thkslpe * dist)` |
| 1654 | gwf2sfr7rp | uninitialized | loop-guarded | elslpe | defined at 1640 | `STRM(2, irch) = elslpe` |
| 1655 | gwf2sfr7rp | uninitialized | loop-guarded | elslpe | defined at 1640 | `STRM(3, irch) = SEG(8, nseg) - (elslpe * dist)` |
| 1683 | gwf2sfr7rp | uninitialized | loop-guarded | dpslpe | defined at 1635 | `avdpth = SEG(10, nseg) - (dpslpe * dist)` |
| 1684 | gwf2sfr7rp | uninitialized | loop-guarded | wdslpe | defined at 1634 | `STRM(5, irch) = SEG(9, nseg) - (wdslpe * dist)` |
| 1689 | gwf2sfr7rp | uninitialized | loop-guarded | avhc | defined at 1652 | `STRM(16, irch) = (avhc * STRM(5, irch) * rchlen) / avthk` |
| 1689 | gwf2sfr7rp | uninitialized | loop-guarded | avthk | defined at 1653, 1901 | `STRM(16, irch) = (avhc * STRM(5, irch) * rchlen) / avthk` |
| 1692 | gwf2sfr7rp | uninitialized | loop-guarded | wdslpe | defined at 1634 | `STRM(5, irch) = SEG(9, nseg) - (wdslpe * dist)` |
| 1697 | gwf2sfr7rp | uninitialized | loop-guarded | avhc | defined at 1652 | `STRM(16, irch) = (avhc * STRM(5, irch) * rchlen) / avthk` |
| 1697 | gwf2sfr7rp | uninitialized | loop-guarded | avthk | defined at 1653, 1901 | `STRM(16, irch) = (avhc * STRM(5, irch) * rchlen) / avthk` |
| 1802 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1795 | `dpthlw = QSTAGE(1 + nstrpts, nseg)` |
| 1805 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1795 | `QSTAGE(1 + nstrpts, nseg) = 0.01` |
| 1807 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1795 | `wdthlw = QSTAGE(1 + 2 * nstrpts, nseg)` |
| 1810 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1795 | `QSTAGE(1 + 2 * nstrpts, nseg) = 1.0` |
| 1812 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1795 | `DO ipt = 2, nstrpts` |
| 1815 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1795 | `dpth1 = QSTAGE((ipt - 1) + nstrpts, nseg)` |
| 1816 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1795 | `dpth2 = QSTAGE(ipt + nstrpts, nseg)` |
| 1817 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1795 | `wdth1 = QSTAGE((ipt - 1) + (2 * nstrpts), nseg)` |
| 1818 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1795 | `wdth2 = QSTAGE(ipt + (2 * nstrpts), nseg)` |
| 1905 | gwf2sfr7rp | uninitialized | loop-guarded | avdpth | defined at 1683 | `STRM(15, irch) = avdpth + STRM(3, irch)` |
| 2506 | gwf2sfr7fm | uninitialized | conditional | thet1 | defined at 2398, 2400 | `stgon = (1.0 - thet1) * STGOLD(lk) + thet1 * STGNEW(lk)` |
| 2513 | gwf2sfr7fm | uninitialized | loop-guarded | roughch | defined at 2451, 2520, 2747, 2820, 2864, 2886, 3003, 3006, 3009, 3012, 3015, 3018, 3139, 3176, 3276, 3320, 3368 | `flowin = (CONST / roughch) * widthch * smooth(dlkstr, dwdh) * (dlkstr ** FIVE_THIRDS) * (DSQRT(sl...` |
| 2513 | gwf2sfr7fm | uninitialized | loop-guarded | widthch | defined at 2452 | `flowin = (CONST / roughch) * widthch * smooth(dlkstr, dwdh) * (dlkstr ** FIVE_THIRDS) * (DSQRT(sl...` |
| 2639 | gwf2sfr7fm | uninitialized | loop-guarded | roughch | defined at 2451, 2520, 2747, 2820, 2864, 2886, 3003, 3006, 3009, 3012, 3015, 3018, 3139, 3176, 3276, 3320, 3368 | `qcnst = CONST * width * SQRT(slope) / roughch` |
| 2715 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2639, 3617 | `depth = (flwmpt / qcnst) ** 0.6D0` |
| 2751 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `depth = cdpth * (flwest ** fdpth)` |
| 2751 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `depth = cdpth * (flwest ** fdpth)` |
| 2752 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `width = awdth * (flwest ** bwdth)` |
| 2752 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `width = awdth * (flwest ** bwdth)` |
| 2773 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (h .LE. strtop .AND. flowc .LT. NEARZERO) iflg = 0` |
| 2794 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `flwen1 = flwmpt - 0.5D0 * flobot1` |
| 2797 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `flwen1 = flwmpt` |
| 2812 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flobot2 .GT. flowc) flobot2 = flowc` |
| 2813 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `depth2 = ((flwmpt - 0.5D0 * flobot2) / qcnst) ** 0.6D0` |
| 2813 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2639, 3617 | `depth2 = ((flwmpt - 0.5D0 * flobot2) / qcnst) ** 0.6D0` |
| 2814 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `depth1 = ((flwmpt - 0.5D0 * flobot1) / qcnst) ** 0.6D0` |
| 2814 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2639, 3617 | `depth1 = ((flwmpt - 0.5D0 * flobot1) / qcnst) ** 0.6D0` |
| 2824 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `flwen2 = (enpt2 / cdpth) ** (1.0 / fdpth)` |
| 2824 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `flwen2 = (enpt2 / cdpth) ** (1.0 / fdpth)` |
| 2826 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `width2 = awdth * (flwen2 ** bwdth)` |
| 2826 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `width2 = awdth * (flwen2 ** bwdth)` |
| 2840 | gwf2sfr7fm | uninitialized | loop-guarded | width2 | defined at 2820, 2826, 2829, 2833, 2881, 2886, 2892, 2895, 2916, 2946, 2960, 3018, 3034, 3037, 3082 | `IF (width2 .GT. NEARZERO) THEN` |
| 2841 | gwf2sfr7fm | uninitialized | loop-guarded | width2 | defined at 2820, 2826, 2829, 2833, 2881, 2886, 2892, 2895, 2916, 2946, 2960, 3018, 3034, 3037, 3082 | `flwpet2 = (precip - etstr) * width2` |
| 2847 | gwf2sfr7fm | uninitialized | loop-guarded | wetperm2 | defined at 2820, 2827, 2830, 2835, 2849, 2882, 2886, 2893, 2917, 3018, 3035, 3038, 3089, 3116 | `flobot2 = ((avhc * wetperm2 * strlen / sbdthk) * (strtop - h))` |
| 2854 | gwf2sfr7fm | uninitialized | loop-guarded | wetperm2 | defined at 2820, 2827, 2830, 2835, 2849, 2882, 2886, 2893, 2917, 3018, 3035, 3038, 3089, 3116 | `flobot2 = ((avhc * wetperm2 * strlen / sbdthk) * (strtop + enpt2 - sbot))` |
| 2857 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `flwmpt2 = flwmpt` |
| 2858 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flobot2 .GE. flowc + flwpet2) THEN` |
| 2859 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `flobot2 = flowc + flwpet2` |
| 2860 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `flwmpt2 = 0.5D0 * (flowc + flwpet2)` |
| 2869 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `depth1 = cdpth * (flwen1 ** fdpth)` |
| 2869 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `depth1 = cdpth * (flwen1 ** fdpth)` |
| 2870 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `width1 = awdth * (flwen1 ** bwdth)` |
| 2870 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `width1 = awdth * (flwen1 ** bwdth)` |
| 2891 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `depth2 = cdpth * (flwen2 ** fdpth)` |
| 2891 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `depth2 = cdpth * (flwen2 ** fdpth)` |
| 2892 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `width2 = awdth * (flwen2 ** bwdth)` |
| 2892 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `width2 = awdth * (flwen2 ** bwdth)` |
| 2901 | gwf2sfr7fm | uninitialized | loop-guarded | depth1 | defined at 2814, 2864, 2869, 2873, 2935, 2945, 2947, 2952, 2957, 2964, 3015, 3080, 3113 | `IF (depth1 .GT. NEARZERO) THEN` |
| 2902 | gwf2sfr7fm | uninitialized | loop-guarded | depth1 | defined at 2814, 2864, 2869, 2873, 2935, 2945, 2947, 2952, 2957, 2964, 3015, 3080, 3113 | `f1 = enpt1 - depth1` |
| 2911 | gwf2sfr7fm | uninitialized | loop-guarded | depth2 | defined at 2813, 2880, 2886, 2891, 2895, 2915, 2936, 2946, 2949, 2954, 2960, 2966, 2998, 3018, 3044, 3082, 3116 | `IF (depth2 .GT. NEARZERO) THEN` |
| 2912 | gwf2sfr7fm | uninitialized | loop-guarded | depth2 | defined at 2813, 2880, 2886, 2891, 2895, 2915, 2936, 2946, 2949, 2954, 2960, 2966, 2998, 3018, 3044, 3082, 3116 | `f2 = enpt2 - depth2` |
| 2913 | gwf2sfr7fm | uninitialized | loop-guarded | depth2 | defined at 2813, 2880, 2886, 2891, 2895, 2915, 2936, 2946, 2949, 2954, 2960, 2966, 2998, 3018, 3044, 3082, 3116 | `enpt2 = depth2` |
| 2947 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2639, 3617 | `flwmdpt1 = smooth(depth1, dwdh) * qcnst * (depth1 ** FIVE_THIRDS)` |
| 2949 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2639, 3617 | `flwmdpt2 = smooth(depth2, dwdh) * qcnst * (depth2 ** FIVE_THIRDS)` |
| 2971 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flobot1 .GE. flowc) THEN` |
| 2981 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `flobotp = flowc` |
| 2981 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `IF (0.5D0 * flobotp .GT. flwmpt) flobotp = flowc` |
| 2983 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `depthx = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** 0.6D0` |
| 2983 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2639, 3617 | `depthx = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** 0.6D0` |
| 2987 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `fhstr1 = (flwmpt - 0.5D0 * flobot1) - (flwmdpt1)` |
| 2988 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `fhstr2 = (flwmpt - 0.5D0 * flobot2) - (flwmdpt2)` |
| 3024 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `flwmdpt1 = (depth1 / cdpth) ** (1.0 / fdpth)` |
| 3024 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `flwmdpt1 = (depth1 / cdpth) ** (1.0 / fdpth)` |
| 3025 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `flwmdpt2 = (depth2 / cdpth) ** (1.0 / fdpth)` |
| 3025 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `flwmdpt2 = (depth2 / cdpth) ** (1.0 / fdpth)` |
| 3027 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `width1 = awdth * (flwmdpt1 ** bwdth)` |
| 3027 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `width1 = awdth * (flwmdpt1 ** bwdth)` |
| 3033 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt2 | defined at 2857, 2860 | `IF (flwmpt2 .GT. NEARZERO) THEN` |
| 3034 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `width2 = awdth * (flwmdpt2 ** bwdth)` |
| 3034 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `width2 = awdth * (flwmdpt2 ** bwdth)` |
| 3049 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `flwmdpta = (deptha / cdpth) ** (1.0 / fdpth)` |
| 3049 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `flwmdpta = (deptha / cdpth) ** (1.0 / fdpth)` |
| 3050 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `flwmdptb = (depthb / cdpth) ** (1.0 / fdpth)` |
| 3050 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `flwmdptb = (depthb / cdpth) ** (1.0 / fdpth)` |
| 3051 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `flwmdptc = (depthc / cdpth) ** (1.0 / fdpth)` |
| 3051 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `flwmdptc = (depthc / cdpth) ** (1.0 / fdpth)` |
| 3052 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `flwmdptd = (depthd / cdpth) ** (1.0 / fdpth)` |
| 3052 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `flwmdptd = (depthd / cdpth) ** (1.0 / fdpth)` |
| 3053 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `widtha = awdth * (flwmdpta ** bwdth)` |
| 3053 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `widtha = awdth * (flwmdpta ** bwdth)` |
| 3054 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `widthb = awdth * (flwmdptb ** bwdth)` |
| 3054 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `widthb = awdth * (flwmdptb ** bwdth)` |
| 3055 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `widthc = awdth * (flwmdptc ** bwdth)` |
| 3055 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `widthc = awdth * (flwmdptc ** bwdth)` |
| 3056 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `widthd = awdth * (flwmdptd ** bwdth)` |
| 3056 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `widthd = awdth * (flwmdptd ** bwdth)` |
| 3094 | gwf2sfr7fm | uninitialized | loop-guarded | deptha | defined at 2994, 2995, 3003, 3040, 3041, 3064, 3065, 3072 | `dlpp1 = (precip * (widtha - widthb)) / (deptha - depthb)` |
| 3094 | gwf2sfr7fm | uninitialized | loop-guarded | depthb | defined at 2996, 2997, 3006, 3042, 3043, 3066, 3067, 3074 | `dlpp1 = (precip * (widtha - widthb)) / (deptha - depthb)` |
| 3094 | gwf2sfr7fm | uninitialized | loop-guarded | widtha | defined at 3003, 3053, 3072, 3139 | `dlpp1 = (precip * (widtha - widthb)) / (deptha - depthb)` |
| 3094 | gwf2sfr7fm | uninitialized | loop-guarded | widthb | defined at 3006, 3054, 3074 | `dlpp1 = (precip * (widtha - widthb)) / (deptha - depthb)` |
| 3095 | gwf2sfr7fm | uninitialized | loop-guarded | depthc | defined at 2999, 3000, 3009, 3045, 3046, 3068, 3069, 3076 | `dlpp2 = (precip * (widthc - widthd)) / (depthc - depthd)` |
| 3095 | gwf2sfr7fm | uninitialized | loop-guarded | depthd | defined at 3001, 3002, 3012, 3047, 3048, 3070, 3071, 3078 | `dlpp2 = (precip * (widthc - widthd)) / (depthc - depthd)` |
| 3095 | gwf2sfr7fm | uninitialized | loop-guarded | widthc | defined at 3009, 3055, 3076 | `dlpp2 = (precip * (widthc - widthd)) / (depthc - depthd)` |
| 3095 | gwf2sfr7fm | uninitialized | loop-guarded | widthd | defined at 3012, 3056, 3078 | `dlpp2 = (precip * (widthc - widthd)) / (depthc - depthd)` |
| 3096 | gwf2sfr7fm | uninitialized | loop-guarded | deptha | defined at 2994, 2995, 3003, 3040, 3041, 3064, 3065, 3072 | `dlet1 = (etstr * (widtha - widthb)) / (deptha - depthb)` |
| 3096 | gwf2sfr7fm | uninitialized | loop-guarded | depthb | defined at 2996, 2997, 3006, 3042, 3043, 3066, 3067, 3074 | `dlet1 = (etstr * (widtha - widthb)) / (deptha - depthb)` |
| 3096 | gwf2sfr7fm | uninitialized | loop-guarded | widtha | defined at 3003, 3053, 3072, 3139 | `dlet1 = (etstr * (widtha - widthb)) / (deptha - depthb)` |
| 3096 | gwf2sfr7fm | uninitialized | loop-guarded | widthb | defined at 3006, 3054, 3074 | `dlet1 = (etstr * (widtha - widthb)) / (deptha - depthb)` |
| 3097 | gwf2sfr7fm | uninitialized | loop-guarded | depthc | defined at 2999, 3000, 3009, 3045, 3046, 3068, 3069, 3076 | `dlet2 = (etstr * (widthc - widthd)) / (depthc - depthd)` |
| 3097 | gwf2sfr7fm | uninitialized | loop-guarded | depthd | defined at 3001, 3002, 3012, 3047, 3048, 3070, 3071, 3078 | `dlet2 = (etstr * (widthc - widthd)) / (depthc - depthd)` |
| 3097 | gwf2sfr7fm | uninitialized | loop-guarded | widthc | defined at 3009, 3055, 3076 | `dlet2 = (etstr * (widthc - widthd)) / (depthc - depthd)` |
| 3097 | gwf2sfr7fm | uninitialized | loop-guarded | widthd | defined at 3012, 3056, 3078 | `dlet2 = (etstr * (widthc - widthd)) / (depthc - depthd)` |
| 3098 | gwf2sfr7fm | uninitialized | loop-guarded | deptha | defined at 2994, 2995, 3003, 3040, 3041, 3064, 3065, 3072 | `dlwp1 = (wetperma - wetpermb) / (deptha - depthb)` |
| 3098 | gwf2sfr7fm | uninitialized | loop-guarded | depthb | defined at 2996, 2997, 3006, 3042, 3043, 3066, 3067, 3074 | `dlwp1 = (wetperma - wetpermb) / (deptha - depthb)` |
| 3098 | gwf2sfr7fm | uninitialized | loop-guarded | wetperma | defined at 3003, 3057, 3084 | `dlwp1 = (wetperma - wetpermb) / (deptha - depthb)` |
| 3098 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermb | defined at 3006, 3058, 3085 | `dlwp1 = (wetperma - wetpermb) / (deptha - depthb)` |
| 3099 | gwf2sfr7fm | uninitialized | loop-guarded | depthc | defined at 2999, 3000, 3009, 3045, 3046, 3068, 3069, 3076 | `dlwp2 = (wetpermc - wetpermd) / (depthc - depthd)` |
| 3099 | gwf2sfr7fm | uninitialized | loop-guarded | depthd | defined at 3001, 3002, 3012, 3047, 3048, 3070, 3071, 3078 | `dlwp2 = (wetpermc - wetpermd) / (depthc - depthd)` |
| 3099 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermc | defined at 3009, 3059, 3086 | `dlwp2 = (wetpermc - wetpermd) / (depthc - depthd)` |
| 3099 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermd | defined at 3012, 3060, 3087 | `dlwp2 = (wetpermc - wetpermd) / (depthc - depthd)` |
| 3101 | gwf2sfr7fm | uninitialized | loop-guarded | width1 | defined at 2864, 2870, 2873, 2905, 2945, 2957, 3015, 3027, 3030, 3080 | `pp1 = precip * (width1) + dlpp1 * dlh` |
| 3102 | gwf2sfr7fm | uninitialized | loop-guarded | width2 | defined at 2820, 2826, 2829, 2833, 2881, 2886, 2892, 2895, 2916, 2946, 2960, 3018, 3034, 3037, 3082 | `pp2 = precip * (width2) + dlpp2 * dlh` |
| 3103 | gwf2sfr7fm | uninitialized | loop-guarded | width1 | defined at 2864, 2870, 2873, 2905, 2945, 2957, 3015, 3027, 3030, 3080 | `et1 = etstr * (width1) + dlet1 * dlh` |
| 3104 | gwf2sfr7fm | uninitialized | loop-guarded | width2 | defined at 2820, 2826, 2829, 2833, 2881, 2886, 2892, 2895, 2916, 2946, 2960, 3018, 3034, 3037, 3082 | `et2 = etstr * (width2) + dlet2 * dlh` |
| 3105 | gwf2sfr7fm | uninitialized | loop-guarded | wetperm1 | defined at 2864, 2871, 2906, 3015, 3028, 3031, 3088, 3113 | `cstr1 = ((wetperm1 + dlwp1 * dlh) * strleak) / sbdthk` |
| 3106 | gwf2sfr7fm | uninitialized | loop-guarded | wetperm2 | defined at 2820, 2827, 2830, 2835, 2849, 2882, 2886, 2893, 2917, 3018, 3035, 3038, 3089, 3116 | `cstr2 = ((wetperm2 + dlwp2 * dlh) * strleak) / sbdthk` |
| 3125 | gwf2sfr7fm | uninitialized | loop-guarded | width1 | defined at 2864, 2870, 2873, 2905, 2945, 2957, 3015, 3027, 3030, 3080 | `IF (width1 .GT. NEARZERO) THEN` |
| 3127 | gwf2sfr7fm | uninitialized | loop-guarded | width1 | defined at 2864, 2870, 2873, 2905, 2945, 2957, 3015, 3027, 3030, 3080 | `flwpet1 = precip * width1 + (dlpp1 * dlh) - etstr * width1 + (dlet1 * dlh)` |
| 3135 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flobot1 .GT. flowc + flwpet1) THEN` |
| 3143 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `flwx = (depthp / cdpth) ** (1.0 / fdpth)` |
| 3143 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `flwx = (depthp / cdpth) ** (1.0 / fdpth)` |
| 3145 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `widthp = awdth * (flwx ** bwdth)` |
| 3145 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `widthp = awdth * (flwx ** bwdth)` |
| 3156 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 3139, 3146, 3149, 3154, 3160, 3176, 3276, 3282, 3285, 3291, 3303, 3320, 3327, 3330, 3336, 3348 | `cstr1 = wetpermp * strleak / sbdthk` |
| 3167 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flobotp .GT. flowc + flwpet1) flobotp = flowc + flwpet1` |
| 3169 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `flwmpt = flwmpt + 0.5D0 * flwpet1` |
| 3180 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `depthx = cdpth * (flwx ** fdpth)` |
| 3180 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `depthx = cdpth * (flwx ** fdpth)` |
| 3182 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `widthx = awdth * (flwx ** bwdth)` |
| 3182 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `widthx = awdth * (flwx ** bwdth)` |
| 3192 | gwf2sfr7fm | uninitialized | loop-guarded | flwmdpt1 | defined at 2947, 3015, 3024, 3080 | `fhstr1 = (flwmpt - 0.5D0 * (pp1 - et1 + flobot1)) - (flwmdpt1)` |
| 3192 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `fhstr1 = (flwmpt - 0.5D0 * (pp1 - et1 + flobot1)) - (flwmdpt1)` |
| 3193 | gwf2sfr7fm | uninitialized | loop-guarded | flwmdpt2 | defined at 2949, 3018, 3025, 3082 | `fhstr2 = (flwmpt - 0.5D0 * (pp2 - et2 + flobot2)) - (flwmdpt2)` |
| 3193 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `fhstr2 = (flwmpt - 0.5D0 * (pp2 - et2 + flobot2)) - (flwmdpt2)` |
| 3265 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flobotp .GE. flowc) THEN` |
| 3266 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `flobotp = flowc` |
| 3267 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `depthp = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** .6D0` |
| 3267 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2639, 3617 | `depthp = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** .6D0` |
| 3272 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `depthx = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** 0.6D0` |
| 3272 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2639, 3617 | `depthx = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** 0.6D0` |
| 3279 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `flwp = (depthp / cdpth) ** (1.0 / fdpth)` |
| 3279 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `flwp = (depthp / cdpth) ** (1.0 / fdpth)` |
| 3281 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `widthp = awdth * (flwp ** bwdth)` |
| 3281 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `widthp = awdth * (flwp ** bwdth)` |
| 3300 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 3139, 3146, 3149, 3154, 3160, 3176, 3276, 3282, 3285, 3291, 3303, 3320, 3327, 3330, 3336, 3348 | `flobotp = ((avhc * wetpermp * strlen / sbdthk) * (strtop + depthp - h))` |
| 3308 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 3139, 3146, 3149, 3154, 3160, 3176, 3276, 3282, 3285, 3291, 3303, 3320, 3327, 3330, 3336, 3348 | `flobotp = ((avhc * wetpermp * strlen / sbdthk) * (strtop + depthp - sbot))` |
| 3311 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `flwmpt = flwmpt + 0.5D0 * flwpetp` |
| 3316 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flobotp .GT. flowc + flwpetp) THEN` |
| 3324 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `flwp = (depthp / cdpth) ** (1.0 / fdpth)` |
| 3324 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `flwp = (depthp / cdpth) ** (1.0 / fdpth)` |
| 3326 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `widthp = awdth * (flwp ** bwdth)` |
| 3326 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `widthp = awdth * (flwp ** bwdth)` |
| 3345 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 3139, 3146, 3149, 3154, 3160, 3176, 3276, 3282, 3285, 3291, 3303, 3320, 3327, 3330, 3336, 3348 | `flobotp = ((avhc * wetpermp * strlen / sbdthk) * (strtop + depthp - h))` |
| 3353 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 3139, 3146, 3149, 3154, 3160, 3176, 3276, 3282, 3285, 3291, 3303, 3320, 3327, 3330, 3336, 3348 | `flobotp = ((avhc * wetpermp * strlen / sbdthk) * (strtop + depthp - sbot))` |
| 3358 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flobotp .GE. flowc + flwpetp) flobotp = flowc + flwpetp` |
| 3372 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2526, 2641, 3617 | `depthx = cdpth * (flwx ** fdpth)` |
| 3372 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2527, 2642, 3617 | `depthx = cdpth * (flwx ** fdpth)` |
| 3373 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2643, 3617 | `widthx = awdth * (flwx ** bwdth)` |
| 3373 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2644, 3617 | `widthx = awdth * (flwx ** bwdth)` |
| 3416 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 3139, 3146, 3149, 3154, 3160, 3176, 3276, 3282, 3285, 3291, 3303, 3320, 3327, 3330, 3336, 3348 | `wetperm = wetpermp` |
| 3436 | gwf2sfr7fm | uninitialized | loop-guarded | errold | defined at 3458 | `WRITE(IOUT, 9003) istsg, nreach, Kkiter, err, errold` |
| 3445 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 3139, 3146, 3149, 3154, 3160, 3176, 3276, 3282, 3285, 3291, 3303, 3320, 3327, 3330, 3336, 3348 | `wetperm = wetpermp` |
| 3482 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2639, 3617 | `depth = (flwmpt / (smooth(depth, dwdh) * qcnst)) ** 0.6D0` |
| 3496 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `etstr = flowin + runof + runoff + precip - flobot` |
| 3524 | gwf2sfr7fm | uninitialized | loop-guarded | nstrpts | defined at 2455, 2532, 2755, 2833, 2873, 2895, 3072, 3074, 3076, 3078, 3080, 3082, 3152, 3185, 3288, 3333, 3376 | `width = QSTAGE((1 + 2 * nstrpts), istsg) + QSTAGE(3 * nstrpts, istsg) / 2.0D0` |
| 3547 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flowc .LT. NEARZERO) THEN` |
| 3584 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flowc .GT. NEARZERO .AND. icalccheck .EQ. 1) THEN` |
| 3600 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `IF (flobot .GE. flowc) flobot = flowc` |
| 3600 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `IF (flobot .GE. flowc) flobot = flowc` |
| 3611 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `IF (flobot .LT. 0.0D0) THEN` |
| 3612 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `fltest = qa + qb + qc + qlat * strlen - flobot` |
| 3636 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `flowot = flowc - flobot` |
| 3636 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `flowot = flowc - flobot` |
| 3637 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `qc = flowc` |
| 3641 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `flobot = flowc` |
| 3642 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `flwmpt = 0.5D0 * flowc` |
| 3648 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `SUMLEAK(l) = SUMLEAK(l) + (flobot * deltinc)` |
| 3651 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `SUMLEAK(l) = flobot` |
| 3659 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `STRM(11, l) = flobot` |
| 3719 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `SUMRCH(l) = SUMRCH(l) + flobot` |
| 3722 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `SUMRCH(l) = SUMRCH(l) + flobot` |
| 3729 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2702, 2706, 2711, 2712, 2724, 2730, 3169, 3311, 3356, 3420, 3427, 3448, 3454, 3477, 3479, 3529, 3534, 3642 | `SFRQ(1, l) = flwmpt` |
| 3730 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `SFRQ(2, l) = flowc` |
| 3731 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `SFRQ(3, l) = flobot` |
| 3736 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3413, 3442, 3550, 3552, 3574, 3575, 3577, 3578, 3581, 3587, 3600, 3617, 3641, 3691 | `SFRQ(3, l) = flobot` |
| 3758 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2704, 2710, 2713, 2725, 2726, 2760, 3418, 3425, 3446, 3453, 3476, 3500, 3527, 3532, 3572, 3627, 3685 | `ELSE IF (SUMLEAK(l) - flowc .LT. - CLOSEZERO) THEN` |
| 4347 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `flow = flowin + runof + runoff + precip - etstr` |
| 4347 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `flow = flowin + runof + runoff + precip - etstr` |
| 4353 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `IF (flowin + runoff + precip .LT. NEARZERO) THEN` |
| 4356 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `ELSE IF (runof .GE. flowin + runoff + precip - etstr) THEN` |
| 4356 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `ELSE IF (runof .GE. flowin + runoff + precip - etstr) THEN` |
| 4357 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `runof = flowin + runoff + precip - etstr` |
| 4357 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `runof = flowin + runoff + precip - etstr` |
| 4358 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `ELSE IF (etstr .GE. flowin + runoff + precip + runof) THEN` |
| 4358 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `ELSE IF (etstr .GE. flowin + runoff + precip + runof) THEN` |
| 4359 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `etstr = flowin + runoff + precip + runof` |
| 4361 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `ELSE IF (flowin + runof + runoff + precip .GT. NEARZERO) THEN` |
| 4362 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `etstr = flowin + runof + runoff + precip` |
| 4367 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `IF (flowin + runoff + precip - flobot .LT. NEARZERO) THEN` |
| 4370 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `ELSE IF (runof .GE. flowin + runoff + precip - flobot - etstr) THEN` |
| 4370 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `ELSE IF (runof .GE. flowin + runoff + precip - flobot - etstr) THEN` |
| 4372 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `runof = - (flowin + runoff + precip - flobot - etstr)` |
| 4372 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `runof = - (flowin + runoff + precip - flobot - etstr)` |
| 4373 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `ELSE IF (etstr .GE. flowin + runoff + precip - flobot + runof) THEN` |
| 4373 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `ELSE IF (etstr .GE. flowin + runoff + precip - flobot + runof) THEN` |
| 4374 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `etstr = flowin + runoff + precip - flobot + runof` |
| 4376 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `ELSE IF (etstr .GT. flowin + runoff + runof + precip - flobot) THEN` |
| 4376 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `ELSE IF (etstr .GT. flowin + runoff + runof + precip - flobot) THEN` |
| 4377 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `etstr = flowin + runof + runoff + precip - flobot` |
| 4378 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `ELSE IF (flowin + runoff + runof + precip - flobot .LT. NEARZERO) THEN` |
| 4382 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `flow = flowin + runof + runoff + precip - etstr` |
| 4382 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `flow = flowin + runof + runoff + precip - etstr` |
| 4390 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 4305, 4310, 4526 | `IF (h .LT. sbot) flobot = CALCUNSATFLOBOT(depth, avhc, fks, wetperm, sbdthk, areamax, strlen, fbc...` |
| 4400 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `qlat = (runof + runoff + precip - etstr) / strlen` |
| 4400 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `qlat = (runof + runoff + precip - etstr) / strlen` |
| 4441 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `qlat = (runof + runoff + precip - etstr) / strlen` |
| 4441 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `qlat = (runof + runoff + precip - etstr) / strlen` |
| 4464 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 4305, 4310, 4526 | `IF (h .LT. sbot) THEN` |
| 4494 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 4305, 4310, 4526 | `STRM(19, l) = h` |
| 4511 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `sfrbudg_in = sfrbudg_in + precip` |
| 4513 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `sfrbudg_out = sfrbudg_out + etstr` |
| 4556 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 4305, 4310, 4526 | `IF (icalccheck .EQ. 1 .AND. sbot .GT. h) THEN` |
| 4564 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 4305, 4310, 4526 | `ELSE IF (sbot .LT. h) THEN` |
| 4575 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `WRITE(IOUT, 9005) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SNG...` |
| 4575 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `WRITE(IOUT, 9005) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SNG...` |
| 4586 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 4034, 4037, 4052, 4761, 4764 | `WRITE(iout2, 9004) txtlst, Kkper, Kkstp` |
| 4588 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `WRITE(iout2, 9005) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4588 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 4034, 4037, 4052, 4761, 4764 | `WRITE(iout2, 9005) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4588 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `WRITE(iout2, 9005) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4603 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `WRITE(IOUT, 9007) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SNG...` |
| 4603 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `WRITE(IOUT, 9007) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SNG...` |
| 4617 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 4034, 4037, 4052, 4761, 4764 | `WRITE(iout2, 9006) txtlst, Kkper, Kkstp` |
| 4619 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `WRITE(iout2, 9007) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4619 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 4034, 4037, 4052, 4761, 4764 | `WRITE(iout2, 9007) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4619 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `WRITE(iout2, 9007) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4628 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 4034, 4037, 4052, 4761, 4764 | `WRITE(iout2, 9009) txtlst, Kkper, Kkstp` |
| 4630 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 4340, 4345, 4355, 4359, 4362, 4364, 4369, 4374, 4377, 4380 | `WRITE(iout2, 9010) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4630 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 4305, 4310, 4526 | `WRITE(iout2, 9010) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4630 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 4034, 4037, 4052, 4761, 4764 | `WRITE(iout2, 9010) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4630 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 4339, 4344 | `WRITE(iout2, 9010) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4723 | gwf2sfr7bd | uninitialized | loop-guarded | icalccheck | defined at 4251, 4256 | `IF (IBUDFL .GT. 0 .AND. icalccheck .EQ. 1) CALL GWF2SFR7UZOT(Kkstp, Kkper)` |
| 4863 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | roughch | defined at 4839, 4871, 4874 | `flwdlk2 = (CONST / roughch) * widthch * (dlkstr2 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 4863 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | slope | defined at 4838, 4871, 4874 | `flwdlk2 = (CONST / roughch) * widthch * (dlkstr2 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 4863 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | widthch | defined at 4840 | `flwdlk2 = (CONST / roughch) * widthch * (dlkstr2 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 4866 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | roughch | defined at 4839, 4871, 4874 | `SLKOTFLW(lk, istsg) = (CONST / roughch) * widthch * (dlkstr1 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 4866 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | slope | defined at 4838, 4871, 4874 | `SLKOTFLW(lk, istsg) = (CONST / roughch) * widthch * (dlkstr1 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 4866 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | widthch | defined at 4840 | `SLKOTFLW(lk, istsg) = (CONST / roughch) * widthch * (dlkstr1 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 5473 | gwf2sfr7flw | uninitialized | loop-guarded | xleft | defined at 5435, 5457 | `wtprm = DSQRT(((xleft - xright) * (xleft - xright)) + ((yleft - yright) * (yleft - yright)))` |
| 5473 | gwf2sfr7flw | uninitialized | loop-guarded | xright | defined at 5441, 5449, 5458 | `wtprm = DSQRT(((xleft - xright) * (xleft - xright)) + ((yleft - yright) * (yleft - yright)))` |
| 5473 | gwf2sfr7flw | uninitialized | loop-guarded | yleft | defined at 5436, 5456 | `wtprm = DSQRT(((xleft - xright) * (xleft - xright)) + ((yleft - yright) * (yleft - yright)))` |
| 5473 | gwf2sfr7flw | uninitialized | loop-guarded | yright | defined at 5442, 5448, 5459 | `wtprm = DSQRT(((xleft - xright) * (xleft - xright)) + ((yleft - yright) * (yleft - yright)))` |
| 6241 | sgwf2sfr7parmov | uninitialized | loop-guarded | jend | defined at 6235, 6237, 6239, 6248, 6250, 6252 | `DO jj = 6, jend` |
| 6254 | sgwf2sfr7parmov | uninitialized | loop-guarded | jend | defined at 6235, 6237, 6239, 6248, 6250, 6252 | `DO jj = 11, jend` |
| 8142 | leadwave | uninitialized | loop-guarded | checktime | defined at 8088, 8103, 8106, 8118, 8127, 8130, 8134, 8137, 8142 | `IF (checktime(j) .LT. NEARZERO) checktime(j) = big` |
| 8156 | leadwave | uninitialized | loop-guarded | checktime | defined at 8088, 8103, 8106, 8118, 8127, 8130, 8134, 8137, 8142 | `IF (CHECKTIME(j) .LE. shortest) THEN` |
| 8158 | leadwave | uninitialized | loop-guarded | checktime | defined at 8088, 8103, 8106, 8118, 8127, 8130, 8134, 8137, 8142 | `shortest = CHECKTIME(j)` |
| 8167 | leadwave | uninitialized | loop-guarded | checktime | defined at 8088, 8103, 8106, 8118, 8127, 8130, 8134, 8137, 8142 | `IF (CHECKTIME(k) > shortest) MORE(k) = 0` |
| 8274 | leadwave | uninitialized | loop-guarded | more | defined at 8089, 8157, 8167 | `IF (more(j) .EQ. 1) THEN` |
| 8704 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `chap = (XSEC(8 + mark(ll) - 1, Istsg) - XSEC(8 + mark(ll), Istsg))` |
| 8705 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `IF (ABS(XSEC(8 + mark(ll), Istsg) - XSEC(8 + mark(ll) - 1, Istsg)) .LT. 1.0E-30 .AND. ABS(XSEC(ma...` |
| 8711 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `ELSE IF (ABS(XSEC(8 + mark(ll), Istsg) - XSEC(8 + mark(ll) - 1, Istsg)) .LT. 1.0E-30) THEN` |
| 8714 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `ELSE IF (ABS(XSEC(mark(ll), Istsg) - XSEC(mark(ll) - 1, Istsg)) .LT. 1.0E-30) THEN` |
| 8718 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `slope = (XSEC(8 + mark(ll), Istsg) - XSEC(8 + mark(ll) - 1, Istsg)) / (XSEC(mark(ll), Istsg) - XS...` |
| 8722 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `ffmin = XSEC(8 + mark(ll), Istsg)` |
| 8723 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `ffmax = XSEC(8 + mark(ll) - 1, Istsg)` |
| 8725 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `ffmin = XSEC(8 + mark(ll) - 1, Istsg)` |
| 8726 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `ffmax = XSEC(8 + mark(ll), Istsg)` |
| 8728 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `b = XSEC(8 + mark(ll) - 1, Istsg) - slope * XSEC(mark(ll) - 1, Istsg)` |
| 8732 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `area1 = (XSEC(mark(ll), Istsg) - XSEC(mark(ll) - 1, Istsg)) * (stage - ffmin)` |
| 8738 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `xinc = (XSEC(mark(ll), Istsg) - XSEC(mark(ll) - 1, Istsg)) / 50.` |
| 8739 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `xmid = XSEC(mark(ll) - 1, Istsg)` |
| 8745 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `IF (XSEC(8 + mark(ll) - 1, Istsg) .LT. XSEC(8 + mark(ll), Istsg)) THEN` |
| 8747 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `xinc = (ABS(XSEC(mark(ll) - 1, Istsg) - xmid)) / 50.` |
| 8748 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `xmid = XSEC(mark(ll) - 1, Istsg)` |
| 8750 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `xinc = (ABS(XSEC(mark(ll), Istsg) - xmid)) / 50.` |
| 8755 | channelarea | uninitialized | loop-guarded | mark | defined at 8697 | `xx = ABS(xmid - XSEC(mark(ll), Istsg))` |

### gwf2str7.f90 (28)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 486 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 445, 470, 474, 478, 482 | `XNUM = ((FLOWIN + STRM(9, L)) / 2.0) * STRM(8, L)` |
| 495 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 445, 470, 474, 478, 482 | `IF (FLOWIN .LE. 0.) HSTR = STRM(5, L)` |
| 511 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 445, 470, 474, 478, 482 | `IF (FLOBOT .LE. FLOWIN) GO TO 320` |
| 513 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 445, 470, 474, 478, 482 | `FLOBOT = FLOWIN` |
| 517 | gwf2str7fm | uninitialized | loop-guarded | flobot | defined at 502, 508, 513, 516 | `FLOWOT = FLOWIN - FLOBOT` |
| 517 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 445, 470, 474, 478, 482 | `FLOWOT = FLOWIN - FLOBOT` |
| 518 | gwf2str7fm | uninitialized | loop-guarded | iflg | defined at 449 | `STRM(9, LL) = ARTRIB(IFLG)` |
| 522 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 445, 470, 474, 478, 482 | `STRM(10, L) = FLOWIN` |
| 523 | gwf2str7fm | uninitialized | loop-guarded | flobot | defined at 502, 508, 513, 516 | `STRM(11, L) = FLOBOT` |
| 529 | gwf2str7fm | uninitialized | loop-guarded | flobot | defined at 502, 508, 513, 516 | `IF ((FLOWIN .LE. 0.0) .AND. (FLOBOT .GE. 0.0)) GO TO 500` |
| 529 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 445, 470, 474, 478, 482 | `IF ((FLOWIN .LE. 0.0) .AND. (FLOBOT .GE. 0.0)) GO TO 500` |
| 532 | gwf2str7fm | uninitialized | loop-guarded | iqflg | defined at 505, 507, 512 | `IF (IQFLG .GT. 0) GO TO 400` |
| 533 | gwf2str7fm | uninitialized | loop-guarded | cstr | defined at 496 | `RHS(IC, IR, IL) = RHS(IC, IR, IL) - CSTR * HSTR` |
| 534 | gwf2str7fm | uninitialized | loop-guarded | cstr | defined at 496 | `HCOF(IC, IR, IL) = HCOF(IC, IR, IL) - CSTR` |
| 538 | gwf2str7fm | uninitialized | loop-guarded | flobot | defined at 502, 508, 513, 516 | `RHS(IC, IR, IL) = RHS(IC, IR, IL) - FLOBOT` |
| 691 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 650, 675, 679, 683, 687 | `XNUM = ((FLOWIN + STRM(9, L)) / 2.0) * STRM(8, L)` |
| 700 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 650, 675, 679, 683, 687 | `IF (FLOWIN .LE. 0.0) HSTR = STRM(5, L)` |
| 714 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 650, 675, 679, 683, 687 | `IF (FLOBOT .LE. FLOWIN) GO TO 320` |
| 715 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 650, 675, 679, 683, 687 | `FLOBOT = FLOWIN` |
| 719 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 707, 711, 715, 718, 742 | `FLOWOT = FLOWIN - FLOBOT` |
| 719 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 650, 675, 679, 683, 687 | `FLOWOT = FLOWIN - FLOBOT` |
| 720 | gwf2str7bd | uninitialized | loop-guarded | iflg | defined at 654 | `STRM(9, LL) = ARTRIB(IFLG)` |
| 724 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 650, 675, 679, 683, 687 | `STRM(10, L) = FLOWIN` |
| 725 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 707, 711, 715, 718, 742 | `STRM(11, L) = FLOBOT` |
| 728 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 707, 711, 715, 718, 742 | `BUFF(IC, IR, IL) = BUFF(IC, IR, IL) + FLOBOT` |
| 731 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 707, 711, 715, 718, 742 | `IF (FLOBOT .LT. 0.) THEN` |
| 734 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 707, 711, 715, 718, 742 | `RATOUT = RATOUT - FLOBOT` |
| 738 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 707, 711, 715, 718, 742 | `RATIN = RATIN + FLOBOT` |

### gwf2sub7.f90 (3)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 1359 | gwf2sub7ot | uninitialized | loop-guarded | nend | defined at 1352, 1371, 1516 | `CALL ULASAV(SUB(LOC2 : NEND), TEXT(3), KSTP, KPER, PERTIM, TOTIM, NCOL, NROW, KQ, ISBOCU(3))` |
| 1378 | gwf2sub7ot | uninitialized | loop-guarded | nend | defined at 1352, 1371, 1516 | `CALL ULASAV(DCOM(LOC2 : NEND), TEXT(4), KSTP, KPER, PERTIM, TOTIM, NCOL, NROW, KQ, ISBOCU(3))` |
| 1523 | gwf2sub7ot | uninitialized | loop-guarded | nend | defined at 1352, 1371, 1516 | `CALL ULASAV(HC(LOC2 : NEND), TEXT(6), KSTP, KPER, PERTIM, TOTIM, NCOL, NROW, K, ISBOCU(5))` |

### gwf2swi27.F90 (4)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 4389 | sswi2_imix | uninitialized | loop-guarded | izl | defined at 4378, 4384 | `IF (izu .GT. 0 .AND. izl .GT. 0) THEN` |
| 4389 | sswi2_imix | uninitialized | loop-guarded | izu | defined at 4372, 4387 | `IF (izu .GT. 0 .AND. izl .GT. 0) THEN` |
| 4390 | sswi2_imix | uninitialized | loop-guarded | izu | defined at 4372, 4387 | `A(j, i, k, izu) = A(j, i, k, izu) - qzbot * switfact` |
| 4391 | sswi2_imix | uninitialized | loop-guarded | izl | defined at 4378, 4384 | `A(j, i, k + 1, izl) = A(j, i, k + 1, izl) + qzbot * switfact` |

### gwf2swr7.f90 (83)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 2065 | gwf2swr7ar | aliasing | global-aliasing | ntmax | argument 1 of sswr_allo_soln, which also assigns that module variable directly | `CALL SSWR_ALLO_SOLN(NTMAX, 0)` |
| 2866 | gwf2swr7rp | uninitialized | loop-guarded | cbnd | defined at 2860, 2862, 2864 | `WRITE(IOUT, 2082) i, REACH(i) % ISWRBND, ADJUSTL(cbnd)` |
| 3081 | gwf2swr7rp | uninitialized | loop-guarded | getextd | defined at 2998, 3027 | `WRITE(creach(8), 2110) getextd` |
| 3433 | gwf2swr7rp | uninitialized | loop-guarded | rbot | defined at 3418, 3421 | `REACH(istrrch) % STRUCT(istrnum) % STRINV = rbot` |
| 3434 | gwf2swr7rp | uninitialized | loop-guarded | dlen | defined at 3419, 3422 | `REACH(istrrch) % STRUCT(istrnum) % STRWID = dlen` |
| 3718 | gwf2swr7rp | uninitialized | call-assumed | istrnum | defined at 3202, 3218, 4190 | `ival = REACH(istrrch) % STRUCT(istrnum) % ISTRTAB` |
| 3718 | gwf2swr7rp | uninitialized | call-assumed | istrrch | defined at 3197, 3218, 4188 | `ival = REACH(istrrch) % STRUCT(istrnum) % ISTRTAB` |
| 3743 | gwf2swr7rp | uninitialized | loop-guarded | cstruct | defined at 3611, 3643, 3645, 3647, 3649, 3651, 3660, 3662, 3679, 3681, 3683, 3694, 3696, 3698, 3709, 3711, 3713, 3722, 3724, 3726, 3747, 3770, 3773, 3775, 3783, 3785, 3793, 3832, 3836, 3892, 3894 | `WRITE(cstruct(1), 2110) REACH(i) % STRUCT(j) % STRELEV(istrpts)` |
| 3745 | gwf2swr7rp | uninitialized | loop-guarded | cstruct | defined at 3611, 3643, 3645, 3647, 3649, 3651, 3660, 3662, 3679, 3681, 3683, 3694, 3696, 3698, 3709, 3711, 3713, 3722, 3724, 3726, 3747, 3770, 3773, 3775, 3783, 3785, 3793, 3832, 3836, 3892, 3894 | `WRITE(cstruct(2), 2110) REACH(i) % STRUCT(j) % STRQ(istrpts)` |
| 3898 | gwf2swr7rp | uninitialized | loop-guarded | cstruct | defined at 3611, 3643, 3645, 3647, 3649, 3651, 3660, 3662, 3679, 3681, 3683, 3694, 3696, 3698, 3709, 3711, 3713, 3722, 3724, 3726, 3747, 3770, 3773, 3775, 3783, 3785, 3793, 3832, 3836, 3892, 3894 | `WRITE(IOUT, 4110) i, j, cstruct(1), indx` |
| 4802 | gwf2swr7fm | uninitialized | loop-guarded | dt | defined at 4796, 4798, 4802 | `dt = dt * TSMULT(Kkper)` |
| 5320 | gwf2swr7fm | uninitialized | loop-guarded | irch | defined at 4968 | `ge = REACH(irch) % CURRENT % QPOTGWET * dtscale` |
| 5323 | gwf2swr7fm | uninitialized | loop-guarded | irch | defined at 4968 | `getextd = REACH(irch) % GETEXTD` |
| 5339 | gwf2swr7fm | uninitialized | loop-guarded | h | defined at 5231, 5286, 5288, 5330 | `IF (h .GE. REACH(i) % GBELEV) THEN` |
| 5343 | gwf2swr7fm | uninitialized | loop-guarded | h | defined at 5231, 5286, 5288, 5330 | `ELSE IF (h .GE. (REACH(i) % GBELEV - getextd)) THEN` |
| 5954 | gwf2swr7bd | uninitialized | loop-guarded | h | defined at 5794, 5799, 5942 | `IF (h .GE. REACH(irch) % GBELEV) THEN` |
| 5958 | gwf2swr7bd | uninitialized | loop-guarded | h | defined at 5794, 5799, 5942 | `ELSE IF (h .GE. (REACH(irch) % GBELEV - getextd)) THEN` |
| 5962 | gwf2swr7bd | uninitialized | loop-guarded | h | defined at 5794, 5799, 5942 | `qq = h * hhcof + rrhs` |
| 6797 | sswr_sort | uninitialized | conditional | istack | defined at 6828, 6829, 6832, 6833 | `r = istack(jstack)` |
| 6798 | sswr_sort | uninitialized | conditional | istack | defined at 6828, 6829, 6832, 6833 | `l = istack(jstack - 1)` |
| 6802 | sswr_sort | aliasing | aliasing | v | passed as arguments 1, 2 of sswr_swap; the callee writes dummy a | `CALL SSWR_SWAP(V(k), V(l + 1))` |
| 6803 | sswr_sort | aliasing | aliasing | v | passed as arguments 1, 2 of sswr_mswap; the callee writes dummy a | `CALL SSWR_MSWAP(V(l), V(r), V(l) .GT. V(r))` |
| 6804 | sswr_sort | aliasing | aliasing | v | passed as arguments 1, 2 of sswr_mswap; the callee writes dummy a | `CALL SSWR_MSWAP(V(l + 1), V(r), V(l + 1) .GT. V(r))` |
| 6805 | sswr_sort | aliasing | aliasing | v | passed as arguments 1, 2 of sswr_mswap; the callee writes dummy a | `CALL SSWR_MSWAP(V(l), V(l + 1), V(l) .GT. V(l + 1))` |
| 6819 | sswr_sort | aliasing | aliasing | v | passed as arguments 1, 2 of sswr_swap; the callee writes dummy a | `CALL SSWR_SWAP(V(i), V(j))` |
| 8019 | sswr_set_rchoff | uninitialized | loop-guarded | s | defined at 8000, 8012 | `smin = MAXVAL(s) + DONE` |
| 8025 | sswr_set_rchoff | uninitialized | loop-guarded | s | defined at 8000, 8012 | `IF (s(irch) .LE. smin) THEN` |
| 8027 | sswr_set_rchoff | uninitialized | loop-guarded | s | defined at 8000, 8012 | `smin = s(irch)` |
| 8039 | sswr_set_rchoff | uninitialized | loop-guarded | s | defined at 8000, 8012 | `REACH(i) % OFFSET = s(i) - smin` |
| 8197 | sswr_calc_rchgeodata | uninitialized | conditional | bottom | defined at 8164, 8169, 8176, 8183 | `IF (zg .GT. bottom) THEN` |
| 8198 | sswr_calc_rchgeodata | uninitialized | conditional | bottom | defined at 8164, 8169, 8176, 8183 | `dz = (zg - bottom + 1.0D-6) / 10.0D0` |
| 8201 | sswr_calc_rchgeodata | uninitialized | conditional | bottom | defined at 8164, 8169, 8176, 8183 | `uz(1) = bottom` |
| 8202 | sswr_calc_rchgeodata | uninitialized | conditional | bottom | defined at 8164, 8169, 8176, 8183 | `uz(2) = bottom + 1.0D-6` |
| 8272 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8162, 8181 | `wp0 = MAX(REACH(irch) % GEO % WETPER(ipos - 1), width)` |
| 8273 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8162, 8181 | `tw0 = MAX(REACH(irch) % GEO % TOPWID(ipos - 1), width)` |
| 8274 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8162, 8181 | `sa0 = MAX(REACH(irch) % GEO % SAREA(ipos - 1), width * length)` |
| 8385 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8162, 8181 | `REACH(irch) % GEO % WETPER = width` |
| 8386 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8162, 8181 | `REACH(irch) % GEO % TOPWID = width` |
| 8389 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8162, 8181 | `REACH(irch) % GEO % SAREA = width * length` |
| 8391 | sswr_calc_rchgeodata | uninitialized | conditional | bottom | defined at 8164, 8169, 8176, 8183 | `z1 = uz(ipos) - bottom` |
| 8392 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8162, 8181 | `REACH(irch) % GEO % XAREA(ipos) = width * z1` |
| 8393 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8162, 8181 | `REACH(irch) % GEO % VOL(ipos) = length * width * z1` |
| 8478 | sswr_set_rchlay | uninitialized | loop-guarded | kbot | defined at 8474 | `REACH(irch) % LAYEND = kbot` |
| 8952 | sswr_gsolwrp | uninitialized | loop-guarded | ptcfn0 | defined at 8928, 8956 | `PTCDEL = PTCDEL * ptcfn0 / fn` |
| 9062 | sswr_gsolwrp | uninitialized | call-assumed | icnvg | defined at 9009, 9015, 9023, 9039 | `IF (icnvg .LT. 0) EXIT OUTER` |
| 9126 | sswr_gsolwrp | uninitialized | loop-guarded | diagmin | defined at 8918, 8923 | `ratio = (DONE / ptcdel) / diagmin` |
| 10303 | sswr_p_qaqflow | uninitialized | conditional | mxactr | defined at 10290, 10293, 10295 | `WRITE(iriv, 2020) mxactr, 0` |
| 10383 | sswr_p_qaqflow | uninitialized | conditional | itmp | defined at 10308, 10312 | `WRITE(iriv, 2030) itmp, 0, Kper, Kstp, n, swrtot` |
| 11762 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11733, 11735, 11738, 11740, 11742, 11752, 11762 | `cond = cond * fact` |
| 11776 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11733, 11735, 11738, 11740, 11742, 11752, 11762 | `value = value - cond * hd` |
| 11782 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11733, 11735, 11738, 11740, 11742, 11752, 11762 | `Rch % CURRENTQAQ(k) % QAQFLOW = cond * hd` |
| 11783 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11733, 11735, 11738, 11740, 11742, 11752, 11762 | `Rch % CURRENTQAQ(k) % CONDUCTANCE = cond` |
| 11786 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11733, 11735, 11738, 11740, 11742, 11752, 11762 | `Rch % CURRENT % QAQFLOW = Rch % CURRENT % QAQFLOW - cond * hd` |
| 11791 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11733, 11735, 11738, 11740, 11742, 11752, 11762 | `rh = cond * hd` |
| 11794 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11733, 11735, 11738, 11740, 11742, 11752, 11762 | `rh = cond * trs` |
| 11795 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11733, 11735, 11738, 11740, 11742, 11752, 11762 | `hc = cond` |
| 11948 | sswr_calc_mfqaq | uninitialized | loop-guarded | cond | defined at 11923, 11925, 11927, 11929, 11938, 11948 | `cond = cond * fact` |
| 11962 | sswr_calc_mfqaq | uninitialized | loop-guarded | cond | defined at 11923, 11925, 11927, 11929, 11938, 11948 | `value = value - cond * hd` |
| 11968 | sswr_calc_mfqaq | uninitialized | loop-guarded | cond | defined at 11923, 11925, 11927, 11929, 11938, 11948 | `Rch % CURRENTQAQ(k) % QAQFLOW = cond * hd` |
| 11969 | sswr_calc_mfqaq | uninitialized | loop-guarded | cond | defined at 11923, 11925, 11927, 11929, 11938, 11948 | `Rch % CURRENTQAQ(k) % CONDUCTANCE = cond` |
| 12029 | sswr_calc_sflow | uninitialized | loop-guarded | iseg | defined at 12022 | `SEG(2, iseg) = qsfr` |
| 12731 | swr_calc_strvals | uninitialized | loop-guarded | cval | defined at 12661, 12664, 12666, 12677, 12680, 12683, 12684 | `cl1 = cval` |
| 12733 | swr_calc_strvals | uninitialized | loop-guarded | cval | defined at 12661, 12664, 12666, 12677, 12680, 12683, 12684 | `cl2 = cval` |
| 12737 | swr_calc_strvals | uninitialized | loop-guarded | cval | defined at 12661, 12664, 12666, 12677, 12680, 12683, 12684 | `cr1 = cval` |
| 12739 | swr_calc_strvals | uninitialized | loop-guarded | cval | defined at 12661, 12664, 12666, 12677, 12680, 12683, 12684 | `cr2 = cval` |
| 12746 | swr_calc_strvals | uninitialized | loop-guarded | cl1 | defined at 12731, 12736 | `IF (cl1 .LT. cr1) THEN` |
| 12746 | swr_calc_strvals | uninitialized | loop-guarded | cr1 | defined at 12732, 12737 | `IF (cl1 .LT. cr1) THEN` |
| 12749 | swr_calc_strvals | uninitialized | loop-guarded | cl2 | defined at 12733, 12738 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12749 | swr_calc_strvals | uninitialized | loop-guarded | cr2 | defined at 12734, 12739 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12758 | swr_calc_strvals | uninitialized | loop-guarded | cl1 | defined at 12731, 12736 | `IF (cl1 .LT. cr1) THEN` |
| 12758 | swr_calc_strvals | uninitialized | loop-guarded | cr1 | defined at 12732, 12737 | `IF (cl1 .LT. cr1) THEN` |
| 12761 | swr_calc_strvals | uninitialized | loop-guarded | cl2 | defined at 12733, 12738 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12761 | swr_calc_strvals | uninitialized | loop-guarded | cr2 | defined at 12734, 12739 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12769 | swr_calc_strvals | uninitialized | loop-guarded | cl1 | defined at 12731, 12736 | `IF (cl1 .LT. cr1) THEN` |
| 12769 | swr_calc_strvals | uninitialized | loop-guarded | cr1 | defined at 12732, 12737 | `IF (cl1 .LT. cr1) THEN` |
| 12774 | swr_calc_strvals | uninitialized | loop-guarded | cl2 | defined at 12733, 12738 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12774 | swr_calc_strvals | uninitialized | loop-guarded | cr2 | defined at 12734, 12739 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12789 | swr_calc_strvals | uninitialized | loop-guarded | gt | defined at 12706, 12710, 12714, 12718, 12741, 12748, 12751, 12756, 12772, 12777 | `REACH(irch) % STRUCT(nn) % STRTOP = gt` |
| 12790 | swr_calc_strvals | uninitialized | loop-guarded | gb | defined at 12707, 12711, 12715, 12719, 12742, 12753, 12760, 12763, 12767 | `REACH(irch) % STRUCT(nn) % STRBOT = gb` |
| 13759 | sswrbtbm | uninitialized | loop-guarded | pd | defined at 13764, 13766, 13768, 13773 | `pe = pd` |
| 14579 | sswr_sflow | uninitialized | conditional | q | defined at 14457, 14493, 14499, 14502, 14505, 14509, 14512, 14513, 14535, 14539, 14540, 14544, 14548, 14549, 14552, 14556, 14557, 14560, 14564, 14565, 14568, 14572, 14573, 14576 | `value = q` |
| 15131 | sswr_pcnvg | uninitialized | loop-guarded | mfdiff | defined at 15125, 15126, 15129 | `IF (mfdiff .GT. bfdiffmax) THEN` |
| 15133 | sswr_pcnvg | uninitialized | loop-guarded | mfdiff | defined at 15125, 15126, 15129 | `bfdiffmax = mfdiff` |

### gwf2swr7util.f90 (21)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 103 | gsol_full_ludcap | uninitialized | loop-guarded | npiv | defined at 98 | `IF (n .NE. npiv) THEN` |
| 105 | gsol_full_ludcap | uninitialized | loop-guarded | npiv | defined at 98 | `t = AU(npiv, i)` |
| 106 | gsol_full_ludcap | uninitialized | loop-guarded | npiv | defined at 98 | `AU(npiv, i) = AU(n, i)` |
| 109 | gsol_full_ludcap | uninitialized | loop-guarded | npiv | defined at 98 | `S(npiv) = S(n)` |
| 111 | gsol_full_ludcap | uninitialized | loop-guarded | npiv | defined at 98 | `PINDEX(n) = npiv` |
| 440 | gsol_cgap | uninitialized | loop-guarded | rho0 | defined at 474 | `beta = rho / rho0` |
| 441 | gsol_cgap | aliasing | aliasing | p | passed as arguments 5, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, Z, beta, P, P)` |
| 454 | gsol_cgap | aliasing | aliasing | t | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, T, alpha, P, T)` |
| 455 | gsol_cgap | aliasing | aliasing | x | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, X, DONE, T, X)` |
| 466 | gsol_cgap | aliasing | aliasing | d | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, D, - alpha, Q, D)` |
| 598 | gsol_bcgsap | uninitialized | loop-guarded | alpha0 | defined at 677 | `beta = (rho / rho0) * (alpha0 / omega0)` |
| 598 | gsol_bcgsap | uninitialized | loop-guarded | omega0 | defined at 678 | `beta = (rho / rho0) * (alpha0 / omega0)` |
| 598 | gsol_bcgsap | uninitialized | loop-guarded | rho0 | defined at 676 | `beta = (rho / rho0) * (alpha0 / omega0)` |
| 602 | gsol_bcgsap | uninitialized | loop-guarded | omega | defined at 644, 647 | `CALL GSOL_AXPY(NCORESV, NR, P, - omega, V, P)` |
| 602 | gsol_bcgsap | aliasing | aliasing | p | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, P, - omega, V, P)` |
| 603 | gsol_bcgsap | aliasing | aliasing | p | passed as arguments 5, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, D, beta, P, P)` |
| 628 | gsol_bcgsap | aliasing | aliasing | x | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, X, alpha, PHAT, X)` |
| 647 | gsol_bcgsap | aliasing | aliasing | d | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, D, omega, SHAT, D)` |
| 648 | gsol_bcgsap | aliasing | aliasing | d | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, D, alpha, PHAT, D)` |
| 649 | gsol_bcgsap | aliasing | aliasing | x | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, X, DONE, D, X)` |
| 3397 | i4vec_reverse | aliasing | aliasing | a | passed as arguments 1, 2 of i4_swap; the callee writes dummy i | `CALL i4_swap(a(i), a(n + 1 - i))` |

### gwf2uzf1.f90 (140)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 930 | gwf2uzf1ar | uninitialized | loop-guarded | iuzlay | defined at 922 | `WRITE(igunit, 9024) igage, iuzrow, iuzcol, iuzlay` |
| 934 | gwf2uzf1ar | uninitialized | loop-guarded | iuzlay | defined at 922 | `WRITE(igunit, 9025) igage, iuzrow, iuzcol, iuzlay` |
| 938 | gwf2uzf1ar | uninitialized | loop-guarded | iuzlay | defined at 922 | `WRITE(igunit, 9026) igage, iuzrow, iuzcol, iuzlay` |
| 1197 | parseuzfoptions | uninitialized | conditional | iostat | defined at 1064 | `IF (Iostat .NE. 0) THEN` |
| 2130 | gwf2uzf1fm | uninitialized | loop-guarded | thr | defined at 2105, 2176 | `UZTHST(iwav, l) = thr` |
| 2876 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `UZTHST(1, l) = thr` |
| 2952 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `UZTHST(iset, l) = thr` |
| 2960 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `UZTHST(ii, l) = thr` |
| 3005 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `UZSTOR(ic, ir) = UZDPST(1, l) * (UZTHST(1, l) - thr) * cellarea` |
| 3097 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = (UZTHST(jm1, l) - thr) / (ths - thr)` |
| 3097 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = (UZTHST(jm1, l) - thr) / (ths - thr)` |
| 3102 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 3102 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 3102 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 3105 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `UZSPST(jm1, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3105 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `UZSPST(jm1, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3105 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `UZSPST(jm1, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3108 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(j - 2, l) - thr) / (ths - thr)) ** epsilon` |
| 3108 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(j - 2, l) - thr) / (ths - thr)) ** epsilon` |
| 3108 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(j - 2, l) - thr) / (ths - thr)) ** epsilon` |
| 3112 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 3112 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 3112 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 3126 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = (UZTHST(k, l) - thr) / (ths - thr)` |
| 3126 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = (UZTHST(k, l) - thr) / (ths - thr)` |
| 3130 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3130 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3130 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3134 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3134 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3134 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3138 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 3138 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 3138 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 3143 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3143 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3143 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3162 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = (UZTHST(k, l) - thr) / (ths - thr)` |
| 3162 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = (UZTHST(k, l) - thr) / (ths - thr)` |
| 3166 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3166 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3166 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3169 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3169 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3169 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3172 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 3172 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 3172 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 3176 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3176 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3176 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3194 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3194 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3194 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3197 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3197 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3197 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 3200 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 3200 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 3200 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 3204 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2815, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3204 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3204 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2816, 2935, 3030, 3382 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 3223 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3228 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * UZDPST(k, l)` |
| 3232 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3235 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3240 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(j, l) - thr) * (UZDPST(j, l) - UZDPST(j + 1, l))` |
| 3245 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(iset + NWAVST(ic, ir) - 1, l) - thr) * UZDPST(iset + NWAVST(ic, ir) - 1, l)` |
| 3260 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3265 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * UZDPST(k, l)` |
| 3269 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3272 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3277 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(j, l) - thr) * (UZDPST(j, l) - UZDPST(j + 1, l))` |
| 3282 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(iset + NWAVST(ic, ir) - 1, l) - thr) * UZDPST(iset + NWAVST(ic, ir) - 1, l)` |
| 3302 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3307 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * UZDPST(k, l)` |
| 3311 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3314 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3319 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(j, l) - thr) * (UZDPST(j, l) - UZDPST(j + 1, l))` |
| 3324 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(iset + NWAVST(ic, ir) - 1, l) - thr) * UZDPST(iset + NWAVST(ic, ir) - 1, l)` |
| 3371 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `UZTHST(1, l) = thr` |
| 3399 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `IF (UZTHST(iset, l) .GT. thr .OR. NWAVST(ic, ir) .GT. 1) ick = 1` |
| 3410 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3415 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * UZDPST(k, l)` |
| 3419 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3422 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3427 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(j, l) - thr) * (UZDPST(j, l) - UZDPST(j + 1, l))` |
| 3432 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2814, 2935, 3030, 3382, 3561, 4144 | `fm = fm + (UZTHST(iset + NWAVST(ic, ir) - 1, l) - thr) * UZDPST(iset + NWAVST(ic, ir) - 1, l)` |
| 4119 | gwf2uzf1bd | uninitialized | loop-guarded | gcumapl | defined at 4095 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 4119 | gwf2uzf1bd | uninitialized | loop-guarded | gcumin | defined at 4096 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 4119 | gwf2uzf1bd | uninitialized | loop-guarded | gcumrch | defined at 4097 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 4119 | gwf2uzf1bd | uninitialized | loop-guarded | gdelstor | defined at 4098 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 4119 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 4094 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 4119 | gwf2uzf1bd | uninitialized | loop-guarded | ghnw | defined at 4092 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 4119 | gwf2uzf1bd | uninitialized | loop-guarded | gseep | defined at 4107 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 4119 | gwf2uzf1bd | uninitialized | loop-guarded | guzstore | defined at 4104 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | gaplinfltr | defined at 4101 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | gcumapl | defined at 4095 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | gcumin | defined at 4096 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | gcumrch | defined at 4097 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | gdelstor | defined at 4098 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | gdlstr | defined at 4106 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 4094 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | ghnw | defined at 4092 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | ginfltr | defined at 4099 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | grchr | defined at 4105 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | gseep | defined at 4107 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | gseepr | defined at 4108 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4124 | gwf2uzf1bd | uninitialized | loop-guarded | guzstore | defined at 4104 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 4142 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 4094 | `IF (nuzr .EQ. iuzrow .AND. nuzc .EQ. iuzcol .AND. ghdif .GT. 0.0) THEN` |
| 4145 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 4094 | `depthinc = ghdif / 40.001D0` |
| 4150 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 4094 | `DO WHILE (depthsave - ghdif .LT. CLOSEZERO)` |
| 4175 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 4094 | `IF (avdpt .GE. ghdif - depthinc) THEN` |
| 4177 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 4094 | `avdpt = ghdif` |
| 4184 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 4094 | `WRITE(iftunit, 9013) il, TOTIM, ghnw, ghdif, avdpt, avwat` |
| 4184 | gwf2uzf1bd | uninitialized | loop-guarded | ghnw | defined at 4092 | `WRITE(iftunit, 9013) il, TOTIM, ghnw, ghdif, avdpt, avwat` |
| 5311 | transpiration | uninitialized | loop-guarded | fm | defined at 5664, 5667, 5669, 5675, 5734, 5743, 5746, 5749, 5752 | `FACTOR = FACTOR / (FM / PET)` |
| 5453 | transpiration | uninitialized | loop-guarded | diff | defined at 5432 | `IF (ABS(diff) .GT. feps) THEN` |
| 5678 | transpiration | uninitialized | loop-guarded | depth2 | defined at 5289 | `Depth(ii) = depth2(ii)` |
| 5679 | transpiration | uninitialized | loop-guarded | theta2 | defined at 5290 | `Theta(ii) = theta2(ii)` |
| 5680 | transpiration | uninitialized | loop-guarded | flux2 | defined at 5291 | `Flux(ii) = flux2(ii)` |
| 5681 | transpiration | uninitialized | loop-guarded | speed2 | defined at 5292 | `Speed(ii) = speed2(ii)` |
| 5682 | transpiration | uninitialized | loop-guarded | ltrail2 | defined at 5293 | `Ltrail(ii) = ltrail2(ii)` |
| 5683 | transpiration | uninitialized | loop-guarded | itrwave2 | defined at 5294 | `Itrwave(ii) = itrwave2(ii)` |
| 5690 | transpiration | uninitialized | loop-guarded | depth2 | defined at 5289 | `Depth(ii) = depth2(ii)` |
| 5691 | transpiration | uninitialized | loop-guarded | theta2 | defined at 5290 | `Theta(ii) = theta2(ii)` |
| 5692 | transpiration | uninitialized | loop-guarded | flux2 | defined at 5291 | `Flux(ii) = flux2(ii)` |
| 5693 | transpiration | uninitialized | loop-guarded | speed2 | defined at 5292 | `Speed(ii) = speed2(ii)` |
| 5694 | transpiration | uninitialized | loop-guarded | ltrail2 | defined at 5293 | `Ltrail(ii) = ltrail2(ii)` |
| 5695 | transpiration | uninitialized | loop-guarded | itrwave2 | defined at 5294 | `Itrwave(ii) = itrwave2(ii)` |
| 5739 | transpiration | uninitialized | loop-guarded | depth2 | defined at 5289 | `IF (Depth2(jk) - depthsave .LT. 0.0D0) jj = jk` |
| 5743 | transpiration | uninitialized | loop-guarded | depth2 | defined at 5289 | `fm = fm + (Theta2(jj - 1) - Thetar) * (depthsave - Depth2(jj))` |
| 5743 | transpiration | uninitialized | loop-guarded | theta2 | defined at 5290 | `fm = fm + (Theta2(jj - 1) - Thetar) * (depthsave - Depth2(jj))` |
| 5746 | transpiration | uninitialized | loop-guarded | depth2 | defined at 5289 | `fm = fm + (Theta2(j) - Thetar) * (Depth2(j) - Depth2(j + 1))` |
| 5746 | transpiration | uninitialized | loop-guarded | theta2 | defined at 5290 | `fm = fm + (Theta2(j) - Thetar) * (Depth2(j) - Depth2(j + 1))` |
| 5749 | transpiration | uninitialized | loop-guarded | depth2 | defined at 5289 | `fm = fm + (Theta2(Nwv) - Thetar) * Depth2(Nwv)` |
| 5749 | transpiration | uninitialized | loop-guarded | theta2 | defined at 5290 | `fm = fm + (Theta2(Nwv) - Thetar) * Depth2(Nwv)` |
| 5752 | transpiration | uninitialized | loop-guarded | theta2 | defined at 5290 | `fm = fm + (Theta2(Nwv) - Thetar) * depthsave` |
| 5958 | caph | uninitialized | result-unset | caph | some RETURN path never assigns the function result | `` |

### hydprograms/hydfmt.f90 (71)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 390 | hydfmt | uninitialized | conditional | ist | defined at 223 | `IDATE = IDATE + IST` |
| 392 | hydfmt | uninitialized | conditional | nc | defined at 348, 353 | `DO 89 ii = 1, NC` |
| 393 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `IF (id(ii) .GT. 0) icnt(id(ii)) = icnt(id(ii)) + 1` |
| 394 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `IF (id(ii) .EQ. 1) THEN` |
| 395 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `zh(icnt(id(ii))) = Z(JCOL(ii))` |
| 395 | hydfmt | uninitialized | conditional | jcol | defined at 350, 358 | `zh(icnt(id(ii))) = Z(JCOL(ii))` |
| 395 | hydfmt | uninitialized | conditional | z | defined at 377, 383 | `zh(icnt(id(ii))) = Z(JCOL(ii))` |
| 396 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `ELSE IF (id(ii) .EQ. 2) THEN` |
| 397 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `zhd(icnt(id(ii))) = Z(JCOL(ii))` |
| 397 | hydfmt | uninitialized | conditional | jcol | defined at 350, 358 | `zhd(icnt(id(ii))) = Z(JCOL(ii))` |
| 397 | hydfmt | uninitialized | conditional | z | defined at 377, 383 | `zhd(icnt(id(ii))) = Z(JCOL(ii))` |
| 398 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `ELSE IF (id(ii) .EQ. 3) THEN` |
| 399 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `zhph(icnt(id(ii))) = Z(JCOL(ii))` |
| 399 | hydfmt | uninitialized | conditional | jcol | defined at 350, 358 | `zhph(icnt(id(ii))) = Z(JCOL(ii))` |
| 399 | hydfmt | uninitialized | conditional | z | defined at 377, 383 | `zhph(icnt(id(ii))) = Z(JCOL(ii))` |
| 400 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `ELSE IF (id(ii) .EQ. 4) THEN` |
| 401 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `zhc(icnt(id(ii))) = Z(JCOL(ii))` |
| 401 | hydfmt | uninitialized | conditional | jcol | defined at 350, 358 | `zhc(icnt(id(ii))) = Z(JCOL(ii))` |
| 401 | hydfmt | uninitialized | conditional | z | defined at 377, 383 | `zhc(icnt(id(ii))) = Z(JCOL(ii))` |
| 402 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `ELSE IF (id(ii) .EQ. 5) THEN` |
| 403 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `zhs(icnt(id(ii))) = Z(JCOL(ii))` |
| 403 | hydfmt | uninitialized | conditional | jcol | defined at 350, 358 | `zhs(icnt(id(ii))) = Z(JCOL(ii))` |
| 403 | hydfmt | uninitialized | conditional | z | defined at 377, 383 | `zhs(icnt(id(ii))) = Z(JCOL(ii))` |
| 404 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `ELSE IF (id(ii) .EQ. 6) THEN` |
| 405 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `zhf(icnt(id(ii))) = Z(JCOL(ii))` |
| 405 | hydfmt | uninitialized | conditional | jcol | defined at 350, 358 | `zhf(icnt(id(ii))) = Z(JCOL(ii))` |
| 405 | hydfmt | uninitialized | conditional | z | defined at 377, 383 | `zhf(icnt(id(ii))) = Z(JCOL(ii))` |
| 406 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `ELSE IF (id(ii) .EQ. 7) THEN` |
| 407 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `zfi(icnt(id(ii))) = Z(JCOL(ii))` |
| 407 | hydfmt | uninitialized | conditional | jcol | defined at 350, 358 | `zfi(icnt(id(ii))) = Z(JCOL(ii))` |
| 407 | hydfmt | uninitialized | conditional | z | defined at 377, 383 | `zfi(icnt(id(ii))) = Z(JCOL(ii))` |
| 408 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `ELSE IF (id(ii) .EQ. 8) THEN` |
| 409 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `zfo(icnt(id(ii))) = Z(JCOL(ii))` |
| 409 | hydfmt | uninitialized | conditional | jcol | defined at 350, 358 | `zfo(icnt(id(ii))) = Z(JCOL(ii))` |
| 409 | hydfmt | uninitialized | conditional | z | defined at 377, 383 | `zfo(icnt(id(ii))) = Z(JCOL(ii))` |
| 410 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `ELSE IF (id(ii) .EQ. 9) THEN` |
| 411 | hydfmt | uninitialized | loop-guarded | id | defined at 248, 252, 256, 260, 264, 268, 272, 276, 280 | `zfa(icnt(id(ii))) = Z(JCOL(ii))` |
| 411 | hydfmt | uninitialized | conditional | jcol | defined at 350, 358 | `zfa(icnt(id(ii))) = Z(JCOL(ii))` |
| 411 | hydfmt | uninitialized | conditional | z | defined at 377, 383 | `zfa(icnt(id(ii))) = Z(JCOL(ii))` |
| 424 | hydfmt | uninitialized | loop-guarded | zh | defined at 395 | `WRITE(nu(1), *) WELLIDH(N), ',', IDATE, ',', ZH(N)` |
| 428 | hydfmt | uninitialized | loop-guarded | zhd | defined at 397 | `WRITE(nu(2), *) WELLIDD(N), ',', IDATE, ',', ZHD(N)` |
| 432 | hydfmt | uninitialized | loop-guarded | zhph | defined at 399 | `WRITE(nu(3), *) WELLIDCH(N), ',', IDATE, ',', ZHPH(N)` |
| 436 | hydfmt | uninitialized | loop-guarded | zhc | defined at 401 | `WRITE(nu(4), *) WELLIDC(N), ',', IDATE, ',', ZHC(N)` |
| 440 | hydfmt | uninitialized | loop-guarded | zhs | defined at 403 | `WRITE(nu(4), *) WELLIDS(N), ',', IDATE, ',', ZHS(N)` |
| 444 | hydfmt | uninitialized | loop-guarded | zhf | defined at 405 | `WRITE(nu(6), *) WELLIDHF(N), ',', IDATE, ',', ZHF(N)` |
| 448 | hydfmt | uninitialized | loop-guarded | zfi | defined at 407 | `WRITE(nu(7), *) WELLIDFI(N), ',', IDATE, ',', ZFI(N)` |
| 452 | hydfmt | uninitialized | loop-guarded | zfo | defined at 409 | `WRITE(nu(8), *) WELLIDFO(N), ',', IDATE, ',', ZFO(N)` |
| 456 | hydfmt | uninitialized | loop-guarded | zfa | defined at 411 | `WRITE(nu(9), *) WELLIDFA(N), ',', IDATE, ',', ZFA(N)` |
| 460 | hydfmt | uninitialized | loop-guarded | zh | defined at 395 | `WRITE(nu(1), FMT1) IDATE, (ZH(N), N = 1, numhh)` |
| 461 | hydfmt | uninitialized | loop-guarded | zhd | defined at 397 | `WRITE(nu(2), FMT1) IDATE, (ZHD(N), N = 1, numhd)` |
| 462 | hydfmt | uninitialized | loop-guarded | zhph | defined at 399 | `WRITE(nu(3), FMT1) IDATE, (ZHPH(N), N = 1, numch)` |
| 463 | hydfmt | uninitialized | loop-guarded | zhc | defined at 401 | `WRITE(nu(4), FMT1) IDATE, (ZHC(N), N = 1, numhc)` |
| 464 | hydfmt | uninitialized | loop-guarded | zhs | defined at 403 | `WRITE(nu(5), FMT1) IDATE, (ZHS(N), N = 1, numhs)` |
| 465 | hydfmt | uninitialized | loop-guarded | zhf | defined at 405 | `WRITE(nu(6), FMT1) IDATE, (ZHF(N), N = 1, numhhf)` |
| 466 | hydfmt | uninitialized | loop-guarded | zfi | defined at 407 | `WRITE(nu(7), FMT1) IDATE, (ZFI(N), N = 1, numhfi)` |
| 467 | hydfmt | uninitialized | loop-guarded | zfo | defined at 409 | `WRITE(nu(8), FMT1) IDATE, (ZFO(N), N = 1, numhfo)` |
| 468 | hydfmt | uninitialized | loop-guarded | zfa | defined at 411 | `WRITE(nu(9), FMT1) IDATE, (ZFA(N), N = 1, numhfa)` |
| 471 | hydfmt | uninitialized | loop-guarded | zh | defined at 395 | `WRITE(nu(1), FMT1) TIME, (ZH(N), N = 1, numhh)` |
| 472 | hydfmt | uninitialized | loop-guarded | zhd | defined at 397 | `WRITE(nu(2), FMT1) TIME, (ZHD(N), N = 1, numhd)` |
| 473 | hydfmt | uninitialized | loop-guarded | zhph | defined at 399 | `WRITE(nu(3), FMT1) TIME, (ZHPH(N), N = 1, numch)` |
| 474 | hydfmt | uninitialized | loop-guarded | zhc | defined at 401 | `WRITE(nu(4), FMT1) TIME, (ZHC(N), N = 1, numhc)` |
| 475 | hydfmt | uninitialized | loop-guarded | zhs | defined at 403 | `WRITE(nu(5), FMT1) TIME, (ZHS(N), N = 1, numhs)` |
| 476 | hydfmt | uninitialized | loop-guarded | zhf | defined at 405 | `WRITE(nu(6), FMT1) TIME, (ZHF(N), N = 1, numhhf)` |
| 477 | hydfmt | uninitialized | loop-guarded | zfi | defined at 407 | `WRITE(nu(7), FMT1) TIME, (ZFI(N), N = 1, numhfi)` |
| 478 | hydfmt | uninitialized | loop-guarded | zfo | defined at 409 | `WRITE(nu(8), FMT1) TIME, (ZFO(N), N = 1, numhfo)` |
| 479 | hydfmt | uninitialized | loop-guarded | zfa | defined at 411 | `WRITE(nu(9), FMT1) TIME, (ZFA(N), N = 1, numhfa)` |
| 564 | modtime | uninitialized | conditional | deltim | defined at 554, 556, 558, 560, 562, 591, 593, 595, 597, 599, 603, 605, 607, 609, 611, 615, 617, 619, 621, 623 | `ITIME = TOTIM / DELTIM` |
| 565 | modtime | uninitialized | conditional | deltim | defined at 554, 556, 558, 560, 562, 591, 593, 595, 597, 599, 603, 605, 607, 609, 611, 615, 617, 619, 621, 623 | `REMTIM = (TOTIM / DELTIM) - INT(TOTIM / DELTIM) + REMTIM` |
| 565 | modtime | uninitialized | conditional | remtim | defined at 536, 565, 567 | `REMTIM = (TOTIM / DELTIM) - INT(TOTIM / DELTIM) + REMTIM` |
| 625 | modtime | uninitialized | conditional | deltim | defined at 554, 556, 558, 560, 562, 591, 593, 595, 597, 599, 603, 605, 607, 609, 611, 615, 617, 619, 621, 623 | `TOTIM = (TOTIM / DELTIM) + START` |
| 632 | modtime | uninitialized | conditional | deltim | defined at 554, 556, 558, 560, 562, 591, 593, 595, 597, 599, 603, 605, 607, 609, 611, 615, 617, 619, 621, 623 | `TOTIM = TOTIM / DELTIM` |

### lmt8.f90 (42)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 261 | lmt8bas7ar | uninitialized | loop-guarded | mtmnw1 | defined at 231 | `IF (MTMNW1 .NE. 0) MTMNW = MTMNW1` |
| 262 | lmt8bas7ar | uninitialized | loop-guarded | mtmnw2 | defined at 235 | `IF (MTMNW2 .NE. 0) MTMNW = MTMNW2` |
| 1994 | lmt8huf7 | uninitialized | call-assumed | dfl | defined at 1766, 1810, 1981 | `X1 = - DFL` |
| 2004 | lmt8huf7 | uninitialized | call-assumed | dfr | defined at 1766, 1810, 1981 | `X2 = DFR` |
| 2014 | lmt8huf7 | uninitialized | call-assumed | dft | defined at 1766, 1810, 1981 | `X3 = - DFT` |
| 2024 | lmt8huf7 | uninitialized | call-assumed | dfb | defined at 1766, 1810, 1981 | `X4 = DFB` |
| 2318 | lmt8riv7 | uninitialized | loop-guarded | rate | defined at 2295, 2310, 2313 | `WRITE(IUMT3D) IL, IR, IC, RATE` |
| 2320 | lmt8riv7 | uninitialized | loop-guarded | rate | defined at 2295, 2310, 2313 | `WRITE(IUMT3D, *) IL, IR, IC, RATE` |
| 2791 | lmt8res7 | uninitialized | loop-guarded | rate | defined at 2785, 2788, 2824 | `BUFF(IC, IR, IL) = BUFF(IC, IR, IL) + RATE` |
| 3193 | lmt8ets7 | uninitialized | loop-guarded | petm2 | defined at 3177, 3180 | `HHCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |
| 3193 | lmt8ets7 | uninitialized | loop-guarded | pxdp2 | defined at 3176, 3179 | `HHCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |
| 3345 | lmt8drt7 | uninitialized | loop-guarded | icr | defined at 3306 | `WRITE(IUMT3D) ILR, IRR, ICR, QIN, mhost, QSW` |
| 3345 | lmt8drt7 | uninitialized | loop-guarded | irr | defined at 3305 | `WRITE(IUMT3D) ILR, IRR, ICR, QIN, mhost, QSW` |
| 3345 | lmt8drt7 | uninitialized | loop-guarded | qin | defined at 3303, 3329 | `WRITE(IUMT3D) ILR, IRR, ICR, QIN, mhost, QSW` |
| 3347 | lmt8drt7 | uninitialized | loop-guarded | icr | defined at 3306 | `WRITE(IUMT3D, *) ILR, IRR, ICR, QIN, mhost, QSW` |
| 3347 | lmt8drt7 | uninitialized | loop-guarded | irr | defined at 3305 | `WRITE(IUMT3D, *) ILR, IRR, ICR, QIN, mhost, QSW` |
| 3347 | lmt8drt7 | uninitialized | loop-guarded | qin | defined at 3303, 3329 | `WRITE(IUMT3D, *) ILR, IRR, ICR, QIN, mhost, QSW` |
| 3573 | lmt8uzf1gw | uninitialized | loop-guarded | iuzfrch | defined at 3524, 3535, 3537, 3552, 3555 | `WRITE(IUMT3D) ((IUZFRCH(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3575 | lmt8uzf1gw | uninitialized | loop-guarded | iuzfrch | defined at 3524, 3535, 3537, 3552, 3555 | `WRITE(IUMT3D, *) ((IUZFRCH(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3635 | lmt8uzf1gw | uninitialized | loop-guarded | igwet | defined at 3607, 3625 | `WRITE(IUMT3D) ((IGWET(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3640 | lmt8uzf1gw | uninitialized | loop-guarded | igwet | defined at 3607, 3625 | `WRITE(IUMT3D, *) ((IGWET(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3939 | lmt8uzfet | uninitialized | loop-guarded | igwet | defined at 3911, 3929 | `WRITE(IUMT3D) ((IGWET(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3944 | lmt8uzfet | uninitialized | loop-guarded | igwet | defined at 3911, 3929 | `WRITE(IUMT3D, *) ((IGWET(J, I), J = 1, NCOL), I = 1, NROW)` |
| 4430 | lmt8sfr2 | uninitialized | conditional | text | defined at 4405, 4408, 4410, 4478, 4480 | `WRITE(IUMT3D) KPER, KSTP, NCOL, NROW, NLAY, TEXT, NSTRM` |
| 4433 | lmt8sfr2 | uninitialized | conditional | text | defined at 4405, 4408, 4410, 4478, 4480 | `WRITE(IUMT3D, *) TEXT, NSTRM` |
| 4485 | lmt8sfr2 | uninitialized | conditional | text | defined at 4405, 4408, 4410, 4478, 4480 | `WRITE(IUMT3D) KPER, KSTP, TEXT, NSTRM, NFLOWTYPE, NINTOT` |
| 4488 | lmt8sfr2 | uninitialized | conditional | text | defined at 4405, 4408, 4410, 4478, 4480 | `WRITE(IUMT3D, *) TEXT, NSTRM, NFLOWTYPE, NINTOT` |
| 4563 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `SFRFLOWVAL(I : I + LENGTH, :) = SFRFLOWVAL((I + 1) : USED, :)` |
| 4573 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `WRITE(IUMT3D) SFRFLOWVAL(1, L)` |
| 4575 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `WRITE(IUMT3D, *) SFRFLOWVAL(1, L)` |
| 4581 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `WRITE(IUMT3D) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L)` |
| 4583 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `WRITE(IUMT3D, *) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L)` |
| 4589 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `WRITE(IUMT3D) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L)` |
| 4592 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `WRITE(IUMT3D, *) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L)` |
| 4599 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `WRITE(IUMT3D) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L), SFRFLOWVAL(4, L)` |
| 4602 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `WRITE(IUMT3D, *) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L), SFRFLOWVAL(4, L)` |
| 4609 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `WRITE(IUMT3D) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L), SFRFLOWVAL(4, L), SFRFLOWVAL(...` |
| 4613 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 4550, 4551, 4552, 4553, 4554, 4563 | `WRITE(IUMT3D, *) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L), SFRFLOWVAL(4, L), SFRFLOWV...` |
| 4727 | lmt8sfr2 | uninitialized | conditional | i | defined at 4560, 4716, 4721, 4741, 4788, 4793 | `WRITE(IUMT3D) I, L, IDISP, FLOWIN, XSA` |
| 4729 | lmt8sfr2 | uninitialized | conditional | i | defined at 4560, 4716, 4721, 4741, 4788, 4793 | `WRITE(IUMT3D, *) I, L, IDISP, FLOWIN, XSA` |
| 4972 | lmt8lak3 | uninitialized | conditional | text | defined at 4965, 4967, 4994 | `WRITE(IUMT3D) KPER, KSTP, NCOL, NROW, NLAY, TEXT, LKNODE` |
| 4975 | lmt8lak3 | uninitialized | conditional | text | defined at 4965, 4967, 4994 | `WRITE(IUMT3D, *) TEXT, LKNODE` |

### mf2005.f90 (8)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 374 | main | aliasing | global-aliasing | cc | argument 4 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 374 | main | aliasing | global-aliasing | cr | argument 3 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 374 | main | aliasing | global-aliasing | cv | argument 5 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 374 | main | aliasing | global-aliasing | hcof | argument 6 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 374 | main | aliasing | global-aliasing | hnew | argument 1 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 374 | main | aliasing | global-aliasing | ibound | argument 7 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 374 | main | aliasing | global-aliasing | rhs | argument 2 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 385 | main | uninitialized | call-assumed | icnvg | defined at 332, 339, 348, 365, 374, 381, 392, 508, 512 | `IF (ICNVG .EQ. 1) GO TO 33` |

### obs2bas7.f90 (48)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 823 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `A = 1 / (DC * DR)` |
| 823 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `A = 1 / (DC * DR)` |
| 828 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(1) = 0.5 * (1. - DRF / DR)` |
| 828 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(1) = 0.5 * (1. - DRF / DR)` |
| 829 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(2) = 0.5 * DRF / DR` |
| 829 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(2) = 0.5 * DRF / DR` |
| 835 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(1) = 0.5 * (1. - DCF / DC)` |
| 835 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(1) = 0.5 * (1. - DCF / DC)` |
| 837 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(3) = 0.5 * DCF / DC` |
| 837 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(3) = 0.5 * DCF / DC` |
| 842 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(3) = A * (DR - DRF) * DCF` |
| 842 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(3) = A * (DR - DRF) * DCF` |
| 842 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(3) = A * (DR - DRF) * DCF` |
| 843 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(4) = A * DRF * DCF` |
| 843 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(4) = A * DRF * DCF` |
| 844 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(2) = A * DRF * (DC - DCF)` |
| 844 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(2) = A * DRF * (DC - DCF)` |
| 844 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(2) = A * DRF * (DC - DCF)` |
| 845 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(1) = A * (DR - DRF) * (DC - DCF)` |
| 845 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(1) = A * (DR - DRF) * (DC - DCF)` |
| 845 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(1) = A * (DR - DRF) * (DC - DCF)` |
| 845 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(1) = A * (DR - DRF) * (DC - DCF)` |
| 849 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(1) = A * (DR * DC - DR * DCF)` |
| 849 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(1) = A * (DR * DC - DR * DCF)` |
| 849 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(1) = A * (DR * DC - DR * DCF)` |
| 851 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(3) = A * (DR * DCF - DC * DRF)` |
| 851 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(3) = A * (DR * DCF - DC * DRF)` |
| 851 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(3) = A * (DR * DCF - DC * DRF)` |
| 851 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(3) = A * (DR * DCF - DC * DRF)` |
| 852 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(4) = A * (DC * DRF)` |
| 852 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(4) = A * (DC * DRF)` |
| 855 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(1) = A * (DR * DC - DC * DRF)` |
| 855 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(1) = A * (DR * DC - DC * DRF)` |
| 855 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(1) = A * (DR * DC - DC * DRF)` |
| 856 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(4) = A * (DR * DCF)` |
| 856 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(4) = A * (DR * DCF)` |
| 857 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(2) = A * (DC * DRF - DR * DCF)` |
| 857 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(2) = A * (DC * DRF - DR * DCF)` |
| 857 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(2) = A * (DC * DRF - DR * DCF)` |
| 857 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(2) = A * (DC * DRF - DR * DCF)` |
| 861 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(1) = A * (DR * DC - DC * DRF - DR * DCF)` |
| 861 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(1) = A * (DR * DC - DC * DRF - DR * DCF)` |
| 861 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(1) = A * (DR * DC - DC * DRF - DR * DCF)` |
| 861 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(1) = A * (DR * DC - DC * DRF - DR * DCF)` |
| 862 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 817 | `RINT(3) = A * (DR * DCF)` |
| 862 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 820 | `RINT(3) = A * (DR * DCF)` |
| 863 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 816 | `RINT(2) = A * (DC * DRF)` |
| 863 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 821 | `RINT(2) = A * (DC * DRF)` |

### pcg7.f90 (15)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 751 | pcg7ap | uninitialized | loop-guarded | hhcof | defined at 539, 563, 611, 612, 748, 750, 986 | `CD(N) = (DONE + DEL) * HHCOF - CDCR - CDCC - CDCV - RELAX * (FCR + FCC + FCV)` |
| 865 | pcg7ap | uninitialized | loop-guarded | pn | defined at 857, 858, 874, 875 | `BHNEW = B * (P(NRL) - PN)` |
| 866 | pcg7ap | uninitialized | loop-guarded | pn | defined at 857, 858, 874, 875 | `HHNEW = H * (P(NRN) - PN)` |
| 867 | pcg7ap | uninitialized | loop-guarded | pn | defined at 857, 858, 874, 875 | `DHNEW = D * (P(NCL) - PN)` |
| 868 | pcg7ap | uninitialized | loop-guarded | pn | defined at 857, 858, 874, 875 | `FHNEW = F * (P(NCN) - PN)` |
| 869 | pcg7ap | uninitialized | loop-guarded | pn | defined at 857, 858, 874, 875 | `ZHNEW = Z * (P(NLL) - PN)` |
| 870 | pcg7ap | uninitialized | loop-guarded | pn | defined at 857, 858, 874, 875 | `SHNEW = S * (P(NLN) - PN)` |
| 939 | pcg7ap | uninitialized | loop-guarded | nh | defined at 918 | `BIGH = BIGH / SQRT(- HCOF(NH))` |
| 940 | pcg7ap | uninitialized | loop-guarded | nr | defined at 785, 930 | `BIGR = BIGR * SQRT(- HCOF(NR))` |
| 963 | pcg7ap | uninitialized | loop-guarded | kh | defined at 917 | `LHCH(1, II) = KH` |
| 964 | pcg7ap | uninitialized | loop-guarded | ih | defined at 915 | `LHCH(2, II) = IH` |
| 965 | pcg7ap | uninitialized | loop-guarded | jh | defined at 916 | `LHCH(3, II) = JH` |
| 968 | pcg7ap | uninitialized | loop-guarded | kr | defined at 929 | `LRCH(1, II) = KR` |
| 969 | pcg7ap | uninitialized | loop-guarded | ir | defined at 681, 927 | `LRCH(2, II) = IR` |
| 970 | pcg7ap | uninitialized | loop-guarded | jr | defined at 928 | `LRCH(3, II) = JR` |

### pcgn2.f90 (23)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 178 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `READ(UNIT = DATA_STRING(1), FMT = 400, IOSTAT = IOS) ITER_MO, ITER_MI, CLOSE_R, CLOSE_H` |
| 181 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `WRITE(IOUT, 800) 'TER_MO, ITER_MI, CLOSE_R, CLOSE_H', DATA_STRING(1)` |
| 185 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `READ(UNIT = DATA_STRING(2), FMT = 405, IOSTAT = IOS) RELAX, IFILL, UNIT_PC, UNIT_TS` |
| 188 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `WRITE(IOUT, 800) 'RELAX, IFILL, UNIT_PC, UNIT_TS', DATA_STRING(2)` |
| 194 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `READ(UNIT = DATA_STRING(3), FMT = 410, IOSTAT = IOS) ADAMP, DAMP, DAMP_LB, RATE_D, CHGLIMIT` |
| 197 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `WRITE(IOUT, 800) 'ADAMP, DAMP, DAMP_LB, RATE_D, CHGLIMIT', DATA_STRING(3)` |
| 203 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `READ(UNIT = DATA_STRING(4), FMT = 415, IOSTAT = IOS) ACNVG, CNVG_LB, MCNVG, RATE_C, IPUNIT` |
| 206 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `WRITE(IOUT, 800) 'ACNVG, CNVG_LB, MCNVG, RATE_C, IPUNIT', DATA_STRING(4)` |
| 217 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `READ(UNIT = DATA_STRING(1), FMT = *, IOSTAT = IOS) ITER_MO, ITER_MI, CLOSE_R, CLOSE_H` |
| 220 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `WRITE(IOUT, 800) 'TER_MO,ITER_MI,CLOSE_R,CLOSE_H', DATA_STRING(1)` |
| 223 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `READ(UNIT = DATA_STRING(2), FMT = *, IOSTAT = IOS) RELAX, IFILL, UNIT_PC, UNIT_TS` |
| 226 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `WRITE(IOUT, 800) 'RELAX, IFILL, UNIT_PC, UNIT_TS', DATA_STRING(2)` |
| 231 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `READ(UNIT = DATA_STRING(3), FMT = *, IOSTAT = IOS) ADAMP, DAMP, DAMP_LB, RATE_D, CHGLIMIT` |
| 234 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `WRITE(IOUT, 800) 'ADAMP, DAMP, DAMP_LB, RATE_D, CHGLIMIT', DATA_STRING(3)` |
| 239 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `READ(UNIT = DATA_STRING(4), FMT = *, IOSTAT = IOS) ACNVG, CNVG_LB, MCNVG, RATE_C, IPUNIT` |
| 242 | pcgn2ar | uninitialized | conditional | data_string | defined at 170 | `WRITE(IOUT, 800) 'ACNVG, CNVG_LB, MCNVG, RATE_C, IPUNIT', DATA_STRING(4)` |
| 1153 | max_hch | uninitialized | loop-guarded | node_save | defined at 1149 | `MHC_NODE = NODE_SAVE` |
| 1509 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NODE), CK_D(NCN))` |
| 1511 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NCN), CK_D(NODE))` |
| 1523 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NODE), CK_D(NRL))` |
| 1525 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NRL), CK_D(NODE))` |
| 1532 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NODE), CK_D(NLL))` |
| 1534 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NLL), CK_D(NODE))` |

### pcgn_solve2.f90 (1)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 2002 | pcg | uninitialized | conditional | start_time | defined at 1914 | `solv_time = elapsed_time(2) - start_time` |

### utl7.f90 (39)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 609 | u1drel | uninitialized | conditional | cnstnt | defined at 590, 596 | `A(J) = CNSTNT` |
| 610 | u1drel | uninitialized | conditional | cnstnt | defined at 590, 596 | `WRITE(IOUT, 3) ANAME, CNSTNT` |
| 616 | u1drel | uninitialized | conditional | fmtin | defined at 590, 599 | `WRITE(IOUT, 5) ANAME, LOCAT, FMTIN` |
| 619 | u1drel | uninitialized | conditional | fmtin | defined at 590, 599 | `IF (FMTIN .EQ. '(FREE)') THEN` |
| 622 | u1drel | uninitialized | conditional | fmtin | defined at 590, 599 | `READ(LOCAT, FMTIN) (A(J), J = 1, JJ)` |
| 628 | u1drel | uninitialized | conditional | cnstnt | defined at 590, 596 | `IF (CNSTNT .EQ. ZERO) GO TO 120` |
| 630 | u1drel | uninitialized | conditional | cnstnt | defined at 590, 596 | `A(J) = A(J) * CNSTNT` |
| 634 | u1drel | uninitialized | conditional | iprn | defined at 590, 600 | `IF (IPRN .EQ. 0) THEN` |
| 637 | u1drel | uninitialized | conditional | iprn | defined at 590, 600 | `ELSE IF (IPRN .GT. 0) THEN` |
| 735 | u2dint | uninitialized | conditional | fname | defined at 713 | `OPEN(UNIT = LOCAT, FILE = FNAME, FORM = FORM, ACCESS = ACCESS, ACTION = ACTION(1))` |
| 738 | u2dint | uninitialized | conditional | fname | defined at 713 | `OPEN(UNIT = LOCAT, FILE = FNAME, ACTION = ACTION(1))` |
| 752 | u2dint | uninitialized | conditional | iconst | defined at 723, 729 | `IA(J, I) = ICONST` |
| 753 | u2dint | uninitialized | conditional | iconst | defined at 723, 729 | `WRITE(IOUT, 82) ANAME, ICONST, K` |
| 755 | u2dint | uninitialized | conditional | iconst | defined at 723, 729 | `WRITE(IOUT, 83) ANAME, ICONST` |
| 762 | u2dint | uninitialized | conditional | fmtin | defined at 723, 732 | `WRITE(IOUT, 94) ANAME, K, LOCAT, FMTIN` |
| 766 | u2dint | uninitialized | conditional | fmtin | defined at 723, 732 | `WRITE(IOUT, 95) ANAME, LOCAT, FMTIN` |
| 770 | u2dint | uninitialized | conditional | fmtin | defined at 723, 732 | `WRITE(IOUT, 96) ANAME, LOCAT, FMTIN` |
| 775 | u2dint | uninitialized | conditional | fmtin | defined at 723, 732 | `IF (FMTIN .EQ. '(FREE)') THEN` |
| 778 | u2dint | uninitialized | conditional | fmtin | defined at 723, 732 | `READ(LOCAT, FMTIN) (IA(J, I), J = 1, JJ)` |
| 804 | u2dint | uninitialized | conditional | iconst | defined at 723, 729 | `IF (ICONST .EQ. 0) GO TO 320` |
| 807 | u2dint | uninitialized | conditional | iconst | defined at 723, 729 | `IA(J, I) = IA(J, I) * ICONST` |
| 811 | u2dint | uninitialized | conditional | iprn | defined at 723, 742, 814 | `IF (IPRN .LT. 0) RETURN` |
| 814 | u2dint | uninitialized | conditional | iprn | defined at 723, 742, 814 | `IF (IPRN .GT. 9 .OR. IPRN .EQ. 0) IPRN = 6` |
| 815 | u2dint | uninitialized | conditional | iprn | defined at 723, 742, 814 | `GO TO (401, 402, 403, 404, 405, 406, 407, 408, 409), IPRN` |
| 836 | u2dint | uninitialized | conditional | iprn | defined at 723, 742, 814 | `GO TO (501, 502, 503, 504, 505, 506, 507, 508, 509), IPRN` |
| 992 | u2drel | uninitialized | conditional | fname | defined at 970 | `OPEN(UNIT = LOCAT, FILE = FNAME, FORM = FORM, ACCESS = ACCESS, ACTION = ACTION(1))` |
| 995 | u2drel | uninitialized | conditional | fname | defined at 970 | `OPEN(UNIT = LOCAT, FILE = FNAME, ACTION = ACTION(1))` |
| 1009 | u2drel | uninitialized | conditional | cnstnt | defined at 980, 986 | `A(J, I) = CNSTNT` |
| 1010 | u2drel | uninitialized | conditional | cnstnt | defined at 980, 986 | `WRITE(IOUT, 2) ANAME, CNSTNT, K` |
| 1012 | u2drel | uninitialized | conditional | cnstnt | defined at 980, 986 | `WRITE(IOUT, 3) ANAME, CNSTNT` |
| 1019 | u2drel | uninitialized | conditional | fmtin | defined at 980, 989 | `WRITE(IOUT, 94) ANAME, K, LOCAT, FMTIN` |
| 1023 | u2drel | uninitialized | conditional | fmtin | defined at 980, 989 | `WRITE(IOUT, 95) ANAME, LOCAT, FMTIN` |
| 1027 | u2drel | uninitialized | conditional | fmtin | defined at 980, 989 | `WRITE(IOUT, 96) ANAME, LOCAT, FMTIN` |
| 1032 | u2drel | uninitialized | conditional | fmtin | defined at 980, 989 | `IF (FMTIN .EQ. '(FREE)') THEN` |
| 1035 | u2drel | uninitialized | conditional | fmtin | defined at 980, 989 | `READ(LOCAT, FMTIN) (A(J, I), J = 1, JJ)` |
| 1062 | u2drel | uninitialized | conditional | cnstnt | defined at 980, 986 | `IF (CNSTNT .EQ. ZERO) GO TO 320` |
| 1065 | u2drel | uninitialized | conditional | cnstnt | defined at 980, 986 | `A(J, I) = A(J, I) * CNSTNT` |
| 1069 | u2drel | uninitialized | conditional | iprn | defined at 980, 999, 1069 | `IF (IPRN .GE. 0) CALL ULAPRW(A, ANAME, 0, 0, JJ, II, 0, IPRN, IOUT)` |
| 1184 | ucolno | uninitialized | loop-guarded | bf | defined at 1151, 1165, 1169, 1173, 1177, 1179 | `WRITE(IOUT, 31) (BF(I), I = 1, NBF)` |

## Skipped units and parse failures

None — every program unit was analyzed.

## Soundness assumptions

Each detector is conservative **given** its policies below; every policy is a place where the engine assumes rather than proves.

### Uninitialized reads

- A variable passed to a call or function reference with unknown intent is assumed defined afterwards; if that assumption is the only defining path of a later read, the read is reported as call-assumed instead of being trusted.
- An assignment to any array element counts as defining the whole array (weak update); partial initializations followed by reads of other elements are not detected.
- Dummy arguments without INTENT(OUT) are assumed defined by the caller.
- Module and COMMON variables are assumed defined at procedure entry; cross-unit initialization order is not analyzed.
- SAVE, DATA, and declaration-initialized variables are assumed defined (their first-call state is not modeled).
- DO loop bodies may execute zero times; a variable whose only definitions sit inside such loops is reported as loop-guarded.
- Pointer and allocatable variables (and pointer-assignment targets) are not value-tracked; see the pointer detector for association misuse.

### Argument aliasing and constant modification

- Overlap is detected by same base variable only: two different arrays overlapping through COMMON/EQUIVALENCE or pointer association are not seen (runtime differential builds audit those).
- Two elements of the same array count as overlapping (the subscripts are not compared), so distinct-element calls appear as findings; the callee writing either dummy still makes these worth review.
- Calls to procedures outside the corpus (or with duplicate names) are not checked.
- written-through-calls (the -possible categories) can be false positives when the transitive callee only reads.

### Interface mismatches

- Only procedures defined in this source tree (with unique names) are checked; intrinsics and external libraries are skipped.
- Types are compared by class (integer/real/double/complex/logical/character); kinds and character lengths are not compared, and REAL/COMPLEX with explicit kind selectors are skipped as unknown.
- Rank is compared only where both sides are known: array elements and array sections bound to array dummies are legal sequence association and are not flagged, and an actual whose rank this unit cannot settle (a module or host variable, an expression) is skipped.
- A default CHARACTER scalar does sequence-associate with a CHARACTER array dummy, so those bindings are reported as argument-rank-character rather than argument-rank: they are undefined only when the actual is shorter than the elements the callee reaches, which the unchecked character lengths cannot settle.
- Calls through dummy procedures or with keyword arguments are not resolved.

### Out-of-bounds subscripts (constant)

- Only compile-time-constant subscripts checked against compile-time-constant declared bounds; everything driven by runtime values belongs to the -fcheck=all / -check all runtime builds.
- The last dimension of assumed-size arrays (*) and dimensions with non-constant extents are skipped.

### Storage association (COMMON layout)

- Layouts are compared as sequences of (type class, element count); kinds and character lengths are not compared, and non-constant array extents make an element count unknown ('?'), which still has to match textually.
- Deliberate remapping through COMMON is legal sequence association but remains a modernization hazard, which is why every layout difference is listed.

### Pointer association misuse

- Association state is tracked per unit only: deallocation or re-association performed by a callee (the PNT/PSV grid-swap idiom) is invisible, so a variable passed to any call is treated as possibly re-associated afterwards.
- ALLOCATE, pointer assignment, and (conservatively) any call taking the variable as an argument clear the deallocated state.

### FORMAT descriptors vs data-transfer items

- Only formats given as a FORMAT statement label or a character literal are checked; formats held in a character variable, named constant, or expression, list-directed (*), namelist, and unformatted transfers are skipped.
- Item types come from the unit's declarations and implicit typing; module/host-associated variables declared elsewhere, derived-type components, function references (other than a few intrinsics whose result class is fixed), and array constructors have unknown type and are never flagged.
- Whole arrays, array sections, and implied-DO loops contribute a known item count only when their extents are compile-time constants; after an item of unknown count the rest of the statement is not checked, and no count finding is emitted for it.
- G accepts every intrinsic type (Fortran 2008 generalized G) and DT consumes one item without a type check, so neither is ever flagged.
- Character length against A/G width and I/F/E width overflow are not checked: truncation and asterisk fill are defined behavior.
- Hollerith constants spanning a continuation line, and formats the tokenizer does not understand, skip the statement.
- A non-character item against A is reported as a mismatch even though gfortran transfers the raw bytes; the detail says so.

## Outside static scope

These undefined-behavior classes need the runtime check matrix (Process.md), not this report:

- Floating-point exceptions (overflow, divide-by-zero, invalid operands): compile with -ffpe-trap / -fpe0 across the matrix.
- Array bounds that depend on runtime values: -fcheck=all / -check all builds; only compile-time-constant subscripts are checked statically.
- Integer overflow: -fsanitize=undefined / -ftrapv builds.
- Argument aliasing through storage the analysis cannot see (pointer targets, sequence association across COMMON): differential -O0 vs -O2 runs across compilers.
