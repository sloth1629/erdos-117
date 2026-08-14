# Experiment logs

Store reproducible text logs here; large or licensed artifacts must not be committed without review.

- `exact_small_groups.json`: self-contained multiplication tables, compressed
  adjacency lists, optimal clique/coloring witnesses, generated abelian covers,
  optional independent maximal-abelian set-cover witnesses, search-node counts,
  software version, and configuration digest.
- `exact_small_groups.stdout.txt`: captured concise stdout from the canonical
  run.
- `verification.txt`: captured test command, Python version, and test result.
- `graph_products.json` and `graph_products.stdout.txt`: exact factor/product
  invariants and graph certificates for the configured OR-product checks.
- `gap_smallgroups_order8.*`, `gap_smallgroups_order32.*`, and
  `gap_smallgroups_order64.*`: GAP 4.16.0 / SmallGrp 1.5.4 table exports,
  Python certificates, and captured output for all isomorphism classes of the
  indicated order. For order 64 the checksummed TSV remains the canonical
  multiplication-table source and the JSON omits duplicate tables, reducing
  the certificate log from about 17 MB to about 2.1 MB.
- `scalar_symplectic_p3_m2.json` and its stdout capture: the order-243 group,
  81-vertex compressed graph, exact clique/coloring records, independent
  projective 8-clique exclusion, finite-field spread, and two abelian-cover
  witnesses.
- `scalar_symplectic_extended.json` and stdout: explicit projective clique
  witnesses, four exact symmetry-reduced residual searches per group, and
  independently checked isotropic spreads for \((p,m)=(5,2)\) and \((3,3)\).
- `scalar_symplectic_bounds.json` and stdout: a checked 33-clique, checked
  strongly regular parameters and Delsarte upper bound 50, and a 50-member
  spread for \((p,m)=(7,2)\).
- `gap_smallgroups_order128_nu_le6.{tsv,json}` and stdout: all 418 survivors
  of a rigorous all-2,328-group greedy-clique prefilter, with exact clique and
  coloring witnesses through clique cutoff 6.
- `h5_exterior.tsv`, `.json`, the concise stdout, and the GAP transcript:
  all 2,986 action-invariant exterior-square kernel records for the 42
  SmallGroups of order at most 16, including complete kernel serial ranges and
  exact clique/coloring witnesses.
- `h6_c2_5.json` and stdout: exhaustive C witnesses for all 156,240
  common-radical-zero alternating-form pencils on \(\mathbb F_2^5\), plus an
  independent Python transvection-orbit and rank-two-subspace reconstruction.
- `h6_exterior.tsv`, `.json`, the concise stdout, and the GAP transcript:
  23,527 action-invariant exterior-square kernels for 161 quotient groups and
  one special \(C_2^5\) row, covering all 162 SmallGroups of order at most 36.
  Decimal adjacency bitmasks keep the canonical raw export near 9 MB. The
  analyzer verifies 18,231 nonfaithful-radical exclusions, 4,982 seven-clique
  exclusions, and 314 exact survivors.
- `f6_maximal_cover_classes.tsv` and `f6_maximal_cover_groups.tsv`: the
  complete ambient subgroup-class census and multiplication-table/maximal-mask
  export for the bounded \(f(6)\) audit. The paired JSON and concise stdout
  record an independent Python reconstruction of all 5,257 subgroups, all
  maximal subgroups, and all 5,545,351 six-subsets across 48 isomorphism
  types. The GAP transcript is `f6_maximal_cover_gap.stdout.txt`.
- `h7_quotient_inventory.{tsv,json}` and stdout: complete, pure inventory of
  all 738 SmallGroups of order at most 81. The certificate identifies the
  three raw elementary-exterior explosions and contains no dependency on
  partial deep-scan fragments.
- `h7_exterior_1_36`, `h7_exterior_37_63`, `h7_exterior_65_80`, and
  `h7_exterior_81`: exact bounded batches covering every non-order-64 quotient.
  They contain 43,368 scanned kernel rows: 32,058 nonfaithful radicals, 10,993
  verified 8-cliques, and 317 exact candidates. The delegated rows are
  \(C_2^5\) and \(C_3^4\), with checksummed certificate pointers in the JSON.
- `h7_exterior_64_1_191`: canonical bounded-ID order-64 batch with 12,602
  kernels (8,606 nonfaithful radicals and 3,996 verified 8-cliques), no exact
  cutoff-seven candidates, and explicit `END_Q_ID=191` metadata.
- `h7_c3_4.json` and stdout: all 56,632 subspaces of
  \(\operatorname{Alt}(4,3)\), of which the 55,941 faithful subspaces form 16
  coordinate-change orbits. The only cutoff-seven orbit has
  \((\nu,a)=(7,10)\). Zero is isolated and each nonzero scalar line is an
  independent twin class, so the 40-point projective graph preserves clique
  and chromatic numbers from the 81-vector graph.
