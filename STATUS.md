# Status

Updated: 2026-08-14

## Current outcome

`[UNVERIFIED]` Erdős Problem 117 is not completely resolved here. The exact
function \(h(n)\) is known in this repository for \(1\le n\le8\), but the
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

The independently audited cutoff-eight closure now gives

\[
h(8)=10.
\]

The lower bound is again supplied by \(S(3,2)\).  For the upper bound, the
exact finite model is reduced exhaustively to nilpotent and solvable
nonnilpotent cases; the finite prime-power branches are closed, and the last
semidirect Frattini branch has an exact \(5+3\) abelian cover.

## Proved advances

1. Exact graph/group dictionary and central-coset compression.
2. A self-contained arbitrary-to-finite model preserving the full compressed
   commutation graph, \(\nu\), and \(a\); finite attainment of \(h(n)\).
3. Universal two-step centralizer drop and recurrence
   \(h(n)\le n h(n-2)\).
4. A self-contained factorial cover argument gives
   \([G:Z(G)]\le n!\), hence the explicit cutoff-eight reduction
   \(|G/Z(G)|\le8!=40{,}320\).  A separately audited eight-cover argument
   proves \(144\le f(8)\le25{,}920\), sharpening this cutoff alone to
   \(|G/Z(G)|\le25{,}920\); its central minimal-normal \(C_2\) branch has
   the sharp index bound \(144\).  Independently, every conjugacy class has
   size at most \(4n^2\), the BFC input used below.
5. A stronger CFSG-dependent universal bound
   \([G:Z(G)]\le2^{O(\nu(G)\log\log\nu(G))}\), hence
   \(h(n)\le2^{O(n\log\log n)}\), obtained from the audited
   Guralnick--Maróti derived-subgroup theorem and the published
   Nagy--Pach--Tomon abelian coset-cover theorem.  The withdrawn
   fixed-base preprint is not used.
6. Exact values \(h(1)=h(2)=1\), \(h(n)=n\) for \(3\le n\le6\), and
   \(h(7)=h(8)=10\).  The values at five through eight are
   computer-assisted.
   At seven, the primary-verified theorem \(f(7)=81\) reduces the problem to
   738 center quotients; structural and exact exterior-square certificates
   exhaust every one.
7. Exact scalar symplectic cover formula
   \(a(S(q,m))=q^m+1\), binary lower construction, and the
   \(S(3,2)\) counterexample.  A self-contained Frobenius-twisted tensor
   construction proves
   \(\pi(q,2^{t-1})\ge q^t+1\) for every prime power \(q\) and odd \(t\).
   It follows that all nonbinary scalar models are jointly subexponential
   in their clique cutoff and that the full scalar-symplectic envelope has
   exact exponential base \(\sqrt2\).  This is a constructional barrier,
   not a universal upper bound for arbitrary groups.
8. Direct-product OR identity and correct direct-power rates via fractional
   chromatic number and complementary Shannon capacity.
9. At cutoff eight, every nonabelian exact center quotient satisfies
   \(|Z(G/Z(G))|\le3{,}600\); the binary elementary central layer has rank
   at most two.  The intermediate structural branch at rank three reduces
   to 39 order-64 quotient types, all of which are eliminated by complete
   exact-extension certificates.  For finite class-two \(p\)-groups,
   every abelian \(A\ge Z(P)\) satisfies
   \([A:Z(P)]\le p^{\nu(P)/p}\), with a drop-sensitive relative-center
   form.  A separate weighted spectral-shift theorem controls elementary
   commutator images even when the centralizer is nonabelian and the group
   has arbitrary exponent.  In the faithful binary slice it proves
   quadratic local drop for \(|[x,P]|\le32\), and for \(|[x,P]|=64\) when
   \(\nu(C_P(x))\le40\).  The full quadratic inequality and invisible
   higher-exponent layers remain open.  These are structural inputs, not a
   fixed-base global upper bound.
10. The finite \(5\)-group branch at cutoff eight is completely eliminated:
    a computer-assisted small-\(\mathbf F _5\) hyperplane lemma and
    Berkovich's verified Proposition 4.5 prove that
    \(\nu(P)\le8\) implies
    \((\nu(P),a(P))\in\{(1,1),(6,6)\}\).  The independent low-dimensional
    certificate checks 16, 122,438, and 10,626 normalized subfamilies in
    dimensions two, three, and four.
