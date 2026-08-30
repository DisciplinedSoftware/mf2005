# Undefined behavior report

Generated 2026-08-30T01:32:10-04:00 at commit 234402d for mf2005.

## Summary

| Metric | Count |
| --- | ---: |
| Source files | 54 |
| Program units analyzed | 793 |
| Program units skipped | 0 |
| Findings (all detectors) | 1,539 |
| — Uninitialized reads | 1,507 |
| — Argument aliasing and constant modification | 30 |
| — Interface mismatches | 2 |
| — Out-of-bounds subscripts (constant) | 0 |
| — Storage association (COMMON layout) | 0 |
| — Pointer association misuse | 0 |

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
- **argument-rank-character** (2) — a CHARACTER scalar is bound to a CHARACTER array dummy: legal sequence association only while the actual is at least as long as the dummy elements the callee reaches

### Out-of-bounds subscripts (constant)

Every compile-time-constant subscript is checked against the declared constant bounds of local and COMMON arrays.

- **constant-subscript** (0) — a constant subscript falls outside the declared constant bounds

### Storage association (COMMON layout)

Compares every named COMMON block's layout across the program units that declare it; differing layouts alias storage under different names and types.

- **common-layout** (0) — a named COMMON block has different layouts across program units

### Pointer association misuse

Per-unit dataflow over ALLOCATE/DEALLOCATE/NULLIFY/pointer-assignment: flags references reachable while the variable may be deallocated or disassociated.

- **use-after-dealloc** (0) — a path reaches this reference after DEALLOCATE/NULLIFY without re-association

## Findings

### de47.f90 (2)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 348 | de47ap | uninitialized | loop-guarded | ieq | defined at 285, 295, 303, 311, 319, 327, 335 | `L = IEQ(M)` |
| 352 | de47ap | uninitialized | loop-guarded | cnd | defined at 294, 302, 310, 318, 326, 334 | `AU(N, IR) = CND(M)` |

### gwf2bas7.f90 (1)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 1789 | sgwf2bas7l | uninitialized | conditional | layer | defined at 1773 | `WRITE(IOUT, 112) LABEL, (LAYER(M), M = 1, NSET)` |

### gwf2bcf7.f90 (45)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 332 | gwf2bcf7fm | uninitialized | conditional | tled | defined at 306 | `RHO = SC1(J, I, K) * TLED` |
| 347 | gwf2bcf7fm | uninitialized | conditional | tled | defined at 306 | `RHO2 = SC2(J, I, KT) * TLED` |
| 348 | gwf2bcf7fm | uninitialized | conditional | tled | defined at 306 | `RHO1 = SC1(J, I, K) * TLED` |
| 789 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 765, 781, 824, 866, 867 | `DO 310 K = K1, K2` |
| 789 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 766, 782, 825, 868, 881 | `DO 310 K = K1, K2` |
| 790 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 767, 783, 826, 827, 869 | `DO 310 I = I1, I2` |
| 790 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 768, 784, 828, 839, 870 | `DO 310 I = I1, I2` |
| 791 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 769, 785, 786, 829, 871 | `DO 310 J = J1, J2` |
| 791 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 770, 787, 796, 830, 872 | `DO 310 J = J1, J2` |
| 796 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 770, 787, 796, 830, 872 | `IF (J2 .EQ. NCOL) J2 = J2 - 1` |
| 797 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 765, 781, 824, 866, 867 | `DO 400 K = K1, K2` |
| 797 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 766, 782, 825, 868, 881 | `DO 400 K = K1, K2` |
| 798 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 767, 783, 826, 827, 869 | `DO 400 I = I1, I2` |
| 798 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 768, 784, 828, 839, 870 | `DO 400 I = I1, I2` |
| 799 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 769, 785, 786, 829, 871 | `DO 400 J = J1, J2` |
| 799 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 770, 787, 796, 830, 872 | `DO 400 J = J1, J2` |
| 832 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 765, 781, 824, 866, 867 | `DO 410 K = K1, K2` |
| 832 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 766, 782, 825, 868, 881 | `DO 410 K = K1, K2` |
| 833 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 767, 783, 826, 827, 869 | `DO 410 I = I1, I2` |
| 833 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 768, 784, 828, 839, 870 | `DO 410 I = I1, I2` |
| 834 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 769, 785, 786, 829, 871 | `DO 410 J = J1, J2` |
| 834 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 770, 787, 796, 830, 872 | `DO 410 J = J1, J2` |
| 839 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 768, 784, 828, 839, 870 | `IF (I2 .EQ. NROW) I2 = I2 - 1` |
| 840 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 765, 781, 824, 866, 867 | `DO 500 K = K1, K2` |
| 840 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 766, 782, 825, 868, 881 | `DO 500 K = K1, K2` |
| 841 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 767, 783, 826, 827, 869 | `DO 500 I = I1, I2` |
| 841 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 768, 784, 828, 839, 870 | `DO 500 I = I1, I2` |
| 842 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 769, 785, 786, 829, 871 | `DO 500 J = J1, J2` |
| 842 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 770, 787, 796, 830, 872 | `DO 500 J = J1, J2` |
| 874 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 765, 781, 824, 866, 867 | `DO 510 K = K1, K2` |
| 874 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 766, 782, 825, 868, 881 | `DO 510 K = K1, K2` |
| 875 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 767, 783, 826, 827, 869 | `DO 510 I = I1, I2` |
| 875 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 768, 784, 828, 839, 870 | `DO 510 I = I1, I2` |
| 876 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 769, 785, 786, 829, 871 | `DO 510 J = J1, J2` |
| 876 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 770, 787, 796, 830, 872 | `DO 510 J = J1, J2` |
| 881 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 766, 782, 825, 868, 881 | `IF (K2 .EQ. NLAY) K2 = K2 - 1` |
| 882 | gwf2bcf7bdadj | uninitialized | conditional | k2 | defined at 766, 782, 825, 868, 881 | `DO 600 K = 1, K2` |
| 883 | gwf2bcf7bdadj | uninitialized | conditional | k1 | defined at 765, 781, 824, 866, 867 | `IF (K .LT. K1) GO TO 600` |
| 884 | gwf2bcf7bdadj | uninitialized | conditional | i1 | defined at 767, 783, 826, 827, 869 | `DO 590 I = I1, I2` |
| 884 | gwf2bcf7bdadj | uninitialized | conditional | i2 | defined at 768, 784, 828, 839, 870 | `DO 590 I = I1, I2` |
| 885 | gwf2bcf7bdadj | uninitialized | conditional | j1 | defined at 769, 785, 786, 829, 871 | `DO 590 J = J1, J2` |
| 885 | gwf2bcf7bdadj | uninitialized | conditional | j2 | defined at 770, 787, 796, 830, 872 | `DO 590 J = J1, J2` |
| 1104 | sgwf2bcf7h | uninitialized | loop-guarded | acnvrt | defined at 1035, 1078 | `WRITE(IOUT, 18) (ACNVRT(L), ICNVRT(L), JCNVRT(L), L = 1, NCNVRT)` |
| 1104 | sgwf2bcf7h | uninitialized | loop-guarded | icnvrt | defined at 1033, 1076 | `WRITE(IOUT, 18) (ACNVRT(L), ICNVRT(L), JCNVRT(L), L = 1, NCNVRT)` |
| 1104 | sgwf2bcf7h | uninitialized | loop-guarded | jcnvrt | defined at 1034, 1077 | `WRITE(IOUT, 18) (ACNVRT(L), ICNVRT(L), JCNVRT(L), L = 1, NCNVRT)` |

### gwf2drt7.f90 (10)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 377 | gwf2drt7bd | uninitialized | loop-guarded | icr | defined at 355, 411 | `IF (ILR .NE. 0 .AND. IBOUND(ICR, IRR, ILR) .GT. 0) THEN` |
| 377 | gwf2drt7bd | uninitialized | loop-guarded | irr | defined at 354, 411 | `IF (ILR .NE. 0 .AND. IBOUND(ICR, IRR, ILR) .GT. 0) THEN` |
| 394 | gwf2drt7bd | uninitialized | loop-guarded | icr | defined at 355, 411 | `WRITE(IOUT, 550) L, ILR, IRR, ICR, QIN` |
| 394 | gwf2drt7bd | uninitialized | loop-guarded | irr | defined at 354, 411 | `WRITE(IOUT, 550) L, ILR, IRR, ICR, QIN` |
| 394 | gwf2drt7bd | uninitialized | loop-guarded | qin | defined at 351, 380, 411 | `WRITE(IOUT, 550) L, ILR, IRR, ICR, QIN` |
| 403 | gwf2drt7bd | uninitialized | loop-guarded | icr | defined at 355, 411 | `BUFF(ICR, IRR, ILR) = BUFF(ICR, IRR, ILR) + QIN` |
| 403 | gwf2drt7bd | uninitialized | loop-guarded | irr | defined at 354, 411 | `BUFF(ICR, IRR, ILR) = BUFF(ICR, IRR, ILR) + QIN` |
| 403 | gwf2drt7bd | uninitialized | loop-guarded | qin | defined at 351, 380, 411 | `BUFF(ICR, IRR, ILR) = BUFF(ICR, IRR, ILR) + QIN` |
| 416 | gwf2drt7bd | uninitialized | loop-guarded | qin | defined at 351, 380, 411 | `DRTF(NDRTVL - 1, L) = QIN` |
| 814 | sgwf2drt7ls | uninitialized | loop-guarded | nlst | defined at 731, 736 | `DO 140 II = NDRTCL - NLST + 1, NDRTCL` |

### gwf2ets7.f90 (11)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 246 | gwf2ets7rp | uninitialized | conditional | iniets | defined at 169, 171, 176, 178 | `IF (INIETS .LT. 0) THEN` |
| 258 | gwf2ets7rp | uninitialized | conditional | insgdf | defined at 169, 171 | `IF (INSGDF .LT. 0) THEN` |
| 315 | gwf2ets7fm | uninitialized | loop-guarded | il | defined at 298, 301, 305, 308 | `IF (IBOUND(IC, IR, IL) .GT. 0) THEN` |
| 319 | gwf2ets7fm | uninitialized | loop-guarded | il | defined at 298, 301, 305, 308 | `HH = HNEW(IC, IR, IL)` |
| 325 | gwf2ets7fm | uninitialized | loop-guarded | il | defined at 298, 301, 305, 308 | `RHS(IC, IR, IL) = RHS(IC, IR, IL) + C` |
| 364 | gwf2ets7fm | uninitialized | loop-guarded | petm2 | defined at 347, 350 | `THCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |
| 364 | gwf2ets7fm | uninitialized | loop-guarded | pxdp2 | defined at 346, 349 | `THCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |
| 372 | gwf2ets7fm | uninitialized | loop-guarded | il | defined at 298, 301, 305, 308 | `RHS(IC, IR, IL) = RHS(IC, IR, IL) + TRHS` |
| 373 | gwf2ets7fm | uninitialized | loop-guarded | il | defined at 298, 301, 305, 308 | `HCOF(IC, IR, IL) = HCOF(IC, IR, IL) + THCOF` |
| 488 | gwf2ets7bd | uninitialized | loop-guarded | petm2 | defined at 471, 474 | `HHCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |
| 488 | gwf2ets7bd | uninitialized | loop-guarded | pxdp2 | defined at 470, 473 | `HHCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |

### gwf2evt7.f90 (1)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 207 | gwf2evt7rp | uninitialized | conditional | inievt | defined at 129, 131 | `IF (INIEVT .LT. 0) THEN` |

### gwf2fhb7.f90 (3)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 268 | gwf2fhb7ar | uninitialized | conditional | nd | defined at 201, 238, 295 | `WRITE(IOUT, 54) (DSH1, M = 1, ND)` |
| 337 | gwf2fhb7ar | uninitialized | conditional | nd | defined at 201, 238, 295 | `WRITE(IOUT, 54) (DSH1, M = 1, ND)` |
| 604 | gwf2fhb7bd | interface | argument-rank-character | ubdsv4(5) | actual 'IFACE ' is a character scalar, dummy auxtxt is a character array at utl7.f90:1610 | `CALL UBDSV4(KSTP, KPER, TEXT, NAUX, 'IFACE ', IFHBCB, NCOL, NROW, NLAY, NFLW, IOUT, DELT, PERTIM,...` |

### gwf2gag7.f90 (4)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 931 | sgwf2gag7so | uninitialized | loop-guarded | pmxdvrt | defined at 889, 890, 891 | `WRITE(IG3, 270) GAGETM, STRM(15, II), PMXDVRT, STRM(10, II), UPSTRFLW` |
| 931 | sgwf2gag7so | uninitialized | loop-guarded | upstrflw | defined at 888 | `WRITE(IG3, 270) GAGETM, STRM(15, II), PMXDVRT, STRM(10, II), UPSTRFLW` |
| 1003 | sgwf2gag7so | uninitialized | loop-guarded | pmxdvrt | defined at 889, 890, 891 | `WRITE(IG3, LFRMAT) GAGETM, STRM(15, II), PMXDVRT, STRM(10, II), UPSTRFLW, (COUT(II, ISOL), CLOAD(...` |
| 1003 | sgwf2gag7so | uninitialized | loop-guarded | upstrflw | defined at 888 | `WRITE(IG3, LFRMAT) GAGETM, STRM(15, II), PMXDVRT, STRM(10, II), UPSTRFLW, (COUT(II, ISOL), CLOAD(...` |

### gwf2huf7.f90 (57)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 521 | gwf2huf7ar | uninitialized | conditional | iflg | defined at 490, 497, 498, 499, 501, 502, 506, 508, 510, 512, 514 | `IHGUFLG(I, NU) = IFLG(I)` |
| 527 | gwf2huf7ar | uninitialized | conditional | iflg | defined at 490, 497, 498, 499, 501, 502, 506, 508, 510, 512, 514 | `IHGUFLG(I, IU) = IFLG(I)` |
| 2421 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2397, 2413, 2464, 2515, 2516 | `DO 310 K = K1, K2` |
| 2421 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2398, 2414, 2465, 2517, 2530 | `DO 310 K = K1, K2` |
| 2422 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2399, 2415, 2466, 2467, 2518 | `DO 310 I = I1, I2` |
| 2422 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2400, 2416, 2468, 2479, 2519 | `DO 310 I = I1, I2` |
| 2423 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2401, 2417, 2418, 2469, 2520 | `DO 310 J = J1, J2` |
| 2423 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2402, 2419, 2428, 2470, 2521 | `DO 310 J = J1, J2` |
| 2428 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2402, 2419, 2428, 2470, 2521 | `IF (J2 .EQ. NCOL) J2 = J2 - 1` |
| 2429 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2397, 2413, 2464, 2515, 2516 | `DO 400 K = K1, K2` |
| 2429 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2398, 2414, 2465, 2517, 2530 | `DO 400 K = K1, K2` |
| 2430 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2399, 2415, 2466, 2467, 2518 | `DO 400 I = I1, I2` |
| 2430 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2400, 2416, 2468, 2479, 2519 | `DO 400 I = I1, I2` |
| 2431 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2401, 2417, 2418, 2469, 2520 | `DO 400 J = J1, J2` |
| 2431 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2402, 2419, 2428, 2470, 2521 | `DO 400 J = J1, J2` |
| 2472 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2397, 2413, 2464, 2515, 2516 | `DO 410 K = K1, K2` |
| 2472 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2398, 2414, 2465, 2517, 2530 | `DO 410 K = K1, K2` |
| 2473 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2399, 2415, 2466, 2467, 2518 | `DO 410 I = I1, I2` |
| 2473 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2400, 2416, 2468, 2479, 2519 | `DO 410 I = I1, I2` |
| 2474 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2401, 2417, 2418, 2469, 2520 | `DO 410 J = J1, J2` |
| 2474 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2402, 2419, 2428, 2470, 2521 | `DO 410 J = J1, J2` |
| 2479 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2400, 2416, 2468, 2479, 2519 | `IF (I2 .EQ. NROW) I2 = I2 - 1` |
| 2480 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2397, 2413, 2464, 2515, 2516 | `DO 500 K = K1, K2` |
| 2480 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2398, 2414, 2465, 2517, 2530 | `DO 500 K = K1, K2` |
| 2481 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2399, 2415, 2466, 2467, 2518 | `DO 500 I = I1, I2` |
| 2481 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2400, 2416, 2468, 2479, 2519 | `DO 500 I = I1, I2` |
| 2482 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2401, 2417, 2418, 2469, 2520 | `DO 500 J = J1, J2` |
| 2482 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2402, 2419, 2428, 2470, 2521 | `DO 500 J = J1, J2` |
| 2523 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2397, 2413, 2464, 2515, 2516 | `DO 510 K = K1, K2` |
| 2523 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2398, 2414, 2465, 2517, 2530 | `DO 510 K = K1, K2` |
| 2524 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2399, 2415, 2466, 2467, 2518 | `DO 510 I = I1, I2` |
| 2524 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2400, 2416, 2468, 2479, 2519 | `DO 510 I = I1, I2` |
| 2525 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2401, 2417, 2418, 2469, 2520 | `DO 510 J = J1, J2` |
| 2525 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2402, 2419, 2428, 2470, 2521 | `DO 510 J = J1, J2` |
| 2530 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2398, 2414, 2465, 2517, 2530 | `IF (K2 .EQ. NLAY) K2 = K2 - 1` |
| 2531 | gwf2huf7bdadj | uninitialized | conditional | k2 | defined at 2398, 2414, 2465, 2517, 2530 | `DO 600 K = 1, K2` |
| 2532 | gwf2huf7bdadj | uninitialized | conditional | k1 | defined at 2397, 2413, 2464, 2515, 2516 | `IF (K .LT. K1) GO TO 600` |
| 2533 | gwf2huf7bdadj | uninitialized | conditional | i1 | defined at 2399, 2415, 2466, 2467, 2518 | `DO 590 I = I1, I2` |
| 2533 | gwf2huf7bdadj | uninitialized | conditional | i2 | defined at 2400, 2416, 2468, 2479, 2519 | `DO 590 I = I1, I2` |
| 2534 | gwf2huf7bdadj | uninitialized | conditional | j1 | defined at 2401, 2417, 2418, 2469, 2520 | `DO 590 J = J1, J2` |
| 2534 | gwf2huf7bdadj | uninitialized | conditional | j2 | defined at 2402, 2419, 2428, 2470, 2521 | `DO 590 J = J1, J2` |
| 2649 | gwf2huf7bdch | uninitialized | call-assumed | dfl | defined at 2633 | `CHCH1 = - DFL` |
| 2669 | gwf2huf7bdch | uninitialized | call-assumed | dfr | defined at 2633 | `CHCH2 = DFR` |
| 2687 | gwf2huf7bdch | uninitialized | call-assumed | dft | defined at 2633 | `CHCH3 = - DFT` |
| 2705 | gwf2huf7bdch | uninitialized | call-assumed | dfb | defined at 2633 | `CHCH4 = DFB` |
| 2952 | sgwf2huf7flot | uninitialized | loop-guarded | hxr | defined at 2946 | `DHXR = H0 - HXR` |
| 2964 | sgwf2huf7flot | uninitialized | loop-guarded | hyb | defined at 2958 | `DHYB = H0 - HYB` |
| 3457 | sgwf2huf7c | uninitialized | loop-guarded | tr0 | defined at 3453 | `IF (TR0 .EQ. 0.0 .AND. TR1 .EQ. 0.0) THEN` |
| 3460 | sgwf2huf7c | uninitialized | loop-guarded | tr0 | defined at 3453 | `CRL = 2. * TR1 * TR0 * DELC(I) / (TR1 * DELR(J + 1) + TR0 * DELR(J))` |
| 3464 | sgwf2huf7c | uninitialized | loop-guarded | tr0 | defined at 3453 | `IF (TR0 .EQ. 0.0 .AND. TR1 .EQ. 0.0) THEN` |
| 3467 | sgwf2huf7c | uninitialized | loop-guarded | tr0 | defined at 3453 | `CRR = 2. * TR1 * TR0 * DELC(I) / (TR1 * DELR(J - 1) + TR0 * DELR(J))` |
| 3471 | sgwf2huf7c | uninitialized | loop-guarded | tc0 | defined at 3454 | `IF (TC0 .EQ. 0.0 .AND. TC1 .EQ. 0.0) THEN` |
| 3474 | sgwf2huf7c | uninitialized | loop-guarded | tc0 | defined at 3454 | `CCT = 2. * TC1 * TC0 * DELR(J) / (TC1 * DELC(I + 1) + TC0 * DELC(I))` |
| 3478 | sgwf2huf7c | uninitialized | loop-guarded | tc0 | defined at 3454 | `IF (TC0 .EQ. 0.0 .AND. TC1 .EQ. 0.0) THEN` |
| 3481 | sgwf2huf7c | uninitialized | loop-guarded | tc0 | defined at 3454 | `CCB = 2. * TC1 * TC0 * DELR(J) / (TC1 * DELC(I - 1) + TC0 * DELC(I))` |
| 3524 | sgwf2huf7ind | uninitialized | conditional | istack | defined at 3569, 3570, 3573, 3574 | `ir = istack(jstack)` |
| 3525 | sgwf2huf7ind | uninitialized | conditional | istack | defined at 3569, 3570, 3573, 3574 | `l = istack(jstack - 1)` |

