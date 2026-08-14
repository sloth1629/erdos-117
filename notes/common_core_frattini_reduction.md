# The common core reduces to a binary Frattini kernel

## [PROVED] Scope and conclusion

Let \(G\) be finite with

\[
\nu(G)=8,
\qquad Q=G/Z(G)
\]

and suppose that \(Q\) is solvable and nonnilpotent. Start with the eight
exact clique-centralizer images

\[
H_i=C_G(x_i)/Z(G)
\]

and perform any maximalization and irredundant-minimalization from
notes/h8_nonnilpotent_reduction.md. Thus

\[
Q=M_1\cup\cdots\cup M_k,\quad D=\bigcap_iM_i,\quad
R=\operatorname {core}_Q(D),\quad L=Q/R.
\tag{CF.1}
\]

This note proves the following sharper residual.

\[
\boxed{
\begin{gathered}
 a(G)>10\ \Longrightarrow\ P:=\Phi(Q)\ne1,\\
 P\text{ is a }2\text{-group},\\
 Q/P\cong C_2^a\times C_3^b\times S_3\quad(a,b\ge0),\\
 \text{every minimal }Q\text{-normal subgroup contained in }P
 \text{ is central of order }2.
\end{gathered}}
\tag{CF.2}
\]

Moreover \(P\le R\) for every choice in (CF.1). Hence every common-core
quotient \(L\) is a quotient of the single canonical skeleton in (CF.2).
If \(L\) is nonabelian, then

\[
L\cong C_2^{a'}\times C_3^{b'}\times S_3
\tag{CF.3}
\]

for some \(a'\le a,b'\le b\). If \(L\) is abelian, it is an elementary
abelian \(2\)- or \(3\)-group. The ternary case is \(C_3^d\) with
\(2\le d\le7\); in the binary case the exact possibilities are

\[
L\cong C_2^2,\ C_2^4,\ \text{or }C_2^6.
\tag{CF.4}
\]

Thus the seven affine skeletons and an arbitrary solvable common core are no
longer the residual. The only remaining nonnilpotent obstruction is a
binary Frattini extension of an elementary central factor times \(S_3\),
still subject to the eight exact fixed-subgroup intersections. No
commutator pairing is asserted to descend through \(Q\to Q/P\) or
\(Q\to Q/R\).

## [PROVED] The maximalization quantifier is exhaustive

Every \(H_i\) is proper because \(x_i\) is noncentral. Since \(Q\) is
finite, it is contained in a maximal subgroup. Choosing one maximal
overgroup for each of the eight \(H_i\)'s preserves the cover, and deleting
duplicates and then redundant members terminates with (CF.1). The
core-free closure in notes/h8_nonnilpotent_reduction.md applies to every
such choice:

\[
R=1\quad\Longrightarrow\quad a(G)\le10.
\tag{CF.5}
\]

Consequently a hypothetical \(a(G)>10\) forces \(R\ne1\) for **every**
choice of maximal overgroups and every resulting minimal maximal subcover,
not merely for one preferred maximalization.

## [PROVED] A complement-free affine chief-factor lemma

Let \(K\) be a finite solvable group with \(\nu(K)\le8\), and let
\(V\triangleleft K\) be a noncentral minimal normal subgroup. Then \(V\) is
elementary abelian and

\[
(V,K/C_K(V))\in
\left\{
\begin{array}{c}
(C_3,C_2),\ (C_2^2,C_3),\ (C_5,C_2),\ (C_5,C_4),\\
(C_7,C_2),\ (C_7,C_3),\ (C_7,C_6)
\end{array}
\right\}.
\tag{CF.6}
\]

In particular, \(|V|\le7\) and the faithful irreducible action group
\(A=K/C_K(V)\) is cyclic. This conclusion does not assume that \(V\) is
complemented.

To prove it, recall the abelian-normal fiber construction. If \(g\in K\)
acts on the abelian normal group \(V\), the coset \(gV\) contains a clique
of size

