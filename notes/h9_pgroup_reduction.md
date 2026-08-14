# Finite \(p\)-groups at clique cutoff nine: an independent reduction

This note is an independent audit record for the finite \(p\)-group branch.
It does **not** claim to determine \(h(9)\).  Its endpoint is a bounded binary
residual.  The notation is that of `AGENTS.md`.

## [PROVED] The inclusion-maximal-centralizer charge

Let \(P\) be a finite \(p\)-group with \(\nu(P)=m\), and let
\(C=C_P(y)<P\) be inclusion-maximal among proper element centralizers.  Put
\(r=\nu(C)\).  If \(C\) is maximal, set \(K=P\).  Otherwise the normalizer
condition supplies

\[
 C\mathrel{\triangleleft}K<P,\qquad [K:C]=p.
\]

In either case

\[
 Z(K)=Z(P).
\tag{H9P.1}
\]

Indeed, an element of \(Z(K)\setminus Z(P)\) would have a proper element
centralizer containing \(K>C\), contrary to the choice of \(C\).  Put
\(A=Z(C)\), choose \(g\in K\setminus C\), and set

\[
 q=[A:Z(P)].
\]

The fixed subgroup of conjugation by \(g\) on \(A\) is
\(A\cap Z(K)=Z(P)\).  Hence, for a transversal \(a_1,\ldots,a_q\) of
\(Z(P)\) in \(A\), the elements \(ga_1,\ldots,ga_q\) are pairwise
noncommuting.  If \(c_1,\ldots,c_r\) is a maximum clique in \(C\), replace
\(c_j\) by \(c_jy\) exactly when \(c_j\) commutes with \(g\).  The resulting
\(r\)-clique is joined to all \(ga_i\), because \(y\in Z(C)\) and
\([y,g]\ne1\).  Consequently

\[
 \boxed{r+q\le m},\qquad q\ge p.
\tag{H9P.2}
\]

The two-step centralizer drop in `notes/candidate_bound.md` also gives
\(r\le m-2\).

## [PROVED] The elementary central-quotient endpoint

If a nonabelian finite \(p\)-group satisfies
\(|P/Z(P)|\le p^2\), then

\[
 P/Z(P)\cong C_p^2,
 \qquad \nu(P)=a(P)=p+1.
\tag{H9P.3}
\]

The quotient cannot be cyclic.  It is therefore \(C_p^2\), the group has
class at most two, and exactness of the center makes its commutator form a
nonzero alternating form on this two-dimensional space.  The \(p+1\)
projective lines are both a maximum nonorthogonal transversal and an
abelian-subgroup cover.

## Odd primes

The uses of Berkovich below refer to the primary-verified finite-only results
recorded in `notes/three_group_nu8.md` and `notes/five_group_nu8.md`: a
nonabelian finite \(p\)-group has clique number at least \(p+1\), equality
has the standard \(p+1\) structure, and odd \(p\)-groups do not have clique
number \(p+2\).

### [PROVED] The \(p=7\) branch

There is no finite \(7\)-group with clique number nine.  For \(m=9\), (H9P.2)
forces every inclusion-maximal proper element centralizer to be abelian:
a nonabelian one would have \(r\ge8\), while \(q\ge7\).  Thus each enlarged
centralizer has image of order at most seven over \(Z(P)\).  Nine such images
cover \(P/Z(P)\), so

\[
 |P/Z(P)|\le1+9(7-1)=55.
\]

The index is a power of seven, hence at most \(49\), and (H9P.3) would give
\(\nu(P)=8\), a contradiction.  Therefore the only nonabelian cutoff-nine
case is the equality branch \((\nu,a)=(8,8)\).

### [PROVED] The \(p=5\) branch

There is no finite \(5\)-group with clique number eight or nine.  In either
case a nonabelian inclusion-maximal centralizer would have \(r\ge6\), and
\(r+q\ge11\).  Thus all of them are abelian.  The same union count gives

\[
 |P/Z(P)|\le1+m(5-1)\le37,
\]

