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

[PROVED] Combining this exhaustive finite lemma with the cited-verified
Bryce--Fedri--Serena theorem \(f(5)=16\), the repository bridge
\(\nu(G)=5\Rightarrow[G:Z(G)]\le16\), the already proved \(h(4)=4\), and the
explicit \(E_2\) lower witness yields the computer-assisted conclusion
\(h(5)=5\). The argument covers arbitrary groups, because only the finite
central quotient \(Q\) and its finite exterior square enter the enumeration.

## Finite maximal-six-cover audit underlying \(f(6)=36\)

[CITED-VERIFIED] Alencar (2011), Lemma 4.1, pp. 51--59, states the finite
maximal irredundant core-free six-cover assertions used in the published
\(f(6)\) argument. Its final computation uses inconsistent \(L_i\) labels on
p. 59. The reconstruction therefore uses no numbered subgroup labels: every
group is identified by `IdGroup`, and every maximal subgroup and qualifying
six-subset is exported as an exact element bitmask.

[COMPUTED] GAP 4.16.0 with SmallGrp 1.5.4 enumerated 165 ambient subgroup
conjugacy-class records and reduced them, by isomorphism ID only, to 48 group
types. The census includes all three order-72 and seven order-108 subgroup
classes of \(S_3^3\), all 21 order-48 and 15 order-96 subgroup classes of
\(S_4^2\), all 14 subdirect classes of \(S_3^3\), all 69 subgroup classes of
\(C_2\times S_3\times S_3\), all SmallGroups of orders 50 and 100 with
centerless cases selected, \(A_5,S_5\), and all 11 subgroup classes of
\(S_4\). Class sizes certify respectively 9, 7, 88, 44, 90, 206, and 30
concrete subgroups in the ambient families just listed.

[COMPUTED] A standard-library Python verifier reparses every complete
multiplication table, exhaustively checks the group axioms, independently
enumerates 5,257 subgroups, recovers the complete maximal-subgroup sets, and
recomputes union, private-element irredundancy, intersection, and conjugate
core for all 5,545,351 six-subsets. It agrees with GAP on 100,483 covers,
10,308 irredundant covers, and 6,678 irredundant core-free covers. Thus the
certificate does not depend on GAP's cover filtering or maximal-subgroup
ordering.

[COMPUTED] The subdirect products of \(S_3^3\) with qualifying covers are
exactly `SmallGroup(18,4)`, with 234 covers and \(|D|=1\), and
`SmallGroup(54,14)`, with 6,318 covers and \(|D|=2\). The order-50 and
order-100 positive cases are exactly `SmallGroup(50,4)`, with 25 covers and
\(|D|=2\), and `SmallGroup(100,11)`, with 25 covers and \(|D|=4\). Every
requested \(A_5,S_5,S_3^3,C_2\times C_3\times S_3\), order-72/108, and
order-48/96 negative case has zero qualifying covers. All nine abstract
subgroup types occurring in \(S_4\) also have zero.

[COMPUTED] Two useful corrections are fixed as regression assertions.
`SmallGroup(36,10)=S_3\times S_3` has 38 six-covers, but none is
irredundant. The audited index-36 witness is instead
`SmallGroup(36,13)=C_2\times((C_3^2):C_2)`, with 72 qualifying covers and
trivial intersection. The finite certificate supplies the enumerative edge
of the reconstructed \(f(6)\) proof; its structural reductions are audited
separately and are not inferred from this computation.

## Exterior-square enumeration at clique cutoff six

[PROVED] The cited-verified six-cover theorem \(f(6)=36\), together with the
repository's irredundant-centralizer bridge, gives
\(\nu(G)=6\Rightarrow [G:Z(G)]\le36\), for finite or infinite \(G\). Thus it is
enough to inspect the 162 isomorphism types of finite central quotients of
order at most 36 and every action-invariant exterior-square kernel.