\[
[V:C_V(g)].
\tag{CF.7}
\]

If \(u\in V\) is moved by \(g\), it is noncommuting with every member of
that fiber clique. If \(g_1V,\ldots,g_tV\) are pairwise noncommuting in
\(K/V\), their fiber cliques are completely joined. These statements are
proved directly in (NR.13)--(NR.14) of the preceding note.

Suppose \(A\) were nonabelian, and choose noncommuting \(a,b\in A\) with
lifts \(g,h\in K\). Since \(V\le C_K(V)\), noncommutation of the actions
implies that \(gV,hV\) do not commute. Hence \(gV,hV,ghV\) are pairwise
noncommuting. If \(V\) is an \(\mathbf F_p\)-space, (CF.7) gives

\[
p^{r(a)}+p^{r(b)}+p^{r(ab)}\le8,\qquad
r(c)=\operatorname {codim}C_V(c).
\tag{CF.8}
\]

Thus \(p=2\) and every displayed rank is one or two. If one rank were two,
the three fixed subspaces could not cover \(V\). Here is a direct count.
The union of any two distinct proper subspaces has size at most
\(3|V|/4\), with equality only for two hyperplanes; hence its complement
has size at least \(|V|/4\). The third fixed subspace, having codimension
at least two, has size at most \(|V|/4\), but contains zero whereas that
complement does not. It therefore cannot contain the whole complement.
(If the first two subspaces coincide, their union is even smaller.) Choose
\(u\) outside the union of all three fixed subspaces.
It is moved by all three actions, so adjoining \(u\) to the three
completely joined fiber cliques gives at least

\[
4+2+2+1=9
\]

vertices, a contradiction. Therefore \(a,b,ab\) all have rank one.

Every invertible rank-one perturbation of the identity over \(\mathbf F_2\)
is an involution. Explicitly, write \(c-I=v\otimes\lambda\). The matrix
determinant lemma and invertibility give \(\lambda(v)=0\); hence
\((c-I)^2=0\) and \(c^2=I\). Thus \(a,b,ab\) are involutions. But
\((ab)^2=1\) for involutions \(a,b\) implies \(ab=ba\), the final
contradiction. Hence \(A\) is abelian.

A finite abelian irreducible linear group is cyclic: the image of its
commutative group algebra on the irreducible module is a finite field, and
the group embeds in the cyclic multiplicative group of that field. A
generator \(a\) of \(A\) has no nonzero fixed vector, since its fixed space
is \(A\)-invariant and the action is faithful and nontrivial. The fiber
clique together with one moved vector now gives

\[
|V|+1\le8.
\tag{CF.9}
\]

The nontrivial cyclic irreducible subgroups of the automorphism groups of
\(C_3,C_2^2,C_5,C_7\) are exactly those in (CF.6).

## [PROVED] There is at most one noncentral minimal normal subgroup

Let \(U,V\) be distinct minimal normal subgroups of a finite solvable group
\(K\) with \(\nu(K)\le8\). They commute and intersect trivially. If both
were noncentral, choose an element moving \(U\). Every nontrivial action in
(CF.6) is fixed-point-free, so the movement index on \(U\) is
\(|U|\ge3\). If the same element moves \(V\), the fiber clique in the
abelian normal subgroup \(U\times V\) has size at least \(3\cdot3=9\).
Otherwise choose an element moving \(V\). If that second element also moves
\(U\), the same contradiction applies. If it centralizes \(U\), the product
of the two chosen elements moves both factors. Therefore

\[
\boxed{\text{at most one minimal normal subgroup of }K\text{ is noncentral}.}
\tag{CF.10}
\]

## [PROVED] Chief actions and the Fitting quotient

Apply (CF.6) to every noncentral chief factor of \(Q\): a chief factor is a
minimal normal subgroup in a quotient of \(Q\), and clique number cannot
increase in a quotient. Every nontrivial chief action is therefore cyclic
of order \(2,3,4\), or \(6\).

