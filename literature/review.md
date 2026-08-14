# Verified Literature Review

Research cut-off: 2026-08-13.  Here \(\omega(G)=\nu(G)\) is the largest size of a pairwise noncommuting subset and \(a(G)\) is the least number of abelian subgroups covering \(G\).  Statements about what a paper *reports* are kept separate from the truth of the reported theorem when the proof-bearing source was not available.

## External problem-status snapshot

[CITED-VERIFIED] Erdős's Problem 26 in *Some Unsolved Problems* (1997), printed p. 8, asks for the least universal abelian-cover bound \(h(n)\) for groups having no pairwise noncommuting set larger than \(n\).  The same paragraph reports Pyber's two-sided exponential estimate \((1+c_1)^n<h(n)<(1+c_2)^n\), for positive constants \(c_1,c_2\), and says the lower bound was already known to Isaacs.  This verifies Erdős's wording and attribution, not the proofs behind it.

[UNVERIFIED] The indexed snapshot of the Erdős Problems page for Problem 117,
last edited 23 January 2026, labels the problem OPEN and says that no complete
or partial solution is claimed in its comments.  This is a historical
external-index snapshot predating the repository's exact-seven proof, not a
current audit of this repository.  The page itself returned HTTP 403, so the
status is recorded as a search-index observation rather than a verified
primary mathematical source.

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

## Finite-geometry translation: symplectic partial ovoids

[PROVED] Let \(\pi(q,m)\) denote the maximum number of pairwise nonorthogonal projective points in a nondegenerate \(2m\)-dimensional symplectic space over \(\mathbb F_q\).  This is exactly the maximum size of a partial ovoid of the polar space \(W(2m-1,q)\).  Indeed, every projective point is isotropic for an alternating form; two points lie on a totally isotropic line exactly when their representatives are orthogonal; and every such line extends to a generator.  Thus “at most one point on every generator” is equivalent to pairwise nonorthogonality.  Bamberg–Bishnoi–Ihringer–Ravi (2024), §2, author-manuscript p. 4, states the same equivalence explicitly.

[CITED-VERIFIED] The finite-geometry word *cap* is potentially ambiguous.  Blokhuis–Moorhouse (1995), §4, printed p. 315, uses *cap in a polar space* for a set of pairwise nonorthogonal points, hence for the object counted by \(\pi(q,m)\).  An ambient projective cap usually means a set with no three collinear points and is a different object.  Also, *maximal* means inclusion-maximal, whereas \(\pi(q,m)\) asks for *maximum* cardinality.

[PROVED] In rank one, \(\pi(q,1)=q+1\).  A point of the symplectic projective line is orthogonal only to itself, so all \(q+1\) projective points are pairwise nonorthogonal.

## Exact rank-two data and the status of \(S(3,2)\)

[CITED-VERIFIED] If \(q\) is even, De Beule–Klein–Metsch–Storme (2008), author-manuscript p. 8, records that \(W(3,q)\cong Q(4,q)\) contains an elliptic-quadric ovoid and hence
\[
 \pi(q,2)=q^2+1.
\]
The right side is the ovoid number, hence the general counting upper bound as well as the exhibited size.

[CITED-VERIFIED] For odd \(q\), the accessible primary sources give
\[
 2q+1\le \pi(q,2)\le q^2-q+1.
\]
The lower construction is described in Cimráková–De Winter–Fack–Storme (2007), Remark 2.11(2) and §4.1, author-manuscript pp. 5 and 8: delete one point \(r\) from a hyperbolic line and choose one suitable point on each of the \(q+1\) isotropic lines through \(r\).  De Beule–Klein–Metsch–Storme (2008), author-manuscript p. 8, states the upper bound explicitly and cites Tallini and a different proof by Klein–Metsch.  In that proof, duality identifies partial ovoids of \(W(3,q)\) with partial spreads of \(Q(4,q)\); Klein–Metsch (2005), Theorem 3.3, author-manuscript p. 8, proves that a maximal partial spread of \(Q(4,q)\) is either a spread or has size at most \(q^2-q+1\), and the standard odd-\(q\) nonexistence of a spread gives the displayed bound.  The 2010 Klein–Metsch correction, printed p. 237, records that the original Lemma 1.2 was false as stated, replaces the affected proof of Proposition 3.2, and explicitly confirms that the two main results remain true; the correction must be cited with the 2005 paper.

