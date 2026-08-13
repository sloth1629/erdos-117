# Two Elementary Exact Families

This note upgrades two patterns first seen in the exact computations to
theorems for every parameter.  The proofs use the central-coset graph from
`notes/foundations.md`.

## Dihedral groups

For \(q\geq 3\), write

\[
D_{2q}=\langle r,s\mid r^q=s^2=1,\ srs=r^{-1}\rangle .
\]

### Theorem EF.1 `[PROVED]`

\[
\nu(D_{2q})=a(D_{2q})=
\begin{cases}
q+1,&q\text{ odd},\\
q/2+1,&q\text{ even}.
\end{cases}
\]

**Proof.**  All rotations commute.  Direct multiplication gives

\[
r^k(sr^i)=(sr^i)r^k\quad\Longleftrightarrow\quad r^{2k}=1
\]

and

\[
(sr^i)(sr^j)=(sr^j)(sr^i)
\quad\Longleftrightarrow\quad r^{2(i-j)}=1.
\]

Suppose first that \(q\) is odd.  The \(q\) reflections are pairwise
noncommuting, and any nonidentity rotation fails to commute with all of them.
This gives a clique of size \(q+1\).  A clique contains at most one rotation
and at most all \(q\) reflections, so it has size at most \(q+1\).  The
rotation subgroup together with the \(q\) order-two reflection subgroups is
an abelian cover of size \(q+1\).  Since every abelian cover has size at least
the clique number, equality follows.

Now suppose that \(q\) is even.  The center is
\(Z=\{1,r^{q/2}\}\).  The reflections split into the \(q/2\) commuting
pairs

\[
\{sr^i,sr^{i+q/2}\}\qquad(0\leq i<q/2),
\]

and two reflections from different pairs do not commute.  Every noncentral
rotation fails to commute with every reflection.  Thus one noncentral
rotation together with one reflection from each pair is a clique of size
\(q/2+1\), and the same observations prove the matching upper bound.  The
rotation subgroup and the \(q/2\) abelian subgroups

\[
\langle Z,sr^i\rangle\qquad(0\leq i<q/2)
\]

cover the group, giving the matching cover bound. \(\square\)

### Corollary EF.2 `[PROVED]`

For every \(n\geq3\), there is a finite dihedral group \(G_n\) with

\[
\nu(G_n)=a(G_n)=n.
\]

Indeed, take \(G_n=D_{4(n-1)}\), which is the even-parameter case of the
theorem with \(q=2(n-1)\).  Consequently \(h(n)\geq n\) for every
\(n\geq3\).

## Heisenberg groups of order \(p^3\)

Let \(p\) be prime and let \(H_p=UT_3(\mathbb F_p)\).  Represent an element by
\((x,y,z)\in\mathbb F_p^3\), corresponding to the upper-unitriangular matrix
with entries \(x,y,z\) in positions \((1,2),(2,3),(1,3)\), respectively.

### Theorem EF.3 `[PROVED]`

For every prime \(p\),

\[
\nu(H_p)=a(H_p)=p+1.
\]

**Proof.**  Direct multiplication shows that the commutator of
\((x,y,z)\) and \((x',y',z')\) has central coordinate

\[
xy'-x'y.
\]

The center consists of the triples \((0,0,z)\), so the central quotient is
\(V=\mathbb F_p^2\).  Two cosets commute exactly when their vectors have
zero determinant.  In dimension two this is equivalent to linear
dependence.

The nonzero vectors of \(V\) split into the \(p+1\) one-dimensional
subspaces.  Vectors in one such line commute, while vectors in different
lines do not.  Therefore choosing one vector from every line gives a clique
of size \(p+1\), and no larger clique is possible.  Coloring each line with
one color gives a proper coloring with \(p+1\) colors; equivalently, the full
preimages of the lines are \(p+1\) abelian subgroups covering \(H_p\).
The clique lower bound makes this cover minimal. \(\square\)
