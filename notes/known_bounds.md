# Known Bounds

No literature bound is treated as verified here unless the exact primary
theorem, hypotheses, and proof have been read. This note first records a
fully self-contained quadratic-exponent bound, valid for arbitrary groups.

## A self-contained Ramsey bound

### [PROVED] Independent center-index bound

Let \(G\) be any group with \(\nu(G)=n<\infty\), and put

\[
r_n=R(n+1,n+1)-1.
\]

Then

\[
[G:Z(G)]\leq r_n^n
\leq\left({2n\choose n}-1\right)^n
<4^{n^2}=2^{2n^2}.
\]

**Proof.** By structural_reductions.md, every element centralizer has index
at most \(r_n\), and if \(X=\{x_1,\ldots,x_n\}\) is a maximum noncommuting
set then \(Z(G)=\bigcap_i C_G(x_i)\). For finite-index subgroups
\(H_i\leq G\), the map

\[
G/\bigcap_iH_i\longrightarrow\prod_i G/H_i,\qquad
g\bigcap_iH_i\longmapsto(gH_i)_i
\]

is injective as a map of sets. Hence the index of an intersection is at most
the product of the indices, giving \([G:Z(G)]\leq r_n^n\). The finite Ramsey
recurrence gives \(R(n+1,n+1)\leq{2n\choose n}\), and the central binomial
coefficient is strictly smaller than the sum \(4^n\) of all coefficients in
\((1+1)^{2n}\). \(\square\)

### [PROVED] Abelian-cover and \(h(n)\) bounds

If \(G\) is nonabelian and \(q=[G:Z(G)]\), then

\[
a(G)\leq q-1.
\]

Indeed, for one representative \(t\) of each nonidentity central coset, the
abelian subgroups \(\langle t,Z(G)\rangle\) cover \(G\); every one also
contains the identity central coset. Equivalently, \(\Delta_G\) has \(q\)
vertices, one isolated, and can be colored with at most \(q-1\) colors.
Therefore, for \(n\geq3\),

\[
h(n)\leq r_n^n-1<4^{n^2}.
\]

This also proves directly, without Pyber's theorem, that \(h(n)\) is finite.

## A self-contained factorial center-index bound

### [PROVED] Maximum-clique centralizers give \([G:Z(G)]\leq\nu(G)!\)

Let \(G\) be any group with \(m=\nu(G)<\infty\). Then

\[
[G:Z(G)]\leq m!.
\tag{KB.1}
\]

We first recall and prove the required factorial cover lemma. Suppose

\[
G=H_1g_1\cup\cdots\cup H_sg_s
\]

is an irredundant right-coset cover and \(D=\bigcap_iH_i\). For every
\(r\in\{0,\ldots,s-1\}\), every intersection \(K\) of \(s-r\) of the
subgroups \(H_i\) satisfies

\[
[K:D]\leq r!.
\tag{KB.2}
\]

The proof is by induction on \(r\). The case \(r=0\) is immediate. After
relabeling, let \(K=H_1\cap\cdots\cap H_{s-r}\). Irredundancy gives an
element \(x\) outside the first \(s-r\) covering cosets. Then the whole
coset \(Kx\) is outside them and is covered by the remaining \(r\) cosets.
Every nonempty intersection of \(Kx\) with \(H_jg_j\) has the form
\((K\cap H_j)z\). By induction,
\([K\cap H_j:D]\leq(r-1)!\). Thus \(Kx\) is covered by at most \(r\)
sets, each containing at most \((r-1)!\) left \(D\)-cosets, and (KB.2)
follows.

Now let \(X=\{x_1,\ldots,x_m\}\) be a maximum pairwise noncommuting set in
\(G\). Its centralizers cover \(G\), because an element outside all of them
could be adjoined to \(X\). The cover is irredundant: \(x_i\) belongs to
\(C_G(x_i)\) and to no \(C_G(x_j)\) with \(j\ne i\). The proved
common-centralizer lemma gives

\[
\bigcap_{i=1}^m C_G(x_i)=Z(G).
\]

Take \(r=m-1\) in (KB.2). Each centralizer is a union of at most
\((m-1)!\) left \(Z(G)\)-cosets. Their union is all of \(G\), so