11. [PROVED] The finite \(3\)-group branch at cutoff eight is closed.
    A maximal-centralizer amplification argument, Berkovich's verified
    small-\(3\)-group structure, a scalar-symplectic obstruction, and the
    private cells of an irredundant centralizer cover prove
    \(\nu(P)=8\Rightarrow a(P)=8\).  Consequently the maximum of \(a(P)\)
    over finite \(3\)-groups with \(\nu(P)\le8\) is ten, attained by
    \(S(3,2)\).
12. [PROVED] (computer-assisted) No finite \(2\)-group has \(\nu(P)=8\).
    Inclusion-maximal element-centralizers give \([P:Z(P)]\le128\), and the
    exact bounded certificate forces equality in any hypothetical case.
    The resulting index-two scalar-symplectic \(C_2^6\) subgroup reduces
    conjugation to a symplectic involution; all four possible ranks yield a
    nine-clique or a maximal-centralizer contradiction.  Both reductions
    received fixed-hash independent reconstruction.
13. [PROVED] The nonnilpotent solvable branch first reduces to a nontrivial
    common core.  For a minimal maximalization of the exact eight-centralizer
    cover, let \(R\) be the core of the maximal-member intersection.  The
    core-free case \(R=1\) leaves eight center quotients of order at most
    \(42\), all closed by the exact cutoff-eight certificate with
    \(a(G)\le10\).  In general, \(Q/R\) is abelian or has form
    \(C\times H\), where \(C\) is central and is a direct product of
    elementary abelian \(2\)-, \(3\)-, \(5\)-, and \(7\)-components, and
    \(H\) is one of seven explicit affine groups.  The residual is further
    forced into the canonical form
    \(Q=C_3\rtimes_\chi S\), where \(S\) is a finite \(2\)-group,
    \(\chi\) is onto \(C_2\), \(1\ne\Phi(Q)=\Phi(S)\), and
    \(|S|\le8192\).  Its abelian common-core quotients are only
    \(C_2^2,C_2^4,C_2^6\).  A final coprime-action decomposition removes
    central direct factors and writes the exact model as
    \(C_3\rtimes_\chi U\).  If \(K=\ker\chi\) and \(\Omega=U\setminus K\),
    then \(\nu=\nu(K)+3\omega(\Omega)\).  At cutoff eight the only
    possibility is \((\nu(K),\omega(\Omega))=(5,1)\), and a five-subgroup
    cover of \(K\) together with three internally commuting fixed-coordinate
    odd layers gives an eight-subgroup abelian cover.
14. [PROVED] The residual in item 13 is exhaustive for arbitrary
    groups at cutoff eight.  The exact finite model is solvable by the
    primary-verified, finite-simple-group-classification-dependent
    nonsoluble classification.  A nilpotent center
    quotient makes the finite model nilpotent; two nonabelian Sylow factors
    would give a \(3\times3\) nine-clique, so central abelian factors may be
    discarded.  The finite \(3\)-, \(5\)-, and \(7\)-group theorems and the
    binary closure eliminate every nilpotent alternative.  The
    nonnilpotent alternative is exactly item 13 and is closed there.
15. [PROVED] Combining items 12--14 with the exact finite model proves, for
    arbitrary groups,
    \[
      h(8)=10.
    \]
    The proof is computer-assisted only through the already audited bounded
    exact-extension certificates; the final coprime and semidirect argument
    is structural.  Two independent reconstructions found no blocker.

## Computation status

- The complete verification suite passes: 34 tests in 517.555 seconds under
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
- Guralnick--Maróti (2011), Theorem 1.8, and Nagy--Pach--Tomon (2026),
  Theorem 1.11 with its Section 8 proof, were read and audited.  Their
  combination supplies the repository's CFSG-dependent
  \(2^{O(n\log\log n)}\) upper bound.  The distinct arXiv:2205.03389
  fixed-base claim is withdrawn and is not used.
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
5. Determine \(h(9)\) and the subsequent exact values; the repository now
   determines every value through cutoff eight.
6. Acquire and audit Pyber's full primary proof for historical completeness.

## Environment

- Git and Python 3: available.
- GAP 4.16.0 / SmallGrp 1.5.4: built under ignored `work/` for the census;
  not required to verify committed certificates.
- TeX (`pdflatex`, `latexmk`, `tectonic`): unavailable at final audit; no PDF
  build is claimed.
