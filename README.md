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

The saved final run passed all 25 tests in 211.839 seconds under Python
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