Choose a chief series \(1=Q_0<Q_1<\cdots<Q_m=Q\) and let

\[
K_0=\bigcap_{j=1}^m C_Q(Q_j/Q_{j-1}).
\]

This subgroup is nilpotent. Indeed, it is normal, and

\[
[K_0,K_0\cap Q_j]\le K_0\cap Q_{j-1}
\]

makes the intersections \(K_0\cap Q_j\) a central series. Hence
\(K_0\le F(Q)\). Conjugation on all chief factors embeds \(Q/K_0\) in a
direct product of the cyclic action groups just listed. It follows that

\[
Q/F(Q)\text{ is abelian of exponent dividing }12,\qquad Q'\le F(Q).
\tag{CF.11}
\]

There are no prime divisors of \(Q\) outside \(\{2,3,5,7\}\). To see this
for a prime \(p\mid |F(Q)|\), take the normal Sylow \(p\)-subgroup of the
nilpotent group \(F(Q)\), and then a minimal \(Q\)-normal subgroup \(U\) in
its nontrivial elementary abelian central layer. If \(U\) is noncentral,
(CF.6) gives \(p\in\{2,3,5,7\}\). If it is central, minimality gives
\(U\cong C_p\), and the exact prime-order central-fiber lemma gives
\(p+2\le8\), hence \(p\in\{2,3,5\}\). The remaining quotient \(Q/F(Q)\)
has only the primes two and three by (CF.11). Thus

\[
\pi(Q)\subseteq\{2,3,5,7\}.
\tag{CF.12}
\]

The central minimal normal subgroups of \(Q\) together form

\[
\Omega_1(Z(Q)_2)\times\Omega_1(Z(Q)_3)\times\Omega_1(Z(Q)_5).
\]

The exact-center rank bounds in notes/structural_reductions.md give rank at
most two at each prime, and (CF.10) allows at most one further, noncentral
minimal normal subgroup, necessarily one from (CF.6). This is a complete
description of the first normal layer of \(Q\).

## [PROVED] The canonical Frattini skeleton

Put \(P=\Phi(Q)\). The Frattini subgroup is nilpotent. Here is the short
finite-group proof. If \(S\) is a Sylow subgroup of \(P\), the Frattini
argument gives

\[
Q=P N_Q(S).
\]

If \(N_Q(S)<Q\), put it in a maximal subgroup \(M\). Since \(P\le M\), the
display would give \(Q\le M\), a contradiction. Thus every Sylow subgroup
of \(P\) is normal, and \(P\) is nilpotent.

The quotient \(\overline Q=Q/P\) has trivial Frattini subgroup. It is
nonnilpotent. Indeed, if \(Q/P\) were nilpotent, every one of its maximal
subgroups would be normal. Every maximal subgroup of \(Q\) contains \(P\),
so every maximal subgroup of \(Q\) would then be normal. A finite group all
of whose maximal subgroups are normal is nilpotent: if a Sylow subgroup
\(S\) were not normal, put its proper normalizer in a maximal subgroup
\(M\). Then \(S\le M\), and the Frattini argument for the normal subgroup
\(M\) gives \(Q=M N_Q(S)=M\), a contradiction. Thus \(Q\) would be
nilpotent, contrary to the hypothesis.

The Frattini-free Fitting argument already proved in (NR.11)--(NR.18), with
(CF.6) replacing the private-coset size bound, now gives

\[
\overline Q=C\times H,
\tag{CF.13}
\]

where \(C\) is central and is a direct product of elementary abelian
\(2\)-, \(3\)-, \(5\)-, and \(7\)-groups, while \(H\) is one of the seven
groups in (CF.6). Indeed \(F(\overline Q)=\operatorname {Soc}(\overline Q)\)
is abelian and self-centralizing; (CF.10) leaves at most one noncentral
minimal factor, and all central minimal factors split directly.