\[
[G:Z(G)]
\leq\sum_{i=1}^m[C_G(x_i):Z(G)]
\leq m(m-1)!=m!.
\]

This proof does not assume that \(G\) is finite; the finite index is a
conclusion. In particular,

\[
\nu(G)\leq8\quad\Longrightarrow\quad
[G:Z(G)]\leq8!=40\,320.
\tag{KB.3}
\]

For a nonabelian group, the usual one subgroup
\(\langle t,Z(G)\rangle\) per nonidentity central coset also gives
\(a(G)\leq m!-1\). The stronger centralizer recurrences below give better
bounds for \(a(G)\), but (KB.1) is useful because it directly bounds the
complete list of possible center quotients.

## A CFSG-dependent subfactorial bound

### [PROVED] Published-input center-index bound

There is an absolute constant \(C>0\) such that every group with
\(n=\nu(G)\ge3\) satisfies

\[
[G:Z(G)]\le \exp\!\bigl(Cn\log\log n\bigr),
\qquad
h(n)\le2^{O(n\log\log n)}.
\]

The complete proof, including the arbitrary-to-finite transfer and all
intermediate index estimates, is in `notes/subfactorial_upper.md`.  Its two
external premises were read at proof level: Guralnick--Maróti, Theorem 1.8,
bounds the derived subgroup of a BFC group, and Nagy--Pach--Tomon,
Theorem 1.11 with Section 8, bounds the intersection index of an irredundant
coset cover of an abelian group.  The former premise is CFSG-dependent.

This theorem is strictly weaker than the fixed-base \(c^n\) estimate stated
in Pyber's official abstract.  It does, however, improve all self-contained
repository upper bounds asymptotically.  It does not use the distinct
withdrawn arXiv:2205.03389 claim of a \(2^{O(k)}\) abelian cover theorem.

### [PROVED] First recursive cover bound

For every \(n\geq2\),

\[
h(n)\leq n\,h(n-1).
\]

**Proof.** Monotonicity \(h(m)\leq h(n)\) for \(m\leq n\) follows directly
from the defining nested classes of groups. Let \(G\) satisfy
\(\nu(G)=m\leq n\). If \(G\) is abelian, \(a(G)=1\). Otherwise \(m\geq3\);
choose a maximum clique \(X=\{x_1,\ldots,x_m\}\). Maximality gives

\[
G=\bigcup_{i=1}^m C_G(x_i),
\]

because an element outside all these centralizers could be adjoined to
\(X\). Every \(x_i\) is noncentral. The centralizer-drop lemma in
structural_reductions.md gives
\(\nu(C_G(x_i))\leq m-1\), so \(C_G(x_i)\) is covered by at most
\(h(m-1)\) abelian subgroups. These are also subgroups of \(G\). Therefore

\[
a(G)\leq m h(m-1)\leq n h(n-1).
\]

Taking the supremum over \(G\) proves the recurrence. \(\square\)

Iterating from \(h(2)=1\) gives the standalone bound

\[
h(n)\leq n!/2\qquad(n\geq2).
\]

This is weaker asymptotically than the CFSG-dependent subfactorial bound
above.

### [PROVED] Strengthened recursive cover bound

The centralizer drop can in fact be sharpened by two, not merely one:
notes/candidate_bound.md, Lemma CB.2, proves

\[
\nu(C_G(x))\leq \nu(G)-2\qquad(x\notin Z(G)).
\]

Applying the same maximum-clique centralizer cover therefore gives

\[
h(n)\leq n\,h(n-2)\qquad(n\geq3).
\]

Iteration from \(h(1)=h(2)=1\) yields

\[
h(2r+1)\leq(2r+1)!!,\qquad
h(2r)\leq\frac{(2r)!!}{2}=2^{r-1}r!.
\]

This strictly improves the preceding factorial recurrence. It is still
superexponential and hence weaker asymptotically than both the proved
CFSG-dependent subfactorial bound above and Pyber's reported fixed-base
exponential theorem, whose primary proof remains inaccessible.

### [PROVED] Private-cell recurrence

For every \(n\geq3\),

\[
h(n)\leq 1+(n-1)h(n-2).
\]

