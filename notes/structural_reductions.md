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

### [PROVED] Cutoff-eight central-prime restriction

If \(Q=G/Z(G)\) is nonabelian and \(\nu(G)\leq8\), every prime-order
element of \(Z(Q)\) has order in \(\{2,3,5\}\). In particular,
\(Z(Q)\) has no element of order \(7\).

This is immediate from the prime-order central fiber lemma:
\(p+2\leq8\), and the only primes at most six are \(2,3,5\).

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

### [UNVERIFIED] Stem-representative obligation

The standard assertion that every isoclinism family contains a stem group
\(S\) with \(Z(S)\leq S'\), and that a family with finite central quotient has
a finite stem representative, has not yet been reconstructed here or checked
against its primary source. Once verified, isoclinism invariance would show
that extremizers may be taken finite and stem. The finite commutation-model
theorem already proves the finite-extremizer statement without this assertion,
but its output need not be isoclinic to \(G\) and is not claimed to be stem.

### [UNVERIFIED] Schur/BFC citation obligation

The classical consequences “finite central quotient implies finite derived
subgroup” (Schur) and “uniformly finite conjugacy classes imply finite derived
subgroup” (the BFC theorem of B. H. Neumann) are not used in any proof above.
Their exact quantitative versions and primary-source hypotheses remain to be
verified before use. What is proved here is the required uniform BFC bound
and the stronger-for-this-purpose exact finite commutation model.

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
