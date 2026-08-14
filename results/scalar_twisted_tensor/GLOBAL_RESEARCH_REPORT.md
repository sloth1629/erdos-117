# GLOBAL RESEARCH REPORT

## Erdős Problem 117: a twisted-tensor barrier for the entire scalar-symplectic class

**Date:** 2026-08-14
**Research scope:** the full problem was screened globally; the certifiable theorem obtained is a sharp asymptotic classification of the scalar-symplectic lower-construction class.
**Evidence convention:** every substantive assertion is marked by exactly one of `[PROVED]`, `[CITED-VERIFIED]`, `[COMPUTED]`, `[CONJECTURE]`, `[DISPROVED]`, or `[UNVERIFIED]`.
**Logarithm convention:** `log` denotes the natural logarithm; `log_2` is written explicitly.

---

# 1. Outcome first

For a prime power \(q\) and \(m\ge 1\), let

\[
S(q,m)=\mathbb F_q^m\times \mathbb F_q^m\times \mathbb F_q
\]

with the audited multiplication

\[
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+x\cdot y').
\]

Let \(\pi(q,m)\) be the maximum size of a set of pairwise nonorthogonal projective points in the symplectic space \(W(2m-1,q)\). The context packet proves

\[
a(S(q,m))=q^m+1,\qquad \nu(S(q,m))=\pi(q,m).
\]

Define the scalar-symplectic envelopes

\[
h_{\mathrm{sc}}(n)
 =\max\bigl(\{1\}\cup\{q^m+1:\pi(q,m)\le n\}\bigr)
\]

and

\[
h_{\mathrm{sc},\ne2}(n)
 =\max\bigl(\{1\}\cup\{q^m+1:q\ge3,\ \pi(q,m)\le n\}\bigr),
\]

where \(q\) ranges over prime powers.

## The strongest result obtained

### Theorem A — twisted-tensor seed tower `[PROVED]`

For every prime power \(q\) and every odd integer \(t\ge1\),

\[
\boxed{\pi\!\left(q,2^{t-1}\right)\ge q^t+1.}
\tag{A.1}
\]

The construction is explicit. It embeds the \(q^t+1\) points of \(\operatorname{PG}(1,q^t)\) into a \(2^t\)-dimensional symplectic \(\mathbb F_q\)-space so that the pairing of two distinct image points is the nonzero norm of their \(2\times2\) determinant.

### Theorem B — nonbinary scalar fields are asymptotically inefficient `[PROVED]`

For every fixed prime power \(q>2\),

\[
\boxed{
\lim_{m\to\infty}
 \frac{\log(q^m+1)}{\pi(q,m)}=0.
}
\tag{B.1}
\]

More strongly, uniformly over all prime powers \(q\ge3\),

\[
\boxed{
\frac{\log(q^m+1)}{\pi(q,m)}\longrightarrow0
\quad\text{whenever}\quad \pi(q,m)\longrightarrow\infty.
}
\tag{B.2}
\]

Consequently,

\[
\boxed{\log h_{\mathrm{sc},\ne2}(n)=o(n)}
\qquad\text{and}\qquad
\boxed{\lim_{n\to\infty}h_{\mathrm{sc},\ne2}(n)^{1/n}=1.}
\tag{B.3}
\]

Thus every nonbinary scalar-symplectic family is subexponential in its noncommuting-clique parameter, even if the field is allowed to vary with the dimension.

### Theorem C — exact exponential rate of the whole scalar class `[PROVED]`

\[
\boxed{
\lim_{n\to\infty}h_{\mathrm{sc}}(n)^{1/n}=\sqrt2.
}
\tag{C.1}
\]

The binary family is not merely one scalar construction attaining the rate: it is the only scalar field regime that contributes a nontrivial asymptotic exponential base. More precisely, the \(q=2\) models have

\[
(\nu,a)=(2m+1,2^m+1),
\]

whereas the union of all \(q\ge3\) models has exponential base one.

### Theorem D — a pointwise scalar barrier `[PROVED]`

For every prime power \(q\) and \(m\ge1\), except \((q,m)=(2,1)\),

\[
\boxed{q^m+1\le 2^{\pi(q,m)/2}.}
\tag{D.1}
\]

The exceptional model has

\[
(\pi(2,1),2^1+1)=(3,3),\qquad 3^{1/3}>\sqrt2.
\]

Equality in (D.1) occurs at \((q,m)=(3,1)\), where \((\nu,a)=(4,4)\); all other nonexceptional cases in the proof are strict. In particular,

\[
\boxed{h_{\mathrm{sc}}(n)\le2^{n/2}\quad(n\ge4).}
\tag{D.2}
\]

## What this settles

`[PROVED]` This resolves a broad constructional subproblem at priority level 3 of the research brief: no scalar-valued, field-linear symplectic group \(S(q,m)\), over any varying sequence of finite fields, can beat the binary asymptotic base \(\sqrt2\).

`[PROVED]` The conclusion also applies to any finite group with the same exact central-coset commutation graph as one of these models—for example, any class-two realization whose central commutator geometry is a nondegenerate scalar-valued alternating \(\mathbb F_q\)-form—because both \(\nu\) and \(a\) are graph invariants of that compressed model.

`[PROVED]` Any sequence of constructions with \(\nu(G_i)\to\infty\) and asymptotic efficiency

\[
\limsup_{i\to\infty} \frac{\log a(G_i)}{\nu(G_i)}>\frac{\log2}{2}
\]

must leave the scalar-symplectic class. Within class two, it must therefore use genuinely higher-codomain commutator maps, non-field-linear geometry, or another mechanism not isoclinic to these scalar models.

`[UNVERIFIED]` The theorem does not rule out a better construction among higher-codomain alternating maps, higher nilpotency class groups, or nonnilpotent groups.

`[UNVERIFIED]` Erdős Problem 117 is not solved and the universal exponential rate is not determined.

`[PROVED]` The surrounding repository subsequently proved \(h(8)=10\) by an
independent exact argument.  The scalar theorem here neither uses nor implies
that cutoff-eight result; historical Phase-I rows below record the state of
the source packet when this research run began.

