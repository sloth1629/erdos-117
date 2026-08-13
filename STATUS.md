# Status

Updated: 2026-08-13

## Current outcome

`[UNVERIFIED]` Erdős Problem 117 is not completely resolved here. The exact
function \(h(n)\) is known in this repository only for \(1\le n\le6\), and
the optimal exponential rate is not determined.

The research pass did decisively refute the proposed binary-symplectic
formula. The order-\(3^5\) group \(S(3,2)\) satisfies

\[
\nu(S(3,2))=7,\qquad a(S(3,2))=10,
\]

so \(h(7)\ge10\), whereas the proposal gives 9.

## Proved advances

1. Exact graph/group dictionary and central-coset compression.
2. A self-contained arbitrary-to-finite model preserving the full compressed
   commutation graph, \(\nu\), and \(a\); finite attainment of \(h(n)\).
3. Universal two-step centralizer drop and recurrence
   \(h(n)\le n h(n-2)\).
4. Self-contained conjugacy-class bound \(4n^2\) and
   \([G:Z(G)]\le(4n^2)^n\).
5. Exact values \(h(1)=h(2)=1\) and \(h(n)=n\) for \(3\le n\le6\).
   The values at five and six are computer-assisted.  They use audited
   irredundant-cover bounds \(f(5)=16\), \(f(6)=36\), followed by exhaustive
   exterior-square computations over all possible finite center quotients.
6. Exact scalar symplectic cover formula
   \(a(S(q,m))=q^m+1\), binary lower construction, and the
   \(S(3,2)\) counterexample.
7. Direct-product OR identity and correct direct-power rates via fractional
   chromatic number and complementary Shannon capacity.

## Computation status

- The complete verification suite passes; its saved output records the exact
  test count and runtime for this milestone.
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
5. Determine \(h(7)\) and the next exact values; the current lower bound is
   \(h(7)\ge10\).
6. Acquire and audit Pyber's full primary proof for historical completeness.

## Environment

- Git and Python 3: available.
- GAP 4.16.0 / SmallGrp 1.5.4: built under ignored `work/` for the census;
  not required to verify committed certificates.
- TeX (`pdflatex`, `latexmk`, `tectonic`): unavailable at final audit; no PDF
  build is claimed.
