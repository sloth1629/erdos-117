# Source and Novelty Audit

Research cut-off: 2026-08-13.  Source PDFs, extracted text, and rendered page images were kept only under ignored `work/literature/`; no copyrighted source PDF is tracked by Git.

## Access and exact-page matrix

| Evidence | Source | Material checked | Access result |
|---|---|---|---|
| [CITED-VERIFIED] | Erdős–Straus (1976), DOI `10.1080/03081087608817122` | Printed p. 311: Isaacs factorial upper report and \(2^{M/2}\)-type examples | Full author-hosted PDF read; formula checked against a rendered page because OCR lost the comparison glyphs and exponent. |
| [CITED-VERIFIED] | B. H. Neumann (1976), DOI `10.1017/S1446788700019303` | Lemmas 1, 2, 4; Corollary 5; Theorem 6, pp. 468–470; quantitative remarks p. 471 | Full official Cambridge PDF read. |
| [CITED-VERIFIED] | Faber–Laver–McKenzie (1978), DOI `10.4153/CJM-1978-081-1` | Graph/cover bridge p. 933; Theorem 3, pp. 936–937 | Full journal PDF read. |
| [UNVERIFIED] | Mason (1978), DOI `10.1017/S0305004100054463` | Publisher extract and metadata only, pp. 205–209 | Official page is paywalled; no theorem from it is used as load-bearing evidence.  This DOI corrects a wrong DOI encountered in secondary search results. |
| [CITED-VERIFIED] | Bertram (1983), DOI `10.1016/0012-365X(83)90004-3` | Official metadata and reference [6] = Isaacs, personal communication | Printed p. 40/full article remained inaccessible; ScienceDirect PDF returned 403 and the located ResearchGate PDF endpoint did not yield a file. |
| [CITED-VERIFIED] | Pyber (1987), DOI `10.1112/jlms/s2-35.2.287` | Official publisher abstract and bibliographic data | Full paper remained inaccessible through Wiley/OUP, OpenAlex OA locations, CiteSeer, and archive/mirror searches; the exact Theorem 6.1 was not verified. |
| [CITED-VERIFIED] | Erdős (1997), DOI `10.1017/CBO9780511662034.004` | Problem 26, printed p. 8 | Full scanned volume read; formula checked on rendered physical PDF page 31. |
| [CITED-VERIFIED] | Pakianathan–Yalçın (2001), DOI `10.1006/jabr.1999.8501`, arXiv `math/0005301` | Introductory Isaacs/Pyber claims, pp. 396–397; bibliography | Full primary text read; the Isaacs pointer `[J]` was checked and found to be Jacobson. |
| [CITED-VERIFIED] | Işık (2005), `https://www.math.ucla.edu/~tao/preprints/nc.pdf` | Theorem 12 and proof, pp. 6–7; bibliography pp. 8–9 | Full public manuscript read.  Unpublished status is recorded. |
| [CITED-VERIFIED] | Abdollahi–Akbari–Maimani (2006), DOI `10.1016/j.jalgebra.2006.02.015` | Lemma 4.1 and Example 4.5, p. 488; reference [10], p. 492 | Full author-uploaded text read through ResearchGate; official DOI metadata cross-checked. |
| [CITED-VERIFIED] | Azad–Iranmanesh–Praeger–Spiga (2011), DOI `10.1007/s10801-011-0288-2`, arXiv `1004.3402` | Historical bound/Isaacs attribution, printed p. 685; scope of Theorems 1.1–1.5 | Full primary PDF read. |
| [UNVERIFIED] | Saccochi (2015), DOI `10.26512/2015.12.D.22224` | Theorem 4.1.1 p. 34; Pyber formula p. 36; Theorem 4.3.2 pp. 48–50; Theorem 5.2.7 pp. 56–59 | Full dissertation PDF read and critical formulas visually rendered.  It is secondary evidence for Pyber/Isaacs. |
| [CITED-VERIFIED] | Darafsheh–Ghorbani–Prajapati (2015), DOI `10.1017/S0004972715000830` | Extraspecial/Isaacs attribution p. 381 and reference list | Full official Cambridge PDF read. |
| [CITED-VERIFIED] | Maróti–Martínez–Moretó (2025), DOI `10.1016/j.jcta.2024.105954` | Pyber discussion p. 2 and the scope of the full paper | Full primary PDF read. |
| [UNVERIFIED] | Erdős Problems, `https://www.erdosproblems.com/117` | Indexed status and last-edit date | Search index said OPEN/no claimed solutions/last edited 2026-01-23; direct page returned HTTP 403. |

