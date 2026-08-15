# Erdős Problem 117

This private repository is a proof-audited research attempt on Erdős
Problem 117. For a group \(G\), let \(\nu(G)\) be the maximum size of a
pairwise noncommuting subset and let \(a(G)\) be the minimum number of
abelian subgroups covering \(G\). The extremal function is

\[
h(n)=\sup\{a(G):\nu(G)\le n\}.
\]

## Outcome of this research pass

No complete resolution is claimed. The strongest repository results are:

- [PROVED] Every arbitrary group with finite \(\nu\) has an exact finite
  commutation model preserving both \(\nu\) and \(a\); consequently \(h(n)\)
  is finite and attained by a finite group.
- [PROVED] For noncentral \(x\),
  \(\nu(C_G(x))\le\nu(G)-2\), hence
  \(h(n)\le n h(n-2)\).
- [PROVED] The irredundant maximum-clique centralizer cover and a
  self-contained factorial coset lemma give
  \([G:Z(G)]\le\nu(G)!\) for arbitrary groups.  In particular, every
  cutoff-eight center quotient has order at most \(8!=40{,}320\).
- [PROVED] A separate cutoff-eight subgroup-cover argument gives
  \(144\le f(8)\le25{,}920\), and therefore sharpens the universal
  cutoff-eight center-index bound to \([G:Z(G)]\le25{,}920\).  In the
  central-minimal-normal \(C_2\) branch the exact bound is \(144\), attained
  by an explicit independently verified cover.  The exact value of \(f(8)\)
  remains open.
- [PROVED] Combining the audited Guralnick--Maróti BFC theorem with the
  published Nagy--Pach--Tomon abelian coset-cover theorem gives the
  CFSG-dependent universal bounds
  \([G:Z(G)]\le2^{O(\nu(G)\log\log\nu(G))}\) and
  \(h(n)\le2^{O(n\log\log n)}\).  This uses neither the withdrawn
  arXiv:2205.03389 claim nor Pyber's unaudited fixed-base proof.
- [PROVED] By a computer-assisted proof, \(h(n)=n\) for \(3\le n\le6\), while
  \(h(1)=h(2)=1\).  The values at five and six combine audited
  irredundant-cover bounds \(f(5)=16\), \(f(6)=36\) with complete
  Schur-cover/exterior-square enumerations.
- [PROVED] By a computer-assisted proof, \(h(7)=10\).  The verified
  seven-cover theorem \(f(7)=81\) reduces the upper bound to 738 finite
  center quotients; bounded kernel batches, explicit exterior-zero
  witnesses, character-annihilator searches, and three special order-64
  certificates exhaust them.  The matching lower witness is \(S(3,2)\).
- [PROVED] Scalar symplectic groups satisfy
  \(a(S(q,m))=q^m+1\), with clique number equal to a partial-ovoid
  parameter.  A Frobenius-twisted tensor construction proves
  \(\pi(q,2^{t-1})\ge q^t+1\) for odd \(t\).  Consequently all nonbinary
  scalar models are jointly subexponential in their clique cutoff, while the
  full scalar-symplectic envelope has exact exponential base \(\sqrt2\),
  supplied only by the binary field.
- [DISPROVED] The proposed exact formula
  \(h(n)=\max\{n,2^{\lfloor(n-1)/2\rfloor}+1\}\) is false:
  \(S(3,2)\) has \((\nu,a)=(7,10)\), while the formula gives 9.
- [PROVED] Binary symplectic groups give
  \(h(2m+1)\ge2^m+1\) and
  \(\liminf h(n)^{1/n}\ge\sqrt2\).  The scalar theorem shows that beating
  this base requires a higher-codomain, non-field-linear, higher-class, or
  nonnilpotent mechanism.
