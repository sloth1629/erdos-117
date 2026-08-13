# Erdős Problem 117 — Research Protocol

## Mission

Resolve Erdős Problem #117 completely. Partial bounds, computations, and literature findings are intermediate assets, not a final answer. Never describe an unverified argument as a solution.

Research date: 2026-08-13.

## Canonical notation

For a group \(G\), let

\[
\nu(G)=\max\{|S|:S\subseteq G,\ xy\ne yx\text{ for all distinct }x,y\in S\}
\]

whenever this maximum is finite, and let

\[
a(G)=\min\{m:G=A_1\cup\cdots\cup A_m,\ A_i\leq G\text{ abelian}\}.
\]

Finally,

\[
h(n)=\sup\{a(G):\nu(G)\leq n\}.
\]

Write \(\Gamma_G\) for the simple noncommuting graph on all elements of \(G\); central elements are isolated. Do not assume that \(G/Z(G)\) preserves commutation. Central cosets may be compressed only after proving the relevant invariance.

## Evidence labels

Every material claim must be marked with exactly one status:

- `[PROVED]`: complete proof and dependencies are in this repository.
- `[CITED-VERIFIED]`: the primary source was read and the exact theorem, page, and hypotheses were checked.
- `[COMPUTED]`: a reproducible exact computation and verifier are present.
- `[CONJECTURE]`: plausible but unproved.
- `[DISPROVED]`: refuted, with a counterexample or proof.
- `[UNVERIFIED]`: reported or suspected but not yet checked.

Never promote experiments to proofs. Never use an inaccessible source as a load-bearing black box. Track finite versus arbitrary-group hypotheses explicitly.

## Proof standards and hazards

1. Treat a pairwise commuting set as a set, not a subgroup; prove that the subgroup it generates is abelian.
2. Check both directions of every graph/group translation.
3. Check \(n=1,2,3\), abelian and trivial groups, large centers, and infinite groups.
4. Do not assume direct-product multiplicativity for clique or chromatic number.
5. State every use of choice, CFSG, isoclinism, or a computational classification.
6. Save witnesses, solver logs, versions, and independent verification for every computational record.
7. Record failed proof attempts in `notes/failed_approaches.md`; do not silently recycle them.
8. Before any novelty claim, complete backward and forward citation searches and update `audit/source_audit.md`.

## Workstream ownership

- A — literature and terminology: `literature/` and `audit/source_audit.md`.
- B — structural group theory and upper bounds: `notes/structural_reductions.md`, `notes/known_bounds.md`.
- C — constructions and exact computation: `src/`, `experiments/`, `results/`.
- D — graph products, asymptotics, and adversarial audit: `notes/`, `audit/adversarial_review.md`.

Keep independent workstream notes until adversarial comparison. Decisive lemmas require an independent reconstruction or explicit audit.

## Reproducibility commands

The canonical commands will evolve with the code. At bootstrap:

```bash
python3 -m unittest discover -s src/verification -p 'test_*.py'
```

If GAP or TeX is unavailable, record that in `STATUS.md`; do not fabricate output.

## Git discipline

Commit and push meaningful milestones. Keep source acquisition, computational data, foundational proofs, and candidate final theorems in separately reviewable commits. Before committing, inspect `git status --short` and the staged diff. Never commit secrets, browser state, credentials, or unlicensed source PDFs.