[PROVED] The exceptional quotient \(Q=C_2^5\) does not require enumeration of
its 229,755,605 exterior-square subspaces. The self-contained alternating-form
argument in `notes/exact_h6.md` proves that every commutator map on
\(\mathbb F_2^5\) with zero radical has a nine-clique: a rank-four scalar form
gives an explicit nine-clique, while the all-rank-two decomposable-subspace
dichotomy gives at least sixteen. An actual quotient \(G/Z(G)\) has zero
commutator radical, so \(C_2^5\) is impossible when \(\nu(G)\le6\).

[COMPUTED] As a redundant check of this structural exclusion, dependency-free
C enumerated all
\({10\brack2}_2=174{,}251\) alternating-form pencils. Exactly 156,240 have
zero common radical, split into 52,080 pencils with nonzero-form rank profile
\((2,4,4)\) and 104,160 with profile \((4,4,4)\). It constructed a nine-clique
for every one in 1,482,030 search nodes, at most 36 per pencil. Independent
Python transvection orbits reproduce the two complete profile sets and exact
representatives \((\omega,\chi)=(11,11)\) and \((9,9)\). Python also enumerates
all 1,892 subspaces whose nonzero forms have rank two; the 31 with zero common
radical form one orbit and have representative \((\omega,\chi)=(17,17)\).

[COMPUTED] GAP 4.16.0 with SmallGrp 1.5.4 scanned every chosen Schur cover for
the other 161 quotients and every one of their 23,527 \(S\)-normal kernels.
The complete serial ranges split into 18,231 graphs with nontrivial
commutator radical, 4,982 faithful graphs carrying a checked seven-clique, and
314 faithful candidate graphs. There are 4,045 distinct faithful adjacency
tuples. Exact clique/coloring certificates for the candidates have distribution

\[
(1,1):1,\quad(3,3):1,\quad(4,4):2,\quad(5,5):93,\quad(6,6):217.
\]

No candidate has chromatic number greater than six. The largest normal-kernel
enumeration is 5,276 for `SmallGroup(32,46)`; six further quotients have 2,825
kernels each. Every radical, clique, coloring, and serial-range certificate is
reparsed by the verification suite.

[PROVED] Combining the preceding exhaustive finite lemma, the structural
\(C_2^5\) exclusion, the cited-verified \(f(6)=36\) bridge, the already exact
value \(h(5)=5\), and the checked Heisenberg witness
\((\nu(H_5),a(H_5))=(6,6)\) yields the following computer-assisted exact
conclusion:

\[
h(6)=6.
\]

The upper bound applies to arbitrary groups because the reduction passes only
to the finite central quotient. The computation is not promoted to a
classification of extensions: enumerating all \(S\)-normal kernels is a safe
overcount.

[DISPROVED] This group refutes
\(a\leq\max\{\nu,2^{\lfloor(\nu-1)/2\rfloor}+1\}\): at \(\nu=7\) the proposed
right side is 9 but the exact cover number is 10.

[COMPUTED] src/verification/test_exact_computation.py independently compares
the optimized clique and coloring routines to naive enumeration for all 33,868
labeled simple graphs on at most six vertices, and also checks group axioms,
coset invariance, named records, direct-product/OR compatibility, witnesses,
and the \(E_m\) symplectic model for \(m=1,2,3\). It also reparses and verifies
every saved Python and GAP certificate. The latest 2026-08-14 run passed all
41 tests in 735.057 seconds under Python 3.9.6 from an isolated archive of
commit `bbb2f41`. The extended tests independently rebuild the
scalar graphs, four residual searches, strongly regular parameters, spreads,
the order-128 prefilter survivors, every exterior-square graph witness, the
eleven cutoff-seven dual searches, all 26,387 ID-261 affine records, and the
disjoint 738-type quotient partition. They also verify the order-144
eight-cover witness, regenerate and check the scalar twisted-tensor bundle,
and audit the class-two linear counterexample and spectral local-drop finite
certificates.
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

[COMPUTED] The cutoff-six exterior run is configured by
experiments/configs/h6_exterior_scan.g (SHA-256
6e65e93760d37fb4afad4722e38aa7ec67dfb1e4bcfb1ed6ea121f3bba92e2f1).
The compact raw TSV SHA-256 is
142224d5416787eadd3e9126f2203b6d0895a5ce2d078713fa8cc87af5ce60a7;
its decimal adjacency bitmasks retain every graph while reducing the raw log
to about 9 MB. The certified JSON, concise analyzer output, and GAP transcript
are `h6_exterior.{json,stdout.txt}` and `h6_exterior_gap.stdout.txt`.

