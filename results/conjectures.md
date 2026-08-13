# Conjectures and Refutations

## Live conjectures

- `[CONJECTURE]` The optimal exponential constant is \(\sqrt2\): \(\log h(n)=(\tfrac12\log2)n+o(n)\).
- `[CONJECTURE]` Asymptotically extremal groups may be controlled, up to the appropriate commutation equivalence, by scalar-valued alternating forms, but characteristic \(2\) is not sufficient for an exact theory.
- `[CONJECTURE]` Optimizing scalar symplectic groups amounts to optimizing \(\log(q^m+1)/\pi(q,m)\), where \(\pi(q,m)\) is the maximum partial-ovoid size of \(W(2m-1,q)\).

## Refuted heuristics

- `[DISPROVED]` *Direct powers of one fixed finite group can explain an exponential lower bound for \(h(n)\).* For a fixed nonabelian seed, both \(a(G^k)\) and \(\nu(G^k)\) grow exponentially in \(k\), so \(a(G^k)\) is only a power of \(\nu(G^k)\); see `notes/graph_products.md`.
- `[DISPROVED]` *For \(n\geq3\), \(h(n)=\max\{n,2^{\lfloor(n-1)/2\rfloor}+1\}\).* The group \(S(3,2)\) of order \(3^5\) has \((\nu,a)=(7,10)\), exceeding the proposed value \(9\); see `notes/candidate_bound.md`. The unqualified formula also fails at \(n=1,2\).

Conjectures remain explicitly separate from proved results. Retain every future refutation with its counterexample.
