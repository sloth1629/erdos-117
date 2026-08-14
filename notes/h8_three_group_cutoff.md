# Finite 3-Groups Through Order 729 at Cutoff Eight

## Exact bounded scope

[COMPUTED] The canonical certificate inspects every GAP SmallGroup of order
\(3,9,27,81,243,\) and \(729\): respectively \(1,2,5,15,67,\) and \(504\)
isomorphism types, hence 594 groups in total. This is an exact inventory of
those six finite orders only. It is not a theorem about all finite 3-groups.

[COMPUTED] The installed SmallGrp catalogue reports 9,310 groups at the next
order \(3^7=2187\). That order is explicitly not scanned by this certificate.

[PROVED] Multiplying either element by a central element does not change
whether a pair commutes. Consequently, central cosets are independent twin
classes in the noncommuting graph and the central-coset graph preserves clique
and chromatic number. Equal open-neighborhood vertices in the compressed graph
are again independent twins, so the Python verifier's second compression also
preserves both invariants.

[PROVED] A proper color class is a pairwise commuting set, and the subgroup it
generates is abelian. Conversely, each abelian subgroup is an independent set
in the noncommuting graph. Therefore the chromatic number of this graph is
exactly the minimum number \(a(G)\) of abelian subgroups covering \(G\).

## Exact results

[COMPUTED] The complete bounded inventory is:

| order | SmallGroups | eligible \(\nu\le8\) | excluded by a verified \(K_9\) | exact eligible distribution |
|---:|---:|---:|---:|:---|
| \(3\) | 1 | 1 | 0 | \((1,1)^1\) |
| \(9\) | 2 | 2 | 0 | \((1,1)^2\) |
| \(27\) | 5 | 5 | 0 | \((1,1)^3,(4,4)^2\) |
| \(81\) | 15 | 11 | 4 | \((1,1)^5,(4,4)^6\) |
| \(243\) | 67 | 24 | 43 | \((1,1)^7,(4,4)^{15},(7,10)^2\) |
| \(729\) | 504 | 49 | 455 | \((1,1)^{11},(4,4)^{31},(7,10)^7\) |

Here each pair is \((\nu,a)\), and its exponent is the number of groups.

[COMPUTED] Exactly 92 scanned groups satisfy \(\nu\le8\), while the other 502
have an explicit verified nine-clique. No scanned group has \(\nu=8\), and no
eligible scanned group has \(a>10\).

[COMPUTED] The 83 eligible AC-groups have \((\nu,a)=(1,1)\) or \((4,4)\).
The nine eligible non-AC groups all have \((\nu,a)=(7,10)\):
SmallGroup(243,65), SmallGroup(243,66), and SmallGroup(729,422), (729,423),
(729,424), (729,478), (729,501), (729,502), (729,503).

[COMPUTED] For each stored exact maximum-clique witness, the indices of its
member centralizers have only the following signatures:

| \(\nu\) | sorted centralizer-index signature | maximal members |
|---:|:---|---:|
| 1 | \((1)\) | 0 |
| 4 | \((3,3,3,3)\) | 4 |
| 7 | \((3,3,3,3,3,3,3)\) | 7 |

[COMPUTED] Thus every maximum-clique centralizer in every eligible nonabelian scanned
3-group is a maximal subgroup.

## Certificate design

[COMPUTED] For graphs with more than 81 central cosets, GAP first seeks a
nine-clique. Every successful row stores the nine representatives in pc
exponent coordinates, together with all 36 forward and reverse product
coordinates; the producer checks noncommutation in the actual SmallGroup.
Every remaining row stores the complete central-coset adjacency masks, GAP's
AC flag, and every graph-derived centralizer index.

[COMPUTED] Python checks the exact 594-row SmallGroup serial sequence, center
orders, pc relative orders, all saved product inequalities, adjacency symmetry,
the AC flag, and every centralizer index. On a stored graph it either verifies
a nine-clique or computes and verifies an exact maximum clique and exact
coloring after independent-twin compression. It lifts both witnesses back to
the original central-coset graph.

[COMPUTED] The Python verifier does not implement GAP's pc collector. It
checks the exported forward and reverse product coordinates for inequality
rather than recomputing those products from the witness coordinates. The GAP
producer checks every pair in the actual group, and the reproducibility audit
reruns the producer and compares the TSV and progress log byte for byte.

## Reproduction

~~~bash
work/gap-4.16.0/gap -l 'work/gap-4.16.0;' -q \
  -c 'ERDOS117_OUTPUT:="experiments/logs/h8_three_group_cutoff.tsv";; ERDOS117_STDOUT_LOG:="experiments/logs/h8_three_group_cutoff_gap.stdout.txt";; Read("experiments/configs/h8_three_group_cutoff.g");'
PYTHONPYCACHEPREFIX=/tmp/erdos117-h8-three-group-pycache \
python3 src/python/analyze_h8_three_group_cutoff.py \
  --input experiments/logs/h8_three_group_cutoff.tsv \
  --gap-script experiments/configs/h8_three_group_cutoff.g \
  --gap-stdout experiments/logs/h8_three_group_cutoff_gap.stdout.txt \
  --output experiments/logs/h8_three_group_cutoff.json \
  --stdout-log experiments/logs/h8_three_group_cutoff.stdout.txt
PYTHONPYCACHEPREFIX=/tmp/erdos117-h8-three-group-test-pycache \
python3 -m unittest src.verification.test_h8_three_group_cutoff -v
~~~

[UNVERIFIED] The observed absence of \(\nu=8\), the three surviving values
\(1,4,7\), and the maximal-centralizer signatures may suggest a structural
3-group obstruction. The computation alone does not justify extrapolating any
of these patterns to order 2187 or to arbitrary finite 3-groups.