[CITED-VERIFIED] Consequently \(\pi(3,2)=7\) follows theoretically, with no computation: both sides of the preceding inequality equal 7.  Cimráková–De Winter–Fack–Storme also report an exhaustive Java search in §4.1 and Table 1, author-manuscript pp. 8–9, that determines the following maximum values:

| \(q\) | \(\pi(q,2)\) | source status |
|---:|---:|---|
| 3 | 7 | theoretical equality above; also exhaustive complete spectrum |
| 5 | 18 | exhaustive complete spectrum and largest-value search |
| 7 | 33 | exhaustive largest-value search |

[CITED-VERIFIED] The paper says explicitly that the spectra for \(q=2,3,4,5\) are complete and that the largest values for \(W(3,5)\) and \(W(3,7)\) were confirmed by exhaustive search.  Since every maximum partial ovoid is inclusion-maximal, the largest maximal value is \(\pi(q,2)\).  These are verified reports in a primary paper, but the external Java program and independent certificates are not archived in this repository; therefore the \(q=5,7\) rows are not labelled `[COMPUTED]` here.

[CITED-VERIFIED] The seven-point nonorthogonal configuration used for the repository group \(S(3,2)\) is therefore a previously known finite-geometric extremum: it is a maximum partial ovoid of \(W(3,3)\).  The repository's exact group statement \((\nu,a)=(7,10)\), and hence its use against the proposed formula for \(h\), is stronger than this geometric input.

[UNVERIFIED] Searches by `S(3,2)`, order \(3^5\), Heisenberg/extraspecial group, noncommuting graph, symplectic clique, partial ovoid, and abelian cover did not locate a publication giving the combined group invariant \((\nu,a)=(7,10)\).  Thus the seven-point clique ingredient is not novel, while no global novelty claim is made for the cover-number computation or counterexample.

## Higher-rank bounds and constructions

[CITED-VERIFIED] De Beule–Klein–Metsch–Storme (2008), Theorem 3.2 and its proof, author-manuscript pp. 8–9, proves the inductive bound
\[
 \pi(q,m)\le 2+(q-1)\pi(q,m-1)\qquad(m\ge3).
\]
Their proof chooses two points of the partial ovoid, partitions the remaining points according to the unique point of their secant line to which they are perpendicular, and passes to a quotient symplectic space.  For \(q>2\), iteration gives
\[
 \pi(q,m)\le (q-1)^{m-2}\pi(q,2)
 +2\frac{(q-1)^{m-2}-1}{q-2}.
\]

[CITED-VERIFIED] The same paper, Theorem 6.1 and proof, author-manuscript pp. 18–19, gives the sharper small-rank estimate
\[
 \pi(q,3)\le
 1+\frac q2\!\left(\sqrt{5q^4+6q^3+7q^2+6q+1}-q^2-q-1\right).
\]
Its Corollary 6.3 combines this \(W(5,q)\) base with Theorem 3.2 in all higher ranks.  Remark 6.2 notes that for \(q=3\) the rank-two inductive base is better, while Theorem 6.1 becomes better for larger \(q\).

[CITED-VERIFIED] Blokhuis–Moorhouse (1995), Theorems 1.1 and 1.6 (printed pp. 296–297) and Proposition 4.1 (printed p. 316), proves a characteristic-dependent polynomial bound.  If \(q=p^e\), then
\[
 \pi(q,m)\le \binom{p+2m-2}{p-1}^{e}+1.
\]
The proof orders point-hyperplane incidence by the polarity: a polar-space cap gives an identity principal submatrix, so its size is at most the \(p\)-rank of the point-hyperplane incidence matrix of \(PG(2m-1,q)\), whose rank is \(\binom{p+2m-2}{p-1}^{e}+1\).  This direct primary-source indexing is one smaller than the convenient weaker vector-dimension restatement in Bamberg et al. (2024), Theorem 2.1.

[CITED-VERIFIED] For \(q=2\), the preceding bound is \(\pi(2,m)\le2m+1\).  Işık (2005), Theorem 12, pp. 6–7, supplies an explicit \(2m+1\)-point symplectic construction and a matching linear-dependence upper proof, hence
\[
 \pi(2,m)=2m+1\qquad(m\ge1).
\]
This exact binary result is proof-verified from an accessible but unpublished manuscript.

