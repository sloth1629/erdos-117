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
  parameter.
- [DISPROVED] The proposed exact formula
  \(h(n)=\max\{n,2^{\lfloor(n-1)/2\rfloor}+1\}\) is false:
  \(S(3,2)\) has \((\nu,a)=(7,10)\), while the formula gives 9.
- [PROVED] Binary symplectic groups give
  \(h(2m+1)\ge2^m+1\) and
  \(\liminf h(n)^{1/n}\ge\sqrt2\).
- [PROVED] Two cutoff-eight structural obstructions are now explicit.  If
  \(Q=G/Z(G)\) is nonabelian and \(\nu(G)\le8\), then
  \(|Z(Q)|\le3{,}600\).  More precisely, the binary elementary layer of
  \(Z(Q)\) has rank at most two: a self-contained reduction sends a
  hypothetical rank-three case to 39 order-64 quotient types, and complete
  exact-extension certificates eliminate all 39.  If \(P\) is a finite class-two \(p\)-group
  and \(A\ge Z(P)\) is abelian, then
  \([A:Z(P)]\le p^{\nu(P)/p}\); a relative version charges the exponent to
  \(\nu(P)-\nu(H)\) for \(A=Z(H)\).
- [PROVED] The finite \(5\)-group branch at cutoff eight is closed.  A
  certified small-\(\mathbf F _5\) hyperplane theorem, combined with
  Berkovich's verified maximal-member bound, proves that
  \(\nu(P)\le8\) forces \((\nu(P),a(P))=(1,1)\) or \((6,6)\).  This removes
  finite \(5\)-groups from the unresolved \(h(8)\) cases.
- [PROVED] The finite \(3\)-group branch at cutoff eight is closed:
  \(\nu(P)=8\) forces \(a(P)=8\), and
  \[
    \max\{a(P):P\text{ a finite \(3\)-group},\ \nu(P)\le8\}=10,
  \]
  with equality supplied by \(S(3,2)\).
- [PROVED] The finite \(2\)-group branch has been reduced substantially.
  If \(P\) is a finite \(2\)-group with \(\nu(P)=8\), then
  \([P:Z(P)]\le2^{11}=2048\).  Moreover, maximalizing its eight
  clique-centralizers in \(P/\Phi(P)\) produces a minimal hyperplane
  subcover whose normals form an odd circuit of size \(3\), \(5\), or \(7\);
  in particular, the original centralizers cannot all be maximal.
- [PROVED] By a computer-assisted argument, the maximal-member subbranch is
  closed: if even one centralizer
  belonging to a maximum eight-clique is maximal, then
  \([P:Z(P)]\le64\) and \(a(P)\le10\).  Thus any finite \(2\)-group
  \(P\) with \(\nu(P)=8\) and \(a(P)>10\) must have every such centralizer
  nonmaximal.
- [PROVED] The solvable nonnilpotent branch has an exact common-core
  reduction.  After maximalizing the exact eight-member cover and taking a
  minimal irredundant subcover, let \(R\) be the core of the maximal-member
  intersection.  If \(R=1\), the
  center quotient is one of eight groups of order at most \(42\), and the
  certified bounded scan gives \(a(G)\le10\).  For \(R\ne1\), the quotient
  by \(R\) is abelian or has form \(C\times H\), where \(C\) is central and
  is a direct product of elementary abelian \(2\)-, \(3\)-, \(5\)-, and
  \(7\)-components, and \(H\) is one of seven explicit affine groups.
- [PROVED] These are exhaustive at cutoff eight.  The exact finite model is
  solvable by the verified, finite-simple-group-classification-dependent
  finite nonsoluble classification.  If its center
  quotient is nilpotent, a Sylow direct-product argument reduces it without
  loss to one finite \(p\)-group, and the closed \(3\)-, \(5\)-, and
  \(7\)-branches leave only \(p=2\).  If the quotient is nonnilpotent, the
  common-core proposition applies.  In the binary residual, every minimal
  maximalization also has nontrivial intersection; otherwise its quotient
  has order at most \(64\) and the bounded certificate closes it.
- [UNVERIFIED] Eliminating the all-nonmaximal binary common core or the
  nonnilpotent solvable common core remains open, so \(h(8)\) is not
  determined.
- [COMPUTED] Exact, independently verified certificates cover explicit
  families, every SmallGroup of orders 8, 32, and 64, all order-128 groups
  surviving a rigorous \(\nu\le6\) prefilter, all 2,986 exterior-square
  cases used for \(h(5)\), and all 23,527 normal-kernel records used for
  \(h(6)\).  Further exact records are
  \((\nu,a)=(18,26)\) for \(S(5,2)\) and \((13,28)\) for \(S(3,3)\).
  At cutoff seven they additionally cover all 738 possible center quotients
  of order at most 81, including 55,970 ordinary normal-kernel records and
  eleven complete character-dual searches.

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

The saved final run passed all 34 tests in 683.411 seconds under Python
3.9.6.

The canonical experiment commands are documented in
[`src/python/README.md`](src/python/README.md). GAP is needed only to
regenerate the SmallGroups and exterior-square exports; the committed
exports and all Python certificate checks are self-contained.  The proofs of
\(h(5)=5\), \(h(6)=6\), and \(h(7)=10\) are explicitly computer-assisted:
their exhaustiveness also relies
on GAP's SmallGroups, Schur-cover, and subgroup-enumeration algorithms.

To build the manuscript when a TeX distribution is available:

```bash
cd proof
latexmk -pdf main.tex
```

TeX was unavailable in the final research environment, so the source was
syntax-audited but no PDF build is claimed.
