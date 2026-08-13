# Python exact computation

The bootstrap implementation uses only the Python standard library.

- `finite_groups.py` constructs and validates explicit multiplication-table
  groups (`C_n`, `S_n`, `D_{2n}`, `Q8`, `Heis(p)`, extraspecial `E_m`, and
  direct products).
- `exact_invariants.py` checks central-coset commutation invariance, constructs
  the compressed noncommuting graph, and exactly computes maximum cliques,
  chromatic numbers, and minimum covers by abelian subgroups.  It emits both
  graph certificates and independently enumerated subgroup-cover certificates
  for configured small instances.
- `run_exact_experiments.py` consumes a deterministic JSON configuration and
  writes machine-readable witnesses and the group-invariant CSV.
- `run_graph_product_experiments.py` records exact clique/coloring certificates
  for configured disjunctive (OR) graph products.
- `analyze_gap_export.py` validates GAP/SmallGrp multiplication-table exports
  and recomputes all invariants with the dependency-free certificate pipeline.
  Its `--omit-multiplication-tables` option leaves large tables only in the
  checksummed TSV while retaining complete graph and subgroup-cover
  certificates in JSON.
- `scalar_symplectic.py` constructs the general prime-field extraspecial group
  and scalar symplectic graph, finite-field isotropic spreads, projective twin
  compression, and a second include/exclude clique decision certificate.
- `run_scalar_symplectic_experiments.py` writes the redundant witnesses used
  for the prime-3 rank-2 record.

From the repository root:

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/run_exact_experiments.py \
  --config experiments/configs/exact_small_groups.json \
  --output experiments/logs/exact_small_groups.json \
  --group-csv results/group_invariants.csv
```

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/run_graph_product_experiments.py \
  --config experiments/configs/graph_products.json \
  --output experiments/logs/graph_products.json
```

For the complete order-64 SmallGroups scan after running `gap_export.g`:

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/analyze_gap_export.py \
  --input experiments/logs/gap_smallgroups_order64.tsv \
  --output experiments/logs/gap_smallgroups_order64.json \
  --omit-multiplication-tables
```

For the scalar-symplectic record:

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/run_scalar_symplectic_experiments.py \
  --config experiments/configs/scalar_symplectic.json \
  --output experiments/logs/scalar_symplectic_p3_m2.json
```
