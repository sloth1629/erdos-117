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

## Prime-5 rank-2 scalar symplectic record

[COMPUTED] For the finite scalar extraspecial group \(P_{5,2}\) of order
\(5^5=3125\), the central-coset graph has \(5^4=625\) vertices and its
nonzero scalar-twin compression is the 156-point projective graph
\(W(3,5)\), with adjacency given by nonorthogonality for the standard
symplectic form. An explicit 18-clique is saved in
`experiments/logs/scalar_symplectic_extended.json`.

[PROVED] Pair transitivity and the stabilizer of a fixed hyperbolic pair
\((e_1,f_1)\) reduce the third point of any clique of size at least three to
four cases. After replacing the third point by a projectively equivalent
representative these are

\[
e_1+t f_1,\qquad e_1+e_2+t f_1,
\]

where \(t\) represents either the square or nonsquare class. Indeed a third
point has a representative \(e_1+t f_1+u\), with \(t\ne0\) and
\(u\in\langle e_1,f_1\rangle^\perp\). The pair stabilizer contains
\(e_1\mapsto r e_1,\ f_1\mapsto r^{-1}f_1\) and the full symplectic group on
the perpendicular complement. After projective renormalization this changes
\(t\) by a square, while the complementary symplectic group is transitive on
its nonzero vectors. Hence \(u=0\) versus \(u\ne0\), and square versus
nonsquare \(t\), give exactly the four cases.

[COMPUTED] A dependency-free C implementation exhaustively searched the four
residual graphs of orders 75, 75, 80, and 80 using greedy-color
branch-and-bound. It visited respectively 18,509, 19,101, 40,198, and 39,252
nodes, and excluded a residual 16-clique in every case. Together with the
saved witness this certifies

\[
\nu(P_{5,2})=18.
\]

[PROVED] The general isotropic counting lower bound and Desarguesian spread
construction already proved in `audit/computation_audit.md` give
\(a(P_{p,m})=p^m+1\). The saved \(\mathbb F_{25}\) spread independently checks
the 26-color upper witness, so

\[
(\nu(P_{5,2}),a(P_{5,2}))=(18,26).
\]

[COMPUTED] This does not improve the current extremal efficiency:
\(\log(26)/18\approx0.1810\), whereas the prime-3 rank-2 record has
\(\log(10)/7\approx0.3289\).

[COMPUTED] The same four-orbit exact certificate has 364 projective vertices
for \(p=3,m=3\). A saved 13-clique and four residual searches of orders 81,
81, 108, and 108 certify

\[
(\nu(P_{3,3}),a(P_{3,3}))=(13,28).
\]

The searches visited 111,536 nodes in total. Its efficiency
\(\log(28)/13\approx0.2563\) is again below the prime-3 rank-2 record.

[COMPUTED] For \(p=7,m=2\), a saved projective 33-clique and the independently
checked strongly regular parameters give

\[
33\leq\nu(P_{7,2})\leq50,\qquad a(P_{7,2})=50.
\]

The upper endpoint is the Delsarte bound \(1-343/(-7)=50\). The exact clique
number was not completed, so this bounded record is excluded from the exact
result table. Already the witness implies
\(\log(a)/\nu\leq\log(50)/33\approx0.1185\), far below the prime-3 rank-2
record.

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

### Exterior-square enumeration for \(h(5)\)

