# The binary order-\(128\) symplectic boundary

## Status and scope

[PROVED] (computer-assisted) This note closes the sole boundary left by
notes/two_group_inclusion_maximal_centralizers.md.  It is intentionally
separate from the proved \(128\)-bound because it additionally uses the
complete exact order-at-most-\(81\) certificate.  A fixed-hash independent
audit reconstructed every computational dependency and every rank case.

[PROVED] The inputs already established elsewhere are:

1. every finite \(2\)-group \(P\) with \(\nu(P)=8\) satisfies
   \([P:Z(P)]\leq128\);
2. the exact cutoff-eight certificate has no binary example with center
   quotient of order at most \(64\);
3. among exact center quotients of order \(64\) at clique cutoff eight, the
   only surviving graph is the scalar nondegenerate symplectic graph on
   \(C_2^6\), and it has clique number seven.

The first input is the new reduction in
notes/two_group_inclusion_maximal_centralizers.md.  The other two are the
computer-assisted results in notes/h8_bounded_cutoff.md and Theorem H7.7 of
notes/exact_h7.md.

## Forcing the scalar order-\(64\) subgroup

### [PROVED] Boundary reduction

Assume for contradiction that \(P\) is a finite \(2\)-group with
\(\nu(P)=8\), and put \(Z=Z(P)\).  The proved and certified inputs force

\[
 [P:Z]=128.
\tag{SBA.1}
\]

Choose a maximum eight-clique, cover \(P\) by its eight centralizers, and
ascend each centralizer only inside the poset of proper element
centralizers.  The proof of the \(128\)-bound produces eight
inclusion-maximal element centralizers \(C_i\) which cover \(P\).  None is a
maximal subgroup of \(P\), since that case would give \([P:Z]\leq64\).
For each \(C_i\), the same proof supplies

\[
 C_i\mathrel{\triangleleft}K_i<P,\qquad
 [K_i:C_i]=2,\qquad Z(K_i)=Z,\qquad [C_i:Z]\leq32.
\tag{SBA.2}
\]

If every \([C_i:Z]\) were at most \(16\), then

\[
 [P:Z]\leq1+8(16-1)=121,
\]

which is impossible for (SBA.1).  Hence some pair \(C\triangleleft K\)
in (SBA.2) satisfies

\[
 [C:Z]=32,\qquad [K:Z]=64.
\tag{SBA.3}
\]

The order-\(64\) exact certificate applied to \(K/Z(K)\) now gives

\[
 V:=K/Z\cong\mathbf F_2^6,
\tag{SBA.4}
\]

and there is a nondegenerate alternating form
\(b:V\times V\to\mathbf F_2\) such that two \(Z\)-cosets commute in \(K\)
exactly when their \(b\)-value is zero.  Equivalently,

\[
 K'=\langle d\rangle\leq Z,\qquad |d|=2,\qquad
 [\widehat u,\widehat v]=d^{\,b(u,v)}.
\tag{SBA.5}
\]

Moreover \(\nu(K)=7\).  Equality in the local table of the \(128\)-bound
then forces

\[
 \nu(C)=5,\qquad [C:Z(C)]=16,\qquad [Z(C):Z]=2.
\tag{SBA.6}
\]

Indeed, the other ways to have \([C:Z]=32\) occur in the rows
\(r=4\) and \(r=6\), where the internal twist constructs respectively
\(4+4=8\) and \(6+2=8\) vertices in \(K\), contrary to \(\nu(K)=7\).
The row \(r=5\) gives (SBA.6).

Finally (SBA.1) and (SBA.3) give \([P:K]=2\), so \(K\triangleleft P\).
Choose \(t\in P\setminus K\).  Conjugation by \(t\) induces

\[
 \alpha\in\operatorname{Sp}(V,b).
\tag{SBA.7}
\]

It fixes the form, rather than merely its zero pattern, because \(t\)
centralizes \(Z=Z(P)\) pointwise.  Since \(t^2\in K\) and inner
automorphisms of \(K\) act trivially on \(K/Z(K)\), one has
\(\alpha^2=1\).  Put

\[
 N=\alpha-I,\qquad F=\ker N,\qquad R=\operatorname{im}N,\qquad
 s=\operatorname{rank}N.
\tag{SBA.8}
\]

In characteristic two, \(N^2=0\), so \(s\leq3\).  Symplecticity gives

\[
 F=R^\perp,\qquad R\leq F,
\tag{SBA.9}
\]

because for \(x\in F\),
\(b(x,Ny)=0\) follows by expanding
\(b(\alpha x,\alpha y)=b(x,y)\), and the two spaces in (SBA.9) have the
same dimension.

## A quotient commutation calculation

