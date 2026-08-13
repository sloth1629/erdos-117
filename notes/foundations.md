# Foundations

Throughout this note graphs are simple, groups are nonempty, and the ambient
set theory is ZFC. Chromatic number and clique number are allowed to be
cardinals until finiteness is proved. Thus a nonempty edgeless graph has both
invariants equal to \(1\), while the empty graph has both equal to \(0\).

## The full noncommuting graph

### [PROVED] The graph/group dictionary

Let \(\Gamma_G\) have vertex set all of \(G\), with distinct \(x,y\) adjacent
exactly when \(xy\ne yx\). Then

\[
\omega(\Gamma_G)=\nu(G),\qquad \chi(\Gamma_G)=a(G),
\]

where, before finiteness is known, the right sides have their natural
cardinal-valued meanings. In particular, whenever \(\nu(G)\) is finite, the
display agrees with the canonical definition in AGENTS.md.

**Proof.** A clique in \(\Gamma_G\) is, definition for definition, a set of
pairwise noncommuting elements. This proves the first equality, including
both directions.

Let \(c:G\to I\) be a proper coloring. Each nonempty color class \(X_i\) is a
pairwise commuting *set*. The subgroup \(\langle X_i\rangle\) is abelian:
every element of it is a finite word in elements of \(X_i\) and their inverses,
and pairwise commuting generators and their inverses allow any two such words
to be reordered. The subgroups \(\langle X_i\rangle\) cover \(G\), so
\(a(G)\leq\chi(\Gamma_G)\).

Conversely, suppose \(G=\bigcup_{i\in I}A_i\), with every \(A_i\leq G\)
abelian. Index the cover by an ordinal (automatic for a finite cover, and
available in ZFC in general) and give \(g\) the least color \(i\) for which
\(g\in A_i\). Two vertices of one color lie in one abelian subgroup and hence
commute, so the coloring is proper. Therefore
\(\chi(\Gamma_G)\leq a(G)\). This also records the only choice convention in
the cardinal-valued formulation; no choice is needed once the cover is
finite. \(\square\)

### [PROVED] Central isolated vertices, including the abelian exception

Every \(z\in Z(G)\) is isolated in \(\Gamma_G\). If \(G\) is nonabelian, the
induced graph on \(G\setminus Z(G)\) contains an edge; adding or deleting the
isolated central vertices then changes neither \(\omega\) nor \(\chi\). If \(G\)
is abelian (including the trivial group), however, the full graph is nonempty
and edgeless, so \(\omega=\chi=\nu=a=1\), whereas the graph obtained by deleting
all central vertices is empty and has the standard graph invariants \(0\).
Thus “remove the center without changing the invariants” requires either the
nonabelian hypothesis or a special empty-graph convention. This repository
uses the full graph and handles abelian groups separately.

## Exact compression by central cosets

### [PROVED] Central-coset graph and blow-up theorem

Define the **central-coset graph** \(\Delta_G\) on the set \(G/Z(G)\), retaining
the identity coset, by joining two distinct cosets \(xZ(G)\) and \(yZ(G)\) when
\(xy\ne yx\). Then this is well-defined and

\[
\omega(\Delta_G)=\omega(\Gamma_G)=\nu(G),\qquad
\chi(\Delta_G)=\chi(\Gamma_G)=a(G).
\]

More precisely, \(\Gamma_G\) is obtained from \(\Delta_G\) by replacing every
vertex with an independent set of size \(|Z(G)|\), with all or none of the
edges between two such sets according as the corresponding vertices of
\(\Delta_G\) are adjacent or nonadjacent.

**Proof.** For \(z,w\in Z(G)\),

\[
(xz)(yw)=xyzw,\qquad (yw)(xz)=yxzw.
\]

Consequently \(xz\) and \(yw\) commute if and only if \(x\) and \(y\) commute.
Two elements \(xz,xw\) in one central coset commute. This proves
well-definedness and the asserted blow-up description.

A clique uses at most one point from each independent fiber, and its projected
cosets form a clique of \(\Delta_G\). Conversely, choosing one representative
from each coset of a clique in \(\Delta_G\) gives a clique in \(\Gamma_G\). For
finite cliques this requires only finite choice. Hence the clique numbers are
equal.

A coloring of \(\Delta_G\) pulls back to a coloring of \(\Gamma_G\). In the
other direction, any transversal induces a copy of \(\Delta_G\) inside
\(\Gamma_G\), so restricting a coloring gives the reverse inequality. (After
the finite-index theorem below only a finite transversal is involved.) Thus
the chromatic numbers are equal, and the preceding theorem identifies them
with \(a(G)\). \(\square\)

### [PROVED] Covers may be made central

Every abelian subgroup \(A\leq G\) enlarges to the abelian subgroup
\(AZ(G)\). Hence a minimum abelian-subgroup cover may always be chosen with
every member containing \(Z(G)\). Equivalently, a proper color class of
\(\Delta_G\), after representatives are chosen, generates together with
\(Z(G)\) an abelian subgroup containing all central cosets in that class. This
gives a direct cover-theoretic proof of
\(a(G)=\chi(\Delta_G)\), independent of the blow-up language.

### [DISPROVED] Ordinary quotient commutation is not the compression

It is false that \(\Delta_G\) is the noncommuting graph of the quotient group
\(G/Z(G)\). Cosets \(xZ(G),yZ(G)\) commute in the quotient exactly when
\([x,y]\in Z(G)\), whereas they are nonadjacent in \(\Delta_G\) exactly when
\([x,y]=1\). For \(D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), the
quotient \(D_8/Z(D_8)\cong C_2\times C_2\) is abelian, but \(\Delta_{D_8}\) is
an isolated identity coset together with a triangle on the other three
cosets. Thus quotienting by the center can erase every noncommuting edge.

### [PROVED] Large and infinite centers cause no change

If \(A\) is any abelian group, finite or infinite, then
\(Z(G\times A)=Z(G)\times A\), and the natural map identifies
\(\Delta_{G\times A}\) with \(\Delta_G\). Consequently
\(\nu(G\times A)=\nu(G)\) and \(a(G\times A)=a(G)\). This supplies an explicit
check that neither invariant is sensitive to an arbitrarily large central
factor.
