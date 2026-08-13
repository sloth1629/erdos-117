# Exact Value at Six: Structural Proof and Finite Certificates

This note proves the computer-assisted exact value at clique cutoff six.  It
records the structural cover theorem, removes the largest exterior-square
enumeration bottleneck \(C_2^5\) without enumerating its subspaces, and gives
the complete finite certificate chain.

## Alternating-map formulation for an elementary abelian central quotient

Let \(V\) and \(W\) be finite-dimensional vector spaces over
\(\mathbb F_2\), and let

\[
B:\mathop{\bigwedge}\nolimits^2V\longrightarrow W
\]

be a linear alternating map. Write

\[
\operatorname{rad}(B)=
\{v\in V:B(v,u)=0\text{ for every }u\in V\}.
\]

The associated nonorthogonality graph has vertex set \(V\), with distinct
\(v,w\) adjacent exactly when \(B(v,w)\ne0\). Put

\[
L=\operatorname{im}
\bigl(B^*:W^*\longrightarrow \mathop{\bigwedge}\nolimits^2V^*\bigr).
\]

Thus \(L\) is the space of scalar alternating forms
\(\lambda\circ B\), for \(\lambda\in W^*\). Since linear functionals
separate points,

\[
\operatorname{rad}(B)=
\bigcap_{\beta\in L}\operatorname{rad}(\beta).
\tag{H6.1}
\]

### Lemma H6.1 [PROVED]

Suppose \(V=\mathbb F_2^5\) and \(\operatorname{rad}(B)=0\). Then the
nonorthogonality graph of \(B\) contains a clique of size at least \(9\).
More precisely:

- if \(L\) contains a rank-four form, the graph has an explicit
  nine-clique; and
- if every member of \(L\) has rank at most two, the graph has a
  sixteen-clique.

#### Rank-four case

Choose \(\beta\in L\) of rank four. Its radical is a line
\(\langle r\rangle\). By (H6.1), there is a form \(\gamma\in L\) for which
\(\gamma(r,-)\ne0\). Choose a complement \(V=U\oplus\langle r\rangle\).
The restriction of \(\beta\) to \(U\) is nondegenerate, so there is a unique
nonzero \(t\in U\) such that

\[
\gamma(r,u)=\beta(t,u)\qquad(u\in U).
\tag{H6.2}
\]

Extend \(t=e_1\) to a symplectic basis
\(e_1,f_1,e_2,f_2\) of \(U\), and set

\[
\begin{aligned}
x_1&=f_1,\\
x_2&=e_1+f_1+e_2,\\
x_3&=e_1+f_1+f_2,\\
x_4&=e_1+f_1+e_2+f_2.
\end{aligned}
\]

Direct substitution in the standard symplectic form gives

\[
\beta(t,x_i)=1,\qquad
\beta(x_i,x_j)=1\quad(i\ne j).
\tag{H6.3}
\]

We claim that

\[
\mathcal C=
\{t\}\cup\{x_i,x_i+r:1\le i\le4\}
\tag{H6.4}
\]

is a nine-clique for \(B\). The nine vectors are distinct because
\(U\cap\langle r\rangle=0\). Equation (H6.3), together with
\(r\in\operatorname{rad}(\beta)\), shows that \(\beta\) detects every pair
in (H6.4) except possibly the four pairs \(\{x_i,x_i+r\}\). For each of
those pairs, (H6.2) gives

\[
\gamma(x_i,x_i+r)=\gamma(x_i,r)
=\gamma(r,x_i)=\beta(t,x_i)=1.
\]

Whenever a scalar form in \(L\) is nonzero on a pair, \(B\) itself is
nonzero on that pair. Hence (H6.4) is the required clique.

#### All-rank-two case

Assume now that every nonzero member of \(L\) has rank two. A rank-two
alternating form is decomposable: it can be written \(a\wedge b\) for
independent \(a,b\in V^*\). Its intrinsic support is the two-dimensional
space

\[
P_{a\wedge b}=\langle a,b\rangle\le V^*.
\]

If \(\dim L=1\), its unique nonzero member has a three-dimensional
radical, contrary to (H6.1). Thus \(L\) contains at least two distinct
nonzero forms in what follows.

We first prove the needed decomposable-subspace dichotomy. If
\(p,q\in L\) are distinct nonzero forms, then \(p+q\) is again nonzero of
rank two. Writing \(p=a\wedge b\), one checks in a basis adapted to the two
supports that \(p+q\) has rank four when
\(P_p\cap P_q=0\), and has rank two when the two supports meet in a line.
The supports cannot be equal, because
\(\bigwedge^2P_p\) is one-dimensional over \(\mathbb F_2\), which would give
\(p=q\). Consequently the family

\[
\mathcal P=\{P_p:0\ne p\in L\}
\]

consists of pairwise line-intersecting two-dimensional subspaces of \(V^*\).

Choose two members

\[
P_1=\langle a,b\rangle,\qquad
P_2=\langle a,c\rangle,\qquad
U_0=\langle a,b,c\rangle.
\]

Any \(P\in\mathcal P\) not containing \(a\) meets \(P_1\) and \(P_2\) in
two distinct lines, so those two lines span \(P\) and show that
\(P\le U_0\). If some such \(P_3\le U_0\) exists, then a member
\(P=\langle a,d\rangle\) which does contain \(a\) must meet \(P_3\) in a
line different from \(\langle a\rangle\); this forces \(d\in U_0\).
Therefore at least one of the following two conclusions holds:

