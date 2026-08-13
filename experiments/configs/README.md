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
