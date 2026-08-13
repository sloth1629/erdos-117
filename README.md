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
- [PROVED] \(h(1)=h(2)=1\), \(h(3)=3\), and \(h(4)=4\).
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
  families and every SmallGroup of orders 8, 32, and 64. The final test
  suite passes 11/11 tests.

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

Python 3.9 or later is sufficient:

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 -m unittest discover -s src/verification -p 'test_*.py' -v
```

The canonical experiment commands are documented in
[`src/python/README.md`](src/python/README.md). GAP is needed only to
regenerate the SmallGroups multiplication-table exports; the committed
tables and all Python verification are self-contained.

To build the manuscript when a TeX distribution is available:

```bash
cd proof
latexmk -pdf main.tex
```

TeX was unavailable in the final research environment, so the source was
syntax-audited but no PDF build is claimed.