[PROVED] Over every finite field, \(\pi(q,m)\ge2m+1\).  On \(V=\mathbb F_q^{2m+1}\), let \(A\) be the alternating matrix with \(A_{ij}=1\) for \(i<j\), \(A_{ij}=-1\) for \(i>j\), and zero diagonal.  If \(Ax=0\), subtracting consecutive row equations gives \(x_{i+1}=-x_i\), and the first row then vanishes automatically; hence \(\operatorname{rad}(A)\) is one-dimensional and \(A\) has rank \(2m\).  The quotient \(V/\operatorname{rad}(A)\) is a nondegenerate symplectic space, and the images of the \(2m+1\) coordinate points are nonzero and pairwise nonorthogonal because their mutual pairings are \(\pm1\).  Identifying this quotient with the standard symplectic space proves the bound.

[CITED-VERIFIED] Ceria–De Beule–Pavese–Smaldore (2023), Theorem 3.3, author-manuscript p. 7, constructs for every odd square \(q\not\equiv0\pmod3\) a partial ovoid of \(W(3,q)\) of size
\[
 \frac{q^{3/2}+3q-q^{1/2}+3}{3}.
\]
Remark 3.13, author-manuscript p. 12, reports Magma computations that the maximum partial-ovoid size in \(W(5,3)\) is 13, i.e. \(\pi(3,3)=13\).  The article does not provide a repository-verifiable exhaustive certificate, so this is `[CITED-VERIFIED]` as a primary-source computational report, not `[COMPUTED]`.

## Consequences for the scalar-symplectic efficiency

[PROVED] For
\[
 E(q,m)=\frac{\log(q^m+1)}{\pi(q,m)},
\]
the verified bounds imply, for \(q=p^e\),
\[
 \frac{\log(q^m+1)}{\binom{p+2m-2}{p-1}^{e}+1}
 \le E(q,m)\le
 \frac{\log(q^m+1)}{2m+1}.
\]
For \(q=2\) equality \(\pi(2,m)=2m+1\) gives
\[
 E(2,m)\longrightarrow\frac{\log2}{2},
 \qquad (2^m+1)^{1/\pi(2,m)}\longrightarrow\sqrt2.
\]
For fixed \(q>2\), the located general bounds do not determine the limit: the lower efficiency bound is polynomially small while the upper bound tends to \((\log q)/2\).

[PROVED] At rank two and odd \(q\), the verified interval \(2q+1\le\pi(q,2)\le q^2-q+1\) gives
\[
 \frac{\log(q^2+1)}{q^2-q+1}
 \le E(q,2)\le
 \frac{\log(q^2+1)}{2q+1},
\]
so \(E(q,2)\to0\) as odd \(q\to\infty\).  For even \(q\), the exact identity \(\pi(q,2)=q^2+1\) gives \(E(q,2)=\log(q^2+1)/(q^2+1)\to0\).  Thus rank-two efficiency tends to zero through all prime powers.  Using the exact values above (natural logarithm),
\[
 E(2,2)=0.32188758,\quad E(3,2)=0.32894073,\quad
 E(5,2)=0.18100536,\quad E(7,2)=0.11854615.
\]
Thus \(S(3,2)\) slightly improves the rank-two binary efficiency, but remains below the binary large-rank limit \((\log2)/2\approx0.34657359\).

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

## Exterior-square source used by the finite reduction