`[PROVED]` No CFSG, classification table, choice beyond finite selections, inaccessible paper, or computation is used in Theorems A–D. The included computation is an independent, non-load-bearing sanity certificate.

---

# 2. Phase I — generate and kill ideas

The screening phase used the packet's exact examples and warnings as adversarial tests. “Verdict” is intentionally separate from the evidence label.

| # | Candidate mechanism | Exact lemma or construction required | Consequence for \(h(n)\) | Tests against audited examples and boundary cases | First nontrivial obstruction | Verdict |
|---:|---|---|---|---|---|---|
| 1 | Twisted-tensor partial-ovoid seed tower | `[PROVED]` For every prime power \(q\) and odd \(t\), construct \(q^t+1\) pairwise nonorthogonal points in dimension \(2^t\), proving \(\pi(q,2^{t-1})\ge q^t+1\). | `[PROVED]` Orthogonal gluing makes every fixed \(q>2\) scalar family subexponential in \(\nu\), and isolates \(q=2\) as the unique scalar source of the \(\sqrt2\) rate. | `[PROVED]` It gives \(q+1\) in a plane at \(t=1\), \(q^3+1\) in \(W(7,q)\) at \(t=3\), gives the exact binary size \(2m+1\) on dimensions \(m=2^{t-1}\), and is valid in characteristic two. | `[PROVED]` The construction controls only scalar-valued symplectic models; it gives no universal upper bound for arbitrary groups. | **survives; selected** |
| 2 | A one-step exponential centralizer potential | `[CONJECTURE]` There is a constant \(C\) such that for every maximum clique \(S\), \(\sum_{x\in S}C^{-(\nu(G)-\nu(C_G(x)))}\le1\). | `[CONJECTURE]` A weighted centralizer-cover induction would give \(a(G)\le C^{\nu(G)}\). | `[DISPROVED]` In the binary scalar group with \(\nu=2m+1\), every noncentral centralizer has clique number \(2m-1\), so every summand is \(C^{-2}\) and the sum is \((2m+1)C^{-2}\), unbounded in \(m\). | `[DISPROVED]` Individual local drops cannot absorb the growing number of centralizers. | **fails** |
| 3 | Charge the non-isotropic quotient above a maximal abelian layer | `[CONJECTURE]` There is an absolute constant \(C\) such that every finite class-two \(p\)-group \(P\), with \(m=\nu(P)\), has a maximal abelian \(A\ge Z(P)\) satisfying \([P:A]\le C^m\), complementary to the packet's proved \([A:Z(P)]\le p^{m/p}\). | `[CONJECTURE]` Combining the two indices would yield a fixed-base upper bound for class-two \(p\)-groups and possibly a reduction target for all groups. | `[PROVED]` The packet's abelian-layer theorem passes abelian, large-center, and characteristic-two cases; `[DISPROVED]` a bound on \([P:A]\) purely in terms of \([A:Z(P)]\) fails for exterior-product maps with one-dimensional maximal isotropic spaces in arbitrarily large ambient dimension. | `[UNVERIFIED]` No quantity has been found that charges the anisotropic quotient while tracking \(\nu\). | **unclear** |
| 4 | Higher-codomain rank-metric or subspace-design construction | `[CONJECTURE]` Construct radical-free alternating maps \(\beta_i:V_i\times V_i\to W_i\) whose isotropic-subspace cover numbers satisfy \(\log a(\beta_i)>(\log2/2+\varepsilon)\nu(\beta_i)\). | `[CONJECTURE]` This would beat the binary lower constant and refute scalar extremality for the full problem. | `[PROVED]` It is not contradicted by \(S(3,2)=(7,10)\), because that example is scalar and only a finite-parameter improvement. `[PROVED]` In characteristic two, any group realization must use a triangular bilinear cocycle, not \(\beta\) itself. | `[UNVERIFIED]` Simultaneously proving a small nonorthogonal clique number and a large isotropic-cover number is the central unsolved design problem. | **unclear; backup** |
| 5 | Central amalgamation giving a Fekete operation | `[CONJECTURE]` Define a group or alternating-map composition \(G\star H\) with \(\log a(G\star H)\ge\log a(G)+\log a(H)-O(1)\) and \(\nu(G\star H)\le\nu(G)+\nu(H)+O(1)\). | `[CONJECTURE]` Fekete's lemma would then produce an exponential rate and amplify any efficient seed. | `[DISPROVED]` Ordinary direct products have OR-product commutation graphs and do not have the needed additive/multiplicative formulas. `[PROVED]` Central products can cancel commutators identified in the common center, so a noncommuting set does not transfer without a lifting argument. | `[UNVERIFIED]` No amalgamation invariant prevents commutator cancellation while preserving the abelian-cover lower bound. | **unclear** |
| 6 | Fixed powers of one good seed | `[CONJECTURE]` One would need clique multiplicativity and chromatic multiplicativity for the seed's OR powers. | `[CONJECTURE]` A seed with \(a>\nu\) would then appear to yield exponential growth. | `[DISPROVED]` The packet proves that direct powers have rates \(\chi_f(\Gamma)^k\) and \(\Theta(\overline\Gamma)^k\), hence only a polynomial relation between \(a\) and \(\nu\). General OR-product equality also fails. | `[DISPROVED]` The parameter \(\nu(G^k)\) itself grows exponentially in \(k\), so \(a(G^k)\) is only polynomial in that parameter. | **fails** |
| 7 | Historical odd-circuit route for the binary cutoff-eight branch | `[CONJECTURE]` The odd-circuit maximalized cover alone forces either a maximal exact centralizer or a ten-subgroup abelian cover. | `[PROVED]` The branch was later closed by a different exact argument in the surrounding repository. | `[PROVED]` The lemma is true when one maximum-clique centralizer is maximal. `[DISPROVED]` Arbitrarily replacing several exact centralizers by private-cell subgroups fails already in the binary rank-three symplectic example. | `[UNVERIFIED]` The odd-circuit mechanism itself still lacks the lost exact private-cell data. | **superseded** |
| 8 | Historical fixed-subgroup route for the solvable cutoff-eight branch | `[CONJECTURE]` The eight induced fixed subgroups on the core satisfy a direct cover/core inequality. | `[PROVED]` The branch was later closed by a different common-core argument in the surrounding repository. | `[PROVED]` The source packet already restricted the quotient skeleton to an abelian factor times one of seven affine groups. | `[UNVERIFIED]` The proposed direct fixed-subgroup inequality was not proved. | **superseded** |
| 9 | A fixed-base coset-cover theorem specialized to BFC centralizer covers | `[CONJECTURE]` Prove \([A:\bigcap H_i]\le C^k\) for the particular irredundant abelian coset covers produced by commutator centralizers, with a fixed explicit \(C\). | `[CONJECTURE]` Combined with the audited BFC derived-subgroup reduction, this would give a universal fixed-base exponential upper bound for \(h(n)\). | `[PROVED]` The valid published general theorem only gives \(\exp(O(k\log\log k))\). `[DISPROVED]` The earlier advertised fixed-base preprint is withdrawn and unusable. | `[UNVERIFIED]` The extra algebraic structure distinguishing centralizer-origin covers from arbitrary covers has not been converted into a quantitative invariant. | **unclear** |
| 10 | Abelian-complement Frobenius groups as lower constructions | `[PROVED]` If \(G=V\rtimes H\) is a Frobenius group with abelian complement \(H\)—so every nonidentity element of \(H\) acts fixed-point-freely on \(V\)—then for any \(1\ne h\in H\), \(Vh\) is a clique of size \(\lvert V\rvert\), and adjoining any nonzero element of \(V\) gives a clique of size \(\lvert V\rvert+1\). The kernel and the \(\lvert V\rvert\) conjugates of \(H\) give an abelian cover of size at most \(\lvert V\rvert+1\). | `[DISPROVED]` Along such families, \(\log a(G)/\nu(G)\le\log(\lvert V\rvert+1)/(\lvert V\rvert+1)\to0\), so they cannot improve the exponential lower base. | `[PROVED]` The conclusion includes the smallest affine/Frobenius examples and is unaffected by large abelian kernels. | `[DISPROVED]` The same large affine fibre that supplies many abelian subgroups also supplies a comparably large clique. | **fails in this scope** |

