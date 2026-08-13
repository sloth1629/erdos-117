# Computation Audit

## Scope and exact translations

[PROVED] For a group \(G\), \(x,y\in G\), and \(z,w\in Z(G)\), the elements
\(xz,yw\) commute if and only if \(x,y\) commute: the two products are
\(xyzw\) and \(yxzw\).  Elements in one coset \(xZ(G)\) commute with each
other.  Thus central cosets are independent twin classes in the noncommuting
graph.  A clique uses at most one vertex from each class and projects to a
clique of the compressed graph; conversely representatives lift a compressed
clique.  A compressed coloring lifts by giving a coset one color, while any
full coloring restricts to chosen representatives.  Hence both clique and
chromatic number are preserved by this compression; this does not assert that
the quotient group \(G/Z(G)\) preserves commutation.

[PROVED] For every finite group \(G\), \(a(G)=\chi(\Gamma_G)\).  An abelian
subgroup cover yields a proper coloring after assigning each element to one
cover member.  Conversely, every color class is pairwise commuting, so the
subgroup it generates is abelian (all finite products of mutually commuting
generators and their inverses commute), and these generated subgroups cover
\(G\).

## Implementation and optimality checks

[COMPUTED] src/python/finite_groups.py uses explicit integer multiplication
tables and validates closure at construction plus identity, inverses, and every
associativity triple before analysis; it has no non-standard dependency.

[COMPUTED] Maximum clique uses recursive branch-and-bound, with a greedy proper
coloring of each candidate subgraph as an upper bound.  Exact coloring tests
successive \(k\) values and uses DSATUR vertex ordering; trying existing colors
and at most one unused color is complete because unused color names are
symmetric.  The verifier checks every edge of clique/coloring witnesses.

[COMPUTED] For explicit exact_small_groups instances other than E3, a second
route enumerates all subgroups by closure, retains maximal abelian subgroups,
and solves exact set cover; every returned member is independently rechecked
for subgroup and commutativity closure and the union is rechecked against all
elements. For E3 and the order-64 SmallGroups scan, the exact graph lower bound
together with a verified generated-subgroup cover supplies \(a(G)\);
exhaustive subgroup enumeration was not requested.