### [PROVED] Inner and outer joins

Write the abelian normal subgroup \(V=K/Z\) additively and write
\(\tau=tZ\).  For \(u,v,x\in V\), direct multiplication in \(P/Z\)
gives

\[
\begin{aligned}
 \tau u\text{ commutes with }\tau v
   &\quad\Longleftrightarrow\quad u+v\in F,\\
 x\text{ commutes with }\tau u
   &\quad\Longleftrightarrow\quad x\in F.
\end{aligned}
\tag{SBA.10}
\]

The possible nonsplit value of \(\tau^2\in V\) cancels from the first
comparison, so no semidirect-product splitting is assumed.

Consequently, one representative from every coset of \(F\) in \(V\)
gives an outer clique of size \(2^s\) in the quotient.  Every inner vertex
of \(V\setminus F\) is joined, already in the quotient, to every member of
that outer clique.  Noncommutation in \(P/Z\) implies noncommutation of
arbitrary lifts in \(P\).

We shall also use two explicit symplectic cliques.  Relative to a basis

\[
 e_1,e_2,e_3,f_1,f_2,f_3,\qquad
 b(e_i,f_j)=\delta_{ij},
\tag{SBA.11}
\]

the following six vectors are pairwise \(b\)-nonorthogonal:

\[
\begin{split}
 X_2=\{&
 e_1+f_1,\ e_3+f_1,\ e_1+f_2,\ e_1+e_2+f_2,\\
 &f_1+f_3,\ e_3+f_1+f_3\}.
\end{split}
\tag{SBA.12}
\]

They all lie outside \(\langle e_1,e_2\rangle^\perp\).  The following
second six-clique lies outside \(\langle e_1\rangle^\perp\):

\[
\begin{split}
 X_1=\{&
 e_1+f_1,\ e_2+f_1,\ e_2+f_1+f_2,\ e_3+f_1+f_2,\\
 &f_1+f_2+f_3,\ e_3+f_1+f_2+f_3\}.
\end{split}
\tag{SBA.13}
\]

Every pair in each displayed set has \(b\)-value one by direct expansion.
The symplectic group is transitive on totally isotropic subspaces of a
fixed dimension, so these coordinate witnesses apply to the spaces
\(R\) in (SBA.9).

## The four ranks

### [PROVED] Rank three gives nine quotient-visible vertices

If \(s=3\), (SBA.10) gives an outer eight-clique.  Choose any
\(x\in V\setminus F\).  It is joined in the quotient to all eight outer
vertices, giving a nine-clique in \(P\), a contradiction.

### [PROVED] Rank two gives ten quotient-visible vertices

If \(s=2\), choose the basis (SBA.11) with
\(R=\langle e_1,e_2\rangle\).  Then
\(F=R^\perp\), and \(X_2\) is a six-clique in \(V\setminus F\).
Equation (SBA.10) supplies an outer four-clique joined to all six inner
vertices.  Thus \(P\) contains a ten-clique, a contradiction.

### [PROVED] Rank one gives either a maximal centralizer or nine vertices

If \(s=1\), choose \(R=\langle e_1\rangle\), so
\(F=e_1^\perp\).  For \(f\in F\), define

\[
 \lambda(f)=[t,\widehat f]\in Z.
\tag{SBA.14}
\]

This is well-defined and additive: \(\alpha(f)=f\) puts the commutator in
\(Z\), changing a lift by an element of \(Z\) has no effect, and the
ordinary commutator identity becomes multiplicative because all the
values in question are central.  No class-two hypothesis on \(P\) is used
in this rank-one step.

If \(\lambda=0\), then \(t\) centralizes the full inverse image
\(\widehat F\) of \(F\) in \(K\).  The group

\[
 L=\langle t,\widehat F\rangle
\]

has \([L:Z]=64\): the two \(F\)-cosets are disjoint, and
\(t^2Z\in F\) because \(\alpha(t^2Z)=t^2Z\).  Hence \(L\) is an index-two subgroup of \(P\) contained in
\(C_P(t)\).  The automorphism \(\alpha\ne1\) makes \(t\) noncentral, so
\(C_P(t)<P\).  It follows that \(C_P(t)=L\) is a maximal subgroup.  The
proved maximal-centralizer branch would then give \([P:Z]\leq64\),
contrary to (SBA.1).

If \(\lambda\ne0\), choose \(f\in F\) with
\([t,\widehat f]\ne1\), and choose \(u\in V\setminus F\).  The three
outer elements

\[
 t,\qquad t\widehat f,\qquad t\widehat u
\tag{SBA.15}
\]

