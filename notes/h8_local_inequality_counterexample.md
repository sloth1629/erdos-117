# A Local Centralizer-Index Inequality Fails

`[DISPROVED]` The proposed inequality

\[
[G:C_G(x)]\leq \nu(G)-\nu(C_G(x))
\]

does not hold for all finite groups. Let
\(G=\operatorname{SmallGroup}(48,15)\), whose GAP structure description is
`(C3 x D8) : C2`, and take the second element in GAP's deterministic
`AsList(G)` enumeration. The saved complete multiplication table verifies
that this element has order two and that its centralizer is an abelian group
of order four. Thus the left side is 12.

`[COMPUTED]` Exact maximum-clique and coloring searches on the independently
reconstructed multiplication table give

\[
(\nu(G),a(G))=(12,12),\qquad
(\nu(C_G(x)),a(C_G(x)))=(1,1).
\]

The JSON saves a 12-clique and a proper 12-coloring for the central-coset
noncommuting graph of \(G\). It also saves the abelian centralizer record and
checks every group axiom, the target's order, all centralizer memberships,
the index, and both graph witnesses. Consequently the proposed right side is
\(12-1=11<12\).

`[COMPUTED]` The raw GAP export is
`experiments/logs/h8_local_inequality_counterexample.tsv`; the canonical
certificate is
`experiments/logs/h8_local_inequality_counterexample.json`. Regenerate and
verify them from the repository root with:

```bash
work/gap-4.16.0/gap -q \
  -c 'ERDOS117_OUTPUT:="experiments/logs/h8_local_inequality_counterexample.tsv";; ERDOS117_STDOUT_LOG:="experiments/logs/h8_local_inequality_counterexample_gap.stdout.txt";; Read("experiments/configs/h8_local_inequality_counterexample.g");'
PYTHONPYCACHEPREFIX=/tmp/erdos117-h8-local-pycache \
python3 src/python/analyze_h8_local_inequality_counterexample.py \
  --input experiments/logs/h8_local_inequality_counterexample.tsv \
  --gap-script experiments/configs/h8_local_inequality_counterexample.g \
  --gap-stdout experiments/logs/h8_local_inequality_counterexample_gap.stdout.txt \
  --output experiments/logs/h8_local_inequality_counterexample.json \
  --stdout-log experiments/logs/h8_local_inequality_counterexample.stdout.txt
PYTHONPYCACHEPREFIX=/tmp/erdos117-h8-local-test-pycache \
python3 -m unittest src.verification.test_h8_local_inequality_counterexample -v
```

`[UNVERIFIED]` This artifact certifies the displayed counterexample only. It
does not assert that order 48 is the least possible counterexample order.