[CITED-VERIFIED] Brown–Johnson–Robertson (1987), printed p. 181, define the nonabelian exterior square \(Q\wedge Q\) and the commutator homomorphism \(Q\wedge Q\to Q'\), whose kernel is the Schur multiplier.  Proposition 7, printed p. 182, constructs the lift-commutator crossed pairing for a central extension.  Corollary 2, printed pp. 182–183, then states that for a covering group \(S\) of \(Q\) the induced map
\[
 Q\wedge Q\longrightarrow S'
\]
is an isomorphism whenever \(H_2(Q)\) is finitely generated.  In particular it applies to the finite groups \(Q\) used in the repository enumeration.  The checked DOI is `10.1016/0021-8693(87)90248-1`; the complete author-hosted primary PDF was read.

## An exact five-subgroup-cover theorem

[CITED-VERIFIED] Bryce–Fedri–Serena (1997) define \(f(k)\) as the largest index \([G:D]\), over groups \(G\) with an irredundant cover by \(k\) subgroups whose intersection is \(D\).  Theorem 1.2, printed p. 470, proves
\[
 f(5)=16.
\]
The proof on printed pp. 475–476 first classifies maximal irredundant core-free five-covers in Theorem 1.1 and then handles nonmaximal covers by replacing one member with a maximal subgroup and reducing to irredundant three- or four-covers.  The theorem is about arbitrary subgroup covers, not specifically abelian or centralizer covers.

[PROVED] If \(\nu(G)=5\), choose a maximum pairwise noncommuting set \(X=\{x_1,\ldots,x_5\}\).  The centralizers \(C_G(x_i)\) cover \(G\), since otherwise an element outside their union could be adjoined to \(X\); the cover is irredundant because \(x_i\) belongs to no \(C_G(x_j)\) for \(j\ne i\).  Its intersection is exactly \(Z(G)\): if \(y\) centralizes every \(x_i\), then \(X\subseteq C_G(y)\), while repository Lemma CB.2 gives \(\nu(C_G(y))\le3\) for every noncentral \(y\), a contradiction.  Applying Bryce–Fedri–Serena therefore yields the exact-cover consequence
\[
 [G:Z(G)]\le16\qquad\text{when }\nu(G)=5.
\]
Only the five-cover index theorem is `[CITED-VERIFIED]`; the bridge from a maximum noncommuting set to intersection \(Z(G)\) is the displayed repository proof.

### What the later \(\omega(G)=5\) classification lead does—and does not—verify

[UNVERIFIED] Jafarian Amiri–Rostami (2017), introduction, printed p. 194, says that its references [17] and [20] “determined all groups \(G\) with \(\omega(G)=5\).”  The two referenced primary papers are Jafarian Amiri–Madadi (2016), DOI `10.1142/S0219498816501978`, and Jafarian Amiri–Madadi–Rostami (2017), DOI `10.1515/ms-2017-0038`.  The first paper's publisher preview (printed p. 1) says only that it describes *structural properties* of all such finite groups; the second paper's official abstract treats only finite F-groups with \(|G:Z(G)|=p^4\).  Neither full proof-bearing article was accessible in this audit, so the secondary phrase “determined all groups” is not promoted to a classification theorem here.

[CITED-VERIFIED] The list
\[
 G/Z(G)\cong D_8,\ C_2^3,\ A_4,\text{ or }C_2^4
\]
was located in Abdollahi–Jafarian Amiri–Mohammadi Hassanabadi (2007), printed p. 44, but with a different scope: that paper reports Ashrafi's earlier result that a **finite 6-centralizer group** has one of exactly these four central quotients.  It is not stated there as a classification of all groups with \(\omega(G)=5\).  The original Ashrafi proof-bearing papers were not acquired, so the underlying classification remains `[UNVERIFIED]` even though the 2007 report and its scope are checked.

[UNVERIFIED] The 6-centralizer list cannot be transferred to every group with \(\omega(G)=5\): the equality “number of element-centralizers = \(\omega(G)+1\)” needs additional conditions (for example the CA setting), and a bare central-factor isomorphism does not preserve commutation in \(G\).  The official abstract of the Mathematica Slovaca paper moreover assumes that \(G\) is a finite F-group with \(|G:Z(G)|=p^4\); an F-group need not be a CA-group by definition.  Thus neither lead currently proves that five clique-centralizers are abelian or that \(a(G)=5\).  The load-bearing conclusion from the audited literature is the proved center-index bound \([G:Z(G)]\le16\), not an externally verified value of \(h(5)\).

## Six-subgroup covers and the exact value \(h(6)=6\)

[CITED-VERIFIED] Abdollahi–Ataei–Jafarian Amiri–Mohammadi Hassanabadi, “Groups with a Maximal Irredundant 6-Cover,” determine the corresponding cover index as
\[
 f(6)=36.
\]
The exact hypothesis and conclusion appear as Theorem D on printed p. 72 of the authors' 2004 seminar extended abstract: 36 is the largest \(|G:D|\) over groups having an irredundant six-subgroup cover with intersection \(D\).  The official abstract of the 2005 *Communications in Algebra* article states the same result.  The full journal article remained closed, but Alencar's open 2011 UFC dissertation reconstructs the argument in full in Chapter 5, §5.1, printed pp. 77–88.  Since the dissertation is secondary, the precise dependency audit below—not the bare citation—is needed before this theorem can be load-bearing.

### Proof reconstruction and dependency audit for \(f(6)=36\)

[CITED-VERIFIED] Three low-cover inputs are available from the full primary Bryce–Fedri–Serena paper.  Their Proposition 2.3, printed p. 470, restates Scorza's three-cover classification; Proposition 2.4 on the same page gives the complete Greco four-cover classification; and Theorem 1.2 with proof on pp. 475–476 gives \(f(5)=16\).  In particular, a core-free irredundant four-cover has group order in \(\{6,8,9\}\); the order-eight cases are nonmaximal 2-groups, and the order-nine cases are supersoluble.  These are the exact consequences used below.  This primary restatement must be used in place of Alencar's visibly corrupted transcription of Proposition 5.2 on printed pp. 79–80.

[DISPROVED] The published maximal-cover list cannot be imported verbatim.  The primary 2005 paper's Lemma 4.1(3), as quoted with its page number and GAP code in a public 2011 question, explicitly includes \(S_3\times S_3\) among the asserted subdirect-product cases; Ataei (2018), Theorem 1.2, printed pp. 110–111, repeats that item in a nine-case list.  The accessible 2004 extended abstract's printed Theorem C on p. 68 omits \(S_3\times S_3\), so it does not share this particular error.  The 2005/2018 item is not correct: the repository's exact modern-GAP audit finds that \(\operatorname{SmallGroup}(36,10)\cong S_3\times S_3\) has 38 six-subgroup covers, all redundant, and hence no maximal irredundant six-cover.  Alencar's later Theorem 4.1, printed pp. 73–76, also omits this false positive and includes the genuine order-36 case
\[
 \operatorname{SmallGroup}(36,13)\cong C_2\times((C_3^2)\rtimes C_2),
\]
where the order-18 factor is centerless.  Thus the omission is a correction, not an accident.  After deleting the false \(S_3\times S_3\) item, the stated families still give
\[
 |G:D|\in\{10,18,20,24,25,27,36\},
\]
so only the consequence \(|G:D|\le36\) is used.  Alencar's proof of the classification in Chapters 2–4 depends materially on enumerative GAP Lemma 4.1, printed pp. 51–59.  The repository reconstruction in `notes/exact_h6.md` audits every structural branch, repairs two logical gaps, and maps each remaining finite leaf to a modern exhaustive certificate.  The independent multiplication-table verifier reconstructs every subgroup and tests all 5,545,351 six-subsets.  Thus the source list remains erroneous, while the corrected maximal upper consequence is repository `[PROVED]` by a computer-assisted proof.

[PROVED] With the corrected maximal-case consequence, the rest of the upper-bound argument is self-contained and uses only the three verified low-cover results.  Let \(G=H_1\cup\cdots\cup H_6\) be irredundant with intersection \(D\).  Quotient by \(D_G\); Alencar Proposition 5.3, printed p. 80, gives an irredundant six-cover with core-free intersection and preserves \(|G:D|\).  If all six members are maximal, the preceding corrected consequence gives \(|G:D|\le36\).  Otherwise select, among counterexamples with \(|G:D|>36\), a cover having as many maximal members as possible.  Enlarge a nonmaximal \(H_1\) to a maximal \(H_1^*\).  The enlarged six-cover must be redundant: if it were irredundant, the intersection of any five members would still be \(D\), so it would be another core-free counterexample with more maximal members.

[PROVED] Any irredundant subcover of the enlarged cover contains \(H_1^*\) and has size 5, 4, or 3.  It cannot have size 2, since a group is not the union of two proper subgroups.

- If it has size 5, write its intersection as \(D_1\).  Then \(|G:D_1|\le f(5)=16\), while the standard intersection lemma for the original six-cover gives \(|D_1:D|\le2\).  Hence \(|G:D|\le32\).

- If it has size 4, write \(G=H_1^*\cup H_2\cup H_3\cup H_4\), with intersection \(D_1\).  The verified four-cover classification gives \(|G:D_1|\in\{6,8,9\}\).  For 6, the intersection of \(H_2,H_3,H_4\) equals \(D_1\), and the factorial coset lemma below gives \(|D_1:D|\le3!=6\), hence \(|G:D|\le36\).  Alencar printed pp. 83–86 treats 9 and 8 by inducing covers inside \(H_1^*\): when the relevant induced cover is irredundant, the verified three-/four-cover bounds give products no larger than \(3\cdot12=36\); if it is redundant, its essential three- or four-member subcover gives a still smaller product.  In the order-eight case, Greco says the quotient is a 2-group and the maximal/nonmaximal indices force \(|G:H_1^*|=2\) and \(|H_1^*:D_1|=2\), contradicting \(|G:D_1|=8\).  Thus no four-subcover branch exceeds 36.

- If it has size 3, Scorza gives \(|G:H_1^*|=2\) and \(|G:D_1|=4\).  Intersecting the three unused original members with \(H_1^*\), together with \(H_1\) and possibly \(D_1\), produces a cover of \(H_1^*\) with at most five essential members.  If five are essential, \(|H_1^*:D|\le16\), so \(|G:D|\le32\).  If four are essential, Greco and the original-cover intersection lemma give at most \(2\cdot9\cdot2=36\); if three are essential, Scorza gives a smaller value.  Alencar carries out these subcases on printed pp. 86–88.

[PROVED] The factorial coset lemma used in the order-six four-subcover branch is proved completely by Alencar, Lemma 5.1, printed pp. 80–82, and has a short independent reconstruction.  If \(G=H_1g_1\cup\cdots\cup H_ng_n\) is an irredundant right-coset cover and \(D=\bigcap_iH_i\), then for every \(r\in\{0,\ldots,n-1\}\),
\[
 \left|\bigcap_{i=1}^{n-r}H_{\rho(i)}:D\right|\le r!
\]
for every permutation \(\rho\).  Induct on \(r\).  Choose a witness \(x\) outside the first \(n-r\) covering cosets.  Multiplying \(K=\bigcap_{i=1}^{n-r}H_{\rho(i)}\) by \(x\) shows \(Kx\) is covered by the remaining \(r\) cosets.  Each nonempty intersection of \(Kx\) with one such coset is a coset of \(K\cap H_j\); by induction each \(K\cap H_j\) contains \(D\) with index at most \((r-1)!\).  Thus \(K\) is a union of at most \(r(r-1)!=r!\) cosets of \(D\).

[COMPUTED] The lower bound 36 is witnessed by \(\operatorname{SmallGroup}(36,13)\cong C_2\times((C_3^2)\rtimes C_2)\), not by \(S_3\times S_3\).  GAP 4.16.0 with SmallGrp 1.5.4 enumerated all \(\binom{15}{6}=5005\) six-tuples of maximal subgroups: 306 are irredundant covers, and exactly 72 have core-free (indeed trivial) intersection.  The machine-readable witnesses are in `experiments/logs/f6_maximal_cover_groups.tsv`, with the concise audit log in `experiments/logs/f6_maximal_cover_gap.stdout.txt`.  Together with the repaired maximal upper proof and the checked nonmaximal reduction, this proves \(f(6)=36\) in the repository; the same equality remains independently `[CITED-VERIFIED]` as an external theorem.

[PROVED] If \(\nu(G)=6\), the centralizers of a maximum noncommuting set form an irredundant six-cover.  If their intersection contained a noncentral \(y\), all six clique elements would lie in \(C_G(y)\), contradicting repository Lemma CB.2, which gives \(\nu(C_G(y))\le4\).  Hence the intersection is \(Z(G)\), and the six-cover theorem gives
\[
 [G:Z(G)]\le36\qquad\text{when }\nu(G)=6.
\]
This center-index reduction does not by itself say that the six centralizers are abelian.  The repository's subsequent complete exterior-square enumeration supplies the missing coloring statement.

[PROVED] The finite central-quotient audit is now complete by a computer-assisted proof.  A structural alternating-map lemma excludes the only infeasible raw enumeration, \(Q=C_2^5\).  For the other 161 quotient types of order at most 36, all 23,527 action-invariant exterior-square kernels were enumerated; every faithful graph of clique number at most six has chromatic number at most six.  With the Heisenberg lower witness this proves \(h(6)=6\).  The literature search still found no external classification or perfect-graph theorem that gives this exact value directly.

## The seven-subgroup cover theorem

[CITED-VERIFIED] Abdollahi–Jafarian Amiri, Theorem B, printed pp. 292 and 299–300, proves
\[
 f(7)=81.
\]
The complete published article was read through the author's public ResearchGate upload.  The lower bound is furnished on pp. 292–293 by the explicit maximal irredundant seven-cover of \((C_3)^4\), whose trivial intersection gives index (81).  (The displayed sentence at the end of Theorem 2.2 says \((C_3)^6\), but the generators and the theorem itself are for \((C_3)^4\); this is a source typo.)

[CITED-VERIFIED] The maximal case is Theorem A, printed pp. 291–292: every maximal irredundant core-free seven-cover lies in a seven-family classification, and direct calculation gives \(|G:D|\le81\).  Its proof occupies pp. 292–299.  The article explicitly says on p. 293 that GAP 4.3 is used in Lemma 4.1 to enumerate covers and determine \(|D|\); Lemmas 4.3, 4.4, and 4.7 handle cases too large for that enumeration partly by hand, but Lemma 4.4 still invokes a separate GAP check on a seven-cover of an elementary abelian Sylow subgroup.  The paper gives neither complete code nor saved logs or certificates.  Thus the theorem is valid `[CITED-VERIFIED]` external evidence, but its computational classification is not repository `[COMPUTED]` and is not yet a self-contained repository proof.

[PROVED] Assuming Theorem A's maximal-case consequence, the final reduction on pp. 299–300 has been reconstructed and checked.  Quotient first by the core of the cover intersection.  From a putative irredundant seven-cover with \(|G:D|>81\), choose one with as many maximal members as possible and enlarge a nonmaximal member.  The enlarged cover is redundant.  An essential six-subcover gives \(|G:D|\le f(6)\cdot2=72\).  An essential five-subcover uses \(f(5)=16\) and the factorial intersection bound \(|D_1:D|\le3!=6\); the only nominal value above 81 is 96, and the index analysis on pp. 299–300 excludes it.  An essential four-subcover is split using Greco into indices \(9,6,8\) and induces covers inside the enlarged maximal subgroup; all branches are at most 81 or contradictory.  Finally an essential three-subcover induces a six-cover in that maximal subgroup and yields at most \(2f(6)=72\).  Consequently the only unaudited repository edge in this reduction is the external/computational seven-cover maximal-case classification; the formerly open \(f(6)=36\) repository edge is now closed above.

[PROVED] For an arbitrary group with \(\nu(G)=7\), the repository's universal
center-index bound first makes \(Q=G/Z(G)\) finite.  Maximum-clique
centralizers contain the center, descend to an irredundant seven-subgroup
cover of this finite \(Q\), and repository Lemma CB.2 makes their intersection
trivial in \(Q\).  The cited finite seven-cover theorem therefore gives
\[
 [G:Z(G)]\le81\qquad\text{when }\nu(G)=7.
\]
This is a center-index bound, not an abelian-cover theorem; it does not contradict the repository example with \((\nu,a)=(7,10)\).

## What is known specifically when \(\nu(G)=7\)

[CITED-VERIFIED] Zarrin, Theorem 1.1 and Lemma 2.1, printed pp. 43--44, apply to an arbitrary group with finite clique number: isoclinism preserves \(\nu\), and every such group is isoclinic to a finite group with the same \(\nu\).  The proof first uses Pyber to make the central quotient finite, then Hall's stem-group theorem and Schur's theorem to make the stem representative finite.

[PROVED] The repository's exact central-coset graph translation strengthens that source statement for the present problem: the isoclinism isomorphism \(G/Z(G)\cong K/Z(K)\), together with the compatible commutator maps in Zarrin's definition on p. 43, preserves commutation in both directions.  It is therefore an isomorphism of the compressed noncommuting graphs, so it preserves both \(\nu=\omega\) and \(a=\chi\).  Hence every arbitrary group with finite \(\nu\), in particular with \(\nu=7\), has a finite isoclinic representative with the same pair \((\nu,a)\).  This makes the finite reduction valid for \(h(7)\), although it supplies no classification of the resulting finite groups.

[CITED-VERIFIED] Zarrin, Theorem 1.2, stated on p. 43 and proved on p. 44, says that every arbitrary group with \(\nu\le20\) is soluble, with sharp threshold \(21=\nu(A_5)\).  Its finite load-bearing input is Endimioni's 1994 theorem, whose original three-page article was not acquired here.  The independently accessible primary paper of Abdollahi--Azad--Mohammadi Hassanabadi--Zarrin gives a stronger finite classification at cutoff 57: Theorem 1.1, printed p. 2 with proof on pp. 4--9, lists every finite nonsoluble group with \(\nu\le57\); every listed family has clique number at least 21.  Consequently the solvability conclusion at \(\nu=7\) has a proof-bearing accessible primary route, although it does not bound \(a(G)\) or the derived length sharply enough to determine \(h(7)\).

[CITED-VERIFIED] Darafsheh--Ghorbani--Prajapati give useful but conditional small-central-quotient pruning.  Theorems 1.2 and 1.3, printed p. 381 and proved on pp. 387--388, show that if \(p\) is the smallest prime dividing a finite nonabelian group and \(|G/Z(G)|=p^2\) or \(p^3\), then \(G\) is an AC-group; the respective clique numbers are \(p+1\) and \(p^2+(1-\delta)p+1\).  For a \(p\)-group with quotient \(p^3\), Remark 5.2, p. 388, specializes this to \(p^2+p+1\) when there is no abelian maximal subgroup and \(p^2+1\) when there is one.  Thus, within the \(p\)-group cases of quotient order \(p^3\le81\), \(\nu=7\) occurs only at \(p=2\), quotient order eight, with no abelian maximal subgroup; the order-27 \(p\)-group branches have clique number 13 or 10.  The more general theorem leaves the parameter \(\delta\) and is not by itself a full order-27 classification.  Lemma 2.4, p. 382, also shows that an AC-group's distinct proper element-centralizers are abelian and give both a maximum noncommuting set and an abelian cover, so \(a(G)=\nu(G)\) in this AC slice.  These results do not cover central quotients of orders 16, 32, 64, 72, 80, or 81, and do not cover the repository's non-AC group \(S(3,2)\).

[CITED-VERIFIED] Results for groups with a prescribed **number of element-centralizers** must not be substituted for results about \(\nu\).  Zarrin, Theorem 3.5(4), printed p. 45, classifies 7-centralizer groups by three central quotients, but the same page proves only \(1+\nu(G)\le |\mathcal C(G)|\).  Thus a group with \(\nu=7\) has at least eight element-centralizers and need not be a 7-centralizer group.  Likewise, Jafarian Amiri--Madadi--Rostami, Lemma 3.1, in the published open article on 10-centralizer groups, gives \(|G/Z(G)|=16\) under the joint hypotheses \(|\mathcal C(G)|=10\) and \(\nu\in\{5,6,7,8\}\); it is only a conditional order-16 slice, not a classification of all \(\nu=7\) groups.

[UNVERIFIED] Exact-title, formula, and terminology searches through the 2026-08-13 research cut-off found no primary source claiming the exact value of \(h(7)\), a direct universal bound \(h(7)\le10\), or a classification of all groups with \(\nu=7\).  Searches separately excluded papers in which “\(\omega(G)=7\)” counts automorphism orbits, papers about 7-centralizer groups, and papers whose \(\omega\) and \(\chi\) refer to a generating graph.  In particular, a located statement \(\omega=\chi\) for finite nilpotent groups belongs to the generating graph defined immediately before it and supplies no noncommuting-graph theorem.  This is an index-bounded negative result about the external literature, not a proof of absence.

[PROVED] Independently of that negative literature search, repository Theorem
H7.19 proves \(h(7)=10\) for arbitrary groups.  The upper bound first reduces
to a finite center quotient of order at most 81, then gives a disjoint exact
disposition of all 738 quotient types through exterior-square kernels,
zero-row obstructions, dual-character searches, and three dedicated
order-64 certificates.  The group \(S(3,2)\) supplies the matching lower
witness \((\nu,a)=(7,10)\).  The complete proof and dependency labels are in
`notes/exact_h7.md`.

## Forward citations and possible later resolutions

[CITED-VERIFIED] Maróti, Martínez and Moretó (2025), printed p. 2, cite Pyber while defining the coclique/abelian-cover number of a noncommuting graph, but the paper's new theorems concern covers of the set of \(p\)-elements by proper subgroups.  Its full text contains no new universal estimate for \(h(n)\), \([G:Z(G)]\) in terms of \(\omega(G)\), or the exponential base.

[UNVERIFIED] The 2024–2026 forward items located through OpenAlex and DOI/title searches—work on pseudo-conjugation/isoclinism, numbers of pairwise noncommuting sets, cyclic-subgroup counts, fixed-point ratios and covers of \(p\)-elements, and hyperplane/coset covers—have abstracts or full texts whose stated scope is different from Erdős Problem 117.  In particular, the 2026 hyperplane-cover paper concerns a different Pyber conjecture about irredundant coset covers of finite abelian groups.

[UNVERIFIED] The forward search found no 2025 or 2026 paper claiming a resolution of Problem 117, the candidate exact formula, or an improved/determined asymptotic exponential constant.  This is an index-bounded negative result, not proof that no such paper exists.

## Load-bearing gaps

[UNVERIFIED] The two principal inaccessible sources are Pyber's full 1987 article (needed for its exact Theorem 6.1, constants, hypotheses, and proof) and Bertram's printed p. 40 (needed to inspect what was actually transmitted from Isaacs).  Neither may be used as a black box for a final solution.

[UNVERIFIED] Before any novelty claim, the project still needs lawful full-text access to Pyber and Bertram or must avoid depending on them. The repository now supplies independent proofs of the exact finite commutation-model reduction and of the scalar symplectic cover formulas, so those particular statements are no longer source gaps. The explicit Pyber fixed-base upper bound and the historical Isaacs/Bertram provenance remain unresolved. The disproved binary candidate is no longer a live proof target.
