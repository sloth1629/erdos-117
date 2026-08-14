# Structural Reductions

This note gives a self-contained arbitrary-group reduction. It deliberately
does not use the false assertion that \(G/Z(G)\) preserves commutation, nor
does it require Schur's theorem or the existence of stem representatives of
isoclinism families.

## From finite clique number to finite-index center

Write \(R(s,t)\) for the least integer such that every graph on \(R(s,t)\)
vertices contains a clique of size \(s\) or an independent set of size \(t\).

### [PROVED] Finite Ramsey lemma used here

The numbers \(R(s,t)\) are finite and

\[
R(s,t)\leq {s+t-2\choose s-1}.
\]

**Proof.** The usual vertex split gives
\(R(s,t)\leq R(s-1,t)+R(s,t-1)\), with \(R(1,t)=R(s,1)=1\). Induction and
Pascal's identity give the displayed binomial bound. \(\square\)

### [PROVED] A finite clique bound gives a uniform BFC bound

If \(\nu(G)=n<\infty\), then for every \(g\in G\),

\[
[G:C_G(g)]\leq R(n+1,n+1)-1.
\]

Thus \(G\) is a BFC group, with a bound depending only on \(n\), even when
\(G\) is infinite.

**Proof.** If the conjugacy class of \(g\) had at least
\(R(n+1,n+1)\) elements, choose a set \(T\) of that size whose elements give
distinct conjugates \(t^{-1}gt\). Ramsey's theorem applied to the
noncommuting graph induced on \(T\) cannot return a clique of size \(n+1\).
It therefore returns \(n+1\) pairwise commuting elements \(U\subseteq T\).

For distinct commuting \(u,v\in U\), equality
\((gu)(gv)=(gv)(gu)\) is equivalent, after cancellation and use of
\(uv=vu\), to \(u^{-1}gu=v^{-1}gv\). The latter is false by the choice of
\(T\). Hence \(gU\) is a pairwise noncommuting set of size \(n+1\), a
contradiction. Finally, conjugacy-class size is \([G:C_G(g)]\). \(\square\)

### [PROVED] A maximum noncommuting set detects the center

If \(X=\{x_1,\ldots,x_n\}\) is a pairwise noncommuting set of maximum
cardinality, then

\[
C_G(X)=\bigcap_{i=1}^n C_G(x_i)=Z(G).
\]

**Proof.** The inclusion \(Z(G)\subseteq C_G(X)\) is immediate. Suppose
\(c\in C_G(X)\setminus Z(G)\), and choose \(y\in G\) not commuting with \(c\).
For each \(i\), set

\[
x_i'=\begin{cases}
x_i,&x_i y\ne yx_i,\\
x_i c,&x_i y=yx_i.
\end{cases}
\]

In the second case \(x_i\) commutes with both \(c\) and \(y\), while \(c\)
does not commute with \(y\), so \(x_i c\) does not commute with \(y\).
Moreover \(c\) commutes with every \(x_i\), and therefore multiplying any
\(x_i\) by \(c\) does not change whether two members of \(X\) commute:
for \(i\ne j\), the two products in opposite orders have respectively the
factors \(x_i x_j\) and \(x_j x_i\), followed by the same power of \(c\).
Thus \(\{x_1',\ldots,x_n',y\}\) is pairwise noncommuting, contradicting the
maximality of \(n\). \(\square\)

### [PROVED] Preliminary centralizer drop

If \(\nu(G)=n<\infty\) and \(x\notin Z(G)\), then

\[
\nu(C_G(x))\leq n-1.
\]

**Proof.** Suppose instead that \(a_1,\ldots,a_n\in C_G(x)\) are pairwise
noncommuting, and choose \(y\in G\) with \(xy\ne yx\). Define

\[
b_i=\begin{cases}
a_i,&a_i y\ne ya_i,\\
xa_i,&a_i y=ya_i.
\end{cases}
\]

Every \(b_i\) fails to commute with \(y\). In the second case this follows
because \(a_i\) commutes with both \(x\) and \(y\), while \(x\) does not
commute with \(y\). Also, for \(\epsilon_i,\epsilon_j\in\{0,1\}\), centrality
of \(x\) relative to all the \(a_i\) gives

\[
(x^{\epsilon_i}a_i)(x^{\epsilon_j}a_j)
=x^{\epsilon_i+\epsilon_j}a_ia_j.
\]

Thus multiplying any selected \(a_i\)'s by \(x\) does not change their
pairwise commutation relations. Hence
\(\{b_1,\ldots,b_n,y\}\) is pairwise noncommuting of size \(n+1\), a
contradiction. \(\square\)

This is stronger in a different direction than the common-centralizer
inequality often used in the literature: if \(x_1,\ldots,x_s\) form a clique,
then

\[
\nu\left(\bigcap_{i=1}^s C_G(x_i)\right)\leq n-s+1.
\]

Indeed, if \(b_1,\ldots,b_\ell\) form a clique in the intersection, then
\[
\{b_1,\ldots,b_{\ell-1},b_\ell x_1,\ldots,b_\ell x_s\}
\]
is a clique of size \(\ell+s-1\). The displayed centralizer lemma uses the
extra hypothesis that the single element \(x\) is noncentral to gain one
when \(s=1\); the common-centralizer inequality alone gives only \(n\) in
that case.

The sharp version needed for the strongest recurrence is proved separately
as Lemma CB.2 in candidate_bound.md:
\[
\nu(C_G(x))\leq n-2\qquad(x\notin Z(G)).
\]

