# Candidate Theorem Strategy Matrix

No candidate below is a theorem. They are deliberately separated from proved lower bounds.

| Rank | Candidate final theorem | Current lower mechanism | Required upper mechanism | Main falsification risk | Status |
|---:|---|---|---|---|---|
| 1 | The exponential rate exists and equals \(\sqrt2\) | The groups \(E_m\) give \(h(2m+1)\ge2^m+1\) | A universal \(a(G)\le2^{\nu(G)/2+o(\nu(G))}\) plus interpolation/submultiplicative control for \(h\) | Odd-characteristic scalar symplectic groups already defeat the simplest exact formula; they or higher-codomain maps may also beat the asymptotic base | `[CONJECTURE]` |
| 2 | The extremal problem reduces asymptotically to optimizing partial ovoids and isotropic covers of alternating-map geometries | Scalar symplectic groups satisfy \(a(S(q,m))=q^m+1\), while \(\nu\) is a partial-ovoid number | Reduction of arbitrary finite groups to controlled class-two geometries, plus sharp finite-polar-space bounds | Nonnilpotent groups or vector-valued commutators may be more efficient | `[CONJECTURE]` |
| 3 | The limit need not be the right invariant; sharp upper/lower exponential constants differ or oscillate | Verified symplectic lower construction | Optimized Pyber-type structural recursion and constructions on selected dimensions | Could merely reflect weakness of present methods rather than true behavior | `[CONJECTURE]` |

Direct powers of a fixed group are not a plausible exponential extremizer: `notes/graph_products.md` proves that they yield only a polynomial relation between \(a\) and \(\nu\).

The former exact candidate
\[
h(n)=\max\{n,2^{\lfloor(n-1)/2\rfloor}+1\}
\]
is `[DISPROVED]`: it fails at \(n=1,2\), and its restriction to \(n\geq3\)
fails at \(n=7\) because the order-\(3^5\) scalar symplectic group has
\((\nu,a)=(7,10)\); see `notes/candidate_bound.md`.