If \(P=1\), then \(\overline Q=Q\), so the exact commutator pairing is
available on (CF.13). The rank-free pairing calculation
(NR.21)--(NR.27) leaves exactly the seven affine groups and
\(C_2\times S_3\), all of order at most \(42\); the certified bounded scan
then gives \(a(G)\le10\). Therefore

\[
a(G)>10\quad\Longrightarrow\quad \Phi(Q)=P\ne1.
\tag{CF.14}
\]

This improves the choice-dependent conclusion \(R\ne1\) to a canonical
nontrivial characteristic subgroup.

## [PROVED] A minimal normal subgroup inside the Frattini kernel is central

Let \(1\ne U\le P\) be minimal normal in \(Q\). Since \(P\) is nilpotent,
\(U\) lies in one Sylow subgroup of \(P\). A nontrivial normal subgroup of
a finite \(p\)-group meets its center nontrivially. The intersection
\(U\cap Z(P)\) is \(Q\)-normal because \(P\) is characteristic in \(Q\).
Minimality therefore gives

\[
U\le Z(P).
\tag{CF.15}
\]

In particular \(P\le C_Q(U)\), so the action of \(Q\) on \(U\) factors
through the canonical quotient (CF.13).

Suppose \(U\) were noncentral. By (CF.6), its action group \(A\) is cyclic,
every nonidentity action is fixed-point-free, and \(|U|\ge3\). The action
map

\[
C\times H\longrightarrow A
\]

is nontrivial and factors through \(C\times H_{\rm ab}\). Write \(H=V:B\).

If the action is nontrivial on \(C\), take the standard
\((|V|+1)\)-clique in \(H\). Multiplying each member by either \(1\) or a
fixed suitable element of \(C\), independently, makes its action on \(U\)
nontrivial without changing any quotient noncommutation. Replacing each
member by its \(U\)-fiber clique gives

\[
\nu(Q)\ge |U|(|V|+1)\ge3\cdot4=12.
\]

If the action is trivial on \(C\), it is nontrivial on the cyclic complement
\(B=H_{\rm ab}\). Choose \(b\in B\) acting nontrivially on \(U\). The
\(|V|\) elements \(vb\) are pairwise noncommuting in \(H\), and every lift
acts fixed-point-freely on \(U\). Their completely joined \(U\)-fiber
cliques have total size

\[
|U||V|\ge3\cdot3=9.
\]

Both alternatives contradict \(\nu(Q)\le8\). Hence every minimal normal
subgroup of \(Q\) contained in \(P\) is central in \(Q\).

## [PROVED] A central minimal layer forces the \(S_3\) skeleton

Let \(U=\langle u\rangle\cong C_p\) be a central minimal normal subgroup of
\(Q\). Exactness of \(Q=G/Z(G)\) gives the nonzero homomorphism

\[
\varphi_u:Q\longrightarrow Z(G),\qquad
\varphi_u(q)=[\widetilde u,\widetilde q].
\tag{CF.16}
\]

Whenever \(\varphi_u(q)\ne1\), chosen lifts in \(G\) of the \(p\) elements
of the \(Uq\)-fiber form a \(p\)-clique in the exact central-coset graph of
\(G\). (They do not form a clique in \(\Gamma_Q\), where \(U\le Z(Q)\).)
Cross-fiber edges below come from noncommutation already visible in
\(Q/P\), so arbitrary lifts retain them. Use (CF.13), again writing
\(H=V:B\).

If \(\varphi_u(P)\ne1\), then every prescribed element of
\(\overline Q\) has a lift on which \(\varphi_u\) is nonzero: for a fixed
\(f\in P\) with nonzero value, at least one of \(q,qf\) works. Apply this
independently to a \((|V|+1)\)-clique in \(H\). The resulting completely
joined fibers give