## Backward-source audit

[CITED-VERIFIED] The historical chain was followed backward from modern papers to Abdollahi–Akbari–Maimani Example 4.5, then to Bertram reference [10], and from Bertram to reference [6], which is explicitly a personal communication from Isaacs.

[CITED-VERIFIED] Darafsheh–Ghorbani–Prajapati independently confirm the same route by citing Bertram, printed p. 40, for \(\omega(G)=2r+1\) in an extraspecial 2-group of order \(2^{2r+1}\).

[CITED-VERIFIED] Erdős–Straus is an earlier independent report of Isaacs's factorial upper estimate and exponential examples, but it contains neither a citation nor a construction.

[UNVERIFIED] Saccochi attributes the arbitrary-to-finite reduction to Macdonald [13, §2].  Her bibliography misprints the item as 1969 and shortens its title; official metadata gives I. D. Macdonald, “Some Explicit Bounds in Groups with Finite Derived Groups,” *Proc. London Math. Soc.* s3-11 (1961), 23–56, DOI `10.1112/plms/s3-11.1.23`.  Its full proof was not accessible.

[CITED-VERIFIED] The Pakianathan–Yalçın citation `[J]` is not a hidden Isaacs source: their bibliography identifies it as N. Jacobson, *Basic Algebra I*.  It is excluded as a provenance failure.

## Pyber acquisition audit

[CITED-VERIFIED] The official abstract supports only the qualitative finite-group assertion \([G:Z(G)]\le c^{\nu(G)}\) for an absolute \(c\).

[UNVERIFIED] Attempts through Wiley, Oxford Academic, DOI resolution, OpenAlex open-access metadata, CiteSeer, Internet Archive/Wayback, and title/filename mirrors did not produce the full 1987 article.  No theorem number, exact page, constant, or proof mechanism from Pyber is promoted to `[CITED-VERIFIED]`.

[UNVERIFIED] The explicit expression in Saccochi p. 36 was visually read as
\[
2^{2^{25}m}\,2^{3(2+2\log_2m)^5}.
\]
The dissertation's preceding page specifies base-2 logarithms.  This transcription should be compared directly with Pyber Theorem 6.1 once access is obtained.

## Exact-formula and alternate-terminology search

[UNVERIFIED] Exact searches were run for `2^{floor((n-1)/2)}+1`, `2^{(n-1)/2}+1`, `max(n,2^{floor((n-1)/2)}+1)`, and plain-text/OCR variants of those expressions.

[UNVERIFIED] Concept searches combined `abelian cover`, `cover by abelian subgroups`, `minimal abelian covering`, `pairwise noncommuting`, `maximal non-commuting subset`, `noncommuting graph`, `clique number`, `chromatic number`, `extraspecial 2-group`, `central index`, and `isoclinism`.  Searches were repeated around the known papers of Bertram, Brown, Pyber, Chin, Abdollahi–Akbari–Maimani, Azad et al., and Darafsheh et al.

[DISPROVED] The candidate as originally written for every \(n\ge1\) fails at \(n=1,2\); the complete three-element argument is recorded in `literature/review.md`.

[DISPROVED] The \(n\ge3\) restriction also fails.  The repository's Theorem CB.1 in `notes/candidate_bound.md` proves that an order-\(3^5\) symplectic Heisenberg group has \((\nu,a)=(7,10)\), while the candidate gives 9 at \(n=7\) and, by monotonicity, at \(n=8\).  The proof is structural and does not depend on the discovery computation.

[UNVERIFIED] No search hit stated the exact formula, an equivalent universal inequality \(\chi(\Gamma_G)\le\max\{\omega(\Gamma_G),2^{\lfloor(\omega(\Gamma_G)-1)/2\rfloor}+1\}\), or the repository's \(\mathbb F_3\) counterexample.  Exact-expression indexing is weak, so this is not an absence proof or novelty certification.

[CITED-VERIFIED] Brown (1988) and Azad et al. (2011) study exact/asymptotic clique and abelian-cover numbers in specific families (symmetric and general linear groups).  Their published scopes are not a universal formula for \(h\).

## Centralizer-drop recurrence search

[UNVERIFIED] The local full-text corpus and web indexes were searched for the exact and symbolic forms `nu(C_G(x))`, `omega(C_G(x))`, `clique number of the centralizer`, `centralizer n-2 pairwise noncommuting`, `h(n-2) abelian cover`, and `h(n) <= n h(n-2)`.  No matching primary theorem was located.