so the index is at most \(25\), and (H9P.3) gives clique number six.  The
primary-verified exclusion of \(p+2=7\) leaves only
\((\nu,a)=(1,1)\) and \((6,6)\).

### [PROVED] (computer-assisted) The \(p=3\) branch

First, clique number six is impossible without computation.  If \(m=6\),
then a nonabelian inclusion-maximal centralizer has \(r\ge4\), so
\(r+q\ge7\).  Hence all are abelian and

\[
 |P/Z(P)|\le1+6(3-1)=13.
\]

The index is at most nine, and (H9P.3) gives clique number four.

For \(m\in\{8,9\}\), an inclusion-maximal centralizer can only be abelian
or have \(r=4\).  In the latter case the equality structure gives
\([C:Z(C)]=9\), while (H9P.2) gives \([Z(C):Z(P)]=3\).  Thus
\([C:Z(P)]\le27\), including the abelian case.  If such a centralizer is
maximal then \([P:Z(P)]\le81\); otherwise the union bounds are

\[
 1+8(27-1)=209,\qquad 1+9(27-1)=235,
\]

whose largest ternary power is again \(81\).

[COMPUTED] The exhaustive exact-center inventory through order \(81\) then excludes
clique numbers eight and nine.  The relevant reproducible evidence is
`experiments/logs/h8_bounded_cutoff.json`, together with the delegated
\(C_3^4\) certificate `experiments/logs/h7_c3_4.json`; the ordinary order
\(27\) and \(81\) rows have clique numbers at least ten, except for the
already known lower-cutoff rows, and the \(C_3^4\) orbit list has no clique
number eight or nine.  This is a computer-assisted conclusion, not a
classification inferred from a blind SmallGroups scan.

Together with the odd-\(p\) exclusion of \(p+2=5\), the ternary possibilities
through cutoff nine are \(\nu\in\{1,4,7\}\), and the exact cutoff-seven
theorem gives \(a(P)\le10\), sharply attained by \(S(3,2)\).

### [PROVED] Primes at least eleven

For \(p\ge11\), Berkovich's lower bound \(\nu(P)\ge p+1\) shows that every
finite \(p\)-group at cutoff nine is abelian.

## The binary reduction

Assume from now on that \(P\) is a finite \(2\)-group with \(\nu(P)=9\),
and write \(Z=Z(P)\), \(Q=P/Z\).  Enlarge each of the nine original
maximum-clique centralizers to a labelled inclusion-maximal proper element
centralizer.  For one such centralizer, the proved exact lower-cutoff
center-index bounds and (H9P.2) give

\[
\begin{array}{c|c|c|c}
r&[C:Z(C)]&q=[Z(C):Z]&[C:Z]\\ \hline
1&1&\le8&\le8\\
3&\le4&\le4&\le16\\
4&\le8&\le4&\le32\\
5&\le16&\le4&\le64\\
6&\le16&\le2&\le32\\
7&\le64&\le2&\le128.
\end{array}
\tag{H9P.4}
\]

The \(r=6\) entry uses the exact binary cutoff-six certificate, not merely
the rounded general six-cover bound.  If one enlarged centralizer is maximal
in \(P\), (H9P.4) immediately gives \(|Q|\le256\).  Otherwise the nine
images, each of order at most \(128\), cover \(Q\), whence

\[
 |Q|\le1+9(128-1)=1144,
 \qquad |Q|\le1024.
\tag{H9P.5}
\]

### [PROVED] The order-256 scalar local boundary

The following local lemma is used only at the exact last row of (H9P.4).
Let \(C=C_K(y)\triangleleft K\), \([K:C]=2\), and \(Z(K)=Z\).  Suppose

\[
 [Z(C):Z]=2,
 \qquad C/Z(C)\cong C_2^6
\]

with the exact scalar nondegenerate symplectic commutation form.  If
\(\nu(K)\le9\), then

\[
 K/Z\cong C_2^8
\]

and its exact commutation form is scalar nondegenerate symplectic.
Consequently \((\nu(K),a(K))=(9,17)\).