\[
p(|V|+1)\le8.
\tag{CF.17}
\]

If \(\varphi_u(P)=1\), the map descends to \(C\times H\). If its restriction
to \(C\) is nonzero, multiplying each member of the same clique by either
\(1\) or a fixed central element again gives (CF.17). In both cases
\(p\ge2\) and \(|V|\ge3\), so equality can occur only for

\[
p=2,\qquad H=S_3\quad(|V|=3).
\tag{CF.18}
\]

It remains that the descended map vanishes on \(C\) and is nonzero on
\(H_{\rm ab}=B\). Then \(p\mid |B|\). Choose \(b\in B\) with nonzero
value. The \(|V|\) elements \(vb\) give

\[
p|V|\le8.
\tag{CF.19}
\]

For \(p=3\), the only complements with three-torsion occur with
\(|V|=4\) or \(7\), contradicting (CF.19). No listed complement has
five-torsion. For \(p=2\), the even complements with \(|V|=5\) or \(7\)
also contradict (CF.19), leaving only \(S_3=C_3:C_2\). Therefore every
central minimal normal subgroup forces exactly (CF.18).

Combining this with the preceding section, every minimal \(Q\)-normal
subgroup in the nontrivial nilpotent group \(P\) is central of order two.
If \(P\) had a nontrivial odd Sylow subgroup, that characteristic Sylow
subgroup would contain a minimal \(Q\)-normal subgroup of odd order. Hence

\[
P=\Phi(Q)\text{ is a nontrivial }2\text{-group},\qquad H=S_3.
\tag{CF.20}
\]

Finally the \(5\)- and \(7\)-components of \(C\) in (CF.13) vanish. By
(CF.11), \(Q/F(Q)\) has no \(r\)-part for \(r=5,7\). The unique Sylow
\(r\)-subgroup of the nilpotent group \(F(Q)\) is therefore also a Sylow
\(r\)-subgroup \(S\) of \(Q\); it is characteristic in \(F(Q)\) and normal
in \(Q\). Since \(P\) is a \(2\)-group, \(S\) maps injectively onto the
central \(r\)-component of \(Q/P\). Hence

\[
[Q,S]\le S\cap P=1,
\]

so \(S\le Z(Q)\). A central minimal subgroup of \(S\) contradicts
(CF.18). Thus (CF.13) sharpens to

\[
Q/P\cong C_2^a\times C_3^b\times S_3,
\tag{CF.21}
\]

which proves (CF.2).

Writing \(|P|=2^s\), the global factorial center-index bound makes the
remaining order inventory explicit:

\[
s\ge1,\qquad
|Q|=2^{s+a+1}3^{b+1}\le 8!=40\,320.
\tag{CF.21a}
\]

In particular \(b\le7\), and for each \(b\) only the finitely many pairs
\((s,a)\) satisfying (CF.21a) remain.

## [PROVED] The abelian common-core quotient and its binary cases

Return to (CF.1) and suppose \(L=Q/R\) is abelian. Since the intersection
of the irredundant maximal cover of \(L\) has trivial core and every subgroup
of an abelian group is normal, its intersection is \(1\). Also
\(\Phi(L)=1\).

Write \(L\) as the product of its elementary abelian Sylow subgroups. A
maximal subgroup of index \(p\) is a hyperplane in the \(p\)-Sylow subgroup
and contains every other Sylow subgroup. Partition the covering maximals
according to this prime. If no prime-family covered its Sylow subgroup,
choose in each Sylow subgroup a point missed by its family; their product
would be missed by the whole cover. Thus one prime-family already covers
\(L\). Irredundancy removes all other families, and the trivial total
intersection removes all other Sylow subgroups. Therefore

\[
L\cong C_p^d
\tag{CF.22}
\]

for one prime \(p\). Since \(L\) is a quotient of (CF.21),
\(p\in\{2,3\}\).