### [PROVED] Central-by-finite conclusion for arbitrary groups

Every group with finite \(\nu(G)\) has finite-index center. Indeed, the
uniform BFC lemma makes every \(C_G(x_i)\) finite-index, while the
maximum-clique lemma says
\(Z(G)=\bigcap_{i=1}^nC_G(x_i)\). A finite intersection of finite-index
subgroups is finite-index. This proof is valid for finite and infinite groups
and is quantitative; the explicit index bound is recorded in known_bounds.md.

### [CITED-VERIFIED] Historical arbitrary-group theorem

B. H. Neumann, “A problem of Paul Erdős on groups,” J. Austral. Math. Soc.
Ser. A 21 (1976), 467–472, DOI 10.1017/S1446788700019303, proves on
pp. 468–470 (Lemma 1, Lemma 4, Corollary 5, Theorem 6) that a group has no
infinite pairwise noncommuting subset if and only if its center has finite
index. The primary paper was read in full. Its proof first uses infinite
Ramsey to show that such a group is an FC group and then constructs an
infinite noncommuting sequence inside any FC group that is not
central-by-finite. The self-contained finite-\(\nu\) proof above is shorter
because a maximum clique is available.

## Exact replacement by a finite group

### [PROVED] Residual finiteness lemma for the central subgroup

Let \(C\) be a finitely generated abelian group and
\(D\subseteq C\setminus\{1\}\) finite. There is a finite-index subgroup
\(N\leq C\) with \(N\cap D=\varnothing\).

**Proof.** Write \(C\cong\mathbb Z^r\oplus F\), with \(F\) finite. A nonzero
free coordinate is detected modulo a suitable integer; a nontrivial element
of \(F\) is detected by the projection to \(F\). More explicitly, choose an
integer \(M\) divisible by the exponent of \(F\) and larger than the absolute
value of every nonzero free coordinate occurring among the finitely many
elements of \(D\) (take any \(M\geq2\) with this divisibility property if
\(D\) is empty). Then, under the displayed additive decomposition,

\[
MC=M\mathbb Z^r\oplus0
\]

has finite index in \(C\). An element of \(D\) with nonzero free part is not
in \(MC\) by the choice of \(M\), and an element with zero free part is a
nonidentity element of \(F\), hence is also not in \(MC\). Thus \(N=MC\)
works. \(\square\)

### [PROVED] Finite commutation-model theorem

If \([G:Z(G)]<\infty\), there is a finite group \(K\) such that

\[
\Delta_K\cong\Delta_G,\qquad
\nu(K)=\nu(G),\qquad a(K)=a(G).
\]

**Proof.** Put \(Z=Z(G)\), choose a finite transversal
\(T=\{t_1=1,t_2,\ldots,t_q\}\) for \(Z\), and let \(H=\langle T\rangle\).
Then \(G=HZ\). With \(C=H\cap Z\), the homomorphism

\[
H\longrightarrow G/Z,\qquad h\longmapsto hZ
\]

is surjective and has kernel \(C\), so \(H/C\cong G/Z\). This explicitly
proves \([H:C]=q<\infty\). Since \(H\) is generated by the finite set \(T\),
the finite-index subgroup \(C\) is finitely generated. For completeness,
take the finite generating alphabet \(T\cup T^{-1}\). For each transversal
element \(t_i\) and each letter \(x\), let \(\overline{t_ix}\in T\) represent
the coset \(Ct_ix\). The finitely many elements

\[
t_ix\overline{t_ix}^{-1}\in C
\]

generate \(C\): rewriting the successive prefixes of any word in
\(T\cup T^{-1}\) that represents an element of \(C\) gives a telescoping
product of these elements (and their inverses); the representative of the
initial and final coset is \(1\). Finally, \(C=H\cap Z(G)\) is contained in
\(Z(H)\), so it is abelian as well as finitely generated.

Let

\[
D=\{[t_i,t_j]:1\leq i,j\leq q,\ [t_i,t_j]\ne1\}\cap C.
\]