\[
\text{all }P\in\mathcal P\text{ contain }\langle a\rangle,
\qquad\text{or}\qquad
\text{all }P\in\mathcal P\text{ lie in }U_0.
\tag{H6.5}
\]

In the second case \(L\le\bigwedge^2U_0\). The annihilator of \(U_0\) in
\(V\), which has dimension two, then lies in the radical of every form in
\(L\), contrary to (H6.1).

In the first case \(L\le a\wedge V^*\). If
\(\dim L=k\), the common radical of \(L\) has dimension \(4-k\): after
choosing \(b_1,\ldots,b_k\) independent modulo \(\langle a\rangle\), it is

\[
\ker a\cap\ker b_1\cap\cdots\cap\ker b_k.
\]

Equation (H6.1) therefore forces \(k=4\), and hence
\(L=a\wedge V^*\). The affine hyperplane

\[
\mathcal A=\{v\in V:a(v)=1\}
\]

has sixteen elements and is a clique. Indeed, for distinct \(v,w\in
\mathcal A\), choose \(b\in V^*\) with \(b(v+w)=1\). Then

\[
(a\wedge b)(v,w)=b(v)+b(w)=b(v+w)=1.
\]

This completes both cases and proves the lemma. \(\square\)

## Consequence for the quotient \(C_2^5\)

### Corollary H6.2 [PROVED]

If \(G/Z(G)\cong C_2^5\), then \(\nu(G)\ge9\). In particular this central
quotient cannot occur in any group with \(\nu(G)\le6\).