If \(p=3\), then the \(S_3\)-factor has no nontrivial \(3\)-group quotient,
so \(L\) is a quotient of \(C_3^b\). A one-dimensional vector space cannot
be covered by proper subspaces, while (CF.21a) gives \(b\le7\). Hence the
ternary alternatives are

\[
L\cong C_3^d,\qquad 2\le d\le7.
\]

For \(p=2\), let the \(k\le8\) covering hyperplanes be
\(\ker f_1,\ldots,\ker f_k\), and consider the injective evaluation map

\[
T:L\longrightarrow\mathbf F_2^k,\qquad
v\longmapsto(f_1(v),\ldots,f_k(v)).
\]

The cover says that the all-one vector \({\bf1}\) is not in \(W=T(L)\).
Irredundancy supplies, for every \(i\), a private point of the \(i\)-th
hyperplane, so

\[
{\bf1}+e_i\in W\qquad(1\le i\le k).
\tag{CF.23}
\]

If \(k\) is even, the vectors in (CF.23) span all of \(\mathbf F_2^k\), a
contradiction. If \(k\) is odd, they span the even-weight hyperplane.
Since this is a maximal proper subspace and \(W\) cannot contain
\({\bf1}\), it follows that \(W\) is exactly that hyperplane. Hence

\[
3\le k\le8,\qquad k\in\{3,5,7\},\qquad
d=\dim W=k-1\in\{2,4,6\},
\]

proving (CF.4).

## [PROVED] Nonabelian quotients of the canonical skeleton

Let \(A=C_2^a\times C_3^b\). Every nonabelian quotient of
\(A\times S_3\) is \(A'\times S_3\) for a quotient \(A'\) of \(A\).
Indeed, if \(N\triangleleft A\times S_3\) has nonabelian quotient, then
\(N\cap S_3=1\); otherwise it contains \(A_3\) and kills the derived
subgroup. Put \(A_0=N\cap A\) and work modulo \(A_0\). The projection of
\(N/A_0\) to \(S_3\) is normal and \(N/A_0\) is the graph of a homomorphism
from that projection to \(A/A_0\). Its kernel is \(N\cap S_3=1\), so this
homomorphism is injective. The projection cannot be all of \(S_3\), because
that would embed \(S_3\) in an abelian group. It cannot be \(A_3\):
normality of the graph
under a transposition would force the image of a generator to equal the
image of its inverse, impossible for an injective order-three image. Thus
the projection is trivial and \(N=A_0\le A\), proving (CF.3).

Since \(P\le M_i\) for every maximal subgroup and \(P\triangleleft Q\), one
has \(P\le D\) and therefore \(P\le R\) in every construction (CF.1).
Combining (CF.21), (CF.22)--(CF.23), and the preceding quotient argument
gives the asserted complete description of the common-core skeleton.

## [UNVERIFIED] Exact remaining task

The result does not yet prove \(a(G)\le10\) in (CF.2). The remaining data
are now canonical and considerably narrower:

\[
\begin{gathered}
1\ne P=\Phi(Q)\text{ is a }2\text{-group},\\
Q/P=C_2^a\times C_3^b\times S_3,\\
P=\bigcup_{i=1}^8(P\cap H_i),\qquad
\bigcap_{i=1}^8(P\cap H_i)=1,
\end{gathered}
\tag{CF.24}
\]

where, if \(\widetilde P\) is the preimage of \(P\) in \(G\),

\[
P\cap H_i=C_{\widetilde P}(x_i)/Z(G).
\tag{CF.25}
\]

These are exact fixed subgroups for lifts \(x_i\); they need not be abstract
element-centralizers in \(P\). The next load-bearing problem is to use the
binary Frattini structure and the cover (CF.24)--(CF.25) to bound the
extension, or to show directly that its exact commutation graph is
ten-colorable. Quotienting by \(P\) can create commuting pairs, so no
pairing or coloring is pulled back without proof.
