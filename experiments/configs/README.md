# Experiment configurations

Version all search parameters and solver settings here.

- `exact_small_groups.json`: deterministic list of explicit groups.  The
  `independent_cover` flag requests exhaustive enumeration of maximal abelian
  subgroups in addition to the exact graph coloring.  It is disabled for `E3`
  because its graph certificate and generated subgroup cover already provide a
  compact reproducible record, while exhaustive subgroup enumeration is not
  needed for this bootstrap run.
- `graph_products.json`: one compressed group-graph OR product and the general
  graph warning example `C5 OR C5`.
- `gap_export.g`: GAP/SmallGrp exporter. It emits group identifiers, structure
  descriptions, and complete multiplication tables; all graph and cover
  calculations are subsequently rerun by the Python implementation.
- `scalar_symplectic.json`: exact scalar-symplectic extraspecial-group records;
  currently the decisive prime-3 rank-2 instance.
- `scalar_symplectic_clique.json`: saved clique witnesses and exact
  symmetry-reduced upper searches for the prime-5 rank-2 and prime-3 rank-3
  instances.
- `scalar_symplectic_bounds.json`: saved constructive clique for the
  rigorously bounded prime-7 rank-2 case.
- `gap_small_n_export.g`: configurable SmallGroups central-coset graph
  prefilter for a rigorous bounded scan by clique cutoff.
- `h5_exterior_scan.g`: Schur-cover/exterior-square enumeration of every
  action-invariant commutator kernel for all quotient groups through the
  configured order bound; used at order 16 for the computer-assisted
  \(h(5)=5\) result.
- `h6_c2_5.json`: expected pencil, rank-profile, and clique counts for the
  alternating-form certificate that excludes \(C_2^5\) at clique cutoff six.
- `h6_exterior_scan.g`: complete chosen-Schur-cover scan through quotient
  order 36, with the structurally excluded \(C_2^5\) represented by one
  explicit special row rather than 229,755,605 exterior subspaces.
- `f6_maximal_cover_audit.g`: modern GAP reconstruction of the finite
  maximal irredundant core-free six-cover assertions used at the \(f(6)=36\)
  edge. It exports complete multiplication tables and exact maximal-subgroup
  masks for an independent Python verifier, avoiding the dissertation's
  inconsistent subgroup labels.
- `h7_quotient_inventory.g`: a Schur-multiplier census of all 738
  `SmallGroup` quotients of order at most 81. It does not construct Schur
  covers or enumerate exterior-square kernels.
- `h7_exterior_scan.g`: resumable chosen-Schur-cover kernel producer at clique
  cutoff seven. Start/end orders, optional start/end SmallGroup IDs, and every
  delegated quotient are explicit metadata; exclusions are emitted as rows,
  never silently skipped.
- `h7_capability_order64.g`: bounded-ID selected-cover center-image census for
  order-64 quotients. It checks an injective pc conversion of the selected
  2-Schur cover, its stem kernel, full quotient/cover pc presentations, and a
  complete 64-entry exterior commutator row for every exported central lift.
  The canonical analyzer uses the nonidentity zero rows only in the one-way
  exclusion direction.
- `h7_order64_dual_export.g`: compact character-dual exporter for the eleven
  regular order-64 cases left after the exterior-zero exclusions. It exports
  full quotient exponents and commutators, cover-conjugation actions, quotient
  automorphism generators, and central/stem checks.
- `h7_c2_3_d8_export.g`: dedicated affine-dual exporter for
  `SmallGroup(64,261)=C2^3 x D8`, including the complete commutator table and
  every cover-conjugation action needed to verify invariant annihilators.
- `h8_literature_candidate_inventory.g`: `[COMPUTED]` feasibility-only
  Schur-cover/exterior inventory for the three literature-motivated post-81
  quotients `SmallGroup(96,227)`, `(108,41)`, and `(144,196)`. It exports
  each complete quotient noncommuting adjacency, named-construction check,
  multiplier/exterior orders, and normal-kernel count; it is not a complete
  cutoff-eight quotient inventory.
- `h8_sg108_exterior_scan.g`: `[COMPUTED]` complete raw scan of the 84
  normal exterior kernels for the single quotient `SmallGroup(108,41)`. It
  records every full adjacency together with either a nonfaithful radical or
  a nine-clique witness. It makes no global claim about \(h(8)\).

For a bounded cutoff-seven batch, set the GAP variables and then run the
generic analyzer. For example, the independently audited 37--63 batch is:

```bash
work/gap-4.16.0/gap -q \
  -c 'ERDOS117_OUTPUT:="experiments/logs/h7_exterior_37_63.tsv";; ERDOS117_STDOUT_LOG:="experiments/logs/h7_exterior_37_63_gap.stdout.txt";; ERDOS117_START_Q_ORDER:=37;; ERDOS117_END_Q_ORDER:=63;; ERDOS117_EXCLUDED_QUOTIENTS:=[];; Read("experiments/configs/h7_exterior_scan.g");'
python3 src/python/analyze_h7_exterior_batch.py \
  --input experiments/logs/h7_exterior_37_63.tsv \
  --gap-script experiments/configs/h7_exterior_scan.g \
  --inventory experiments/logs/h7_quotient_inventory.json \
  --gap-stdout experiments/logs/h7_exterior_37_63_gap.stdout.txt \
  --start-order 37 --end-order 63 \
  --output experiments/logs/h7_exterior_37_63.json \
  --stdout-log experiments/logs/h7_exterior_37_63.stdout.txt
```

The two post-81 GAP exports are regenerated from the repository root by:

```bash
work/gap-4.16.0/gap -q \
  -c 'ERDOS117_OUTPUT:="experiments/logs/h8_literature_candidate_inventory.tsv";; ERDOS117_STDOUT_LOG:="experiments/logs/h8_literature_candidate_inventory_gap.stdout.txt";; Read("experiments/configs/h8_literature_candidate_inventory.g");'
work/gap-4.16.0/gap -q \
  -c 'ERDOS117_OUTPUT:="experiments/logs/h8_sg108_exterior_scan.tsv";; ERDOS117_STDOUT_LOG:="experiments/logs/h8_sg108_exterior_scan_gap.stdout.txt";; Read("experiments/configs/h8_sg108_exterior_scan.g");'
```

`[UNVERIFIED]` These two configurations dispose only of the three named
post-81 candidates; they do not prove that those candidates exhaust the
possible center quotients at clique cutoff eight.
