# Citation Graph

Research cut-off: 2026-08-13.  An arrow means “cites or explicitly attributes to,” not “supplies a checked proof of.”

## Main provenance map

```text
Isaacs, personal communication [UNVERIFIED]
  |-- reported directly by Erdos--Straus 1976, p.311 [CITED-VERIFIED report]
  `-- Bertram 1983, p.40; ref.[6] = personal communication [page UNVERIFIED]
        |-- Abdollahi--Akbari--Maimani 2006, Ex.4.5 p.488 [CITED-VERIFIED report]
        |-- Darafsheh--Ghorbani--Prajapati 2015, p.381 [CITED-VERIFIED report]
        |-- Azad--Iranmanesh--Praeger--Spiga 2011, p.685 [CITED-VERIFIED report]
        `-- Saccochi 2015, Thms.4.3.2 and 5.2.7 [UNVERIFIED secondary reconstruction]

Neumann 1976, Thm.6 and p.471 [CITED-VERIFIED]
  `-- Faber--Laver--McKenzie 1978, p.933 and Thm.3 [CITED-VERIFIED]

Macdonald 1961, section 2 [UNVERIFIED: inaccessible]
  `-- Saccochi 2015, Thm.4.1.1 p.34 [UNVERIFIED secondary report]

Pyber 1987 [abstract CITED-VERIFIED; full theorem UNVERIFIED]
  |-- Erdos 1997, Problem 26 p.8 [CITED-VERIFIED report]
  |-- Pakianathan--Yalcin 2001, pp.396--397 [CITED-VERIFIED report]
  |-- Isik 2005, pp.1 and 8--9 [CITED-VERIFIED report]
  |-- Azad--Iranmanesh--Praeger--Spiga 2011, p.685 [CITED-VERIFIED report]
  |-- Saccochi 2015, p.36 [UNVERIFIED secondary formula]
  `-- Maroti--Martinez--Moreto 2025, p.2 [CITED-VERIFIED, different local problem]

Isik 2005, Thm.12 pp.6--7 [CITED-VERIFIED independent accessible proof]
  `-- omega(S(2,r)) = 2r+1 only; no abelian-cover lower-bound proof
```

## Edge audit

[CITED-VERIFIED] Erdős–Straus (1976), p. 311, names Isaacs but gives no reference.  It is therefore an independent historical report rather than a bibliographic path to a proof.

[CITED-VERIFIED] Bertram's official reference list resolves [6] to “I. M. Isaacs, Personal communication.”  Abdollahi–Akbari–Maimani reference [10] is Bertram; Darafsheh–Ghorbani–Prajapati explicitly say “see [4, page 40],” where [4] is Bertram.

[CITED-VERIFIED] Abdollahi–Akbari–Maimani, Example 4.5, is the cleanest published statement of the alleged lower construction located here, but it is a statement-only example.  Darafsheh et al. add no proof and cite the same Bertram page.

[CITED-VERIFIED] Azad et al., printed p. 685, join both Bertram and Pyber to the statement that extraspecial 2-groups attain the \(c=1\) logarithmic center-index lower bound.  Their own theorems concern \(GL_n(q)\), so that edge does not produce a universal solution.

[UNVERIFIED] Saccochi is the only located source spelling out both the Isaacs factorial recursion and the extraspecial central-coset count.  It is a secondary dissertation and its references ultimately return to Bertram/private communication or to additional sources not yet audited.

[CITED-VERIFIED] Işık supplies an independent readable proof of the clique number for an explicit extraspecial 2-group, rather than merely another arrow to Bertram.  It does not close the cover-number edge.

[CITED-VERIFIED] Pakianathan–Yalçın's purported citation “[J]” for the factorial cover bound resolves to Jacobson's *Basic Algebra I*.  This malformed edge is excluded from the proof graph.

## Forward-search branches from Pyber

[UNVERIFIED] An OpenAlex query for works citing Pyber's work identifier `W2003169277` returned 53 records in the snapshot used here.  OpenAlex coverage and citation matching are incomplete, so this is a search queue rather than a complete forward graph.

[CITED-VERIFIED] Maróti–Martínez–Moretó (2025) was read in full.  Its Pyber edge is introductory; its results cover \(p\)-elements by proper subgroups and do not change \(h(n)\).

[UNVERIFIED] The other located 2024–2026 branches are Almeida–Moghaddamfar–Nakaoka (pseudo-conjugation/isoclinism), Yang–Zarrin (numbers of noncommuting sets), Gao–Garonzi (cyclic-subgroup counts), Guralnick et al. (fixed-point ratios and \(p\)-element covers), and Nagy–Pach–Tomon (hyperplane/coset covers).  Their available abstracts or texts expose no claim about the universal \(h(n)\) or its exponential constant.

## Candidate-formula and recurrence nodes

[DISPROVED] The unrestricted candidate \(h(n)=\max\{n,2^{\lfloor(n-1)/2\rfloor}+1\}\) fails at \(n=1,2\), as proved in `literature/review.md`, and its restriction to \(n\ge3\) fails at \(n=7,8\) by the order-\(3^5\) group proved in `notes/candidate_bound.md`, Theorem CB.1.

[UNVERIFIED] No located citation points from the exact candidate, an equivalent chromatic bound, the order-\(3^5\) counterexample, or the recurrence \(h(n)\le n h(n-2)\) to an earlier paper.

[UNVERIFIED] The nearest located antecedent is Isaacs's different recursion as reconstructed by Saccochi, Theorem 4.3.2, pp. 48–50: it proves only \(\omega(C_G(x)\cap C_G(y))<\omega(G)\) for noncommuting \(x,y\) and leads to \(f(n)=n+\binom n2 f(n-1)\).  It does not state \(\nu(C_G(x))\le\nu(G)-2\).

[PROVED] The repository nevertheless proves the two-step centralizer drop in Lemma CB.2 and derives \(h(n)\le n h(n-2)\) in Corollary CB.3 of `notes/candidate_bound.md`.  These nodes are repository proofs reached only after the literature comparison; “not located earlier” is not a global novelty assertion.
