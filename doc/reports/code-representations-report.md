# Code representations report

Generated 2026-08-28T18:34:54-04:00 at commit 54615a1 for mf2005: 793 program units in 54 files (0 skipped).

## Overview

| Representation | Group | Status | Headline |
| --- | --- | --- | --- |
| Control-flow graph | Control and data flow (per unit) | ok | Units with a graph: 793; Structured: 581; Reducible (GOTO): 212 |
| Dominator tree and loop nest tree | Control and data flow (per unit) | ok | Units: 793; Loops: 2,972; Counted DO / DO WHILE: 2,803 / 98 |
| Reaching definitions, def-use chains, and SSA summary | Control and data flow (per unit) | ok | Units: 793; Variables: 20,864; Definitions / uses: 33,683 / 93,991 |
| Call graph with MOD/REF summaries | Whole program | ok | Units: 793; Call edges: 1,652; External callees (c / intrinsic / dummy / source / unknown): 25 (6 / 9 / 2 / 0 / 8) |
| State ownership graph | Whole program | ok | Globals: 1,744; Module variables: 1,369; COMMON members: 37 |
| Program dependence graph and slicing | Whole program | ok | Units: 793; Nodes (statement lines): 42,042; Data-dependence edges: 113,286 |
| Storage association model | Whole program | ok | COMMON blocks: 9 (0 not consistent); EQUIVALENCE sets: 0; Sequence-association sites: 367 (26 possible) |
| Affine loop access summaries | Array and numeric semantics | ok | Loops: 2,904; Loop nests (top-level): 1,408; Max nesting depth: 6 |
| Kind propagation | Array and numeric semantics | ok | Sites: 3,738; Mixed arithmetic: 1,277; Narrowing / widening: 916 / 844 |
| Reduction sites and reassociation sensitivity | Array and numeric semantics | ok | Sites: 1,249; Order-sensitive (fp-reassociation): 636; Exact: 613 |
| I/O resource model | Non-code models | ok | I/O statements: 3,855; Program units doing I/O: 331; Distinct unit expressions: 107 |
| Phase protocol and package matrix | Non-code models | ok | Packages: 56; Phases: 19; Protocol calls: 244 |
| Configuration space | Non-code models | ok | Files with directives: 9 of 63; Directive lines: 46; Macros referenced: 15 |
| Clone classes (identifier-normalized) | Non-code models | ok | Clone classes: 939; Occurrences: 3,023; Statements covered: 21,626 of 54,477 (39.7%) |
| Coverage overlay on the control-flow graph | Dynamic and external | partial | Source: doc/reports/coverage_2026-08-20_02h45m42/gcc-release-single/coverage-gcc-release-single.json; Build variant: gcc-release-single; Report time: 2026-08-20T02:51:30 |
| Linkage ground truth | Dynamic and external | ok | Objects: 58 (54 Fortran, 4 C); Files matched: 54 of 54 Fortran objects agree fully; Definition agreement: 100.0% (2,099 matched, 0 missing, 0 extra) |
| External IR readiness | Dynamic and external | partial | lfortran: available (0.64.0); flang: not found; psyclone: not found |

## Control and data flow (per unit)

Structures computed inside one program unit: the substrate for structured-control-flow recovery, coverage, and Rust mutability.

### Control-flow graph (`cfg`)

Status: **ok**

Basic blocks and edges of every program unit, with labels, GOTO, computed GOTO, arithmetic IF, shared-termination DO loops, and ERR=/END= I/O branches lowered to ordinary edges. Each unit is classified as structured (no jumps), reducible (jumps, but every loop has one entry), or irreducible (a loop entered at two points).

**For the port:** Rust has no GOTO: every reducible unit can be restructured mechanically (relooper-style) into loop/break/continue; every irreducible unit needs code duplication or a state-machine rewrite first. The graph is also the substrate for branch coverage and for every dataflow view below.

| Metric | Value |
| --- | ---: |
| Units with a graph | 793 |
| Structured | 581 |
| Reducible (GOTO) | 212 |
| Irreducible | 0 |
| Blocks | 39,094 |
| Edges | 51,624 |
| Jump statements | 1,172 |
| Units skipped | 0 |

Assumptions and policies:

- Units the front end skips (EQUIVALENCE, ENTRY, assigned GOTO, WHERE/FORALL/ASSOCIATE/BLOCK) have no graph; they are listed with the reason.
- Blocks are delimited by the lowering's variable events, so a block without events (a bare CONTINUE) shows no lines.
- STOP lowers to a self-looping halt block; RETURN and the labeled END flow to the single exit block.
- Reducibility is decided on the graph after unreachable blocks are removed; dead code after an unconditional jump is counted, not drawn.

### Dominator tree and loop nest tree (`dominators`)

Status: **ok**