- [PROVED] Two cutoff-eight structural obstructions are now explicit.  If
  \(Q=G/Z(G)\) is nonabelian and \(\nu(G)\le8\), then
  \(|Z(Q)|\le3{,}600\).  More precisely, the binary elementary layer of
  \(Z(Q)\) has rank at most two: a self-contained reduction sends a
  hypothetical rank-three case to 39 order-64 quotient types, and complete
  exact-extension certificates eliminate all 39.  If \(P\) is a finite class-two \(p\)-group
  and \(A\ge Z(P)\) is abelian, then
  \([A:Z(P)]\le p^{\nu(P)/p}\); a relative version charges the exponent to
  \(\nu(P)-\nu(H)\) for \(A=Z(H)\).
- [PROVED] A weighted spectral-shift theorem now controls the visible
  elementary part of a class-two local centralizer index without assuming an
  exponent-\(p\) group or an abelian centralizer.  In the faithful binary
  slice it proves the quadratic local-drop bound for commutator-image order at
  most 32, and for order 64 when the centralizer clique number is at most 40.
  Full quadratic local drop remains unproved.
- [PROVED] The finite \(5\)-group branch at cutoff eight is closed.  A
  certified small-\(\mathbf F _5\) hyperplane theorem, combined with
  Berkovich's verified maximal-member bound, proves that
  \(\nu(P)\le8\) forces \((\nu(P),a(P))=(1,1)\) or \((6,6)\).  This removes
  the finite \(5\)-group branch in the exhaustive proof of \(h(8)=10\).
- [PROVED] The finite \(3\)-group branch at cutoff eight is closed:
  \(\nu(P)=8\) forces \(a(P)=8\), and
  \[
    \max\{a(P):P\text{ a finite \(3\)-group},\ \nu(P)\le8\}=10,
  \]
  with equality supplied by \(S(3,2)\).
- [PROVED] (computer-assisted) No finite \(2\)-group has clique number
  eight.  Inclusion-maximal proper element-centralizers first sharpen the
  center quotient to order at most \(128\); the exact cutoff-eight
  certificate removes all smaller powers of two.  At order \(128\), an
  index-two subgroup is forced to have the scalar symplectic
  \(C_2^6\) graph.  The four ranks of the induced symplectic involution
  each give a nine-clique or a forbidden maximal element-centralizer.
- [PROVED] The solvable nonnilpotent branch has an exact common-core
  reduction.  After maximalizing the exact eight-member cover and taking a
  minimal irredundant subcover, let \(R\) be the core of the maximal-member
  intersection.  If \(R=1\), the
  center quotient is one of eight groups of order at most \(42\), and the
  certified bounded scan gives \(a(G)\le10\).  For \(R\ne1\), the quotient
  by \(R\) is abelian or has form \(C\times H\), where \(C\) is central and
  is a direct product of elementary abelian \(2\)-, \(3\)-, \(5\)-, and
  \(7\)-components, and \(H\) is one of seven explicit affine groups.
- [PROVED] The common-core residual has a canonical Frattini form.  A
  hypothetical counterexample has
  \(1\ne\Phi(Q)=\Phi(S)\), where \(S\) is a finite \(2\)-group, and
  \[
    Q\cong C_3\rtimes_\chi S,\qquad \chi:S\twoheadrightarrow C_2,
    \qquad |S|\le8192.
  \]
  Every abelian minimal-maximalization quotient is exactly
  \(C_2^2,C_2^4\), or \(C_2^6\); no commutator pairing is descended through
  the Frattini or common-core quotient.
- [PROVED] The canonical semidirect branch is closed without descending a
  commutator pairing.  After deleting central direct factors, the finite
  exact model is \(C_3\rtimes_\chi U\), where \(U\) is a finite \(2\)-group.
  For \(K=\ker\chi\) and the odd coset \(\Omega=U\setminus K\),
  \[
    \nu(C_3\rtimes_\chi U)=\nu(K)+3\omega(\Omega).
  \]
  At clique cutoff eight this forces \((\nu(K),\omega(\Omega))=(5,1)\);
  five abelian subgroups cover the even fibers and three abelian subgroups
  cover the odd fibers.  Thus the putative residual has \(a=8\), not
  \(a>10\).