form a clique.  The first two fail to commute by (SBA.14), while the third
fails to commute with both already in \(P/Z\), because
\(u,u+f\notin F\).  The six inner vertices \(X_1\subseteq V\setminus F\)
are joined in the quotient to every vertex of (SBA.15).  This gives a
nine-clique in \(P\), again a contradiction.

### [PROVED] Rank zero gives nine vertices through the center layer

Suppose \(s=0\).  Then \(\alpha=1\), \(P/Z\) is abelian, and \(P\) has
class at most two.  Define

\[
 T:V\longrightarrow\Omega_1(Z),\qquad
 T(v)=[t,\widehat v].
\tag{SBA.16}
\]

The map is well-defined and \(\mathbf F_2\)-linear.  Its values have order
at most two because \(\widehat v^{\,2}\in Z\) and \(P\) has class two.

The image of \(T\) is not contained in \(D=\langle d\rangle\).  Otherwise
every commutator in \(P\) would lie in \(D\), giving a scalar alternating
pairing

\[
 (P/Z)\times(P/Z)\longrightarrow C_2
\]

with zero radical.  But bilinearity first puts \(2(P/Z)\) in the radical,
so zero radical would make \(P/Z\cong\mathbf F_2^7\); an alternating form
in odd dimension has nonzero radical.  This contradicts the definition of
the exact center quotient.

Choose a vector-space complement
\(\Omega_1(Z)=D\oplus E\).  The \(D\)-component of \(T\) is a scalar
linear functional on \(V\), hence has the form \(v\mapsto b(w,v)d\) for
some \(w\in V\).  Replacing \(t\) by \(t\widehat w\) eliminates that
component.  We may therefore assume

\[
 0\ne T(V)\leq E.
\tag{SBA.17}
\]

Choose a linear functional \(\varphi:E\to\mathbf F_2\) such that
\(\varphi T\ne0\), and put

\[
 F_0=\ker(\varphi T).
\tag{SBA.18}
\]

This is a hyperplane, hence \(F_0=a^\perp\) for a nonzero \(a\in V\).
After a symplectic change of basis, \(X_1\) from (SBA.13) is a six-clique
in \(V\setminus F_0\).

In additive notation on the elementary central subgroup \(D\oplus E\),
the class-two commutator identities give

\[
\begin{aligned}
 [\widehat x,t\widehat u]
   &=T(x)+b(x,u)d,\\
 [t\widehat u,t\widehat v]
   &=T(u+v)+b(u,v)d.
\end{aligned}
\tag{SBA.19}
\]

Here \([\widehat x,t]=[t,\widehat x]^{-1}=[t,\widehat x]\), since
\(T(x)\) has order at most two.

Thus every \(x\in X_1\) fails to commute with every outer
\(t\widehat u\), because the \(E\)-component \(T(x)\) has nonzero
\(\varphi\)-value.

The restriction of \(b\) to the five-dimensional hyperplane \(F_0\) has
rank four, so choose \(u_0,u_1\in F_0\) with \(b(u_0,u_1)=1\), and choose
\(v\notin F_0\).  Formula (SBA.19) shows that

\[
 t\widehat u_0,\qquad t\widehat u_1,\qquad t\widehat v
\tag{SBA.20}
\]

is an outer three-clique.  The first pair has nonzero \(D\)-component,
whereas each pair involving \(v\) has \(E\)-component whose
\(\varphi\)-value is one.  Joining (SBA.20) to the six vertices \(X_1\)
gives a nine-clique, the final contradiction.

## Conclusion and independent audit

### [PROVED] Finite binary closure

Every possible rank \(s=0,1,2,3\) leads either to a nine-clique in \(P\)
or to a maximal proper element centralizer, which the \(128\)-boundary
excludes.  Therefore

\[
 \text{there is no finite \(2\)-group \(P\) with }\nu(P)=8.
\tag{SBA.21}
\]

[PROVED] The independent fixed-hash audit checked all of the following:

1. verify that the order-\(64\) certificate really leaves only the scalar
   \(C_2^6\) graph at cutoff eight, not merely at cutoff seven;
2. reconstruct (SBA.10) without assuming that \(P/Z\) splits over \(K/Z\);
3. check all fifteen pairings in each of (SBA.12) and (SBA.13);
4. verify the lift-independence and additivity in (SBA.14) and (SBA.16);
5. check the nonsplit \(t^2Z\) issue in the rank-one maximal-centralizer
   case;
6. reconstruct both identities in (SBA.19), including commutator
   conventions;
7. check that exactness of \(Z(P)\) supplies precisely the radical
   contradiction used in rank zero.

The auditor independently recomputed all thirty displayed pairings,
reconstructed the nonsplit and commutator formulas, and reran the saved
cutoff-eight certificate successfully.  No exploratory SmallGroups scan is
used in this proof.