- `h7_c2_6_rank6_pencils.json` and `h7_c2_6_rank4_pencils.json`: exhaustive
  normalized-pencil certificates used in the structural \(C_2^6\) reduction.
  The first has six exact symplectic pencil orbits and minimum clique number 9.
  The second directly checks all 5,471 no-rank-six pencils, storing 5,450
  8-cliques and 21 exact common-radical witnesses; its 12-orbit stabilizer
  table is a supplementary cross-check.
- `h7_c4_2_c2_2.json` and stdout: dependency-free exact exterior-kernel
  certificate for `SmallGroup(64,192)`. The three-case projection
  classification lists all 5,276 subgroups of (C_4\times C_2^5) once;
  2,925 have nonzero radical, and all 2,351 faithful kernels have saved,
  verified 8-cliques. Hence there is no cutoff-seven candidate for this
  quotient.
- `h7_capability_192_260.tsv` and `h7_capability_261_267.tsv`, their GAP
  transcripts, and `h7_capability_order64.json`: exact selected-cover
  center-image census for all 76 order-64 IDs from 192 through 267. The image
  sizes have distribution (1:14,2:30,4:32). For the 62 nontrivial-image IDs,
  126 saved nonidentity witnesses each include quotient/lift pc exponents and
  a complete 64-entry universal exterior commutator row, verified identically
  zero. These rows support the one-way exterior-zero exclusions; the artifact
  does not use a converse capability assertion.
- `h7_order64_dual_*.tsv`, their GAP transcripts, and
  `h7_order64_dual.json`: compact exact character-dual certificates for IDs
  193, 195, 202, 203, 207, 211, 216, 226, 236, 242, and 250. A transparent
  no-orbit BFS retains all 5,206 invariant subgroups without an 8-clique and
  prunes 24,551 boundary subgroups with saved 8-cliques. Every retained graph
  has a nonidentity radical, so there are no faithful candidates.
- `h7_c2_3_d8.{tsv,json}`, its GAP transcript, and concise stdout: dedicated
  affine-dual certificate for `SmallGroup(64,261)`. It classifies all 2,047
  nonzero scalar characters and all 26,387 odd-containing invariant
  annihilators; 26,323 have a saved 8-clique and 64 have a saved nontrivial
  radical. The all-even case has a separate explicit commutator-row
  obstruction.
- `h8_bounded_cutoff.json` and stdout: `[COMPUTED]` canonical cutoff-eight
  reanalysis of the already certified 738 quotient types with \(|Q|\le81\).
  Its SHA-256 is
  `052036975d9a6d30d920873ae8f171dbaa010eec6c7852b3180a918050b0ae61`.
  The exact scope string is “center quotients |Q|<=81 only; no global h(8)
  upper bound.”
- `h8_literature_candidate_inventory.{tsv,json}` and the two stdout files:
  `[COMPUTED]` feasibility-only records for the three named post-81
  quotients. The raw TSV and analyzed JSON SHA-256 values are respectively
  `cdc74d7e60f70793b6df40821dd6522f7488306f9737ebe4964adcca6c37c790`
  and
  `14b10618cb4c1edae5c706420e2eec18d883ddde405057217a7d2bf85daccac3`.
- `h8_sg108_exterior_scan.{tsv,json}` and the two stdout files:
  `[COMPUTED]` complete normal-kernel scan for `SmallGroup(108,41)`. The raw
  TSV and analyzed JSON SHA-256 values are respectively
  `03287666fc42ddce444754d8d7e1b82e223ff724597fe0a881ab62f52` and
  `d7b5cb95e07bab5286131316d76d258a3cfd668dee8e1009632f868f094f316e`.
- `h8_verification.txt`: `[COMPUTED]` focused saved-record tests and the full
  28-test discovery run, including exact commands and timings.
- `rank3_order64_tail_verification.txt`: `[COMPUTED]` independent join of the
  cutoff-eight binary rank-three normal form with the complete order-64
  certificates.  The verifier derives 44 base and 39 theorem-forced quotient
  IDs directly from all 267 committed Cayley tables, then partitions the 39
  into 19 ordinary faithful cases of exact clique number at least 12, seven
  all-nonfaithful cases, five generic dual searches with no faithful candidate,
  and eight exterior-zero exclusions.  The canonical command is
  `PYTHONPYCACHEPREFIX=/tmp/erdos117-rank3-tail-pycache python3 -m unittest
  src.verification.test_rank3_order64_tail -v`; the saved run passed in
  150.840 seconds.  The verifier, test, and transcript SHA-256 values are
  respectively `5a4f6f6bf152a495ac9753fd04f15402fe16ef7caef75c39a80b8b18513106be`,
  `4d29a897d542e6078a669eac0b3817809e089195f03c17592b4f7f24271058cf`,
  and `926765379528a0460763befddb6464e9f668c279ec7c2ef7543793ce750410c7`.