## 2.1 Screening certificates for the decisive failures

### Centralizer-potential counterfamily `[DISPROVED]`

In a binary scalar symplectic group of rank \(m\), a noncentral vector \(v\) has centralizer geometry \(v^\perp\). Its radical is \(\langle v\rangle\), and the quotient \(v^\perp/\langle v\rangle\) is a nondegenerate binary symplectic space of dimension \(2m-2\). Central radical clones do not change clique number, so Lemma 4.10 gives

\[
\nu(C_G(v))=2(m-1)+1=2m-1.
\]

Thus every clique-member centralizer has drop two, while a maximum clique has \(2m+1\) members. Any proposed fixed \(C\) in Candidate 2 would require \((2m+1)C^{-2}\le1\) for all \(m\), which is impossible.

### Exterior-product obstruction to comparing the two abelian indices `[DISPROVED]`

Let \(V\) be an \(r\)-dimensional vector space and take

\[
\beta(v,w)=v\wedge w\in\Lambda^2V.
\]

Then \(\beta(v,w)=0\) exactly when \(v,w\) are linearly dependent. Hence every isotropic subspace has dimension at most one, while the ambient dimension \(r\) is arbitrary. This disproves any attempt to bound the ambient-to-isotropic index solely by the size of a maximal isotropic subspace. It does not disprove Candidate 3's more modest bound in terms of \(\nu(P)\).

### Frobenius-family inefficiency `[DISPROVED]`

Write the abelian kernel additively. For \(1\ne h\in H\), two elements \((v,h),(w,h)\) commute exactly when

\[
(1-h)(v-w)=0.
\]

Fixed-point-freeness makes \(1-h\) invertible, so the coset \(Vh\) is a \(\lvert V\rvert\)-clique. Every nonzero \(x\in V\) fails to commute with every member of \(Vh\), giving a \(\lvert V\rvert+1\)-clique. Conversely, if an element is \((u,h)\) with \(h\ne1\), invertibility of \(h-1\) lets one solve \(u=(h-1)v\); conjugating \((0,h)\) by \((v,1)\) produces \((u,h)\). Thus \(V\) together with the \(\lvert V\rvert\) conjugates of the abelian complement covers \(G\), proving the bounds in Candidate 10.

## Screening conclusion

`[PROVED]` Candidates 2, 6, and 10 fail by explicit mechanisms, not merely by lack of progress.

`[PROVED]` Candidate 1 is the only candidate in this run for which the decisive lemma, all field characteristics, and the resulting asymptotic statement can be closed self-containedly.

`[UNVERIFIED]` Candidates 3, 4, 5, 7, 8, and 9 remain mathematically viable but have a precise first gap listed above.

---

# 3. Phase II — selection by leverage

The surviving mechanisms were ranked as follows.

| Rank | Direction | Full-problem consequence | Plausibility of completion now | Independence | Independent verification |
|---:|---|---|---|---|---|
| 1 | Twisted-tensor scalar barrier | `[PROVED]` Rules out the entire nonbinary scalar-symplectic class as an asymptotic improvement and determines the scalar-class rate exactly. | `[PROVED]` Complete proof is available now. | `[PROVED]` No classification, computation, or inaccessible source is needed. | `[PROVED]` Every step reduces to finite-field Frobenius, a Moore-matrix argument, and elementary inequalities. |
| 2 | Higher-codomain alternating maps | `[CONJECTURE]` Could beat \(\sqrt2\) and change the global lower rate. | `[UNVERIFIED]` No family with both parameters proved has been found. | `[PROVED]` In principle self-contained. | `[UNVERIFIED]` Exact isotropic-cover lower bounds are difficult to certify. |
| 3 | Structured BFC coset covers | `[CONJECTURE]` Could give a universal fixed-base upper bound. | `[UNVERIFIED]` The missing theorem is substantially stronger than the valid general cover result. | `[UNVERIFIED]` A full proof may require deep finite-group structure. | `[UNVERIFIED]` Constants and hypotheses are delicate. |
| 4 | The historical \(h(8)\) residual branches | `[PROVED]` They were subsequently closed in the surrounding repository, independently of this scalar result. | `[PROVED]` Exact theorem \(h(8)=10\) is now available. | `[PROVED]` Finite, sharply scoped. | `[UNVERIFIED]` Whether those proofs expose a reusable asymptotic invariant remains open. |
| 5 | Central amalgamation/Fekete operation | `[CONJECTURE]` Could prove existence of a global rate. | `[UNVERIFIED]` Commutator cancellation blocks the natural definitions. | `[PROVED]` Conceptually independent. | `[UNVERIFIED]` Both invariant formulas would require new proofs. |

