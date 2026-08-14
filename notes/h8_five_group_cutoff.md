# Finite 5-Groups Through Order \(5^6\) at Cutoff Eight

## Exact bounded scope

`[COMPUTED]` The canonical certificate inspects every GAP SmallGroup of order
\(5^3,5^4,5^5\), and \(5^6\): respectively 5, 15, 77, and 684 isomorphism
types. This is an exact inventory of those four finite orders only. It is not
a classification of all finite 5-groups and gives no global conclusion about
\(h(8)\).

`[PROVED]` Central cosets are independent twin classes in the noncommuting
graph: multiplying either element by a central element does not change
whether the pair commutes. Thus the central-coset graph preserves clique and
chromatic number. Vertices with equal open neighborhoods are again
independent twins, so the second compression used by the Python verifier also
preserves both numbers.

## Results

`[COMPUTED]` The exact cutoff-eight inventory is:

| order | SmallGroups | eligible \(\nu\le8\) | excluded by saved \(K_9\) | exact eligible distribution |
|---:|---:|---:|---:|:---|
| \(5^3=125\) | 5 | 5 | 0 | \((1,1)^3,(6,6)^2\) |
| \(5^4=625\) | 15 | 11 | 4 | \((1,1)^5,(6,6)^6\) |
| \(5^5=3125\) | 77 | 22 | 55 | \((1,1)^7,(6,6)^{15}\) |
| \(5^6=15625\) | 684 | 42 | 642 | \((1,1)^{11},(6,6)^{31}\) |

Here each pair is \((\nu,a)\), and the exponent is the number of groups.
There are 80 eligible groups in total: 26 abelian groups with \((1,1)\) and
54 nonabelian groups with \((6,6)\). Every eligible nonabelian graph has
central quotient order 25, twin quotient order 7, and the graph test verifies
that every noncentral element centralizer is abelian. No scanned group has
\(\nu=8\), and no eligible group has \(a>\nu\).

`[COMPUTED]` For each of the 701 excluded groups, the GAP export saves nine
central-coset representatives in pc exponent coordinates and all 36 forward
and reverse product coordinates. The verifier checks that every corresponding
product pair differs. For each eligible group, GAP saves the complete
central-coset adjacency. Python independently checks symmetry, compresses all
equal-neighborhood twins, computes an exact maximum clique and exact coloring,
and verifies the lifted witnesses on the original central-coset graph.

`[COMPUTED]` The Python verifier does not contain a second implementation of
GAP's pc collector, so it checks the exported forward/reverse product
coordinates rather than deriving those products again from the witness
coordinates. The GAP producer itself checks all witness pairs in the actual
SmallGroup, and a separate canonical rerun reproduced the complete TSV
byte-for-byte. This dependency is explicit rather than described as an
independent pc multiplication check.

## Reproduction

```bash
work/gap-4.16.0/gap -q \
  -c 'ERDOS117_OUTPUT:="experiments/logs/h8_five_group_cutoff.tsv";; ERDOS117_STDOUT_LOG:="experiments/logs/h8_five_group_cutoff_gap.stdout.txt";; Read("experiments/configs/h8_five_group_cutoff.g");'
PYTHONPYCACHEPREFIX=/tmp/erdos117-h8-five-group-pycache \
python3 src/python/analyze_h8_five_group_cutoff.py \
  --input experiments/logs/h8_five_group_cutoff.tsv \
  --gap-script experiments/configs/h8_five_group_cutoff.g \
  --gap-stdout experiments/logs/h8_five_group_cutoff_gap.stdout.txt \
  --output experiments/logs/h8_five_group_cutoff.json \
  --stdout-log experiments/logs/h8_five_group_cutoff.stdout.txt
PYTHONPYCACHEPREFIX=/tmp/erdos117-h8-five-group-test-pycache \
python3 -m unittest src.verification.test_h8_five_group_cutoff -v
```

`[CITED-VERIFIED]` Berkovich (2010) is finite-only (p. 415); Lemmas 1.2--1.3
(pp. 416--417), Theorem 2.3 (pp. 419--420), and Theorem 4.4 (pp. 424--425)
provide external motivation and partial pruning for the \(p=5\) branch. None
of those results is used here to infer an unscanned-order classification from
the four bounded computations above.