[COMPUTED] The finite maximal-cover audit is configured by
experiments/configs/f6_maximal_cover_audit.g (SHA-256
81674bcbcefa95caa62bf67aa2067b9628c96e2d3179fe6db55696d675185af8).
The class-census and complete multiplication-table TSV SHA-256 values are
18864118296e8d517d7e662edc1e94bcbbacd385cce6ea27645abe68c6acf86f
and 30eec574a216b234dfa20c0fa3d8369788ba5cfa463a8849dfc1ba4219c9ca8e.
The independent verifier is `src/python/analyze_f6_maximal_cover_audit.py`;
the resulting JSON, concise output, and GAP transcript are
`f6_maximal_cover.{json,stdout.txt}` and
`f6_maximal_cover_gap.stdout.txt`.

[COMPUTED] The redundant \(C_2^5\) run is configured by
experiments/configs/h6_c2_5.json (SHA-256
0f9f635bbfed250f50b02a6bde478b3ede0a93bc6e561f382c17aaba71be7b1e).
Its C source SHA-256 is
6e5c6ba2a82a51bef5527443f97778c15b617706a2f04f34daebc789d4626872,
and `h6_c2_5.json` stores both the C exhaustive record and the independent
Python reconstruction.

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

## Cutoff-seven inventory and exact exterior certificates

