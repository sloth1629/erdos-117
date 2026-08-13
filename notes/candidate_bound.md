# Audit of the proposed binary-symplectic bound

Consider the proposed inequality

\[
h(n)\leq \max\!\left\{n,2^{\lfloor(n-1)/2\rfloor}+1\right\}. \tag{CB}
\]

## The proposal is false

### Candidate (CB) [DISPROVED]

The group constructed below has \(\nu=7\) and \(a=10\). Consequently
\(h(7)\geq10\), whereas the right side of (CB) at \(n=7\) is \(9\).
The same example also gives \(h(8)\geq10>9\).

### The counterexample

#### Theorem CB.1 [PROVED]

There is a group \(H\) of order \(3^5=243\) such that

\[
\nu(H)=7,\qquad a(H)=10.
\]

**Construction.** Put \(X=Y=\mathbb F_3^2\), and define

\[
H=X\times Y\times\mathbb F_3
\]

with multiplication

\[
(x,y,z)(x',y',z')
=\bigl(x+x',y+y',z+z'+x\mathbin\cdot y'\bigr).
\]

Bilinearity proves associativity. The identity is \((0,0,0)\), and

\[
(x,y,z)^{-1}=(-x,-y,-z+x\mathbin\cdot y),
\]

so this is a group. Direct calculation gives the commutator form on
\(V=X\oplus Y\):

\[
B((x,y),(x',y'))=x\mathbin\cdot y'-x'\mathbin\cdot y.
\]

This alternating form is nondegenerate, so

\[
Z(H)=\{(0,0,z):z\in\mathbb F_3\},
\qquad H/Z(H)\cong V.
\]

Thus two central cosets commute exactly when their vectors are orthogonal
under \(B\).

**Proof that \(a(H)=10\).** The image in \(V\) of an abelian subgroup of
\(H\) is a totally isotropic vector subspace. If \(U\leq V\) is totally
isotropic, then \(U\leq U^\perp\); nondegeneracy and
\(\dim U+\dim U^\perp=4\) give \(\dim U\leq2\). Hence one abelian subgroup
covers at most \(3^2-1=8\) of the \(80\) nonzero vectors of \(V\). Every
abelian cover therefore has at least \(80/8=10\) members.

Here is an explicit cover attaining that bound. For
\(s,t\in\mathbb F_3\), let

\[
A_{s,t}=\begin{pmatrix}s&t\\t&s+t\end{pmatrix},\qquad
L_{s,t}=\{(x,A_{s,t}x):x\in\mathbb F_3^2\},
\]

and put

\[
L_\infty=\{(0,y):y\in\mathbb F_3^2\}.
\]

All ten subspaces are totally isotropic because every \(A_{s,t}\) is
symmetric. Moreover

\[
\det A_{s,t}=s^2+st-t^2
\]

is nonzero whenever \((s,t)\ne(0,0)\): for \(t=0\) this is immediate, while
for \(t\ne0\), writing \(r=s/t\) reduces the assertion to checking
\(r^2+r-1\ne0\) for \(r=0,1,2\). Therefore the difference of any two
distinct matrices in this family is invertible. It follows that the nine
graphs \(L_{s,t}\), together with \(L_\infty\), meet pairwise only in zero.
They contain \(10(3^2-1)=80\) distinct nonzero vectors, so they partition
\(V\setminus\{0\}\). Their full preimages in \(H\) are ten abelian
subgroups covering \(H\). Thus \(a(H)=10\).

**Proof that \(\nu(H)=7\).** Reorder the preceding \(X\oplus Y\)
coordinates into interleaved symplectic coordinates \(v=(a,b,c,d)\), in
which

\[
B(v,v')=ab'-ba'+cd'-dc'.
\]

The following seven vectors are pairwise nonorthogonal:

\[
\begin{split}
&(1,0,0,0),\quad(0,1,0,0),\quad(1,1,0,0),\\
&(-1,1,0,1),\quad(-1,1,1,0),\quad
(-1,1,1,1),\quad(-1,1,1,-1).
\end{split}
\]

Indeed, the last four have \((c,d)\)-pairs representing the four
one-dimensional subspaces of \(\mathbb F_3^2\), so their mutual determinants
are nonzero. Their first two coordinates are equal, and hence contribute
zero to their mutual pairings. Pairings involving any of the first three
vectors are immediate and nonzero. Representatives in the corresponding
central cosets give a noncommuting set of size seven.

For the upper bound, let \(v_1,\ldots,v_r\) be pairwise nonorthogonal
vectors. No two are nonzero scalar multiples. If \(r\geq2\), rescale the
first two and extend them to a symplectic basis, so that
\(v_1=(1,0,0,0)\) and \(v_2=(0,1,0,0)\). Every remaining projective point
has a unique representative of the form

\[
(\epsilon,1,u),\qquad \epsilon\in\{1,-1\},\quad
u\in\mathbb F_3^2.
\]

Let \(P\) be the set of \(u\)'s arising with \(\epsilon=1\), and \(M\) the
set arising with \(\epsilon=-1\). With
\(\det(u,u')=u_1u'_2-u_2u'_1\), pairwise nonorthogonality says

\[
\det(p,p')\ne0,\qquad \det(m,m')\ne0,
\qquad \det(p,m)\ne1                                      \tag{1}
\]

for distinct \(p,p'\in P\), distinct \(m,m'\in M\), and all
\(p\in P,m\in M\).

We claim that (1) forces \(|P|+|M|\leq5\). An internally admissible set in
\(\mathbb F_3^2\) contains at most one vector from each of the four
one-dimensional directions, so each of \(P,M\) has size at most four. If
one has size at most one, the claim follows. Otherwise, reorder two members
of \(P\) so that their determinant is \(-1\), and apply an element of
\(\operatorname{SL}_2(3)\) to make them

\[
p_1=(0,1),\qquad p_2=(1,0).
\]

The cross condition in (1) then confines \(M\) to

\[
R=\{(0,0),(0,-1),(1,0),(1,-1)\}.
\]

As \(|M|\geq2\), zero cannot occur, leaving only three candidates

\[
r_0=(0,-1),\qquad s_0=(1,0),\qquad t_0=(1,-1).             \tag{2}
\]

This already proves \(|P|+|M|\leq5\) when \(|P|=2\). If \(P\) has a third
member \(p=(x,y)\), then \(x,y\in\{1,-1\}\). For

\[
(x,y)=(1,1),(1,-1),(-1,1),(-1,-1),
\]

respectively, the cross condition excludes from \(M\), respectively,

\[
t_0,\quad s_0,\quad r_0,\quad\{r_0,s_0\}.
\]

Hence \(|M|\leq2\), which settles \(|P|=3\).

Finally, if \(|P|=4\), its other two directions have representatives

\[
u\in\{(1,1),(-1,-1)\},\qquad
w\in\{(1,-1),(-1,1)\}.
\]

Among the three candidates (2), the two choices for \(u\) allow,
respectively, \(\{r_0,s_0\}\) or \(\{t_0\}\), while the two choices for
\(w\) allow, respectively, \(\{r_0,t_0\}\) or
\(\{s_0,t_0\}\). Their intersection has size at most one. Thus
\(|M|\leq1\), completing the claim. Therefore \(r\leq2+5=7\), and the
displayed seven vectors prove \(\nu(H)=7\). \(\square\)

The proof is entirely internal and does not depend on computation.

## A universal recurrence that survives the counterexample

### Lemma CB.2 [PROVED]

If \(x\notin Z(G)\) and \(\nu(G)<\infty\), then

\[
\nu(C_G(x))\leq \nu(G)-2.
\]

**Proof.** Let \(a_1,\ldots,a_\ell\) be pairwise noncommuting elements of
\(C_G(x)\), and choose \(y\) with \(xy\ne yx\). Define

\[
b_i=\begin{cases}
a_i,&a_i y\ne y a_i,\\
x a_i,&a_i y=y a_i.
\end{cases}
\]

Because every \(a_i\) commutes with \(x\), multiplying any selected \(a_i\)
by \(x\) preserves every pairwise commutation relation among the selected
elements: both products have the same leading power of \(x\), followed by
\(a_i a_j\) or \(a_j a_i\).

If \(a_i\) fails to commute with \(y\), then it also fails to commute with
\(xy\); equality \(a_i(xy)=(xy)a_i\), together with \(a_ix=xa_i\), would
imply \(a_i y=y a_i\). If \(a_i\) commutes with \(y\), then \(xa_i\)
fails to commute with \(y\), because equality would imply \(xy=yx\).
It also fails to commute with \(xy\): equality

\[
(xa_i)(xy)=(xy)(xa_i)
\]

reduces, using \(a_i x=x a_i\) and \(a_i y=y a_i\), to \(xy=yx\).
Finally, \(y\) and \(xy\) fail to commute. Hence

\[
\{b_1,\ldots,b_\ell,y,xy\}
\]

is a pairwise noncommuting set, and
\(\ell+2\leq\nu(G)\). Taking the maximum over such sets in \(C_G(x)\)
proves the assertion. \(\square\)

### Corollary CB.3 [PROVED]

For every \(n\geq3\),

\[
h(n)\leq n\,h(n-2).
\]

Consequently, for \(m\geq1\),

\[
h(2m+1)\leq(2m+1)!!,
\]

and

\[
h(2m)\leq\frac{(2m)!!}{2}
=2^{m-1}m!\leq(2m)!!.
\]

**Proof.** A nonabelian group contains the pairwise noncommuting triple
\(x,y,xy\), so \(h(1)=h(2)=1\). Let \(G\) be nonabelian, put
\(r=\nu(G)\leq n\), and choose a maximum noncommuting set \(S\) of size
\(r\). Maximality gives

\[
G=\bigcup_{x\in S}C_G(x).
\]

Every \(x\in S\) is noncentral, so Lemma CB.2 gives
\(\nu(C_G(x))\leq r-2\leq n-2\). Covering each centralizer and taking their
union gives

\[
a(G)\leq\sum_{x\in S}a(C_G(x))
\leq r h(n-2)\leq n h(n-2).
\]

Taking the supremum over \(G\), then iterating from the two base cases,
proves all three displayed bounds. The even estimate with the factor
\(1/2\) is the direct iteration from \(h(2)=1\); the looser
\((2m)!!=2^m m!\) is of course also valid. \(\square\)

### Corollary CB.4 [PROVED]

\[
h(4)=4.
\]

**Proof.** Corollary CB.3 gives \(h(4)\leq4h(2)=4\). In \(S_3\), the
three transpositions are pairwise noncommuting, each fails to commute with
either \(3\)-cycle, and the two \(3\)-cycles commute with each other.
Therefore \(\nu(S_3)=4\). Each transposition lies in a unique subgroup of
order \(2\), and the two \(3\)-cycles lie in the unique subgroup of order
\(3\). Those four abelian subgroups cover \(S_3\), and no three abelian
subgroups can cover the three transpositions and a \(3\)-cycle. Hence
\(a(S_3)=4\), proving the reverse inequality. \(\square\)

## Structural conclusion

### Conclusion CB.5 [PROVED]

Scalar symplectic commutator maps over \(\mathbb F_2\) do not control the
extremal problem: changing the ground field to \(\mathbb F_3\), while keeping
the commutator codomain one-dimensional, already beats (CB).
Higher-dimensional commutator codomains are therefore not needed to refute
the proposal.