**Proof.** Let \(G\) satisfy \(\nu(G)=m\leq n\). If \(G\) is abelian, then
\(a(G)=1\), so suppose that \(G\) is nonabelian. Thus \(m\geq3\). Choose a
maximum noncommuting set \(X=\{x_1,\ldots,x_m\}\), put
\(C_i=C_G(x_i)\), and define the private cell

\[
P_i=C_i\mathbin{\big\backslash}\bigcup_{k\ne i}C_k.
\]

Each \(P_i\) is nonempty: \(x_i\in P_i\), because the members of \(X\) are
pairwise noncommuting. Moreover, \(P_i\) is a pairwise commuting set. Indeed,
if \(y,z\in P_i\) did not commute, then each of \(y,z\) would fail to commute
with every \(x_k\) for \(k\ne i\), and hence

\[
(X\setminus\{x_i\})\cup\{y,z\}
\]

would be a noncommuting set of size \(m+1\), a contradiction. Consequently
\(A_i=\langle P_i\rangle\) is an abelian subgroup: all generators in \(P_i\)
commute pairwise, so all words in those generators and their inverses commute.
This is the step for which treating a commuting set itself as a subgroup would
not suffice.

Fix an index \(j\). The usual maximum-clique argument gives
\(G=\bigcup_i C_i\). If an element \(g\) lies outside every \(C_i\) with
\(i\ne j\), it must therefore lie in \(C_j\), and then the definition gives
\(g\in P_j\subseteq A_j\). Thus the following is an actual subgroup cover:

\[
G=A_j\cup\bigcup_{i\ne j}C_i.
\]

Every \(x_i\) is noncentral, and the proved two-step centralizer drop gives
\(\nu(C_i)\leq m-2\). Covering each of the \(m-1\) displayed centralizers by
at most \(h(m-2)\) abelian subgroups, while retaining the single abelian
subgroup \(A_j\), yields

\[
a(G)\leq1+(m-1)h(m-2)
      \leq1+(n-1)h(n-2).
\]

Here the last inequality uses monotonicity of \(h\). Taking the supremum over
all \(G\) with \(\nu(G)\leq n\) proves the recurrence. The argument applies to
arbitrary groups; the abelian and trivial cases were separated at the start,
and no finiteness or choice of coset representatives is used. \(\square\)

For example, the exact value \(h(6)=6\) gives the unconditional improvement

\[
h(8)\leq1+7h(6)=43,
\]

in place of the preceding recurrence's bound \(h(8)\leq8h(6)=48\).

## Specialized class-two bounds

### [PROVED] Charged abelian and relative-center layers

Let \(P\) be a finite \(p\)-group of nilpotency class at most two and put
\(m=\nu(P)\).  The centralizer-chain block construction in
`class_two_abelian_layer.md` proves, for every abelian subgroup
\(A\ge Z(P)\),

\[
[A:Z(P)]\le p^{m/p}\le3^{m/3}.
\]

More generally, if \(Z(P)\le H\le P\) and \(r=\nu(H)\), then

\[
[Z(H):Z(P)]\le p^{(m-r)/p}\le3^{(m-r)/3}.
\]

The proof builds a genuine clique block of size equal to each strict
centralizer-chain index, so the sum of those indices is charged to \(m\),
or to \(m-r\) in the relative form.  It does not bound the complementary
index \([P:H]\); that is the explicitly recorded remaining local obstacle
to a fixed-base class-two theorem.

## The quadratic conjugacy-class mechanism

### [PROVED] Finite-group conjugacy-class bound

If \(F\) is a finite group with \(\nu(F)=n\), then every conjugacy class of
\(F\) has size at most \(4n^2\).

**Proof.** List the conjugacy classes \(D_1,\ldots,D_s\) in nondecreasing
order of size, and let \(r\) be least such that

\[
|D_1|+\cdots+|D_r|>|F|/2.
\]

Put \(X=F\setminus(D_1\cup\cdots\cup D_{r-1})\), so
\(|X|\geq |F|/2\). Choose a clique
\(\{x_1,\ldots,x_\ell\}\) of maximum size in the graph induced on \(X\).
Then \(\ell\leq n\), and maximality (by inclusion, which follows from
maximum cardinality) gives