[COMPUTED] `h7_quotient_inventory.tsv` is a complete 738-row
GAP 4.16.0 / SmallGrp 1.5.4 inventory of every `SmallGroup` quotient of order
at most 81. The dependency-free analyzer validates the SmallGroup serials,
Schur-multiplier invariant factors, and
\(|Q\wedge Q|=|M(Q)|\,|Q'|\). The three exact raw elementary-exterior
explosions are \(C_2^6\) (623,476,476,706,836,148 subspaces), \(C_2^5\), and
\(C_4\times C_2^4\) (229,755,605 each).

[COMPUTED] Four exact chosen-cover batches cover all 471 non-order-64
quotients. Excluding the separately certified \(C_2^5\) and \(C_3^4\) rows,
they inspect 43,368 action-invariant kernels: 32,058 have a nonzero common
radical, 10,993 contain a verified 8-clique, and 317 reach exact optimization.
The latter distribution is
\((1,1):1,(3,3):1,(4,4):2,(5,5):93,(6,6):217,(7,7):3\), with no
\(a>10\) at \(\nu\le7\). The three \((7,7)\) records are the first kernels of
`SmallGroup(8,5)`, `(12,3)`, and `(12,4)`. The order-64 cases omitted from
these ordinary batches are covered by the dedicated certificates below.

[COMPUTED] For \(Q=C_3^4\), all 56,632 alternating-form subspaces were
enumerated. Exactly 55,941 are faithful and form 16 checked coordinate-change
orbits; the unique orbit with \(\nu\le7\) has \((\nu,a)=(7,10)\) and size
234. Zero is isolated and every \(\mathbb F_3^\times\)-line is an independent
twin class, so the 40-point projective graph and 81-vector graph have the same
clique and chromatic numbers. Exact chromatic search and its witness use the
same recorded DSATUR implementation and are not described as an independent
second solver.

[COMPUTED] The \(C_2^6\) rank-six certificate enumerates all 16,383
normalized pencils containing a fixed nondegenerate form. Sixty-three explicit
symplectic transvections give 14 raw-form orbits (including zero and the fixed
form), hence six pencil orbits; exact orbit clique numbers are
\(9,11,12,15,15,15\). Generator transport is checked directly.

[COMPUTED] The complementary rank-four certificate directly checks all 5,471
normalized pencils containing a fixed rank-four form and no rank-six form.
It stores verified 8-cliques for 5,450; the remaining 21 have common radical
exactly equal to the four-element radical of the fixed form. A separately
verified 25-generator stabilizer partitions all 16,383 pencils into 12 orbits,
seven of them covering the 5,471 relevant pencils. Only the two orbits of
sizes 15 and 6 have clique number at most seven, and both are precisely among
the common-radical cases. The passage from these pencil computations to the
full \(C_2^6\) structural conclusion is kept in the structural proof rather
than overclaimed here.

[COMPUTED] A canonical bounded-ID order-64 batch completed and independently
verified `SmallGroup(64,1)` through `(64,191)`: 12,602 kernels split into
8,606 nonfaithful-radical records and 3,996 verified 8-clique records, with
no cutoff-seven candidates. A later exploratory producer exposed a new
`AllSubgroups` bottleneck at `(64,192)=C4 x C4 x C2 x C2`, whose exterior
square has order 128. This shows that exterior order alone is not a safe
enumeration threshold. A dedicated dependency-free producer subsequently
classified all 5,276 subgroups of (C_4\times C_2^5) by their projection to
the (C_4) factor. Exactly 2,925 kernels have nonzero radical; every one of
the 2,351 faithful kernels has a saved and verified 8-clique. Thus this
quotient has no cutoff-seven candidate. The interrupted generic fragment is
not part of any exact aggregate above.

[COMPUTED] A canonical selected-cover census covers all 76
`SmallGroup(64,i)` for \(192\le i\le267\). Each 2-Schur cover is converted
injectively to a pc group; its kernel is checked both central and contained in
the derived subgroup. The image of its center in the quotient has size
distribution \(1:14,2:30,4:32\). For each of the 62 nontrivial-image cases,
the certificate stores at least one nonidentity quotient element together
with all 64 universal exterior commutator coordinates \(q\wedge r\), each
zero. There are 126 such witnesses in total. This is the load-bearing
one-way exterior-zero exclusion; no converse capability assertion is used.
For IDs 262--266, for example, the witness is position 7 with quotient
exponent vector \((0,0,0,0,0,1)\).

[COMPUTED] The eleven remaining regular order-64 IDs
193, 195, 202, 203, 207, 211, 216, 226, 236, 242, and 250 have compact
character-dual certificates. A no-automorphism-quotient BFS enumerates every
action-invariant character subgroup whose union graph has no 8-clique. The
eleven searches retain 5,206 subgroups and prune 24,551 boundary subgroups by
saved verified 8-cliques. Every retained graph has a saved nonidentity
radical; there are no faithful cutoff-seven candidates. The GAP exports also
contain the complete 64-by-64 commutator table, cover conjugation transport,
quotient automorphism permutations, and stem checks. The regression test
freshly rebuilds all eleven searches and compares every saved record.

[COMPUTED] For `SmallGroup(64,261)=C2^3 x D8`, the exterior dual is
\(C_2^9\times C_4\). Exactly 1,152 of 2,048 scalar characters have clique
number at most seven: all 1,024 even characters and an affine 7-space of 128
odd characters. All-even subgroups annihilate a saved nonzero exterior
element on an explicit quotient commutator row. The complete affine RREF
parametrization gives 26,387 odd-containing subgroups: 26,323 have saved
8-cliques and the other 64 have nontrivial radicals, leaving no candidate.
The regression verifier independently reconstructs every saved subgroup and
witness. IDs 192 and 267 are handled by the dedicated
\(C_4^2\times C_2^2\) and \(C_2^6\) certificates above.

[COMPUTED] A global partition assertion derives all 738 inventory keys and
checks the pairwise-disjoint union

\[
660\text{ ordinary}+2\text{ delegated}+62\text{ exterior-zero}
+11\text{ generic dual}+3\text{ special}=738.
\]

Thus the computational quotient inventory has neither an omitted nor a
multiply assigned isomorphism type. The group-theoretic use of this partition
in the exact \(h(7)\) argument is stated separately in `notes/exact_h7.md`.

## Cutoff-eight bounded slice and post-81 feasibility checks

[COMPUTED] The repository-relative certificate
`experiments/logs/h8_bounded_cutoff.json` has SHA-256
`052036975d9a6d30d920873ae8f171dbaa010eec6c7852b3180a918050b0ae61`.
It reuses the checksummed cutoff-seven inventory and saved exports to analyze
all center-quotient graphs with \(|Q|\le81\) at clique cutoff eight. Among
14,989 ordinary boundary rows, representing 12,266 distinct adjacencies,
exact twin-compressed optimization leaves precisely four rows with
\((\omega,\chi)=(8,8)\), for `SmallGroup(14,1)`, `(21,1)`, `(42,1)`, and
`(49,2)` with kernel serial one. Every other distinct ordinary adjacency has
a saved verified nine-clique.

[COMPUTED] A fresh target-nine no-orbit BFS for the eleven generic order-64
dual cases retains all 5,206 invariant character subgroups without a
nine-clique and prunes 24,551 boundary subgroups with saved nine-cliques.
Every retained subgroup has a checked nonidentity radical, hence none is an
exact-center candidate. The dedicated `SmallGroup(64,192)` and `(64,261)`
records have minimum faithful clique numbers 12 and 13. The delegated
\(C_2^5\), \(C_2^6\), \(C_3^4\), and 62 universal exterior-zero records are
bound by their recorded SHA-256 values and independently rechecked. In this
bounded inventory, the maximum cover number at \(\nu\le8\) remains ten and
there is no example with \(a>10\).

[COMPUTED] The original ID-261 cutoff-eight aggregate inherited its scalar
universe from the cutoff-seven certificate.  The dedicated repair artifact
`experiments/logs/h8_sg261_target9_scalar_bridge.json`, SHA-256
`c0686cf7afd668be0f6c61593b963761bf748be97f521cf213d8b063eadf366b`,
now supplies the omitted target-nine completeness bridge.  Its verifier
exact-solves all 2,048 scalar graphs and obtains
\(1^1,3^{155},5^{884},6^{112},11^{448},12^{448}\).  It stores and rechecks a
nine-clique for each of the 896 excluded characters, and proves equality of
three independently rebuilt 1,152-element index sets: the saved
cutoff-seven scalar-good set, the 1,024-even-plus-128-odd affine universe,
and the target-nine scalar-good set.  Their common index-list SHA-256 is
`a20bc2a9d502e1ceabebeb3b9f57bfcb7ad029d13980d15d2a082e2ad893e965`.
The same equality holds at target ten.  Thus the existing 26,387 affine
subgroup parametrization is complete for the cutoff-eight use; this repairs
an evidence link and does not change the mathematical conclusion.

[COMPUTED] The feasibility-only post-81 inventory JSON has SHA-256
`14b10618cb4c1edae5c706420e2eec18d883ddde405057217a7d2bf85daccac3`;
its raw TSV SHA-256 is
`cdc74d7e60f70793b6df40821dd6522f7488306f9737ebe4964adcca6c37c790`.
The named constructions are checked to be `SmallGroup(96,227)`, `(108,41)`,
and `(144,196)`, with exact abstract quotient clique numbers 29, 5, and 10.
The first and third are excluded at cutoff eight because pairwise
noncommuting quotient elements remain pairwise noncommuting under arbitrary
lifts.

[COMPUTED] The complete `(108,41)` scan JSON has SHA-256
`d7b5cb95e07bab5286131316d76d258a3cfd668dee8e1009632f868f094f316e`;
its 84-row raw TSV SHA-256 is
`03287666fc42ddce444754d8d7e1b82e223ff724597fe0a881ab62f52`. Exactly
38 normal kernels have a saved nonfaithful radical. The other 46 are distinct
faithful graphs, with exact clique distribution
\(20^9,28^9,32^{12},37^1,39^1,40^{13},48^1\). Thus the minimum faithful
clique number is 20 and there is no cutoff-eight candidate for this quotient.

[COMPUTED] Every serialized source and input path in the three h8 JSON files
is repository-relative, and every recorded source/input hash is rechecked by
the saved-record verifier. The focused bounded verifier passed in 150.447
seconds and the two post-81 tests passed in 0.303 seconds. A subsequent full
discovery run on 2026-08-14 passed all 28 tests in 382.173 seconds; its exact
command and result are preserved in `experiments/logs/h8_verification.txt`.

[UNVERIFIED] The bounded certificate proves only the exact statement
“center quotients |Q|<=81 only; no global h(8) upper bound.” The three post-81
groups form a literature-motivated feasibility list, not a complete list of
center quotients possible at cutoff eight. No global conclusion about
\(h(8)\) is drawn from these computations.

## Binary rank-three order-64 tail

[COMPUTED] The structural reduction in `notes/structural_reductions.md`,
(SR.12i), forces a hypothetical binary rank-three case to have an order-64
center quotient \(Q\) that is nonabelian, has class at most two,
\(|\Omega_1(Z(Q))|=8\), and
\(Q/\Omega_1(Z(Q))\cong C_2^3\).  The dependency-free verifier evaluates
these predicates on all 267 committed Cayley tables.  The first three select
44 IDs; the elementary quotient condition removes exactly
`17,84,87,103,247`, leaving 39.

[COMPUTED] The verifier joins those 39 to the complete extension artifacts.
They split into 19 ordinary IDs whose faithful records have minimum exact
clique number 12, seven ordinary IDs with no faithful normal kernel, five
generic-dual IDs with no faithful cutoff-nine candidate, and eight IDs with
nonidentity universal exterior-zero witnesses.  The four parts are disjoint
and exhaustive.  No claim that all 39 quotient types are capable is made;
the nonfaithful and exterior-zero parts are precisely where exact center
quotients fail.

[COMPUTED] The canonical test reparses every order-64 table, checks full
associativity, rebuilds the entire dependent cutoff-eight certificate, and
then performs the structural join.  It passed in 150.840 seconds.  The
verifier, test, and transcript SHA-256 values are respectively
`5a4f6f6bf152a495ac9753fd04f15402fe16ef7caef75c39a80b8b18513106be`,
`4d29a897d542e6078a669eac0b3817809e089195f03c17592b4f7f24271058cf`,
and `926765379528a0460763befddb6464e9f668c279ec7c2ef7543793ce750410c7`.
An independent audit obtained the same ID partition and separately verified
all ordinary, generic-frontier, and exterior-zero witnesses used here.

## Local centralizer-index counterexample

[DISPROVED] The proposed local inequality

\[
[G:C_G(x)]\leq\nu(G)-\nu(C_G(x))
\]

fails for `SmallGroup(48,15)`, with GAP structure description
`(C3 x D8) : C2`, and the order-two element `AsList(G)[2]=f1`. The complete
GAP table and independent Python reconstruction give an abelian centralizer
of order four and index 12. Exact clique and coloring witnesses give
\((\nu(G),a(G))=(12,12)\), while the centralizer has
\((\nu(C_G(x)),a(C_G(x)))=(1,1)\). Hence the displayed sides are 12 and 11.

[COMPUTED] The GAP script, raw TSV, analyzed JSON, concise Python output, GAP
progress log, verification transcript, Python producer, regression test, and
explanatory note have SHA-256 values respectively
`ec13967916aa1c3c0d5b602f207a76b51e0839b279052030a54d88b8fda4a4ea`,
`d3826b1d038f91c5415a5b454495bb8f52648590e542a67cacd6ea2285feac8e`,
`a071e4d6ace21968b23a60487093ad76dc5c00678743c7f94bab4147d825ef9b`,
`43f983a19a49032f934b0ccc5fce02dcab93ed70856d513859d0c63e4d674267`,
`737b8871fb0a71164bd7f219bdd4e645b9451574dba67f00a4495a350a835861`,
`48f23aed6cd229b26613c5c661c7402d6b31b9d2b2e3162ee9d81313c019d4ad`,
`e437d1b95c8999d59450785447423519ab09ce70defd681be826cf3ef39db06e`,
`35385c634cbd4ab06fa5c5c5c82971a04fafb32b8c13eb56cff7f40b29b83459`,
and
`7e6718ba7c720a6b29bdfc6c3f6d90d31e1a2e42c77a9aec9e6b882bdeec4f35`.
The exact regeneration and test commands are indexed in
`experiments/configs/README.md` and `src/python/README.md`; the saved test
passed in 0.028 seconds.

[UNVERIFIED] This certificate establishes the stated counterexample only. It
does not establish that order 48 is the least possible counterexample order.

## Finite 5-groups through order \(5^6\) at cutoff eight

[COMPUTED] GAP 4.16.0 / SmallGrp 1.5.4 enumerated all 5, 15, 77, and 684
SmallGroups of orders \(5^3,5^4,5^5,5^6\). A deterministic witness-first
scan partitions the 781 types into 701 groups with a saved nine-clique and 80
full central-coset graphs. A byte-for-byte independent producer rerun took
23.897 seconds and reproduced the complete TSV and GAP progress log.

[COMPUTED] Exact twin-compressed clique and coloring searches give the
following eligible distributions:

\[
\begin{array}{c|c|c|c}
|G|&\#\{\nu\le8\}&\#\{\nu\ge9\}&(\nu,a)\text{ distribution}\cr
125&5&0&(1,1)^3,(6,6)^2\cr
625&11&4&(1,1)^5,(6,6)^6\cr
3125&22&55&(1,1)^7,(6,6)^{15}\cr
15625&42&642&(1,1)^{11},(6,6)^{31}.
\end{array}
\]

Thus the four scanned orders contain no group with \(\nu=8\). Their 80
eligible groups comprise 26 abelian and 54 nonabelian groups; every
nonabelian eligible graph is AC, has center index 25 and twin quotient order
7, and has \((\nu,a)=(6,6)\). No eligible group has \(a>\nu\).

[COMPUTED] Each excluded row stores nine pc exponent vectors and all 36
forward/reverse product vectors; GAP checks the actual group elements
pairwise, while Python checks the saved product-vector inequalities. Python
does not implement a second pc collector, so that part of the certificate
retains an explicit GAP dependency. Every eligible row instead stores the
complete central-coset adjacency, on which Python independently checks
symmetry, twin compression, clique, coloring, and AC witnesses. The saved
regression test passed in 0.096 seconds, and an independent package audit
reported no blocker.

[COMPUTED] The GAP script, raw TSV, analyzed JSON, Python producer, regression
test, and explanatory note have SHA-256 values respectively
`b7201ee828a95a9d26264d7d0fab5d658b945e30dd6bf312ef908afa47f8975f`,
`40490e97f6f4156c608184334d5d975c695cfff682479902f2e39dd518a8aaeb`,
`889713f240cdf73276fd2d398a290558337f4a80737f654b89226d77cac73dfa`,
`9c5115d3eec8d4b22995f6a2108d121c8131cf7101984460f254cc1e11239ed2`,
`88b9b6696e7c62baaa470357556aa8b3b7a878be48285c664dd77fc05ef06cff`,
and
`b3445ae48aafbcccdf054e72777b7ac2b508eeb3d1d892c9873b511738bab401`.
Exact commands and the full manifest are indexed in the configuration,
Python, and log READMEs.

[CITED-VERIFIED] Berkovich (2010), finite scope p. 415, Lemmas 1.2--1.3
pp. 416--417, Theorem 2.3 pp. 419--420, and Theorem 4.4 pp. 424--425 provide
the earlier \(p=5\) pruning.  Proposition 4.5 pp. 425--426 supplies the
additional maximal-member input used by the separate all-orders proof below.

[COMPUTED] This bounded inventory by itself remains an exact census of the
four displayed orders only.  No extrapolation from those 781 SmallGroups is
used in the all-orders proof.

## Small \(\mathbf F _5\) hyperplane covers and all finite \(5\)-groups

[COMPUTED] The dependency-free verifier
`src/verification/verify_f5_small_hyperplane_cover.py` normalizes a
hyperplane cover to contain the coordinate normals and exhausts the
remaining torus masks in dimensions two through four.  The exact census is
\[
\begin{array}{c|r|r|r}
d&\text{subfamilies}&\text{covers}&\text{without a projective line}\\ \hline
2&16&1&0\\
3&122438&87&0\\
4&10626&6&0.
\end{array}
\]
In dimension four it first checks all 152 noncoordinate normals; exactly 24
attain the maximum mask size 16, and cardinality forces any four-member
torus cover to use only those maximizers.  The targeted regression test
rebuilds the enumeration in under one second.

[COMPUTED] A second implementation independently recovered the
dimension-four mask distribution
\(12^{64},13^{64},16^{24}\), all
\(\binom{24}{4}=10626\) candidate quadruples, and the six covers, each
containing exactly one projective line.  A separate structural audit checked
the dual-span normalization, the dimensions-at-least-five union bound, and
the group-theoretic reduction, including duplicate maximal enlargements.

[PROVED] The resulting computer-assisted theorem is not a SmallGroups
extrapolation.  Berkovich Proposition 4.5 forces at least six maximal
members in the eight-centralizer cover.  Maximalizing the other at most two
members and applying the hyperplane certificate gives a six-pencil.  A
genuinely new pencil member is then covered by the common pencil
intersection and at most three proper subgroup intersections, contradicting
the elementary lower bound of six for a proper-subgroup cover of a finite
\(5\)-group.  Therefore finite \(5\)-groups with \(\nu\le8\) have exactly
\((\nu,a)=(1,1)\) or \((6,6)\).

[COMPUTED] The theorem note, verifier, regression test, and saved targeted
transcript have SHA-256 values respectively
`3a0d4f0ab36884b5ad6c28a2a284e569f07f374eabf0c4cea08bafb855ebf650`,
`c7d517132291ef64246ec9c1329065006c73dad6c668f46310281f2f2bc4430c`,
`b16bf07e4302f09bd55713e6a5a9c6919e838993aa2e62cfe94224abecf931c7`,
and
`be8395740edd31494450c250af06a5fbd37889a7cafe187d8da953c494158caa`.

## Finite 3-groups through order \(3^6\) at cutoff eight

[COMPUTED] GAP 4.16.0 / SmallGrp 1.5.4 enumerated all 594 SmallGroups of
orders \(3,9,27,81,243,729\). The exact partition is 502 groups with a saved
nine-clique and 92 groups with a complete eligible central-coset graph. Their
exact distributions by order are

\[
\begin{array}{c|c}
|G|&(\nu,a)\text{ distribution}\cr
3&(1,1)^1\cr
9&(1,1)^2\cr
27&(1,1)^3,(4,4)^2\cr
81&(1,1)^5,(4,4)^6\cr
243&(1,1)^7,(4,4)^{15},(7,10)^2\cr
729&(1,1)^{11},(4,4)^{31},(7,10)^7.
\end{array}
\]

[COMPUTED] No scanned group has \(\nu=8\), and no eligible scanned group has
\(a>10\). The nine non-AC eligible groups are exactly the nine records with
\((\nu,a)=(7,10)\). Every maximum-clique member centralizer in each eligible
nonabelian scanned group has index three.

[COMPUTED] A fresh GAP producer rerun took 6 minutes 8.72 seconds and
reproduced the canonical TSV and progress log byte for byte. The independent
audit separately parsed all 594 rows, checked every one of the 502 saved
nine-cliques, and recomputed every eligible clique/coloring certificate. The
targeted unit test passed in 1.271 seconds after the final wording-only edits.

[COMPUTED] The config, raw TSV, analyzed JSON, analyzer, test, and explanatory
note SHA-256 values are respectively
`138e6479414b6cd6c6610b771125a1e3788f92f7b2a9091f92238a2aaff858bb`,
`d3abec3c9391c0809fd76d0f2a384d0cd3936e258730e4c4dbdc2ee33265782b`,
`f5d7bf5b53d5b981acd774ce4b23f7cd9899a419acfb7753326e3d3060c7fd16`,
`362d1f83d01ddd09fe92af8fe1f18b2c5f45c92862af79417460a71df9b12938`,
`356df635e4426ce4af2bccbf7ac99019bbba61b118f0ef7cabe1c855544b41b3`,
and
`e93f7d7168f630bc2bff3d4ecb1df71a3c8d2f416f7fe43395a3bc8961b92c3e`.

[UNVERIFIED] This certificate stops at order \(3^6\); the installed catalogue
contains 9,310 groups at order \(3^7\). The independent all-orders finite
3-group conclusion is structural and is not inferred from this bounded scan.
