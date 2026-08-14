# Adversarial Review

[DISPROVED] The proposed global closed formula has not survived review.
The separate cutoff-seven theorem \(h(7)=10\), however, has now survived the
independent audit recorded below.

## Workstream D findings

- `[DISPROVED]` Ordinary direct powers are not an exponential-in-\(\nu\) lower-bound mechanism. Treating their OR-product behavior as evidence for the global exponential constant confuses the power parameter with the clique bound.
- `[PROVED]` Chromatic and clique parameters have different direct-power asymptotics: fractional chromatic number versus a complementary Shannon capacity. Any argument assuming one-shot multiplicativity is invalid until separately proved.
- `[UNVERIFIED]` The symplectic \(\mathbb F_2\) construction proves the lower constant \(\sqrt2\), but there is no audited universal upper bound near that constant.
- `[DISPROVED]` The simplest binary-symplectic exact formula fails already for the scalar symplectic group \(S(3,2)\): a complete internal proof and an independent exact computation give \((\nu,a)=(7,10)\).
- `[UNVERIFIED]` Odd-characteristic scalar forms and higher-codomain alternating maps must be searched aggressively; either could defeat the proposed asymptotic constant.
- `[PROVED]` A finite reduction cannot be inferred merely by replacing \(G\) with \(G/Z(G)\). The repository instead constructs a finite group preserving the exact central-coset commutation graph. A finite stem representative remains an unnecessary separate source obligation.
- `[PROVED]` The improved centralizer lemma \(\nu(C_G(x))\leq\nu(G)-2\) was reconstructed independently and gives \(h(n)\leq n h(n-2)\); its algebraic branches were checked explicitly.

- [PROVED] The factorial coset argument was independently reconstructed.
  In an irredundant \(m\)-subgroup cover with intersection \(D\), each
  member contains at most \((m-1)!\) left \(D\)-cosets, so the whole group
  contains at most \(m!\).  Maximum-clique centralizers form such a cover
  with intersection \(Z(G)\).  Thus \([G:Z(G)]\le\nu(G)!\) for arbitrary
  groups, and cutoff eight reduces to center quotients of order at most
  \(40{,}320\).  No maximal-subgroup or finite-group hypothesis is used.

Continue auditing quantifiers, finite/infinite scope, central-coset arguments, product claims, source dependence, and computational certificates.

## Independent audit of the subfactorial upper bound (2026-08-14)

