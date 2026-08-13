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

## Finite-geometry branch

```text
pairwise nonorthogonal projective points in F_q^(2m)
  = partial ovoids of W(2m-1,q) [PROVED translation]
  |
  |-- Blokhuis--Moorhouse 1995, Thms.1.1,1.6; Prop.4.1
  |     `-- p-rank bound pi(q,m) <= binom(p+2m-2,p-1)^e+1
  |
  |-- Tallini 1991 [UNVERIFIED original historical source]
  |     `-- odd-q W(3,q) upper q^2-q+1, later cited by DKMS 2008
  |           `-- accessible independent proof: Klein--Metsch 2005,
  |               Thm.3.3 + Klein--Metsch 2010 correction [CITED-VERIFIED]
  |
  |-- Cimrakova--De Winter--Fack--Storme 2007 [CITED-VERIFIED]
  |     |-- construction 2q+1, Remark 2.11(2)
  |     `-- exhaustive maxima pi(3,2)=7, pi(5,2)=18, pi(7,2)=33,
  |         section 4.1 and Table 1
  |
  |-- De Beule--Klein--Metsch--Storme 2008 [CITED-VERIFIED]
  |     |-- exact pi(q,2)=q^2+1 for even q, manuscript p.8
  |     |-- recurrence pi(q,m) <= 2+(q-1)pi(q,m-1), Thm.3.2
  |     `-- sharper W(5,q) upper bound, Thm.6.1
  |
  `-- Ceria--De Beule--Pavese--Smaldore 2023 [CITED-VERIFIED]
        |-- odd-square W(3,q) construction, Thm.3.3
        `-- reported Magma value pi(3,3)=13, Remark 3.13
```

[CITED-VERIFIED] The Klein–Metsch 2010 correction is a mandatory edge: it says the original Lemma 1.2 was false as stated, supplies the replacement argument for Proposition 3.2, and confirms the two main results of the 2005 paper.  The odd-\(q\) \(q^2-q+1\) bound is therefore cited to the paper and correction together.

[CITED-VERIFIED] Combining the verified \(2q+1\) construction and \(q^2-q+1\) upper bound gives \(\pi(3,2)=7\) without computation.  The 2007 exhaustive table independently gives the same value and gives 18 and 33 for \(q=5,7\).  Those external search results are citation evidence, not repository `[COMPUTED]` evidence.

[CITED-VERIFIED] Consequently the seven-point symplectic clique underlying the repository's \(S(3,2)\) group was already known as a maximum partial ovoid of \(W(3,3)\).  This edge reaches only \(\nu=7\), not the abelian-cover value \(a=10\).

[UNVERIFIED] No located edge joins the finite-geometry literature to the combined group statement \((\nu,a)=(7,10)\).  The negative search is index-bounded and cannot certify novelty.

## Candidate-formula and recurrence nodes

[DISPROVED] The unrestricted candidate \(h(n)=\max\{n,2^{\lfloor(n-1)/2\rfloor}+1\}\) fails at \(n=1,2\), as proved in `literature/review.md`, and its restriction to \(n\ge3\) fails at \(n=7,8\) by the order-\(3^5\) group proved in `notes/candidate_bound.md`, Theorem CB.1.

[UNVERIFIED] No located citation points from the exact candidate, an equivalent chromatic bound, the order-\(3^5\) counterexample, or the recurrence \(h(n)\le n h(n-2)\) to an earlier paper.

[UNVERIFIED] The nearest located antecedent is Isaacs's different recursion as reconstructed by Saccochi, Theorem 4.3.2, pp. 48–50: it proves only \(\omega(C_G(x)\cap C_G(y))<\omega(G)\) for noncommuting \(x,y\) and leads to \(f(n)=n+\binom n2 f(n-1)\).  It does not state \(\nu(C_G(x))\le\nu(G)-2\).

[PROVED] The repository nevertheless proves the two-step centralizer drop in Lemma CB.2 and derives \(h(n)\le n h(n-2)\) in Corollary CB.3 of `notes/candidate_bound.md`.  These nodes are repository proofs reached only after the literature comparison; “not located earlier” is not a global novelty assertion.

## Exterior-square node

```text
Brown--Johnson--Robertson 1987 [CITED-VERIFIED]
  |-- Q wedge Q and commutator map, p.181
  |-- central-extension crossed pairing, Prop.7 p.182
  `-- Schur cover S gives Q wedge Q ~= S', Cor.2 pp.182--183
        `-- finite-Q exterior-square enumeration [repository application]
```

[CITED-VERIFIED] Corollary 2 assumes that \(H_2(Q)\) is finitely generated, so it applies to finite \(Q\).  This is the exact load-bearing historical source for the Schur-cover bridge; the primary paper and the cited pages were read, and its DOI is `10.1016/0021-8693(87)90248-1`.

## Five-cover node

```text
maximum noncommuting set X={x1,...,x5}
  |-- centralizers C_G(xi) form an irredundant 5-cover [PROVED]
  |-- Lemma CB.2 forces intersection_i C_G(xi)=Z(G) [PROVED]
  `-- Bryce--Fedri--Serena 1997, Thm.1.2: f(5)=16 [CITED-VERIFIED]
        `-- [G:Z(G)] <= 16 when nu(G)=5 [PROVED + cited input]
```

[CITED-VERIFIED] Bryce–Fedri–Serena's theorem is exactly about the index of the intersection of an irredundant five-subgroup cover.  The centralizer/intersection bridge is not attributed to that paper and is supplied separately by the repository.  The source's sharpness example for \(f(5)\) does not by itself prove sharpness of the resulting center-index bound within groups having \(\nu=5\).

```text
Jafarian Amiri--Rostami 2017, introduction p.194 [CITED-VERIFIED report]
  |-- Jafarian Amiri--Madadi 2016 [publisher preview only]
  |     `-- claims structural properties of finite groups with omega=5
  `-- Jafarian Amiri--Madadi--Rostami 2017 [official abstract only]
        `-- finite F-groups with |G:Z(G)|=p^4

Abdollahi--Jafarian Amiri--Mohammadi Hassanabadi 2007, p.44
  `-- reports Ashrafi: finite 6-centralizer groups have quotient
      D8, A4, C2^3, or C2^4 [CITED-VERIFIED report]
```

[UNVERIFIED] The four-quotient list has now been located, but its checked scope is finite **6-centralizer groups**, not every group with \(\omega(G)=5\); the original Ashrafi proof was not read.  A central-factor list alone cannot be used as a commutation classification, while the F-group hypothesis in the second paper is weaker than having all proper centralizers abelian.  These edges therefore remain outside the proof graph for \(h(5)\).

## Six-cover node

```text
maximum noncommuting set X={x1,...,x6}
  |-- centralizers C_G(xi) form an irredundant 6-cover [PROVED]
  |-- Lemma CB.2 forces intersection_i C_G(xi)=Z(G) [PROVED]
  `-- Abdollahi et al. 2005: f(6)=36 [CITED-VERIFIED statement]
        `-- [G:Z(G)] <= 36 when nu(G)=6 [PROVED + cited input]
```

[CITED-VERIFIED] Theorem D on printed p. 72 of the authors' 2004 extended abstract gives the exact six-cover theorem, and the official 2005 journal abstract agrees.  The complete journal proof was not accessible, so the checked edge is the primary theorem statement and proof outline rather than a line-by-line full-proof audit.

[UNVERIFIED] No located classification of all \(\omega(G)=6\) groups or small-clique perfect-graph theorem turns this center-index bound into \(a(G)\le6\).  Thus this branch reduces the finite search but does not determine \(h(6)\).
