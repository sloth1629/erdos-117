# Exact Problem and Boundary Conventions

## Canonical extremal function

For every nonempty group \(G\), let \(a(G)\) be the least number of abelian
subgroups whose union is \(G\). When finite, let \(\nu(G)\) be the maximum
size of a set of pairwise noncommuting elements. For \(n\geq1\), define

\[
h(n)=\sup\{a(G):G\text{ is a group and }\nu(G)\leq n\}.
\]

[PROVED] The supremum is finite, integer-valued, and attained by a finite
group. See the exact finite commutation-model theorem in
notes/structural_reductions.md and the self-contained bounds in
notes/known_bounds.md.

## Boundary values and conventions

- [PROVED] \(h(1)=h(2)=1\). Every nonabelian group contains the pairwise
  noncommuting triple \(x,y,xy\).
- [PROVED] \(h(3)=3\), attained by \(D_8\).
- [PROVED] \(h(4)=4\), attained by \(S_3\).
- [PROVED] \(h(5)=5\) and \(h(6)=6\), by the complete exterior-square
  certificates in `notes/exact_h5.md` and `notes/exact_h6.md`.
- [PROVED] \(h(7)=10\), by the computer-assisted proof in
  `notes/exact_h7.md`; the lower witness is \(S(3,2)\).
- [PROVED] Central elements remain vertices of the full noncommuting graph
  and are isolated. This makes the abelian case agree exactly with
  \(a(G)=\nu(G)=1\).
- [PROVED] The central-coset graph retains the identity coset and preserves
  both invariants. It is not the noncommuting graph of \(G/Z(G)\).
- [PROVED] The definition ranges over arbitrary finite or infinite groups;
  the exact finite model shows that this makes no difference to \(h\).

## What would constitute a complete resolution

A complete resolution must determine \(h(n)\) exactly for every \(n\), or
determine the sharp asymptotic behavior explicitly asked for in a defensible
reformulation, with matching constructions and universal upper bounds. It
must include arbitrary groups, all boundary cases, and every constant.

[UNVERIFIED] This repository has not achieved that objective. It determines
\(h(n)\) through \(n=7\), proves new general reductions and bounds, and
disproves one natural exact candidate.  Its strongest audited universal
upper bound is the CFSG-dependent estimate
\(h(n)\le2^{O(n\log\log n)}\), but the optimal exponential rate and
the values \(h(n)\) for \(n\geq8\) remain open except for lower and upper
bounds.