This is a finite set of nonidentity elements of \(C\). By the preceding lemma
choose a finite-index \(N\leq C\) avoiding \(D\). Because \(C\leq Z(H)\), the
subgroup \(N\) is normal in \(H\). Set \(K=H/N\). It is finite because
\([H:N]=[H:C][C:N]<\infty\). No finiteness statement for \(H'\), and hence
no use of Schur's theorem, is needed.

Every \(h\in H\) has the form \(t_i c\), with \(c\in C\). For
\(h=t_i c\) and \(k=t_j d\), with \(c,d\in C\), centrality of \(C\) gives

\[
[h,k]=[t_i,t_j].
\]

If \([t_i,t_j]\ne1\), it is not in \(N\): this is automatic when it is not in
\(C\), since \(N\leq C\), and follows from \(N\cap D=\varnothing\) when it
is in \(C\). Hence

\[
hN\text{ commutes with }kN
\quad\Longleftrightarrow\quad
t_i\text{ commutes with }t_j
\quad\Longleftrightarrow\quad
h\text{ commutes with }k.
\]

This verifies explicitly that quotienting creates no new commuting pairs.

An element \(t_i cN\) is central in \(K\) exactly when \(t_i\) commutes with
all of \(H\). Since \(G=HZ\), this is exactly when \(t_i\in Z\), hence when
\(i=1\). Therefore \(Z(K)=C/N\). The canonical identifications
\(K/Z(K)\cong H/C\cong G/Z(G)\) now identify \(\Delta_K\) with
\(\Delta_G\), edge for edge. The central-coset theorem in foundations.md
then proves both invariant equalities, including \(a(K)=a(G)\). \(\square\)

### [PROVED] Exact finite reduction for \(h(n)\), and attainment

For every \(n\geq1\),

\[
h(n)=\sup\{a(K):K\text{ finite and }\nu(K)\leq n\}.
\]

Indeed, the reverse inequality is tautological, while every arbitrary \(G\)
on the left has finite-index center and hence an exactly matching finite
commutation model \(K\). The elementary bound in known_bounds.md shows that
this supremum is a finite integer. A bounded nonempty set of integers attains
its supremum; applying the finite-model theorem if necessary shows that
\(h(n)\) is attained by a finite group.

### [PROVED] A maximum clique gives an exact core-free subgroup cover

Let \(G\) be nonabelian with finite \(m=\nu(G)\), and choose a maximum
noncommuting set \(X=\{x_1,\ldots,x_m\}\). Then

\[
G=\bigcup_{i=1}^m C_G(x_i)
\quad\text{and}\quad
\bigcap_{i=1}^m C_G(x_i)=Z(G),
\]

and the cover is irredundant. Maximality of \(X\) proves the union, while
\(x_i\) belongs to no \(C_G(x_j)\) for \(j\ne i\), proving
irredundancy. If a noncentral \(y\) belonged to the intersection, all
\(m\) members of \(X\) would lie in \(C_G(y)\). Lemma CB.2 of
`notes/candidate_bound.md` gives

\[
\nu(C_G(y))\leq\nu(G)-2=m-2,
\]

a contradiction. This proves the intersection statement.

The repository's finite-center-quotient bound makes
\(Q=G/Z(G)\) finite. The images of the centralizers in \(Q\) therefore
form an irredundant \(m\)-subgroup cover with trivial intersection. In
particular, since \(h(7)=10\) is already proved, the only new branch for
\(h(8)\) has \(m=8\) and a finite center quotient carrying such a
core-free irredundant eight-cover.

## Central fibers in an exact center quotient

### [PROVED] Prime-order central fiber lemma

Let \(Q=G/Z(G)\) be nonabelian, and suppose that
\(c\in Z(Q)\) has prime order \(p\). Then

\[
\nu(G)\geq p+2.
\]

**Proof.** Let \(\pi:G\to Q\) be the quotient map. Choose a lift
\(\widetilde c\) of \(c\). For \(q\in Q\), choose any lift
\(\widetilde q\) and define

\[
\phi_c(q)=[\widetilde c,\widetilde q].
\]

Because \(c\in Z(Q)\), the displayed commutator lies in \(Z(G)\).
Multiplying either lift by an element of \(Z(G)\) does not change it, so
\(\phi_c\) is well-defined. The centrality of all its values makes the
usual commutator identities multiplicative without conjugation terms;
hence \(\phi_c:Q\to Z(G)\) is a homomorphism. It is nontrivial. Otherwise
\(\widetilde c\) would commute with a lift of every element of \(Q\), as
well as with the kernel \(Z(G)\), and would itself lie in \(Z(G)\). This
would give \(c=1\), contrary to the choice of \(c\).

Put \(K=\ker\phi_c\). There is a noncentral element \(q\in Q\setminus K\).
Indeed, if every element outside \(K\) were central, choose
\(z\in Q\setminus K\). For every \(k\in K\), the element \(zk\) also lies
outside \(K\), so both \(z\) and \(zk\) would be central. It would follow
that \(k=z^{-1}(zk)\) is central. Thus \(K\leq Z(Q)\), while the assumed
containment \(Q\setminus K\subseteq Z(Q)\) would make all of \(Q\)
abelian, a contradiction.

Choose \(r\in Q\) with \(qr\ne rq\), and choose lifts
\(\widetilde q,\widetilde r\). For \(0\leq i<p\), put

\[
y_i=\widetilde c^{\,i}\widetilde q.
\]

The \(p\) images \(c^iq\) are distinct. Since \(\phi_c(q)\ne1\), and its
order divides \(p\), it has order exactly \(p\). Central commutator
calculus gives, for \(i\ne j\),

\[
[y_i,y_j]=\phi_c(q)^{\,i-j}\ne1.
\]

Thus the \(y_i\) are pairwise noncommuting. In \(Q\), the three elements
\(q,r,qr\) are pairwise noncommuting. Consequently arbitrary lifts of
\(r\) and \(qr\) fail to commute with one another and with every \(y_i\):
for the cross pairs this is already detected by their images in \(Q\).
These \(p+2\) elements form a noncommuting set in \(G\). \(\square\)

### [PROVED] Prime-power central fiber strengthening

Let \(Q=G/Z(G)\) be nonabelian, and let \(c\in Z(Q)\) have order
\(p^e\), where \(p\) is prime and \(e\geq1\). Then

\[
\nu(G)\geq p^e+2.
\]

**Proof.** Put \(d=c^{p^{e-1}}\), which has order \(p\). Apply the
kernel argument from the prime-order lemma to

\[
\phi_d(q)=[\widetilde d,\widetilde q].
\]

It supplies a noncentral \(q\in Q\) with \(\phi_d(q)\ne1\). Choose
\(\widetilde d=\widetilde c^{\,p^{e-1}}\) and put
\(t=[\widetilde c,\widetilde q]\). Since \(c\) is central in \(Q\), the
element \(t\) is central in \(G\), and

\[
t^{p^{e-1}}=\phi_d(q)\ne1,
\qquad
t^{p^e}=[\widetilde c^{\,p^e},\widetilde q]=1.
\]

Thus \(t\) has order exactly \(p^e\). The \(p^e\) distinct quotient
elements \(c^iq\), for \(0\leq i<p^e\), have lifts satisfying

\[
[\widetilde c^{\,i}\widetilde q,
  \widetilde c^{\,j}\widetilde q]=t^{i-j}\ne1
\qquad(i\ne j).
\]

Finally choose \(r\in Q\) not commuting with \(q\). As before, arbitrary
lifts of \(r\) and \(qr\) are mutually noncommuting and are noncommuting
with every member of the fiber clique, already as detected in \(Q\).
This gives \(p^e+2\) elements. \(\square\)

### [PROVED] Cutoff-eight central-prime restriction

If \(Q=G/Z(G)\) is nonabelian and \(\nu(G)\leq8\), every prime-order
element of \(Z(Q)\) has order in \(\{2,3,5\}\). In particular,
\(Z(Q)\) has no element of order \(7\).

This is immediate from the prime-order central fiber lemma:
\(p+2\leq8\), and the only primes at most six are \(2,3,5\).

### [PROVED] Cutoff-eight central-exponent restriction

If \(Q=G/Z(G)\) is nonabelian and \(\nu(G)\leq8\), write
\(Z(Q)_p\) for the \(p\)-primary component of its finite center. Then

\[
\exp\bigl(Z(Q)_2\bigr)\leq4,
\qquad
\exp\bigl(Z(Q)_3\bigr)\leq3,
\qquad
\exp\bigl(Z(Q)_5\bigr)\leq5,
\]

and \(Z(Q)\) has no other primary part. Equivalently,
\(\exp Z(Q)\) divides \(60\). Indeed, the prime-power lemma gives
\(p^e+2\leq8\), so \(p^e\leq6\), for every prime-power order of a
central element.

### [PROVED] The exact central elementary-abelian pairing

Let \(Q=G/Z(G)\), let \(p\) be prime, and let
\(A\leq Z(Q)\) be elementary abelian of exponent \(p\).  Put

\[
W=\{z\in Z(G):z^p=1\},
\]

written additively as an \(\mathbf F_p\)-space.  Lifting \(a\in A\) and
\(q\in Q\) to \(G\), define

\[
b(a,q)=[\widetilde a,\widetilde q]\in W.
\tag{SR.1}
\]

This is independent of the lifts.  Because \(a\) is central in \(Q\), all
the displayed commutators are central in \(G\); the commutator identities
therefore show that \(b\) is additive in both variables.  It is
\(\mathbf F_p\)-linear in \(a\), and its second variable factors through
the elementary abelian quotient

\[
B_p(Q)=Q/(Q'Q^p).
\]

Thus (SR.1) is an \(\mathbf F_p\)-bilinear map
\(A\times B_p(Q)\to W\).  It has zero left radical:

\[
b(a,q)=0\text{ for every }q\in Q\quad\Longrightarrow\quad a=0.
\tag{SR.2}
\]

Indeed, a lift of such an \(a\) commutes with lifts of all elements of
\(Q\), and it commutes with the kernel \(Z(G)\), so it belongs to
\(Z(G)\) and has trivial image in \(Q\).

Write

\[
\beta(a,a')=b(a,a')\qquad(a,a'\in A),
\quad
T_q(a)=b(a,q)\qquad(q\in Q).
\]

Then \(\beta:A\times A\to W\) is alternating.  With the commutator
convention \([x,y]=x^{-1}y^{-1}xy\), two lifts in the same \(Aq\)-fiber
satisfy the exact formula

\[
[\widetilde a\widetilde q,
  \widetilde {a'}\widetilde q]
=\beta(a,a')+T_q(a)-T_q(a').
\tag{SR.3}
\]

In particular, an evaluation-rank argument must retain the internal form
\(\beta\): without an isotropy hypothesis, its first term can cancel the
last two terms.

### [PROVED] Isotropic central fibers have bounded evaluation rank

Continue with the preceding notation and suppose that
\(\beta=b|_{A\times A}=0\).  If

\[
\rho(q)=\operatorname{rank}_{\mathbf F_p}(T_q),
\]

then every \(q\in Q\) gives

\[
\nu(G)\geq p^{\rho(q)}.
\tag{SR.4}
\]

If \(q\notin Z(Q)\), the stronger estimate is

\[
\nu(G)\geq p^{\rho(q)}+2.
\tag{SR.5}
\]

To prove (SR.4), choose one representative from each coset of
\(\ker T_q\) in \(A\).  There are \(p^{\rho(q)}\) representatives, and
(SR.3) says that the corresponding lifts in the \(Aq\)-fiber are pairwise
noncommuting.  If \(q\) is noncentral, choose \(s\in Q\) not commuting
with it.  The three quotient elements \(q,s,qs\) are pairwise
noncommuting.  Since \(A\leq Z(Q)\), arbitrary lifts of \(s\) and \(qs\)
are noncommuting with one another and with every member of the fiber
clique.  This proves (SR.5).

Consequently, if \(Q\) is nonabelian and \(\nu(G)\leq8\), then:

- for \(p=2\), \(\rho(q)\leq3\) for all \(q\), and
  \(\rho(q)\leq2\) for noncentral \(q\);
- for \(p=3\) or \(p=5\), \(\rho(q)\leq1\) for every \(q\).

For \(p\in\{3,5\}\), there is a further scalarization.  The evaluations

\[
\mathcal T=\{T_q:q\in Q\}\leq\operatorname{Hom}_{\mathbf F_p}(A,W)
\]

form a linear space all of whose maps have rank at most one, and (SR.2)
says that their common kernel is zero.  A rank-at-most-one linear space
has one of two forms: either all its images lie in one fixed line of
\(W\), or all its kernels contain one fixed hyperplane of \(A\).  Here is
a short proof.  Fix a nonzero map \(u\otimes\varphi\in\mathcal T\).  For
each rank-one \(v\otimes\psi\in\mathcal T\), the fact that their sum still
has rank at most one forces either \(u,v\) to be dependent or
\(\varphi,\psi\) to be dependent.  If one map has image different from
\(\langle u\rangle\), comparison with it forces every functional to be a
multiple of \(\varphi\); otherwise every image lies in
\(\langle u\rangle\).

The common-hyperplane alternative contradicts (SR.2) when
\(\dim A\geq2\).  Hence, for \(p=3\) or \(5\),

\[
\beta=0,\qquad \nu(G)\leq8,\qquad \dim A\geq2
\quad\Longrightarrow\quad
b(A,Q)\text{ lies in one order-}p\text{ subgroup of }Z(G).
\tag{SR.6}
\]

The hypothesis \(\beta=0\) is essential for the fiber-clique argument;
(SR.3), rather than the rank of \(T_q\) alone, governs a general central
elementary-abelian layer.

### [PROVED] Radical split for a general central layer

For the general pairing (SR.1), put

\[
R=\{a\in A:\beta(a,A)=0\}.
\]

Then \(R\leq Z(Q)\) is elementary abelian and
\(b|_{R\times R}=0\).  The isotropic evaluation-rank theorem therefore
applies verbatim to \(R\): replace \(T_q\) there by \(T_q|_R\).  In
particular, at cutoff eight its ranks are at most three (at most two for
noncentral \(q\)) when \(p=2\), and at most one when
\(p\in\{3,5\}\).  If \(p\in\{3,5\}\) and \(\dim R\geq2\), all values
\(b(R,Q)\) lie in one order-\(p\) subgroup of \(Z(G)\).

The complementary part is an exact alternating-form problem.  The map
\(\beta\) descends to a vector-valued alternating map

\[
\overline\beta:(A/R)\times(A/R)\longrightarrow W
\]

with zero radical.  Inside the preimage of \(A\), two central cosets
commute exactly when their \(\overline\beta\)-value is zero.  Hence its
nonorthogonality graph has clique number at most \(\nu(G)\), and in the
cutoff-eight problem at most eight.  Thus every central elementary-abelian
layer splits rigorously into a zero-radical exterior-form core and the
isotropic radical controlled above; no bound on the rank of a general
\(T_q\) is asserted across the nonisotropic core.

### [PROVED] Quotient geometry of a scalarized odd isotropic layer

Let \(R\leq Z(Q)\) be a nonzero finite-dimensional elementary abelian
\(p\)-subgroup with
\(b|_{R\times R}=0\), and suppose that \(b(R,Q)\) lies in one fixed
order-\(p\) subgroup \(L\leq Z(G)\).  After identifying
\(L\cong\mathbf F_p\), the pairing defines a homomorphism

\[
\tau:Q\longrightarrow R^*,
\qquad \tau(q)(r)=b(r,q).
\tag{SR.7}
\]

It is onto: its image is a linear subspace of the finite-dimensional
space \(R^*\), while the zero left radical (SR.2) says that its
annihilator in \(R\) is zero.  (The finite-dimensional hypothesis is
automatic in the cutoff problem because the preceding finite reduction
makes \(Q\) finite.)  Put
\(N=\ker\tau\).  Every \(q\notin N\) has a \(p\)-point clique in its
\(Rq\)-fiber.

Suppose now that \(\nu(G)\leq8\).

- If \(p=5\), the set \(Q\setminus N\) is pairwise commuting.  Otherwise
  two noncommuting elements outside \(N\) would supply two five-point
  fiber cliques, and distinct fibers are completely joined because their
  quotient representatives do not commute.  This would give a
  ten-clique.  In fact

  \[
  Q\setminus N\subseteq Z(Q).
  \tag{SR.8}
  \]

  To see this, fix \(q\notin N\).  It commutes with every other element
  outside \(N\).  For \(n\in N\), the product \(qn\) is outside \(N\),
  so \([q,qn]=1\), and hence \([q,n]=1\).  Thus \(q\) commutes with all
  of \(Q\).

  This is already impossible when \(Q\) is nonabelian.  Surjectivity of
  \(\tau\) and \(R\ne0\) make \(N\) proper, so choose \(z\notin N\).
  For every \(n\in N\), both \(z\) and \(zn\) lie outside \(N\) and are
  central by (SR.8).  Hence \(n=z^{-1}(zn)\) is central as well.  Thus
  every element of \(Q\) is central, a contradiction.  Consequently a
  nonabelian exact quotient at cutoff eight has no nonzero scalarized
  isotropic \(5\)-layer.

- If \(p=3\) and \(q,r\notin N\) do not commute, then

  \[
  \tau(r)=-\tau(q),\qquad qr\in N.
  \tag{SR.9}
  \]

  Indeed, \(q,r,qr\) are pairwise noncommuting in \(Q\).  If
  \(\tau(qr)=\tau(q)+\tau(r)\ne0\), each of their three fibers contains a
  three-clique, and the three cliques are completely joined across
  fibers, producing a nine-clique.  Therefore \(\tau(qr)=0\), which is
  exactly (SR.9).  Equivalently, outside \(N\), noncommuting pairs can
  occur only between the two evaluation fibers labelled by
  \(\varphi\) and \(-\varphi\) on a single projective line of \(R^*\).

  If \(\dim R\geq2\), this also contradicts nonabelianity of \(Q\).  Fix
  \(q\notin N\), with \(\tau(q)=\varphi\).  First, \(q\) commutes with
  every \(n\in N\): the two outside elements \(q\) and \(qn\) have the
  same nonzero evaluation, not opposite evaluations, so (SR.9) rules out
  noncommutation.  It likewise commutes with every \(r\notin N\) except
  possibly those with \(\tau(r)=-\varphi\).  For such an \(r\), choose
  \(s\in Q\) whose evaluation \(\psi\) is linearly independent from
  \(\varphi\), using surjectivity of \(\tau\).  Both \(s\) and \(rs\)
  have evaluations different from \(-\varphi\), so \(q\) commutes with
  both.  Since a centralizer is a subgroup, it also contains
  \(r=(rs)s^{-1}\).  Thus every element outside \(N\) is central in
  \(Q\).  As in the \(p=5\) case, a fixed \(z\notin N\) and the central
  element \(zn\) then show that every \(n\in N\) is central.  This makes
  \(Q\) abelian, a contradiction.

The same argument gives more than a radical bound.  Let

\[
A_p=\{a\in Z(Q):a^p=1\},
\qquad d_p=\dim_{\mathbf F_p}A_p.
\]

Assume that \(Q\) is finite and nonabelian, \(\nu(G)\leq8\), and
\(p\in\{3,5\}\).  There is no two-dimensional subspace
\(U\leq A_p\) with \(b|_{U\times U}=0\).  Indeed, the isotropic
evaluation-rank theorem and rank-one dichotomy apply to \(U\); since
\(\dim U=2\), (SR.6) scalarizes \(b(U,Q)\).  The preceding \(p=3\) or
\(p=5\) argument then forces \(Q\) to be abelian, a contradiction.

Consequently, if \(a,a'\in A_p\) are linearly independent, then
\(b(a,a')\ne0\).  Choosing one representative from every projective line
of \(A_p\) therefore gives a noncommuting set of size

\[
\frac{p^{d_p}-1}{p-1}\leq8.
\]

For both \(p=3\) and \(p=5\), this implies

\[
\dim_{\mathbf F_p}A_p\leq2.
\tag{SR.10}
\]

In particular, the internal radical of \(b|_{A_p\times A_p}\) has
dimension at most one, but (SR.10) also bounds the zero-radical core.  The
nonabelian hypothesis is essential: when \(Q\) itself is elementary
abelian, scalar symplectic exact extensions supply the known cutoff-seven
and cutoff-eight extremal phenomena.

Together with the central-exponent restriction, (SR.10) gives the concrete
odd-center bound

\[
|Z(Q)|_{\mathrm{odd}}\leq3^2\,5^2=225.
\tag{SR.11}
\]

Indeed, the Sylow \(3\)- and \(5\)-subgroups of \(Z(Q)\) have exponent
\(3\) and \(5\), respectively, so they are exactly the elementary abelian
spaces \(A_3\) and \(A_5\) just bounded.

### [PROVED] The binary central layer has rank at most fourteen

Assume that \(Q=G/Z(G)\) is finite and nonabelian and that
\(\nu(G)\leq8\). Put

\[
A=A_2=\{a\in Z(Q):a^2=1\},
\qquad d_2=\dim_{\mathbf F_2}A.
\]

Then

\[
d_2\leq14,
\qquad |Z(Q)_2|\leq2^{28}.
\tag{SR.12}
\]

We prove first that the internal alternating map
\(\beta=b|_{A\times A}\) from (SR.3) vanishes whenever \(d_2\geq3\).
Suppose instead that some three-dimensional \(U\leq A\) has
\(\beta|_{U\times U}\ne0\). For fixed \(q\in Q\), identify the eight
vertices in the \(Uq\)-fiber with the elements of \(U\). By (SR.3), the
vertices \(a,a'\) commute precisely when

\[
\beta(a,a')+T_q(a+a')=0.
\tag{SR.12a}
\]

Let \(\lambda:\bigwedge^2U\to W\) be induced by \(\beta\), and for
\(0\ne v\in U\) put \(L_v(a)=\beta(a,v)\). The unordered pairs with
difference \(v\) that satisfy (SR.12a) are the solutions of
\(L_v(a)=T_q(v)\), modulo the two-element fibers \(\{a,a+v\}\). Hence
their number is either zero or

\[
2^{\dim\ker L_v-1}.
\tag{SR.12b}
\]

If \(\operatorname{rank}\lambda=3\), every \(L_v\) has rank two, so the
fiber graph has at most seven nonedges. If
\(\operatorname{rank}\lambda=2\), the kernel of \(\lambda\) is generated
by the exterior square of a two-plane \(P\leq U\). The maps \(L_v\) have
rank one for the three nonzero \(v\in P\), and rank two for the other four
directions. Thus there are at most
\(3\cdot2+4\cdot1=10\) nonedges. In either case the graph has at least
eighteen edges. A triangle-free graph on eight vertices has at most sixteen
edges: for every edge \(uv\), the disjointness of the two open neighborhoods
gives \(\deg u+\deg v\leq8\); summing over edges and applying Cauchy--Schwarz
gives
\(4|E|^2/8\leq\sum_v(\deg v)^2\leq8|E|\), hence \(|E|\leq16\).
Thus the fiber contains a triangle.

It remains to handle \(\operatorname{rank}\lambda=1\). Write
\(L=\operatorname{im}\lambda\). If the composite of \(T_q|_U\) with
\(W\to W/L\) is nonzero, a commuting difference must lie in its kernel,
which has dimension at most two. The radical direction of the scalar
alternating form can contribute at most four nonedges, and each of the
other two directions when the kernel contains it contributes at most two.
If the radical direction is absent, all three directions contribute at most
two. There are therefore at most eight nonedges, and again a triangle exists.

Finally suppose that \(T_q(U)\leq L\), and identify \(L\) with
\(\mathbf F_2\). Choose a basis \(e,f,r\) of \(U\) with

\[
\beta(e,f)=1,
\qquad r\in\operatorname{rad}\beta.
\]

If \(T_q(r)=0\), there is a \(t\in\langle e,f\rangle\) such that
\(T_q(u)=\beta(t,u)\) for every \(u\in U\). Translation by \(t\)
identifies (SR.12a) with the graph of \(\beta\), which contains the triangle
\(\{e,f,e+f\}\). If \(T_q(r)=1\), put

\[
u=e+(1+T_q(e))r,
\qquad v=f+(1+T_q(f))r.
\]

Then \(T_q(u)=T_q(v)=1\) and \(\beta(u,v)=1\), so
\(\{0,u,v\}\) is a triangle in the fiber. We have proved that every
\(Uq\)-fiber contains a triangle whenever \(\beta|_U\ne0\).

Choose noncommuting \(q,s\in Q\). The quotient elements \(q,s,qs\) are
pairwise noncommuting, and centrality of \(U\) makes the three fibers
\(Uq,Us,Uqs\) completely joined to one another. A triangle from each
fiber would give a nine-clique in \(G\), a contradiction. Therefore
\(\beta|_U=0\) for every three-space \(U\), and hence

\[
\beta=0\quad\text{on }A\times A.
\tag{SR.12c}
\]

We next bound the evaluation ranks. By (SR.4), every \(T_q|_A\) has rank
at most three; by (SR.5), it has rank at most two when \(q\notin Z(Q)\).
Suppose that a central \(z\in Q\) has \(\operatorname{rank}T_z=3\), and
put \(K=\ker T_z\). One representative from each coset of \(K\) in
\(A\) gives an eight-clique in the \(Az\)-fiber. If a noncentral
\(q\in Q\) did not annihilate \(K\), then inside each coset of \(K\) we
could choose its representative so that the corresponding lift in
\(Az\) does not commute with a fixed lift of \(q\): the commutator changes
by the nonzero map \(T_q|_K\), whereas all pairwise edges inside the fiber
depend only on the distinct \(T_z\)-values. This would adjoin \(q\) to the
eight-clique. Consequently every noncentral \(q\) annihilates \(K\).
Fix one noncentral \(q_0\). For every \(c\in Z(Q)\), the element \(q_0c\)
is noncentral and

\[
T_{q_0c}|_K=T_{q_0}|_K+T_c|_K.
\]

Thus every central element also annihilates \(K\). The zero-left-radical
property (SR.2) now gives \(K=0\), so a rank-three evaluation can occur
only when \(d_2=3\). In particular, if \(d_2\geq4\), every evaluation has
rank at most two.

Choose a maximum noncommuting set
\(X=\{x_1,\ldots,x_m\}\) in \(G\), so \(m\leq8\), and put
\(q_i=x_iZ(G)\) and \(K_i=\ker T_{q_i}\leq A\). Here \(X\) is a clique
in the exact central-coset commutation graph of \(G\), not in the ordinary
noncommuting graph of \(Q\). The kernels cover \(A\): otherwise a lift of
an \(a\in A\setminus\bigcup_iK_i\) could be adjoined to \(X\). Their
intersection is zero: a lift of an element in every \(K_i\) commutes with
all of \(X\), and the maximum-clique center lemma then places it in
\(Z(G)\).

Assume \(d_2\geq4\), and consider the injective map

\[
\Phi:A\longrightarrow\bigoplus_{i=1}^m\operatorname{im}T_{q_i},
\qquad a\longmapsto(T_{q_1}(a),\ldots,T_{q_m}(a)).
\tag{SR.12d}
\]

Every block on the right has dimension at most two, and the kernel-cover
property says that \(\operatorname{im}\Phi\) contains no vector that is
nonzero in every block. If \(m\leq7\), or if one block is zero, the target
of (SR.12d) has dimension at most fourteen. Suppose instead that \(m=8\)
and every block is nonzero. If \(d_2\geq15\), the target dimension is
fifteen or sixteen. In dimension fifteen, injectivity makes
\(\operatorname{im}\Phi\) the whole target, which plainly contains a
full-support vector. In dimension sixteen, the image is either the whole
target or a hyperplane. Write a functional defining the latter hyperplane
blockwise as \(\ell_1+\cdots+\ell_8\). Each two-dimensional block contains
a nonzero vector in \(\ker\ell_i\); their direct sum is a full-support
vector in the hyperplane. Every possibility is contradictory, proving
\(d_2\leq14\).

The central-exponent restriction gives \(\exp Z(Q)_2\leq4\). Therefore
\(Z(Q)_2\cong C_4^u\times C_2^v\), with \(u+v=d_2\), and

\[
|Z(Q)_2|=2^{2u+v}\leq2^{2d_2}\leq2^{28}.
\]

Together with (SR.11), this also gives

\[
|Z(Q)|\leq225\cdot2^{28}.
\]

### [PROVED] Coprime abelian central direct factors cross cutoff nine

Let

\[
Q=A\times H,
\]

where \(Q\) is finite, \(1\ne A\) is abelian, \(H\) is nonabelian, and
\(\gcd(|A|,|H_{\mathrm{ab}}|)=1\).  Every exact center extension
\(G\to Q\), if one exists, satisfies

\[
\nu(G)\geq3\nu(H)\geq9.
\tag{SR.13}
\]

Indeed, the central commutator pairing restricted to \(A\times H\) is
zero.  For fixed \(a\in A\), its values have order dividing \(|a|\),
while it factors through a homomorphism from \(H_{\mathrm{ab}}\); the
coprimality hypothesis forces every value to be trivial.  Exactness then
says that the internal alternating pairing on \(A\) has zero radical.  In
particular, \(A\) cannot be cyclic.  Choose \(a,a'\in A\) with nontrivial
internal commutator.  The three elements \(a,a',aa'\) lift to a
three-clique.

Let \(h_1,\ldots,h_t\) be a maximum noncommuting set in \(H\).  In each
fiber \(Ah_i\), use this same three-clique.  The same-fiber commutators are
unchanged because the cross pairing \(b(A,H)\) is zero.  Points in two
different fibers are noncommuting already in the quotient \(H\).  Their
union is therefore a clique of size \(3t\), proving (SR.13).

If \(A\cong C_p^2\), the sharper projective-line construction gives
\(\nu(G)\geq(p+1)\nu(H)\).

In particular, the capable family \(C_p^2\times S_3\) does not produce a
cutoff-eight exact extension when \(p\) is odd, despite having quotient
clique number four and unbounded order as \(p\) varies.

As a nilpotent consequence, a nonabelian nilpotent exact quotient at
cutoff eight must be a \(p\)-group.  If two Sylow subgroups were
nonabelian, a three-clique in each would give a nine-clique in their direct
product already in \(Q\).  If exactly one Sylow subgroup \(H\) were
nonabelian and another Sylow factor \(A\) were nontrivial, that \(A\) would
be an abelian central direct factor coprime to \(H_{\mathrm{ab}}\), and
(SR.13) would give the same contradiction.

## Isoclinism and stem groups

### [PROVED] Isoclinism preserves exactly the two invariants

Suppose \(G\) and \(H\) are isoclinic: there are isomorphisms

\[
\alpha:G/Z(G)\longrightarrow H/Z(H),\qquad
\beta:G'\longrightarrow H'
\]

compatible with the commutator maps. Then \(\alpha\) is an isomorphism
\(\Delta_G\cong\Delta_H\). Compatibility says that if
\(\alpha(xZ(G))=x'Z(H)\) and
\(\alpha(yZ(G))=y'Z(H)\), then
\(\beta([x,y])=[x',y']\). Since \(\beta\) is injective,
\([x,y]=1\) if and only if \([x',y']=1\). Therefore
\(\nu(G)=\nu(H)\) and \(a(G)=a(H)\).

### [CITED-VERIFIED] Finite central factor gives a finite stem representative

Hall (1940), printed p. 135, proves for arbitrary groups that every
isoclinism family contains a stem representative \(S\) with
\(Z(S)\leq S'\). Wiegold (1965), Theorem 2.1(i), printed pp. 345--346,
proves that a group with finite central factor has finite derived subgroup;
his §3.3 on p. 346 then combines this with Hall's theorem to obtain a finite
isoclinic stem representative. These primary-source checks are recorded in
`audit/source_audit.md`, under “Primary stem and cutoff-eight \(p\)-group
audit.”

[PROVED] Combining those verified source facts with the preceding isoclinism
lemma, this finite stem group has the same \((\nu,a)\) and an isomorphic
central quotient.  The independent finite commutation-model theorem above
remains useful because it avoids isoclinism theory entirely.

### [UNVERIFIED] Quantitative BFC citation obligation

The exact quantitative form and primary-source hypotheses of the BFC theorem
“uniformly finite conjugacy classes imply finite derived subgroup” have not
been checked here and are not used above. The needed uniform conjugacy-class
bound and the exact finite commutation model are proved directly in this
note. Finite central factor, by contrast, is covered by the verified
Hall--Wiegold result in the preceding paragraph.

## Adversarial checks on tempting reductions

### [DISPROVED] Literal quotient and subgroup shortcuts

The following shortcuts are invalid.

1. Replacing \(G\) by \(G/Z(G)\) can erase noncommutation; \(D_8\) is the
   smallest standard counterexample recorded in foundations.md.
2. The subgroup \(H=\langle T\rangle\) generated by a central transversal need
   not be finite. For example, in \(Q_8\times\langle z\rangle\), choosing a
   representative \((i,z)\) can make \(H\) contain a nontrivial infinite power
   of \(z\).
3. An arbitrary finite quotient of \(H\) can kill a nontrivial commutator. The
   finite-model proof must choose \(N\) to avoid every nontrivial commutator
   among the finitely many transversal representatives.
4. The constructed finite model preserves the zero/nonzero pattern of the
   commutator map. It need not preserve all commutator values, so isoclinism
   is not being silently asserted.
