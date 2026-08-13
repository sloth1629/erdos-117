# Exact value at five: independent proof audit

## Statement

`[PROVED]` (by a computer-assisted proof)

\[
h(5)=5.
\]

The upper bound has one primary-source input and one finite exhaustive input.
This note records the independent structural audit of their connection.

## Five centralizers reduce the center quotient

Let \(G\) satisfy \(\nu(G)=5\), and let \(x_1,\ldots,x_5\) be a maximum
pairwise noncommuting set. Its centralizers cover \(G\): otherwise an element
outside their union could be adjoined. The cover is irredundant because
\(x_i\notin C_G(x_j)\) for \(i\ne j\). Its intersection is \(Z(G)\). Indeed,
if a noncentral \(y\) belonged to the intersection, all five \(x_i\) would lie
in \(C_G(y)\), contradicting the proved inequality
\(\nu(C_G(y))\le\nu(G)-2=3\).

Bryce--Fedri--Serena, Theorem 1.2 (printed p. 470; proof pp. 475--476),
proves that the intersection of an irredundant five-subgroup cover has index
at most 16. Hence

\[
Q=G/Z(G),\qquad |Q|\le16.
\]

This argument applies to arbitrary groups; the cited cover theorem itself
forces the displayed finite quotient.

## Why the Schur-cover enumeration is exhaustive

For a central extension

\[
1\longrightarrow A\longrightarrow G\longrightarrow Q\longrightarrow1,
\]

the commutator of chosen lifts of \(q,r\in Q\) is independent of the lift
choices. It is a crossed pairing and therefore induces a surjection

\[
\kappa_G:Q\wedge Q\longrightarrow G',\qquad
q\wedge r\longmapsto[\widehat q,\widehat r].
\]

The construction is \(Q\)-equivariant for conjugation, so
\(\ker\kappa_G\) is \(Q\)-invariant. Brown--Johnson--Robertson define the
exterior square and commutator map on printed p. 181, prove the central
extension construction in Proposition 7 on p. 182, and prove in Corollary 2,
pp. 182--183, that for a Schur cover \(S\twoheadrightarrow Q\),

\[
Q\wedge Q\cong S'
\]

compatibly with lifted commutators when \(H_2(Q)\) is finitely generated.
This hypothesis holds because \(Q\) is finite. Under this identification,
\(K=\ker\kappa_G\) is an \(S\)-normal subgroup of \(S'\), and

\[
q\text{ and }r\text{ fail to commute in the extension}
\quad\Longleftrightarrow\quad
[\widetilde q,\widetilde r]\notin K.
\]

Thus enumerating every \(S\)-normal \(K\le S'\) for one fixed Schur cover of
each \(Q\) includes every central-extension commutation graph. It may
overcount because not every such kernel need be realized by an extension;
overcounting is harmless for the universal coloring implication. No
homomorphism \(S\to G\), and no isomorphism \(G\cong S/K\), is asserted or
needed.

## Finite certificate

GAP 4.16.0 with SmallGrp 1.5.4 enumerates all 42 isomorphism types of groups
of order at most 16. For their fixed Schur covers it exports all 2,986
\(S\)-normal kernels, representing 2,396 distinct labeled adjacency tuples.
The independent Python verifier checks complete kernel serial ranges,
symmetry of every graph, exact clique witnesses, and exact coloring
witnesses. All 364 records with clique number at most five are five-colorable:

| \((\omega,\chi)\) | \((1,1)\) | \((3,3)\) | \((4,4)\) | \((5,5)\) |
|:---|---:|---:|---:|---:|
| records | 42 | 84 | 4 | 234 |

Consequently \(a(G)=\chi(\Delta_G)\le5\). If \(\nu(G)\le4\), the already
proved value \(h(4)=4\) applies. The extraspecial binary group \(S(2,2)\)
has \((\nu,a)=(5,5)\), giving the lower bound and equality.

## Adversarial conclusions

- The reduction is valid for infinite as well as finite original groups.
- A fixed Schur cover suffices because its derived subgroup realizes the
  exterior square with its commutator symbols; uniqueness of the whole cover
  is neither true nor required.
- Normal-kernel enumeration is a safe superset, not a classification of
  central extensions.
- The result is explicitly computer-assisted. Its load-bearing computation
  is reproduced by `test_h5_exterior_square_scan_certificates`.
- No blocking mathematical flaw was found in the reduction or certificate.

For the next case, the analogous literature statement \(f(6)=36\) reduces
\(\nu(G)=6\) to \(|G:Z(G)|\le36\), but does not itself prove an abelian
six-cover. The tempting stronger route “all such commuting graphs are
perfect” is false: the exact compressed graphs of `SmallGroup(32,49)` and
`SmallGroup(32,50)` have \(\nu=a=5\) while containing induced five-cycles.