Here is the proof skeleton, with every clique-producing branch explicit.
The kernel of the scalar functional on \(\bigwedge^2 C_2^6\) is spanned by
isotropic decomposable wedges, so \(C'=\langle d\rangle\cong C_2\); this
line is characteristic and lies in \(Z\).  For \(t\in K\setminus C\), let
\(\alpha\) be its involutory symplectic action on \(C/Z(C)\), put
\(F=\ker(\alpha-1)\), and \(s=\operatorname{rank}(\alpha-1)\le3\).
After symplectic normalization write
\(R=\operatorname{im}(\alpha-1)=\langle e_1,\ldots,e_s\rangle\), so
\(F=R^\perp\).  Representatives of \(V/F\), each doubled by the nontrivial element of
\(Z(C)/Z\), form an outer clique of size \(2^{s+1}\).  If \(s>0\), it is
joined to the following scalar six-clique outside \(F\), in symplectic
coordinates \((e_1,e_2,e_3,f_1,f_2,f_3)\):

\[
000100,\ 110100,\ 100110,\ 111110,\ 110111,\ 111111.
\]

This gives a ten-clique, so \(\alpha=1\).  The residual commutator map
\(\varphi:V\to Z(C)/Z\) must vanish, since otherwise two outer base points,
each doubled, give four vertices joined to a scalar six-clique outside
\(\ker\varphi\).  Thus \(K\) has class at most two.  Writing
\(a=Z(C)/Z\), \(e=[a,t]\), and \(L(u)=[t,u]\), any value
\(L(u)\notin\langle e\rangle\) gives the outer four-clique
\(\{t,ta,tu,tua\}\), again joinable to a scalar six-clique.  Hence
\(L(C/Z)\le\langle e\rangle\).  Its kernel is a scalar symplectic
six-space.  If \(e\ne d\), Cartesian sums of its seven-clique with
\(\{a,t,a+t\}\) give a \(21\)-clique.  Therefore \(e=d\), all commutators
lie on one line, and exactness makes \(2(K/Z)\) radical.  Thus \(K/Z\) is
elementary abelian of dimension eight and the scalar form is nondegenerate.

### [PROVED] A scalar order-256 subgroup cannot extend by index two

If \(K\triangleleft L\), \([L:K]=2\), \(Z(K)=Z(L)=Z\), and \(K/Z\) is
scalar symplectic \(C_2^8\), then \(\nu(L)\ge10\).  With notation
\(F=\ker(\alpha-1)\), outer representatives give \(2^s\) vertices.  For
\(s=4,3,2,1\), respectively, use: the outer \(16\)-clique; outer eight
plus \(f_1,e_1+f_1\); outer four plus a scalar six-clique; or outer two
plus the following scalar eight-clique outside \(F\):

\[
\begin{gathered}
00001000,\ 11001000,\ 10001100,\ 11101100,\\
11001110,\ 11111110,\ 11101111,\ 11111111.
\end{gathered}
\]

If \(s=0\), the cross-commutator map cannot take values only in the scalar
line: exactness would give a nondegenerate alternating scalar form in odd
dimension nine.  Modulo that line it gives a nonzero functional.  Three
outer vertices can be chosen pairwise noncommuting, two over its kernel and
one outside; transporting the displayed eight-clique into the complementary
affine hyperplane joins all eight to those three.  This gives eleven.

### [PROVED] Orders \(1024\) and \(512\) do not occur

If \(|Q|=1024\), the union count forces at least eight enlarged centralizer
images of order \(128\).  Each is the exact scalar local boundary above and
supplies \(K/Z\) of order \(256\).  Normalize \(K\) upward by index two.
Equal centers contradict scalar index-two rigidity.  If the new normalizer
has larger center, a noncentral element of that center has this normalizer
as its full proper centralizer by the order count; its clique number is at
least nine from \(K\), contradicting the two-step centralizer drop to seven.

Now suppose \(|Q|=512\).  An enlarged image of order \(128\) would give a
scalar order-256 subgroup of index two in \(P\), again impossible.  Thus all
nine labelled images \(A_i\) have order at most \(64\).  At least eight have
order \(64\).  If exactly eight do and the ninth has order \(s\le32\), put

\[
 E=\sum_x(m_x-1)=\sum_i|A_i|-512=s,
 \qquad
 S_2=\sum_x {m_x\choose2}=\sum_{i<j}|A_i\cap A_j|.
\]

The pointwise inequality \({m\choose2}\le\frac92(m-1)\) gives
\(S_2\le\frac92s\), whereas subgroup intersections give
\(S_2\ge28\cdot8+s=224+s\), a contradiction.  Hence all nine images have
order \(64\).  Now \(E=64\), while the same two inequalities force
\(S_2=288\).  Equality says every pair intersection is one common subgroup
\(D\) of order eight and every repeated point lies in all nine images:

\[
 Q=D\ \dot\cup\ \bigdotcup_{i=1}^9(A_i\setminus D).
\]

Let \(B_i=C_P(x_i)/Z\le A_i\) be the original labelled centralizers.  Every
point of \(A_i\setminus D\) is covered by some \(B_j\), and the displayed
partition forces \(j=i\).  Hence \(A_i=B_i\cup D\).  A group cannot be the
union of two proper subgroups, so \(A_i=B_i\) for all \(i\).  But the
intersection of the original maximum-clique centralizers is trivial in
\(Q\) by the two-step centralizer drop, contradicting \(|D|=8\).

Therefore

\[
 \boxed{|P/Z(P)|\le256.}
\tag{H9P.6}
\]

### [PROVED] The binary abelian-cover bound \(a(P)\le73\)

The private-cell recurrence in `notes/known_bounds.md` gives, for a chosen
private cell of the nine-clique,

\[
 P=A_j\cup\bigcup_{i\ne j}C_P(x_i),
\]

where \(A_j\) is abelian.  Each of the other eight centralizers is a finite
\(2\)-group with clique number at most seven.  The complete cutoff-seven
inventory in `notes/exact_h7.md` proves, by a computer-assisted proof, that every
such binary group has abelian cover number at most nine: the only extremal
binary row is the scalar \(C_2^6\) form with chromatic number nine.  Hence

\[
 \boxed{a(P)\le1+8\cdot9=73.}
\tag{H9P.7}
\]

### [PROVED] The all-maximal subcase and its exact form

[PROVED] If all nine original clique centralizers are maximal subgroups, their images
form a maximal irredundant core-free nine-cover of \(Q\).

[CITED-VERIFIED] Abdollahi--Ataei--
Mohammadi Hassanabadi, *Minimal blocking sets in \(PG(n,2)\) and covering
groups by subgroups*, arXiv:0708.2282v1, Theorem 1.6 (author manuscript
p. 2; HTML lines 81--83), classifies finite \(p\)-groups with this exact
hypothesis as

\[
 C_2^8,\qquad C_3^5,\qquad C_5^3.
\]

It is not being applied to a cover with nonmaximal members.  In the binary
case \(Q=C_2^8\).  The nine hyperplane normals form a nine-circuit.  Each
evaluation \(B(x_i,-)\) has one-dimensional image; pairwise noncommutation
forces all nine image lines to coincide.  The circuit spans \(Q^*\), and
zero radical then forces the \(x_i\) to span \(Q\), so the entire commutator
map is a single nondegenerate scalar symplectic form.  Thus this subcase has

\[
 (\nu(P),a(P))=(9,17).
\tag{H9P.8}
\]

## [PROVED] The order-\(256\) boundary has \(a(P)\le17\)

Assume \(|Q|=256\).  It is enough to derive a contradiction from
\(a(P)>17\).  No inclusion-maximal proper element centralizer can then be
maximal in \(P\): its image would have order \(128\), and the exact last row
of (H9P.4), followed by the scalar local boundary above, would make \(Q\)
scalar symplectic and give \(a(P)=17\).  Thus all nine labelled enlarged
images have order at most \(64\).

Suppose first that all nine labelled enlarged
images \(A_i\) had order at most \(32\).  At least eight would have order
\(32\): with at most seven, their union has size at most

\[
 1+7(32-1)+2(16-1)=248.
\]

If exactly eight have order \(32\), write \(s\in\{8,16\}\) for the order of
the ninth; smaller \(s\) cannot cover \(256\).  Put

\[
 E=\sum_x(m_x-1)=s,
 \qquad S_2=\sum_x{m_x\choose2}.
\]

The multiplicity inequality gives \(S_2\le\frac92s\).  The \(28\)
large-large intersections have order at least four and the eight
large-small intersections have total size at least \(s\), so

\[
 S_2\ge112+s>\frac92s
 \qquad(s=8,16),
\]

a contradiction.  Thus all nine would have order \(32\).  Now \(E=32\),
while the pair-intersection lower bound and the multiplicity upper bound
both equal \(144\).  Equality forces all pair intersections to be one common
subgroup \(D\) of order four and gives

\[
 Q=D\ \dot\cup\ \bigdotcup_i(A_i\setminus D).
\]

For the original labelled images \(B_i\le A_i\), the private-cell argument
used at order \(512\) gives \(A_i=B_i\cup D\), hence \(A_i=B_i\) for every
\(i\).  This contradicts \(\bigcap_iB_i=1\).  Therefore some enlarged image
has order \(64\).

There is also a complete one-large-image subcase.  Suppose, retaining the
original labels, that \(|A_1|=64\) and \(|A_j|\le32\) for \(j>1\).  The
complement of \(A_1\) has \(192\) points, while

\[
 |A_j\setminus A_1|
 \le |A_j|-\frac{|A_j||A_1|}{|Q|}
 \le24.
\]

The eight contributions must attain equality and be disjoint.  Thus every
\(|A_j|=32\), every \(|A_j\cap A_1|=8\), and the sets
\(A_j\setminus A_1\) partition \(Q\setminus A_1\).  Original-cover
membership forces \(A_j\setminus A_1\subseteq B_j\), so
\(A_j=B_j\cup(A_j\cap A_1)\), and the two-subgroup union lemma gives
\(B_j=A_j\).  Moreover \(A_j\setminus A_1\) lies in the \(j\)-th original
private cell and generates \(A_j\): if \(H<G\), fix \(g\notin H\) and write
every \(h\in H\) as \(g^{-1}(gh)\), with both \(g\) and \(gh\) outside
\(H\).  Hence these eight \(A_j\) are abelian.  Covering \(B_1\) by at most
nine abelian subgroups gives \(a(P)\le8+9=17\).

It follows that a hypothetical case with \(a(P)>17\) has at least two
labelled order-\(64\) enlarged images.

### [COMPUTED] The exact local order-\(64\) input

The complete cutoff-seven inventory removes the nominal

\[
 r=7,\qquad [C:Z(C)]=32,\qquad [Z(C):Z]=2
\]

route to an order-\(64\) image: no exact binary clique-seven row has center
quotient of order \(32\).  Hence every order-\(64\) inclusion-maximal
centralizer in the present branch has

\[
 \nu(C)=5,
 \qquad [C:Z(C)]=16,
 \qquad [Z(C):Z]=4.
\tag{H9P.9}
\]

This is the complete H7 certificate documented in notes/exact_h7.md, not a
blind SmallGroups scan.

The complete exterior-square certificate
experiments/logs/h5_exterior.json has \(225\) rows with quotient order
\(16\) and exact clique number five.  Filtering for exact center,
equivalently for radical consisting only of the identity quotient vertex,
leaves exactly \(84\) rows.  All have

\[
 C/Z(C)\cong C_2^4.
\]

They split into exactly two commutator geometries:

* \(28\) scalar rows, with \(C'\cong C_2\) and the nondegenerate scalar
  symplectic form on \(C_2^4\);
* \(56\) determinant rows, with \(C'\cong C_2^2\), whose five commuting
  two-spaces form a two-spread of \(C_2^4\).  Equivalently, every nonzero
  evaluation of the commutator map has rank two.

The dedicated verifier
src/verification/verify_h9_h5_local_dichotomy.py independently parses the
canonical JSON and TSV, checks the exact radical, quotient structure,
commutator-image order, degree profiles, and the five commuting triples in
every determinant row.  Its concise saved output is
experiments/logs/h9_h5_local_dichotomy.json, and
src/verification/test_h9_h5_local_dichotomy.py recomputes and compares the
whole certificate.  No file under tmp/ is a dependency.

### [PROVED] Local rigidity at (H9P.9)

Let \(C=C_P(y)\) have (H9P.9), put \(A=Z(C)\), and choose

\[
 C\mathrel{\triangleleft}K\mathrel{\triangleleft}P,
 \qquad [K:C]=[P:K]=2.
\]

For \(t\in K\setminus C\), inclusion-maximality gives

\[
 C_A(t)=Z.
\tag{H9P.10}
\]

Indeed, if \(a\in A\setminus Z\) commuted with \(t\), then
\(C<C_P(a)\); maximality among proper element centralizers would force
\(C_P(a)=P\), contrary to \(a\notin Z\).

Let \(R=C/A\cong C_2^4\), and let \(\alpha\) be the linear action of \(t\)
on \(R\).  Since \(t^2\in C\) and \(R\) is abelian, \(\alpha^2=1\).  In the
scalar case, suppose \(\alpha\) moved \(cA\).  The two layers \(tA\) and
\(tcA\) are fully joined four-cliques.  The exact centralizer of every
nonzero vector in a scalar symplectic four-space is nonabelian, so choose
noncommuting \(u,v\in C_C(c)\).  For either \(u\) or \(v\), and for either
outer layer, at most one of the four twists by \(A/Z\) commutes with that
whole layer; (H9P.10) supplies the one-coset assertion.  Avoiding the two
forbidden values gives twists of \(u,v\) which remain noncommuting and join
both outer four-cliques.  This is a ten-clique.  Hence \(\alpha=1\) in the
scalar case.

In the determinant case put \(F=\ker(\alpha-1)\) and
\(s=\operatorname{rank}(\alpha-1)\).  Outer layers indexed by \(R/F\),
each charged by the four elements of \(A/Z\), give a clique of size
\(4\cdot2^s\).  Thus \(s\le1\).  A nonidentity rank-one involution is a
transvection fixing a three-space \(F\) pointwise.  Each of the five spread
planes meets \(F\) nontrivially; its fixed intersection forces that plane
to be invariant.  At least four spread planes are transverse to \(F\).
Every invariant transverse plane would have to contain the common line
\(\operatorname{im}(\alpha-1)\), impossible for pairwise disjoint spread
planes.  Thus \(s=0\) here as well, and \(\alpha=1\).

Define

\[
 f:C\longrightarrow A,
 \qquad f(c)=c^{-1}c^t,
 \qquad E=f(A)=[A,t].
\]

Because \(t\) acts trivially on \(C/A\), \(f(c)\in A\); because \(A=Z(C)\),
\(f\) is a homomorphism.  Its restriction to \(A\) has kernel \(Z\), so
\(|E|=4\).  The induced map

\[
 \bar f:C/A\longrightarrow A/E
\]

vanishes.  Otherwise choose \(c\) with \(f(c)\notin E\).  The layers
\(tA\) and \(tcA\) are then fully joined four-cliques.  Given a noncommuting
pair in \(C\), twist each member independently by \(A/Z\); at most one
value makes it commute with the first outer layer and at most one with the
second.  The two surviving twists join the eight outer vertices and give a
ten-clique.  Therefore

\[
 f(C)\le E.
\tag{H9P.11}
\]

Put \(D_t=C_C(t)=\ker f\).  Surjectivity of \(f|_A:A\to E\) and (H9P.11)
give

\[
 D_tA=C,\qquad D_t\cap A=Z,\qquad Z(D_t)=Z.
\]

The map \(D_t/Z\to C/A\) preserves the exact commutation graph.  Also
\(C'=D_t'\le Z\).  In fact \(C'\le E\): otherwise choose a commutator value
outside \(E\), realized by a noncommuting pair in \(D_t\), and multiply
that pair by the five-clique in \(\langle A,t\rangle\) consisting of the
four charged outer representatives and one element of \(A\setminus Z\).
The two coordinate labels cannot cancel, giving a ten-clique.

In the determinant case \(|C'|=|E|=4\), so \(C'=E\le Z\).  In the scalar
case \(|C'|=2\).  If \(E\cong C_2^2\), conjugation by \(t\), which inverts
\(E\), fixes it pointwise, so \(E\le C_A(t)=Z\).  The only other possibility
is \(E\cong C_4\), with \(C'\) its subgroup of order two.  A scalar
five-clique in \(D_t\), multiplied by two elements of
\(\langle A,t\rangle\) whose commutator generates \(E\), is then a
ten-clique: the three possible labels are \(e^2,e,e^3\), all nontrivial.
Thus the cyclic case is impossible.  We have proved in both geometries that

\[
 [K,K]\le Z;
\]

in particular, the intermediate group \(K\) has class at most two.

### [PROVED] The transversal count and a second exact centralizer

Fix \(p\in P\setminus K\).  The same inclusion-maximality argument gives

\[
 C_A(p)=Z.
\tag{H9P.12}
\]

For every \(h\in K\setminus C\), exactly one \(Z\)-coset in \(hA\)
centralizes \(p\).  There is at most one: two such elements have quotient in
\(C_A(p)=Z\).  To prove existence, suppose no element of \(hA\) centralizes
\(p\).  Let \(T\) be a transversal of \(Z\) in \(A\), so \(hT\) is a
four-clique, and let \(Y\) be a five-clique in \(C\).  For each \(y\in Y\),
twist \(y\) independently by one of the four classes in \(A/Z\).
Commutation with \(p\) forbids at most one class by (H9P.12).  Commutation
with \(hT\) is independent of the member of \(T\), and forbids at most one
class by \(C_A(h)=Z\).  At least two choices remain.  The five twists still
form a clique because \(A=Z(C)\), and they join both \(p\) and the four
vertices \(hT\), producing a ten-clique.  This proves existence.

There are \([C:A]=16\) cosets \(hA\) in \(K\setminus C\).  Therefore

\[
 |C_K(p)\cap(K\setminus C)|=16|Z|=|C|/4.
\]

Put

\[
 H=C_P(p),\qquad D=C\cap H=C_C(p).
\]

The subgroup \(C_K(p)\) crosses \(C\), so its inside and outside parts have
equal size.  It follows that

\[
 |D|=|C|/4,\qquad |C_K(p)|=|C|/2.
\]

Since \(H\) crosses \(K\), this doubles once more:

\[
 |H|=|C|,\qquad |H/Z|=64.
\tag{H9P.13}
\]

Every inclusion-maximal centralizer has image of order at most \(64\) in
the present \(a(P)>17\) branch.  Hence an inclusion-maximal enlargement of
\(H\) equals \(H\) itself, and the exact local input (H9P.9) applies to
\(H\).  Put \(B=Z(H)\).  Then

\[
 [B:Z]=4,\qquad [H:B]=16.
\]

Moreover

\[
 D\cap A=Z,\qquad DA=C,\qquad Z(D)=Z.
\tag{H9P.14}
\]

Here the first equality is (H9P.12), the second follows from orders, and an
element of \(Z(D)\) centralizes both \(D\) and \(A\), hence \(C=DA\), so it
lies in \(A\cap D=Z\).  The bijection \(D/Z\to C/A\) preserves commutators,
so \(D/Z\) has one of the two exact five-clique geometries above.

Because \(B\) centralizes \(D\), (H9P.14) gives \(D\cap B=Z\); the order
calculation then gives \(DB=H\).  Also

\[
 |CH|=\frac{|C||H|}{|D|}=|P|,
\]

so \(P=CH\).  The decompositions \(C=DA\), \(H=DB\) show that \(D\) is
normal in both \(C\) and \(H\), hence in \(P\).  With

\[
 S=\langle A,B\rangle
\]

we finally obtain the exact central product

\[
 P=DS,\qquad [D,S]=1,\qquad D\cap S=Z,\qquad Z(S)=Z,\qquad |S/Z|=16.
\tag{H9P.15}
\]

Indeed, \(A\) and \(B\) centralize \(D\); an element of \(D\cap S\) lies in
\(Z(D)=Z\), while an element of \(Z(S)\) centralizes both factors in
\(P=DS\) and therefore lies in \(Z(P)=Z\).

### [PROVED] The central product is scalar

Write \(U=D'\le Z\).  If two elements \(s,t\in S\) had a noncentral
commutator, a five-clique \(X\subset D\) would make

\[
 X\{s,t\}=\{xs,xt:x\in X\}
\]

a ten-clique.  Its ten displayed products are distinct: an equality between
two of them puts both coordinate quotients in \(D\cap S=Z\), whereas a
noncommuting clique in \(D\) and a noncommuting pair in \(S\) have distinct
central cosets.  A central \(D\)-commutator cannot cancel a noncentral
\(S\)-commutator.  The same grid is a ten-clique if
\([s,t]\in Z\setminus U\), because every \(D\)-commutator lies in \(U\).
Consequently

\[
 1\ne S'\le U\le Z.
\tag{H9P.16}
\]

The first inequality uses \(Z(S)=Z<S\).

Suppose that \(D\) had the determinant geometry.  Then
\(U\cong C_2^2\), and every nonzero evaluation
\(D/Z\to U\) of its alternating commutator form is onto.  Choose
\(s,t\in S\) with \(0\ne e=[s,t]\in U\), and choose a nonzero functional
\(\lambda:U\to C_2\) with \(\ker\lambda=\langle e\rangle\).  The scalar
form obtained by composing the determinant form with \(\lambda\) is
nondegenerate: otherwise a nonzero evaluation would have image in
\(\ker\lambda\), contradicting surjectivity.  A scalar symplectic
four-space has a five-clique \(X\) on which every pair value under
\(\lambda\) is nonzero.  Thus no actual \(D\)-commutator between two
members of \(X\) is \(0\) or \(e\).  The grid \(X\{s,t\}\) is again a
ten-clique, a contradiction.

Therefore \(D\) has the scalar geometry and \(U\cong C_2\).  Equation
(H9P.16) now gives \(S'=U\).  Since \(S\) has class at most two and
\(S'\) has exponent two,

\[
 [s^2,r]=[s,r]^2=1
\]

for all \(r,s\in S\).  Exactness of the center gives \(s^2\in Z\), so
\(S/Z\cong C_2^4\).  Its scalar alternating form has zero radical and is
therefore nondegenerate.  The two commuting factors in (H9P.15) give the
orthogonal direct sum

\[
 P/Z\cong (D/Z)\perp(S/Z)\cong C_2^8
\]

with its nondegenerate scalar symplectic form.  The standard scalar formula
now gives

\[
 \boxed{a(P)=17}.
\tag{H9P.17}
\]

This contradicts the standing assumption \(a(P)>17\) and closes every
order-\(256\) configuration.

## [UNVERIFIED] Exact remaining binary residual

Combining (H9P.6) with the order-\(256\) closure, any binary cutoff-nine
group not yet proved to satisfy \(a(P)\le17\) has

\[
 \boxed{|P/Z(P)|\le128.}
\tag{H9P.18}
\]

The general proved bound (H9P.7) still gives \(a(P)\le73\).  A complete
exact-kernel computation or a new structural argument is still required at
center-quotient orders at most \(128\); in particular, the elementary
quotient \(C_2^7\) has an exterior square of dimension \(21\) and is not
covered by the current bounded enumeration.  No claim that every such group
has \(a(P)\le17\) is made here.
