# Verified Literature Review

Research cut-off: 2026-08-13.  Here \(\omega(G)=\nu(G)\) is the largest size of a pairwise noncommuting subset and \(a(G)\) is the least number of abelian subgroups covering \(G\).  Statements about what a paper *reports* are kept separate from the truth of the reported theorem when the proof-bearing source was not available.

## Current problem status

[CITED-VERIFIED] Erdős's Problem 26 in *Some Unsolved Problems* (1997), printed p. 8, asks for the least universal abelian-cover bound \(h(n)\) for groups having no pairwise noncommuting set larger than \(n\).  The same paragraph reports Pyber's two-sided exponential estimate \((1+c_1)^n<h(n)<(1+c_2)^n\), for positive constants \(c_1,c_2\), and says the lower bound was already known to Isaacs.  This verifies Erdős's wording and attribution, not the proofs behind it.

[UNVERIFIED] The indexed snapshot of the current Erdős Problems page for Problem 117 labels the problem OPEN, says that no complete or partial solution is claimed in its comments, and gives 23 January 2026 as its last edit.  The page itself returned HTTP 403 during this audit, so the status is recorded as a search-index observation rather than a verified primary mathematical source.

## Graph/group translation and the qualitative theorem

[CITED-VERIFIED] Faber, Laver and McKenzie (1978), printed p. 933, define the noncommuting graph on all elements of an arbitrary group and identify its chromatic number with the least number of abelian subgroups covering the group.  Their bridge is valid in both directions: a subgroup in a cover is an independent set, while every color class is pairwise commuting and therefore generates an abelian subgroup.

[CITED-VERIFIED] Faber–Laver–McKenzie, Theorem 3, pp. 936–937, proves for an arbitrary group \(G\) the equivalence of: finite chromatic number/finite abelian cover; finite \([G:Z(G)]\); the conjunction of an \(nC\) condition with a finite-index abelian subgroup; the conjunction of the FC condition with a finite-index abelian subgroup; a uniform finite upper bound on complete subgraphs; and absence of an infinite complete subgraph.

[CITED-VERIFIED] B. H. Neumann (1976), Theorem 6, p. 470, proves for arbitrary groups that absence of an infinite pairwise noncommuting subset is equivalent to finite center index.  Lemma 1 (p. 468) first obtains the FC property using infinite Ramsey theory; Lemma 2 (p. 469) turns FC plus a finite-index abelian subgroup into finite center index; Lemma 4 and Corollary 5 (pp. 469–470) recursively construct an infinite noncommuting set if an FC group is not central-by-finite.

[CITED-VERIFIED] Neumann, p. 471, records the elementary bound \(\nu(G)\le [G:Z(G)]-1\), obtains only \(\log [G:Z(G)]=O(\nu(G)^2)\) from his proof, conjectures a quadratic center-index bound, and observes that every positive integer except 2 occurs as a finite value of \(\nu(G)\).

## The quantitative upper bound: Pyber

[CITED-VERIFIED] The official publisher abstract for Pyber (1987) states the finite-group result that a bound \(n\) on the number of pairwise noncommuting elements forces \([G:Z(G)]\le c^n\) for an absolute constant \(c\).  The accessible abstract supplies neither Theorem 6.1 nor its constant or proof.

[UNVERIFIED] Pyber's full text was not accessible in this audit: the Wiley/OUP PDF endpoints returned access errors, OpenAlex listed no open-access location, and the other located mirrors did not yield the article.  Consequently the exact theorem statement, pages, hypotheses, constant, and proof cannot yet carry a repository proof.

