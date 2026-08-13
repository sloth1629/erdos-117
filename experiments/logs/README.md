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