\[
X\subseteq C_F(x_1)\cup\cdots\cup C_F(x_\ell).
\]

Consequently some \(j\) satisfies

\[
|C_F(x_j)|\geq |X|/\ell\geq |F|/(2n).
\]

The element \(x_j\) belongs to a class \(D_t\) with \(t\geq r\). Therefore

\[
|D_r|\leq |x_j^F|=[F:C_F(x_j)]\leq2n.
\]

Now set \(Y=D_1\cup\cdots\cup D_r\). For each \(g\in F\), the two subsets
\(Y\) and \(gY\), each of size greater than \(|F|/2\), intersect. Thus
\(g=yz^{-1}\) for some \(y,z\in Y\), and hence
\(g\in D_iD_j^{-1}\) for some \(i,j\leq r\). The product
\(D_iD_j^{-1}\) is invariant under conjugation, so it contains the entire
class \(g^F\). It follows that

\[
|g^F|\leq |D_i|\,|D_j|\leq |D_r|^2\leq4n^2.
\]

The inverse on \(D_j^{-1}\) is essential for the literal argument. A
secondary exposition (Saccochi, 2015, Lemma 4.1.2, printed pp. 34--35)
writes \(YY\); replacing this by \(YY^{-1}\) repairs the notation without
changing the estimate. \(\square\)

### [PROVED] Transfer to arbitrary groups

Let \(G\) be arbitrary with \(\nu(G)=n<\infty\). The Ramsey argument above
first proves \([G:Z(G)]<\infty\), and the finite commutation-model theorem in
structural_reductions.md then gives a finite \(K\) with
\(\Delta_K\cong\Delta_G\). For corresponding central cosets \(gZ(G)\) and
\(kZ(K)\), the graph isomorphism identifies the central cosets that commute
with them: these are precisely the vertices in the closed non-neighborhood
of the corresponding vertex. Therefore

\[
[G:C_G(g)]
=
[G/Z(G):C_G(g)/Z(G)]
=
[K/Z(K):C_K(k)/Z(K)]
=
[K:C_K(k)].
\]

The finite lemma applied to \(K\) now shows that every conjugacy class of
\(G\) has size at most \(4n^2\).

### [PROVED] Improved center-index and \(h(n)\) bounds

For a maximum noncommuting set \(x_1,\ldots,x_n\), the proved identity
\(Z(G)=\bigcap_iC_G(x_i)\) and the preceding class bound give

\[
[G:Z(G)]
\leq\prod_{i=1}^n[G:C_G(x_i)]
\leq(4n^2)^n
=2^{2n(1+\log_2n)}.
\]

Consequently

\[
h(n)\leq(4n^2)^n-1\qquad(n\geq3).
\]

This proof is self-contained modulo the finite-model and elementary
finitely-generated-abelian lemmas proved in structural_reductions.md. It is
strictly stronger than the independent \(4^{n^2}\) Ramsey bound for
\(n\geq3\), but the latter is retained because it proves the central
finite-index input needed before the finite model is constructed.

## Boundary values

### [PROVED] Nonabelian groups have \(\nu\geq3\)

If \(x\) and \(y\) do not commute, then \(x,y,xy\) are pairwise
noncommuting: equality \(x(xy)=(xy)x\), or equality \(y(xy)=(xy)y\), would
in either case imply \(xy=yx\). Hence the value \(2\) never occurs as
\(\nu(G)\).

### [PROVED] Exact values \(h(1)=h(2)=1\)

A group has \(\nu(G)=1\) exactly when it is abelian, and every nonabelian group
has \(\nu(G)\geq3\). Thus the conditions \(\nu(G)\leq1\) and
\(\nu(G)\leq2\) both force \(G\) to be abelian, for which \(a(G)=1\).

### [PROVED] Exact value \(h(3)=3\)

The recursive bound and \(h(2)=1\) give \(h(3)\leq3\).

The bound is attained by \(D_8\): its central-coset graph is an isolated
identity coset plus a triangle on \(rZ(D_8),sZ(D_8),rsZ(D_8)\). Hence
\(\nu(D_8)=a(D_8)=3\), and \(h(3)=3\).