[PROVED] For prime \(p\) and \(m\geq1\), scalar-cocycle multiplication
\[
(a,b,c)(a',b',c')=(a+a',b+b',c+c'+a\cdot b')
\]
has commutator scalar \(a\cdot b'-a'\cdot b\). Thus its central-coset graph is
the graph on \(\mathbb F_p^{2m}\) joining vectors with nonzero standard
symplectic product. Scalar multiples of one nonzero vector form independent
twin classes, so compressing them to projective points preserves clique
number.

[PROVED] A pairwise commuting set of quotient vectors spans a totally
isotropic subspace and therefore has dimension at most \(m\). In a coloring,
the class containing zero has at most \(p^m\) vectors and each other class at
most \(p^m-1\). Counting the \(p^{2m}\) vectors gives at least \(p^m+1\)
colors. Conversely, the \(p^m+1\) projective lines in
\(\mathbb F_{p^m}^2\), transported through the trace-pairing Gram matrix, form
a spread by totally isotropic \(m\)-spaces; their full preimages are abelian
subgroups covering the group. Hence this construction has \(a=p^m+1\).

[COMPUTED] For \(p=3,m=2\), the implementation checked all 14,348,907
associativity triples in the order-243 table, all central-coset element pairs,
and all 81-by-81 scalar-form adjacencies. A 7-clique is explicit. The primary
color-bounded clique search visited 15,661 nodes; a structurally different
include/exclude recursion on 40 projective classes exhaustively excluded an
8-clique in 10,912 nodes with 6,333 cache hits. Therefore \(\nu=7\).

[COMPUTED] Exact DSATUR searches at 7, 8, and 9 colors failed after 58, 207,
and 873 nodes; a 10-color search succeeded. Independently, the saved
\(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\) spread uses trace Gram matrix
\(\operatorname{diag}(2,1)\), has 10 isotropic subspaces of size 9, and gives
10 full-preimage abelian subgroups of order 27. Both the direct preimages and
the subgroups generated from the spread coloring were checked for closure,
commutativity, and complete coverage. Thus \(a=10\).

## Extended scalar-symplectic clique certificates

[PROVED] For odd prime \(p\) and rank \(m\ge2\), fix an adjacent projective
pair \(\langle e_1\rangle,\langle f_1\rangle\). Every third point adjacent to
both has a representative \(e_1+t f_1+u\), where \(t\ne0\) and
\(u\in\langle e_1,f_1\rangle^\perp\). The pair stabilizer contains the maps
\(e_1\mapsto r e_1,\ f_1\mapsto r^{-1}f_1\) and the full symplectic group on
the perpendicular complement. Projective renormalization changes \(t\) by a
square, and the latter symplectic group is transitive on its nonzero vectors.
Consequently the third point has exactly four relevant orbits: \(u=0\) or
\(u\ne0\), independently with \(t\) square or nonsquare. Point/pair
transitivity therefore reduces exclusion of a clique of size \(L+1\) to four
residual exclusions after a fixed three-clique.

[PROVED] The projective nonorthogonality graph has

\[
v=\frac{p^{2m}-1}{p-1},\qquad k=p^{2m-1},\qquad
\lambda=\mu=p^{2m-2}(p-1).
\]

Indeed two distinct projective points give independent symplectic linear
functionals, so vectors on which both are nonzero number
\(p^{2m-2}(p-1)^2\), before division by \(p-1\). Hence
\(A^2=(k-\mu)I+\mu J\), with restricted eigenvalues
\(\pm p^{m-1}\). The Hoffman/Delsarte bound applied to the complement gives
\(\omega\le p^m+1\).

[COMPUTED] `src/c/scalar_symplectic_clique.c` implements the four exact
residual searches using 64-bit bitsets and Tomita greedy-color
branch-and-bound. For \((p,m)=(5,2)\), the residual graph orders are
75, 75, 80, and 80. The searches visited 18,509, 19,101, 40,198, and 39,252
nodes and excluded a residual 16-clique in every case. A separately verified
18-clique therefore proves \(\nu=18\). The checked 26-member spread gives
\(a=26\).

[COMPUTED] For \((p,m)=(3,3)\), the residual graph orders are 81, 81, 108,
and 108. The four searches visited 437, 437, 55,623, and 55,039 nodes and,
together with a saved 13-clique, prove \(\nu=13\). The checked 28-member
spread gives \(a=28\). A Python implementation independently recomputes the
four residual maxima as 7, 7, 10, and 10 (and as 15 in every prime-5 case),
so the C upper certificates have an independent algorithm/language check.

[COMPUTED] For \((p,m)=(7,2)\), an explicit 33-clique is verified. Exhaustive
degree and common-neighbor checks give the strongly regular parameters
\((v,k,\lambda,\mu)=(400,343,294,294)\) and least eigenvalue \(-7\), hence the
rigorous interval \(33\le\nu\le50\). The 50-member spread verifies \(a=50\).
No exact \(\nu\) is claimed.

[COMPUTED] These extensions do not improve the prime-3 rank-2 efficiency:
the values or witness-implied upper bounds for \(\log(a)/\nu\) are about
0.1810 for \((5,2)\), 0.2563 for \((3,3)\), and at most 0.1185 for \((7,2)\),
versus about 0.3289 for \((3,2)\).

## Exterior-square enumeration at clique cutoff five

[PROVED] Let \(Q=G/Z(G)\), choose a Schur cover \(S\twoheadrightarrow Q\),
and put \(D=S'\). The lifted-commutator map identifies \(D\cong Q\wedge Q\):
the natural map \(Q\wedge Q\twoheadrightarrow S'\) is surjective, and both
sides have order \(|M(Q)||Q'|\). Every central extension of \(Q\) induces a
map \(D\to G'\), and its kernel is invariant under the natural \(Q\)-action,
equivalently normal in \(S\). Thus every possible central-coset graph for
quotient \(Q\) is obtained from membership of lifted commutators in one of the
\(S\)-normal subgroups \(K\le D\). Enumerating all such subgroups may be an
overcount, but cannot omit a graph needed for the upper bound.

[COMPUTED] GAP enumerated all 42 SmallGroups \(Q\) of orders 1 through 16.
For each, `AllSubgroups(D)` enumerated every subgroup and `IsNormal(S,K)`
retained every action-invariant kernel. The export records the total subgroup
count, retained count, and complete kernel serial range separately for every
\(Q\). There are 2,986 records and 2,396 distinct adjacency tuples.

[COMPUTED] Exact Python clique/coloring calculations give distribution

\[
(1,1):42,(3,3):84,(4,4):4,(5,5):234,(6,6):215,(7,7):22,(8,8):1,
(9,9):1492,(11,11):492,(13,13):315,(15,15):85.
\]

All 364 records with clique number at most five have chromatic number at most
five. Each result is
certified by a checked clique and coloring; the verifier also checks all
kernel serial ranges and the checksums of the GAP script and raw export.

[COMPUTED] Combining this exhaustive finite lemma with the cited-verified
Bryce--Fedri--Serena theorem \(f(5)=16\), the repository bridge
\(\nu(G)=5\Rightarrow[G:Z(G)]\le16\), the already proved \(h(4)=4\), and the
explicit \(E_2\) lower witness yields the computer-assisted conclusion
\(h(5)=5\). The argument covers arbitrary groups, because only the finite
central quotient \(Q\) and its finite exterior square enter the enumeration.

[DISPROVED] This group refutes
\(a\leq\max\{\nu,2^{\lfloor(\nu-1)/2\rfloor}+1\}\): at \(\nu=7\) the proposed
right side is 9 but the exact cover number is 10.

[COMPUTED] src/verification/test_exact_computation.py independently compares
the optimized clique and coloring routines to naive enumeration for all 33,868
labeled simple graphs on at most six vertices, and also checks group axioms,
coset invariance, named records, direct-product/OR compatibility, witnesses,
and the \(E_m\) symplectic model for \(m=1,2,3\). It also reparses and verifies
every saved Python and GAP certificate. The latest 2026-08-13 run passed all
15 tests under Python 3.9.6. The extended tests independently rebuild the
scalar graphs, four residual searches, strongly regular parameters, spreads,
the order-128 prefilter survivors, and every exterior-square graph witness.
Exact output and timing are preserved in verification.txt.

## Reproduction records

[COMPUTED] The exact finite-group run is configured by
experiments/configs/exact_small_groups.json (SHA-256
a15c05ab9bc0b31479ba78ea83a43047caefa26423b88abd53ddb233633f3471)
and recorded in experiments/logs/exact_small_groups.json; that record contains
all multiplication tables, central cosets, compressed adjacencies, witnesses,
search counts, generated abelian covers, and optional independent covers.

[COMPUTED] The graph-product run is configured by
experiments/configs/graph_products.json (SHA-256
67ee0f40ed8b730d4c118f6a087f13c98c0a92bee42059d253a563ba78e56d1b)
and recorded in experiments/logs/graph_products.json; its exact certificates
include both the D8/S3 compressed product and the general-graph
\(C_5\vee C_5\) warning.

[COMPUTED] The scalar-symplectic run is configured by
experiments/configs/scalar_symplectic.json (SHA-256
2607851d001173a3047788e0df76d6f9b7a6dab326a4cc63523687b54782d213)
and recorded in experiments/logs/scalar_symplectic_p3_m2.json. The canonical
order-243 multiplication table has SHA-256
1ea70ac5aecdb0088d33df420e03c3d81f37fa518844b22a65f5afa50bd6aba3.
The JSON saves the full compressed and projective adjacencies, clique and two
colorings, failed-color search counts, projective exclusion counts, field
model, spread subspaces, and two subgroup covers.

[COMPUTED] The extended exact scalar run is configured by
experiments/configs/scalar_symplectic_clique.json (SHA-256
341f17fcd55f7ab1dc771345bcc4eb0de451981118106d022079aa13141173e0)
and recorded in experiments/logs/scalar_symplectic_extended.json. The C
solver source SHA-256 is
09df944f82d0e99674f8005482db1d692de99eefc64c0dceccee6934e5f97c67.
The bounded prime-7 run uses scalar_symplectic_bounds.json (SHA-256
b562a2d2741dafc4fa3f72695d5fce6b83bdae608dcb66597221b2dbff0ec35b)
and is recorded in experiments/logs/scalar_symplectic_bounds.json.

[COMPUTED] The order-128 cutoff scan is recorded in
gap_smallgroups_order128_nu_le6.{tsv,json}; the raw TSV SHA-256 is
c7318e9bb2f8670787a3e8ba9afab5622dcff8a1cc5132b4a73c281d0e779956.
The GAP prefilter inspected all 2,328 SmallGroups and a rigorous greedy clique
excluded 1,910. Exact certificates for all 418 survivors have distribution
\((1,1):15,(3,3):60,(5,5):199,(6,6):144\), with no \(a>\nu\). Among them,
21 records at \(\nu=5\) and all 144 at \(\nu=6\) are non-AC groups.

[COMPUTED] The exterior-square run is configured by
experiments/configs/h5_exterior_scan.g (SHA-256
f17d31a5ea202bab29127bf383a5a7ad354a0e2acce5d66848f22e2a58eb4e5f).
Its raw TSV SHA-256 is
5a326a69d96c57c48f9b0751d001ab8156089c776927c8c33cd4ab640660b55f;
the certified JSON, concise Python output, and GAP regeneration transcript are
experiments/logs/h5_exterior.{json,stdout.txt} and
experiments/logs/h5_exterior_gap.stdout.txt.

[COMPUTED] GAP 4.16.0 with SmallGrp 1.5.4 independently supplied all complete
multiplication tables at orders 8, 32, and 64. The Python analyzer validated
all tables and recomputed every graph and cover invariant; it did not use GAP
graph algorithms. The raw TSV and certified JSON pairs are named
gap_smallgroups_orderN.{tsv,json}. Their raw TSV SHA-256 values for
\(N=8,32,64\) are respectively
68a347f6a0ade373aafca577b9a3d04138e7607136ec17fee4aff023cee36575,
de5c457611a4b04d4f391bc49356defc5733df3a19fef5f1b537798689bb34be, and
4047bc195b59a9e3c631a31499bf93bf0f4c577dbbded558249bc5f3dda54b27.
The complete enumerations produced 5, 51, and 267 records, matching the three
corresponding NumberSmallGroups values.

[COMPUTED] At order 64 the center indices are 1 (11 groups), 4 (31), 8 (70),
16 (128), and 32 (27), so the largest compressed graph has 32 vertices. Every
record contains a clique and a coloring of the same size, plus a generated
abelian subgroup cover of that size. The verifier reconstructs all 267 tables
from the checksummed TSV, checks every group axiom and central-coset adjacency,
and rechecks all clique, coloring, and subgroup-cover certificates. Thus the
reported equality \(a(G)=\nu(G)\) for all 267 records does not depend on an
uncertified optimizer conclusion.

[COMPUTED] The order-64 \((\nu,a)\) counts are
\((1,1):11\), \((3,3):31\), \((5,5):72\), \((6,6):38\),
\((7,7):10\), \((9,9):69\), \((11,11):33\), and \((17,17):3\).
No record has \(a>\nu\), and no record violates the candidate bound
\(\max\{\nu,2^{\lfloor(\nu-1)/2\rfloor}+1\}\). Candidate-bound slack is zero
for 141 records and positive for the other 126, with distribution
\(1:11,2:10,8:69,22:33,240:3\).

[COMPUTED] Canonical commands and concise outputs are captured in
experiments/logs/exact_small_groups.stdout.txt,
experiments/logs/graph_products.stdout.txt, and
experiments/logs/verification.txt.  Python bytecode was redirected to
/tmp/erdos117-pycache because the system Python cache location is not writable
inside the workspace sandbox.

[UNVERIFIED] SageMath and Magma were unavailable on the executable path. GAP
was locally built under ignored work/ and is not a repository dependency; its
official bundle checksum provenance is tracked separately by the bootstrap
workstream. Missing optional-package informational warnings in the GAP stdout
do not affect SmallGrp table export.

[UNVERIFIED] The exact clique value for \(p=7,m=2\) was not completed; only
the certified interval \(33\le\nu\le50\) is claimed.