### gwf2hydmod7.f90 (25)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 203 | gwf2hyd7bas7ar | uninitialized | conditional | hydbaslbl | defined at 212 | `WRITE(HYDBASLBL(1 : 2), FMT = '(A2)') HYDBASARR(NHYDBAS)` |
| 206 | gwf2hyd7bas7ar | uninitialized | conditional | hydbaslbl | defined at 212 | `WRITE(HYDBASLBL(3 : 3), FMT = '(A1)') LINE(ISTART : ISTOP)` |
| 211 | gwf2hyd7bas7ar | uninitialized | conditional | hydbaslbl | defined at 212 | `WRITE(HYDBASLBL(4 : 6), FMT = '(I3.3)') KLAY` |
| 292 | gwf2hyd7bas7ar | uninitialized | call-assumed | w1 | defined at 261 | `HYDBASSTRT(NHYDBAS) = H1 * W1 + H2 * W2 + H3 * W3 + H4 * W4` |
| 292 | gwf2hyd7bas7ar | uninitialized | call-assumed | w2 | defined at 261 | `HYDBASSTRT(NHYDBAS) = H1 * W1 + H2 * W2 + H3 * W3 + H4 * W4` |
| 292 | gwf2hyd7bas7ar | uninitialized | call-assumed | w3 | defined at 261 | `HYDBASSTRT(NHYDBAS) = H1 * W1 + H2 * W2 + H3 * W3 + H4 * W4` |
| 292 | gwf2hyd7bas7ar | uninitialized | call-assumed | w4 | defined at 261 | `HYDBASSTRT(NHYDBAS) = H1 * W1 + H2 * W2 + H3 * W3 + H4 * W4` |
| 371 | gwf2hyd7ibs7ar | uninitialized | conditional | hydibslbl | defined at 380 | `WRITE(HYDIBSLBL(1 : 2), FMT = '(A2)') ARR` |
| 374 | gwf2hyd7ibs7ar | uninitialized | conditional | hydibslbl | defined at 380 | `WRITE(HYDIBSLBL(3 : 3), FMT = '(A1)') INTYP` |
| 379 | gwf2hyd7ibs7ar | uninitialized | conditional | hydibslbl | defined at 380 | `WRITE(HYDIBSLBL(4 : 6), FMT = '(I3.3)') KLAY` |
| 529 | gwf2hyd7sub7ar | uninitialized | conditional | hydsublbl | defined at 538 | `WRITE(HYDSUBLBL(1 : 2), FMT = '(A2)') ARR` |
| 532 | gwf2hyd7sub7ar | uninitialized | conditional | hydsublbl | defined at 538 | `WRITE(HYDSUBLBL(3 : 3), FMT = '(A1)') INTYP` |
| 537 | gwf2hyd7sub7ar | uninitialized | conditional | hydsublbl | defined at 538 | `WRITE(HYDSUBLBL(4 : 6), FMT = '(I3.3)') KLAY` |
| 708 | gwf2hyd7str7rp | uninitialized | conditional | hydstrlbl | defined at 717 | `WRITE(HYDSTRLBL(1 : 2), FMT = '(A2)') HYDSTRARR(NUMSTR)` |
| 715 | gwf2hyd7str7rp | uninitialized | conditional | hydstrlbl | defined at 717 | `WRITE(HYDSTRLBL(3 : 5), FMT = '(I3.3)') INT(XL)` |
| 716 | gwf2hyd7str7rp | uninitialized | conditional | hydstrlbl | defined at 717 | `WRITE(HYDSTRLBL(6 : 8), FMT = '(I3.3)') INT(YL)` |
| 854 | gwf2hyd7sfr7rp | uninitialized | conditional | hydsfrlbl | defined at 863 | `WRITE(HYDSFRLBL(1 : 2), FMT = '(A2)') HYDSFRARR(NUMSFR)` |
| 861 | gwf2hyd7sfr7rp | uninitialized | conditional | hydsfrlbl | defined at 863 | `WRITE(HYDSFRLBL(3 : 5), FMT = '(I3.3)') INT(XL)` |
| 862 | gwf2hyd7sfr7rp | uninitialized | conditional | hydsfrlbl | defined at 863 | `WRITE(HYDSFRLBL(6 : 8), FMT = '(I3.3)') INT(YL)` |
| 960 | gwf2hyd7bas7se | uninitialized | loop-guarded | ibfact | defined at 949, 954 | `IF (IBHYDBAS(N) .AND. IBFACT .EQ. 0) THEN` |
| 968 | gwf2hyd7bas7se | uninitialized | loop-guarded | ibfact | defined at 949, 954 | `IF (IBHYDBAS(N) .AND. IBFACT .EQ. 0) THEN` |
| 1020 | gwf2hyd7ibs7se | uninitialized | loop-guarded | ibfact | defined at 1009, 1014 | `IF (IBHYDIBS(N) .AND. IBFACT .EQ. 0) THEN` |
| 1036 | gwf2hyd7ibs7se | uninitialized | loop-guarded | ibfact | defined at 1009, 1014 | `IF (IBHYDIBS(N) .AND. IBFACT .EQ. 0) THEN` |
| 1113 | gwf2hyd7sub7se | uninitialized | loop-guarded | ibfact | defined at 1102, 1107 | `IF (IBHYDSUB(N) .AND. IBFACT .EQ. 0) THEN` |
| 1133 | gwf2hyd7sub7se | uninitialized | loop-guarded | ibfact | defined at 1102, 1107 | `IF (IBHYDSUB(N) .AND. IBFACT .EQ. 0) THEN` |

### gwf2lak7.f90 (20)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 665 | gwf2lak7rp | uninitialized | loop-guarded | lid | defined at 654, 656, 660, 662 | `ILAKE(4, M) = LID` |
| 673 | gwf2lak7rp | uninitialized | loop-guarded | lid | defined at 654, 656, 660, 662 | `BGAREA(LID) = BGAREA(LID) + DELC(J) * DELR(I)` |
| 1497 | gwf2lak7fm | uninitialized | loop-guarded | thck | defined at 1494, 1495 | `IF (STGON .GT. BOTCL .OR. THCK .GT. 0.0) THEN` |
| 2260 | gwf2lak7bd | uninitialized | loop-guarded | jcls | defined at 2245, 2260, 2269, 2277, 2298, 2307 | `IF (JCLS(IC4, IC5) .EQ. 1) JCLS(IC4, IC5) = 2` |
| 2263 | gwf2lak7bd | uninitialized | loop-guarded | jcls | defined at 2245, 2260, 2269, 2277, 2298, 2307 | `IF (JCLS(ICL, 1) .GE. 2) GO TO 1300` |
| 2499 | gwf2lak7bd | uninitialized | loop-guarded | tvolm | defined at 2455, 2473 | `TV = TVOLM / 1000000.` |
| 2517 | gwf2lak7bd | uninitialized | loop-guarded | botlk | defined at 1947, 1949, 1952, 1988, 2514, 2515, 2925, 2938 | `IF (STGNEW(LAKE) .LE. BOTLK) THEN` |
| 2543 | gwf2lak7bd | uninitialized | loop-guarded | icb | defined at 2537 | `WRITE(IOUT, 876) (ILB(I), IRB(I), ICB(I), I = 1, LDR1)` |
| 2543 | gwf2lak7bd | uninitialized | loop-guarded | ilb | defined at 2535 | `WRITE(IOUT, 876) (ILB(I), IRB(I), ICB(I), I = 1, LDR1)` |
| 2543 | gwf2lak7bd | uninitialized | loop-guarded | irb | defined at 2536 | `WRITE(IOUT, 876) (ILB(I), IRB(I), ICB(I), I = 1, LDR1)` |
| 3157 | sgwf2lak7bcf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3110, 3114, 3155, 3156 | `IF (CNDFC1 .GT. 0.0 .AND. CNDFC2 .GT. 0.0) CNDFCT(II) = 1.0 / (1.0 / CNDFC2 + 1.0 / CNDFC1)` |
| 3157 | sgwf2lak7bcf7rps | uninitialized | loop-guarded | cndfc2 | defined at 3153, 3154 | `IF (CNDFC1 .GT. 0.0 .AND. CNDFC2 .GT. 0.0) CNDFCT(II) = 1.0 / (1.0 / CNDFC2 + 1.0 / CNDFC1)` |
| 3159 | sgwf2lak7bcf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3110, 3114, 3155, 3156 | `WRITE(IOUT, 7325) (ILAKE(I1, II), I1 = 1, 5), DELC(J), DELR(I), BEDLAK(II), CNDFC1, CNDFC2, CNDFC...` |
| 3159 | sgwf2lak7bcf7rps | uninitialized | loop-guarded | cndfc2 | defined at 3153, 3154 | `WRITE(IOUT, 7325) (ILAKE(I1, II), I1 = 1, 5), DELC(J), DELR(I), BEDLAK(II), CNDFC1, CNDFC2, CNDFC...` |
| 3271 | sgwf2lak7lpf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3226, 3229, 3269, 3270 | `IF (CNDFC1 .GT. 0.0 .AND. CNDFC2 .GT. 0.0) CNDFCT(II) = 1.0 / (1.0 / CNDFC2 + 1.0 / CNDFC1)` |
| 3271 | sgwf2lak7lpf7rps | uninitialized | loop-guarded | cndfc2 | defined at 3259, 3264, 3266 | `IF (CNDFC1 .GT. 0.0 .AND. CNDFC2 .GT. 0.0) CNDFCT(II) = 1.0 / (1.0 / CNDFC2 + 1.0 / CNDFC1)` |
| 3273 | sgwf2lak7lpf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3226, 3229, 3269, 3270 | `WRITE(IOUT, 7325) (ILAKE(I1, II), I1 = 1, 5), DELC(J), DELR(I), BEDLAK(II), CNDFC1, CNDFC2, CNDFC...` |
| 3273 | sgwf2lak7lpf7rps | uninitialized | loop-guarded | cndfc2 | defined at 3259, 3264, 3266 | `WRITE(IOUT, 7325) (ILAKE(I1, II), I1 = 1, 5), DELC(J), DELR(I), BEDLAK(II), CNDFC1, CNDFC2, CNDFC...` |
| 3372 | sgwf2lak7huf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3330, 3333, 3367, 3368 | `CNDFCT(II) = CNDFC1` |
| 3373 | sgwf2lak7huf7rps | uninitialized | loop-guarded | cndfc1 | defined at 3330, 3333, 3367, 3368 | `WRITE(IOUT, 7325) (ILAKE(I1, II), I1 = 1, 5), DELC(J), DELR(I), BEDLAK(II), CNDFC1, CNDFCT(II)` |

### gwf2lpf7.f90 (39)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 830 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 806, 822, 865, 907, 908 | `DO 310 K = K1, K2` |
| 830 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 807, 823, 866, 909, 922 | `DO 310 K = K1, K2` |
| 831 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 808, 824, 867, 868, 910 | `DO 310 I = I1, I2` |
| 831 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 809, 825, 869, 880, 911 | `DO 310 I = I1, I2` |
| 832 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 810, 826, 827, 870, 912 | `DO 310 J = J1, J2` |
| 832 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 811, 828, 837, 871, 913 | `DO 310 J = J1, J2` |
| 837 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 811, 828, 837, 871, 913 | `IF (J2 .EQ. NCOL) J2 = J2 - 1` |
| 838 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 806, 822, 865, 907, 908 | `DO 400 K = K1, K2` |
| 838 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 807, 823, 866, 909, 922 | `DO 400 K = K1, K2` |
| 839 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 808, 824, 867, 868, 910 | `DO 400 I = I1, I2` |
| 839 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 809, 825, 869, 880, 911 | `DO 400 I = I1, I2` |
| 840 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 810, 826, 827, 870, 912 | `DO 400 J = J1, J2` |
| 840 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 811, 828, 837, 871, 913 | `DO 400 J = J1, J2` |
| 873 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 806, 822, 865, 907, 908 | `DO 410 K = K1, K2` |
| 873 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 807, 823, 866, 909, 922 | `DO 410 K = K1, K2` |
| 874 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 808, 824, 867, 868, 910 | `DO 410 I = I1, I2` |
| 874 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 809, 825, 869, 880, 911 | `DO 410 I = I1, I2` |
| 875 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 810, 826, 827, 870, 912 | `DO 410 J = J1, J2` |
| 875 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 811, 828, 837, 871, 913 | `DO 410 J = J1, J2` |
| 880 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 809, 825, 869, 880, 911 | `IF (I2 .EQ. NROW) I2 = I2 - 1` |
| 881 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 806, 822, 865, 907, 908 | `DO 500 K = K1, K2` |
| 881 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 807, 823, 866, 909, 922 | `DO 500 K = K1, K2` |
| 882 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 808, 824, 867, 868, 910 | `DO 500 I = I1, I2` |
| 882 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 809, 825, 869, 880, 911 | `DO 500 I = I1, I2` |
| 883 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 810, 826, 827, 870, 912 | `DO 500 J = J1, J2` |
| 883 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 811, 828, 837, 871, 913 | `DO 500 J = J1, J2` |
| 915 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 806, 822, 865, 907, 908 | `DO 510 K = K1, K2` |
| 915 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 807, 823, 866, 909, 922 | `DO 510 K = K1, K2` |
| 916 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 808, 824, 867, 868, 910 | `DO 510 I = I1, I2` |
| 916 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 809, 825, 869, 880, 911 | `DO 510 I = I1, I2` |
| 917 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 810, 826, 827, 870, 912 | `DO 510 J = J1, J2` |
| 917 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 811, 828, 837, 871, 913 | `DO 510 J = J1, J2` |
| 922 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 807, 823, 866, 909, 922 | `IF (K2 .EQ. NLAY) K2 = K2 - 1` |
| 923 | gwf2lpf7bdadj | uninitialized | conditional | k2 | defined at 807, 823, 866, 909, 922 | `DO 600 K = 1, K2` |
| 924 | gwf2lpf7bdadj | uninitialized | conditional | k1 | defined at 806, 822, 865, 907, 908 | `IF (K .LT. K1) GO TO 600` |
| 925 | gwf2lpf7bdadj | uninitialized | conditional | i1 | defined at 808, 824, 867, 868, 910 | `DO 590 I = I1, I2` |
| 925 | gwf2lpf7bdadj | uninitialized | conditional | i2 | defined at 809, 825, 869, 880, 911 | `DO 590 I = I1, I2` |
| 926 | gwf2lpf7bdadj | uninitialized | conditional | j1 | defined at 810, 826, 827, 870, 912 | `DO 590 J = J1, J2` |
| 926 | gwf2lpf7bdadj | uninitialized | conditional | j2 | defined at 811, 828, 837, 871, 913 | `DO 590 J = J1, J2` |

### gwf2mnw17.f90 (19)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 661 | gwf2mnw17rp | uninitialized | loop-guarded | cond | defined at 653, 658, 659, 660, 661 | `cond = cond * 1.0D3` |
| 663 | gwf2mnw17rp | uninitialized | loop-guarded | cond | defined at 653, 658, 659, 660, 661 | `WELL2(11, m) = cond` |
| 674 | gwf2mnw17rp | uninitialized | loop-guarded | hlim | defined at 566, 667, 671 | `WRITE(IOUT, 9004) m, k, j, i, (WELL2(ii, m), ii = 3, 6), hlim, hrfw, WELL2(16, m), igrp, WELL2(11...` |
| 674 | gwf2mnw17rp | uninitialized | loop-guarded | hrfw | defined at 567, 668, 672 | `WRITE(IOUT, 9004) m, k, j, i, (WELL2(ii, m), ii = 3, 6), hlim, hrfw, WELL2(16, m), igrp, WELL2(11...` |
| 766 | gwf2mnw17ad | uninitialized | loop-guarded | cond | defined at 758, 763, 764, 765, 766, 824, 831 | `cond = cond * 1.0D3` |
| 768 | gwf2mnw17ad | uninitialized | loop-guarded | cond | defined at 758, 763, 764, 765, 766, 824, 831 | `WELL2(11, m) = cond` |
| 809 | gwf2mnw17ad | uninitialized | loop-guarded | i | defined at 753, 763, 764, 765, 796, 830 | `hwell = HNEW(i, j, k)` |
| 809 | gwf2mnw17ad | uninitialized | loop-guarded | j | defined at 752, 763, 764, 765, 795, 829 | `hwell = HNEW(i, j, k)` |
| 809 | gwf2mnw17ad | uninitialized | loop-guarded | k | defined at 751, 763, 764, 765, 794, 828 | `hwell = HNEW(i, j, k)` |
| 919 | gwf2mnw17fm | uninitialized | loop-guarded | cond | defined at 911, 916, 917, 918, 919, 1010 | `cond = cond * 1.0D3` |
| 921 | gwf2mnw17fm | uninitialized | loop-guarded | cond | defined at 911, 916, 917, 918, 919, 1010 | `WELL2(11, m) = cond` |
| 955 | gwf2mnw17fm | uninitialized | loop-guarded | i | defined at 906, 916, 917, 918, 943, 989, 1005 | `hwell = HNEW(i, j, k)` |
| 955 | gwf2mnw17fm | uninitialized | loop-guarded | j | defined at 905, 916, 917, 918, 942, 988, 1004 | `hwell = HNEW(i, j, k)` |
| 955 | gwf2mnw17fm | uninitialized | loop-guarded | k | defined at 904, 916, 917, 918, 941, 987, 1003 | `hwell = HNEW(i, j, k)` |
| 978 | gwf2mnw17fm | uninitialized | loop-guarded | i | defined at 906, 916, 917, 918, 943, 989, 1005 | `hwell = HNEW(i, j, k)` |
| 978 | gwf2mnw17fm | uninitialized | loop-guarded | j | defined at 905, 916, 917, 918, 942, 988, 1004 | `hwell = HNEW(i, j, k)` |
| 978 | gwf2mnw17fm | uninitialized | loop-guarded | k | defined at 904, 916, 917, 918, 941, 987, 1003 | `hwell = HNEW(i, j, k)` |
| 1205 | gwf2mnw17bd | uninitialized | loop-guarded | href | defined at 1197, 1201, 1285 | `dd = hwell - href` |
| 1228 | gwf2mnw17bd | uninitialized | loop-guarded | href | defined at 1197, 1201, 1285 | `WRITE(IOWELL2(1), '(i9,2i10,1X,g11.4,1X,i10,2x,6g11.4)') k, j, i, q, 0, qd, hwell, HNEW(i, j, k),...` |