For every program unit, the dominator tree of its control-flow graph (the entry at the root; a block's parent is the last block every path must pass through to reach it) and the loop nest tree of its natural loops: per loop the header block, nesting depth, block count, back edges, exit edges and distinct exit targets, the source line range of the body, and its kind (counted DO, DO WHILE, or a loop formed by a backward GOTO or arithmetic IF).

**For the port:** The loop nest tree is the scaffold of the Rust loop structure: a counted DO with one exit target becomes a for-range, a DO WHILE a while, and every multi-exit or jump-formed loop a loop with break (a labeled break when the exit leaves an enclosing loop). Dominators decide where a value is definitely computed before use, which drives let placement, phi counts in the dataflow view, and where restructuring must duplicate code (irreducible edges).

| Metric | Value |
| --- | ---: |
| Units | 793 |
| Loops | 2,972 |
| Counted DO / DO WHILE | 2,803 / 98 |
| GOTO-formed loops | 71 |
| Multi-exit loops | 262 |
| Max nesting depth | 6 |
| Units with irreducible loops | 0 |

Assumptions and policies:

- Only blocks reachable from the entry are considered; unreachable code has no dominator and belongs to no loop.
- Natural loops are merged per header block: two back edges to the same header form one loop with two back edges, never two loops.
- A loop is a counted DO or a DO WHILE when its header block's first event lies on that DO statement's line (the lowering places the loop counter definition or the WHILE condition reads in the header block); a DO without loop control, or a DO WHILE with a constant condition, has no header event and is matched instead as the largest natural loop whose body lines fall inside that DO construct's line span, innermost DO first, each loop claimed once.
- Every other loop is kind 'goto': it was formed by a backward GOTO, arithmetic IF, computed GOTO, or an ERR=/END= branch.
- The body line range is the minimum and maximum event line over the loop's blocks; event-free blocks (bare CONTINUE, plain DO header) contribute no lines, so the range may start after the DO statement.
- Exit targets count distinct blocks outside the loop reached by exit edges; a RETURN inside a DO adds the exit block as a second target and makes the loop multi-exit.
- The Rust hint is a loop-form suggestion only: for-range needs a counted DO with one exit target, while needs a DO WHILE, everything else is a loop with break; whether the counter is modified inside the body is left to the dataflow view.
- Units skipped by the front end have no graph and are absent here (the control-flow graph view lists them).

### Reaching definitions, def-use chains, and SSA summary (`dataflow`)

Status: **ok**

For every program unit: which assignment reaches which read (reaching definitions solved over the control-flow graph, def-use chains per read), how many phi nodes an SSA form would need per variable (iterated dominance frontier of its definition blocks), and a classification of every variable by role (dummy, global, saved, local, result) and mutability (read-only, single-assignment, mutable, loop-carried, write-only, dead-store).

**For the port:** The mutability class is the Rust binding form: a read-only dummy becomes a shared reference, a written dummy a mutable reference, a single-assignment local a plain let, a mutable or loop-carried local a let mut, and saved or global state a struct field. Def-use chains show which stores feed which reads (what to keep when a computation is split), dead stores are code the port can drop, and phi counts size the SSA-style rewrite of GOTO-heavy units.

| Metric | Value |
| --- | ---: |
| Units | 793 |
| Variables | 20,864 |
| Definitions / uses | 33,683 / 93,991 |
| Def-use edges | 163,194 |
| Phi nodes (SSA) | 48,564 |
| Single-assignment | 2,872 (13.8%) |
| Loop-carried | 2,840 |
| Dead stores | 670 |

Assumptions and policies:

- Definitions and uses are the lowering's variable events, at statement line granularity; only blocks reachable from the entry are analysed.
- A scalar definition kills every earlier definition of the same variable; an array definition (a variable with a declared shape or array attribute, including whole-array assignment) is a weak update that kills nothing, so every earlier array definition still reaches.
- A bare variable passed to a call is read by the callee and, when the callee's inferred signature says the dummy is written (or the callee is unknown), possibly written: such call-argument definitions are weak (kill nothing) and count as uses; arguments are matched by position.
- ALLOCATE, DEALLOCATE and NULLIFY change association status only and are neither definitions nor uses here.
- Parameters (named constants), procedure names, and statement functions are not variables in this view.
- Dummies, module/COMMON/host variables, and saved variables are implicitly defined at entry and live at exit; a read with no reaching definition is an entry value, never an error, and their stores are never dead.
- A substring assignment to a character scalar and a derived-type component assignment update only part of the variable and are weak definitions like array element stores (assignment statements only; a READ into a substring or component still counts as a whole definition).
- A dead store is a direct definition (assignment, READ, DO counter, I/O status) of a local (non-dummy, non-global, non-saved, non-result) variable that reaches no use; loop-counter definitions on a DO statement are exempt because the loop itself reads the counter, and a definition made by a callee through a call argument is never reported as a dead store.
- A variable is loop-carried when a definition inside a natural loop reaches a use inside the same loop through the loop's back edge (computed by a reaching-definitions pass restricted to the loop body seeded with the back-edge contributions).
- Single-assignment means exactly one definition line, not inside any loop; the value is not otherwise known to be constant.
- Phi counts use the iterated dominance frontier of the definition blocks, for arrays and scalars alike (an array phi stands for a memory phi).
- Uses and definitions are deduplicated per (line, variable).

## Whole program

Interprocedural structures: what calls what, who owns which state, what depends on what, and what Fortran storage tricks Rust cannot express.

### Call graph with MOD/REF summaries (`callgraph`)

Status: **ok**

Every program unit as a node, every CALL statement and function reference as an edge (with call-site lines and counts), and the callees that are not Fortran units in the corpus classified as C functions, intrinsics, dummy procedures, or unknown. Each unit carries a MOD/REF summary: the inferred intent of every dummy argument (in, out, inout, unused) and the global variables it reads, writes, or passes on to calls. Whole-program facts: recursion cycles (strongly connected components), a callees-before-callers porting order, fan-in and fan-out, reachability from the main programs, and call depth.

**For the port:** The porting order says which units can be translated and tested first (leaves with no corpus callees), which ones must be ported together (recursion cycles), and which are dead candidates (unreachable from any main program). The MOD/REF summary is the Rust signature draft: in dummies become shared references, out/inout become &mut, and global reads/writes say which module state each function must borrow; a global passed on to a call with writing intent marks a hidden &mut.

| Metric | Value |
| --- | ---: |
| Units | 793 |
| Call edges | 1,652 |
| External callees (c / intrinsic / dummy / source / unknown) | 25 (6 / 9 / 2 / 0 / 8) |
| Recursion cycles | 0 |
| Unreachable units | 13 |
| Max call depth | 6 |

Assumptions and policies:

- Edges come from CALL statements and function references recognised by the lowering; a name referenced with an argument list that the lowering could not tell from an array reference is reported as an external callee of kind unknown rather than dropped.
- A corpus procedure passed as an actual argument (EXTERNAL name or module procedure) gets a reference edge from the passing unit (flag 1 in the edge list, dashed in the graph) so that it is reachable and ordered before its passer; the unit that eventually calls it through the dummy is not identified.
- Callee names resolve to the first corpus unit with that name (case-insensitive); names defined more than once are listed in the section note and their edges point at the first definition.
- A callee is classified as C when its name (lower-cased, trailing underscores removed) matches a function-like definition or prototype at the start of a line in the C files under the source directory (regex `^[A-Za-z_][\w \t*]*\b(\w+)\s*\(` per line, C keywords excluded); this is a textual heuristic, not a compile.
- A callee is classified as intrinsic when it is in the built-in list of standard Fortran intrinsic and standard procedures plus common compiler extensions (DATE_AND_TIME, SYSTEM_CLOCK, GETARG, SECNDS, ISNAN, ...); as dummy when the calling unit declares it as a dummy argument (procedure passed in); as source when a SUBROUTINE or FUNCTION of that name exists in the parsed sources but was not lowered as a corpus unit (for example an internal procedure of a main program); otherwise unknown.
- Dummy intents are inferred from use, not declared: in = read (or passed whole to a call) and never written; out = assigned directly and never read; inout = both, or written only by being passed whole to a call whose callee may write it; unused = neither read, passed, nor written.
- Globals are module, host-associated, and COMMON variables. 'Written through a call' lists globals passed whole as call arguments (any callee, since the lowering assumes such arguments may be written); the actual write depends on the callee's intent, visible in its own row.
- Recursion cycles are strongly connected components of size two or more plus units that call themselves directly.
- Reachability and depth are computed from every unit of kind program (the corpus has one per executable); depth is the shortest call distance from the nearest program. Without any program unit every unit counts as reachable and depth is empty.
- The porting order lists callees before callers over the condensation of the call graph; members of one cycle are listed together, sorted by id.

### State ownership graph (`ownership`)

Status: **ok**

15 variable(s) are exported by more than one used module (see the ambiguous column).

Every persistent variable of the program (module variable, COMMON member, SAVEd or DATA-initialised local) with its declaring container, owner package, type, and the program units that write it (directly, through a call argument, or by allocation) and read it, each tagged with the protocol phase it runs in; the variables are classified by how ownership is shared across packages and phases.

**For the port:** Rust needs one owner per value: package-private globals become private fields of the package struct, values written only during setup become build-once fields exposed by reference, globals mutated from several packages need an explicit ownership decision (the list of packages is the negotiation), and SAVEd locals become fields of a per-procedure state struct. The package x phase write matrix shows where mutation concentrates in the time loop.

| Metric | Value |
| --- | ---: |
| Globals | 1,744 |
| Module variables | 1,369 |
| COMMON members | 37 |
| SAVE locals | 338 |
| Shared-mutable | 99 |
| Shared-read | 118 |
| Package-private | 625 |
| Allocated-immutable | 813 |

Assumptions and policies:

- A global is keyed by its container: module variables by declaring module (resolved through the unit's USE lists; a name exported by several used modules is attributed to the module that declares it, and flagged ambiguous when more than one does), COMMON members by block name, SAVEd locals by unit; named constants are excluded. The owner package comes from the module name (GWFLPFMODULE -> LPF, GLOBAL and GWFBASMODULE -> BAS, PARAMMODULE -> PAR) or, when that names no package of the corpus, from the defining file (pcgn_solve2.f90 -> PCGN).
- Writer kinds: 'direct' is an assignment, READ, DO index, or pointer assignment in the unit; 'alloc' is ALLOCATE or the target side of a pointer assignment; 'dealloc' is DEALLOCATE or NULLIFY; 'call-arg' is a whole variable passed to a procedure whose inferred signature may write that argument (or whose signature is unknown) - a pass to an argument the callee never writes counts as a read.
- Reads are every value use in the unit, including subscript and condition reads; a unit that both reads and writes a global appears in both lists.
- The phase of a writer or reader is the unit's own phase suffix, or for helpers and utilities the set of protocol phases whose entry points reach it through the call graph (joined with '|'); a unit reached from no phase is 'other'.
- Classes are assigned in order: unused (no writer, no reader), write-only (no reader), allocated-immutable (every write in an AR/DA/PNT/PSV phase and read elsewhere), shared-mutable (writers in two or more packages), shared-read (one writing package, two or more packages involved), package-private (one package writes and reads it); a variable with writers in setup phases and readers only inside the writing package is allocated-immutable, not package-private.
- SAVEd locals include DATA-initialised and declaration-initialised variables and, under a bare SAVE statement, every declared non-dummy local; their only writer and reader is the declaring unit, so their class reflects phases only.
- Units the front end skipped have no events, so their reads and writes are missing; host-associated variables of module procedures are attributed to the host module.

### Program dependence graph and slicing (`pdg`)

Status: **ok**

For every program unit, a graph whose nodes are source lines and whose edges are data dependences (a definition of a variable reaching a use) and control dependences (a line executes only when a branch line decides so). Every call site carries a summary: the callee, the actual argument variables by position, the positions the callee may write, and the globals it writes. The page slices this graph backward or forward from any line, optionally following calls into callees.

**For the port:** A backward slice from an output is the smallest set of statements a port must reproduce for that output; a forward slice from an input shows every consumer of a value. Slices scope the review of a numeric discrepancy to the lines that can cause it, expose which dummies and globals a statement really depends on (the Rust borrow set), and the output-slice size per unit ranks units by how tangled their outputs are.

| Metric | Value |
| --- | ---: |
| Units | 793 |
| Nodes (statement lines) | 42,042 |
| Data-dependence edges | 113,286 |
| Control-dependence edges | 34,174 |
| Call sites | 3,418 |
| Max in-degree | 218 |

Assumptions and policies:

- Nodes are source lines: several statements on one line (an IF with its action, or a multi-statement line) merge into one node.
- Data dependences come from reaching definitions over the unit's own control-flow graph: an assignment to a scalar local kills earlier definitions of that variable on the path; assignments to arrays, pointers/allocatables, character variables, module arrays, and to module or host variables whose rank is unknown are weak updates that kill nothing.
- A variable passed whole to a call is a weak (may-)definition at the call line only when the callee's inferred signature says that position may be written (directly or through further calls); for callees without a signature (external, program, duplicate names) or with fewer dummies than actuals every variable actual may be written.
- A use whose only reaching definition is the unit entry (a dummy or a global read before any local assignment) has no data edge; such lines are recorded per dummy as entry uses for forward slicing across calls.
- Control dependence is computed at basic-block level (Ferrante-Ottenstein-Warren) and mapped to lines: every line of a dependent block depends on the branch line of its controlling block, taken as the last event line of that block.
- A branch whose condition references no variable (IF (ALLOCATED(X)), IF (.TRUE.), DO WHILE (.TRUE.)) leaves its block without events; its dependents are then attached to the nearest branch statement (IF, ELSE IF, DO, SELECT CASE, CASE, arithmetic or computed GOTO) at or before the dependent block's first line, which becomes a node of its own; a dependence that cannot be attributed to any line is counted, not drawn.
- Unreachable blocks (dead code after an unconditional jump) contribute no nodes or edges.
- Call summaries use the inferred intents of corpus callees; for callees without a signature (external, program, or duplicate names) every variable actual counts as possibly written.
- Interprocedural slicing on the page follows dummies only (written positions backward, all variable actuals forward) and globals written by the callee backward; globals read by the callee are not followed.
- The output-slice size is the number of lines in the intraprocedural backward slice from every line that assigns a dummy, a global, or the function result.

### Storage association model (`storage`)

Status: **ok**

Every site where the program relies on Fortran storage or sequence association rather than on typed ownership: COMMON block layouts per unit, EQUIVALENCE sets with their overlaps, array elements or sections passed to array dummies, assumed-size and adjustable-shape dummies, assumed-length character dummies, substrings and internal files, and POINTER/TARGET/ALLOCATABLE declarations and pointer assignments.

**For the port:** None of these has a direct Rust equivalent: each site names the explicit construct that replaces it (a shared struct, an explicit slice from an offset, a view carrying its own dims, a byte buffer, an index into a grid table) so the port neither reproduces aliasing by accident nor loses the semantics the aliasing encoded.

| Metric | Value |
| --- | ---: |
| COMMON blocks | 9 (0 not consistent) |
| EQUIVALENCE sets | 0 |
| Sequence-association sites | 367 (26 possible) |
| Assumed-size dummies | 23 (+38 assumed-shape) |
| Adjustable dummies | 678 |
| Character sites | 190 |
| Pointer sites | 3,271 (863 declarations, 2408 assignments) |

Assumptions and policies:

- Declarations are read from the syntax tree of every program unit and module, so units the front end skipped (EQUIVALENCE) are covered; call sites come from the front end's call list and are missing for skipped units.
- A COMMON block is consistent when every unit declares the same sequence of (type class, element count); member names may differ. Element counts need constant bounds; a member with a non-constant bound compares as unknown and makes the block 'unverified' rather than inconsistent.
- EQUIVALENCE offsets are computed in elements of each member's own type from constant subscripts (column-major) or substring starts; a set is type punning when the members' type classes differ and a partial overlap when any member starts at a non-zero offset or the members' sizes differ.
- Sequence association is reported when an array element is passed to a dummy the callee declares as an array (explicit, adjustable, or assumed-size); an array section passed to such a dummy is a contiguous pass when it names whole leading dimensions followed by scalar subscripts (A(:,:,K)) and a possible copy-in/copy-out otherwise; a callee outside the corpus or defined twice makes the site 'possible' since its dummies are unknown.
- Adjustable dummies are explicit-shape dummy arrays whose bounds name any variable (dummy, module, or COMMON); assumed-shape dummies are listed for contrast and need no storage association.
- Character sites cover assumed-length (*) dummies, substrings passed as actual arguments in CALL statements, and READ/WRITE whose unit is a character variable (internal file); substrings inside function references are not scanned.
- Pointer sites are one per declaration statement carrying POINTER, TARGET, or ALLOCATABLE (also in module specification parts) and one per pointer assignment; the multi-grid PNT/PSV routines account for most of the pointer assignments.

## Array and numeric semantics

Loop access patterns, precision flow, and reduction order: where iteration order and kinds decide bit-for-bit reproducibility.

### Affine loop access summaries (`loops`)

Status: **ok**

Every DO loop (counted, DO WHILE, shared-termination) with its index, bounds, depth and enclosing loop; every array reference in its body with read/write direction and each subscript classified as affine (integer-coefficient combination of the enclosing loop indices plus loop-invariant symbols), indirect (subscripted by another array) or nonaffine; and a dependence verdict per loop: order-independent, carried with a distance vector, scalar-carried, or unknown.

**For the port:** Order-independent loops become iterators, chunks_mut or rayon parallel loops without changing results; carried loops must stay sequential with the distance made explicit (a sliding window or an in-place update); unknown loops (indirect subscripts, calls, nonaffine indices) stay sequential and need a runtime check before any restructuring. Indirect subscripts (IBOUND, IPOS-style gathers) mark where slices and bounds checks replace raw indexing.

| Metric | Value |
| --- | ---: |
| Loops | 2,904 |
| Loop nests (top-level) | 1,408 |
| Max nesting depth | 6 |
| Order-independent | 1,360 (46.8%) |
| Carried | 149 |
| Scalar-carried | 583 |
| Unknown | 812 |
| Loops with indirect subscripts | 287 |

Assumptions and policies:

- A subscript is affine when it is a linear combination of loop indices with integer-constant coefficients plus symbols not assigned anywhere in the loop body; products or quotients of invariant symbols stay invariant; anything involving a variant scalar, a function, or a product of indices is nonaffine; a subscript containing an array reference is indirect; a section (colon) subscript is classed as section and treated as unknown for dependences.
- Names assigned in a loop body are assignment targets, READ items, nested DO indices, ALLOCATE/DEALLOCATE/NULLIFY objects, IOSTAT-style specifiers, actuals passed to procedures whose inferred signature writes the dummy (or whose signature is unknown), and module variables the callee is known to write.
- Array references are element/section references whose base is a declared or module array or a subscripted nonlocal name; substrings of scalar characters are not arrays; an array passed whole or by element to a procedure that may write it is recorded as a call write and makes the loop's dependence unknown.
- Two affine accesses to the same array are compared only when their index coefficients and invariant symbols agree per dimension; a constant difference on a dimension that involves this loop's index alone gives the distance; when no dimension involves the loop index every iteration touches the same cells (distance *); differences on dimensions of other loops only do not carry a dependence for this loop.
- A scalar written and read in the body is a temporary when its first write precedes its first read in program order (reads of a statement count before its write), whether or not the write is conditional; otherwise it is scalar-carried.
- Loop-carried effects through procedures that read module variables, through pointer aliasing, or through EQUIVALENCE are not modeled; units the front end skips have no loops listed.
- DO WHILE and plain DO loops have no index; their body accesses are classified against the enclosing counted loops only.

### Kind propagation (`precision`)

Status: **ok**

The type class of every expression (integer, real, double, complex, logical, character) derived from declarations, implicit typing, module declarations, literal forms and intrinsic result rules; the sites where single and double precision meet (mixed arithmetic, narrowing and widening assignments, single-precision literals in double context, mixed comparisons, integer divisions feeding a real result); and, per real variable, the kinds that flow into it.

**For the port:** Rust has no implicit promotion: every mixed site becomes an explicit cast whose placement decides the result bit pattern. Variables with a single inflow kind map directly to f32 or f64; variables that receive both need a decision, and under the double build (default REAL promoted to 8 bytes) the real/double distinction collapses everywhere except explicit REAL*4 / KIND=4 declarations, so both builds must be reproduced from the same port.

| Metric | Value |
| --- | ---: |
| Sites | 3,738 |
| Mixed arithmetic | 1,277 |
| Narrowing / widening | 916 / 844 |
| Literal precision | 273 |
| Mixed comparisons | 423 |
| Integer divisions feeding reals | 5 |
| Variables needing a decision | 1,167 |
| Units affected | 261 of 793 |

Assumptions and policies:

- Type classes follow the front end's vocabulary (integer, real, double, complex, logical, character, derived, unknown); REAL*8, REAL(8) and REAL(KIND=k) with k a resolvable integer constant are refined to double or real, other kind selectors stay unknown.
- A real literal is double when it has a D exponent or a kind suffix that resolves to 8 (or cannot be resolved); otherwise it is single precision.
- Promotion follows integer < real < double; complex absorbs any numeric operand; an operation with an unknown operand has unknown kind and is never reported as a site.
- Module variables are typed from the module's declarations (transitively through USE); host-associated names use the enclosing module; a name that resolves nowhere falls back to the unit's implicit typing.
- Function results use the corpus definition's declared or implicit type; unknown external functions use the caller's implicit type for the name; the usual intrinsic result rules (DBLE, REAL, FLOAT, SNGL, INT, NINT, generic math and reductions) are applied and other intrinsics are unknown.
- Derived-type components (nested included) are typed from the type definitions visible in the unit or its modules; otherwise the reference is unknown.
- A single-precision literal meeting a double operand or a double target is reported as literal-precision, not as mixed arithmetic or widening.
- Integer divisions are reported only when their integer result demonstrably feeds a real or double result in the same statement (assignment target, mixed operation, comparison, or conversion intrinsic); divisions passed to procedures are not.
- Inflow kinds record the right-hand-side kinds of assignments to a variable inside one unit; values received through dummies, READ, or calls are not tracked.
- Under the double build option the reported real/double distinction collapses except for explicit REAL*4 / KIND=4 declarations; sites are reported for the source as written.

### Reduction sites and reassociation sensitivity (`reductions`)

Status: **ok**

Every accumulation inside a DO loop (S = S + e, S = S - e, S = S * e, S = e + S, S = MAX/MIN(S, e), logical S = S .OR./.AND. e, and A(k) = A(k) + e into a slot fixed for the innermost loop) and every SUM / PRODUCT / DOT_PRODUCT / MAXVAL / MINVAL reference, with the accumulator and operand kinds, the enclosing loop nest, and whether the result depends on summation order (floating-point + - *) or is exact (integer, logical, max, min).

**For the port:** Floating-point sums are not associative: a Rust iterator sum, a pairwise or SIMD reduction, or a parallel fold changes the last bits unless the Fortran summation order is kept (or a Kahan/pairwise policy is decided and validated). Exact sites can use iterators freely. Mixed-kind sites (a double accumulator fed single-precision products, or the reverse) pin where the widening happens.

| Metric | Value |
| --- | ---: |
| Sites | 1,249 |
| Order-sensitive (fp-reassociation) | 636 |
| Exact | 613 |
| Unknown kind | 0 |
| Mixed-kind | 92 |
| Units with fp reductions | 155 |
| Intrinsic reductions | 16 |

Assumptions and policies:

- A site is an assignment inside a DO loop whose target appears as the leftmost term of an additive chain, as a factor of a product, as an argument of MAX/MIN (or their kind-specific forms), or as an operand of .OR./.AND.; the target is matched by its normalized text.
- An array-element accumulator counts only when its subscripts contain neither the innermost loop's index nor any name assigned in that loop's body; scatter-adds through varying subscripts are loop accesses, not reduction sites.
- Sensitivity is fp-reassociation for real, double or complex accumulators under + - *, exact for integer or logical accumulators and for MAX/MIN, and unknown when the accumulator kind is unknown.
- Mixed-kind flags a real accumulator with a double operand or a double accumulator with a real operand; integer operands are not flagged.
- Intrinsic reductions are typed by their argument kind; their summation order is compiler-defined and reported as fp-reassociation when the kind is real, double or complex.
- Reductions written with GOTO loops, WHERE/FORALL, or in units the front end skips are not listed.

## Non-code models

Resources, protocols, configurations, and duplication that the source implies but never states.

### I/O resource model (`io`)

Status: **ok**

Every file-I/O statement of the corpus with its unit expression canonicalized (a literal unit, a named unit variable, an IUNIT(k) slot, the default unit, or an internal character file), the format it uses (list-directed, a resolved FORMAT label, or a string), the specifiers that decide the file's identity and error handling, and the item count. A FORMAT catalogue classifies each format by its edit descriptors, and a resource graph relates unit expressions to the program units that open, read, write, position, and close them.

**For the port:** Fortran unit numbers are a global mutable resource table that Rust replaces with owned handles: the resource graph shows which routine must own each handle and which routines borrow it, and the IUNIT(k) slots show the package-to-file indirection that becomes a typed configuration struct. Fixed-width formats fix the byte layout of every listing and binary file, so they are the specification for the port's output compatibility tests; list-directed and internal I/O mark the places where a parser, not a formatter, is needed.

| Metric | Value |
| --- | ---: |
| I/O statements | 3,855 |
| Program units doing I/O | 331 |
| Distinct unit expressions | 107 |
| FORMAT statements | 1,821 |
| Fixed-width formats | 1,094 |
| List-directed statements | 910 |
| Internal-file statements | 252 |
| IUNIT indices used | 47 |

Assumptions and policies:

- A unit expression is canonicalized by its text: a named unit variable such as IN or IOUT is one resource across all program units even though different callers pass different actual units; IUNIT(k) keeps a constant index and keeps the variable text otherwise; a character variable used as the unit is an internal file; any other expression keeps its text.
- A FORMAT label is resolved inside the program unit that contains the statement; an unresolved label is reported as such, not guessed.
- The edit-descriptor histogram is computed from the FORMAT text (string literals and Hollerith constants counted as literals), so a format held in a character variable is only counted as 'variable format'.
- The item count is the number of top-level items in the input/output list; an implied-DO counts as one item and NAMELIST I/O as zero.
- Internal subprograms are attributed to their own program unit, not to the host; statements in units the front end skipped are not visited.
- The resource life cycle (opened by, read by, closed by) is per unit expression, not per run: whether a READ actually follows an OPEN of the same file at run time is a dynamic property this model does not check.
- Only program units with at least one I/O or FORMAT statement get a row.
- IUNIT(k) slots are followed one call deep: a slot passed as an actual argument is attributed to the callee's dummy at that position (the unit variable the callee reads), and slot names come from the CUNIT DATA table when the corpus has one; a slot forwarded further through another dummy is not followed.

### Phase protocol and package matrix (`phases`)

Status: **ok**

2 PROGRAM units; the protocol is read from MAIN (mf2005.f90); the others are HYDFMT (hydprograms/hydfmt.f90).

The ordered sequence of package calls the main program makes, with the loop nest (stress period, time step, iteration) and the guard condition around each call, folded into a phase state machine; and the matrix of which package implements which phase, cross-checked against what the main program actually calls and reaches.

**For the port:** The protocol is the trait the Rust port needs: one method per phase, called in this order under these loops. Phases implemented but never reached from the main program are dead code to drop; calls to names outside the corpus are the external surface; the guard column gives the IUNIT index that activates each package.

| Metric | Value |
| --- | ---: |
| Packages | 56 |
| Phases | 19 |
| Protocol calls | 244 |
| Transitions | 47 |
| Loop nesting depth | 3 |
| Phases implemented, unreachable | 0 |
| Phases reached only indirectly | 94 |
| External callees | 0 |

Assumptions and policies:

- Unit names follow <family><digit>...<PKG><digit><PHASE>: the family prefix is GWF/OBS/GLO/LMT/HYD plus one digit (possibly repeated, as in GWF2HYD7BAS7AR), the package is the letters (plus the 1/2/2I/4 of MNW1, MNW2, MNW2I, DE4) before the version digit, and the phase is the trailing letters; OBS and HYD packages keep their family (OBSBAS, HYDBAS), the LMT family maps to package LMT and GLO to BAS.
- A leading S marks an internal helper when the rest of the name starts with a family prefix or with a package already known from the corpus (SGWF2BAS7PNT, SSWR_..., SDE47N); helpers are classified by that package and never count as protocol entry points.
- Recognised phases are AR RP ST AD FM AP CV OC BD BDS BDCH BDADJ SE OT DA PNT PSV; any other suffix is 'other'. Names starting with U without a family prefix are utilities: package from the file (utl7 -> UTL, parutl7 -> PAR, hufutl7 -> HUF) and phase 'util' when the file stem contains UTL, otherwise 'other'.
- A name that does not fit the convention takes its package from the enclosing module, else from the file stem classified the same way (gwf2sfr7.f90 -> SFR, pcgn2.f90 -> PCGN), else '?'; SWI2 and SWI, PARUTL and PAR, HUFUTL and HUF, PARAM and PAR, GLOBAL and BAS are merged.
- The protocol is read from the execution part of the main program (the PROGRAM named MF2005, else the unnamed main program of mf2005.f90, else the program with the most calls): CALL statements in textual order, with the stack of enclosing DO loops (their index variables) and the innermost enclosing IF/ELSE IF/CASE condition text as the guard; an ELSE branch is recorded as .NOT. of its IF condition.
- Transitions link consecutive calls at the same loop depth (the state at a depth is reset when its loop ends) plus one loop-back transition from the last to the first call of every loop body; guards are not evaluated, so the state machine is the union over every input.
- Reachability is transitive over CALL statements and function references resolved by name inside the corpus; a phase 'implemented but not reached' is unreachable from the main program through any call chain, while 'not called from main' only means the main program never names it directly (PNT/PSV are normally called from AR).
- Calls to Fortran intrinsic subroutines (DATE_AND_TIME, ...) are marked intrinsic; a callee absent from the parsed corpus but defined by a SUBROUTINE/FUNCTION statement somewhere in the sources is 'unparsed' (the front end dropped the unit); every other absent callee is 'external'.

### Configuration space (`configs`)

Status: **ok**

The compile-time variants the sources can take: every preprocessor directive with its condition, macro names, nesting depth, and the number of lines it guards; for each source file, whether the preprocessed text differs across the compiler/platform parse profiles (and which profiles group together); INCLUDE fragments with the units that include them and the variables they define; and the build options and semantic compiler flags (kind promotion, language standard, line length, preprocessing) that alter meaning without touching the text.

**For the port:** A Rust port needs one source of truth per variant: every #if region is a cfg feature or a runtime switch to decide, every INCLUDE fragment is a shared constant module, and every kind-promotion flag is a generic parameter (f32/f64) that the port must expose explicitly. The parse profiles cover the platform/compiler macros; the build options cover kind promotion, so the two together enumerate the variant matrix a test suite has to cover.

| Metric | Value |
| --- | ---: |
| Files with directives | 9 of 63 |
| Directive lines | 46 |
| Macros referenced | 15 |
| Config-sensitive files | 0 |
| Parse profiles | 9 |
| Build options | 2 |
| Semantic compiler flags | 11 |
| Include fragments | 1 |

Assumptions and policies:

- Directives are recognized by a line-start '#' followed by a directive name on raw source lines; a directive's guarded line count is the number of source lines up to the next branch or end of its region (nested regions included).
- Macro names are taken from #define/#undef/#ifdef/#ifndef arguments and from identifiers in #if/#elif expressions ('defined' excluded).
- Profile sensitivity hashes the preprocessed text of each Fortran file under every built-in parse profile plus the configured one; files whose preprocessing fails under a profile are listed with the error and get no letter for that profile.
- Preprocessing uses the same minimal directive emulation as the parse driver (#ifdef/#ifndef/#else/#endif/#define with token substitution); directives beyond that set are reported as preprocessing failures, not evaluated.
- INCLUDE lines are matched by a case-insensitive regex on raw source lines; the including unit is the unit whose start line precedes the INCLUDE line in the same file.
- An include fragment's 'variables defined' come from a regex over its type-declaration and DATA lines, not from a parse.
- Build options are read from meson_options.txt and semantic flags from meson.build by regex; other build systems are not inspected.
- C sources are scanned for directives only; their preprocessing is not modeled.

### Clone classes (identifier-normalized) (`clones`)

Status: **ok**

Maximal runs of executable statements that occur at two or more places after identifier normalization (every non-keyword, non-intrinsic name replaced by a placeholder numbered by first use; numbers and strings replaced by generic literals). Occurrences are grouped into classes via shared statement windows; each class lists its locations, size, a normalized sample, and the packages it spans.

**For the port:** Each clone class is one Rust function (or generic, or trait method) instead of N copies: the placeholders show the parameters it needs, the occurrence list shows the call sites, and the spanned packages show where a shared module pays off. Classes with slight divergences are also where copy-paste bugs hide: a fix applied to one copy and not the others.

| Metric | Value |
| --- | ---: |
| Clone classes | 939 |
| Occurrences | 3,023 |
| Statements covered | 21,626 of 54,477 (39.7%) |
| Largest class | 158 statements × 43 occurrences (1,166 covered) |
| Classes spanning ≥ 3 packages | 139 |
| Cross-unit classes | 584 |
| Window / minimum tokens | 6 statements / 18 |

Assumptions and policies:

- Statements are the execution-part statements of each program unit with constructs flattened, so an IF/DO/END line is one statement like any other; FORMAT statements and comments are not part of the sequence.
- Tokens come from the parser's canonical statement text; identifiers that are Fortran keywords, I/O specifier names, or standard intrinsic names stay literal, every other identifier becomes a placeholder numbered by first occurrence within the window, numbers become '#' and strings become a generic string literal.
- A seed is a window of 6 consecutive statements whose normalized text occurs at 2 or more distinct positions and has at least 18 tokens (so runs of bare END IF/CONTINUE lines are not seeds).
- A class is a maximal repeat: the occurrences of a seed whose preceding windows do not all agree, extended statement by statement while every occurrence still shares the next window; all occurrences of a class therefore have the same length, and a longer repeat shared by only some occurrences is its own (overlapping) class.
- Occurrences of one class that overlap or adjoin inside the same unit (a periodic block repeated back to back, such as pointer-switch lists) merge into one longer occurrence, so occurrence lengths differ only for such periodic classes; the class score is the total of statements its occurrences cover.
- The package of a unit is derived from its name by regex (^S?(GWF|OBS|GWT|LMT|LGR)\d*([A-Z]+?)\d -> group 2; else ^S?([A-Z]+)\d -> group 1; else the file stem without digits, upper-cased).
- Statement coverage counts a statement once even when several classes cover it.

## Dynamic and external

Ground truth from builds, runs, and other front ends that audits the static representations above.

### Coverage overlay on the control-flow graph (`coverage`)

Status: **partial**

doc/reports/coverage_2026-08-20_02h45m42/gcc-release-single/coverage-gcc-release-single.json is a summary report (per-file totals only), so the overlay stops at file level. For the block overlay produce a full line-level JSON report in the same folder: `gcovr --root <project> --object-directory <coverage build dir> --filter src/ --json <folder>/coverage.json` (or add `--json <file>` to [coverage] extra_args so `dsmodern coverage` writes it). 1 corpus file(s) have no entry in the report.

Line and branch execution counts from the newest coverage report of a test run, mapped onto every program unit and onto the blocks of its control-flow graph: covered (some line ran), uncovered (instrumented, never ran), or unknown (no instrumented line). Per unit it gives the share of blocks and lines executed, the share of branches taken, and whether the unit ran at all.

**For the port:** Blocks that never executed under the reference tests are code the port cannot validate by differential testing; they must be covered by new scenarios or ported with extra review. Units never executed rank the scenario-generation backlog, and branch counts on the graph show which decisions the tests actually exercise.

| Metric | Value |
| --- | ---: |
| Source | doc/reports/coverage_2026-08-20_02h45m42/gcc-release-single/coverage-gcc-release-single.json |
| Build variant | gcc-release-single |
| Report time | 2026-08-20T02:51:30 |
| Files | 53 of 54 corpus files (57 in report) |
| Units executed | file level only |
| Lines covered | 60.8% |
| Branches taken | 45.3% |
| Files never executed | 14 |

Assumptions and policies:

- The newest full (line-level) report wins; when only summary reports exist, the newest summary is used and the overlay stops at file level.
- Report file names are matched to sources relative to the project root (the source directory prefix is stripped); files not in the corpus are counted but not overlaid.
- A unit's line range runs from its first statement to its last event line, so trailing lines without variable events (bare RETURN, END) are not attributed to it.
- A block's line range is the span of its event lines; blocks whose lines overlap (loop headers shared by several blocks) take the union status, and a block without an instrumented line is 'unknown', not uncovered.
- Line coverage counts only lines the compiler instrumented; declarations and comments are not lines.
- Branch percentages come from the compiler's branch counters on those lines and are not the same as edges of the control-flow graph.
- A build variant is reported only when the report's file name or its sibling HTML title states it.

### Linkage ground truth (`linkage`)

Status: **ok**

For every source file, the global symbols its object file defines and references (procedures, module procedures and variables, COMMON blocks, the main program) compared with the symbols the static model predicts from the parsed source: definitions matched, predicted but absent, present but unpredicted, and cross-file references the model did or did not foresee. C objects form the C boundary: their exported symbols and which Fortran objects reference them.

**For the port:** A reference the model did not predict is a call or a global access the call graph and ownership views miss; a predicted symbol the compiler never emitted is a phantom the port would carry for nothing. The C boundary lists exactly the functions the Rust port must expose or replace with an FFI shim.

| Metric | Value |
| --- | ---: |
| Objects | 58 (54 Fortran, 4 C) |
| Files matched | 54 of 54 Fortran objects agree fully |
| Definition agreement | 100.0% (2,099 matched, 0 missing, 0 extra) |
| Reference agreement | 100.0% (2,106 matched, 0 over-predicted) |
| Unpredicted references | 0 |
| C boundary symbols | 99 (6 referenced from Fortran) |
| Sources without an object | 0 |

Assumptions and policies:

- Objects come from one unoptimized single-precision build, so no procedure is inlined away and every module variable keeps its symbol.
- The object-to-source rule is the build system's: the per-target '<name>.p' directory is dropped and the object name minus '.o' is the source path relative to that directory (flattened '_' separators are tried only when the plain name does not exist).
- Name mangling follows gfortran: external procedures and COMMON blocks get a lower-case name plus a trailing underscore, module entities '__<module>_MOD_<name>', the main program 'main' and 'MAIN__', and a BIND(C) interface its binding label.
- Module variables are the entity declarations of a module's own specification part minus PARAMETER names (PRIVATE variables are still emitted); internal procedures and private module procedures are local symbols and are not predicted.
- Predicted references are the call sites, procedure actual arguments, module-variable events, and specification-expression names of the file's lowered units whose target is defined in another file and is reachable through the unit's (or its host module's) USE chain, with USE renames resolved; units the lowering skipped contribute no references, and a module variable touched only by an inquiry intrinsic is not an event.
- Standard intrinsic procedures and the common compiler extensions (ISNAN, SECNDS, C_LOC, ...) are never predicted as external references.
- Compiler-generated derived-type helpers ('__copy_', '__vtab_', '__def_init_', '__final_', '__deallocate_') are listed separately and do not count against agreement.
- Runtime and C-library references (names starting with '_' other than module symbols, and the common libc/libm names) are dropped before comparing references.

### External IR readiness (`irs`)

Status: **partial**

flang, psyclone not available; their columns read 'unavailable'.

A per-file matrix of what the external front ends accept: whether a semantic ASR can be built (with legacy dialect switches: implicit typing, implicit interfaces, argument casting), whether LLVM IR can be emitted from it, whether a second compiler front end parses the file, and whether the PSyIR tool chain is importable. Failures carry the first diagnostic so the blocking construct is named.

**For the port:** Files with an ASR are candidates for mechanical translation and for semantic diffing against the Rust port; LLVM IR gives a reference lowering for numeric semantics. Files the front ends reject list the dialect features the port must handle by hand (or the upstream fixes worth contributing first).

| Metric | Value |
| --- | ---: |
| lfortran | available (0.64.0) |
| flang | not found |
| psyclone | not found |
| Files | 54 |
| ASR ok | 48 of 54 |
| LLVM IR ok | 37 of 54 |
| Second front end ok | n/a |
| Total time | 9.0 s |

Assumptions and policies:

- Files are processed in module-dependency order (from MODULE/USE lines) so the module files a file needs exist before it is tried; a dependency that failed leaves its dependents failing on the missing module file, which is recorded as such.
- Fixed-form files get the fixed-form switch and files whose extension requests preprocessing get the preprocessor; the source root is the only include path and no macros are predefined.
- Each invocation has a 120 s limit; a timeout counts as neither success nor a syntax failure.
- 'LLVM ok' means the IR printer finished without error; it does not mean the IR was assembled or linked.
- The second front end is only asked for a syntax check; PSyclone is probed for importability only (PSyIR construction is a follow-up).
- Style suggestions are not errors; the first diagnostic line (colour codes stripped, its detail line appended when the message ends with a colon) is the recorded error.

## Interactive views

The per-unit graphs, tables, and slices live in the HTML report (`code-representations-report.html`); this file carries the headline figures only.