### [PROVED] Exact value \(h(4)=4\)

The strengthened recurrence gives \(h(4)\leq4h(2)=4\). The group
\(S_3\) has an abelian subgroup of order three and three reflection
subgroups, giving an abelian cover of size four. Its three reflections
together with a nonidentity rotation are pairwise noncommuting, so
\(\nu(S_3)=a(S_3)=4\). Hence \(h(4)=4\).

### [PROVED] Exact values through seven

The computer-assisted proofs in `notes/exact_h5.md`, `notes/exact_h6.md`,
and `notes/exact_h7.md` give

\[
h(5)=5,\qquad h(6)=6,\qquad h(7)=10.
\]

At cutoffs five, six, and seven, audited irredundant-cover bounds reduce the
center quotient to orders at most 16, 36, and 81, respectively.  Complete
Schur-cover/exterior-square certificates then give the upper bounds.  The
matching witnesses are the scalar symplectic groups used in those notes.
The cutoff-seven proof exhausts a disjoint 738-type quotient inventory; its
finite certificates and final verification hashes are recorded in
`proof/computational_appendix.tex`.

## A closed finite \(5\)-group branch at cutoff eight

### [PROVED] Finite \(5\)-groups with \(\nu\leq8\)

If \(P\) is a finite \(5\)-group with \(\nu(P)\leq8\), then either \(P\) is
abelian and

\[
  (\nu(P),a(P))=(1,1),
\]

or

\[
  (\nu(P),a(P))=(6,6).
\]

The proof is computer-assisted. Berkovich's primary-verified lower and
structure theorems reduce the nonabelian case to excluding clique numbers
seven and eight; his Proposition 4.5 also forces at least six maximal
members in an eight-centralizer cover. After enlarging the other at most
two members and passing to \(P/\Phi(P)\), a self-contained reduction plus an
exact enumeration in dimensions two, three, and four shows that every cover
by at most eight \(\mathbf F _5\)-hyperplanes contains a full six-member
pencil. A genuinely new pencil member would then be covered by at most four
proper subgroups, which is impossible for a finite \(5\)-group. The complete
proof, source audit, certificate, and reproduction command are in
notes/five_group_nu8.md. This closes only the finite \(5\)-group branch; it
does not determine \(h(8)\).

## Stronger reported bounds still under audit

### [UNVERIFIED] Pyber's exponential center-index theorem

The official abstract of L. Pyber, “The Number of Pairwise Non-Commuting
Elements and the Index of the Centre in a Finite Group,” J. London Math.
Soc. (2) 35 (1987), 287–295, DOI 10.1112/jlms/s2-35.2.287, reports an
absolute constant \(c\) with
\([G:Z(G)]\leq c^{\nu(G)}\) for finite \(G\). The full primary proof, exact
constant conventions, and every quantitative loss have not yet been checked,
so the result is not load-bearing here. Once verified for finite groups, the
exact finite-model theorem in structural_reductions.md transfers it without
loss to arbitrary groups and yields \(h(n)\leq c^n-1\) for \(n\geq3\).

The checked secondary exposition (Saccochi, 2015, printed p. 36) displays
the explicit estimate

\[
[G:Z(G)]
\leq
2^{\,2^{25}n}\,2^{\,3(2+2\log_2n)^5}
\]

and attributes its details to Pyber's Theorem 6.1. This formula remains
unverified until the primary proof is checked. The thesis explicitly
reduces to finite groups before its sketch and then uses finiteness again in
the order bound for \(G'\), the finite nilpotent subgroup
\(C=C_G(G')\), and the Sylow direct-product decomposition. The exact finite
commutation model would discharge only the initial finite-reduction step; it
does not verify those primary quantitative ingredients.

### [UNVERIFIED] Remaining quantitative structural obligations

The Guralnick--Maróti BFC derived-subgroup theorem is now audited and used in
the CFSG-dependent subfactorial bound above.  Pyber's fixed-base argument,
its constants, and any sharper CFSG-free replacement remain unaudited.
None is needed for the self-contained \(4^{n^2}\) and \((4n^2)^n\) bounds
or the exact finite reduction.