### gwf2mnw27.f90 (389)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 415 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `IF (Rw .GT. 0.0) THEN` |
| 418 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 428 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `IF (Rw .GT. 0.0) THEN` |
| 429 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `IF (Rskin .GT. 0.0) THEN` |
| 430 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 432 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 433 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 434 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 437 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 438 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 442 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 444 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 445 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 448 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 453 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `IF (Rskin .GT. 0.0) THEN` |
| 454 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 456 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 457 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 460 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 464 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 466 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 479 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `IF (Rw .GT. 0.0) THEN` |
| 480 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `IF (B .GE. 0.0) THEN` |
| 481 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 482 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 484 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 485 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 486 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 487 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 490 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 491 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 492 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 496 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 498 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 499 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 500 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 503 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 504 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 509 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 510 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 512 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 513 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 514 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 517 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 518 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 522 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 524 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 525 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 528 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 534 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `IF (B .GE. 0.0) THEN` |
| 535 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 536 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 538 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 539 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 540 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 543 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 544 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 548 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 550 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 551 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 554 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 559 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 560 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 562 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 563 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 566 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 570 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 572 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 587 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 380 | `IF (CWC .GT. 0.0) THEN` |
| 589 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 380 | `CWCNode = CWC` |
| 605 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `IF (Rw .GT. 0.0) THEN` |
| 608 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 618 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `IF (Rw .GT. 0.0) THEN` |
| 619 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `IF (Rskin .GT. 0.0) THEN` |
| 620 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 622 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 623 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 624 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 627 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 628 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 632 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 634 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 635 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 638 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 643 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `IF (Rskin .GT. 0.0) THEN` |
| 644 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 646 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 647 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 650 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 654 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 656 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 669 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `IF (Rw .GT. 0.0) THEN` |
| 670 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `IF (B .GE. 0.0) THEN` |
| 671 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 672 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 674 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 675 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 676 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 677 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 680 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 681 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 682 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 686 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 688 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 689 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 690 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 693 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 694 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 699 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 700 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 702 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 703 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 704 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 707 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 708 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 712 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 714 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 715 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 718 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 724 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `IF (B .GE. 0.0) THEN` |
| 725 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 726 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 728 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 729 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 730 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 733 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 734 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 738 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 740 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 741 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 744 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 749 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 750 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 752 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 753 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 756 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 760 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 762 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 777 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 380 | `IF (CWC .GT. 0.0) THEN` |
| 779 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 380 | `CWCNode = CWC` |
| 787 | gwf2mnw27rp | uninitialized | loop-guarded | il | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 1065, 1166, 1472, 1507, 1527 | `MNWNOD(1, NODNUM + INODE - 1) = IL` |
| 788 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `MNWNOD(2, NODNUM + INODE - 1) = IR` |
| 789 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `MNWNOD(3, NODNUM + INODE - 1) = IC` |
| 794 | gwf2mnw27rp | uninitialized | loop-guarded | pp | defined at 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 792 | `MNWNOD(19, NODNUM + INODE - 1) = PP` |
| 797 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `IRlast = IR` |
| 798 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `IClast = IC` |
| 801 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 801 | gwf2mnw27rp | uninitialized | loop-guarded | iclast | defined at 798, 1049 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 801 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 801 | gwf2mnw27rp | uninitialized | loop-guarded | irlast | defined at 797, 1048 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 809 | gwf2mnw27rp | uninitialized | loop-guarded | pp | defined at 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 792 | `IF (pp .NE. 0.D0) MNWNOD(20, NODNUM + INODE - 1) = 1D30` |
| 838 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `IF (Rw .GT. 0.0) THEN` |
| 841 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 851 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `IF (Rw .GT. 0.0) THEN` |
| 852 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `IF (Rskin .GT. 0.0) THEN` |
| 853 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 855 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 856 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 857 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 860 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 861 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 865 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 867 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 868 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 871 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 876 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `IF (Rskin .GT. 0.0) THEN` |
| 877 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 879 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 880 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 883 | gwf2mnw27rp | uninitialized | loop-guarded | rskin | defined at 356 | `RskinNode = Rskin` |
| 887 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `IF (Kskin .GT. 0.0) THEN` |
| 889 | gwf2mnw27rp | uninitialized | loop-guarded | kskin | defined at 356 | `KskinNode = Kskin` |
| 903 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `IF (Rw .GT. 0.0) THEN` |
| 904 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `IF (B .GE. 0.0) THEN` |
| 905 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 906 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 908 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 909 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 910 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 911 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 914 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 915 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 916 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 920 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 922 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 923 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 924 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 927 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 928 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 933 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 934 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 936 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 937 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 938 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 941 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 942 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 946 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 948 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 949 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 952 | gwf2mnw27rp | uninitialized | loop-guarded | rw | defined at 349, 356, 370 | `RwNode = Rw` |
| 958 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `IF (B .GE. 0.0) THEN` |
| 959 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 960 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 962 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 963 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 964 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 967 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 968 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 972 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 974 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 975 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 978 | gwf2mnw27rp | uninitialized | loop-guarded | b | defined at 370 | `BNode = B` |
| 983 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `IF (C .GE. 0.0) THEN` |
| 984 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 986 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 987 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 990 | gwf2mnw27rp | uninitialized | loop-guarded | c | defined at 370 | `CNode = C` |
| 994 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `IF (P .GE. 0.0) THEN` |
| 996 | gwf2mnw27rp | uninitialized | loop-guarded | p | defined at 370 | `PNode = P` |
| 1012 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 380 | `IF (CWC .GT. 0.0) THEN` |
| 1014 | gwf2mnw27rp | uninitialized | loop-guarded | cwc | defined at 380 | `CWCNode = CWC` |
| 1022 | gwf2mnw27rp | uninitialized | loop-guarded | ztop | defined at 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016 | `MNWINT(1, INTNUM + IINT - 1) = Ztop` |
| 1023 | gwf2mnw27rp | uninitialized | loop-guarded | zbotm | defined at 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016 | `MNWINT(2, INTNUM + IINT - 1) = Zbotm` |
| 1024 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `MNWINT(3, INTNUM + IINT - 1) = IR` |
| 1025 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `MNWINT(4, INTNUM + IINT - 1) = IC` |
| 1029 | gwf2mnw27rp | uninitialized | loop-guarded | zbotmlast | defined at 1038 | `IF (Ztop .GT. Zbotmlast) THEN` |
| 1029 | gwf2mnw27rp | uninitialized | loop-guarded | ztop | defined at 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016 | `IF (Ztop .GT. Zbotmlast) THEN` |
| 1038 | gwf2mnw27rp | uninitialized | loop-guarded | zbotm | defined at 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016 | `Zbotmlast = Zbotm` |
| 1048 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `IRlast = IR` |
| 1049 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `IClast = IC` |
| 1051 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 1051 | gwf2mnw27rp | uninitialized | loop-guarded | iclast | defined at 798, 1049 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 1051 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 1051 | gwf2mnw27rp | uninitialized | loop-guarded | irlast | defined at 797, 1048 | `IF ((IR .NE. IRlast) .OR. (IC .NE. IClast)) THEN` |
| 1061 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `DO WHILE (Ztop .LE. BOTM(IC, IR, LBOTM(K)))` |
| 1061 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `DO WHILE (Ztop .LE. BOTM(IC, IR, LBOTM(K)))` |
| 1061 | gwf2mnw27rp | uninitialized | loop-guarded | ztop | defined at 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016 | `DO WHILE (Ztop .LE. BOTM(IC, IR, LBOTM(K)))` |
| 1076 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `IF (IBOUND(IC, IR, IL) .NE. 0) THEN` |
| 1076 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `IF (IBOUND(IC, IR, IL) .NE. 0) THEN` |
| 1095 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `MNWNOD(2, NODNUM) = IR` |
| 1096 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `MNWNOD(3, NODNUM) = IC` |
| 1113 | gwf2mnw27rp | uninitialized | loop-guarded | nodnum | defined at 393, 1079, 1122, 1167 | `IF (MNWNOD(1, NODNUM) .EQ. IL) THEN` |
| 1116 | gwf2mnw27rp | uninitialized | loop-guarded | nodnum | defined at 393, 1079, 1122, 1167 | `MNWNOD(13, NODNUM) = INTNUM + IINT - 1` |
| 1121 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `IF (IBOUND(IC, IR, IL) .NE. 0) THEN` |
| 1121 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `IF (IBOUND(IC, IR, IL) .NE. 0) THEN` |
| 1122 | gwf2mnw27rp | uninitialized | loop-guarded | nodnum | defined at 393, 1079, 1122, 1167 | `NODNUM = NODNUM + 1` |
| 1135 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `MNWNOD(2, NODNUM) = IR` |
| 1136 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `MNWNOD(3, NODNUM) = IC` |
| 1163 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `DO WHILE (Zbotm .LT. BOTM(IC, IR, LBOTM(K)) .AND. ((K + 1) .LE. NLAY))` |
| 1163 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `DO WHILE (Zbotm .LT. BOTM(IC, IR, LBOTM(K)) .AND. ((K + 1) .LE. NLAY))` |
| 1163 | gwf2mnw27rp | uninitialized | loop-guarded | zbotm | defined at 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016 | `DO WHILE (Zbotm .LT. BOTM(IC, IR, LBOTM(K)) .AND. ((K + 1) .LE. NLAY))` |
| 1167 | gwf2mnw27rp | uninitialized | loop-guarded | nodnum | defined at 393, 1079, 1122, 1167 | `NODNUM = NODNUM + 1` |
| 1180 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `MNWNOD(2, NODNUM) = IR` |
| 1181 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `MNWNOD(3, NODNUM) = IC` |
| 1508 | gwf2mnw27rp | uninitialized | loop-guarded | ic | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1474, 1511, 1529 | `IF (Zpump .LT. BOTM(IC, IR, LBOTM(IL) - 1) .AND. Zpump .GT. BOTM(IC, IR, LBOTM(IL))) THEN` |
| 1508 | gwf2mnw27rp | uninitialized | loop-guarded | ir | defined at 411, 416, 421, 431, 436, 443, 447, 455, 459, 465, 468, 483, 489, 497, 502, 511, 516, 523, 527, 537, 542, 549, 553, 561, 565, 571, 574, 588, 591, 601, 606, 611, 621, 626, 633, 637, 645, 649, 655, 658, 673, 679, 687, 692, 701, 706, 713, 717, 727, 732, 739, 743, 751, 755, 761, 764, 778, 781, 834, 839, 844, 854, 859, 866, 870, 878, 882, 888, 891, 907, 913, 921, 926, 935, 940, 947, 951, 961, 966, 973, 977, 985, 989, 995, 998, 1013, 1016, 1473, 1510, 1528 | `IF (Zpump .LT. BOTM(IC, IR, LBOTM(IL) - 1) .AND. Zpump .GT. BOTM(IC, IR, LBOTM(IL))) THEN` |
| 1797 | gwf2mnw27rp | uninitialized | loop-guarded | cprime | defined at 1699, 1713 | `MNW2(12, MNWID) = Cprime` |
| 1818 | gwf2mnw27rp | uninitialized | loop-guarded | capmult | defined at 1708, 1713, 1716 | `MNW2(24, MNWID) = CapMult` |
| 1822 | gwf2mnw27rp | uninitialized | loop-guarded | capmult | defined at 1708, 1713, 1716 | `WRITE(iout, 1113) CapMult` |
| 1830 | gwf2mnw27rp | uninitialized | loop-guarded | capmult | defined at 1708, 1713, 1716 | `IF (CapMult .EQ. 0.D0) THEN` |
| 1992 | gwf2mnw27ad | uninitialized | loop-guarded | ic | defined at 1965, 2022 | `hhnew = hnew(ic, ir, il)` |
| 1992 | gwf2mnw27ad | uninitialized | loop-guarded | il | defined at 1963, 2020 | `hhnew = hnew(ic, ir, il)` |
| 1992 | gwf2mnw27ad | uninitialized | loop-guarded | ir | defined at 1964, 2021 | `hhnew = hnew(ic, ir, il)` |
| 2060 | gwf2mnw27ad | uninitialized | loop-guarded | qpot | defined at 2006, 2034, 2063 | `ratio = qpot / qdes` |
| 2068 | gwf2mnw27ad | uninitialized | loop-guarded | qoff | defined at 1922, 1925, 1930, 1933 | `IF (ratio .LT. Qoff) THEN` |
| 2075 | gwf2mnw27ad | uninitialized | loop-guarded | qon | defined at 1923, 1926, 1931, 1934 | `ELSE IF (ratio .GT. Qon .AND. (ABS(qact) .LT. Qsmall)) THEN` |
| 2077 | gwf2mnw27ad | uninitialized | loop-guarded | qpot | defined at 2006, 2034, 2063 | `mnw2(30, iw) = Qpot` |
| 2078 | gwf2mnw27ad | uninitialized | loop-guarded | qpot | defined at 2006, 2034, 2063 | `MNWNOD(4, firstnode) = Qpot` |
| 2084 | gwf2mnw27ad | uninitialized | loop-guarded | qcut | defined at 1921 | `IF (QCUT .EQ. 0 .AND. ratio .GT. 0.D0) THEN` |
| 2086 | gwf2mnw27ad | uninitialized | loop-guarded | qpot | defined at 2006, 2034, 2063 | `mnw2(30, iw) = Qpot` |
| 2087 | gwf2mnw27ad | uninitialized | loop-guarded | qpot | defined at 2006, 2034, 2063 | `MNWNOD(4, firstnode) = Qpot` |
| 2264 | gwf2mnw27fm | uninitialized | loop-guarded | lasth | defined at 2158 | `htemp = ABS(lastH - hwell)` |
| 2268 | gwf2mnw27fm | uninitialized | call-assumed | qactcap | defined at 2161 | `mnw2(29, iw) = qactCap` |
| 2278 | gwf2mnw27fm | uninitialized | call-assumed | qactcap | defined at 2161 | `WRITE(iout, *) ' with Pump-Capacity Q = ', qactCap` |
| 2365 | gwf2mnw27fm | uninitialized | loop-guarded | hlim | defined at 2351 | `qact = (hlim - hhnew) * cond` |
| 2367 | gwf2mnw27fm | uninitialized | loop-guarded | hlim | defined at 2351 | `rhs(ic, ir, il) = rhs(ic, ir, il) - cond * hlim` |
| 2543 | gwf2mnw27bd | uninitialized | loop-guarded | iweldry | defined at 2473, 2480 | `IF (MNWPRNT .GT. 1 .AND. iweldry .EQ. 1) THEN` |
| 2601 | gwf2mnw27bd | uninitialized | loop-guarded | hwell | defined at 2504, 2657 | `IF (MNWNOD(15, INODE) .NE. hwell .AND. MNWNOD(15, INODE) .NE. Hdry .AND. numnddel .NE. 0) THEN` |
| 3353 | smnw2cond | uninitialized | loop-guarded | zbotm | defined at 3269, 3287 | `alpha2 = hwell - zbotm` |
| 3365 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3261, 3294, 3435 | `IF (totlength .GT. 0D0) THEN` |
| 3366 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3261, 3294, 3435 | `alpha3 = alpha2 / totlength` |
| 3412 | smnw2cond | uninitialized | loop-guarded | firstint | defined at 3258 | `IF (firstint .EQ. lastint) THEN` |
| 3412 | smnw2cond | uninitialized | loop-guarded | lastint | defined at 3259 | `IF (firstint .EQ. lastint) THEN` |
| 3413 | smnw2cond | uninitialized | loop-guarded | ztop | defined at 3268, 3286 | `topscreen = ztop` |
| 3414 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3261, 3294, 3435 | `bottomscreen = ztop - totlength` |
| 3414 | smnw2cond | uninitialized | loop-guarded | ztop | defined at 3268, 3286 | `bottomscreen = ztop - totlength` |
| 3419 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3261, 3294, 3435 | `topscreen = top - ((thck - totlength) / 2)` |
| 3420 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3261, 3294, 3435 | `bottomscreen = topscreen - totlength` |
| 3424 | smnw2cond | uninitialized | loop-guarded | totlength | defined at 3261, 3294, 3435 | `topscreen = zbotm + totlength` |
| 3424 | smnw2cond | uninitialized | loop-guarded | zbotm | defined at 3269, 3287 | `topscreen = zbotm + totlength` |
| 3425 | smnw2cond | uninitialized | loop-guarded | zbotm | defined at 3269, 3287 | `bottomscreen = zbotm` |
| 3489 | smnw2cond | uninitialized | call-assumed | isolnflag | defined at 3475 | `IF (ISOLNFLAG .EQ. 0 .AND. ITFLAG .GT. 0 .AND. QQ .NE. 0.D0) THEN` |
| 3517 | smnw2cond | uninitialized | loop-guarded | dhp | defined at 3393, 3475, 3481, 3513 | `MNWNOD(18, INODE) = dhp` |
| 3523 | smnw2cond | uninitialized | loop-guarded | bottomscreen | defined at 3414, 3420, 3425, 3439, 3443, 3452, 3583 | `ratio = (topscreen - bottomscreen) / thck` |
| 3523 | smnw2cond | uninitialized | loop-guarded | topscreen | defined at 3413, 3419, 3424, 3438, 3442, 3451, 3580 | `ratio = (topscreen - bottomscreen) / thck` |
| 3531 | smnw2cond | uninitialized | loop-guarded | dhp | defined at 3393, 3475, 3481, 3513 | `IF (ITFLAG .EQ. 1. .AND. (Qact .LT. 0.D0 .AND. dhp .GE. 0.D0) .OR. (Qact .GT. 0.D0 .AND. dhp .LE....` |
| 3537 | smnw2cond | uninitialized | loop-guarded | dhp | defined at 3393, 3475, 3481, 3513 | `dpp = dhp / (Qact * (- 1.D0))` |
| 3545 | smnw2cond | uninitialized | loop-guarded | dhp | defined at 3393, 3475, 3481, 3513 | `WRITE(iout, *) '***WARNING*** Partial penetration term (dpp) set to 0.0 due to misalignment of dh...` |
| 3579 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `IF (topscreen .GT. top) THEN` |
| 3579 | smnw2cond | uninitialized | loop-guarded | topscreen | defined at 3413, 3419, 3424, 3438, 3442, 3451, 3580 | `IF (topscreen .GT. top) THEN` |
| 3580 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `topscreen = top` |
| 3582 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `IF (mnwnod(21, inode) .LT. bot) THEN` |
| 3583 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `bottomscreen = bot` |
| 3588 | smnw2cond | uninitialized | loop-guarded | b | defined at 3228, 3232, 3310, 3314 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3588 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3588 | smnw2cond | uninitialized | loop-guarded | bottomscreen | defined at 3414, 3420, 3425, 3439, 3443, 3452, 3583 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3588 | smnw2cond | uninitialized | call-assumed | skin | defined at 3232, 3314 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3588 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3588 | smnw2cond | uninitialized | loop-guarded | topscreen | defined at 3413, 3419, 3424, 3438, 3442, 3451, 3580 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, topscreen, bottoms...` |
| 3594 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `WRITE(iout, '(A15,I3,1PG12.4,1x,5G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, topscreen,...` |
| 3594 | smnw2cond | uninitialized | loop-guarded | bottomscreen | defined at 3414, 3420, 3425, 3439, 3443, 3452, 3583 | `WRITE(iout, '(A15,I3,1PG12.4,1x,5G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, topscreen,...` |
| 3594 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `WRITE(iout, '(A15,I3,1PG12.4,1x,5G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, topscreen,...` |
| 3594 | smnw2cond | uninitialized | loop-guarded | topscreen | defined at 3413, 3419, 3424, 3438, 3442, 3451, 3580 | `WRITE(iout, '(A15,I3,1PG12.4,1x,5G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, topscreen,...` |
| 3605 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `t1 = top` |
| 3606 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `t2 = bot` |
| 3608 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `IF (mnwnod(20, inode) .GT. top) THEN` |
| 3609 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `t1 = top` |
| 3613 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `IF (mnwnod(21, inode) .LT. bot) THEN` |
| 3614 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `t2 = bot` |
| 3618 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `IF (mnwnod(21, inode) .GT. top) THEN` |
| 3626 | smnw2cond | uninitialized | loop-guarded | b | defined at 3228, 3232, 3310, 3314 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, alpha, S...` |
| 3626 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, alpha, S...` |
| 3626 | smnw2cond | uninitialized | call-assumed | skin | defined at 3232, 3314 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, alpha, S...` |
| 3626 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, alpha, S...` |
| 3633 | smnw2cond | uninitialized | loop-guarded | b | defined at 3228, 3232, 3310, 3314 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, alpha, Ski...` |
| 3633 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, alpha, Ski...` |
| 3633 | smnw2cond | uninitialized | call-assumed | skin | defined at 3232, 3314 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, alpha, Ski...` |
| 3633 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, alpha, Ski...` |
| 3641 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ' N/A ',...` |
| 3641 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ' N/A ',...` |
| 3645 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, ' N/A ', '...` |
| 3645 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `WRITE(iout, '(A15,I3,1PG12.4,1x,7G12.4,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, ' N/A ', '...` |
| 3658 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ...` |
| 3658 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ...` |
| 3663 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ...` |
| 3663 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, top, bot, ...` |
| 3672 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, al...` |
| 3672 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, al...` |
| 3677 | smnw2cond | uninitialized | loop-guarded | bot | defined at 3209 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, ' ...` |
| 3677 | smnw2cond | uninitialized | loop-guarded | top | defined at 3203, 3205, 3206 | `WRITE(iout, '(A15,I3,1PG12.4,1x,6G12.4,12A,12A,10A)') WELLID(iw), nod, cond, top, bot, t1, t2, ' ...` |
| 3812 | cel2wel2 | uninitialized | conditional | c | defined at 3795, 3799, 3801, 3805, 3810 | `cel2wel2 = A + B + C` |
| 3904 | smnw2seep | uninitialized | loop-guarded | ic | defined at 3891, 4036, 4129 | `hwell = hnew(ic, ir, il)` |
| 3904 | smnw2seep | uninitialized | loop-guarded | il | defined at 3889, 4034, 4127 | `hwell = hnew(ic, ir, il)` |
| 3904 | smnw2seep | uninitialized | loop-guarded | ir | defined at 3890, 4035, 4128 | `hwell = hnew(ic, ir, il)` |
| 3924 | smnw2seep | uninitialized | conditional | qpot | defined at 3917, 3927 | `ratio = qpot / qdes` |
| 3952 | smnw2seep | uninitialized | conditional | qpot | defined at 3917, 3927 | `mnw2(30, iw) = Qpot` |
| 4053 | smnw2seep | uninitialized | conditional | hwell | defined at 3887, 3902, 3904, 3915, 4083, 4085, 4097, 4108, 4110 | `IF (kSeep .GT. 1 .AND. hwell .LT. Bottom) THEN` |
| 4085 | smnw2seep | uninitialized | loop-guarded | ic | defined at 3891, 4036, 4129 | `hwell = hnew(ic, ir, il)` |
| 4085 | smnw2seep | uninitialized | loop-guarded | il | defined at 3889, 4034, 4127 | `hwell = hnew(ic, ir, il)` |
| 4085 | smnw2seep | uninitialized | loop-guarded | ir | defined at 3890, 4035, 4128 | `hwell = hnew(ic, ir, il)` |
| 4110 | smnw2seep | uninitialized | loop-guarded | ic | defined at 3891, 4036, 4129 | `hwell = hnew(ic, ir, il)` |
| 4110 | smnw2seep | uninitialized | loop-guarded | il | defined at 3889, 4034, 4127 | `hwell = hnew(ic, ir, il)` |
| 4110 | smnw2seep | uninitialized | loop-guarded | ir | defined at 3890, 4035, 4128 | `hwell = hnew(ic, ir, il)` |
| 4126 | smnw2seep | uninitialized | conditional | firstnode | defined at 3885, 4030 | `DO INODE = firstnode, lastnode` |
| 4126 | smnw2seep | uninitialized | conditional | lastnode | defined at 3886, 4031 | `DO INODE = firstnode, lastnode` |
| 4135 | smnw2seep | uninitialized | conditional | hwell | defined at 3887, 3902, 3904, 3915, 4083, 4085, 4097, 4108, 4110 | `qact = (hwell - hnew(ic, ir, il)) * MNWNOD(14, INODE)` |
| 4137 | smnw2seep | uninitialized | conditional | hwell | defined at 3887, 3902, 3904, 3915, 4083, 4085, 4097, 4108, 4110 | `MNWNOD(15, INODE) = hwell` |
| 4148 | smnw2seep | uninitialized | loop-guarded | qseep | defined at 4029, 4057 | `IF (ABS(seepchk) .LT. ABS(MNW2(18, IW)) .AND. qseep .NE. 0.0) LIMQ(3, IW) = 1` |
| 4220 | smnw2seep | uninitialized | conditional | hwell | defined at 3887, 3902, 3904, 3915, 4083, 4085, 4097, 4108, 4110 | `MNW2(17, iw) = hwell` |
| 4290 | gwf2mnw27bh | uninitialized | conditional | nodepump | defined at 4250, 4267 | `IF (nodepump .EQ. firstnode) THEN` |
| 4301 | gwf2mnw27bh | uninitialized | conditional | nodepump | defined at 4250, 4267 | `IF (nodepump .EQ. inode .AND. inode .NE. lastnode) THEN` |
| 4627 | mnw2horiz | uninitialized | loop-guarded | xi | defined at 4620, 4640, 4665, 4824, 4835, 4851 | `IF (x2face .EQ. xi) THEN` |
| 4628 | mnw2horiz | uninitialized | loop-guarded | xi | defined at 4620, 4640, 4665, 4824, 4835, 4851 | `lxf = SQRT(((x2 - xi) ** 2) + ((y2 - yi) ** 2) + ((z2 - zi) ** 2))` |
| 4652 | mnw2horiz | uninitialized | loop-guarded | yi | defined at 4615, 4645, 4666, 4819, 4840, 4852 | `IF (y2face .EQ. yi) THEN` |
| 4653 | mnw2horiz | uninitialized | loop-guarded | yi | defined at 4615, 4645, 4666, 4819, 4840, 4852 | `lyf = SQRT(((x2 - xi) ** 2) + ((y2 - yi) ** 2) + ((z2 - zi) ** 2))` |
| 4677 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 4616, 4641, 4670, 4820, 4836, 4856 | `IF (z2face .EQ. zi) THEN` |
| 4678 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 4616, 4641, 4670, 4820, 4836, 4856 | `lzf = SQRT(((x2 - xi) ** 2) + ((y2 - yi) ** 2) + ((z2 - zi) ** 2))` |
| 4746 | mnw2horiz | uninitialized | loop-guarded | xi | defined at 4620, 4640, 4665, 4824, 4835, 4851 | `IF (xi .EQ. xi2) THEN` |
| 4746 | mnw2horiz | uninitialized | loop-guarded | xi2 | defined at 4698, 4709, 4725 | `IF (xi .EQ. xi2) THEN` |
| 4750 | mnw2horiz | uninitialized | loop-guarded | xi | defined at 4620, 4640, 4665, 4824, 4835, 4851 | `xa = xi` |
| 4751 | mnw2horiz | uninitialized | loop-guarded | xi2 | defined at 4698, 4709, 4725 | `xb = xi2` |
| 4758 | mnw2horiz | uninitialized | loop-guarded | yi | defined at 4615, 4645, 4666, 4819, 4840, 4852 | `IF (yi .EQ. yi2) THEN` |
| 4758 | mnw2horiz | uninitialized | loop-guarded | yi2 | defined at 4693, 4714, 4726 | `IF (yi .EQ. yi2) THEN` |
| 4762 | mnw2horiz | uninitialized | loop-guarded | yi | defined at 4615, 4645, 4666, 4819, 4840, 4852 | `ya = yi` |
| 4763 | mnw2horiz | uninitialized | loop-guarded | yi2 | defined at 4693, 4714, 4726 | `yb = yi2` |
| 4770 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 4616, 4641, 4670, 4820, 4836, 4856 | `IF (zi .EQ. zi2) THEN` |
| 4770 | mnw2horiz | uninitialized | loop-guarded | zi2 | defined at 4694, 4710, 4730 | `IF (zi .EQ. zi2) THEN` |
| 4774 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 4616, 4641, 4670, 4820, 4836, 4856 | `za = zi` |
| 4775 | mnw2horiz | uninitialized | loop-guarded | zi2 | defined at 4694, 4710, 4730 | `zb = zi2` |
| 4787 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 4616, 4641, 4670, 4820, 4836, 4856 | `zseg2(inode) = zi` |
| 4788 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 4616, 4641, 4670, 4820, 4836, 4856 | `zseg1(inode + 1) = zi` |
| 4867 | mnw2horiz | uninitialized | loop-guarded | zi | defined at 4616, 4641, 4670, 4820, 4836, 4856 | `zseg2(inode + 1) = zi` |
| 5247 | cel2wel2seg | uninitialized | conditional | omega0 | defined at 5129 | `IF (omega0 .GT. 90.0) omega = 180.0 - omega` |
| 5324 | mnw2capacity | uninitialized | loop-guarded | ifirstl | defined at 5304 | `L1 = CapTable(iw, ifirstL, 1)` |
| 5325 | mnw2capacity | uninitialized | loop-guarded | isecondl | defined at 5305 | `L2 = CapTable(iw, isecondL, 1)` |
| 5326 | mnw2capacity | uninitialized | loop-guarded | ifirstl | defined at 5304 | `Q1 = CapTable(iw, ifirstL, 2)` |
| 5327 | mnw2capacity | uninitialized | loop-guarded | isecondl | defined at 5305 | `Q2 = CapTable(iw, isecondL, 2)` |
| 5821 | ltst2 | uninitialized | loop-guarded | sume | defined at 5741, 5798 | `E = SUME` |
| 5835 | ltst2 | uninitialized | loop-guarded | pdl | defined at 5819, 5822, 5825, 5830 | `XP = XP + V(I) * PDL` |

### gwf2mnw2i7.f90 (9)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 326 | gwf2mnw2i7ot | uninitialized | loop-guarded | seepflg | defined at 314, 420 | `IF (SEEPFLG .EQ. hwell .OR. SEEPFLG .EQ. Hdry) THEN` |
| 334 | gwf2mnw2i7ot | uninitialized | loop-guarded | cond | defined at 315, 421 | `hwell = HCELL + (q / COND)` |
| 334 | gwf2mnw2i7ot | uninitialized | loop-guarded | hcell | defined at 313, 367, 419 | `hwell = HCELL + (q / COND)` |
| 334 | gwf2mnw2i7ot | uninitialized | loop-guarded | q | defined at 269, 271, 311, 366, 424 | `hwell = HCELL + (q / COND)` |
| 435 | gwf2mnw2i7ot | uninitialized | loop-guarded | seepflg | defined at 314, 420 | `IF (SEEPFLG .NE. hwell .AND. SEEPFLG .NE. Hdry) THEN` |
| 439 | gwf2mnw2i7ot | uninitialized | loop-guarded | cond | defined at 315, 421 | `hwell = HCELL + (q / COND)` |
| 439 | gwf2mnw2i7ot | uninitialized | loop-guarded | hcell | defined at 313, 367, 419 | `hwell = HCELL + (q / COND)` |
| 439 | gwf2mnw2i7ot | uninitialized | loop-guarded | q | defined at 269, 271, 311, 366, 424 | `hwell = HCELL + (q / COND)` |
| 504 | gwf2mnw2i7ot | uninitialized | loop-guarded | sftest | defined at 434, 440 | `IF (sftest .LT. 1.0) THEN` |

### gwf2rch7.f90 (1)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 172 | gwf2rch7rp | uninitialized | conditional | inirch | defined at 118, 120 | `IF (INIRCH .LT. 0) THEN` |

### gwf2res7.f90 (4)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 419 | gwf2res7bd | uninitialized | loop-guarded | rate | defined at 413, 416 | `BUFF(IC, IR, IL) = BUFF(IC, IR, IL) + RATE` |
| 422 | gwf2res7bd | uninitialized | loop-guarded | rate | defined at 413, 416 | `IF (RATE) 94, 190, 96` |
| 426 | gwf2res7bd | uninitialized | loop-guarded | rate | defined at 413, 416 | `RATOUT = RATOUT - RATE` |
| 431 | gwf2res7bd | uninitialized | loop-guarded | rate | defined at 413, 416 | `RATIN = RATIN + RATE` |

### gwf2sfr7.f90 (373)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 558 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `IF (IBOUND(jrch, irch, krch) .LE. 0) WRITE(IOUT, 9018) ireach, jseg` |
| 558 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9018) ireach, jseg` |
| 558 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `IF (IBOUND(jrch, irch, krch) .LE. 0) WRITE(IOUT, 9018) ireach, jseg` |
| 558 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9018) ireach, jseg` |
| 558 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `IF (IBOUND(jrch, irch, krch) .LE. 0) WRITE(IOUT, 9018) ireach, jseg` |
| 575 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `THTR(ii) = THTS(ii) - SC2LPF(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 575 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `THTR(ii) = THTS(ii) - SC2LPF(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 575 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `THTR(ii) = THTS(ii) - SC2LPF(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 578 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `IF (LAYCON(krch) .LT. 2) THEN` |
| 579 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `THTR(ii) = THTS(ii) - SC1(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 579 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `THTR(ii) = THTS(ii) - SC1(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 579 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `THTR(ii) = THTS(ii) - SC1(jrch, irch, krch) / (DELR(jrch) * DELC(irch))` |
| 583 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `DO k = 1, krch` |
| 586 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `THTR(ii) = THTS(ii) - SC2(jrch, irch, kkrch) / (DELR(jrch) * DELC(irch))` |
| 586 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `THTR(ii) = THTS(ii) - SC2(jrch, irch, kkrch) / (DELR(jrch) * DELC(irch))` |
| 590 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `THTR(ii) = THTS(ii) - SC2HUF(jrch, irch)` |
| 590 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `THTR(ii) = THTS(ii) - SC2HUF(jrch, irch)` |
| 599 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 599 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 599 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 599 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 599 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 602 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 602 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 602 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 602 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 602 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 607 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 607 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 607 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 607 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 607 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 611 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 611 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 611 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 611 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 611 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9020) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 617 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 617 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 617 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 617 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 617 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 622 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 622 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 622 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 622 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 622 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9021) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 629 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 629 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 629 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 629 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 629 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 635 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 635 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 635 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 635 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 635 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9022) krch, irch, jrch, jseg, ireach, STRM(1, ii), STRM(3, ii), STRM(2, ii), STRM(8, ...` |
| 642 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 642 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 642 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 642 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 642 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii), ISTRM(6, ii)` |
| 645 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 645 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 645 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 645 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 645 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `WRITE(IOUT, 9019) krch, irch, jrch, jseg, ireach, STRM(1, ii)` |
| 658 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `IF (jseg .LE. 0 .OR. jseg .GT. NSS) THEN` |
| 662 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `IF (jseg .NE. nseg) THEN` |
| 665 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `IF (jseg .NE. nseg) THEN` |
| 671 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `IF (ireach .NE. nreach) THEN` |
| 679 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `ISTRM(1, ii) = krch` |
| 680 | gwf2sfr7ar | uninitialized | loop-guarded | irch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554, 710, 790 | `ISTRM(2, ii) = irch` |
| 681 | gwf2sfr7ar | uninitialized | loop-guarded | jrch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `ISTRM(3, ii) = jrch` |
| 682 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `ISTRM(4, ii) = jseg` |
| 683 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `ISTRM(5, ii) = ireach` |
| 686 | gwf2sfr7ar | uninitialized | loop-guarded | ireach | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `ISEG(4, jseg) = ireach` |
| 686 | gwf2sfr7ar | uninitialized | loop-guarded | jseg | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `ISEG(4, jseg) = ireach` |
| 688 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `uzfar_check % ltype = LAYHDT(krch)` |
| 734 | gwf2sfr7ar | uninitialized | loop-guarded | thsslpe | defined at 719 | `THTS(irch) = SEG(18, nseg) - (thsslpe * dist)` |
| 735 | gwf2sfr7ar | uninitialized | loop-guarded | thislpe | defined at 720 | `THTI(irch) = SEG(19, nseg) - (thislpe * dist)` |
| 736 | gwf2sfr7ar | uninitialized | loop-guarded | epsslpe | defined at 721 | `EPS(irch) = SEG(20, nseg) - (epsslpe * dist)` |
| 737 | gwf2sfr7ar | uninitialized | loop-guarded | uhcslpe | defined at 722 | `UHC(irch) = SEG(21, nseg) - (uhcslpe * dist)` |
| 755 | gwf2sfr7ar | uninitialized | loop-guarded | krch | defined at 493, 496, 501, 505, 517, 522, 534, 539, 551, 554 | `DO k = 1, krch` |
| 1108 | parsesfroptions | uninitialized | conditional | iostat | defined at 990 | `IF (Iostat .NE. 0) THEN` |
| 1498 | gwf2sfr7rp | uninitialized | loop-guarded | hcslpe | defined at 1487 | `avhc = SEG(6, nseg) - (hcslpe * dist)` |
| 1499 | gwf2sfr7rp | uninitialized | loop-guarded | thkslpe | defined at 1488 | `avthk = SEG(7, nseg) - (thkslpe * dist)` |
| 1500 | gwf2sfr7rp | uninitialized | loop-guarded | elslpe | defined at 1486 | `STRM(2, irch) = elslpe` |
| 1501 | gwf2sfr7rp | uninitialized | loop-guarded | elslpe | defined at 1486 | `STRM(3, irch) = SEG(8, nseg) - (elslpe * dist)` |
| 1529 | gwf2sfr7rp | uninitialized | loop-guarded | dpslpe | defined at 1481 | `avdpth = SEG(10, nseg) - (dpslpe * dist)` |
| 1530 | gwf2sfr7rp | uninitialized | loop-guarded | wdslpe | defined at 1480 | `STRM(5, irch) = SEG(9, nseg) - (wdslpe * dist)` |
| 1535 | gwf2sfr7rp | uninitialized | loop-guarded | avhc | defined at 1498 | `STRM(16, irch) = (avhc * STRM(5, irch) * rchlen) / avthk` |
| 1535 | gwf2sfr7rp | uninitialized | loop-guarded | avthk | defined at 1499, 1747 | `STRM(16, irch) = (avhc * STRM(5, irch) * rchlen) / avthk` |
| 1538 | gwf2sfr7rp | uninitialized | loop-guarded | wdslpe | defined at 1480 | `STRM(5, irch) = SEG(9, nseg) - (wdslpe * dist)` |
| 1543 | gwf2sfr7rp | uninitialized | loop-guarded | avhc | defined at 1498 | `STRM(16, irch) = (avhc * STRM(5, irch) * rchlen) / avthk` |
| 1543 | gwf2sfr7rp | uninitialized | loop-guarded | avthk | defined at 1499, 1747 | `STRM(16, irch) = (avhc * STRM(5, irch) * rchlen) / avthk` |
| 1648 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1641 | `dpthlw = QSTAGE(1 + nstrpts, nseg)` |
| 1651 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1641 | `QSTAGE(1 + nstrpts, nseg) = 0.01` |
| 1653 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1641 | `wdthlw = QSTAGE(1 + 2 * nstrpts, nseg)` |
| 1656 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1641 | `QSTAGE(1 + 2 * nstrpts, nseg) = 1.0` |
| 1658 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1641 | `DO ipt = 2, nstrpts` |
| 1661 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1641 | `dpth1 = QSTAGE((ipt - 1) + nstrpts, nseg)` |
| 1662 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1641 | `dpth2 = QSTAGE(ipt + nstrpts, nseg)` |
| 1663 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1641 | `wdth1 = QSTAGE((ipt - 1) + (2 * nstrpts), nseg)` |
| 1664 | gwf2sfr7rp | uninitialized | loop-guarded | nstrpts | defined at 1641 | `wdth2 = QSTAGE(ipt + (2 * nstrpts), nseg)` |
| 1751 | gwf2sfr7rp | uninitialized | loop-guarded | avdpth | defined at 1529 | `STRM(15, irch) = avdpth + STRM(3, irch)` |
| 2239 | gwf2sfr7fm | uninitialized | conditional | thet1 | defined at 2131, 2133 | `stgon = (1.0 - thet1) * STGOLD(lk) + thet1 * STGNEW(lk)` |
| 2246 | gwf2sfr7fm | uninitialized | loop-guarded | roughch | defined at 2184, 2253, 2480, 2553, 2597, 2619, 2736, 2739, 2742, 2745, 2748, 2751, 2872, 2909, 3009, 3053, 3101 | `flowin = (CONST / roughch) * widthch * smooth(dlkstr, dwdh) * (dlkstr ** FIVE_THIRDS) * (DSQRT(sl...` |
| 2246 | gwf2sfr7fm | uninitialized | loop-guarded | widthch | defined at 2185 | `flowin = (CONST / roughch) * widthch * smooth(dlkstr, dwdh) * (dlkstr ** FIVE_THIRDS) * (DSQRT(sl...` |
| 2372 | gwf2sfr7fm | uninitialized | loop-guarded | roughch | defined at 2184, 2253, 2480, 2553, 2597, 2619, 2736, 2739, 2742, 2745, 2748, 2751, 2872, 2909, 3009, 3053, 3101 | `qcnst = CONST * width * SQRT(slope) / roughch` |
| 2448 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2372, 3350 | `depth = (flwmpt / qcnst) ** 0.6D0` |
| 2484 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `depth = cdpth * (flwest ** fdpth)` |
| 2484 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `depth = cdpth * (flwest ** fdpth)` |
| 2485 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `width = awdth * (flwest ** bwdth)` |
| 2485 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `width = awdth * (flwest ** bwdth)` |
| 2506 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (h .LE. strtop .AND. flowc .LT. NEARZERO) iflg = 0` |
| 2527 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `flwen1 = flwmpt - 0.5D0 * flobot1` |
| 2530 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `flwen1 = flwmpt` |
| 2545 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flobot2 .GT. flowc) flobot2 = flowc` |
| 2546 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `depth2 = ((flwmpt - 0.5D0 * flobot2) / qcnst) ** 0.6D0` |
| 2546 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2372, 3350 | `depth2 = ((flwmpt - 0.5D0 * flobot2) / qcnst) ** 0.6D0` |
| 2547 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `depth1 = ((flwmpt - 0.5D0 * flobot1) / qcnst) ** 0.6D0` |
| 2547 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2372, 3350 | `depth1 = ((flwmpt - 0.5D0 * flobot1) / qcnst) ** 0.6D0` |
| 2557 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `flwen2 = (enpt2 / cdpth) ** (1.0 / fdpth)` |
| 2557 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `flwen2 = (enpt2 / cdpth) ** (1.0 / fdpth)` |
| 2559 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `width2 = awdth * (flwen2 ** bwdth)` |
| 2559 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `width2 = awdth * (flwen2 ** bwdth)` |
| 2573 | gwf2sfr7fm | uninitialized | loop-guarded | width2 | defined at 2553, 2559, 2562, 2566, 2614, 2619, 2625, 2628, 2649, 2679, 2693, 2751, 2767, 2770, 2815 | `IF (width2 .GT. NEARZERO) THEN` |
| 2574 | gwf2sfr7fm | uninitialized | loop-guarded | width2 | defined at 2553, 2559, 2562, 2566, 2614, 2619, 2625, 2628, 2649, 2679, 2693, 2751, 2767, 2770, 2815 | `flwpet2 = (precip - etstr) * width2` |
| 2580 | gwf2sfr7fm | uninitialized | loop-guarded | wetperm2 | defined at 2553, 2560, 2563, 2568, 2582, 2615, 2619, 2626, 2650, 2751, 2768, 2771, 2822, 2849 | `flobot2 = ((avhc * wetperm2 * strlen / sbdthk) * (strtop - h))` |
| 2587 | gwf2sfr7fm | uninitialized | loop-guarded | wetperm2 | defined at 2553, 2560, 2563, 2568, 2582, 2615, 2619, 2626, 2650, 2751, 2768, 2771, 2822, 2849 | `flobot2 = ((avhc * wetperm2 * strlen / sbdthk) * (strtop + enpt2 - sbot))` |
| 2590 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `flwmpt2 = flwmpt` |
| 2591 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flobot2 .GE. flowc + flwpet2) THEN` |
| 2592 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `flobot2 = flowc + flwpet2` |
| 2593 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `flwmpt2 = 0.5D0 * (flowc + flwpet2)` |
| 2602 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `depth1 = cdpth * (flwen1 ** fdpth)` |
| 2602 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `depth1 = cdpth * (flwen1 ** fdpth)` |
| 2603 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `width1 = awdth * (flwen1 ** bwdth)` |
| 2603 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `width1 = awdth * (flwen1 ** bwdth)` |
| 2624 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `depth2 = cdpth * (flwen2 ** fdpth)` |
| 2624 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `depth2 = cdpth * (flwen2 ** fdpth)` |
| 2625 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `width2 = awdth * (flwen2 ** bwdth)` |
| 2625 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `width2 = awdth * (flwen2 ** bwdth)` |
| 2634 | gwf2sfr7fm | uninitialized | loop-guarded | depth1 | defined at 2547, 2597, 2602, 2606, 2668, 2678, 2680, 2685, 2690, 2697, 2748, 2813, 2846 | `IF (depth1 .GT. NEARZERO) THEN` |
| 2635 | gwf2sfr7fm | uninitialized | loop-guarded | depth1 | defined at 2547, 2597, 2602, 2606, 2668, 2678, 2680, 2685, 2690, 2697, 2748, 2813, 2846 | `f1 = enpt1 - depth1` |
| 2644 | gwf2sfr7fm | uninitialized | loop-guarded | depth2 | defined at 2546, 2613, 2619, 2624, 2628, 2648, 2669, 2679, 2682, 2687, 2693, 2699, 2731, 2751, 2777, 2815, 2849 | `IF (depth2 .GT. NEARZERO) THEN` |
| 2645 | gwf2sfr7fm | uninitialized | loop-guarded | depth2 | defined at 2546, 2613, 2619, 2624, 2628, 2648, 2669, 2679, 2682, 2687, 2693, 2699, 2731, 2751, 2777, 2815, 2849 | `f2 = enpt2 - depth2` |
| 2646 | gwf2sfr7fm | uninitialized | loop-guarded | depth2 | defined at 2546, 2613, 2619, 2624, 2628, 2648, 2669, 2679, 2682, 2687, 2693, 2699, 2731, 2751, 2777, 2815, 2849 | `enpt2 = depth2` |
| 2680 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2372, 3350 | `flwmdpt1 = smooth(depth1, dwdh) * qcnst * (depth1 ** FIVE_THIRDS)` |
| 2682 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2372, 3350 | `flwmdpt2 = smooth(depth2, dwdh) * qcnst * (depth2 ** FIVE_THIRDS)` |
| 2704 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flobot1 .GE. flowc) THEN` |
| 2714 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `flobotp = flowc` |
| 2714 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `IF (0.5D0 * flobotp .GT. flwmpt) flobotp = flowc` |
| 2716 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `depthx = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** 0.6D0` |
| 2716 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2372, 3350 | `depthx = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** 0.6D0` |
| 2720 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `fhstr1 = (flwmpt - 0.5D0 * flobot1) - (flwmdpt1)` |
| 2721 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `fhstr2 = (flwmpt - 0.5D0 * flobot2) - (flwmdpt2)` |
| 2757 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `flwmdpt1 = (depth1 / cdpth) ** (1.0 / fdpth)` |
| 2757 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `flwmdpt1 = (depth1 / cdpth) ** (1.0 / fdpth)` |
| 2758 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `flwmdpt2 = (depth2 / cdpth) ** (1.0 / fdpth)` |
| 2758 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `flwmdpt2 = (depth2 / cdpth) ** (1.0 / fdpth)` |
| 2760 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `width1 = awdth * (flwmdpt1 ** bwdth)` |
| 2760 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `width1 = awdth * (flwmdpt1 ** bwdth)` |
| 2766 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt2 | defined at 2590, 2593 | `IF (flwmpt2 .GT. NEARZERO) THEN` |
| 2767 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `width2 = awdth * (flwmdpt2 ** bwdth)` |
| 2767 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `width2 = awdth * (flwmdpt2 ** bwdth)` |
| 2782 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `flwmdpta = (deptha / cdpth) ** (1.0 / fdpth)` |
| 2782 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `flwmdpta = (deptha / cdpth) ** (1.0 / fdpth)` |
| 2783 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `flwmdptb = (depthb / cdpth) ** (1.0 / fdpth)` |
| 2783 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `flwmdptb = (depthb / cdpth) ** (1.0 / fdpth)` |
| 2784 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `flwmdptc = (depthc / cdpth) ** (1.0 / fdpth)` |
| 2784 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `flwmdptc = (depthc / cdpth) ** (1.0 / fdpth)` |
| 2785 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `flwmdptd = (depthd / cdpth) ** (1.0 / fdpth)` |
| 2785 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `flwmdptd = (depthd / cdpth) ** (1.0 / fdpth)` |
| 2786 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `widtha = awdth * (flwmdpta ** bwdth)` |
| 2786 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `widtha = awdth * (flwmdpta ** bwdth)` |
| 2787 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `widthb = awdth * (flwmdptb ** bwdth)` |
| 2787 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `widthb = awdth * (flwmdptb ** bwdth)` |
| 2788 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `widthc = awdth * (flwmdptc ** bwdth)` |
| 2788 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `widthc = awdth * (flwmdptc ** bwdth)` |
| 2789 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `widthd = awdth * (flwmdptd ** bwdth)` |
| 2789 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `widthd = awdth * (flwmdptd ** bwdth)` |
| 2827 | gwf2sfr7fm | uninitialized | loop-guarded | deptha | defined at 2727, 2728, 2736, 2773, 2774, 2797, 2798, 2805 | `dlpp1 = (precip * (widtha - widthb)) / (deptha - depthb)` |
| 2827 | gwf2sfr7fm | uninitialized | loop-guarded | depthb | defined at 2729, 2730, 2739, 2775, 2776, 2799, 2800, 2807 | `dlpp1 = (precip * (widtha - widthb)) / (deptha - depthb)` |
| 2827 | gwf2sfr7fm | uninitialized | loop-guarded | widtha | defined at 2736, 2786, 2805, 2872 | `dlpp1 = (precip * (widtha - widthb)) / (deptha - depthb)` |
| 2827 | gwf2sfr7fm | uninitialized | loop-guarded | widthb | defined at 2739, 2787, 2807 | `dlpp1 = (precip * (widtha - widthb)) / (deptha - depthb)` |
| 2828 | gwf2sfr7fm | uninitialized | loop-guarded | depthc | defined at 2732, 2733, 2742, 2778, 2779, 2801, 2802, 2809 | `dlpp2 = (precip * (widthc - widthd)) / (depthc - depthd)` |
| 2828 | gwf2sfr7fm | uninitialized | loop-guarded | depthd | defined at 2734, 2735, 2745, 2780, 2781, 2803, 2804, 2811 | `dlpp2 = (precip * (widthc - widthd)) / (depthc - depthd)` |
| 2828 | gwf2sfr7fm | uninitialized | loop-guarded | widthc | defined at 2742, 2788, 2809 | `dlpp2 = (precip * (widthc - widthd)) / (depthc - depthd)` |
| 2828 | gwf2sfr7fm | uninitialized | loop-guarded | widthd | defined at 2745, 2789, 2811 | `dlpp2 = (precip * (widthc - widthd)) / (depthc - depthd)` |
| 2829 | gwf2sfr7fm | uninitialized | loop-guarded | deptha | defined at 2727, 2728, 2736, 2773, 2774, 2797, 2798, 2805 | `dlet1 = (etstr * (widtha - widthb)) / (deptha - depthb)` |
| 2829 | gwf2sfr7fm | uninitialized | loop-guarded | depthb | defined at 2729, 2730, 2739, 2775, 2776, 2799, 2800, 2807 | `dlet1 = (etstr * (widtha - widthb)) / (deptha - depthb)` |
| 2829 | gwf2sfr7fm | uninitialized | loop-guarded | widtha | defined at 2736, 2786, 2805, 2872 | `dlet1 = (etstr * (widtha - widthb)) / (deptha - depthb)` |
| 2829 | gwf2sfr7fm | uninitialized | loop-guarded | widthb | defined at 2739, 2787, 2807 | `dlet1 = (etstr * (widtha - widthb)) / (deptha - depthb)` |
| 2830 | gwf2sfr7fm | uninitialized | loop-guarded | depthc | defined at 2732, 2733, 2742, 2778, 2779, 2801, 2802, 2809 | `dlet2 = (etstr * (widthc - widthd)) / (depthc - depthd)` |
| 2830 | gwf2sfr7fm | uninitialized | loop-guarded | depthd | defined at 2734, 2735, 2745, 2780, 2781, 2803, 2804, 2811 | `dlet2 = (etstr * (widthc - widthd)) / (depthc - depthd)` |
| 2830 | gwf2sfr7fm | uninitialized | loop-guarded | widthc | defined at 2742, 2788, 2809 | `dlet2 = (etstr * (widthc - widthd)) / (depthc - depthd)` |
| 2830 | gwf2sfr7fm | uninitialized | loop-guarded | widthd | defined at 2745, 2789, 2811 | `dlet2 = (etstr * (widthc - widthd)) / (depthc - depthd)` |
| 2831 | gwf2sfr7fm | uninitialized | loop-guarded | deptha | defined at 2727, 2728, 2736, 2773, 2774, 2797, 2798, 2805 | `dlwp1 = (wetperma - wetpermb) / (deptha - depthb)` |
| 2831 | gwf2sfr7fm | uninitialized | loop-guarded | depthb | defined at 2729, 2730, 2739, 2775, 2776, 2799, 2800, 2807 | `dlwp1 = (wetperma - wetpermb) / (deptha - depthb)` |
| 2831 | gwf2sfr7fm | uninitialized | loop-guarded | wetperma | defined at 2736, 2790, 2817 | `dlwp1 = (wetperma - wetpermb) / (deptha - depthb)` |
| 2831 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermb | defined at 2739, 2791, 2818 | `dlwp1 = (wetperma - wetpermb) / (deptha - depthb)` |
| 2832 | gwf2sfr7fm | uninitialized | loop-guarded | depthc | defined at 2732, 2733, 2742, 2778, 2779, 2801, 2802, 2809 | `dlwp2 = (wetpermc - wetpermd) / (depthc - depthd)` |
| 2832 | gwf2sfr7fm | uninitialized | loop-guarded | depthd | defined at 2734, 2735, 2745, 2780, 2781, 2803, 2804, 2811 | `dlwp2 = (wetpermc - wetpermd) / (depthc - depthd)` |
| 2832 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermc | defined at 2742, 2792, 2819 | `dlwp2 = (wetpermc - wetpermd) / (depthc - depthd)` |
| 2832 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermd | defined at 2745, 2793, 2820 | `dlwp2 = (wetpermc - wetpermd) / (depthc - depthd)` |
| 2834 | gwf2sfr7fm | uninitialized | loop-guarded | width1 | defined at 2597, 2603, 2606, 2638, 2678, 2690, 2748, 2760, 2763, 2813 | `pp1 = precip * (width1) + dlpp1 * dlh` |
| 2835 | gwf2sfr7fm | uninitialized | loop-guarded | width2 | defined at 2553, 2559, 2562, 2566, 2614, 2619, 2625, 2628, 2649, 2679, 2693, 2751, 2767, 2770, 2815 | `pp2 = precip * (width2) + dlpp2 * dlh` |
| 2836 | gwf2sfr7fm | uninitialized | loop-guarded | width1 | defined at 2597, 2603, 2606, 2638, 2678, 2690, 2748, 2760, 2763, 2813 | `et1 = etstr * (width1) + dlet1 * dlh` |
| 2837 | gwf2sfr7fm | uninitialized | loop-guarded | width2 | defined at 2553, 2559, 2562, 2566, 2614, 2619, 2625, 2628, 2649, 2679, 2693, 2751, 2767, 2770, 2815 | `et2 = etstr * (width2) + dlet2 * dlh` |
| 2838 | gwf2sfr7fm | uninitialized | loop-guarded | wetperm1 | defined at 2597, 2604, 2639, 2748, 2761, 2764, 2821, 2846 | `cstr1 = ((wetperm1 + dlwp1 * dlh) * strleak) / sbdthk` |
| 2839 | gwf2sfr7fm | uninitialized | loop-guarded | wetperm2 | defined at 2553, 2560, 2563, 2568, 2582, 2615, 2619, 2626, 2650, 2751, 2768, 2771, 2822, 2849 | `cstr2 = ((wetperm2 + dlwp2 * dlh) * strleak) / sbdthk` |
| 2858 | gwf2sfr7fm | uninitialized | loop-guarded | width1 | defined at 2597, 2603, 2606, 2638, 2678, 2690, 2748, 2760, 2763, 2813 | `IF (width1 .GT. NEARZERO) THEN` |
| 2860 | gwf2sfr7fm | uninitialized | loop-guarded | width1 | defined at 2597, 2603, 2606, 2638, 2678, 2690, 2748, 2760, 2763, 2813 | `flwpet1 = precip * width1 + (dlpp1 * dlh) - etstr * width1 + (dlet1 * dlh)` |
| 2868 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flobot1 .GT. flowc + flwpet1) THEN` |
| 2876 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `flwx = (depthp / cdpth) ** (1.0 / fdpth)` |
| 2876 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `flwx = (depthp / cdpth) ** (1.0 / fdpth)` |
| 2878 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `widthp = awdth * (flwx ** bwdth)` |
| 2878 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `widthp = awdth * (flwx ** bwdth)` |
| 2889 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 2872, 2879, 2882, 2887, 2893, 2909, 3009, 3015, 3018, 3024, 3036, 3053, 3060, 3063, 3069, 3081 | `cstr1 = wetpermp * strleak / sbdthk` |
| 2900 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flobotp .GT. flowc + flwpet1) flobotp = flowc + flwpet1` |
| 2902 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `flwmpt = flwmpt + 0.5D0 * flwpet1` |
| 2913 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `depthx = cdpth * (flwx ** fdpth)` |
| 2913 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `depthx = cdpth * (flwx ** fdpth)` |
| 2915 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `widthx = awdth * (flwx ** bwdth)` |
| 2915 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `widthx = awdth * (flwx ** bwdth)` |
| 2925 | gwf2sfr7fm | uninitialized | loop-guarded | flwmdpt1 | defined at 2680, 2748, 2757, 2813 | `fhstr1 = (flwmpt - 0.5D0 * (pp1 - et1 + flobot1)) - (flwmdpt1)` |
| 2925 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `fhstr1 = (flwmpt - 0.5D0 * (pp1 - et1 + flobot1)) - (flwmdpt1)` |
| 2926 | gwf2sfr7fm | uninitialized | loop-guarded | flwmdpt2 | defined at 2682, 2751, 2758, 2815 | `fhstr2 = (flwmpt - 0.5D0 * (pp2 - et2 + flobot2)) - (flwmdpt2)` |
| 2926 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `fhstr2 = (flwmpt - 0.5D0 * (pp2 - et2 + flobot2)) - (flwmdpt2)` |
| 2998 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flobotp .GE. flowc) THEN` |
| 2999 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `flobotp = flowc` |
| 3000 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `depthp = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** .6D0` |
| 3000 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2372, 3350 | `depthp = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** .6D0` |
| 3005 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `depthx = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** 0.6D0` |
| 3005 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2372, 3350 | `depthx = ((flwmpt - 0.5D0 * flobotp) / (smooth(depthp, dwdh) * qcnst)) ** 0.6D0` |
| 3012 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `flwp = (depthp / cdpth) ** (1.0 / fdpth)` |
| 3012 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `flwp = (depthp / cdpth) ** (1.0 / fdpth)` |
| 3014 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `widthp = awdth * (flwp ** bwdth)` |
| 3014 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `widthp = awdth * (flwp ** bwdth)` |
| 3033 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 2872, 2879, 2882, 2887, 2893, 2909, 3009, 3015, 3018, 3024, 3036, 3053, 3060, 3063, 3069, 3081 | `flobotp = ((avhc * wetpermp * strlen / sbdthk) * (strtop + depthp - h))` |
| 3041 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 2872, 2879, 2882, 2887, 2893, 2909, 3009, 3015, 3018, 3024, 3036, 3053, 3060, 3063, 3069, 3081 | `flobotp = ((avhc * wetpermp * strlen / sbdthk) * (strtop + depthp - sbot))` |
| 3044 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `flwmpt = flwmpt + 0.5D0 * flwpetp` |
| 3049 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flobotp .GT. flowc + flwpetp) THEN` |
| 3057 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `flwp = (depthp / cdpth) ** (1.0 / fdpth)` |
| 3057 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `flwp = (depthp / cdpth) ** (1.0 / fdpth)` |
| 3059 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `widthp = awdth * (flwp ** bwdth)` |
| 3059 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `widthp = awdth * (flwp ** bwdth)` |
| 3078 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 2872, 2879, 2882, 2887, 2893, 2909, 3009, 3015, 3018, 3024, 3036, 3053, 3060, 3063, 3069, 3081 | `flobotp = ((avhc * wetpermp * strlen / sbdthk) * (strtop + depthp - h))` |
| 3086 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 2872, 2879, 2882, 2887, 2893, 2909, 3009, 3015, 3018, 3024, 3036, 3053, 3060, 3063, 3069, 3081 | `flobotp = ((avhc * wetpermp * strlen / sbdthk) * (strtop + depthp - sbot))` |
| 3091 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flobotp .GE. flowc + flwpetp) flobotp = flowc + flwpetp` |
| 3105 | gwf2sfr7fm | uninitialized | loop-guarded | cdpth | defined at 2259, 2374, 3350 | `depthx = cdpth * (flwx ** fdpth)` |
| 3105 | gwf2sfr7fm | uninitialized | loop-guarded | fdpth | defined at 2260, 2375, 3350 | `depthx = cdpth * (flwx ** fdpth)` |
| 3106 | gwf2sfr7fm | uninitialized | loop-guarded | awdth | defined at 2376, 3350 | `widthx = awdth * (flwx ** bwdth)` |
| 3106 | gwf2sfr7fm | uninitialized | loop-guarded | bwdth | defined at 2377, 3350 | `widthx = awdth * (flwx ** bwdth)` |
| 3149 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 2872, 2879, 2882, 2887, 2893, 2909, 3009, 3015, 3018, 3024, 3036, 3053, 3060, 3063, 3069, 3081 | `wetperm = wetpermp` |
| 3169 | gwf2sfr7fm | uninitialized | loop-guarded | errold | defined at 3191 | `WRITE(IOUT, 9003) istsg, nreach, Kkiter, err, errold` |
| 3178 | gwf2sfr7fm | uninitialized | loop-guarded | wetpermp | defined at 2872, 2879, 2882, 2887, 2893, 2909, 3009, 3015, 3018, 3024, 3036, 3053, 3060, 3063, 3069, 3081 | `wetperm = wetpermp` |
| 3215 | gwf2sfr7fm | uninitialized | loop-guarded | qcnst | defined at 2372, 3350 | `depth = (flwmpt / (smooth(depth, dwdh) * qcnst)) ** 0.6D0` |
| 3229 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `etstr = flowin + runof + runoff + precip - flobot` |
| 3257 | gwf2sfr7fm | uninitialized | loop-guarded | nstrpts | defined at 2188, 2265, 2488, 2566, 2606, 2628, 2805, 2807, 2809, 2811, 2813, 2815, 2885, 2918, 3021, 3066, 3109 | `width = QSTAGE((1 + 2 * nstrpts), istsg) + QSTAGE(3 * nstrpts, istsg) / 2.0D0` |
| 3280 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flowc .LT. NEARZERO) THEN` |
| 3317 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flowc .GT. NEARZERO .AND. icalccheck .EQ. 1) THEN` |
| 3333 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `IF (flobot .GE. flowc) flobot = flowc` |
| 3333 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `IF (flobot .GE. flowc) flobot = flowc` |
| 3344 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `IF (flobot .LT. 0.0D0) THEN` |
| 3345 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `fltest = qa + qb + qc + qlat * strlen - flobot` |
| 3369 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `flowot = flowc - flobot` |
| 3369 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `flowot = flowc - flobot` |
| 3370 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `qc = flowc` |
| 3374 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `flobot = flowc` |
| 3375 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `flwmpt = 0.5D0 * flowc` |
| 3381 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `SUMLEAK(l) = SUMLEAK(l) + (flobot * deltinc)` |
| 3384 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `SUMLEAK(l) = flobot` |
| 3392 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `STRM(11, l) = flobot` |
| 3452 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `SUMRCH(l) = SUMRCH(l) + flobot` |
| 3455 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `SUMRCH(l) = SUMRCH(l) + flobot` |
| 3462 | gwf2sfr7fm | uninitialized | loop-guarded | flwmpt | defined at 2435, 2439, 2444, 2445, 2457, 2463, 2902, 3044, 3089, 3153, 3160, 3181, 3187, 3210, 3212, 3262, 3267, 3375 | `SFRQ(1, l) = flwmpt` |
| 3463 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `SFRQ(2, l) = flowc` |
| 3464 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `SFRQ(3, l) = flobot` |
| 3469 | gwf2sfr7fm | uninitialized | loop-guarded | flobot | defined at 3146, 3175, 3283, 3285, 3307, 3308, 3310, 3311, 3314, 3320, 3333, 3350, 3374, 3424 | `SFRQ(3, l) = flobot` |
| 3491 | gwf2sfr7fm | uninitialized | loop-guarded | flowc | defined at 2437, 2443, 2446, 2458, 2459, 2493, 3151, 3158, 3179, 3186, 3209, 3233, 3260, 3265, 3305, 3360, 3418 | `ELSE IF (SUMLEAK(l) - flowc .LT. - CLOSEZERO) THEN` |
| 3683 | gwf2sfr7bd | interface | argument-rank-character | ubdsv4(5) | actual 'IFACE ' is a character scalar, dummy auxtxt is a character array at utl7.f90:1610 | `CALL UBDSV4(Kkstp, Kkper, text, naux, 'IFACE ', iout1, NCOL, NROW, NLAY, NSTRM, IOUT, DELT, PERTI...` |
| 3983 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `flow = flowin + runof + runoff + precip - etstr` |
| 3983 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `flow = flowin + runof + runoff + precip - etstr` |
| 3989 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `IF (flowin + runoff + precip .LT. NEARZERO) THEN` |
| 3992 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `ELSE IF (runof .GE. flowin + runoff + precip - etstr) THEN` |
| 3992 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `ELSE IF (runof .GE. flowin + runoff + precip - etstr) THEN` |
| 3993 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `runof = flowin + runoff + precip - etstr` |
| 3993 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `runof = flowin + runoff + precip - etstr` |
| 3994 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `ELSE IF (etstr .GE. flowin + runoff + precip + runof) THEN` |
| 3994 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `ELSE IF (etstr .GE. flowin + runoff + precip + runof) THEN` |
| 3995 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `etstr = flowin + runoff + precip + runof` |
| 3997 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `ELSE IF (flowin + runof + runoff + precip .GT. NEARZERO) THEN` |
| 3998 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `etstr = flowin + runof + runoff + precip` |
| 4003 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `IF (flowin + runoff + precip - flobot .LT. NEARZERO) THEN` |
| 4006 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `ELSE IF (runof .GE. flowin + runoff + precip - flobot - etstr) THEN` |
| 4006 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `ELSE IF (runof .GE. flowin + runoff + precip - flobot - etstr) THEN` |
| 4008 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `runof = - (flowin + runoff + precip - flobot - etstr)` |
| 4008 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `runof = - (flowin + runoff + precip - flobot - etstr)` |
| 4009 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `ELSE IF (etstr .GE. flowin + runoff + precip - flobot + runof) THEN` |
| 4009 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `ELSE IF (etstr .GE. flowin + runoff + precip - flobot + runof) THEN` |
| 4010 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `etstr = flowin + runoff + precip - flobot + runof` |
| 4012 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `ELSE IF (etstr .GT. flowin + runoff + runof + precip - flobot) THEN` |
| 4012 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `ELSE IF (etstr .GT. flowin + runoff + runof + precip - flobot) THEN` |
| 4013 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `etstr = flowin + runof + runoff + precip - flobot` |
| 4014 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `ELSE IF (flowin + runoff + runof + precip - flobot .LT. NEARZERO) THEN` |
| 4018 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `flow = flowin + runof + runoff + precip - etstr` |
| 4018 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `flow = flowin + runof + runoff + precip - etstr` |
| 4026 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 3941, 3946, 4162 | `IF (h .LT. sbot) flobot = CALCUNSATFLOBOT(depth, avhc, fks, wetperm, sbdthk, areamax, strlen, fbc...` |
| 4036 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `qlat = (runof + runoff + precip - etstr) / strlen` |
| 4036 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `qlat = (runof + runoff + precip - etstr) / strlen` |
| 4077 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `qlat = (runof + runoff + precip - etstr) / strlen` |
| 4077 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `qlat = (runof + runoff + precip - etstr) / strlen` |
| 4100 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 3941, 3946, 4162 | `IF (h .LT. sbot) THEN` |
| 4130 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 3941, 3946, 4162 | `STRM(19, l) = h` |
| 4147 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `sfrbudg_in = sfrbudg_in + precip` |
| 4149 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `sfrbudg_out = sfrbudg_out + etstr` |
| 4192 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 3941, 3946, 4162 | `IF (icalccheck .EQ. 1 .AND. sbot .GT. h) THEN` |
| 4200 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 3941, 3946, 4162 | `ELSE IF (sbot .LT. h) THEN` |
| 4211 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `WRITE(IOUT, 9005) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SNG...` |
| 4211 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `WRITE(IOUT, 9005) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SNG...` |
| 4222 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 3670, 3673, 3688, 4397, 4400 | `WRITE(iout2, 9004) txtlst, Kkper, Kkstp` |
| 4224 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `WRITE(iout2, 9005) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4224 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 3670, 3673, 3688, 4397, 4400 | `WRITE(iout2, 9005) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4224 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `WRITE(iout2, 9005) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4239 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `WRITE(IOUT, 9007) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SNG...` |
| 4239 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `WRITE(IOUT, 9007) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SNG...` |
| 4253 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 3670, 3673, 3688, 4397, 4400 | `WRITE(iout2, 9006) txtlst, Kkper, Kkstp` |
| 4255 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `WRITE(iout2, 9007) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4255 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 3670, 3673, 3688, 4397, 4400 | `WRITE(iout2, 9007) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4255 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `WRITE(iout2, 9007) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4264 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 3670, 3673, 3688, 4397, 4400 | `WRITE(iout2, 9009) txtlst, Kkper, Kkstp` |
| 4266 | gwf2sfr7bd | uninitialized | loop-guarded | etstr | defined at 3976, 3981, 3991, 3995, 3998, 4000, 4005, 4010, 4013, 4016 | `WRITE(iout2, 9010) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4266 | gwf2sfr7bd | uninitialized | loop-guarded | h | defined at 3941, 3946, 4162 | `WRITE(iout2, 9010) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4266 | gwf2sfr7bd | uninitialized | conditional | iout2 | defined at 3670, 3673, 3688, 4397, 4400 | `WRITE(iout2, 9010) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4266 | gwf2sfr7bd | uninitialized | loop-guarded | precip | defined at 3975, 3980 | `WRITE(iout2, 9010) il, ir, ic, ISTRM(4, l), ISTRM(5, l), STRM(10, l), STRM(11, l), STRM(9, l), SN...` |
| 4359 | gwf2sfr7bd | uninitialized | loop-guarded | icalccheck | defined at 3887, 3892 | `IF (IBUDFL .GT. 0 .AND. icalccheck .EQ. 1) CALL GWF2SFR7UZOT(Kkstp, Kkper)` |
| 4477 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | roughch | defined at 4453, 4485, 4488 | `flwdlk2 = (CONST / roughch) * widthch * (dlkstr2 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 4477 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | slope | defined at 4452, 4485, 4488 | `flwdlk2 = (CONST / roughch) * widthch * (dlkstr2 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 4477 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | widthch | defined at 4454 | `flwdlk2 = (CONST / roughch) * widthch * (dlkstr2 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 4480 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | roughch | defined at 4453, 4485, 4488 | `SLKOTFLW(lk, istsg) = (CONST / roughch) * widthch * (dlkstr1 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 4480 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | slope | defined at 4452, 4485, 4488 | `SLKOTFLW(lk, istsg) = (CONST / roughch) * widthch * (dlkstr1 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 4480 | gwf2sfr7lakoutflw | uninitialized | loop-guarded | widthch | defined at 4454 | `SLKOTFLW(lk, istsg) = (CONST / roughch) * widthch * (dlkstr1 ** FIVE_THIRDS) * (DSQRT(slope))` |
| 5017 | gwf2sfr7flw | uninitialized | loop-guarded | xleft | defined at 4979, 5001 | `wtprm = DSQRT(((xleft - xright) * (xleft - xright)) + ((yleft - yright) * (yleft - yright)))` |
| 5017 | gwf2sfr7flw | uninitialized | loop-guarded | xright | defined at 4985, 4993, 5002 | `wtprm = DSQRT(((xleft - xright) * (xleft - xright)) + ((yleft - yright) * (yleft - yright)))` |
| 5017 | gwf2sfr7flw | uninitialized | loop-guarded | yleft | defined at 4980, 5000 | `wtprm = DSQRT(((xleft - xright) * (xleft - xright)) + ((yleft - yright) * (yleft - yright)))` |
| 5017 | gwf2sfr7flw | uninitialized | loop-guarded | yright | defined at 4986, 4992, 5003 | `wtprm = DSQRT(((xleft - xright) * (xleft - xright)) + ((yleft - yright) * (yleft - yright)))` |
| 5689 | sgwf2sfr7parmov | uninitialized | loop-guarded | jend | defined at 5683, 5685, 5687, 5696, 5698, 5700 | `DO jj = 6, jend` |
| 5702 | sgwf2sfr7parmov | uninitialized | loop-guarded | jend | defined at 5683, 5685, 5687, 5696, 5698, 5700 | `DO jj = 11, jend` |
| 7375 | leadwave | uninitialized | loop-guarded | checktime | defined at 7321, 7336, 7339, 7351, 7360, 7363, 7367, 7370, 7375 | `IF (checktime(j) .LT. NEARZERO) checktime(j) = big` |
| 7389 | leadwave | uninitialized | loop-guarded | checktime | defined at 7321, 7336, 7339, 7351, 7360, 7363, 7367, 7370, 7375 | `IF (CHECKTIME(j) .LE. shortest) THEN` |
| 7391 | leadwave | uninitialized | loop-guarded | checktime | defined at 7321, 7336, 7339, 7351, 7360, 7363, 7367, 7370, 7375 | `shortest = CHECKTIME(j)` |
| 7400 | leadwave | uninitialized | loop-guarded | checktime | defined at 7321, 7336, 7339, 7351, 7360, 7363, 7367, 7370, 7375 | `IF (CHECKTIME(k) > shortest) MORE(k) = 0` |
| 7507 | leadwave | uninitialized | loop-guarded | more | defined at 7322, 7390, 7400 | `IF (more(j) .EQ. 1) THEN` |
| 7893 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `chap = (XSEC(8 + mark(ll) - 1, Istsg) - XSEC(8 + mark(ll), Istsg))` |
| 7894 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `IF (ABS(XSEC(8 + mark(ll), Istsg) - XSEC(8 + mark(ll) - 1, Istsg)) .LT. 1.0E-30 .AND. ABS(XSEC(ma...` |
| 7900 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `ELSE IF (ABS(XSEC(8 + mark(ll), Istsg) - XSEC(8 + mark(ll) - 1, Istsg)) .LT. 1.0E-30) THEN` |
| 7903 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `ELSE IF (ABS(XSEC(mark(ll), Istsg) - XSEC(mark(ll) - 1, Istsg)) .LT. 1.0E-30) THEN` |
| 7907 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `slope = (XSEC(8 + mark(ll), Istsg) - XSEC(8 + mark(ll) - 1, Istsg)) / (XSEC(mark(ll), Istsg) - XS...` |
| 7911 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `ffmin = XSEC(8 + mark(ll), Istsg)` |
| 7912 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `ffmax = XSEC(8 + mark(ll) - 1, Istsg)` |
| 7914 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `ffmin = XSEC(8 + mark(ll) - 1, Istsg)` |
| 7915 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `ffmax = XSEC(8 + mark(ll), Istsg)` |
| 7917 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `b = XSEC(8 + mark(ll) - 1, Istsg) - slope * XSEC(mark(ll) - 1, Istsg)` |
| 7921 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `area1 = (XSEC(mark(ll), Istsg) - XSEC(mark(ll) - 1, Istsg)) * (stage - ffmin)` |
| 7927 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `xinc = (XSEC(mark(ll), Istsg) - XSEC(mark(ll) - 1, Istsg)) / 50.` |
| 7928 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `xmid = XSEC(mark(ll) - 1, Istsg)` |
| 7934 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `IF (XSEC(8 + mark(ll) - 1, Istsg) .LT. XSEC(8 + mark(ll), Istsg)) THEN` |
| 7936 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `xinc = (ABS(XSEC(mark(ll) - 1, Istsg) - xmid)) / 50.` |
| 7937 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `xmid = XSEC(mark(ll) - 1, Istsg)` |
| 7939 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `xinc = (ABS(XSEC(mark(ll), Istsg) - xmid)) / 50.` |
| 7944 | channelarea | uninitialized | loop-guarded | mark | defined at 7886 | `xx = ABS(xmid - XSEC(mark(ll), Istsg))` |

### gwf2str7.f90 (28)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 400 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 359, 384, 388, 392, 396 | `XNUM = ((FLOWIN + STRM(9, L)) / 2.0) * STRM(8, L)` |
| 409 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 359, 384, 388, 392, 396 | `IF (FLOWIN .LE. 0.) HSTR = STRM(5, L)` |
| 425 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 359, 384, 388, 392, 396 | `IF (FLOBOT .LE. FLOWIN) GO TO 320` |
| 427 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 359, 384, 388, 392, 396 | `FLOBOT = FLOWIN` |
| 431 | gwf2str7fm | uninitialized | loop-guarded | flobot | defined at 416, 422, 427, 430 | `FLOWOT = FLOWIN - FLOBOT` |
| 431 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 359, 384, 388, 392, 396 | `FLOWOT = FLOWIN - FLOBOT` |
| 432 | gwf2str7fm | uninitialized | loop-guarded | iflg | defined at 363 | `STRM(9, LL) = ARTRIB(IFLG)` |
| 436 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 359, 384, 388, 392, 396 | `STRM(10, L) = FLOWIN` |
| 437 | gwf2str7fm | uninitialized | loop-guarded | flobot | defined at 416, 422, 427, 430 | `STRM(11, L) = FLOBOT` |
| 443 | gwf2str7fm | uninitialized | loop-guarded | flobot | defined at 416, 422, 427, 430 | `IF ((FLOWIN .LE. 0.0) .AND. (FLOBOT .GE. 0.0)) GO TO 500` |
| 443 | gwf2str7fm | uninitialized | loop-guarded | flowin | defined at 359, 384, 388, 392, 396 | `IF ((FLOWIN .LE. 0.0) .AND. (FLOBOT .GE. 0.0)) GO TO 500` |
| 446 | gwf2str7fm | uninitialized | loop-guarded | iqflg | defined at 419, 421, 426 | `IF (IQFLG .GT. 0) GO TO 400` |
| 447 | gwf2str7fm | uninitialized | loop-guarded | cstr | defined at 410 | `RHS(IC, IR, IL) = RHS(IC, IR, IL) - CSTR * HSTR` |
| 448 | gwf2str7fm | uninitialized | loop-guarded | cstr | defined at 410 | `HCOF(IC, IR, IL) = HCOF(IC, IR, IL) - CSTR` |
| 452 | gwf2str7fm | uninitialized | loop-guarded | flobot | defined at 416, 422, 427, 430 | `RHS(IC, IR, IL) = RHS(IC, IR, IL) - FLOBOT` |
| 568 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 527, 552, 556, 560, 564 | `XNUM = ((FLOWIN + STRM(9, L)) / 2.0) * STRM(8, L)` |
| 577 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 527, 552, 556, 560, 564 | `IF (FLOWIN .LE. 0.0) HSTR = STRM(5, L)` |
| 591 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 527, 552, 556, 560, 564 | `IF (FLOBOT .LE. FLOWIN) GO TO 320` |
| 592 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 527, 552, 556, 560, 564 | `FLOBOT = FLOWIN` |
| 596 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 584, 588, 592, 595, 619 | `FLOWOT = FLOWIN - FLOBOT` |
| 596 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 527, 552, 556, 560, 564 | `FLOWOT = FLOWIN - FLOBOT` |
| 597 | gwf2str7bd | uninitialized | loop-guarded | iflg | defined at 531 | `STRM(9, LL) = ARTRIB(IFLG)` |
| 601 | gwf2str7bd | uninitialized | loop-guarded | flowin | defined at 527, 552, 556, 560, 564 | `STRM(10, L) = FLOWIN` |
| 602 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 584, 588, 592, 595, 619 | `STRM(11, L) = FLOBOT` |
| 605 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 584, 588, 592, 595, 619 | `BUFF(IC, IR, IL) = BUFF(IC, IR, IL) + FLOBOT` |
| 608 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 584, 588, 592, 595, 619 | `IF (FLOBOT .LT. 0.) THEN` |
| 611 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 584, 588, 592, 595, 619 | `RATOUT = RATOUT - FLOBOT` |
| 615 | gwf2str7bd | uninitialized | loop-guarded | flobot | defined at 584, 588, 592, 595, 619 | `RATIN = RATIN + FLOBOT` |

### gwf2sub7.f90 (3)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 1154 | gwf2sub7ot | uninitialized | loop-guarded | nend | defined at 1147, 1166, 1311 | `CALL ULASAV(SUB(LOC2 : NEND), TEXT(3), KSTP, KPER, PERTIM, TOTIM, NCOL, NROW, KQ, ISBOCU(3))` |
| 1173 | gwf2sub7ot | uninitialized | loop-guarded | nend | defined at 1147, 1166, 1311 | `CALL ULASAV(DCOM(LOC2 : NEND), TEXT(4), KSTP, KPER, PERTIM, TOTIM, NCOL, NROW, KQ, ISBOCU(3))` |
| 1318 | gwf2sub7ot | uninitialized | loop-guarded | nend | defined at 1147, 1166, 1311 | `CALL ULASAV(HC(LOC2 : NEND), TEXT(6), KSTP, KPER, PERTIM, TOTIM, NCOL, NROW, K, ISBOCU(5))` |

### gwf2swi27.F90 (4)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 4138 | sswi2_imix | uninitialized | loop-guarded | izl | defined at 4127, 4133 | `IF (izu .GT. 0 .AND. izl .GT. 0) THEN` |
| 4138 | sswi2_imix | uninitialized | loop-guarded | izu | defined at 4121, 4136 | `IF (izu .GT. 0 .AND. izl .GT. 0) THEN` |
| 4139 | sswi2_imix | uninitialized | loop-guarded | izu | defined at 4121, 4136 | `A(j, i, k, izu) = A(j, i, k, izu) - qzbot * switfact` |
| 4140 | sswi2_imix | uninitialized | loop-guarded | izl | defined at 4127, 4133 | `A(j, i, k + 1, izl) = A(j, i, k + 1, izl) + qzbot * switfact` |

### gwf2swr7.f90 (83)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 2016 | gwf2swr7ar | aliasing | global-aliasing | ntmax | argument 1 of sswr_allo_soln, which also assigns that module variable directly | `CALL SSWR_ALLO_SOLN(NTMAX, 0)` |
| 2791 | gwf2swr7rp | uninitialized | loop-guarded | cbnd | defined at 2785, 2787, 2789 | `WRITE(IOUT, 2082) i, REACH(i) % ISWRBND, ADJUSTL(cbnd)` |
| 3006 | gwf2swr7rp | uninitialized | loop-guarded | getextd | defined at 2923, 2952 | `WRITE(creach(8), 2110) getextd` |
| 3358 | gwf2swr7rp | uninitialized | loop-guarded | rbot | defined at 3343, 3346 | `REACH(istrrch) % STRUCT(istrnum) % STRINV = rbot` |
| 3359 | gwf2swr7rp | uninitialized | loop-guarded | dlen | defined at 3344, 3347 | `REACH(istrrch) % STRUCT(istrnum) % STRWID = dlen` |
| 3643 | gwf2swr7rp | uninitialized | call-assumed | istrnum | defined at 3127, 3143, 4115 | `ival = REACH(istrrch) % STRUCT(istrnum) % ISTRTAB` |
| 3643 | gwf2swr7rp | uninitialized | call-assumed | istrrch | defined at 3122, 3143, 4113 | `ival = REACH(istrrch) % STRUCT(istrnum) % ISTRTAB` |
| 3668 | gwf2swr7rp | uninitialized | loop-guarded | cstruct | defined at 3536, 3568, 3570, 3572, 3574, 3576, 3585, 3587, 3604, 3606, 3608, 3619, 3621, 3623, 3634, 3636, 3638, 3647, 3649, 3651, 3672, 3695, 3698, 3700, 3708, 3710, 3718, 3757, 3761, 3817, 3819 | `WRITE(cstruct(1), 2110) REACH(i) % STRUCT(j) % STRELEV(istrpts)` |
| 3670 | gwf2swr7rp | uninitialized | loop-guarded | cstruct | defined at 3536, 3568, 3570, 3572, 3574, 3576, 3585, 3587, 3604, 3606, 3608, 3619, 3621, 3623, 3634, 3636, 3638, 3647, 3649, 3651, 3672, 3695, 3698, 3700, 3708, 3710, 3718, 3757, 3761, 3817, 3819 | `WRITE(cstruct(2), 2110) REACH(i) % STRUCT(j) % STRQ(istrpts)` |
| 3823 | gwf2swr7rp | uninitialized | loop-guarded | cstruct | defined at 3536, 3568, 3570, 3572, 3574, 3576, 3585, 3587, 3604, 3606, 3608, 3619, 3621, 3623, 3634, 3636, 3638, 3647, 3649, 3651, 3672, 3695, 3698, 3700, 3708, 3710, 3718, 3757, 3761, 3817, 3819 | `WRITE(IOUT, 4110) i, j, cstruct(1), indx` |
| 4715 | gwf2swr7fm | uninitialized | loop-guarded | dt | defined at 4709, 4711, 4715 | `dt = dt * TSMULT(Kkper)` |
| 5233 | gwf2swr7fm | uninitialized | loop-guarded | irch | defined at 4881 | `ge = REACH(irch) % CURRENT % QPOTGWET * dtscale` |
| 5236 | gwf2swr7fm | uninitialized | loop-guarded | irch | defined at 4881 | `getextd = REACH(irch) % GETEXTD` |
| 5252 | gwf2swr7fm | uninitialized | loop-guarded | h | defined at 5144, 5199, 5201, 5243 | `IF (h .GE. REACH(i) % GBELEV) THEN` |
| 5256 | gwf2swr7fm | uninitialized | loop-guarded | h | defined at 5144, 5199, 5201, 5243 | `ELSE IF (h .GE. (REACH(i) % GBELEV - getextd)) THEN` |
| 5852 | gwf2swr7bd | uninitialized | loop-guarded | h | defined at 5692, 5697, 5840 | `IF (h .GE. REACH(irch) % GBELEV) THEN` |
| 5856 | gwf2swr7bd | uninitialized | loop-guarded | h | defined at 5692, 5697, 5840 | `ELSE IF (h .GE. (REACH(irch) % GBELEV - getextd)) THEN` |
| 5860 | gwf2swr7bd | uninitialized | loop-guarded | h | defined at 5692, 5697, 5840 | `qq = h * hhcof + rrhs` |
| 6688 | sswr_sort | uninitialized | conditional | istack | defined at 6719, 6720, 6723, 6724 | `r = istack(jstack)` |
| 6689 | sswr_sort | uninitialized | conditional | istack | defined at 6719, 6720, 6723, 6724 | `l = istack(jstack - 1)` |
| 6693 | sswr_sort | aliasing | aliasing | v | passed as arguments 1, 2 of sswr_swap; the callee writes dummy a | `CALL SSWR_SWAP(V(k), V(l + 1))` |
| 6694 | sswr_sort | aliasing | aliasing | v | passed as arguments 1, 2 of sswr_mswap; the callee writes dummy a | `CALL SSWR_MSWAP(V(l), V(r), V(l) .GT. V(r))` |
| 6695 | sswr_sort | aliasing | aliasing | v | passed as arguments 1, 2 of sswr_mswap; the callee writes dummy a | `CALL SSWR_MSWAP(V(l + 1), V(r), V(l + 1) .GT. V(r))` |
| 6696 | sswr_sort | aliasing | aliasing | v | passed as arguments 1, 2 of sswr_mswap; the callee writes dummy a | `CALL SSWR_MSWAP(V(l), V(l + 1), V(l) .GT. V(l + 1))` |
| 6710 | sswr_sort | aliasing | aliasing | v | passed as arguments 1, 2 of sswr_swap; the callee writes dummy a | `CALL SSWR_SWAP(V(i), V(j))` |
| 7879 | sswr_set_rchoff | uninitialized | loop-guarded | s | defined at 7860, 7872 | `smin = MAXVAL(s) + DONE` |
| 7885 | sswr_set_rchoff | uninitialized | loop-guarded | s | defined at 7860, 7872 | `IF (s(irch) .LE. smin) THEN` |
| 7887 | sswr_set_rchoff | uninitialized | loop-guarded | s | defined at 7860, 7872 | `smin = s(irch)` |
| 7899 | sswr_set_rchoff | uninitialized | loop-guarded | s | defined at 7860, 7872 | `REACH(i) % OFFSET = s(i) - smin` |
| 8052 | sswr_calc_rchgeodata | uninitialized | conditional | bottom | defined at 8019, 8024, 8031, 8038 | `IF (zg .GT. bottom) THEN` |
| 8053 | sswr_calc_rchgeodata | uninitialized | conditional | bottom | defined at 8019, 8024, 8031, 8038 | `dz = (zg - bottom + 1.0D-6) / 10.0D0` |
| 8056 | sswr_calc_rchgeodata | uninitialized | conditional | bottom | defined at 8019, 8024, 8031, 8038 | `uz(1) = bottom` |
| 8057 | sswr_calc_rchgeodata | uninitialized | conditional | bottom | defined at 8019, 8024, 8031, 8038 | `uz(2) = bottom + 1.0D-6` |
| 8127 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8017, 8036 | `wp0 = MAX(REACH(irch) % GEO % WETPER(ipos - 1), width)` |
| 8128 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8017, 8036 | `tw0 = MAX(REACH(irch) % GEO % TOPWID(ipos - 1), width)` |
| 8129 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8017, 8036 | `sa0 = MAX(REACH(irch) % GEO % SAREA(ipos - 1), width * length)` |
| 8240 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8017, 8036 | `REACH(irch) % GEO % WETPER = width` |
| 8241 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8017, 8036 | `REACH(irch) % GEO % TOPWID = width` |
| 8244 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8017, 8036 | `REACH(irch) % GEO % SAREA = width * length` |
| 8246 | sswr_calc_rchgeodata | uninitialized | conditional | bottom | defined at 8019, 8024, 8031, 8038 | `z1 = uz(ipos) - bottom` |
| 8247 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8017, 8036 | `REACH(irch) % GEO % XAREA(ipos) = width * z1` |
| 8248 | sswr_calc_rchgeodata | uninitialized | conditional | width | defined at 8017, 8036 | `REACH(irch) % GEO % VOL(ipos) = length * width * z1` |
| 8329 | sswr_set_rchlay | uninitialized | loop-guarded | kbot | defined at 8325 | `REACH(irch) % LAYEND = kbot` |
| 8788 | sswr_gsolwrp | uninitialized | loop-guarded | ptcfn0 | defined at 8764, 8792 | `PTCDEL = PTCDEL * ptcfn0 / fn` |
| 8898 | sswr_gsolwrp | uninitialized | call-assumed | icnvg | defined at 8845, 8851, 8859, 8875 | `IF (icnvg .LT. 0) EXIT OUTER` |
| 8962 | sswr_gsolwrp | uninitialized | loop-guarded | diagmin | defined at 8754, 8759 | `ratio = (DONE / ptcdel) / diagmin` |
| 10106 | sswr_p_qaqflow | uninitialized | conditional | mxactr | defined at 10093, 10096, 10098 | `WRITE(iriv, 2020) mxactr, 0` |
| 10186 | sswr_p_qaqflow | uninitialized | conditional | itmp | defined at 10111, 10115 | `WRITE(iriv, 2030) itmp, 0, Kper, Kstp, n, swrtot` |
| 11550 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11521, 11523, 11526, 11528, 11530, 11540, 11550 | `cond = cond * fact` |
| 11564 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11521, 11523, 11526, 11528, 11530, 11540, 11550 | `value = value - cond * hd` |
| 11570 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11521, 11523, 11526, 11528, 11530, 11540, 11550 | `Rch % CURRENTQAQ(k) % QAQFLOW = cond * hd` |
| 11571 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11521, 11523, 11526, 11528, 11530, 11540, 11550 | `Rch % CURRENTQAQ(k) % CONDUCTANCE = cond` |
| 11574 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11521, 11523, 11526, 11528, 11530, 11540, 11550 | `Rch % CURRENT % QAQFLOW = Rch % CURRENT % QAQFLOW - cond * hd` |
| 11579 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11521, 11523, 11526, 11528, 11530, 11540, 11550 | `rh = cond * hd` |
| 11582 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11521, 11523, 11526, 11528, 11530, 11540, 11550 | `rh = cond * trs` |
| 11583 | sswr_calc_qaq | uninitialized | loop-guarded | cond | defined at 11521, 11523, 11526, 11528, 11530, 11540, 11550 | `hc = cond` |
| 11733 | sswr_calc_mfqaq | uninitialized | loop-guarded | cond | defined at 11708, 11710, 11712, 11714, 11723, 11733 | `cond = cond * fact` |
| 11747 | sswr_calc_mfqaq | uninitialized | loop-guarded | cond | defined at 11708, 11710, 11712, 11714, 11723, 11733 | `value = value - cond * hd` |
| 11753 | sswr_calc_mfqaq | uninitialized | loop-guarded | cond | defined at 11708, 11710, 11712, 11714, 11723, 11733 | `Rch % CURRENTQAQ(k) % QAQFLOW = cond * hd` |
| 11754 | sswr_calc_mfqaq | uninitialized | loop-guarded | cond | defined at 11708, 11710, 11712, 11714, 11723, 11733 | `Rch % CURRENTQAQ(k) % CONDUCTANCE = cond` |
| 11812 | sswr_calc_sflow | uninitialized | loop-guarded | iseg | defined at 11805 | `SEG(2, iseg) = qsfr` |
| 12504 | swr_calc_strvals | uninitialized | loop-guarded | cval | defined at 12434, 12437, 12439, 12450, 12453, 12456, 12457 | `cl1 = cval` |
| 12506 | swr_calc_strvals | uninitialized | loop-guarded | cval | defined at 12434, 12437, 12439, 12450, 12453, 12456, 12457 | `cl2 = cval` |
| 12510 | swr_calc_strvals | uninitialized | loop-guarded | cval | defined at 12434, 12437, 12439, 12450, 12453, 12456, 12457 | `cr1 = cval` |
| 12512 | swr_calc_strvals | uninitialized | loop-guarded | cval | defined at 12434, 12437, 12439, 12450, 12453, 12456, 12457 | `cr2 = cval` |
| 12519 | swr_calc_strvals | uninitialized | loop-guarded | cl1 | defined at 12504, 12509 | `IF (cl1 .LT. cr1) THEN` |
| 12519 | swr_calc_strvals | uninitialized | loop-guarded | cr1 | defined at 12505, 12510 | `IF (cl1 .LT. cr1) THEN` |
| 12522 | swr_calc_strvals | uninitialized | loop-guarded | cl2 | defined at 12506, 12511 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12522 | swr_calc_strvals | uninitialized | loop-guarded | cr2 | defined at 12507, 12512 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12531 | swr_calc_strvals | uninitialized | loop-guarded | cl1 | defined at 12504, 12509 | `IF (cl1 .LT. cr1) THEN` |
| 12531 | swr_calc_strvals | uninitialized | loop-guarded | cr1 | defined at 12505, 12510 | `IF (cl1 .LT. cr1) THEN` |
| 12534 | swr_calc_strvals | uninitialized | loop-guarded | cl2 | defined at 12506, 12511 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12534 | swr_calc_strvals | uninitialized | loop-guarded | cr2 | defined at 12507, 12512 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12542 | swr_calc_strvals | uninitialized | loop-guarded | cl1 | defined at 12504, 12509 | `IF (cl1 .LT. cr1) THEN` |
| 12542 | swr_calc_strvals | uninitialized | loop-guarded | cr1 | defined at 12505, 12510 | `IF (cl1 .LT. cr1) THEN` |
| 12547 | swr_calc_strvals | uninitialized | loop-guarded | cl2 | defined at 12506, 12511 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12547 | swr_calc_strvals | uninitialized | loop-guarded | cr2 | defined at 12507, 12512 | `ELSE IF (cl2 .GE. cr2) THEN` |
| 12562 | swr_calc_strvals | uninitialized | loop-guarded | gt | defined at 12479, 12483, 12487, 12491, 12514, 12521, 12524, 12529, 12545, 12550 | `REACH(irch) % STRUCT(nn) % STRTOP = gt` |
| 12563 | swr_calc_strvals | uninitialized | loop-guarded | gb | defined at 12480, 12484, 12488, 12492, 12515, 12526, 12533, 12536, 12540 | `REACH(irch) % STRUCT(nn) % STRBOT = gb` |
| 13515 | sswrbtbm | uninitialized | loop-guarded | pd | defined at 13520, 13522, 13524, 13529 | `pe = pd` |
| 14316 | sswr_sflow | uninitialized | conditional | q | defined at 14194, 14230, 14236, 14239, 14242, 14246, 14249, 14250, 14272, 14276, 14277, 14281, 14285, 14286, 14289, 14293, 14294, 14297, 14301, 14302, 14305, 14309, 14310, 14313 | `value = q` |
| 14849 | sswr_pcnvg | uninitialized | loop-guarded | mfdiff | defined at 14843, 14844, 14847 | `IF (mfdiff .GT. bfdiffmax) THEN` |
| 14851 | sswr_pcnvg | uninitialized | loop-guarded | mfdiff | defined at 14843, 14844, 14847 | `bfdiffmax = mfdiff` |

### gwf2swr7util.f90 (21)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 98 | gsol_full_ludcap | uninitialized | loop-guarded | npiv | defined at 93 | `IF (n .NE. npiv) THEN` |
| 100 | gsol_full_ludcap | uninitialized | loop-guarded | npiv | defined at 93 | `t = AU(npiv, i)` |
| 101 | gsol_full_ludcap | uninitialized | loop-guarded | npiv | defined at 93 | `AU(npiv, i) = AU(n, i)` |
| 104 | gsol_full_ludcap | uninitialized | loop-guarded | npiv | defined at 93 | `S(npiv) = S(n)` |
| 106 | gsol_full_ludcap | uninitialized | loop-guarded | npiv | defined at 93 | `PINDEX(n) = npiv` |
| 428 | gsol_cgap | uninitialized | loop-guarded | rho0 | defined at 462 | `beta = rho / rho0` |
| 429 | gsol_cgap | aliasing | aliasing | p | passed as arguments 5, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, Z, beta, P, P)` |
| 442 | gsol_cgap | aliasing | aliasing | t | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, T, alpha, P, T)` |
| 443 | gsol_cgap | aliasing | aliasing | x | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, X, DONE, T, X)` |
| 454 | gsol_cgap | aliasing | aliasing | d | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, D, - alpha, Q, D)` |
| 586 | gsol_bcgsap | uninitialized | loop-guarded | alpha0 | defined at 665 | `beta = (rho / rho0) * (alpha0 / omega0)` |
| 586 | gsol_bcgsap | uninitialized | loop-guarded | omega0 | defined at 666 | `beta = (rho / rho0) * (alpha0 / omega0)` |
| 586 | gsol_bcgsap | uninitialized | loop-guarded | rho0 | defined at 664 | `beta = (rho / rho0) * (alpha0 / omega0)` |
| 590 | gsol_bcgsap | uninitialized | loop-guarded | omega | defined at 632, 635 | `CALL GSOL_AXPY(NCORESV, NR, P, - omega, V, P)` |
| 590 | gsol_bcgsap | aliasing | aliasing | p | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, P, - omega, V, P)` |
| 591 | gsol_bcgsap | aliasing | aliasing | p | passed as arguments 5, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, D, beta, P, P)` |
| 616 | gsol_bcgsap | aliasing | aliasing | x | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, X, alpha, PHAT, X)` |
| 635 | gsol_bcgsap | aliasing | aliasing | d | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, D, omega, SHAT, D)` |
| 636 | gsol_bcgsap | aliasing | aliasing | d | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, D, alpha, PHAT, D)` |
| 637 | gsol_bcgsap | aliasing | aliasing | x | passed as arguments 3, 6 of gsol_axpy; the callee writes dummy r | `CALL GSOL_AXPY(NCORESV, NR, X, DONE, D, X)` |
| 3322 | i4vec_reverse | aliasing | aliasing | a | passed as arguments 1, 2 of i4_swap; the callee writes dummy i | `CALL i4_swap(a(i), a(n + 1 - i))` |

### gwf2uzf1.f90 (140)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 855 | gwf2uzf1ar | uninitialized | loop-guarded | iuzlay | defined at 847 | `WRITE(igunit, 9024) igage, iuzrow, iuzcol, iuzlay` |
| 859 | gwf2uzf1ar | uninitialized | loop-guarded | iuzlay | defined at 847 | `WRITE(igunit, 9025) igage, iuzrow, iuzcol, iuzlay` |
| 863 | gwf2uzf1ar | uninitialized | loop-guarded | iuzlay | defined at 847 | `WRITE(igunit, 9026) igage, iuzrow, iuzcol, iuzlay` |
| 1116 | parseuzfoptions | uninitialized | conditional | iostat | defined at 983 | `IF (Iostat .NE. 0) THEN` |
| 1953 | gwf2uzf1fm | uninitialized | loop-guarded | thr | defined at 1928, 1999 | `UZTHST(iwav, l) = thr` |
| 2548 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `UZTHST(1, l) = thr` |
| 2624 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `UZTHST(iset, l) = thr` |
| 2632 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `UZTHST(ii, l) = thr` |
| 2677 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `UZSTOR(ic, ir) = UZDPST(1, l) * (UZTHST(1, l) - thr) * cellarea` |
| 2769 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = (UZTHST(jm1, l) - thr) / (ths - thr)` |
| 2769 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = (UZTHST(jm1, l) - thr) / (ths - thr)` |
| 2774 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 2774 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 2774 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 2777 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `UZSPST(jm1, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2777 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `UZSPST(jm1, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2777 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `UZSPST(jm1, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2780 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(j - 2, l) - thr) / (ths - thr)) ** epsilon` |
| 2780 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(j - 2, l) - thr) / (ths - thr)) ** epsilon` |
| 2780 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(j - 2, l) - thr) / (ths - thr)) ** epsilon` |
| 2784 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 2784 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 2784 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(jm1, l) - thr) / (ths - thr)) ** epsilon` |
| 2798 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = (UZTHST(k, l) - thr) / (ths - thr)` |
| 2798 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = (UZTHST(k, l) - thr) / (ths - thr)` |
| 2802 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2802 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2802 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2806 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2806 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2806 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2810 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 2810 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 2810 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 2815 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2815 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2815 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2834 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = (UZTHST(k, l) - thr) / (ths - thr)` |
| 2834 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = (UZTHST(k, l) - thr) / (ths - thr)` |
| 2838 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2838 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2838 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2841 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2841 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2841 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2844 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 2844 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 2844 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 2848 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2848 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2848 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2866 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2866 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2866 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2869 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2869 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2869 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `UZSPST(k, l) = (epsilon * fks / (ths - thr)) * (fhold ** eps_m1)` |
| 2872 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 2872 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 2872 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(k - 1, l) - thr) / (ths - thr)) ** epsilon` |
| 2876 | gwf2uzf1bd | uninitialized | loop-guarded | epsilon | defined at 2487, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2876 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2876 | gwf2uzf1bd | uninitialized | loop-guarded | ths | defined at 2488, 2607, 2702, 3054 | `fhold = ((UZTHST(k, l) - thr) / (ths - thr)) ** epsilon` |
| 2895 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 2900 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * UZDPST(k, l)` |
| 2904 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 2907 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 2912 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(j, l) - thr) * (UZDPST(j, l) - UZDPST(j + 1, l))` |
| 2917 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(iset + NWAVST(ic, ir) - 1, l) - thr) * UZDPST(iset + NWAVST(ic, ir) - 1, l)` |
| 2932 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 2937 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * UZDPST(k, l)` |
| 2941 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 2944 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 2949 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(j, l) - thr) * (UZDPST(j, l) - UZDPST(j + 1, l))` |
| 2954 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(iset + NWAVST(ic, ir) - 1, l) - thr) * UZDPST(iset + NWAVST(ic, ir) - 1, l)` |
| 2974 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 2979 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * UZDPST(k, l)` |
| 2983 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 2986 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 2991 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(j, l) - thr) * (UZDPST(j, l) - UZDPST(j + 1, l))` |
| 2996 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(iset + NWAVST(ic, ir) - 1, l) - thr) * UZDPST(iset + NWAVST(ic, ir) - 1, l)` |
| 3043 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `UZTHST(1, l) = thr` |
| 3071 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `IF (UZTHST(iset, l) .GT. thr .OR. NWAVST(ic, ir) .GT. 1) ick = 1` |
| 3082 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3087 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * UZDPST(k, l)` |
| 3091 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3094 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(k, l) - thr) * (UZDPST(k, l) - UZDPST(k + 1, l))` |
| 3099 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(j, l) - thr) * (UZDPST(j, l) - UZDPST(j + 1, l))` |
| 3104 | gwf2uzf1bd | uninitialized | loop-guarded | thr | defined at 2486, 2607, 2702, 3054, 3233, 3816 | `fm = fm + (UZTHST(iset + NWAVST(ic, ir) - 1, l) - thr) * UZDPST(iset + NWAVST(ic, ir) - 1, l)` |
| 3791 | gwf2uzf1bd | uninitialized | loop-guarded | gcumapl | defined at 3767 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 3791 | gwf2uzf1bd | uninitialized | loop-guarded | gcumin | defined at 3768 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 3791 | gwf2uzf1bd | uninitialized | loop-guarded | gcumrch | defined at 3769 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 3791 | gwf2uzf1bd | uninitialized | loop-guarded | gdelstor | defined at 3770 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 3791 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 3766 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 3791 | gwf2uzf1bd | uninitialized | loop-guarded | ghnw | defined at 3764 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 3791 | gwf2uzf1bd | uninitialized | loop-guarded | gseep | defined at 3779 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 3791 | gwf2uzf1bd | uninitialized | loop-guarded | guzstore | defined at 3776 | `WRITE(iftunit, 9011) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | gaplinfltr | defined at 3773 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | gcumapl | defined at 3767 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | gcumin | defined at 3768 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | gcumrch | defined at 3769 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | gdelstor | defined at 3770 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | gdlstr | defined at 3778 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 3766 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | ghnw | defined at 3764 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | ginfltr | defined at 3771 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | grchr | defined at 3777 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | gseep | defined at 3779 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | gseepr | defined at 3780 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3796 | gwf2uzf1bd | uninitialized | loop-guarded | guzstore | defined at 3776 | `WRITE(iftunit, 9012) il, TOTIM, ghnw, ghdif, gcumapl, gcumin, gcumrch, guzstore, gdelstor, gseep,...` |
| 3814 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 3766 | `IF (nuzr .EQ. iuzrow .AND. nuzc .EQ. iuzcol .AND. ghdif .GT. 0.0) THEN` |
| 3817 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 3766 | `depthinc = ghdif / 40.001D0` |
| 3822 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 3766 | `DO WHILE (depthsave - ghdif .LT. CLOSEZERO)` |
| 3847 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 3766 | `IF (avdpt .GE. ghdif - depthinc) THEN` |
| 3849 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 3766 | `avdpt = ghdif` |
| 3856 | gwf2uzf1bd | uninitialized | loop-guarded | ghdif | defined at 3766 | `WRITE(iftunit, 9013) il, TOTIM, ghnw, ghdif, avdpt, avwat` |
| 3856 | gwf2uzf1bd | uninitialized | loop-guarded | ghnw | defined at 3764 | `WRITE(iftunit, 9013) il, TOTIM, ghnw, ghdif, avdpt, avwat` |
| 4803 | transpiration | uninitialized | loop-guarded | fm | defined at 5156, 5159, 5161, 5167, 5226, 5235, 5238, 5241, 5244 | `FACTOR = FACTOR / (FM / PET)` |
| 4945 | transpiration | uninitialized | loop-guarded | diff | defined at 4924 | `IF (ABS(diff) .GT. feps) THEN` |
| 5170 | transpiration | uninitialized | loop-guarded | depth2 | defined at 4781 | `Depth(ii) = depth2(ii)` |
| 5171 | transpiration | uninitialized | loop-guarded | theta2 | defined at 4782 | `Theta(ii) = theta2(ii)` |
| 5172 | transpiration | uninitialized | loop-guarded | flux2 | defined at 4783 | `Flux(ii) = flux2(ii)` |
| 5173 | transpiration | uninitialized | loop-guarded | speed2 | defined at 4784 | `Speed(ii) = speed2(ii)` |
| 5174 | transpiration | uninitialized | loop-guarded | ltrail2 | defined at 4785 | `Ltrail(ii) = ltrail2(ii)` |
| 5175 | transpiration | uninitialized | loop-guarded | itrwave2 | defined at 4786 | `Itrwave(ii) = itrwave2(ii)` |
| 5182 | transpiration | uninitialized | loop-guarded | depth2 | defined at 4781 | `Depth(ii) = depth2(ii)` |
| 5183 | transpiration | uninitialized | loop-guarded | theta2 | defined at 4782 | `Theta(ii) = theta2(ii)` |
| 5184 | transpiration | uninitialized | loop-guarded | flux2 | defined at 4783 | `Flux(ii) = flux2(ii)` |
| 5185 | transpiration | uninitialized | loop-guarded | speed2 | defined at 4784 | `Speed(ii) = speed2(ii)` |
| 5186 | transpiration | uninitialized | loop-guarded | ltrail2 | defined at 4785 | `Ltrail(ii) = ltrail2(ii)` |
| 5187 | transpiration | uninitialized | loop-guarded | itrwave2 | defined at 4786 | `Itrwave(ii) = itrwave2(ii)` |
| 5231 | transpiration | uninitialized | loop-guarded | depth2 | defined at 4781 | `IF (Depth2(jk) - depthsave .LT. 0.0D0) jj = jk` |
| 5235 | transpiration | uninitialized | loop-guarded | depth2 | defined at 4781 | `fm = fm + (Theta2(jj - 1) - Thetar) * (depthsave - Depth2(jj))` |
| 5235 | transpiration | uninitialized | loop-guarded | theta2 | defined at 4782 | `fm = fm + (Theta2(jj - 1) - Thetar) * (depthsave - Depth2(jj))` |
| 5238 | transpiration | uninitialized | loop-guarded | depth2 | defined at 4781 | `fm = fm + (Theta2(j) - Thetar) * (Depth2(j) - Depth2(j + 1))` |
| 5238 | transpiration | uninitialized | loop-guarded | theta2 | defined at 4782 | `fm = fm + (Theta2(j) - Thetar) * (Depth2(j) - Depth2(j + 1))` |
| 5241 | transpiration | uninitialized | loop-guarded | depth2 | defined at 4781 | `fm = fm + (Theta2(Nwv) - Thetar) * Depth2(Nwv)` |
| 5241 | transpiration | uninitialized | loop-guarded | theta2 | defined at 4782 | `fm = fm + (Theta2(Nwv) - Thetar) * Depth2(Nwv)` |
| 5244 | transpiration | uninitialized | loop-guarded | theta2 | defined at 4782 | `fm = fm + (Theta2(Nwv) - Thetar) * depthsave` |
| 5423 | caph | uninitialized | result-unset | caph | some RETURN path never assigns the function result | `` |