`[PROVED]` The twisted-tensor direction was selected because it is the unique candidate combining a broad global consequence, a complete proof now, no deep external dependency, and easy independent auditing.

`[UNVERIFIED]` The designated backup is the higher-codomain alternating-map program, because Theorem B makes it the most direct remaining route to a better lower exponential constant.

---

# 4. Complete proof of the selected result

## 4.1 Audited scalar group dictionary

### Proposition 4.1 `[PROVED]`

The multiplication

\[
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+x\cdot y')
\]

on \(\mathbb F_q^m\times\mathbb F_q^m\times\mathbb F_q\) is associative and defines a group of order \(q^{2m+1}\) and nilpotency class two. It has inverse

\[
(x,y,z)^{-1}=(-x,-y,-z+x\cdot y),
\]

and gives commutator form

\[
B((x,y),(x',y'))=x\cdot y'-x'\cdot y.
\]

Its center is the last coordinate, the form on the central quotient is nondegenerate alternating, and

\[
\nu(S(q,m))=\pi(q,m),\qquad a(S(q,m))=q^m+1.
\]

**Proof.** The cocycle \(c((x,y),(x',y'))=x\cdot y'\) is bilinear, so its cocycle identity is an immediate expansion and proves associativity in every characteristic. The inverse and commutator follow by multiplication. Every commutator lies in the last coordinate, and the displayed form is nonzero for \(m\ge1\), so the class is exactly two. Pairing against all \((0,y')\) and then all \((x',0)\) proves nondegeneracy and identifies the center. A noncommuting set uses at most one representative from each projective point and is exactly a partial ovoid after central compression. The image of an abelian subgroup is an additive isotropic set; its \(\mathbb F_q\)-linear span remains isotropic by bilinearity and therefore has at most \(q^m\) vectors. A symplectic spread partitions all nonzero vectors into \(q^m+1\) Lagrangian subspaces. This gives the lower and upper abelian-cover bounds. \(\square\)

**Characteristic-two audit.** The group law uses the valid triangular cocycle \(x\cdot y'\); it never treats the alternating commutator form itself as a cocycle.

## 4.2 The twisted-tensor construction

### Lemma 4.2 — the descended tensor space `[PROVED]`

Let \(E=\mathbb F_{q^t}\), \(F=\mathbb F_q\), \(\sigma(c)=c^q\), and let \(U=E^2\) with basis \(e_0,e_1\). Put

\[
T=U^{\otimes_E t}.
\]

Define the \(\sigma\)-semilinear map

\[
\tau(u_0\otimes u_1\otimes\cdots\otimes u_{t-1})
 =\sigma(u_{t-1})\otimes\sigma(u_0)\otimes\cdots\otimes\sigma(u_{t-2}).
\tag{4.1}
\]

Then \(\tau^t=1\), and its fixed space

\[
V=T^\tau
\]

has \(F\)-dimension \(2^t\). Moreover, the \(E\)-span of \(V\) is all of \(T\).

**Proof.** The standard tensor basis is indexed by bit strings \(b\in\{0,1\}^t\). If \(s\) is cyclic shift, then

\[
\tau(c e_b)=c^q e_{s(b)}.
\]

Partition the bit strings into cyclic-shift orbits. Let an orbit have length \(d\mid t\), with ordered basis \(f_0,\ldots,f_{d-1}\) satisfying \(\tau(c f_j)=c^q f_{j+1}\), indices modulo \(d\). Its fixed vectors are exactly

\[
x(c)=\sum_{j=0}^{d-1}c^{q^j}f_j,
\qquad c\in\mathbb F_{q^d}.
\tag{4.2}
\]

Thus this orbit contributes \(d\) dimensions over \(F\). Summing the orbit lengths gives

\[
\dim_F V=\sum_{\text{orbits}}d=2^t.
\]

Choose an \(F\)-basis \(c_1,\ldots,c_d\) of \(\mathbb F_{q^d}\). The coefficient matrix of \(x(c_1),\ldots,x(c_d)\) in the \(f_j\)-basis is the Moore matrix \((c_i^{q^j})\). It is nonsingular: otherwise a nonzero linearized polynomial of \(q\)-degree at most \(d-1\) would vanish on the entire \(d\)-dimensional \(F\)-space \(\mathbb F_{q^d}\), giving at least \(q^d\) roots despite ordinary degree at most \(q^{d-1}\). Hence the fixed vectors from each orbit span its full \(E\)-coordinate space. Summing over orbits proves that \(E V=T\). Finally, \(\tau^t=1\) because after \(t\) shifts every coefficient has been raised to \(q^t\), which is the identity on \(E\). \(\square\)

### Lemma 4.3 — a symplectic form on the fixed space `[PROVED]`

Assume \(t\) is odd. On \(U\) let

\[
D((a,b),(c,d))=ad-bc.
\]

On pure tensors define

\[
\mathcal B(u_0\otimes\cdots\otimes u_{t-1},
           v_0\otimes\cdots\otimes v_{t-1})
 =\prod_{i=0}^{t-1}D(u_i,v_i),
\tag{4.3}
\]

and extend \(E\)-bilinearly. Then the restriction \(B=\mathcal B|_{V\times V}\) is an \(F\)-valued nondegenerate alternating form on the \(2^t\)-dimensional \(F\)-space \(V\).

**Proof.** The tensor product of nondegenerate forms is nondegenerate, so \(\mathcal B\) is nondegenerate on \(T\). Cyclic shift and Frobenius give

\[
\mathcal B(\tau x,\tau y)=\mathcal B(x,y)^q.
\]

For fixed \(x,y\in V\), this implies \(\mathcal B(x,y)\in F\). If \(x\in V\) is orthogonal to every element of \(V\), it is orthogonal to the \(E\)-span \(EV=T\), so nondegeneracy on \(T\) forces \(x=0\).

Swapping the two arguments multiplies (4.3) by \((-1)^t=-1\). In odd characteristic this makes the restriction alternating. In characteristic two, the matrix of \(\mathcal B\) in the tensor basis is the tensor power of a zero-diagonal \(2\times2\) alternating matrix; it is symmetric with zero diagonal, hence its associated bilinear form also satisfies \(\mathcal B(x,x)=0\) for every \(x\). Therefore \(B\) is alternating in every characteristic. \(\square\)

### Theorem 4.4 — explicit partial ovoid `[PROVED]`

For every prime power \(q\) and odd \(t\ge1\), the symplectic space \((V,B)\) from Lemma 4.3 contains \(q^t+1\) pairwise nonorthogonal projective points. Consequently,

\[
\pi\!\left(q,2^{t-1}\right)\ge q^t+1.
\]

**Proof.** For \(P=[a:b]\in\operatorname{PG}(1,E)\), set

\[
w_P=\bigotimes_{i=0}^{t-1}
       \left(a^{q^i}e_0+b^{q^i}e_1\right).
\tag{4.4}
\]

The cyclic Frobenius map \(\tau\) fixes \(w_P\), so \(w_P\in V\). Replacing \((a,b)\) by \((\lambda a,\lambda b)\) multiplies (4.4) by

\[
\prod_{i=0}^{t-1}\lambda^{q^i}=N_{E/F}(\lambda)\in F^\times,
\]

so the projective point \([w_P]\in\operatorname{PG}(V)\) is well defined.

For distinct \(P=[a:b]\) and \(Q=[c:d]\), the determinant \(ad-bc\) is nonzero and

\[
B(w_P,w_Q)
 =\prod_{i=0}^{t-1}(ad-bc)^{q^i}
 =N_{E/F}(ad-bc)\ne0.
\tag{4.5}
\]

Thus all \(q^t+1\) points of \(\operatorname{PG}(1,E)\) have pairwise nonzero symplectic pairing. Since \(\dim_FV=2^t=2\cdot2^{t-1}\), they form a partial ovoid in \(W(2^t-1,q)=W(2(2^{t-1})-1,q)\). \(\square\)

### Boundary audit for Theorem 4.4 `[PROVED]`

- At \(t=1\), (4.4) is the identity parametrization of all \(q+1\) projective points of a symplectic plane.
- At \(t=3\), it gives \(q^3+1\) points in \(W(7,q)\).
- At \(q=2\), its seed size is \(2^t+1=2\cdot2^{t-1}+1\), matching the exact binary partial-ovoid number on those dimensions.
- The proof needs \(t\) odd in odd characteristic because an even tensor power of an alternating form is symmetric rather than alternating. No claim for even \(t\) in odd characteristic is used.
- In characteristic two, the zero-diagonal audit in Lemma 4.3 closes the usual skew-versus-alternating trap.

## 4.3 Orthogonal gluing

### Lemma 4.5 — superadditivity of \(\pi(q,m)-1\) `[PROVED]`

For all \(r,s\ge1\),

\[
\pi(q,r+s)\ge\pi(q,r)+\pi(q,s)-1.
\tag{4.6}
\]

**Proof.** Let \(A\) and \(C\) be pairwise nonorthogonal vector representatives in orthogonal symplectic summands \(V_1,V_2\). Fix \(c_0\in C\) and take

\[
\{(a,c_0):a\in A\}
\ \cup\
\{(0,c):c\in C\setminus\{c_0\}\}.
\tag{4.7}
\]

Pairs in the first part have the nonzero \(V_1\)-pairing of their \(A\)-coordinates, pairs in the second part have the nonzero \(V_2\)-pairing of their \(C\)-coordinates, and every cross-pair has pairing \(B_2(c_0,c)\ne0\). The size is \(|A|+|C|-1\). \(\square\)

### Corollary 4.6 `[PROVED]`

Writing \(b_q(m)=\pi(q,m)-1\), one has

\[
b_q(r+s)\ge b_q(r)+b_q(s).
\tag{4.8}
\]

In particular, since \(b_q(1)=q\),

\[
\pi(q,m)\ge mq+1.
\tag{4.9}
\]

## 4.4 Fixed-field collapse

### Theorem 4.7 `[PROVED]`

For every fixed prime power \(q>2\),

\[
\frac{\log(q^m+1)}{\pi(q,m)}\to0.
\]

**Proof.** Among odd \(t\), the dimensions

\[
M_t=2^{t-1}
\]

are \(1,4,16,64,\ldots\). Given \(m\), choose the largest such \(M=M_t\le m\). Then

\[
M>m/4.
\tag{4.10}
\]

Theorem 4.4 and repeated gluing give, with \(k=\lfloor m/M\rfloor\ge1\),

\[
\pi(q,m)-1\ge kq^t\ge q^t.
\tag{4.11}
\]

Let \(\alpha=\log_2q\). Since \(t=1+\log_2M\),

\[
q^t=qM^\alpha>q(m/4)^\alpha=\frac{m^\alpha}{q}.
\tag{4.12}
\]

Therefore

\[
\pi(q,m)>1+\frac{m^{\log_2q}}{q}.
\tag{4.13}
\]

Also

\[
\log(q^m+1)\le m\log q+\log2.
\tag{4.14}
\]

Because \(q>2\) implies \(\log_2q>1\), the quotient of (4.14) by (4.13) tends to zero. \(\square\)

### Quantitative form `[PROVED]`

For fixed \(q>2\),

\[
\frac{\log(q^m+1)}{\pi(q,m)}
<
\frac{m\log q+\log2}{1+m^{\log_2q}/q}
=O_q\!\left(m^{1-\log_2q}\right).
\tag{4.15}
\]

## 4.5 Uniform collapse over every nonbinary field

### Theorem 4.8 `[PROVED]`

For any sequence of prime powers \(q_j\ge3\) and integers \(m_j\ge1\), if

\[
\pi(q_j,m_j)\to\infty,
\]

then

\[
\frac{\log(q_j^{m_j}+1)}{\pi(q_j,m_j)}\to0.
\]

**Proof.** The plane-gluing bound (4.9) gives

\[
\frac{\log(q^m+1)}{\pi(q,m)}
\le
\frac{m\log q+\log2}{mq+1}
\le
\frac{\log q+\log2}{q}.
\tag{4.16}
\]

Hence any subsequence with \(q_j\to\infty\) has ratio tending to zero. On a subsequence with bounded \(q_j\), only finitely many prime powers occur. If \(\pi(q_j,m_j)\to\infty\), then \(m_j\to\infty\) on each fixed-field subsequence, and Theorem 4.7 applies. Every subsequence has a further subsequence on which the ratio tends to zero, so the full sequence does as well. \(\square\)

### Corollary 4.9 — nonbinary scalar envelope `[PROVED]`

\[
\log h_{\mathrm{sc},\ne2}(n)=o(n),
\qquad
h_{\mathrm{sc},\ne2}(n)^{1/n}\to1.
\]

**Proof.** The maximum defining the envelope is finite because \(\pi(q,m)\ge mq+1\) bounds both \(q\) and \(m\) when \(\pi(q,m)\le n\). Suppose there were \(\varepsilon>0\) and arbitrarily large \(n\) with

\[
\log h_{\mathrm{sc},\ne2}(n)\ge\varepsilon n.
\]

Choose a maximizing pair \((q,m)\). Then

\[
\frac{\log(q^m+1)}{\pi(q,m)}
\ge
\frac{\log(q^m+1)}{n}
\ge\varepsilon.
\]

The numerator tends to infinity, so \(mq\to\infty\), and (4.9) gives \(\pi(q,m)\to\infty\). This contradicts Theorem 4.8. \(\square\)

## 4.6 The binary exact value

### Lemma 4.10 `[PROVED]`

For every \(m\ge1\),

\[
\pi(2,m)=2m+1.
\tag{4.17}
\]

**Proof.** If \(v_1,\ldots,v_k\) are pairwise nonorthogonal in a binary symplectic space, their Gram matrix has zero diagonal and one off diagonal. Over \(\mathbb F_2\), this matrix has rank \(k\) when \(k\) is even and rank \(k-1\) when \(k\) is odd. Its rank is at most the ambient dimension \(2m\), so \(k\le2m+1\).

For equality, let

\[
V=\{x\in\mathbb F_2^{2m+1}:\textstyle\sum_i x_i=0\}
\]

with the dot product. The restriction is alternating and nondegenerate: the orthogonal complement of the even-weight hyperplane in the full dot-product space is generated by the all-ones vector, which has odd weight and is not in \(V\). For \(i=1,\ldots,2m+1\), put \(v_i=\mathbf1+e_i\). Each \(v_i\) has even weight, and for \(i\ne j\), \(v_i\cdot v_j=1\). Thus \(2m+1\) is attained. \(\square\)

### Corollary 4.11 `[PROVED]`

For the binary scalar groups,

\[
\nu(S(2,m))=2m+1,
\qquad
a(S(2,m))=2^m+1.
\tag{4.18}
\]

## 4.7 Exact scalar exponential rate

### Theorem 4.12 `[PROVED]`

\[
\lim_{n\to\infty}h_{\mathrm{sc}}(n)^{1/n}=\sqrt2.
\]

**Proof.** The binary model with

\[
m=\left\lfloor\frac{n-1}{2}\right\rfloor
\]

has \(\nu=2m+1\le n\) and

\[
a=2^m+1,
\]

so

\[
\liminf_{n\to\infty}h_{\mathrm{sc}}(n)^{1/n}\ge\sqrt2.
\]

Conversely, the binary portion of the envelope is at most \(2^{(n-1)/2}+1=2^{n/2+o(n)}\), while Corollary 4.9 says the union of all nonbinary scalar models is \(e^{o(n)}\). The maximum of these two quantities is \(2^{n/2+o(n)}\). \(\square\)

## 4.8 Pointwise barrier

### Theorem 4.13 `[PROVED]`

Except for \((q,m)=(2,1)\),

\[
q^m+1\le2^{\pi(q,m)/2}.
\]

**Proof.**

**Case 1: \(q=2\).** By Lemma 4.10, \(\pi(2,m)=2m+1\). At \(m=1\), \(3>2^{3/2}\), giving the stated exception. For \(m\ge2\),

\[
2^m+1=2^m(1+2^{-m})<2^m\sqrt2=2^{(2m+1)/2}.
\]

**Case 2: \(q=3\).** The \(t=3\) twisted-tensor seed gives

\[
b_3(4)=\pi(3,4)-1\ge27,
\]

while a plane gives \(b_3(1)=3\). If \(m=4k+r\), \(0\le r\le3\), gluing gives

\[
\pi(3,m)\ge27k+3r+1.
\tag{4.19}
\]

For \(k=0\), the positive-dimensional cases are

\[
4=2^{4/2},\qquad 10<2^{7/2},\qquad 28<2^{10/2}
\]

for \(r=1,2,3\). For \(r=0\), the first case is \(m=4\), where \(82<2^{14}\). Increasing \(k\) by one multiplies \(3^m+1\) by less than \(81\), while the right side supplied by (4.19) is multiplied by

\[
2^{27/2}>81.
\]

Induction proves the inequality for every \(m\). Equality occurs only at \(m=1\).

**Case 3: \(q\ge4\).** The plane-gluing bound gives \(\pi(q,m)\ge mq+1\). Since \(q^m\ge4\),

\[
q^m+1\le\frac54q^m.
\]

For \(q\ge4\), \(q\le2^{q/2}\): equality holds at \(q=4\), and \(2^{x/2}/x\) is increasing for \(x\ge4\) because its logarithmic derivative is \((\log2)/2-1/x>0\). Therefore

\[
q^m+1\le\frac54\,2^{mq/2}
<\sqrt2\,2^{mq/2}
=2^{(mq+1)/2}
\le2^{\pi(q,m)/2}.
\]

This completes all prime powers and all \(m\ge1\). \(\square\)

### Corollary 4.14 `[PROVED]`

For every \(n\ge4\),

\[
h_{\mathrm{sc}}(n)\le2^{n/2}.
\]

**Proof.** Every nonexceptional model satisfies Theorem 4.13 and \(\pi(q,m)\le n\). The sole exception has cover number three, which is at most \(2^{n/2}\) for \(n\ge4\). \(\square\)

---

# 5. Independent finite certificates

### Twisted-tensor certificate `[COMPUTED]`

The file `certificates/W73_Q3_TWISTED_TENSOR_28.json` directly checks the \(q=3,t=3\) instance of Theorem 4.4. It contains a nonsingular alternating \(8\times8\) matrix over \(\mathbb F_3\) and 28 distinct projective vectors whose 378 pairwise symplectic products are all nonzero.

The generator constructs the Frobenius-fixed basis of \((\mathbb F_{27}^2)^{\otimes3}\), changes all \(\operatorname{PG}(1,27)\) tensor images into that basis, and exports only base-field coordinates. The independent verifier does not implement \(\mathbb F_{27}\); it checks solely exact linear algebra over \(\mathbb F_3\).

The saved verifier transcript reports:

```text
PASS: twisted-tensor certificate is internally valid
field=F_3
ambient_dimension=8
form_rank=8
projective_points=28
unordered_pairs_checked=378
nonzero_pairing_value_counts={1: 225, 2: 153}
```

### Auxiliary norm-one certificate `[COMPUTED]`

The file `certificates/W53_Q3_NORM_ONE_13.json` contains a nonsingular alternating \(6\times6\) matrix over \(\mathbb F_3\) and thirteen distinct projective vectors whose 78 pairwise symplectic products are all nonzero.

Its generator realizes \(\mathbb F_{27}=\mathbb F_3[a]/(a^3-a-1)\), takes the thirteen norm-one elements \(x\), and exports \((x,x^{-1})\). Its independent verifier again ignores extension-field arithmetic and checks only the exported object over \(\mathbb F_3\).

The saved verifier transcript reports:

```text
PASS: certificate is internally valid
field=F_3
ambient_dimension=6
form_rank=6
projective_points=13
unordered_pairs_checked=78
nonzero_pairing_value_counts={1: 32, 2: 46}
```

### Pointwise arithmetic audit `[COMPUTED]`

The script `scripts/verify_scalar_pointwise_audit.py` checks exact squared-integer versions of the inequalities in Theorem 4.13 for \(q=2,3\) through \(m=500\), and for every integer \(4\le q\le256\) and \(1\le m\le100\). It confirms the \((2,1)\) exception and the \((3,1)\) equality case. This finite audit is not substituted for the symbolic proof.

### Reproduction `[COMPUTED]`

From the bundle root, run

```bash
python3 scripts/generate_w73_q3_twisted_tensor_certificate.py certificates/W73_Q3_TWISTED_TENSOR_28.json
python3 scripts/verify_w73_q3_twisted_tensor_certificate.py certificates/W73_Q3_TWISTED_TENSOR_28.json
python3 scripts/generate_w53_q3_certificate.py certificates/W53_Q3_NORM_ONE_13.json
python3 scripts/verify_w53_q3_certificate.py certificates/W53_Q3_NORM_ONE_13.json
python3 scripts/verify_scalar_pointwise_audit.py
```

`[PROVED]` None of these computations is load-bearing for Theorems A–D. The first directly audits the smallest nontrivial twisted-tensor seed used in the \(q=3\) pointwise proof; the second checks an independent norm-one geometry; the third checks finite arithmetic boundaries.

---

# 6. Adversarial audit

## 6.1 Attempts to break the tensor construction

1. **Projective scaling could leave the descended \(\mathbb F_q\)-space.**
   `[PROVED]` Scaling \((a,b)\) by \(\lambda\in\mathbb F_{q^t}^\times\) scales its tensor image by \(N(\lambda)\in\mathbb F_q^\times\), so the projective image is well defined over the base field.

2. **The fixed space might have the wrong dimension.**
   `[PROVED]` The cyclic-bit-orbit calculation gives exactly the sum of all orbit lengths, \(2^t\), and the Moore-polynomial argument proves that these fixed vectors span after scalar extension.

3. **The restricted form might acquire a radical.**
   `[PROVED]` The fixed space spans the full tensor space over \(\mathbb F_{q^t}\). A fixed vector orthogonal to the fixed space is therefore orthogonal to the full tensor space, contradicting nondegeneracy.

4. **Skew-symmetry could be mistaken for alternation in characteristic two.**
   `[PROVED]` The tensor-basis matrix has zero diagonal; in characteristic two it is symmetric with zero diagonal, which directly implies \(B(x,x)=0\).

5. **The determinant norm could vanish for distinct projective points.**
   `[PROVED]` Distinct points of \(\operatorname{PG}(1,q^t)\) have nonzero determinant, and the norm of a nonzero finite-field element is nonzero.

6. **The construction might require maximality rather than merely pairwise nonorthogonality.**
   `[PROVED]` The parameter \(\pi(q,m)\) is a maximum over partial ovoids; any pairwise nonorthogonal set supplies a valid lower bound. No maximality or completeness claim is used.

7. **Even tensor length might have been silently included.**
   `[PROVED]` The theorem is stated only for odd \(t\). This is enough because the available block dimensions \(1,4,16,\ldots\) differ by a bounded factor four.

## 6.2 Attempts to break the asymptotic deductions

1. **The leftover dimension after choosing a tensor block might invalidate gluing.**
   `[PROVED]` A partial ovoid in a nondegenerate orthogonal summand remains pairwise nonorthogonal in the full space. Repeated gluing of \(\lfloor m/M\rfloor\) blocks is therefore valid even without using the leftover summand.

2. **The fixed-\(q\) estimate might fail at \(q=3\).**
   `[PROVED]` Its exponent is \(\log_2 3>1\), so (4.15) still tends to zero. The argument does not rely on an integer exponent.

3. **Allowing \(q\) to vary might defeat fixed-field convergence.**
   `[PROVED]` For unbounded \(q\), the elementary bound \((\log q+\log2)/q\to0\) applies; bounded \(q\) leaves finitely many fields and reduces to Theorem 4.7.

4. **The supremum defining the scalar envelope might not be attained.**
   `[PROVED]` The inequality \(\pi(q,m)\ge mq+1\) leaves only finitely many pairs \((q,m)\) at each cutoff \(n\), so the supremum is a maximum.

5. **The exceptional \((2,1)\) model could affect the asymptotic upper rate.**
   `[PROVED]` It is a single bounded model with \(a=3\), so it has no effect on the \(n\)-th-root limit and is absorbed by \(2^{n/2}\) for \(n\ge4\).

6. **Finite odd-characteristic improvements might contradict nonbinary subexponentiality.**
   `[PROVED]` The audited example \(S(3,2)=(\nu,a)=(7,10)\) is compatible with Theorem B: the theorem concerns sequences with \(\pi\to\infty\), not isolated finite cutoffs.

7. **The first cutoffs or floor choices might have been lost in asymptotic notation.**
   `[PROVED]` No nondegenerate scalar model has \(\pi\le2\), so \(h_{\mathrm{sc}}(1)=h_{\mathrm{sc}}(2)=1\). Lemma 4.10 gives \(h_{\mathrm{sc}}(3)=3\), the unique pointwise exception. In Theorem 4.12 the choice \(m=\lfloor(n-1)/2\rfloor\) satisfies \(2m+1\le n\) for both parities, and its floor error is \(O(1)\), hence disappears after division by \(n\).

## 6.3 Group-theoretic scope audit

- `[PROVED]` The proof concerns finite scalar-symplectic groups \(S(q,m)\), equivalently their nondegenerate scalar-valued alternating commutator geometries.
- `[PROVED]` Abelian groups are harmless: they have \((\nu,a)=(1,1)\) and do not occur among \(m\ge1\) nondegenerate scalar models.
- `[PROVED]` Large centers do not change \(\nu\) or \(a\) after central-coset compression in this family.
- `[PROVED]` No quotient by a noncentral subgroup, no unproved clique lifting, and no direct-product multiplicativity is used.
- `[PROVED]` The proof applies to every characteristic, including two, but it does not assert a reduction of arbitrary groups to class two.
- `[UNVERIFIED]` No claim is made for arbitrary, nilpotent of higher class, solvable nonnilpotent, or nonsolvable groups beyond the negative inference that a better lower construction must leave this scalar class.

## 6.4 External-dependency audit

- `[PROVED]` The load-bearing proof is self-contained modulo standard finite-field existence and elementary linear algebra, both reconstructed at the needed points.
- `[PROVED]` CFSG is not used.
- `[PROVED]` Classification tables are not used.
- `[PROVED]` Computer search is not used.
- `[PROVED]` The withdrawn fixed-base hyperplane-cover manuscript is not used.
- `[UNVERIFIED]` The twisted-tensor point set has antecedents in finite-geometry literature; this report makes no claim that the geometric construction itself is novel. The new deliverable is the self-contained proof and its explicit asymptotic exclusion consequence for Erdős 117.


### 6.5 Primary-literature cross-checks

`[CITED-VERIFIED]` Francesco Pavese, *\((r,s)\)-sets from Desarguesian ovoids*, arXiv:2605.22289v1 (2026), Section 3, explicitly writes the \(q^3+1\)-point set

\[
(1,t)\otimes(1,t^q)\otimes(1,t^{q^2})
\quad(t\in\mathbb F_{q^3}),
\]

plus the point at infinity, and places it under the tensor-cube alternating form. This matches the \(t=3\) specialization of Theorem 4.4 after a coordinate change.

`[CITED-VERIFIED]` Marco Ceria, Jan De Beule, Francesco Pavese, and Valentino Smaldore, *On large partial ovoids of symplectic and Hermitian polar spaces*, arXiv:2203.04553, Theorem 3.7, proves a partial ovoid of \(W(5,q)\) of size \(q^2+q+1\). This matches the cardinality and geometry independently checked by the auxiliary norm-one certificate.

`[PROVED]` Neither cited result is a load-bearing dependency: the general odd-\(t\) tensor theorem and all asymptotic deductions are proved in full in this report.

---

# 7. Dependency graph

```text
Finite-field Frobenius + cyclic tensor descent
                    |
                    v
  2^t-dimensional base-field symplectic space
                    |
                    v
 Norm pairing on PG(1,q^t): q^t+1 nonorthogonal points
                    |
                    v
  pi(q,2^(t-1)) >= q^t+1  [Theorem A]
                    |
             orthogonal gluing
                    |
        +-----------+------------------+
        |                              |
        v                              v
fixed q>2: log(a)/nu -> 0       q=3 block bound for
        |                       pointwise inequality
        v                              |
uniform q>=3 collapse                  |
        |                              |
        v                              v
nonbinary scalar envelope      q^m+1 <= 2^(pi/2)
     has base 1                 outside (2,1)
        |                              |
        +---------------+--------------+
                        |
          binary Gram-rank formula
             pi(2,m)=2m+1
                        |
                        v
 scalar envelope has exact base sqrt(2)
                        |
                        v
Any better global lower family must leave scalar symplectic geometry
```

`[PROVED]` The graph has no arrow from the scalar result to a universal upper bound for arbitrary groups. That missing arrow is precisely why the full problem remains open.

---

# 8. Exact remaining gap

`[UNVERIFIED]` **One-sentence gap:** determine whether a higher-codomain/non-field-linear commutator geometry or a non-class-two group can achieve \(\limsup \log a(G)/\nu(G)>\log2/2\), or else prove a universal upper bound excluding it.

---

# 9. Final solve-status declaration

- **Erdős Problem 117:** `[UNVERIFIED]` not solved.
- **The value of \(h(8)\):** `[PROVED]` \(h(8)=10\) in the surrounding repository, independently of this bundle.
- **Scalar-symplectic asymptotic optimization:** `[PROVED]` solved exactly: rate \(\sqrt2\), with all nonbinary scalar fields jointly subexponential.
- **Pointwise scalar upper barrier:** `[PROVED]` established, with the unique small exception \(S(2,1)\).
- **Scope of the achieved advance:** `[PROVED]` a sharply scoped theorem ruling out an entire broad class of possible improvements to the current lower exponential constant.