- `h8_local_inequality_counterexample.{tsv,json}` and its stdout,
  GAP-transcript, and verification files: `[DISPROVED]` exact
  `SmallGroup(48,15)` counterexample to
  \([G:C_G(x)]\leq\nu(G)-\nu(C_G(x))\). The record contains the complete
  multiplication table, independently reconstructed centralizer, exact
  12-clique, and proper 12-coloring. `[UNVERIFIED]` It makes no least-order
  or minimal-counterexample claim. The complete current SHA-256 manifest is:

  ```text
  ec13967916aa1c3c0d5b602f207a76b51e0839b279052030a54d88b8fda4a4ea  experiments/configs/h8_local_inequality_counterexample.g
  d3826b1d038f91c5415a5b454495bb8f52648590e542a67cacd6ea2285feac8e  experiments/logs/h8_local_inequality_counterexample.tsv
  a071e4d6ace21968b23a60487093ad76dc5c00678743c7f94bab4147d825ef9b  experiments/logs/h8_local_inequality_counterexample.json
  43f983a19a49032f934b0ccc5fce02dcab93ed70856d513859d0c63e4d674267  experiments/logs/h8_local_inequality_counterexample.stdout.txt
  737b8871fb0a71164bd7f219bdd4e645b9451574dba67f00a4495a350a835861  experiments/logs/h8_local_inequality_counterexample_gap.stdout.txt
  48f23aed6cd229b26613c5c661c7402d6b31b9d2b2e3162ee9d81313c019d4ad  experiments/logs/h8_local_inequality_counterexample_verification.txt
  e437d1b95c8999d59450785447423519ab09ce70defd681be826cf3ef39db06e  src/python/analyze_h8_local_inequality_counterexample.py
  35385c634cbd4ab06fa5c5c5c82971a04fafb32b8c13eb56cff7f40b29b83459  src/verification/test_h8_local_inequality_counterexample.py
  7e6718ba7c720a6b29bdfc6c3f6d90d31e1a2e42c77a9aec9e6b882bdeec4f35  notes/h8_local_inequality_counterexample.md
  ```
- `h8_five_group_cutoff.{tsv,json}`, stdout files, and verification
  transcript: `[COMPUTED]` exact cutoff-eight inventory of all 781
  SmallGroups of orders \(5^3\) through \(5^6\). The raw record stores 701
  nine-clique exclusions and 80 complete candidate adjacencies. No candidate
  has \(\nu=8\); the exact eligible values are only \((1,1)\) and \((6,6)\).
  `[UNVERIFIED]` No unscanned-order classification is claimed. The current
  SHA-256 manifest is:

  ```text
  b7201ee828a95a9d26264d7d0fab5d658b945e30dd6bf312ef908afa47f8975f  experiments/configs/h8_five_group_cutoff.g
  40490e97f6f4156c608184334d5d975c695cfff682479902f2e39dd518a8aaeb  experiments/logs/h8_five_group_cutoff.tsv
  7cd05a480c05e7096ac3116b6fa13fbb2a371030d53c5a5828251068ce5476ae  experiments/logs/h8_five_group_cutoff_gap.stdout.txt
  889713f240cdf73276fd2d398a290558337f4a80737f654b89226d77cac73dfa  experiments/logs/h8_five_group_cutoff.json
  5caec96ef98b4b76f55108256a83808745779aaeecdaeecec9eb464eddcb4e92  experiments/logs/h8_five_group_cutoff.stdout.txt
  cba329928eff08de400ef375f4e59354c04be13553106c3b5a4848e754f07799  experiments/logs/h8_five_group_cutoff_verification.txt
  9c5115d3eec8d4b22995f6a2108d121c8131cf7101984460f254cc1e11239ed2  src/python/analyze_h8_five_group_cutoff.py
  88b9b6696e7c62baaa470357556aa8b3b7a878be48285c664dd77fc05ef06cff  src/verification/test_h8_five_group_cutoff.py
  b3445ae48aafbcccdf054e72777b7ac2b508eeb3d1d892c9873b511738bab401  notes/h8_five_group_cutoff.md
  ```

The unit suite checks that the five disjoint families--660 ordinary scans,
two delegated cases, 62 exterior-zero exclusions, eleven generic dual cases,
and three special cases--are exactly the 738 inventory keys. The interrupted
43 MB exploratory regular scan is preserved under ignored `work/` and is not
a canonical log.