### hydprograms/hydfmt.f90 (71)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 293 | hydfmt | uninitialized | conditional | ist | defined at 126 | `IDATE = IDATE + IST` |
| 295 | hydfmt | uninitialized | conditional | nc | defined at 251, 256 | `DO 89 ii = 1, NC` |
| 296 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `IF (id(ii) .GT. 0) icnt(id(ii)) = icnt(id(ii)) + 1` |
| 297 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `IF (id(ii) .EQ. 1) THEN` |
| 298 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `zh(icnt(id(ii))) = Z(JCOL(ii))` |
| 298 | hydfmt | uninitialized | conditional | jcol | defined at 253, 261 | `zh(icnt(id(ii))) = Z(JCOL(ii))` |
| 298 | hydfmt | uninitialized | conditional | z | defined at 280, 286 | `zh(icnt(id(ii))) = Z(JCOL(ii))` |
| 299 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `ELSE IF (id(ii) .EQ. 2) THEN` |
| 300 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `zhd(icnt(id(ii))) = Z(JCOL(ii))` |
| 300 | hydfmt | uninitialized | conditional | jcol | defined at 253, 261 | `zhd(icnt(id(ii))) = Z(JCOL(ii))` |
| 300 | hydfmt | uninitialized | conditional | z | defined at 280, 286 | `zhd(icnt(id(ii))) = Z(JCOL(ii))` |
| 301 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `ELSE IF (id(ii) .EQ. 3) THEN` |
| 302 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `zhph(icnt(id(ii))) = Z(JCOL(ii))` |
| 302 | hydfmt | uninitialized | conditional | jcol | defined at 253, 261 | `zhph(icnt(id(ii))) = Z(JCOL(ii))` |
| 302 | hydfmt | uninitialized | conditional | z | defined at 280, 286 | `zhph(icnt(id(ii))) = Z(JCOL(ii))` |
| 303 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `ELSE IF (id(ii) .EQ. 4) THEN` |
| 304 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `zhc(icnt(id(ii))) = Z(JCOL(ii))` |
| 304 | hydfmt | uninitialized | conditional | jcol | defined at 253, 261 | `zhc(icnt(id(ii))) = Z(JCOL(ii))` |
| 304 | hydfmt | uninitialized | conditional | z | defined at 280, 286 | `zhc(icnt(id(ii))) = Z(JCOL(ii))` |
| 305 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `ELSE IF (id(ii) .EQ. 5) THEN` |
| 306 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `zhs(icnt(id(ii))) = Z(JCOL(ii))` |
| 306 | hydfmt | uninitialized | conditional | jcol | defined at 253, 261 | `zhs(icnt(id(ii))) = Z(JCOL(ii))` |
| 306 | hydfmt | uninitialized | conditional | z | defined at 280, 286 | `zhs(icnt(id(ii))) = Z(JCOL(ii))` |
| 307 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `ELSE IF (id(ii) .EQ. 6) THEN` |
| 308 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `zhf(icnt(id(ii))) = Z(JCOL(ii))` |
| 308 | hydfmt | uninitialized | conditional | jcol | defined at 253, 261 | `zhf(icnt(id(ii))) = Z(JCOL(ii))` |
| 308 | hydfmt | uninitialized | conditional | z | defined at 280, 286 | `zhf(icnt(id(ii))) = Z(JCOL(ii))` |
| 309 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `ELSE IF (id(ii) .EQ. 7) THEN` |
| 310 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `zfi(icnt(id(ii))) = Z(JCOL(ii))` |
| 310 | hydfmt | uninitialized | conditional | jcol | defined at 253, 261 | `zfi(icnt(id(ii))) = Z(JCOL(ii))` |
| 310 | hydfmt | uninitialized | conditional | z | defined at 280, 286 | `zfi(icnt(id(ii))) = Z(JCOL(ii))` |
| 311 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `ELSE IF (id(ii) .EQ. 8) THEN` |
| 312 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `zfo(icnt(id(ii))) = Z(JCOL(ii))` |
| 312 | hydfmt | uninitialized | conditional | jcol | defined at 253, 261 | `zfo(icnt(id(ii))) = Z(JCOL(ii))` |
| 312 | hydfmt | uninitialized | conditional | z | defined at 280, 286 | `zfo(icnt(id(ii))) = Z(JCOL(ii))` |
| 313 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `ELSE IF (id(ii) .EQ. 9) THEN` |
| 314 | hydfmt | uninitialized | loop-guarded | id | defined at 151, 155, 159, 163, 167, 171, 175, 179, 183 | `zfa(icnt(id(ii))) = Z(JCOL(ii))` |
| 314 | hydfmt | uninitialized | conditional | jcol | defined at 253, 261 | `zfa(icnt(id(ii))) = Z(JCOL(ii))` |
| 314 | hydfmt | uninitialized | conditional | z | defined at 280, 286 | `zfa(icnt(id(ii))) = Z(JCOL(ii))` |
| 327 | hydfmt | uninitialized | loop-guarded | zh | defined at 298 | `WRITE(nu(1), *) WELLIDH(N), ',', IDATE, ',', ZH(N)` |
| 331 | hydfmt | uninitialized | loop-guarded | zhd | defined at 300 | `WRITE(nu(2), *) WELLIDD(N), ',', IDATE, ',', ZHD(N)` |
| 335 | hydfmt | uninitialized | loop-guarded | zhph | defined at 302 | `WRITE(nu(3), *) WELLIDCH(N), ',', IDATE, ',', ZHPH(N)` |
| 339 | hydfmt | uninitialized | loop-guarded | zhc | defined at 304 | `WRITE(nu(4), *) WELLIDC(N), ',', IDATE, ',', ZHC(N)` |
| 343 | hydfmt | uninitialized | loop-guarded | zhs | defined at 306 | `WRITE(nu(4), *) WELLIDS(N), ',', IDATE, ',', ZHS(N)` |
| 347 | hydfmt | uninitialized | loop-guarded | zhf | defined at 308 | `WRITE(nu(6), *) WELLIDHF(N), ',', IDATE, ',', ZHF(N)` |
| 351 | hydfmt | uninitialized | loop-guarded | zfi | defined at 310 | `WRITE(nu(7), *) WELLIDFI(N), ',', IDATE, ',', ZFI(N)` |
| 355 | hydfmt | uninitialized | loop-guarded | zfo | defined at 312 | `WRITE(nu(8), *) WELLIDFO(N), ',', IDATE, ',', ZFO(N)` |
| 359 | hydfmt | uninitialized | loop-guarded | zfa | defined at 314 | `WRITE(nu(9), *) WELLIDFA(N), ',', IDATE, ',', ZFA(N)` |
| 363 | hydfmt | uninitialized | loop-guarded | zh | defined at 298 | `WRITE(nu(1), FMT1) IDATE, (ZH(N), N = 1, numhh)` |
| 364 | hydfmt | uninitialized | loop-guarded | zhd | defined at 300 | `WRITE(nu(2), FMT1) IDATE, (ZHD(N), N = 1, numhd)` |
| 365 | hydfmt | uninitialized | loop-guarded | zhph | defined at 302 | `WRITE(nu(3), FMT1) IDATE, (ZHPH(N), N = 1, numch)` |
| 366 | hydfmt | uninitialized | loop-guarded | zhc | defined at 304 | `WRITE(nu(4), FMT1) IDATE, (ZHC(N), N = 1, numhc)` |
| 367 | hydfmt | uninitialized | loop-guarded | zhs | defined at 306 | `WRITE(nu(5), FMT1) IDATE, (ZHS(N), N = 1, numhs)` |
| 368 | hydfmt | uninitialized | loop-guarded | zhf | defined at 308 | `WRITE(nu(6), FMT1) IDATE, (ZHF(N), N = 1, numhhf)` |
| 369 | hydfmt | uninitialized | loop-guarded | zfi | defined at 310 | `WRITE(nu(7), FMT1) IDATE, (ZFI(N), N = 1, numhfi)` |
| 370 | hydfmt | uninitialized | loop-guarded | zfo | defined at 312 | `WRITE(nu(8), FMT1) IDATE, (ZFO(N), N = 1, numhfo)` |
| 371 | hydfmt | uninitialized | loop-guarded | zfa | defined at 314 | `WRITE(nu(9), FMT1) IDATE, (ZFA(N), N = 1, numhfa)` |
| 374 | hydfmt | uninitialized | loop-guarded | zh | defined at 298 | `WRITE(nu(1), FMT1) TIME, (ZH(N), N = 1, numhh)` |
| 375 | hydfmt | uninitialized | loop-guarded | zhd | defined at 300 | `WRITE(nu(2), FMT1) TIME, (ZHD(N), N = 1, numhd)` |
| 376 | hydfmt | uninitialized | loop-guarded | zhph | defined at 302 | `WRITE(nu(3), FMT1) TIME, (ZHPH(N), N = 1, numch)` |
| 377 | hydfmt | uninitialized | loop-guarded | zhc | defined at 304 | `WRITE(nu(4), FMT1) TIME, (ZHC(N), N = 1, numhc)` |
| 378 | hydfmt | uninitialized | loop-guarded | zhs | defined at 306 | `WRITE(nu(5), FMT1) TIME, (ZHS(N), N = 1, numhs)` |
| 379 | hydfmt | uninitialized | loop-guarded | zhf | defined at 308 | `WRITE(nu(6), FMT1) TIME, (ZHF(N), N = 1, numhhf)` |
| 380 | hydfmt | uninitialized | loop-guarded | zfi | defined at 310 | `WRITE(nu(7), FMT1) TIME, (ZFI(N), N = 1, numhfi)` |
| 381 | hydfmt | uninitialized | loop-guarded | zfo | defined at 312 | `WRITE(nu(8), FMT1) TIME, (ZFO(N), N = 1, numhfo)` |
| 382 | hydfmt | uninitialized | loop-guarded | zfa | defined at 314 | `WRITE(nu(9), FMT1) TIME, (ZFA(N), N = 1, numhfa)` |
| 448 | modtime | uninitialized | conditional | deltim | defined at 438, 440, 442, 444, 446, 475, 477, 479, 481, 483, 487, 489, 491, 493, 495, 499, 501, 503, 505, 507 | `ITIME = TOTIM / DELTIM` |
| 449 | modtime | uninitialized | conditional | deltim | defined at 438, 440, 442, 444, 446, 475, 477, 479, 481, 483, 487, 489, 491, 493, 495, 499, 501, 503, 505, 507 | `REMTIM = (TOTIM / DELTIM) - INT(TOTIM / DELTIM) + REMTIM` |
| 449 | modtime | uninitialized | conditional | remtim | defined at 420, 449, 451 | `REMTIM = (TOTIM / DELTIM) - INT(TOTIM / DELTIM) + REMTIM` |
| 509 | modtime | uninitialized | conditional | deltim | defined at 438, 440, 442, 444, 446, 475, 477, 479, 481, 483, 487, 489, 491, 493, 495, 499, 501, 503, 505, 507 | `TOTIM = (TOTIM / DELTIM) + START` |
| 516 | modtime | uninitialized | conditional | deltim | defined at 438, 440, 442, 444, 446, 475, 477, 479, 481, 483, 487, 489, 491, 493, 495, 499, 501, 503, 505, 507 | `TOTIM = TOTIM / DELTIM` |

