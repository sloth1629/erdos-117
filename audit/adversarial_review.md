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

Continue auditing quantifiers, finite/infinite scope, central-coset arguments, product claims, source dependence, and computational certificates.

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

### Verdict

- [COMPUTED] A final independent rerun of all seven cutoff-seven regression
  tests passed in 171.838 seconds. This rerun covered the inventory
  and \(C_3^4\) orbits, all bounded batches and both \(C_2^6\) pencil
  certificates, ID 192, the selected-cover zero rows, the global partition,
  all eleven
  generic-dual searches, and the ID-261 affine reconstruction.  After the
  final serialization-only normalization, the complete 25-test suite was
  rerun on the release worktree and passed in 211.839 seconds.
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