**Proof.** Put \(V=G/Z(G)\). Because \(V\) has exponent two, every square
of an element of \(G\) is central. Also \(G\) has nilpotency class at most
two. It follows from the class-two commutator identities that \(G'\) has
exponent two and that

\[
B(\bar x,\bar y)=[x,y]
\]

is a well-defined alternating \(\mathbb F_2\)-bilinear map
\(\bigwedge^2V\to G'\). Its radical is zero: if \(B(\bar x,V)=0\), then
\(x\) commutes with every element of \(G\), so \(\bar x=0\). Lemma H6.1
now supplies nine cosets whose representatives are pairwise noncommuting.
\(\square\)

### Computational implication [PROVED]

An exterior-square scan at clique cutoff six need not enumerate any of the
\(229{,}755{,}605\) subspaces of
\(\bigwedge^2\mathbb F_2^5\) arising for \(Q=C_2^5\). Some abstract
\(S\)-normal kernels for this quotient can produce degenerate alternating
maps and smaller cliques, but those graphs do not arise with
\(Q=G/Z(G)\): the preceding proof shows that an actual central quotient has
zero radical. Thus skipping the entire quotient \(C_2^5\) is valid for a
search restricted to \(\nu(G)\le6\).

## A failed perfect-graph shortcut

### [DISPROVED]

The assertion that a group with \(\nu(G)\le6\) must have a perfect compressed
noncommuting graph is false. The saved exact graphs for
SmallGroup(32,49) and SmallGroup(32,50) have
\(\nu=a=5\) but contain an induced five-cycle on compressed vertices
\(1,2,3,4,15\); seven saved order-64 examples behave similarly. This does
not refute the weaker possible implication
\(\nu(G)\le6\Rightarrow a(G)\le6\), because the whole graphs in these
examples still satisfy \(\chi=\omega\).

## The six-cover center-index input

The finite exterior-square calculation at cutoff six requires a bound on the
order of the central quotient. The relevant group-cover statement is

\[
f(6)=36,
\tag{H6.6}
\]

where \(f(6)\) is the largest \([G:D]\) among irredundant six-subgroup
covers with intersection \(D\).

### The centralizer bridge [PROVED]

If \(\nu(G)=6\), then the centralizers of a maximum noncommuting set
\(x_1,\ldots,x_6\) form an irredundant six-cover: maximality gives the cover,
and \(x_i\) is private to \(C_G(x_i)\). Their intersection is \(Z(G)\).
Indeed, if a noncentral \(y\) centralized all six \(x_i\), then the
centralizer-drop lemma would give

\[
6\le \nu(C_G(y))\le \nu(G)-2=4,
\]

a contradiction. Consequently (H6.6) implies

\[
[G:Z(G)]\le36.
\tag{H6.7}
\]

This argument applies to arbitrary groups; no finiteness assumption on the
original \(G\) is introduced.

### Status of a proof of \(f(6)=36\)

#### Primary-source theorem statement [CITED-VERIFIED]

Abdollahi--Ataei--Jafarian Amiri--Mohammadi Hassanabadi state (H6.6) in
their primary extended abstract, Theorem D, printed p. 72, and in the
official abstract of their 2005 journal article.

#### Nonmaximal reduction [PROVED]

The repository reconstructs the reduction from an arbitrary irredundant
six-cover to the maximal core-free case and smaller-cover classifications.
Its source provenance is Alencar's 2011 dissertation, Chapter 5, printed
pp. 77--88; the proof-bearing pages were extracted and visually checked rather
than trusted only through OCR.  The reconstructed chain is:

1. quotient by the core of \(D\), preserving \([G:D]\) and
   irredundancy;
2. if the cover is not maximal, enlarge one member to a maximal subgroup,
   choosing the original cover to maximize the number of maximal members;
3. the enlarged cover is redundant, and an essential subcover has five,
   four, or three members;
4. a five-member subcover gives \(16\cdot2=32\);
5. a four-member subcover has core-free quotient index \(6,8\), or \(9\);
   the index-six case closes by the proved coset-intersection bound
   \([H_2\cap H_3\cap H_4:D]\le3!=6\), while the index-eight and
   index-nine cases close by the explicit subgroup-cover case split; and
6. a three-member subcover gives index four, after which the induced covers
   of the enlarged member have at most five members and yield at most
   \(32\), \(36\), or \(18\).

The new factorial coset-intersection lemma used in step 5 is proved
self-contained on printed pp. 80--82. The four-cover input can be taken from
Bryce--Fedri--Serena, Proposition 2.4, printed p. 470, which cleanly records
Greco's classification. It gives precisely quotient indices \(6,8,9\);
the index-eight quotients are 2-groups, and the index-nine quotients are
supersoluble. This avoids typographical omissions in the dissertation's
restatement of Greco.

#### Maximal core-free upper bound [PROVED]

We need only the following consequence of the maximal-cover classification,
not its published isomorphism list.

> If a finite group \(G\) has a maximal irredundant six-cover with
> intersection \(D\) and \(D_G=1\), then \([G:D]\le36\).

Here is the structural proof, with the finite leaves isolated explicitly.
We use the following elementary cover facts.  They follow from the coset-cover
argument given in Alencar, Lemma 2.1, printed pp. 31--34.  We state their exact
content so that every later invocation is visible.

- If \(G=\bigcup_{i=1}^mH_i\) is irredundant, with
  \(D=\bigcap_iH_i\), then \(\bigcap_{j\ne i}H_j=D\) for every \(i\).
- If the members are maximal, \(U\) is abelian minimal normal, and exactly
  \(s\) members contain \(U\), then either \(U\le D\) or \(|U|\le m-s\).
  Indeed, a member not containing \(U\) complements it, and the standard
  private-element coset decomposition covers \(U\) by at most \(m-s\)
  singleton intersections.
- More generally, if the intersection of \(t\) members already equals \(D\),
  deleting one of them enlarges the intersection by index at most
  \(m-t+1\).  This is the same coset decomposition with one fewer member.
- If a normal subgroup \(N\) is contained in \(s\) cover members, then no
  prime \(p>m-s\) divides \(|N|\).  Indeed, every \(p\)-element of \(N\)
  lies in at least those \(s\) members, so the element form of the same cover
  lemma puts it in \(D\).  The subgroup generated by all \(p\)-elements of
  \(N\) is characteristic in \(N\), hence normal in \(G\), and is contained
  in \(D\); core-freeness makes it trivial, contradicting Cauchy's theorem.

Here \(m=6\).  Since \(D_G=1\), a nontrivial normal \(U\) cannot lie in
\(D\).  A core-free irredundant finite-index cover is finite, so ordinary
finite-group arguments apply.  The structural reductions below are a
reconstruction of Alencar's Propositions 4.1--4.2 and Lemmas 4.3--4.4, with
the two identified gaps replaced explicitly; the displayed embeddings and
finite leaves, rather than the source's final classification list, are the
load-bearing statements.

We will also use, once, the following elementary special case.  A finite
2-group cannot have such a cover.  For if it did, every maximal cover member
would be normal, so \(D=D_G=1\), and \(\Phi(G)\le D\) would make
\(G\cong\mathbb F_2^d\).  If \(f_i\) defines the \(i\)-th covering
hyperplane, the map

\[
F:v\longmapsto(f_1(v),\ldots,f_6(v))
\]

is injective because the hyperplanes intersect trivially.  Irredundancy gives,
for every \(i\), a private vector in the \(i\)-th hyperplane and hence puts
\({\bf1}+e_i\) in \(\operatorname{im}F\).  The six vectors
  \({\bf1}+e_i\) form a basis of \(\mathbb F_2^6\): if
\(x+(\sum_i x_i){\bf1}=0\), summing coordinates (six is even) gives
\(\sum_i x_i=0\), hence \(x=0\).  Thus \(F\) is surjective.  But the cover
condition says precisely that \({\bf1}\notin\operatorname{im}F\), a
contradiction.

Likewise, if a finite abelian group with trivial Frattini subgroup has both
2- and 3-parts, its maximal subgroups of index two have the form
\(H_2\times P_3\), while those of index three have the form
\(P_2\times H_3\).  Such subgroups cover \(P_2\times P_3\) only if the
index-two family already covers \(P_2\), or the index-three family already
covers \(P_3\): otherwise choose one point missed by each family and pair
them.  A cover using both types is therefore redundant.  We use this to
exclude one mixed abelian subcase below.

**1. The semisimple branch.**  Suppose \(G\) has no nontrivial abelian
normal subgroup.  The usual counting lemma for a cover by one subgroup and
five others shows that the last five maximal subgroups have index five and
their pairwise intersections lie in the first.  For each such member \(M_i\),
the coset action gives a primitive quotient

\[
G/(M_i)_G\le S_5.
\]

The only primitive subgroups of \(S_5\) whose order is divisible by five are
\(C_5\), \(C_5\rtimes C_2\), \(C_5\rtimes C_4\), \(A_5\), and \(S_5\).
For completeness, let \(P\) be a Sylow-five subgroup.  If \(P\triangleleft H\),
then \(H\le N_{S_5}(P)\cong C_5\rtimes C_4\), giving the first three
possibilities.  If \(P\) is not normal, its number of conjugates is six, so
\(30\mid|H|\).  A subgroup of order 30 cannot lie in \(A_5\), where it would
have index two and be normal; otherwise it would meet \(A_5\) in a subgroup
of order 15, impossible because such a group is cyclic but \(A_5\) has no
element of order 15.  Thus \(|H|=60\) or \(120\), giving \(A_5\) or \(S_5\).
The modern finite certificate shows that neither \(A_5\) nor \(S_5\) has a
qualifying cover.  If every quotient for \(i=2,\ldots,6\) were one of the
first three, all five quotients would be soluble.  But

\[
\bigcap_{i=2}^6(M_i)_G\le \bigcap_{i=2}^6M_i=D
\]

and the left side is normal in \(G\), so it is contained in \(D_G=1\).
Thus \(G\) would embed in a product of soluble groups and itself be soluble,
which is incompatible with this branch.  Hence some quotient is \(A_5\) or
\(S_5\).  More generally, every minimal normal subgroup \(N\) of \(G\) is
isomorphic to \(A_5\): choose \(i\ge2\) with \(N\nleq M_i\), possible because
\(\bigcap_{i=2}^6M_i=D\) and \(N\nleq D\).  Then
\(N\cap(M_i)_G=1\), so \(N\) embeds as a minimal normal subgroup of the
corresponding primitive group.  It is \(C_5\) in the three soluble cases and
\(A_5\) in the other two; the first option is excluded by semisimplicity.

We also need that each of the five cores \(K_i=(M_i)_G\), \(i\ge2\), is
nontrivial.  If \(K_i=1\), then \(G\) itself is a primitive subgroup of
\(S_5\).  The three soluble possibilities contradict the present branch,
while \(A_5\) and \(S_5\) are excluded by the certificate.  Thus choose a
minimal normal \(N_i\le K_i\) for every \(i=2,\ldots,6\); each
\(N_i\cong A_5\).  Suppose two cores, say \(K_i,K_j\), intersect
nontrivially and put \(T=K_i\cap K_j\).  This is normal in \(G\).  If a
prime \(p\ge5\) divided \(|T|\), Cauchy's theorem would give a nonidentity
\(p\)-element \(x\in T\).  It lies in both \(M_i,M_j\).  The cover lemma
for a \(p\)-element in an irredundant six-cover says either \(x\in D\) or
\(p\le6-s\), where \(s\ge2\) is the number of members containing \(x\).
The second alternative is impossible because \(p\ge5>4\), so every
\(p\)-element of \(T\) lies in \(D\).  The subgroup generated by *all*
\(p\)-elements of \(T\) is invariant under every automorphism of \(T\),
hence characteristic in \(T\) and normal in \(G\); it is contained in
\(D\).  Core-freeness forces it to be trivial, a contradiction.
Thus \(|T|\) is divisible only by two and three.  Burnside's theorem makes
\(T\) soluble, and its last nontrivial derived subgroup is a forbidden
abelian normal subgroup of \(G\).  Otherwise the five cores contain pairwise
disjoint minimal normal copies of \(A_5\).
Distinct disjoint normal subgroups centralize one another.  These five copies
form an internal direct product: inductively, if \(N_k\) met the product of
the preceding copies nontrivially, minimal normality would put \(N_k\) inside
that product, while its commutation with every factor would put it in the
center of that product, which is trivial.  Their product therefore has order
\(60^5\).  On the other hand two disjoint cores embed
\(G\) in \(S_5^2\), giving \(|G|\le120^2\), a contradiction.  Thus the
semisimple branch is empty.

This argument also repairs a gap in the dissertation.  Its Lemma 3.3 claims,
without justification, that a conclusion for one triple of cover members can
be repeated with a fourth member.  The displayed five-core intersection
argument above supplies exactly the embedding needed downstream, without
that lemma.

**2. An abelian minimal normal subgroup.**  We may now choose an abelian
minimal normal subgroup \(U\).  It is elementary abelian, and the cover lemma
gives \(|U|\le5\).

- If \(|U|=2\), at least two members, say \(M_5,M_6\), complement \(U\).
  They have index two and are normal.  Every element of prime order at least
  five lies in both, and the cover lemma then puts it in \(D\); the subgroup
  generated by all its conjugates would be normal and contained in \(D\).
  Hence no such prime divides \(|G|\), and Burnside's theorem makes \(G\)
  soluble.  The normal subgroup \(M_5\cap M_6\) is nontrivial (otherwise
  \(|G|\le4\)), so choose a minimal normal \(V\) in it.  It is elementary
  abelian and the cover-size lemma gives \(|V|\le4\).

  If \(|V|=2\), two further members complement \(V\) and have index two.
  Every element of order three then lies in four members and hence in \(D\),
  so \(G\) is a 2-group, contrary to the preceding paragraph.  If \(|V|=4\),
  exactly the four members outside \(M_5,M_6\) complement \(V\) and have
  index four.  Their pairwise intersections are covered by
  \(M_5\cup M_6\).  But the original \(U\), being too small to complement an
  index-four member, lies in all four; it must then lie in \(M_5\) or \(M_6\),
  and hence in five cover members, forcing \(U\le D\), a contradiction.
  Thus \(|V|=3\).

  Conjugation on \(V\) gives \([G:C_G(V)]\le2\).  Equality one would make
  \(V\) central.  Then each of its index-three complements is normal;
  \(M_5,M_6\) are already normal of index two.  These five normal members
  have quotients exactly \(C_3,C_3,C_3,C_2,C_2\).  Their intersection is
  \(D\) by the five-member intersection lemma.  Since this intersection is
  normal, it is contained in \(D_G=1\); equivalently, the product quotient
  map is injective.  Thus \(G\) embeds in
  \(C_3^3\times C_2^2\) and is abelian.  Its Frattini subgroup lies in every
  maximal cover member and hence in \(D\); being normal, it is trivial.  The
  six original members
  therefore give an irredundant cover of this elementary abelian mixed group
  using both index types, contrary to the preceding mixed-abelian
  observation.  Thus \([G:C_G(V)]=2\).

  A private-element calculation now places both \(U\) and \(V\) in the
  remaining member \(M_1\).  If \(V\nleq M_1\), then
  \(M_1,M_2,M_3,M_4\) are its four index-three complements.  For a
  2-element \(x\in C_G(V)\), the direct-complement identity puts \(x\) in
  all four corresponding cores.  Choose \(1\ne v\in V\).  The element
  \(vx\) lies in none of those four complements, so it lies in
  \(M_5\cup M_6\).  Since \(v\in M_5\cap M_6\), the element \(x\) lies in
  at least one of \(M_5,M_6\), hence in five cover members and therefore in
  \(D\).  Characteristic closure would eliminate all 2-elements of
  \(C_G(V)\), contradicting \(U\le C_G(V)\): the normal subgroups \(U,V\)
  have coprime orders and therefore commute.

  If \(U\nleq M_1\), then \(M_1,M_5,M_6\) are its normal index-two
  complements, so every 3-element \(x\in G\) lies in all three.  For
  \(1\ne u\in U\), the element \(ux\) lies in none of those complements and
  hence in one of \(M_2,M_3,M_4\); since \(u\) lies in each of the latter,
  \(x\) belongs to a fourth cover member.  The element cover lemma puts all
  3-elements in \(D\), whose characteristic closure eliminates them.  Then
  \(G\) would be a 2-group, already excluded.  Thus \(U,V\le M_1\).

  Thus three members have index three and two have index two.  The maps from
  their cores first embed \(G\) in \(C_2^2\times S_3^3\), a supersoluble
  group, so the remaining maximal index is two or three.

  If \([G:M_1]=2\), the cover-size lemma gives
  \(M_5\cap M_6\cap(M_2)_G=1\): a minimal normal subgroup in this
  intersection would have order at most three; order two would also lie in
  the index-three members, and order three would then lie in too many cover
  members, in either case forcing it into \(D\).  The three coset actions
  therefore give

  \[
  G\hookrightarrow C_2^2\times S_3
  \]

  and hence \(|G|\le24\).  If \([G:M_1]=3\), the analogous argument gives
  \((M_1)_G\cap(M_2)_G\cap M_5=1\), and hence

  \[
  G\hookrightarrow C_2\times S_3^2.
  \]

  Here \(|G|\le72\).  Rather than use a fragile order-divisibility shortcut,
  the certificate enumerates every subgroup conjugacy class of the whole
  ambient group \(C_2\times S_3^2\).  All qualifying subgroup types have
  order at most 36, and the sole order-36 type is
  \(\operatorname{SmallGroup}(36,13)\).  Hence \(|G|\le36\) in this branch.

- If \(|U|=3\) and there is no normal subgroup of order two, at least three
  members, say \(M_4,M_5,M_6\), complement \(U\) and have index three.  Put
  \(K=\bigcap_{i=4}^6(M_i)_G\) and
  \(T=\bigcap_{i=1}^3(M_i)_G\).  We claim that \(K=1\) or \(T=1\).
  If \(K\ne1\), the preceding normal-subgroup prime lemma shows that \(K\)
  has order divisible only by two and three, hence is soluble.  A minimal
  normal subgroup \(V\le K\) is therefore elementary abelian; it has order at
  most three, and the absence of a normal subgroup of order two gives
  \(|V|=3\).  It is contained in exactly \(M_4,M_5,M_6\), so the equality
  case of the cover-counting lemma gives

  \[
  M_i\cap M_j\subseteq M_4\cup M_5\cup M_6
  \qquad(i\ne j\in\{1,2,3\}).
  \]

  If \(T\ne1\), every 3-element of \(T\) belongs to a fourth cover member by
  this inclusion and hence lies in \(D\); characteristic closure eliminates
  all such elements.  Primes at least five are eliminated by the normal-
  subgroup prime lemma, so \(T\) is a 2-group.  A minimal normal subgroup in
  \(T\) is then elementary abelian of order at most three, hence has order
  two, contrary to the hypothesis.  Thus \(T=1\), proving the claim.

  Use the triple whose core intersection is trivial.  If one of its three
  index-three members is normal, the direct-complement calculation makes
  the corresponding order-three minimal normal subgroup central and all
  three members normal; their quotient maps embed \(G\) in \(C_3^3\), so
  \(|G|\le27\).  Otherwise each core quotient is \(S_3\), and
  the three quotient maps embed \(G\) as a subdirect product of \(S_3^3\).
  Thus the only larger leaf is a subdirect product of \(S_3^3\).  The exhaustive subdirect-product
  certificate finds qualifying covers only for
  \(\operatorname{SmallGroup}(18,4)\), with \(|D|=1\), and
  \(\operatorname{SmallGroup}(54,14)\), with \(|D|=2\).  Their indices are
  \(18\) and \(27\).

- Suppose \(|U|=4\).  The preceding branches let us assume that \(G\) has no
  normal subgroup of order two or three.  Four members, say
  \(M_3,M_4,M_5,M_6\), complement \(U\), and their coset actions have image
  in \(S_4\).  Two of their cores have trivial intersection.  To see this,
  if \((M_3)_G\cap(M_4)_G=1\) there is nothing to prove.  Otherwise that
  normal intersection has only primes two and three and is soluble; a
  minimal normal subgroup \(W\) in it has order at most four, and the
  exclusions of orders two and three force \(|W|=4\).  It is contained in
  exactly \(M_3,M_4\), so the equality case of the counting lemma puts every
  pairwise intersection among \(M_1,M_2,M_5,M_6\) inside
  \(M_3\cup M_4\).  Also
  \((M_i)_G\cap(M_5)_G\cap(M_6)_G=1\) for \(i=3,4\), since otherwise a
  minimal normal subgroup there would have order at most three.  If
  \((M_5)_G\cap(M_6)_G\ne1\), the same soluble-minimal-normal argument gives
  a normal subgroup \(Q\) of order four inside it.  The pairwise-intersection
  inclusion puts \(Q\) inside \(M_3\cup M_4\); a subgroup contained in the
  union of two subgroups lies in one of them, placing \(Q\) in one of the
  just-proved trivial triple-core intersections, a contradiction.  Hence two
  complement cores, call them \(N_5,N_6\), are disjoint, and their coset
  actions embed \(G\) in \(S_4^2\).

  Put \(C=C_G(U)\).  For each complement core \(N_i\), the direct-complement
  identity gives \(C=U\times N_i\).  Every element of odd prime-power order
  in \(C\) lies in all four such cores, because \([C:N_i]=4\), and hence lies
  in \(N_5\cap N_6=1\).  Moreover every quotient \(C/N_i\cong U\) is
  elementary abelian, so \(\Phi(C)\le N_i\) for all four complement cores;
  in particular \(\Phi(C)\le N_5\cap N_6=1\).  Thus \(C\) is elementary
  abelian, say \(|C|=2^d\), and

  \[
  C=U\times N_i,\qquad N_5\cap N_6=1.
  \]

  Hence \(\dim N_i=d-2\), and the two disjoint subspaces give
  \(2(d-2)\le d\), so \(d\le4\).  Conjugation embeds
  \(G/C\) in \(\operatorname{Aut}(U)\cong S_3\); since a qualifying group
  cannot be a 2-group, \([G:C]\) is three or six.  The possible orders are
  \(12,24\) for \(d=2\), \(24,48\) for \(d=3\), and \(48,96\) for
  \(d=4\).  Thus the only values exceeding \(36\) are \(48\) and \(96\).
  The certificate exhausts all subgroup conjugacy classes of those orders in
  \(S_4^2\) and finds no qualifying cover.  Thus this branch has no
  counterexample to the index bound.  This
  dimension argument replaces the invalid implication in the dissertation's
  Proposition 4.2 that \(S_4\) itself having no cover would exclude all its
  subgroups.

- Finally let \(|U|=5\).  Five cover members complement \(U\).  Their cores
  \(K_i=(M_i)_G\) satisfy \(C_G(U)=U\times K_i\).  For every prime
  \(p\ne5\), each \(p\)-element of \(C_G(U)\) belongs to all five \(K_i\),
  because \([C_G(U):K_i]=5\).  It therefore lies in \(D\); the subgroup
  generated by all such \(p\)-elements is characteristic in \(C_G(U)\),
  normal in \(G\), and contained in \(D\), so core-freeness makes it trivial.
  Moreover \(C_G(U)/K_i\cong U\) is elementary abelian, so
  \(\Phi(C_G(U))\le K_i\) for every \(i\).  The Frattini subgroup is
  characteristic in the normal subgroup \(C_G(U)\), while
  \(\bigcap_iK_i\le D\); core-freeness therefore gives
  \(\Phi(C_G(U))=1\).  Thus \(C_G(U)\) is elementary abelian.  For every
  \(i\ne j\), \(K_i\cap K_j=1\):
  otherwise a minimal normal subgroup in their intersection would, by the
  cover-size lemma, have order at most four, impossible in this 5-group.
  Writing \(|C_G(U)|=5^d\), each \(K_i\) has dimension \(d-1\), so two
  disjoint such cores give \(2(d-1)\le d\) and \(d\le2\).  Hence the
  centralizer has order \(5\) or \(25\), while
  conjugation gives \(G/C_G(U)\le\operatorname{Aut}(C_5)\cong C_4\).
  If the center is nontrivial, choose the minimal normal \(U\) inside the
  center.  Then \(C_G(U)=G\), so \(|G|\le25\).  If the centralizer has order five, the
  possible primitive groups have order \(10\) or \(20\).  The only remaining
  candidates have order \(50\) or \(100\) and trivial center.  The finite
  certificate censuses all five groups of order \(50\) and all sixteen of
  order \(100\), verifies that the structural filter selects exactly the two
  and five centerless types respectively, and exhaustively cover-checks each
  selected type.  The only qualifying types are
  \(\operatorname{SmallGroup}(50,4)\), always with \(|D|=2\), and
  \(\operatorname{SmallGroup}(100,11)\), always with \(|D|=4\).  Both have
  index \(25\).

This exhausts the structural branches and proves the asserted maximal
core-free upper bound.

The proof is self-contained modulo the standard finite-group results stated
where used (Burnside's \(p^aq^b\)-theorem, basic coset actions and Frattini
facts) and the explicitly labeled finite leaves below.  Alencar's Chapter 4
is the source of the case architecture, but neither its contradictory
subdirect-product labels nor its two flawed implications are used.

#### Finite leaves and independent certificate [COMPUTED]

The following table records the exact one-to-one correspondence between a
structural leaf above and its finite certificate.

| structural leaf | complete finite family | certified conclusion |
|---|---|---|
| semisimple primitive quotient | \(A_5,S_5\) | no qualifying cover |
| \(|U|=2\), possible large case | order-72 subgroups of \(S_3^3\), and every subgroup class of \(C_2\times S_3^2\) | no qualifying order-72 cover; unique qualifying order-36 type is \((36,13)\) |
| \(|U|=3\) | all subdirect products of \(S_3^3\) | positives exactly \((18,4)\), \(|D|=1\), and \((54,14)\), \(|D|=2\) |
| \(|U|=4\) | every order-48 and order-96 subgroup class of \(S_4^2\) | no qualifying cover |
| \(|U|=5\) | all groups of orders \(50\) and \(100\) (with the structural center filter) | positives exactly \((50,4)\), \(|D|=2\), and \((100,11)\), \(|D|=4\) |

The GAP 4.16.0/SmallGrp 1.5.4 producer is
`experiments/configs/f6_maximal_cover_audit.g`.  It enumerates ambient
subgroup conjugacy classes and every six-subset of maximal subgroups.  The
outputs are `experiments/logs/f6_maximal_cover_classes.tsv` and
`experiments/logs/f6_maximal_cover_groups.tsv`.  To avoid trusting GAP's
subgroup or maximality routines as the final certificate, the independent
Python verifier `src/python/analyze_f6_maximal_cover_audit.py` reads the saved
multiplication tables, checks the group axioms, generates every subgroup,
recovers all maximals, and rechecks every union, private-element witness,
intersection, and core.

The verifier independently enumerates \(5{,}257\) subgroups in \(48\)
isomorphism types and tests all \(5{,}545{,}351\) six-subsets: \(100{,}483\)
are covers, \(10{,}308\) are irredundant, and \(6{,}678\) also have
core-free intersection.  Its ambient census comprises \(165\) conjugacy
class records, including all fourteen subdirect classes in \(S_3^3\), all
twenty-one order-48 and fifteen order-96 classes in \(S_4^2\), and every
group of orders \(50\) and \(100\).  The producer and two load-bearing TSV
SHA-256 values are respectively

\[
\begin{aligned}
&81674bcbcefa95caa62bf67aa2067b9628c96e2d3179fe6db55696d675185af8,\\
&18864118296e8d517d7e662edc1e94bcbbacd385cce6ea27645abe68c6acf86f,\\
&30eec574a216b234dfa20c0fa3d8369788ba5cfa463a8849dfc1ba4219c9ca8e.
\end{aligned}
\]

The computed positive types are \((18,4),(24,14),(36,13),(50,4),(54,14)\),
and \((100,11)\), with qualifying-cover counts
\(234,4,72,25,6318,25\) and intersection orders \(1,1,1,2,2,4\),
respectively.  In particular,

\[
\operatorname{SmallGroup}(36,13)
 \cong C_2\times\bigl((C_3^2)\rtimes C_2\bigr)
\]

has 72 qualifying covers with trivial intersection.  It proves
\(f(6)\ge36\).  By contrast, \(S_3\times S_3=\operatorname{SmallGroup}(36,10)\)
has 38 six-subsets which cover, but none is irredundant; a published claim
listing it as a qualifying type is false.  SmallGroup identifiers and exact
subgroup masks replace the dissertation's contradictory \(L_i\) labels.

Combining the structural maximal upper bound, this exact lower witness, and
the checked nonmaximal reduction proves (H6.6), and hence (H6.7).

## Exact value of \(h(6)\)

### Exterior-square reduction [PROVED]

Let \(G\) be arbitrary with \(\nu(G)=6\).  The preceding center-index bound
gives a finite group

\[
Q=G/Z(G),\qquad |Q|\le36.
\]

For the central extension \(1\to Z(G)\to G\to Q\to1\), lifted commutators
give a \(Q\)-equivariant homomorphism

\[
\kappa_G:Q\wedge Q\longrightarrow G',
\qquad q\wedge r\longmapsto[\widehat q,\widehat r].
\tag{H6.8}
\]

It is independent of the lift choices because the extension kernel is
central.  Brown--Johnson--Robertson, Proposition 7, printed p. 182, proves
the universal exterior-pairing factorization; their Corollary 2,
pp. 182--183, identifies \(Q\wedge Q\) with \(S_Q'\) for a Schur cover
\(S_Q\twoheadrightarrow Q\) when \(Q\) is finite.  Under this identification
\(K=\ker\kappa_G\) is normal in \(S_Q\), and

\[
q\sim r
\quad\Longleftrightarrow\quad
[\widetilde q,\widetilde r]\notin K
\tag{H6.9}
\]

defines exactly the compressed noncommuting graph of \(G\) on the central
cosets.  Enumerating every \(S_Q\)-normal \(K\le S_Q'\) is therefore an
exhaustive overcount of all possible commutation graphs; neither a map
\(S_Q\to G\) nor an isomorphism \(G\cong S_Q/K\) is asserted.

An enumerated graph can be the graph on the *exact* quotient \(G/Z(G)\) only
when its radical is the identity.  Indeed, an isolated coset \(q=xZ(G)\)
means \([x,g]=1\) for every \(g\in G\), so \(x\in Z(G)\) and \(q=1\).
Conversely the identity coset is always isolated.  Finally, the foundational
graph compression gives

\[
\nu(G)=\omega(\Delta_G),\qquad a(G)=\chi(\Delta_G),
\tag{H6.10}
\]

including for infinite \(G\), because one representative from each central
coset records every commutation relation and every color class generates an
abelian subgroup.

### Complete finite scan [COMPUTED]

There are exactly 162 isomorphism types of groups \(Q\) of order at most
36.  The GAP 4.16.0/SmallGrp 1.5.4 producer
`experiments/configs/h6_exterior_scan.g` scans 161 of them.  For each it
constructs a fixed Schur cover, identifies \(S_Q'\), and enumerates all
\(S_Q\)-normal subgroups \(K\le S_Q'\).  Kernel serial ranges are complete,
giving 23,527 records.  The omitted quotient is
\(C_2^5=\operatorname{SmallGroup}(32,51)\): Corollary H6.2 proves that any
zero-radical commutator map for this exact central quotient has a nine-clique,
so it cannot occur at cutoff six.  This avoids enumerating its
229,755,605 exterior-square subspaces.

Of the 23,527 kernel records, 18,231 have radical larger than the identity
and hence do not represent an exact center quotient.  Among the 5,296
faithful records (4,045 distinct labeled graphs), 4,982 contain a stored
seven-clique.  The remaining 314 graphs were solved exactly.  Their complete
distribution is

| \((\omega,\chi)\) | \((1,1)\) | \((3,3)\) | \((4,4)\) | \((5,5)\) | \((6,6)\) |
|:---|---:|---:|---:|---:|---:|
| records | 1 | 1 | 2 | 93 | 217 |

Thus every faithful graph with clique number at most six has chromatic
number at most six.  The independent standard-library verifier
`src/python/analyze_h6_exterior_scan.py` reparses every adjacency tuple,
checks symmetry, radical witnesses and complete kernel serial ranges, and
computes exact maximum cliques and chromatic numbers for the 314 candidates.
It was rerun independently for this audit and returned no failure.  The GAP
script, raw TSV, verifier, and certified JSON SHA-256 values are

\[
\begin{aligned}
&6e65e93760d37fb4afad4722e38aa7ec67dfb1e4bcfb1ed6ea121f3bba92e2f1,\\
&142224d5416787eadd3e9126f2203b6d0895a5ce2d078713fa8cc87af5ce60a7,\\
&f0090cde8899b82e9fcbec5845419dc45e8b3e1852ec30fc124faf0ec531f376,\\
&d350e66ac16cdf3459ed24b0cb1e18ba730331663ff379ece4c6d9f50fee4eb9.
\end{aligned}
\]

### Theorem H6.3 [PROVED]

\[
h(6)=6.
\]

**Proof.**  Let \(G\) satisfy \(\nu(G)\le6\).  If \(\nu(G)\le5\), the
proved computer-assisted value \(h(5)=5\) gives \(a(G)\le5\).  Otherwise
\(\nu(G)=6\), the center-index argument gives \(|G/Z(G)|\le36\), and
(H6.8)--(H6.10) place its compressed graph among the faithful records of the
complete scan.  Corollary H6.2 excludes \(C_2^5\).  The scan gives
\(a(G)=\chi(\Delta_G)\le6\), proving \(h(6)\le6\).

For the reverse inequality, the dihedral group of order ten has five
reflections and the nonidentity rotations.  The five reflections are
pairwise noncommuting and any nonidentity rotation fails to commute with
every reflection, giving a six-clique.  Its abelian subgroups are contained
either in the rotation subgroup or in one of the five order-two reflection
subgroups, so covering all five reflections and the nonidentity rotations
requires at least six abelian subgroups; those six subgroups also give a
cover.  A noncommuting set meets each abelian cover member at most once, so
the same cover also gives \(\nu(D_{10})\le6\).  Hence
\((\nu(D_{10}),a(D_{10}))=(6,6)\), and \(h(6)\ge6\).
\(\square\)