### lmt8.f90 (42)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 169 | lmt8bas7ar | uninitialized | loop-guarded | mtmnw1 | defined at 139 | `IF (MTMNW1 .NE. 0) MTMNW = MTMNW1` |
| 170 | lmt8bas7ar | uninitialized | loop-guarded | mtmnw2 | defined at 143 | `IF (MTMNW2 .NE. 0) MTMNW = MTMNW2` |
| 1776 | lmt8huf7 | uninitialized | call-assumed | dfl | defined at 1548, 1592, 1763 | `X1 = - DFL` |
| 1786 | lmt8huf7 | uninitialized | call-assumed | dfr | defined at 1548, 1592, 1763 | `X2 = DFR` |
| 1796 | lmt8huf7 | uninitialized | call-assumed | dft | defined at 1548, 1592, 1763 | `X3 = - DFT` |
| 1806 | lmt8huf7 | uninitialized | call-assumed | dfb | defined at 1548, 1592, 1763 | `X4 = DFB` |
| 2052 | lmt8riv7 | uninitialized | loop-guarded | rate | defined at 2029, 2044, 2047 | `WRITE(IUMT3D) IL, IR, IC, RATE` |
| 2054 | lmt8riv7 | uninitialized | loop-guarded | rate | defined at 2029, 2044, 2047 | `WRITE(IUMT3D, *) IL, IR, IC, RATE` |
| 2445 | lmt8res7 | uninitialized | loop-guarded | rate | defined at 2439, 2442, 2478 | `BUFF(IC, IR, IL) = BUFF(IC, IR, IL) + RATE` |
| 2775 | lmt8ets7 | uninitialized | loop-guarded | petm2 | defined at 2759, 2762 | `HHCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |
| 2775 | lmt8ets7 | uninitialized | loop-guarded | pxdp2 | defined at 2758, 2761 | `HHCOF = - (PETM1 - PETM2) * C / ((PXDP2 - PXDP1) * X)` |
| 2901 | lmt8drt7 | uninitialized | loop-guarded | icr | defined at 2862 | `WRITE(IUMT3D) ILR, IRR, ICR, QIN, mhost, QSW` |
| 2901 | lmt8drt7 | uninitialized | loop-guarded | irr | defined at 2861 | `WRITE(IUMT3D) ILR, IRR, ICR, QIN, mhost, QSW` |
| 2901 | lmt8drt7 | uninitialized | loop-guarded | qin | defined at 2859, 2885 | `WRITE(IUMT3D) ILR, IRR, ICR, QIN, mhost, QSW` |
| 2903 | lmt8drt7 | uninitialized | loop-guarded | icr | defined at 2862 | `WRITE(IUMT3D, *) ILR, IRR, ICR, QIN, mhost, QSW` |
| 2903 | lmt8drt7 | uninitialized | loop-guarded | irr | defined at 2861 | `WRITE(IUMT3D, *) ILR, IRR, ICR, QIN, mhost, QSW` |
| 2903 | lmt8drt7 | uninitialized | loop-guarded | qin | defined at 2859, 2885 | `WRITE(IUMT3D, *) ILR, IRR, ICR, QIN, mhost, QSW` |
| 3105 | lmt8uzf1gw | uninitialized | loop-guarded | iuzfrch | defined at 3056, 3067, 3069, 3084, 3087 | `WRITE(IUMT3D) ((IUZFRCH(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3107 | lmt8uzf1gw | uninitialized | loop-guarded | iuzfrch | defined at 3056, 3067, 3069, 3084, 3087 | `WRITE(IUMT3D, *) ((IUZFRCH(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3167 | lmt8uzf1gw | uninitialized | loop-guarded | igwet | defined at 3139, 3157 | `WRITE(IUMT3D) ((IGWET(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3172 | lmt8uzf1gw | uninitialized | loop-guarded | igwet | defined at 3139, 3157 | `WRITE(IUMT3D, *) ((IGWET(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3442 | lmt8uzfet | uninitialized | loop-guarded | igwet | defined at 3414, 3432 | `WRITE(IUMT3D) ((IGWET(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3447 | lmt8uzfet | uninitialized | loop-guarded | igwet | defined at 3414, 3432 | `WRITE(IUMT3D, *) ((IGWET(J, I), J = 1, NCOL), I = 1, NROW)` |
| 3861 | lmt8sfr2 | uninitialized | conditional | text | defined at 3836, 3839, 3841, 3909, 3911 | `WRITE(IUMT3D) KPER, KSTP, NCOL, NROW, NLAY, TEXT, NSTRM` |
| 3864 | lmt8sfr2 | uninitialized | conditional | text | defined at 3836, 3839, 3841, 3909, 3911 | `WRITE(IUMT3D, *) TEXT, NSTRM` |
| 3916 | lmt8sfr2 | uninitialized | conditional | text | defined at 3836, 3839, 3841, 3909, 3911 | `WRITE(IUMT3D) KPER, KSTP, TEXT, NSTRM, NFLOWTYPE, NINTOT` |
| 3919 | lmt8sfr2 | uninitialized | conditional | text | defined at 3836, 3839, 3841, 3909, 3911 | `WRITE(IUMT3D, *) TEXT, NSTRM, NFLOWTYPE, NINTOT` |
| 3994 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `SFRFLOWVAL(I : I + LENGTH, :) = SFRFLOWVAL((I + 1) : USED, :)` |
| 4004 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `WRITE(IUMT3D) SFRFLOWVAL(1, L)` |
| 4006 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `WRITE(IUMT3D, *) SFRFLOWVAL(1, L)` |
| 4012 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `WRITE(IUMT3D) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L)` |
| 4014 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `WRITE(IUMT3D, *) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L)` |
| 4020 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `WRITE(IUMT3D) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L)` |
| 4023 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `WRITE(IUMT3D, *) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L)` |
| 4030 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `WRITE(IUMT3D) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L), SFRFLOWVAL(4, L)` |
| 4033 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `WRITE(IUMT3D, *) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L), SFRFLOWVAL(4, L)` |
| 4040 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `WRITE(IUMT3D) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L), SFRFLOWVAL(4, L), SFRFLOWVAL(...` |
| 4044 | lmt8sfr2 | uninitialized | loop-guarded | sfrflowval | defined at 3981, 3982, 3983, 3984, 3985, 3994 | `WRITE(IUMT3D, *) SFRFLOWVAL(1, L), SFRFLOWVAL(2, L), SFRFLOWVAL(3, L), SFRFLOWVAL(4, L), SFRFLOWV...` |
| 4158 | lmt8sfr2 | uninitialized | conditional | i | defined at 3991, 4147, 4152, 4172, 4219, 4224 | `WRITE(IUMT3D) I, L, IDISP, FLOWIN, XSA` |
| 4160 | lmt8sfr2 | uninitialized | conditional | i | defined at 3991, 4147, 4152, 4172, 4219, 4224 | `WRITE(IUMT3D, *) I, L, IDISP, FLOWIN, XSA` |
| 4382 | lmt8lak3 | uninitialized | conditional | text | defined at 4375, 4377, 4404 | `WRITE(IUMT3D) KPER, KSTP, NCOL, NROW, NLAY, TEXT, LKNODE` |
| 4385 | lmt8lak3 | uninitialized | conditional | text | defined at 4375, 4377, 4404 | `WRITE(IUMT3D, *) TEXT, LKNODE` |

### mf2005.f90 (8)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 348 | main | aliasing | global-aliasing | cc | argument 4 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 348 | main | aliasing | global-aliasing | cr | argument 3 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 348 | main | aliasing | global-aliasing | cv | argument 5 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 348 | main | aliasing | global-aliasing | hcof | argument 6 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 348 | main | aliasing | global-aliasing | hnew | argument 1 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 348 | main | aliasing | global-aliasing | ibound | argument 7 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 348 | main | aliasing | global-aliasing | rhs | argument 2 of pcgn2ap, which also assigns that module variable directly | `CALL PCGN2AP(HNEW, RHS, CR, CC, CV, HCOF, IBOUND, KKITER, KKSTP, KKPER, ICNVG, HNOFLO, IGRID)` |
| 359 | main | uninitialized | call-assumed | icnvg | defined at 306, 313, 322, 339, 348, 355, 366, 482, 486 | `IF (ICNVG .EQ. 1) GO TO 33` |

### obs2bas7.f90 (48)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 699 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `A = 1 / (DC * DR)` |
| 699 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `A = 1 / (DC * DR)` |
| 704 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(1) = 0.5 * (1. - DRF / DR)` |
| 704 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(1) = 0.5 * (1. - DRF / DR)` |
| 705 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(2) = 0.5 * DRF / DR` |
| 705 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(2) = 0.5 * DRF / DR` |
| 711 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(1) = 0.5 * (1. - DCF / DC)` |
| 711 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(1) = 0.5 * (1. - DCF / DC)` |
| 713 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(3) = 0.5 * DCF / DC` |
| 713 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(3) = 0.5 * DCF / DC` |
| 718 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(3) = A * (DR - DRF) * DCF` |
| 718 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(3) = A * (DR - DRF) * DCF` |
| 718 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(3) = A * (DR - DRF) * DCF` |
| 719 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(4) = A * DRF * DCF` |
| 719 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(4) = A * DRF * DCF` |
| 720 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(2) = A * DRF * (DC - DCF)` |
| 720 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(2) = A * DRF * (DC - DCF)` |
| 720 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(2) = A * DRF * (DC - DCF)` |
| 721 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(1) = A * (DR - DRF) * (DC - DCF)` |
| 721 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(1) = A * (DR - DRF) * (DC - DCF)` |
| 721 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(1) = A * (DR - DRF) * (DC - DCF)` |
| 721 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(1) = A * (DR - DRF) * (DC - DCF)` |
| 725 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(1) = A * (DR * DC - DR * DCF)` |
| 725 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(1) = A * (DR * DC - DR * DCF)` |
| 725 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(1) = A * (DR * DC - DR * DCF)` |
| 727 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(3) = A * (DR * DCF - DC * DRF)` |
| 727 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(3) = A * (DR * DCF - DC * DRF)` |
| 727 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(3) = A * (DR * DCF - DC * DRF)` |
| 727 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(3) = A * (DR * DCF - DC * DRF)` |
| 728 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(4) = A * (DC * DRF)` |
| 728 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(4) = A * (DC * DRF)` |
| 731 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(1) = A * (DR * DC - DC * DRF)` |
| 731 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(1) = A * (DR * DC - DC * DRF)` |
| 731 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(1) = A * (DR * DC - DC * DRF)` |
| 732 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(4) = A * (DR * DCF)` |
| 732 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(4) = A * (DR * DCF)` |
| 733 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(2) = A * (DC * DRF - DR * DCF)` |
| 733 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(2) = A * (DC * DRF - DR * DCF)` |
| 733 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(2) = A * (DC * DRF - DR * DCF)` |
| 733 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(2) = A * (DC * DRF - DR * DCF)` |
| 737 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(1) = A * (DR * DC - DC * DRF - DR * DCF)` |
| 737 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(1) = A * (DR * DC - DC * DRF - DR * DCF)` |
| 737 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(1) = A * (DR * DC - DC * DRF - DR * DCF)` |
| 737 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(1) = A * (DR * DC - DC * DRF - DR * DCF)` |
| 738 | sobs2bas7hbf | uninitialized | conditional | dcf | defined at 693 | `RINT(3) = A * (DR * DCF)` |
| 738 | sobs2bas7hbf | uninitialized | conditional | dr | defined at 696 | `RINT(3) = A * (DR * DCF)` |
| 739 | sobs2bas7hbf | uninitialized | conditional | dc | defined at 692 | `RINT(2) = A * (DC * DRF)` |
| 739 | sobs2bas7hbf | uninitialized | conditional | drf | defined at 697 | `RINT(2) = A * (DC * DRF)` |

### pcg7.f90 (15)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 599 | pcg7ap | uninitialized | loop-guarded | hhcof | defined at 387, 411, 459, 460, 596, 598, 834 | `CD(N) = (DONE + DEL) * HHCOF - CDCR - CDCC - CDCV - RELAX * (FCR + FCC + FCV)` |
| 713 | pcg7ap | uninitialized | loop-guarded | pn | defined at 705, 706, 722, 723 | `BHNEW = B * (P(NRL) - PN)` |
| 714 | pcg7ap | uninitialized | loop-guarded | pn | defined at 705, 706, 722, 723 | `HHNEW = H * (P(NRN) - PN)` |
| 715 | pcg7ap | uninitialized | loop-guarded | pn | defined at 705, 706, 722, 723 | `DHNEW = D * (P(NCL) - PN)` |
| 716 | pcg7ap | uninitialized | loop-guarded | pn | defined at 705, 706, 722, 723 | `FHNEW = F * (P(NCN) - PN)` |
| 717 | pcg7ap | uninitialized | loop-guarded | pn | defined at 705, 706, 722, 723 | `ZHNEW = Z * (P(NLL) - PN)` |
| 718 | pcg7ap | uninitialized | loop-guarded | pn | defined at 705, 706, 722, 723 | `SHNEW = S * (P(NLN) - PN)` |
| 787 | pcg7ap | uninitialized | loop-guarded | nh | defined at 766 | `BIGH = BIGH / SQRT(- HCOF(NH))` |
| 788 | pcg7ap | uninitialized | loop-guarded | nr | defined at 633, 778 | `BIGR = BIGR * SQRT(- HCOF(NR))` |
| 811 | pcg7ap | uninitialized | loop-guarded | kh | defined at 765 | `LHCH(1, II) = KH` |
| 812 | pcg7ap | uninitialized | loop-guarded | ih | defined at 763 | `LHCH(2, II) = IH` |
| 813 | pcg7ap | uninitialized | loop-guarded | jh | defined at 764 | `LHCH(3, II) = JH` |
| 816 | pcg7ap | uninitialized | loop-guarded | kr | defined at 777 | `LRCH(1, II) = KR` |
| 817 | pcg7ap | uninitialized | loop-guarded | ir | defined at 529, 775 | `LRCH(2, II) = IR` |
| 818 | pcg7ap | uninitialized | loop-guarded | jr | defined at 776 | `LRCH(3, II) = JR` |

### pcgn2.f90 (23)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 118 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `READ(UNIT = DATA_STRING(1), FMT = 400, IOSTAT = IOS) ITER_MO, ITER_MI, CLOSE_R, CLOSE_H` |
| 121 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `WRITE(IOUT, 800) 'TER_MO, ITER_MI, CLOSE_R, CLOSE_H', DATA_STRING(1)` |
| 125 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `READ(UNIT = DATA_STRING(2), FMT = 405, IOSTAT = IOS) RELAX, IFILL, UNIT_PC, UNIT_TS` |
| 128 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `WRITE(IOUT, 800) 'RELAX, IFILL, UNIT_PC, UNIT_TS', DATA_STRING(2)` |
| 134 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `READ(UNIT = DATA_STRING(3), FMT = 410, IOSTAT = IOS) ADAMP, DAMP, DAMP_LB, RATE_D, CHGLIMIT` |
| 137 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `WRITE(IOUT, 800) 'ADAMP, DAMP, DAMP_LB, RATE_D, CHGLIMIT', DATA_STRING(3)` |
| 143 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `READ(UNIT = DATA_STRING(4), FMT = 415, IOSTAT = IOS) ACNVG, CNVG_LB, MCNVG, RATE_C, IPUNIT` |
| 146 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `WRITE(IOUT, 800) 'ACNVG, CNVG_LB, MCNVG, RATE_C, IPUNIT', DATA_STRING(4)` |
| 157 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `READ(UNIT = DATA_STRING(1), FMT = *, IOSTAT = IOS) ITER_MO, ITER_MI, CLOSE_R, CLOSE_H` |
| 160 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `WRITE(IOUT, 800) 'TER_MO,ITER_MI,CLOSE_R,CLOSE_H', DATA_STRING(1)` |
| 163 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `READ(UNIT = DATA_STRING(2), FMT = *, IOSTAT = IOS) RELAX, IFILL, UNIT_PC, UNIT_TS` |
| 166 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `WRITE(IOUT, 800) 'RELAX, IFILL, UNIT_PC, UNIT_TS', DATA_STRING(2)` |
| 171 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `READ(UNIT = DATA_STRING(3), FMT = *, IOSTAT = IOS) ADAMP, DAMP, DAMP_LB, RATE_D, CHGLIMIT` |
| 174 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `WRITE(IOUT, 800) 'ADAMP, DAMP, DAMP_LB, RATE_D, CHGLIMIT', DATA_STRING(3)` |
| 179 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `READ(UNIT = DATA_STRING(4), FMT = *, IOSTAT = IOS) ACNVG, CNVG_LB, MCNVG, RATE_C, IPUNIT` |
| 182 | pcgn2ar | uninitialized | conditional | data_string | defined at 110 | `WRITE(IOUT, 800) 'ACNVG, CNVG_LB, MCNVG, RATE_C, IPUNIT', DATA_STRING(4)` |
| 1031 | max_hch | uninitialized | loop-guarded | node_save | defined at 1027 | `MHC_NODE = NODE_SAVE` |
| 1340 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NODE), CK_D(NCN))` |
| 1342 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NCN), CK_D(NODE))` |
| 1354 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NODE), CK_D(NRL))` |
| 1356 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NRL), CK_D(NODE))` |
| 1363 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NODE), CK_D(NLL))` |
| 1365 | ck_domain | aliasing | aliasing | ck_d | passed as arguments 1, 3, 4 of renumber; the callee writes dummy ck_d | `CALL RENUMBER(CK_D, MAX_NODE, CK_D(NLL), CK_D(NODE))` |

### pcgn_solve2.f90 (1)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 1917 | pcg | uninitialized | conditional | start_time | defined at 1829 | `solv_time = elapsed_time(2) - start_time` |

### utl7.f90 (39)

| Line | Unit | Detector | Category | Subject | Detail | Statement |
| ---: | --- | --- | --- | --- | --- | --- |
| 516 | u1drel | uninitialized | conditional | cnstnt | defined at 497, 503 | `A(J) = CNSTNT` |
| 517 | u1drel | uninitialized | conditional | cnstnt | defined at 497, 503 | `WRITE(IOUT, 3) ANAME, CNSTNT` |
| 523 | u1drel | uninitialized | conditional | fmtin | defined at 497, 506 | `WRITE(IOUT, 5) ANAME, LOCAT, FMTIN` |
| 526 | u1drel | uninitialized | conditional | fmtin | defined at 497, 506 | `IF (FMTIN .EQ. '(FREE)') THEN` |
| 529 | u1drel | uninitialized | conditional | fmtin | defined at 497, 506 | `READ(LOCAT, FMTIN) (A(J), J = 1, JJ)` |
| 535 | u1drel | uninitialized | conditional | cnstnt | defined at 497, 503 | `IF (CNSTNT .EQ. ZERO) GO TO 120` |
| 537 | u1drel | uninitialized | conditional | cnstnt | defined at 497, 503 | `A(J) = A(J) * CNSTNT` |
| 541 | u1drel | uninitialized | conditional | iprn | defined at 497, 507 | `IF (IPRN .EQ. 0) THEN` |
| 544 | u1drel | uninitialized | conditional | iprn | defined at 497, 507 | `ELSE IF (IPRN .GT. 0) THEN` |
| 622 | u2dint | uninitialized | conditional | fname | defined at 600 | `OPEN(UNIT = LOCAT, FILE = FNAME, FORM = FORM, ACCESS = ACCESS, ACTION = ACTION(1))` |
| 625 | u2dint | uninitialized | conditional | fname | defined at 600 | `OPEN(UNIT = LOCAT, FILE = FNAME, ACTION = ACTION(1))` |
| 639 | u2dint | uninitialized | conditional | iconst | defined at 610, 616 | `IA(J, I) = ICONST` |
| 640 | u2dint | uninitialized | conditional | iconst | defined at 610, 616 | `WRITE(IOUT, 82) ANAME, ICONST, K` |
| 642 | u2dint | uninitialized | conditional | iconst | defined at 610, 616 | `WRITE(IOUT, 83) ANAME, ICONST` |
| 649 | u2dint | uninitialized | conditional | fmtin | defined at 610, 619 | `WRITE(IOUT, 94) ANAME, K, LOCAT, FMTIN` |
| 653 | u2dint | uninitialized | conditional | fmtin | defined at 610, 619 | `WRITE(IOUT, 95) ANAME, LOCAT, FMTIN` |
| 657 | u2dint | uninitialized | conditional | fmtin | defined at 610, 619 | `WRITE(IOUT, 96) ANAME, LOCAT, FMTIN` |
| 662 | u2dint | uninitialized | conditional | fmtin | defined at 610, 619 | `IF (FMTIN .EQ. '(FREE)') THEN` |
| 665 | u2dint | uninitialized | conditional | fmtin | defined at 610, 619 | `READ(LOCAT, FMTIN) (IA(J, I), J = 1, JJ)` |
| 691 | u2dint | uninitialized | conditional | iconst | defined at 610, 616 | `IF (ICONST .EQ. 0) GO TO 320` |
| 694 | u2dint | uninitialized | conditional | iconst | defined at 610, 616 | `IA(J, I) = IA(J, I) * ICONST` |
| 698 | u2dint | uninitialized | conditional | iprn | defined at 610, 629, 701 | `IF (IPRN .LT. 0) RETURN` |
| 701 | u2dint | uninitialized | conditional | iprn | defined at 610, 629, 701 | `IF (IPRN .GT. 9 .OR. IPRN .EQ. 0) IPRN = 6` |
| 702 | u2dint | uninitialized | conditional | iprn | defined at 610, 629, 701 | `GO TO (401, 402, 403, 404, 405, 406, 407, 408, 409), IPRN` |
| 723 | u2dint | uninitialized | conditional | iprn | defined at 610, 629, 701 | `GO TO (501, 502, 503, 504, 505, 506, 507, 508, 509), IPRN` |
| 851 | u2drel | uninitialized | conditional | fname | defined at 829 | `OPEN(UNIT = LOCAT, FILE = FNAME, FORM = FORM, ACCESS = ACCESS, ACTION = ACTION(1))` |
| 854 | u2drel | uninitialized | conditional | fname | defined at 829 | `OPEN(UNIT = LOCAT, FILE = FNAME, ACTION = ACTION(1))` |
| 868 | u2drel | uninitialized | conditional | cnstnt | defined at 839, 845 | `A(J, I) = CNSTNT` |
| 869 | u2drel | uninitialized | conditional | cnstnt | defined at 839, 845 | `WRITE(IOUT, 2) ANAME, CNSTNT, K` |
| 871 | u2drel | uninitialized | conditional | cnstnt | defined at 839, 845 | `WRITE(IOUT, 3) ANAME, CNSTNT` |
| 878 | u2drel | uninitialized | conditional | fmtin | defined at 839, 848 | `WRITE(IOUT, 94) ANAME, K, LOCAT, FMTIN` |
| 882 | u2drel | uninitialized | conditional | fmtin | defined at 839, 848 | `WRITE(IOUT, 95) ANAME, LOCAT, FMTIN` |
| 886 | u2drel | uninitialized | conditional | fmtin | defined at 839, 848 | `WRITE(IOUT, 96) ANAME, LOCAT, FMTIN` |
| 891 | u2drel | uninitialized | conditional | fmtin | defined at 839, 848 | `IF (FMTIN .EQ. '(FREE)') THEN` |
| 894 | u2drel | uninitialized | conditional | fmtin | defined at 839, 848 | `READ(LOCAT, FMTIN) (A(J, I), J = 1, JJ)` |
| 921 | u2drel | uninitialized | conditional | cnstnt | defined at 839, 845 | `IF (CNSTNT .EQ. ZERO) GO TO 320` |
| 924 | u2drel | uninitialized | conditional | cnstnt | defined at 839, 845 | `A(J, I) = A(J, I) * CNSTNT` |
| 928 | u2drel | uninitialized | conditional | iprn | defined at 839, 858, 928 | `IF (IPRN .GE. 0) CALL ULAPRW(A, ANAME, 0, 0, JJ, II, 0, IPRN, IOUT)` |
| 1017 | ucolno | uninitialized | loop-guarded | bf | defined at 984, 998, 1002, 1006, 1010, 1012 | `WRITE(IOUT, 31) (BF(I), I = 1, NBF)` |

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

## Outside static scope

These undefined-behavior classes need the runtime check matrix (Process.md), not this report:

- Floating-point exceptions (overflow, divide-by-zero, invalid operands): compile with -ffpe-trap / -fpe0 across the matrix.
- Array bounds that depend on runtime values: -fcheck=all / -check all builds; only compile-time-constant subscripts are checked statically.
- Integer overflow: -fsanitize=undefined / -ftrapv builds.
- Argument aliasing through storage the analysis cannot see (pointer targets, sequence association across COMMON): differential -O0 vs -O2 runs across compilers.
