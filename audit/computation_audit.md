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

[DISPROVED] This group refutes
\(a\leq\max\{\nu,2^{\lfloor(\nu-1)/2\rfloor}+1\}\): at \(\nu=7\) the proposed
right side is 9 but the exact cover number is 10.

[COMPUTED] src/verification/test_exact_computation.py independently compares
the optimized clique and coloring routines to naive enumeration for all 33,868
labeled simple graphs on at most six vertices, and also checks group axioms,
coset invariance, named records, direct-product/OR compatibility, witnesses,
and the \(E_m\) symplectic model for \(m=1,2,3\). It also reparses and verifies
every saved Python and GAP certificate. The latest 2026-08-13 run passed all
11 tests under Python 3.9.6. The scalar-symplectic test independently rebuilds
the table, graph, projective exclusion, spread, and covers. Exact output and
timing are preserved in verification.txt.

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

[UNVERIFIED] The \(p=5,m=2\) scalar-symplectic graph was not assigned a value.
Its 156-class projective clique calculation exceeded the short bounded trial,
so it is excluded from all result tables and claims.