[PROVED] Let \(Q=G/Z(G)\), let \(S\twoheadrightarrow Q\) be a Schur cover,
and put \(D=S'\). The standard lifted-commutator map identifies
\(D\cong Q\wedge Q\). Every central extension of \(Q\), including \(G\),
therefore induces a homomorphism \(D\to G'\). Its kernel \(K\) is invariant
under the natural \(Q\)-action and hence is normal in \(S\). For chosen lifts
\(s_q\in S\), two central cosets \(q,r\in Q\) commute in \(G\) exactly when
\([s_q,s_r]\in K\). Thus enumerating every \(S\)-normal subgroup \(K\le D\)
enumerates a superset of all possible central-coset commutation graphs with
quotient \(Q\); the harmless superset arises because an actual extension
kernel satisfies additional restrictions not needed for the upper bound.

[COMPUTED] GAP 4.16.0 and SmallGrp 1.5.4 enumerated every group \(Q\) of
order at most 16, constructed a Schur cover, enumerated every subgroup of
\(D=S'\), and retained every \(S\)-normal subgroup. This gives 2,986 records
and 2,396 distinct adjacency tuples. Exact clique/coloring certificates have
distribution

| \((\omega,\chi)\) | (1,1) | (3,3) | (4,4) | (5,5) | (6,6) | (7,7) | (8,8) | (9,9) | (11,11) | (13,13) | (15,15) |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| records | 42 | 84 | 4 | 234 | 215 | 22 | 1 | 1492 | 492 | 315 | 85 |

[COMPUTED] In particular, all 364 records with \(\omega\le5\) have
\(\chi=\omega\le5\). The tracked GAP log records every exterior-subgroup
count, every retained normal-kernel count, and a serial number for every
kernel; the serial ranges are complete. The Python verifier reparses all
2,986 graphs and checks every clique and coloring witness.

[PROVED] Combining this exhaustive lemma with the cited-verified
Bryce--Fedri--Serena value \(f(5)=16\) and the repository proof that
\(\nu(G)=5\) implies \([G:Z(G)]\le16\) yields the computer-assisted exact
conclusion

\[
h(5)=5.
\]

Indeed groups with \(\nu\le4\) satisfy the already proved \(h(4)=4\); groups
with \(\nu=5\) have one of the enumerated central-coset graphs and hence
\(a(G)=\chi\le5\). The extraspecial group \(E_2\) supplies equality.

### Exterior-square enumeration for \(h(6)\)

[PROVED] The cited-verified value \(f(6)=36\) and the repository's
irredundant-centralizer bridge imply
\[
\nu(G)=6\quad\Longrightarrow\quad [G:Z(G)]\le36
\]
for arbitrary groups. The self-contained alternating-form proof in
`notes/exact_h6.md` separately excludes the only infeasible exterior-square
enumeration case: if \(G/Z(G)\cong C_2^5\), then \(\nu(G)\ge9\).

[COMPUTED] GAP 4.16.0 and SmallGrp 1.5.4 enumerated all 162 quotient types of
order at most 36. For the 161 nonexceptional quotients it enumerated every one
of 23,527 action-invariant exterior-square kernels. Exact verification splits
them into 18,231 nonfaithful-radical graphs, 4,982 graphs with a saved
seven-clique, and 314 faithful candidates. The candidates have distribution

| \((\omega,\chi)\) | (1,1) | (3,3) | (4,4) | (5,5) | (6,6) |
|:---|---:|---:|---:|---:|---:|
| records | 1 | 1 | 2 | 93 | 217 |

[COMPUTED] A redundant \(C_2^5\) certificate enumerates all 174,251
two-dimensional pencils of alternating forms on \(\mathbb F_2^5\). All
156,240 pencils with zero common radical have a checked nine-clique, and an
independent Python transvection-orbit reconstruction verifies the complete
split 52,080 of rank profile \((2,4,4)\) and 104,160 of profile \((4,4,4)\).

[PROVED] Consequently every group with \(\nu(G)\le6\) has \(a(G)\le6\).
The already exact \(h(5)=5\) handles the smaller-clique case, and the
Heisenberg group \(H_5\) has \((\nu,a)=(6,6)\). Therefore the
computer-assisted exact value is

\[
h(6)=6.
\]

### Direct SmallGroups scans

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

[COMPUTED] A separate SmallGroups order-128 prefilter examined all 2,328
isomorphism classes. A deterministic greedy clique rigorously excluded 1,910
groups from the range \(\nu\leq6\). Exact clique and coloring certificates for
all 418 survivors give distribution
\((1,1):15,(3,3):60,(5,5):199,(6,6):144\), with no \(a>\nu\).
Of these, 21 of the \(\nu=5\) groups and all 144 of the \(\nu=6\) groups are
non-AC groups, so equality here is not solely an AC-group/perfect-graph
consequence. This is a bounded computation, not a structural theorem.