- [PROVED] These are exhaustive at cutoff eight.  The exact finite model is
  solvable by the verified, finite-simple-group-classification-dependent
  finite nonsoluble classification.  If its center
  quotient is nilpotent, a Sylow direct-product argument reduces it without
  loss to one finite \(p\)-group; the odd-prime results and the binary
  closure eliminate the nilpotent alternative completely, while the
  preceding semidirect calculation eliminates the nonnilpotent alternative.
- [PROVED] Consequently, by a computer-assisted proof for arbitrary groups,
  \[
    h(8)=10.
  \]
  The upper bound is the exhaustive reduction above, and the lower bound is
  already supplied by \(S(3,2)\), which has \((\nu,a)=(7,10)\).
- [COMPUTED] Exact, independently verified certificates cover explicit
  families, every SmallGroup of orders 8, 32, and 64, all order-128 groups
  surviving a rigorous \(\nu\le6\) prefilter, all 2,986 exterior-square
  cases used for \(h(5)\), and all 23,527 normal-kernel records used for
  \(h(6)\).  Further exact records are
  \((\nu,a)=(18,26)\) for \(S(5,2)\) and \((13,28)\) for \(S(3,3)\).
  At cutoff seven they additionally cover all 738 possible center quotients
  of order at most 81, including 55,970 ordinary normal-kernel records and
  eleven complete character-dual searches.
- [PROVED] The integrated asymptotic pass reduces the candidate
  \(\sqrt2\)-base upper bound to a prime-uniform p-group interface.  It
  proves active binary codomain dimension \(O((\log\nu)^2)\), the half-rate
  on regular commuting/triangular operator pencils and several critical
  p-group ranges, asymptotically lossless fractional rounding, and
  conditional nilpotent-to-global transfer.  The p-group antecedent and the
  rate amplifier remain [UNVERIFIED]; no complete solution is claimed.
- [COMPUTED] A new dependency-free dynamic-centralizer bundle checks exact
  order-32 and order-64 LP models, the binary chain-ring Heisenberg family,
  and all 28,672 natural one-pair extensions.  It supports an exact entropy
  telescope and refutes two naive nodewise inductions without refuting the
  global half-rate target.

The integrated Pro-pass asymptotic frontier is in
[`notes/asymptotic_reductions_integrated.md`](notes/asymptotic_reductions_integrated.md),
with its evidence ledger in
[`audit/pro_asymptotic_integration_audit.md`](audit/pro_asymptotic_integration_audit.md).
The publication-style synthesis is in
[`proof/main.tex`](proof/main.tex), and the concise state of the problem is
in [`STATUS.md`](STATUS.md).

## Repository map

- `literature/`: primary-source review, bibliography, claim ledger, and
  citation graph.
- `notes/`: definitions, complete structural proofs, constructions, product
  analysis, refutations, and open obligations.
- `src/`: dependency-free Python computation and independent verification.
- `experiments/`: deterministic configurations, exact witnesses, raw GAP
  exports, and saved logs.
- `results/`: exact records, proved family formulas, and conjectures.
- `proof/`: manuscript, bibliography, dependency graph, and computational
  appendix.
- `audit/`: source, proof, computation, and release audits.

See [`AGENTS.md`](AGENTS.md) for evidence labels and proof discipline.

## Reproduce the exact verification

Python 3.9 or later is sufficient to verify the committed certificates:

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 -m unittest discover -s src/verification -p 'test_*.py' -v
```

The saved integrated run passed all 43 tests in 690.066 seconds under Python
3.9.6.

The canonical experiment commands are documented in
[`src/python/README.md`](src/python/README.md). GAP is needed only to
regenerate the SmallGroups and exterior-square exports; the committed
exports and all Python certificate checks are self-contained.  The proofs of
\(h(5)=5\), \(h(6)=6\), \(h(7)=10\), and \(h(8)=10\) are explicitly
computer-assisted: their exhaustiveness also relies
on GAP's SmallGroups, Schur-cover, and subgroup-enumeration algorithms.

To build the manuscript when a TeX distribution is available:

```bash
cd proof
latexmk -pdf main.tex
```

TeX was unavailable in the final research environment, so the source was
syntax-audited but no PDF build is claimed.
