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
- `run_scalar_symplectic_clique.py` compiles the dependency-free C clique
  solver, checks its four symmetry-reduced upper searches, and independently
  verifies saved clique and spread witnesses for the prime-5 rank-2 and
  prime-3 rank-3 records.
- `run_scalar_symplectic_bounds.py` verifies constructive cliques, strongly
  regular/Delsarte upper bounds, and isotropic spreads for rigorously bounded
  cases such as prime 7, rank 2.
- `analyze_gap_small_n.py` exactly verifies clique/coloring certificates in a
  central-coset graph prefilter export such as the order-128, \(\nu\leq6\)
  scan.
- `analyze_h5_exterior_scan.py` verifies every graph and kernel serial range
  in the Schur-cover/exterior-square export used for the computer-assisted
  \(h(5)=5\) conclusion.
- `h6_c2_5.py` and `run_h6_c2_5.py` give independent alternating-form orbit,
  rank-two-subspace, and C exhaustive checks for the exceptional central
  quotient \(C_2^5\).
- `analyze_h6_exterior_scan.py` verifies all normal-kernel serial ranges,
  radical exclusions, seven-clique exclusions, and exact surviving
  clique/coloring witnesses for every other SmallGroup quotient of order at
  most 36.
- `analyze_f6_maximal_cover_audit.py` reparses GAP multiplication tables,
  independently enumerates every subgroup and maximal subgroup, and exhausts
  every six-subset to recheck cover, private-element irredundancy, intersection,
  and corefreeness for the finite \(f(6)\) audit.

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

To regenerate a SmallGroups export from the locally built GAP 4.16.0 bundle,
use this template from the repository root, substituting N=8, 32, or 64:

    work/gap-4.16.0/gap -l 'work/gap-4.16.0;' -q \
      -c 'ERDOS117_ORDER:=N;; ERDOS117_OUTPUT:="experiments/logs/gap_smallgroups_orderN.tsv";; Read("experiments/configs/gap_export.g");'

Then run the analyzer shown above with matching input and output names. Use
the omit-multiplication-tables option for order 64; omit it for orders 8 and
32 if duplicate tables in JSON are desired.

For the scalar-symplectic record:

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/run_scalar_symplectic_experiments.py \
  --config experiments/configs/scalar_symplectic.json \
  --output experiments/logs/scalar_symplectic_p3_m2.json
```

For the extended symmetry-reduced certificates (requires an ISO C11 compiler
but no third-party library):

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/run_scalar_symplectic_clique.py \
  --config experiments/configs/scalar_symplectic_clique.json \
  --output experiments/logs/scalar_symplectic_extended.json \
  --stdout-log experiments/logs/scalar_symplectic_extended.stdout.txt
```

For the rigorous larger-case interval:

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/run_scalar_symplectic_bounds.py \
  --config experiments/configs/scalar_symplectic_bounds.json \
  --output experiments/logs/scalar_symplectic_bounds.json \
  --stdout-log experiments/logs/scalar_symplectic_bounds.stdout.txt
```

For the order-128 cutoff scan, first generate the GAP prefilter export:

```bash
work/gap-4.16.0/gap -l 'work/gap-4.16.0;' -q \
  -c 'ERDOS117_ORDER:=128;; ERDOS117_CLIQUE_CUTOFF:=6;; ERDOS117_OUTPUT:="experiments/logs/gap_smallgroups_order128_nu_le6.tsv";; Read("experiments/configs/gap_small_n_export.g");'
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/analyze_gap_small_n.py \
  --input experiments/logs/gap_smallgroups_order128_nu_le6.tsv \
  --output experiments/logs/gap_smallgroups_order128_nu_le6.json \
  --order 128 --total-groups 2328 --clique-cutoff 6
```

For the exterior-square cutoff-five certificate:

```bash
work/gap-4.16.0/gap -l 'work/gap-4.16.0;' -q \
  -c 'ERDOS117_MAX_Q_ORDER:=16;; ERDOS117_OUTPUT:="experiments/logs/h5_exterior.tsv";; Read("experiments/configs/h5_exterior_scan.g");'
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/analyze_h5_exterior_scan.py \
  --input experiments/logs/h5_exterior.tsv \
  --gap-script experiments/configs/h5_exterior_scan.g \
  --output experiments/logs/h5_exterior.json \
  --stdout-log experiments/logs/h5_exterior.stdout.txt \
  --clique-cutoff 5
```

For the cutoff-six certificate, first run the separate \(C_2^5\) check, then
the GAP enumeration of all other quotients, and finally the exact analyzer:

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/run_h6_c2_5.py \
  --config experiments/configs/h6_c2_5.json \
  --output experiments/logs/h6_c2_5.json \
  --stdout-log experiments/logs/h6_c2_5.stdout.txt
work/gap-4.16.0/gap -q -b \
  -c 'ERDOS117_OUTPUT:="experiments/logs/h6_exterior.tsv";; ERDOS117_STDOUT_LOG:="experiments/logs/h6_exterior_gap.stdout.txt";; ERDOS117_MAX_Q_ORDER:=36;; Read("experiments/configs/h6_exterior_scan.g");'
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/analyze_h6_exterior_scan.py \
  --input experiments/logs/h6_exterior.tsv \
  --gap-script experiments/configs/h6_exterior_scan.g \
  --c2-5-certificate experiments/logs/h6_c2_5.json \
  --output experiments/logs/h6_exterior.json \
  --stdout-log experiments/logs/h6_exterior.stdout.txt
```

For the finite maximal-cover audit used in the reconstructed \(f(6)=36\)
argument:

```bash
work/gap-4.16.0/gap -q \
  -c 'ERDOS117_CLASS_OUTPUT:="experiments/logs/f6_maximal_cover_classes.tsv";; ERDOS117_COVER_OUTPUT:="experiments/logs/f6_maximal_cover_groups.tsv";; ERDOS117_STDOUT_LOG:="experiments/logs/f6_maximal_cover_gap.stdout.txt";; Read("experiments/configs/f6_maximal_cover_audit.g");'
PYTHONPYCACHEPREFIX=/tmp/erdos117-pycache \
python3 src/python/analyze_f6_maximal_cover_audit.py \
  --classes experiments/logs/f6_maximal_cover_classes.tsv \
  --groups experiments/logs/f6_maximal_cover_groups.tsv \
  --gap-script experiments/configs/f6_maximal_cover_audit.g \
  --gap-stdout experiments/logs/f6_maximal_cover_gap.stdout.txt \
  --output experiments/logs/f6_maximal_cover.json \
  --stdout-log experiments/logs/f6_maximal_cover.stdout.txt
```
