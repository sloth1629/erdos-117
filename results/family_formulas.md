# Family Formulas

Every formula must specify its parameter range, finite/arbitrary scope, evidence label, and proof or verified source.

## Explicit extraspecial 2-groups

[COMPUTED] For each integer \(m\in\{1,2,3\}\), the finite group \(E_m\) was
instantiated on triples \((a,b,c)\in\mathbb F_2^m\times\mathbb F_2^m\times
\mathbb F_2\), with cocycle \(a\mathbin\cdot b'\); all group axioms and every
pair of elements in every pair of central cosets were checked exactly.

| \(m\) | \(|E_m|\) | \(|Z(E_m)|\) | compressed vertices | \(\nu(E_m)\) | \(a(E_m)\) | exact coloring exclusions |
|---:|---:|---:|---:|---:|---:|:---|
| 1 | 8 | 2 | 4 | 3 | 3 | clique bound attains 3 |
| 2 | 32 | 2 | 16 | 5 | 5 | clique bound attains 5 |
| 3 | 128 | 2 | 64 | 7 | 9 | exhaustive failures at 7 and 8 colors |

[COMPUTED] For \(m\in\{1,2,3\}\), exhaustive comparison of every pair of
compressed vertices identifies adjacency with

\[
 (a,b)\sim(a',b')\quad\Longleftrightarrow\quad
 a\cdot b'+a'\cdot b=1\quad\text{in }\mathbb F_2.
\]

[PROVED] For every finite \(E_m\) in this explicit family, \(m\geq1\),
\(\nu(E_m)=2m+1\) and \(a(E_m)=2^m+1\). Complete proofs are Theorems C2.1
and C2.2 in `notes/class_two_geometry.md`; the computation here independently
checks \(m\leq3\).

## Odd-characteristic scalar symplectic record

[COMPUTED] Let \(P_{3,2}\) be the finite group on
\(\mathbb F_3^2\times\mathbb F_3^2\times\mathbb F_3\) with
\[
(a,b,c)(a',b',c')=(a+a',b+b',c+c'+a\cdot b').
\]
The complete multiplication table has order 243 and center order 3. Exhaustive
comparison identifies its 81-vertex central-coset graph with
\[
(a,b)\sim(a',b')\quad\Longleftrightarrow\quad
a\cdot b'-a'\cdot b\neq0.
\]

[COMPUTED] Exact certificates give
\[
\nu(P_{3,2})=7,\qquad a(P_{3,2})=10.
\]
The 7-clique is saved explicitly. An independent include/exclude recursion on
the 40 nonzero projective twin classes exhaustively excludes an 8-clique in
10,912 search nodes. Exact coloring independently rejects 7, 8, and 9 colors.

[COMPUTED] A second 10-color upper witness is the Desarguesian symplectic
spread built from
\(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\). Its 10 totally isotropic
2-subspaces each have 9 quotient vectors, meet pairwise only at zero, and
partition the 80 nonzero vectors. Their full preimages are 10 checked abelian
subgroups of order 27 covering \(P_{3,2}\).

[DISPROVED] The candidate bound
\[
a(G)\leq\max\{\nu(G),2^{\lfloor(\nu(G)-1)/2\rfloor}+1\}
\]
fails: its right side is 9 for \(\nu=7\), while \(a(P_{3,2})=10\).
Consequently the computed lower record improves to \(h(7)\geq10\).

[UNVERIFIED] The prime-5 rank-2 case was not completed in this bounded
milestone; its 156-vertex projective clique search was not quick enough for
inclusion, so no value is claimed.

## Dihedral checks

[COMPUTED] For finite \(D_{2n}=\langle r,s\mid r^n=s^2=1,
srs=r^{-1}\rangle\), exact calculations gave the following values.

| \(n\) | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\nu(D_{2n})=a(D_{2n})\) | 4 | 3 | 6 | 4 | 8 | 5 | 10 | 6 |

[PROVED] For every finite \(D_{2n}\), \(n\geq3\), the formula is
\(\nu(D_{2n})=a(D_{2n})=n+1\) for odd \(n\), and \(n/2+1\) for even \(n\).
The complete elementary proof is Theorem EF.1 in
notes/elementary_families.md.

## Heisenberg checks

[COMPUTED] For the finite unitriangular Heisenberg groups
\(H_p=UT_3(\mathbb F_p)\) at \(p\in\{2,3,5\}\), exact multiplication-table,
graph, and independent subgroup-cover calculations give
\(\nu(H_p)=a(H_p)=p+1\), namely \(3,4,6\).

[PROVED] The formula \(\nu(H_p)=a(H_p)=p+1\) holds for every prime \(p\).
The complete determinant-geometry proof is Theorem EF.3 in
notes/elementary_families.md; the listed computations are independent
checks for \(p\in\{2,3,5\}\).

## OR products and the direct-product hazard

[COMPUTED] The compressed noncommuting graph of the finite group
\(D_8\times S_3\) was checked vertex-by-vertex against the OR product of the
compressed factor graphs; the factor pairs \((\omega,\chi)=(3,3),(4,4)\) give
\((\nu,a)=(12,12)\) for the product.

[DISPROVED] Clique and chromatic numbers are not multiplicative under OR
products for arbitrary finite simple graphs: exact certificates give
\((\omega(C_5),\chi(C_5))=(2,3)\), whereas
\((\omega(C_5\vee C_5),\chi(C_5\vee C_5))=(5,8)\), so \(5>2^2\) and \(8<3^2\).

[UNVERIFIED] The preceding \(C_5\vee C_5\) record is a graph-level warning, not
a counterexample formed from noncommuting graphs of finite groups; no strict
group direct-product example was found in the configured pair check.

## SmallGroups enumeration

[COMPUTED] GAP 4.16.0 with SmallGrp 1.5.4 exported all finite groups of orders
8 (5 isomorphism classes), 32 (51 classes), and 64 (267 classes). Python then
validated every multiplication table and independently reconstructed every
central-coset graph and exact \((\nu,a)\). At order 8 the distribution is 3
groups with \((1,1)\) and 2 with \((3,3)\). At order 32 it is 7 with
\((1,1)\), 15 with \((3,3)\), 21 with \((5,5)\), 5 with \((6,6)\), and 3
with \((9,9)\).

[COMPUTED] The exact order-64 distribution is:

| \((\nu,a)\) | (1,1) | (3,3) | (5,5) | (6,6) | (7,7) | (9,9) | (11,11) | (17,17) |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| number of groups | 11 | 31 | 72 | 38 | 10 | 69 | 33 | 3 |

[COMPUTED] No group in these 323 isomorphism classes has \(a>\nu\). For all
267 order-64 groups the valid clique and coloring certificates have the same
size, so they certify optimality directly. The largest compressed graph has
32 vertices. The three records with \((\nu,a)=(17,17)\) are
`SmallGroup(64,52)`, `SmallGroup(64,53)`, and `SmallGroup(64,54)`.

[COMPUTED] Every order-64 record satisfies
\[
a(G)\leq\max\{\nu(G),2^{\lfloor(\nu(G)-1)/2\rfloor}+1\}.
\]
The candidate-bound slack (right side minus \(a\)) is 0 for 141 groups, 1 for
11, 2 for 10, 8 for 69, 22 for 33, and 240 for 3. This bounded enumeration is
not a classification result beyond orders 8, 32, and 64.