[UNVERIFIED] Saccochi's 2015 dissertation, Theorem 6.1 as reproduced on printed p. 36, attributes to Pyber the explicit finite-group estimate
\[
 [G:Z(G)]\le 2^{2^{25}m}\,2^{3(2+2\log_2 m)^5},\qquad m=\omega(G).
\]
The same page sketches the mechanism: take \(C=C_G(G')\), a finite nilpotent group of class at most two; bound \([G:C]\) and \([Z(C):Z(G)]\) using BFC/derived-group estimates; bound \([C:Z(C)]\) Sylow subgroup by Sylow subgroup, using \(\omega(A\times B)\ge\omega(A)\omega(B)\); then multiply the three indices.  This is a useful acquisition target but remains secondary evidence until Pyber's paper is read.

[UNVERIFIED] Saccochi, Theorem 4.1.1, p. 34, states that if \(\omega(G)<\infty\), then there is a finite group \(H\) with \(H/Z(H)\cong G/Z(G)\) and \(\omega(H)=\omega(G)\), citing Macdonald [13, §2].  Macdonald's proof was not acquired, so this finite-reduction step is not yet available as a load-bearing citation.

## Isaacs's abelian-cover bound and citation chain

[CITED-VERIFIED] Erdős and Straus (1976), printed p. 311, report that Isaacs related the maximum \(M\) of a pairwise noncommuting set to the minimum abelian-cover size \(m\), with an upper estimate of the form \(m\lesssim(M!)^2\) and finite examples of the form \(m\gtrsim2^{M/2}\).  No construction, proof, or bibliographic reference is supplied there.

[CITED-VERIFIED] Bertram (1983) is the published node to which later papers point for the Isaacs statements; the official article metadata/reference list identifies reference [6] as “I. M. Isaacs, Personal communication.”  Bertram's proof-bearing printed p. 40 was not accessible in this audit.

[CITED-VERIFIED] Abdollahi, Akbari and Maimani (2006), Lemma 4.1, p. 488, again proves that the chromatic number of the noncommuting graph on \(G\setminus Z(G)\) is the minimum abelian-cover size for a finite nonabelian group.  On the same page, Example 4.5, explicitly attributed to Isaacs through Bertram [10], reports for every extraspecial 2-group \(S\) of order \(2^{2r+1}\) that \(\omega(S)=2r+1\), \([S:Z(S)]=2^{2r}\), and \(\chi(\Gamma_S)\ge2^r+1\); the example contains no proof.

[CITED-VERIFIED] Darafsheh, Ghorbani and Prajapati (2015), p. 381, likewise state \(\omega(G)=2r+1\) for extraspecial 2-groups of order \(2^{2r+1}\) and explicitly direct the reader to Bertram, p. 40.  This independently verifies the later citation route, not the missing Isaacs proof.

[CITED-VERIFIED] Azad, Iranmanesh, Praeger and Spiga (2011), printed p. 685, state that for \(N=[G:Z(G)]\) one has \(c\log_2N\le\omega(G)\le N-1\), and that the lower bound is achieved with \(c=1\) by extraspecial 2-groups, attributing this to Isaacs through Bertram and Pyber.  Their results about \(GL_n(q)\) are family-specific and do not determine the universal function \(h\).

[CITED-VERIFIED] Işık's accessible 2005 manuscript, Theorem 12, pp. 6–7, directly proves \(\omega(S(2,r))=2r+1\) for its explicit extraspecial group \(S(2,r)\).  The proof translates commutation to nonorthogonality for a symplectic form on \(\mathbb F_2^{2r}\), rules out \(2r+2\) vectors by a linear-independence argument, and constructs \(2r+1\) vectors inductively.  It does not prove the lower bound for an abelian cover and is an unpublished manuscript.

[UNVERIFIED] Saccochi, Theorem 4.3.2, pp. 48–50, gives a complete secondary reconstruction of the Isaacs recursion
\[
 f(1)=1,\qquad f(n)=n+\binom n2 f(n-1),\qquad a(G)\le f(\omega(G))<(\omega(G)!)^2
\]
for groups with finite \(\omega(G)\) (the final strict factorial inequality is for \(\omega(G)>1\)).  Its mechanism covers intersections \(C_G(x_j)\cap C_G(x_k)\) inductively after their clique number drops, and covers the remaining elements by \(n\) pairwise-commuting sets.  Because the original source is a private communication and this is a dissertation reconstruction, the theorem remains secondary evidence here.

[UNVERIFIED] Saccochi, Theorem 5.2.7, pp. 56–59, reconstructs for every extraspecial 2-group of order \(2^{2r+1}\) the assertions \([G:Z(G)]=2^{2r}\), \(\omega(G)=2r+1\), and \(a(G)\ge2^r+1\).  For the cover lower bound it enlarges each covering subgroup to contain the center, uses the asserted maximum abelian-subgroup order \(2^{r+1}\), and counts the \(2^{2r}-1\) nontrivial central cosets, at most \(2^r-1\) per subgroup.  The cited maximum-order input and the all-isomorphism-types argument still require primary or repository verification.

[CITED-VERIFIED] Pakianathan and Yalçın (2001), pp. 396–397, state the Isaacs inequality \(nc(G)\le cc(G)\le(nc(G)!)^2\), but their pointer “[J]” resolves to Jacobson's *Basic Algebra I*, not to a source for this theorem.  This is a citation defect and cannot repair the Isaacs provenance gap.

## Search for the proposed sharp formula

[DISPROVED] As a formula for all \(n\ge1\) under the repository's definition of \(h\),
\[
 h(n)=\max\{n,2^{\lfloor(n-1)/2\rfloor}+1\}
\]
is false at \(n=1,2\).  Indeed, if \(xy\ne yx\), then \(x,y,xy\) are pairwise noncommuting: commutation of \(x\) with \(xy\), or of \(y\) with \(xy\), would imply \(xy=yx\).  Thus \(\nu(G)\le2\) forces \(G\) to be abelian, so \(h(1)=h(2)=1\), whereas the displayed right-hand side is 2 in both cases.

[DISPROVED] The restriction to \(n\ge3\) is also false.  The repository proof in `notes/candidate_bound.md`, Theorem CB.1, constructs the order-\(3^5\) rank-two Heisenberg/extraspecial group \(H\) with
\[
\nu(H)=7,\qquad a(H)=10.
\]
The proposed right-hand side is only 9 at \(n=7\), so \(h(7)\ge10>9\); monotonicity gives the same contradiction at \(n=8\).  The proof derives \(a(H)=10\) from a ten-subspace symplectic spread and proves \(\nu(H)=7\) by an explicit seven-point configuration plus a projective/symplectic upper bound, so computation is not a dependency.

[UNVERIFIED] Searches on the exact expressions \(2^{\lfloor(n-1)/2\rfloor}+1\), \(2^{(n-1)/2}+1\), and \(\max\{n,2^{\lfloor(n-1)/2\rfloor}+1\}\), together with searches under “abelian cover/covering,” “pairwise noncommuting,” “noncommuting graph clique/chromatic number,” and “extraspecial group,” found neither a published universal formula nor a published refutation matching the repository's \(\mathbb F_3\) example.  This negative search is not a novelty proof.

[CITED-VERIFIED] The second branch of that candidate exactly matches the lower bound reported in Abdollahi–Akbari–Maimani Example 4.5 when \(n=2r+1\): \(a(G)=\chi(\Gamma_G)\ge2^r+1\).  The source gives only a lower bound and does not claim equality for the cover number or a universal upper bound.

[CITED-VERIFIED] Neumann, p. 471, gives for every positive integer \(r\ne2\) a dihedral group whose maximum pairwise noncommuting-set size is exactly \(r\).  Together with the elementary inequality \(a(G)\ge\nu(G)\), this supplies the candidate's linear lower branch \(h(n)\ge n\) for every \(n\ge3\); Neumann says the verification of the dihedral example is easy but omits it.

[UNVERIFIED] Monotonicity of \(h\) would extend the reported extraspecial lower branch from odd \(n=2r+1\) to the next even \(n=2r+2\), giving \(h(n)\ge2^{\lfloor(n-1)/2\rfloor}+1\) for all \(n\ge3\), once that lower construction is independently verified.  No located source says that extraspecial 2-groups are extremal or supplies the matching universal upper bound.

## Centralizer-drop recurrence

[PROVED] The repository's Lemma CB.2 in `notes/candidate_bound.md` proves that every noncentral \(x\) in a group with finite \(\nu\) satisfies
\[
\nu(C_G(x))\le\nu(G)-2.
\]
Given a noncommuting \(y\) and a noncommuting set \(a_i\) in \(C_G(x)\), the proof replaces each \(a_i\) that commutes with \(y\) by \(xa_i\), producing a pairwise noncommuting set consisting of the modified \(a_i\)'s together with \(y,xy\).

[PROVED] Corollary CB.3 covers a group by the centralizers of the members of a maximum noncommuting set and obtains
\[
h(n)\le n\,h(n-2)\quad(n\ge3),
\]
hence \(h(2r+1)\le(2r+1)!!\) and \(h(2r)\le(2r)!!/2=2^{r-1}r!\).

[UNVERIFIED] Full-text and exact/alternate-term searches found no earlier source for this two-step centralizer drop or recurrence.  The nearest located antecedent is the different Isaacs argument reconstructed by Saccochi, pp. 48–50, which proves only \(\omega(C_G(x)\cap C_G(y))<\omega(G)\) and yields \(f(n)=n+\binom n2f(n-1)\).  “Repository-new relative to the located corpus” is not a global novelty claim.

## Forward citations and possible later resolutions

[CITED-VERIFIED] Maróti, Martínez and Moretó (2025), printed p. 2, cite Pyber while defining the coclique/abelian-cover number of a noncommuting graph, but the paper's new theorems concern covers of the set of \(p\)-elements by proper subgroups.  Its full text contains no new universal estimate for \(h(n)\), \([G:Z(G)]\) in terms of \(\omega(G)\), or the exponential base.

[UNVERIFIED] The 2024–2026 forward items located through OpenAlex and DOI/title searches—work on pseudo-conjugation/isoclinism, numbers of pairwise noncommuting sets, cyclic-subgroup counts, fixed-point ratios and covers of \(p\)-elements, and hyperplane/coset covers—have abstracts or full texts whose stated scope is different from Erdős Problem 117.  In particular, the 2026 hyperplane-cover paper concerns a different Pyber conjecture about irredundant coset covers of finite abelian groups.

[UNVERIFIED] The forward search found no 2025 or 2026 paper claiming a resolution of Problem 117, the candidate exact formula, or an improved/determined asymptotic exponential constant.  This is an index-bounded negative result, not proof that no such paper exists.

## Load-bearing gaps

[UNVERIFIED] The two principal inaccessible sources are Pyber's full 1987 article (needed for its exact Theorem 6.1, constants, hypotheses, and proof) and Bertram's printed p. 40 (needed to inspect what was actually transmitted from Isaacs).  Neither may be used as a black box for a final solution.

[UNVERIFIED] Before any novelty claim, the project still needs lawful full-text access to Pyber and Bertram or must avoid depending on them. The repository now supplies independent proofs of the exact finite commutation-model reduction and of the scalar symplectic cover formulas, so those particular statements are no longer source gaps. The explicit Pyber fixed-base upper bound and the historical Isaacs/Bertram provenance remain unresolved. The disproved binary candidate is no longer a live proof target.
