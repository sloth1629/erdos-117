# Status

Updated: 2026-08-13

## Current outcome

`[UNVERIFIED]` Erdős Problem 117 is not completely resolved here. The exact
function \(h(n)\) is known in this repository only for \(1\le n\le4\), and
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
5. Exact values \(h(1)=h(2)=1\), \(h(3)=3\), \(h(4)=4\).
6. Exact scalar symplectic cover formula
   \(a(S(q,m))=q^m+1\), binary lower construction, and the
   \(S(3,2)\) counterexample.
7. Direct-product OR identity and correct direct-power rates via fractional
   chromatic number and complementary Shannon capacity.

## Computation status

- 11/11 verification tests pass.
- Both optimized graph algorithms agree with brute force on all 33,868
  labeled graphs with at most six vertices.
- All SmallGroups of orders 8, 32, and 64 were exported by GAP 4.16.0 /
  SmallGrp 1.5.4 and independently reverified in Python.
- The \(S(3,2)\) record has separate clique, coloring, projective-exclusion,
  symplectic-spread, and abelian-subgroup-cover certificates.

## Source status

- Neumann (1976) and Faber–Laver–McKenzie (1978) were primary-verified.
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
5. Acquire and audit Pyber's full primary proof for historical completeness.

## Environment

- Git and Python 3: available.
- GAP 4.16.0 / SmallGrp 1.5.4: built under ignored `work/` for the census;
  not required to verify committed certificates.
- TeX (`pdflatex`, `latexmk`, `tectonic`): unavailable at final audit; no PDF
  build is claimed.