- [CITED-VERIFIED] Guralnick--Maróti, Theorem 1.8, was read in the
  proof-bearing 2011 article.  It applies to arbitrary \(b\)-BFC groups and
  gives \(|G'|<b^{(7+\log_2b)/2}\); the CFSG dependence is explicit.
- [CITED-VERIFIED] Nagy--Pach--Tomon, Theorem 1.11 and its Section 8 proof
  in the 2026 Transactions article, were reconstructed through the
  elementary-abelian and finite-abelian reductions.  The last witness in
  Lemma 5.4 has a harmless subscript typo, and the final
  \(\log\log p\) notation needs a harmless normalization at \(p=2,3\).
  Neither affects the stated \(\exp(O(k\log\log k))\) theorem.
- [PROVED] The repository bridge was independently checked.  With
  \(D=G'\), \(C=C_G(D)\), and \(A=Z(C)\), one has
  \(G/C\hookrightarrow\operatorname{Aut}(D)\), \(C'\le A\), and an
  irredundant centralizer cover of the abelian group \(C/A\).  The map
  \(a\mapsto([a,g_1],\ldots,[a,g_t])\) has kernel exactly \(Z(G)\).
  These give
  \([G:Z(G)]\le2^{O(\nu(G)\log\log\nu(G))}\), and the exact finite model
  transfers the result to arbitrary groups.
- [DISPROVED] The argument does not use the distinct withdrawn
  arXiv:2205.03389 theorem and does not yield a fixed-base exponential
  bound.  Any such interpretation is rejected.

## Independent structural audits at cutoff eight (2026-08-14)

### Binary central layer

- [PROVED] The proof of `notes/structural_reductions.md`, (SR.12), was
  independently reconstructed.  On every three-dimensional binary central
  subspace, the affine-fiber argument was checked separately when the
  internal alternating map has ranks one, two, and three.  Every nonzero
  internal map forces a triangle in each of three mutually joined quotient
  fibers and hence a nine-clique.  Thus the internal map is zero when the
  binary central rank is at least three.
- [PROVED] The sharper charged second-center argument was reconstructed
  independently.  For an arbitrary group \(M\), if
  \(Z(M)\le H\le Z_2(M)\), \(H\) is abelian, and
  \(H/Z(M)\cong C_p^d\), the block-replacement centralizer chain gives
  \(d\le(\nu(M)-\nu(C_M(H)))/p\).  No finiteness of \(M\) is used.  Applied
  after the preceding binary internal-map reduction, this proves
  \(\dim_{\mathbf F_2}\Omega_1(Z(G/Z(G)))\le3\); rank three can occur only
  when the full preimage of this binary layer has abelian centralizer.  The
  exponent-four restriction consequently gives
  \(|Z(G/Z(G))_2|\le2^6\).
- [PROVED] The rank-three equality case was independently reconstructed as
  well.  The exact evaluation space has no rank-two member: weighted
  three-fiber cliques first force any such member to represent a central
  quotient element, and a six-map rank-one tensor argument then gives a
  contradiction.  The evaluation space is therefore the scalar dual of
  the binary layer.  A second charged chain in its abelian self-centralizing
  kernel gives the exact normal form
  \(H/Z(G)\cong G/H\cong C_2^3\), with \(H=C_G(H)\), and hence
  \(|G/Z(G)|=64\).  This conclusion does not use the unproved possibility
  of absorbing the remaining class-three central cocycle by a global
  change of lifts.
- [COMPUTED] The ensuing order-64 tail was independently reconstructed from
  all 267 committed Cayley tables.  The theorem's quotient-level predicates
  select exactly 39 types: 26 ordinary IDs, five generic-dual IDs, and eight
  exterior-zero IDs.  A separate audit recomputed the radicals of all 5,965
  ordinary kernel rows, verified a nine-clique in every one of the 3,488
  faithful rows, checked 226,481 generic invariant-closure frontier steps,
  and reconstructed all 14 relevant nonidentity exterior-zero rows.  The
  frozen regression test independently rebuilds the same dependency chain
  and passed in 150.840 seconds.
- [PROVED] Combining that complete finite tail with (SR.12i) eliminates the
  rank-three equality case.  Hence
  \(\dim_{\mathbf F_2}\Omega_1(Z(G/Z(G)))\le2\),
  \(|Z(G/Z(G))_2|\le16\), and the odd-layer bound gives
  \(|Z(G/Z(G))|\le3{,}600\).  This is a computer-assisted conclusion; it is
  not a determination of \(h(8)\).
- [UNVERIFIED] As a redundant scratch stress check rather than a proof
  dependency, all
  nonzero three-space alternating maps with codomain dimensions one, two,
  and three were enumerated against every evaluation map; none of the
  \(56+4{,}032+261{,}632\) affine fibers was triangle-free.  Exact extension
  graphs in the available SmallGroups scan likewise supplied nine-cliques
  whenever the filtered binary central rank was at least three.  These
  scratch runs are not canonical certificates and are not used in the proof.

### Abelian layers in class-two \(p\)-groups

- [PROVED] The charged centralizer-chain construction in
  `notes/class_two_abelian_layer.md` was reconstructed with the repository's
  commutator convention.  At a chain step of index
  \(q_i=[K_{i-1}:K_i]\), the new fiber really is a \(q_i\)-clique; multiplying
  each old vertex by a separately chosen element of \(K_{i-1}\) preserves
  every old edge and makes every cross edge noncommuting.  The smaller
  subgroup \(K_i\) continues to centralize the enlarged clique.  Therefore
  \(\sum_iq_i\le\nu(P)\), while
  \([A:Z(P)]=\prod_iq_i\le p^{\sum_iq_i/p}\).
- [PROVED] Starting the same invariant with a maximum clique in
  \(H\ge Z(P)\) proves the relative form
  \([Z(H):Z(P)]\le p^{(\nu(P)-\nu(H))/p}\).  This controls the central layer
  but not the complementary index \([P:C_P(x)]\); the note correctly leaves
  that drop-sensitive local bound as [UNVERIFIED].

## Independent cutoff-seven audit (2026-08-14)

### Dependency chain and global coverage

- [CITED-VERIFIED] The cutoff-seven external input is Abdollahi--Jafarian
  Amiri's \(f(7)=81\), Theorem B, printed p. 292 with proof on pp. 299--300.
  Its maximal-case proof uses unarchived GAP 4.3 calculations, so the
  repository correctly does not relabel that historical classification as
  [COMPUTED].
- [PROVED] For an arbitrary group with \(\nu(G)=7\), the repository's
  universal center-index bound first makes \(Q=G/Z(G)\) finite. Maximum-clique
  centralizers then descend to an irredundant seven-cover of this finite
  \(Q\), and Lemma CB.2 makes the cover intersection trivial. Applying the
  cited \(f(7)=81\) theorem inside finite \(Q\) gives \(|Q|\le81\), without
  relying on any unconfirmed infinite-group scope of the source. For
  \(\nu(G)\le6\), the already proved theorem \(h(6)=6\) supplies the separate
  branch; the finite quotient enumeration is not incorrectly applied there.
- [PROVED] The exterior-square bridge was checked in both directions needed
  here. A central extension gives a \(Q\)-equivariant map
  \(Q\wedge Q\to G'\); its kernel determines the compressed noncommuting
  graph, and an exact center quotient has radical exactly \(\{1\}\). A color
  class of central cosets generates, together with \(Z(G)\), an abelian
  subgroup covering all those cosets, while an abelian cover maps to a
  coloring. Thus both \(\nu=\omega\) and \(a=\chi\) are preserved.
- [COMPUTED] The final regression test reconstructs the complete SmallGroups
  inventory and checks the pairwise-disjoint partition

  \[
  660+2+62+11+3=738.
  \]

  These are respectively the ordinary bounded batches, the delegated
  \(C_2^5\) and \(C_3^4\) cases, the explicit exterior-zero exclusions, the
  generic character-dual cases, and IDs \(192,261,267\). Their union equals
  every inventory key. ID 260 occurs only in the 62-type part; its direct
  structural exclusion is a redundant cross-check, not a second count.
- [COMPUTED] I independently reparsed all five bounded batches. Their
  55,970 normal-kernel rows split into 40,664 nonfaithful radicals, 14,989
  saved eight-cliques, and 317 exact candidates. Every hash, serial range,
  radical, clique, and exact candidate certificate verified. The candidate
  distribution is
  \((1,1):1,(3,3):1,(4,4):2,(5,5):93,(6,6):217,(7,7):3\).
- [PROVED] The two ordinary-batch delegations are also complete. Corollary
  H6.2 proves that every zero-radical alternating map for \(C_2^5\) has a
  nine-clique, so this quotient cannot occur at cutoff seven. The separate
  \(C_3^4\) computation therefore covers the only other delegated inventory
  key.
- [COMPUTED] The \(C_3^4\) producer enumerates all 56,632 alternating-form
  subspaces. Its 55,941 faithful cases form 16 checked coordinate-change
  orbits, and the unique cutoff-seven orbit has size 234 and
  \((\omega,\chi)=(7,10)\). The projective compression was checked to
  preserve both invariants because each nonzero scalar line is an independent
  twin class and zero is isolated.

### Character-annihilator calculations

- [PROVED] For finite abelian \(E=Q\wedge Q\), the assignment
  \(K\mapsto K^\perp\) is an inclusion-reversing subgroup bijection, not an
  inclusion-preserving one. It converts the conjugation invariance of \(K\)
  into contragredient invariance of \(L=K^\perp\), and
  \(e\notin K\) exactly when some character of \(L\) is nonzero on \(e\).
  Consequently the graph for \(K\) is the edgewise union of the scalar
  character graphs. These directions agree with both canonical producers.
- [PROVED] The no-orbit generic BFS is exhaustive. If \(H<L\) has already
  been reached inside a target invariant no-eight subgroup \(L\), adjoining
  \(\lambda\in L\setminus H\) and taking invariant closure stays inside
  \(L\). The child therefore contains no scalar-bad character and its union
  graph, being a subgraph of the target graph, cannot meet an eight-clique
  boundary. Iteration reaches every eligible \(L\). Thus scalar and boundary
  pruning cannot remove a target.
- [PROVED] The common-modulus character formula
  \(\sum_i c_i x_i(m/o_i)\pmod m\), and the corresponding pullback division by
  \(m/o_i\), give the full character group of \(\prod_i C_{o_i}\). In
  particular the ID-250 computation genuinely uses \(m=8\) for
  \(C_8\times C_2^5\); it is not an invalid modulus-four reduction.
- [COMPUTED] A fresh reconstruction from all eleven TSV exports reproduced
  the canonical JSON exactly. The search retained 5,206 no-eight invariant
  subgroups and saved 24,551 pruned boundary subgroups. Every retained graph
  has radical size at least four, hence there are zero faithful candidates.
  The targeted unit test repeated all eleven BFS computations and passed in
  68.9 seconds on this audit run.

### The three difficult order-64 cases

- [PROVED] For \(Q=C_2^6\), the structural trichotomy is complete. A
  form space containing a rank-six form is one-dimensional at cutoff seven;
  a rank-four form with no rank-six form contradicts zero common radical by
  the certified pencil dichotomy; and an all-rank-two space either has common
  radical or produces a 32-clique. The sole eligible graph is therefore the
  scalar nondegenerate symplectic graph, with
  \((\omega,\chi)=(7,9)\).
- [COMPUTED] I freshly regenerated both \(C_2^6\) pencil certificates.
  All 16,383 normalized pencils through the fixed rank-six form were checked,
  and all 5,471
  no-rank-six pencils through the fixed rank-four form split as 5,450 saved
  eight-cliques and 21 pencils with the fixed nonzero common radical. The
  orbit totals and exact representative clique values agree with the saved
  certificates.
- [PROVED] The \(C_4^2\times C_2^2\) subgroup parametrization is exhaustive:
  a subgroup of \(C_4\times C_2^5\) has projection \(0\), \(2C_4\), or
  \(C_4\), giving the three displayed \(N\)-and-coset families uniquely.
- [COMPUTED] Fresh generation gave exactly 5,276 such subgroups. Of these,
  2,925 have nonidentity radical and every one of the 2,351 faithful cases
  has a verified eight-clique. Both the producer reconstruction and the
  independent saved-record verifier passed.
- [PROVED] For \(Q=C_2^3\times D_8\), the scalar-good set is exactly the
  disjoint union of 1,024 even characters and an affine odd set \(x+U\) of
  size 128, where \(\dim U=7\) and \(d=2x\in U\setminus\{0\}\). Every
  scalar-good subgroup containing an odd element is uniquely
  \(M\cup(y+M)\), with \(\langle d\rangle\le M\le U\). Passing to
  \(U/\langle d\rangle\cong\mathbb F_2^6\) gives the complete RREF/coset
  count 26,387. All-even subgroups are separately nonfaithful because a
  saved nonidentity quotient vertex has commutator row
  \(\{0,2e_{10}\}\), annihilated by every even character.
- [COMPUTED] A fresh affine reconstruction and a second saved-record pass
  checked all 26,387 subgroups. Exactly 26,323 have verified eight-cliques
  and the remaining 64 have saved nontrivial radicals; there is no faithful
  candidate. All 16 actions are bijective and transport every commutator
  table entry. The targeted regression test passed in 38.8 seconds.

### Exterior-zero exclusions

- [PROVED] The load-bearing statement is deliberately one-way: if
  \(1\ne q\in Q\) has \(q\wedge r=1\) for every \(r\in Q\), then its lift is
  central in every central extension, so \(Q\) cannot be an exact quotient
  by a center. No converse capability theorem or classification is needed.
- [COMPUTED] The strengthened selected-cover export has 76 complete ID
  records, with center-image size distribution \(1:14,2:30,4:32\). The 62
  excluded IDs have 126 nonidentity witnesses; every witness has a nonzero
  quotient pc-exponent vector and a saved 64-entry exterior commutator row
  consisting entirely of zero vectors. The producer also checks the
  lift-to-\(Q\) image and central/stem cover-kernel conditions. The refreshed
  hashes and targeted validator pass.
- [UNVERIFIED] The independent Python side does not implement a second pc
  collector; it validates presentations, orders, exponent ranges, inventory
  agreement, row completeness, and every serialized zero entry, while the
  group operations themselves are reproduced by GAP. The result is properly
  labeled [COMPUTED], not promoted to a computation-free proof. This is a
  residual implementation-independence limitation, not a detected logical or
  coverage gap.

### Finite \(5\)-groups at cutoff eight

- [CITED-VERIFIED] Berkovich Proposition 4.5, printed pp. 425--426, applies
  exactly to an eight-member cover of a finite \(5\)-group: because
  \(7<8<10\), at least six cover members are maximal.  The standing finite
  scope is explicit on p. 415, and the proposition does not assume
  irredundancy.
- [COMPUTED] Two independent reconstructions of
  `verify_f5_small_hyperplane_cover.py` reproduced the normalized
  dimension-two, -three, and -four censuses:
  \(16/122{,}438/10{,}626\) tested subfamilies,
  \(1/87/6\) covers, and zero covers without a six-point projective line.
  The independent dimension-four implementation separately recovered all
  152 noncoordinate normals, the mask-size distribution
  \(12^{64},13^{64},16^{24}\), and all six pencil covers.
- [PROVED] The arbitrary-dimensional hyperplane reduction was reconstructed.
  Once independent normals are normalized to the coordinate points, each
  extra hyperplane covers at most \(4^{d-2}\) of the \(4^{d-1}\) torus
  points.  Thus \(d\ge5\) is impossible, while the exact certificate covers
  \(d=2,3,4\).
- [PROVED] The group bridge remains valid when the two nonmaximal
  centralizers have duplicate maximal enlargements.  Choose a genuinely new
  pencil member \(M\) and source indices for the other five pencil members.
  Their intersections with \(M\) lie in the common pencil intersection
  \(D\); only three original indices remain.  Hence \(M\) is covered by
  \(D\) and at most three proper intersections, impossible for a finite
  \(5\)-group.  No finite \(5\)-group has \(\nu=8\), and the verified
  \(\nu=p+1\) and \(\nu\ne p+2\) results give exactly
  \((\nu,a)=(1,1)\) or \((6,6)\) at cutoff eight.
- [UNVERIFIED] This audit closes only the finite \(5\)-group branch.  It
  supplies no classification of the \(2\)- or \(3\)-group branches and no
  global value of \(h(8)\).

### Verdict

- [COMPUTED] A final independent rerun of all seven cutoff-seven regression
  tests passed in 171.838 seconds. This rerun covered the inventory
  and \(C_3^4\) orbits, all bounded batches and both \(C_2^6\) pencil
  certificates, ID 192, the selected-cover zero rows, the global partition,
  all eleven
  generic-dual searches, and the ID-261 affine reconstruction.  After the
  final serialization-only normalization, the then-complete 25-test suite
  passed in 211.839 seconds.  The later release worktree, including the
  cutoff-eight and local-counterexample additions, followed by the binary
  rank-three order-64 tail, passed all 34 tests in 683.411 seconds.
- [PROVED] Subject to the explicitly identified [CITED-VERIFIED]
  \(f(7)=81\) input and the exact [COMPUTED] certificates above, the case
  split proves \(a(G)\le10\) for every arbitrary group with
  \(\nu(G)\le7\). The independently proved group \(S(3,2)\), with
  \((\nu,a)=(7,10)\), supplies the reverse inequality. Hence the audited
  conclusion is \(h(7)=10\).
- [UNVERIFIED] No blocking mathematical, direction-of-duality,
  faithfulness, action-invariance, enumeration-completeness, or global
  coverage defect was found. This statement records the scope of the audit,
  not a claim that arbitrary future implementation changes are defect-free.
