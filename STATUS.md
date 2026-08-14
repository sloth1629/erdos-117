# Status

Updated: 2026-08-14

## Current outcome

`[UNVERIFIED]` Erdős Problem 117 is not completely resolved here. The exact
function \(h(n)\) is known in this repository for \(1\le n\le7\), but the
general function and optimal exponential rate are not determined.

The exact cutoff-seven audit now matches the earlier lower witness.  The
order-\(3^5\) group \(S(3,2)\) satisfies

\[
\nu(S(3,2))=7,\qquad a(S(3,2))=10,
\]

and the complete upper proof gives

\[
h(7)=10.
\]

This also decisively refutes the proposed binary-symplectic formula, which
gives 9 at seven.

## Proved advances

1. Exact graph/group dictionary and central-coset compression.
2. A self-contained arbitrary-to-finite model preserving the full compressed
   commutation graph, \(\nu\), and \(a\); finite attainment of \(h(n)\).
3. Universal two-step centralizer drop and recurrence
   \(h(n)\le n h(n-2)\).
4. Self-contained conjugacy-class bound \(4n^2\) and
   \([G:Z(G)]\le(4n^2)^n\).
5. Exact values \(h(1)=h(2)=1\), \(h(n)=n\) for \(3\le n\le6\), and
   \(h(7)=10\).  The values at five through seven are computer-assisted.
   At seven, the primary-verified theorem \(f(7)=81\) reduces the problem to
   738 center quotients; structural and exact exterior-square certificates
   exhaust every one.
6. Exact scalar symplectic cover formula
   \(a(S(q,m))=q^m+1\), binary lower construction, and the
   \(S(3,2)\) counterexample.
7. Direct-product OR identity and correct direct-power rates via fractional
   chromatic number and complementary Shannon capacity.

## Computation status

- The complete verification suite passes: 25 tests in 211.839 seconds under
  Python 3.9.6, with the transcript saved for this milestone.
- Both optimized graph algorithms agree with brute force on all 33,868
  labeled graphs with at most six vertices.
- All SmallGroups of orders 8, 32, and 64 were exported by GAP 4.16.0 /
  SmallGrp 1.5.4 and independently reverified in Python.
- All 2,328 SmallGroups of order 128 were prefiltered rigorously; exact
  certificates for all 418 groups not already excluded by a 7-clique give
  no \(a>\nu\) at \(\nu\le6\).
- The \(h(5)\) enumeration covers all 42 possible center quotients of order
  at most 16 and all 2,986 action-invariant exterior-square kernels; every
  one of the 364 cases with clique number at most five is five-colorable.
- The \(h(6)\) enumeration covers all 162 quotient types of order at most 36.
  For 161 types it checks all 23,527 action-invariant exterior-square kernels;
  a structural lemma and a redundant 174,251-pencil census handle
  \(C_2^5\).  All 314 faithful candidates not already excluded by a
  seven-clique are six-colorable.
- The \(h(7)\) proof inventories all 738 quotient types of order at most 81.
  Ordinary bounded batches scan 660 types and 55,970 normal kernels.  The
  remaining cases are partitioned into two delegated elementary-abelian
  quotients, 62 explicit nonidentity zero exterior rows, eleven complete
  character-dual searches, and three special order-64 certificates.  The
  only eligible \(C_3^4\) orbit has \((\nu,a)=(7,10)\); no other case exceeds
  ten at clique cutoff seven.
- The reconstructed finite edge of the \(f(6)=36\) proof independently
  rebuilds 5,257 subgroups in 48 group types and tests 5,545,351 six-subsets
  of maximal subgroups.  It corrects the published false positive
  \(S_3\times S_3\) and verifies the true order-36 witness
  `SmallGroup(36,13)`.
- Symmetry-reduced exact searches give
  \((\nu(S(5,2)),a(S(5,2)))=(18,26)\) and
  \((\nu(S(3,3)),a(S(3,3)))=(13,28)\).
- The \(S(3,2)\) record has separate clique, coloring, projective-exclusion,
  symplectic-spread, and abelian-subgroup-cover certificates.

## Source status

- Neumann (1976) and Faber–Laver–McKenzie (1978) were primary-verified.
- Bryce–Fedri–Serena (1997), including the proof that \(f(5)=16\), was
  primary-verified from the complete official PDF.
- Abdollahi–Jafarian Amiri (2007), Theorem B on p. 292 with proof on
  pp. 299--300, was primary-verified and supplies the load-bearing
  seven-cover bound \(f(7)=81\).
- The primary statement \(f(6)=36\), Alencar's full proof reconstruction,
  and every finite classification leaf used in that reconstruction were
  audited; the finite leaves have modern GAP exports and an independent
  multiplication-table verifier.
- The finite-geometry literature was audited at theorem level: the
  scalar-symplectic clique parameter is the maximum partial-ovoid size in
  \(W(2m-1,q)\), and the exact values for \(q=3,5,7\) in rank two agree with
  the repository computations where independently completed.
- Pyber's official abstract verifies a finite-group fixed-base exponential
  center-index bound, but the full paper, exact constants, and proof were not
  accessible; no repository proof depends on them.
- The current online OPEN status was visible only through an indexed
  snapshot because the direct page returned HTTP 403; it remains an
  explicitly bounded status check, not a mathematical premise.

## Remaining decisive obligations

1. Determine or sharply bound the partial-ovoid parameter
   \(\pi(q,m)=\nu(S(q,m))\) across finite fields.
2. Decide whether higher-codomain class-two maps or nonnilpotent groups beat
   the binary asymptotic lower efficiency.
3. Prove an upper bound near \(2^{n/2}\), or produce a construction showing
   a larger exponential constant.
4. Establish existence and value of an asymptotic exponential rate, or
   formulate the correct limsup/liminf answer.
5. Determine \(h(8)\) and the next exact values.
6. Acquire and audit Pyber's full primary proof for historical completeness.

## Environment

- Git and Python 3: available.
- GAP 4.16.0 / SmallGrp 1.5.4: built under ignored `work/` for the census;
  not required to verify committed certificates.
- TeX (`pdflatex`, `latexmk`, `tectonic`): unavailable at final audit; no PDF
  build is claimed.
