# Independent audit of the cutoff-eight subgroup-cover frontier

## [PROVED] Audit verdict

Two independent hostile reconstructions checked the new cutoff-eight cover
argument.  With the already audited exact values

\[
f(3)=4,\quad f(4)=9,\quad f(5)=16,\quad f(6)=36,\quad f(7)=81,
\]

from this repository, the complete integrated verdict is

\[
\boxed{144\le f(8)\le25\,920}.
\]

The following subsidiary statements also survive the audit.

1. A core-free irredundant eight-cover either has intersection index at most
   \(2,880\), or it can be enlarged, preserving its intersection, to an
   irredundant cover by eight maximal subgroups.
2. In the maximal/core-free branch with a central minimal normal subgroup
   \(C_2\), the intersection index is at most \(144\), and the explicit
   order-144 witness makes this sharp.
3. For arbitrary, possibly infinite groups,
   \[
   \nu(G)=8\Longrightarrow [G:Z(G)]\le25\,920.
   \]

The audit does not prove \(f(8)=144\).

## [PROVED] Reconstructed load-bearing steps

The hostile audits independently reconstructed, rather than merely cited,
the following steps from `notes/f8_eight_cover_frontier.md`.

- The factorial intersection lemma for irredundant coset covers, including
  the induction on omitted members and the count of cosets of the total
  intersection.
- The complement-index counting lemma and its equality case.
- Both cases of
  \[
  [G:D]\le
  \max\{(n-1)^2,(n-2)^3\}(n-3)!.
  \]
- Preservation of the intersection during nonredundant maximal enlargement,
  and the \(f(j)(9-j)!\) estimate when enlargement becomes redundant.
- The private-fiber proof that an abelian minimal normal subgroup in a
  maximal/core-free eight-cover has order in \(\{2,3,4,5,7\}\).
- The graph-of-homomorphisms description and induced irredundant cover used
  in the central-\(C_2\) branch.
- The exact centralizer cover of a maximum eight-clique and its intersection
  \(Z(G)\).

One audit worked only from a deliberately restricted packet and therefore
temporarily labelled the numerical thresholds \(2,880\) and \(144\)
`[UNVERIFIED]`: the packet omitted the proofs of \(f(5),f(6),f(7)\).
That was an evidence-scope warning, not a mathematical counterexample.  The
missing inputs are proved and independently certified in this repository,
so the integrated labels above are `[PROVED]`.

## [COMPUTED] Independent order-144 witness verification

`src/verification/verify_f8_order144_witness.py` independently checks the
semidirect-product tuple model and the eight displayed subgroups.  It checks
all \(144^3=2,985,984\) associativity triples, subgroup closure, indices,
union, trivial intersection, and every private set.  The regression test is
`src/verification/test_f8_eight_cover_frontier.py`.

The verifier also checks the audit observation that the arbitrary-cover
witness has clique number ten, not eight: its generalized-dihedral factor
has nine pairwise noncommuting reflections, and any nonzero translation
joins all nine.  This does not affect its role as an \(f(8)\) lower witness.

## Source provenance

The imported research memo and the two external audit reports had SHA-256
hashes

```text
f53a04a46c202cbc0111368965a8e0e6fc0caa3daf1be290e311ff7b7e92ab37  f8_eight_cover_frontier.md
e9af9bf1c897ca84ecb4a377b89001f843faec752cdaadb99906e9f5dc1f1b39  PRO_F8_HOSTILE_AUDIT_REPORT_KO.md
2c628e336072aefa3b972ee49dad7bf4ba3856a325a89cf7dd8c2d6c4cbe2eb7  pro_h8_25920_audit_report.md
```

The repository note is the normalized proof-bearing version; unsupported
ad-hoc evidence labels in the imported documents were not retained.