[UNVERIFIED] The closest source result is the Isaacs argument reconstructed in Saccochi, Theorem 4.3.2, pp. 48–50: for noncommuting \(x,y\), it proves only
\[
\omega(C_G(x)\cap C_G(y))<\omega(G),
\]
then uses all \(\binom n2\) pair intersections to obtain \(f(n)=n+\binom n2f(n-1)\).  It neither states nor visibly implies \(\nu(C_G(x))\le\nu(G)-2\) without an additional argument.

[PROVED] After this comparison search, the project proved \(\nu(C_G(x))\le\nu(G)-2\) in `notes/candidate_bound.md`, Lemma CB.2, by modifying a noncommuting set in \(C_G(x)\) and adjoining \(y,xy\).  Corollary CB.3 then proves \(h(n)\le n h(n-2)\), \(h(2r+1)\le(2r+1)!!\), and \(h(2r)\le2^{r-1}r!\).

[UNVERIFIED] No located source stated that lemma, recurrence, or resulting bounds.  They are repository-new relative to this audited corpus, but the negative search does not establish global novelty.

## Forward-citation audit

[UNVERIFIED] The OpenAlex query `works?filter=referenced_works:W2003169277&per_page=100` returned 53 works citing Pyber in the saved 2026-08-13 snapshot.  Title/DOI searches and reference-list searches supplemented this set; the count is not exhaustive.

[CITED-VERIFIED] Maróti–Martínez–Moretó, *JCTA* 210 (2025), 105954, was read in full.  It quotes the standard \(n\le cc(\Gamma)\le[G:Z(G)]\) setup and Pyber's exponential center-index theorem, then studies the induced graph on \(p\)-elements and proper-subgroup covers.  It contains no improvement of \(h\).

[UNVERIFIED] Yang–Zarrin, *Bull. Aust. Math. Soc.* 112 (2025), 497–504, DOI `10.1017/S0004972724001370`, studies the number of pairwise noncommuting sets rather than the universal cover-vs-clique extremum.

[UNVERIFIED] Gao–Garonzi, *Vietnam J. Math.* (2025), DOI `10.1007/s10013-025-00744-z`, arXiv `2405.12160`, bounds groups using the number of cyclic subgroups and cites Pyber only as background.

[UNVERIFIED] Guralnick–Maróti–Martínez Madrid–Moretó–Rizo, *J. London Math. Soc.* 111 (2025), DOI `10.1112/jlms.70167`, arXiv `2407.20355`, concerns fixed-point ratios, Sylow numbers, and covers of \(p\)-elements.

[UNVERIFIED] Almeida–Moghaddamfar–Nakaoka, *International Journal of Algebra and Computation* 35(2) (2025), DOI `10.1142/S0218196725500018`, concerns pseudo-conjugation actions and isoclinism.

[UNVERIFIED] Nagy–Pach–Tomon, *Transactions of the AMS* 379 (2026), 137–156, DOI `10.1090/tran/9483`, concerns hyperplane covers and a different Pyber conjecture on irredundant coset covers of finite abelian groups.

[UNVERIFIED] No 2025/2026 forward item located in this audit claims a solution of Erdős Problem 117, the corrected exact formula, or determination/improvement of the asymptotic exponential constant.  This conclusion is bounded by database coverage and terminology.

## Remaining load-bearing acquisitions

[UNVERIFIED] Priority 1 is lawful access to Pyber (1987), especially Theorem 6.1 and its surrounding lemmas, to verify the exact constant, finite hypothesis, and proof losses.

[UNVERIFIED] Priority 2 is Bertram (1983), printed p. 40, to determine whether it contains an actual proof of the Isaacs recursion/construction or only the statement of the private communication.

[UNVERIFIED] Priority 3 is a primary proof of the extraspecial maximum abelian-subgroup order and central-coset covering count for both extraspecial 2-group isomorphism types.  Işık closes only the explicit-group clique-number subclaim.

[UNVERIFIED] Priority 4 is a proof-level audit of the Macdonald finite reduction, because a final arbitrary-group theorem cannot silently import a finite-group Pyber theorem.

[UNVERIFIED] No global novelty claim is authorized by this audit.  The binary candidate is disproved; the proved centralizer-drop recurrence still requires broader citation review before any claim of originality.
