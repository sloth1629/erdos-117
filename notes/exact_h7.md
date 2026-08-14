# Exact Value at Seven: Structural Proof and Finite Certificates

This note proves the computer-assisted exact value

\[
h(7)=10.
\]

There is one new cutoff-seven primary-source input: the verified theorem
\(f(7)=81\) for irredundant seven-subgroup covers.  The repository then
reduces every central extension to a finite exterior-square graph and gives
an exact, reproducible disposition of all 738 possible center quotients.
The largest cases require three different arguments: alternating-form
structure for \(C_2^6\), character-annihilator searches for eleven
order-64 quotients, and an affine character classification for
\(C_2^3\times D_8\).  The lower bound is the independently proved group
\(S(3,2)\), for which \((\nu,a)=(7,10)\).

## 1. Alternating-map model for \(C_2^6\)

Let \(G/Z(G)\cong C_2^6\), and put

\[
V=G/Z(G)\cong\mathbb F_2^6.
\]

Because \(V\) is abelian, \(G\) has nilpotency class at most two. Because
every square is central, the class-two commutator identities also give
\([x,y]^2=[x^2,y]=1\). Thus \(G'\) is an elementary abelian 2-group, generated
by the at most fifteen commutators of lifts of a basis of \(V\). In
particular it is finite even when \(G\) itself is infinite. The map

\[
B:\bigwedge^2V\longrightarrow G',\qquad
B(\bar x,\bar y)=[x,y]
\tag{H7.1}
\]

is therefore a well-defined alternating \(\mathbb F_2\)-linear map. It has
zero radical:

\[
B(v,V)=0\quad\Longrightarrow\quad v=0,
\tag{H7.2}
\]

because a lift of a radical vector commutes with every element of \(G\) and
so represents the identity coset of \(Z(G)\).

Put \(W=\operatorname{im}B=G'\) and

\[
L=\operatorname{im}
\bigl(B^*:W^*\longrightarrow\bigwedge^2V^*\bigr).
\]

Linear functionals on \(W\) separate its points, and hence

\[
\begin{aligned}
B(v,w)\ne0
&\quad\Longleftrightarrow\quad
\beta(v,w)=1\text{ for some }\beta\in L,\\
\operatorname{rad}B
&=\bigcap_{\beta\in L}\operatorname{rad}\beta.
\end{aligned}
\tag{H7.3}
\]

Write \(\Delta(L)\) for the graph on \(V\) in which distinct \(v,w\) are
adjacent exactly under the first condition in (H7.3). Central-coset
compression gives

\[
\nu(G)=\omega(\Delta(L)),\qquad
a(G)=\chi(\Delta(L)).
\tag{H7.4}
\]

The chromatic equality uses both directions of the dictionary: a color class
is a pairwise commuting set and therefore generates an abelian subgroup,
while an abelian cover restricts to a coloring. If \(L_0\le L\), then
\(\Delta(L_0)\) is a spanning subgraph of \(\Delta(L)\). Consequently

\[
\omega(\Delta(L_0))\le\omega(\Delta(L)).
\tag{H7.5}
\]

This elementary monotonicity is the pruning step used below: an eight-clique
in any two-dimensional pencil contained in \(L\) excludes \(L\) at cutoff
seven.

### Proposition H7.1 [PROVED]

For an actual center quotient \(G/Z(G)\cong C_2^6\), the associated form
space \(L\) has zero common radical, and (H7.4)--(H7.5) apply even if \(G\) is
infinite.

**Proof.** The preceding derivation proves every assertion. Notice in
particular that it uses the commutator map of the central extension, not the
commuting graph of the abstract quotient \(G/Z(G)\), which is abelian.
\(\square\)

## 2. A pencil containing a nondegenerate form

All alternating forms on a six-dimensional vector space have rank \(0,2,4\),
or \(6\), and two forms of the same rank are equivalent under
\(\operatorname{GL}(V)\). Fix the lexicographic bit encoding

\[
(0,1),(0,2),\ldots,(0,5),(1,2),\ldots,(4,5)
\tag{H7.6}
\]

of the fifteen coefficients of an alternating form. In this encoding the
certificate fixes the nondegenerate form

\[
\beta_6=e_0^*\wedge e_3^*+e_1^*\wedge e_4^*
             +e_2^*\wedge e_5^*,
\qquad \operatorname{code}(\beta_6)=2180.
\tag{H7.7}
\]

Every two-dimensional pencil containing \(\beta_6\) is
\(\langle\beta_6,\gamma\rangle\), where
\(\gamma\notin\{0,\beta_6\}\), and the two choices \(\gamma\) and
\(\gamma+\beta_6\) give the same pencil. Hence there are exactly

\[
\frac{2^{15}-2}{2}=16{,}383
\tag{H7.8}
\]

normalized pencils. This count makes a direct exhaustive loop possible; no
enumeration of the \(623{,}476{,}476{,}706{,}836{,}148\) subspaces of
\(\bigwedge^2V^*\) is involved.

### Lemma H7.2 [COMPUTED]

Every two-dimensional alternating-form pencil on \(\mathbb F_2^6\) that
contains a rank-six form has an eight-clique. In fact its clique number is at
least nine.

The producer `src/python/h7_c2_6_pencils.py` directly loops over all 16,383
normalized choices in (H7.8), constructs the 64-vertex graph, and checks an
eight-clique for every one. Independently of that load-bearing raw
loop, it compresses the pencils under the stabilizer
\(\operatorname{Sp}(6,2)\). The 63 symplectic transvections

\[
\tau_u(x)=x+\beta_6(x,u)u\qquad(0\ne u\in V)
\tag{H7.9}
\]

preserve \(\beta_6\) and generate the full symplectic group (of order
\(1{,}451{,}520\)). Breadth-first orbit enumeration, always normalizing
\(\gamma\sim\gamma+\beta_6\), gives the following complete partition.

For completeness, the generation assertion has an elementary induction.
The transvections act transitively on nonzero vectors: if
\(\beta_6(x,y)=1\), then \(\tau_{x+y}(x)=y\); if the pairing is zero and
\(x\ne y\), choose \(z\) with
\(\beta_6(x,z)=\beta_6(y,z)=1\) and use two such moves. After arranging that
an isometry fixes a symplectic-basis vector \(e\), write the image of its
partner as \(f+ae+w\), with \(w\in\langle e,f\rangle^\perp\). The
transvection with vector \(e+w\), followed if necessary by the transvection
with vector \(e\), fixes \(e\) and sends this image to \(f\). Induction on
the orthogonal complement proves generation. The standard order formula
\(2^{3^2}\prod_{i=1}^3(2^{2i}-1)\) gives the displayed group order.

| representative \(\gamma\) | orbit size | ranks of the three nonzero forms | exact \(\omega\) |
|---:|---:|:---:|---:|
| 1 | 315 | \((2,6,6)\) | 12 |
| 4 | 336 | \((2,4,6)\) | 15 |
| 36 | 5,040 | \((4,4,6)\) | 15 |
| 40 | 3,780 | \((4,6,6)\) | 11 |
| 76 | 4,032 | \((4,6,6)\) | 15 |
| 728 | 2,880 | \((6,6,6)\) | 9 |

The orbit sizes sum to 16,383. Exact maximum-clique witnesses for the six
representatives prove the stronger minimum nine, and transport through every
generator is checked on every representative. The saved certificate is
`experiments/logs/h7_c2_6_rank6_pencils.json`; its concise transcript is
`experiments/logs/h7_c2_6_rank6_pencils.stdout.txt`.
The producer and saved-certificate SHA-256 values are respectively
`dd3e14510d8a1047eebb4c64c7476cdefa6aa72c5cc9cd2a2a74429251d0b1b6`
and
`7ce95c5c98ab265ccee87cfa53c30ffe781fb1ea6f77e13c1ced0cbf75482855`.

The direct normalized-pencil loop is important logically: even without the
generation statement for the transvections, the checked loop itself exhausts
every possible \(\gamma\). The orbit calculation is an independent
compression and exact-strength check.

### Consequence H7.3 [PROVED]

Suppose \(L\le\bigwedge^2V^*\), \(\omega(\Delta(L))\le7\), and \(L\)
contains a rank-six form. Then \(L\) is one-dimensional.

**Proof.** Move the rank-six form to \(\beta_6\) by a change of basis. If
\(\dim L\ge2\), choose
\(\gamma\in L\setminus\langle\beta_6\rangle\). Lemma H7.2 gives an
eight-clique in \(\Delta(\langle\beta_6,\gamma\rangle)\), and (H7.5) gives
the same clique in \(\Delta(L)\), a contradiction. \(\square\)

## 3. Pencils through a rank-four form

Fix now

\[
\beta_4=e_0^*\wedge e_3^*+e_1^*\wedge e_4^*,
\qquad \operatorname{code}(\beta_4)=132,
\tag{H7.10}
\]

with

\[
U=\langle e_0,e_1,e_3,e_4\rangle,\qquad
R=\operatorname{rad}\beta_4=\langle e_2,e_5\rangle.
\tag{H7.11}
\]

We record the completeness of the stabilizer calculation explicitly. Since
the radical is intrinsic, every
\(g\in\operatorname{Stab}_{\operatorname{GL}(V)}(\beta_4)\) preserves \(R\).
Relative to \(V=U\oplus R\), it has, and may have arbitrarily, the block form

\[
g=\begin{pmatrix}A&0\\ C&D\end{pmatrix},\qquad
A\in\operatorname{Sp}(U,\beta_4|_U),\quad
D\in\operatorname{GL}(R),\quad
C\in\operatorname{Hom}(U,R).
\tag{H7.12}
\]

Indeed, preservation of the radical forces the upper-right block to vanish,
and preservation of the form is then exactly the condition
\(A\in\operatorname{Sp}(U)\); the other two blocks do not enter the value of
\(\beta_4\). Thus the full stabilizer is

\[
\operatorname{Hom}(U,R)\rtimes
  \bigl(\operatorname{Sp}(4,2)\times\operatorname{GL}(2,2)\bigr)
\tag{H7.13}
\]

and has order \(2^8\cdot720\cdot6=1{,}105{,}920\). It is generated by the
fifteen symplectic transvections on \(U\), two elementary generators of
\(\operatorname{GL}(R)\), and the eight elementary shears spanning
\(\operatorname{Hom}(U,R)\). Hence the 25 transformations used below
generate the full stabilizer, not merely a convenient subgroup.

As before, all pencils through \(\beta_4\) are exhausted by the 16,383
normalized values \(\gamma\sim\gamma+\beta_4\). Once the rank-six case has
been excluded, only the 5,471 pencils for which both \(\gamma\) and
\(\gamma+\beta_4\) have rank at most four remain. Their rank-profile counts
are

\[
\begin{array}{c|rrr}
\text{profile}&(2,2,4)&(2,4,4)&(4,4,4)\\ \hline
\text{pencils}&10&375&5{,}086.
\end{array}
\tag{H7.14}
\]

### Lemma H7.4 [COMPUTED]

Let \(P=\langle\beta_4,\gamma\rangle\) be one of the 5,471 pencils in
(H7.14). Then at least one of the following holds:

1. \(\Delta(P)\) contains an eight-clique;
2. \(\operatorname{rad}P=R=\operatorname{rad}\beta_4\).

The producer `src/python/h7_c2_6_rank4_pencils.py` checks this dichotomy
directly for every normalized \(\gamma\), so its completeness does not depend
on orbit classification. Of the 5,471 pencils it saves and verifies an
eight-clique for 5,450; the other 21 have common radical exactly

\[
R=\{0,4,32,36\}
\]

in the vector-bit encoding. Its full-stabilizer orbit compression gives seven
relevant orbits:

| representative \(\gamma\) | orbit size | rank profile | \(|\operatorname{rad}P|\) | exact \(\omega(P)\) |
|---:|---:|:---:|---:|---:|
| 1 | 15 | \((2,4,4)\) | 4 | 6 |
| 2 | 360 | \((2,4,4)\) | 2 | 11 |
| 4 | 10 | \((2,2,4)\) | 4 | 9 |
| 38 | 1,080 | \((4,4,4)\) | 2 | 9 |
| 48 | 1,440 | \((4,4,4)\) | 1 | 13 |
| 76 | 6 | \((4,4,4)\) | 4 | 5 |
| 2,052 | 2,560 | \((4,4,4)\) | 1 | 15 |

The sizes sum to 5,471. The only orbits whose clique number is at most seven
are represented by 1 and 76; in both cases the common radical has four
elements and is exactly \(R\).

For clarity, alternative 2 is a property of the pencil, not of the chosen
second generator. Replacing \(\gamma\) by \(\gamma+\beta_4\) does not change
it, because for \(r\in R\)

\[
(\gamma+\beta_4)(r,x)=\gamma(r,x).
\tag{H7.15}
\]

It is also invariant under the stabilizer: a stabilizer element preserves
\(R\) and transports the common radical of the pencil. Thus the assertion
for representatives 1 and 76 propagates to their entire orbits. The complete
certificate is `experiments/logs/h7_c2_6_rank4_pencils.json`; its SHA-256 is
`e6f11f3e313308ffc5f9b80871a31a6ea724e5e4599a256cd011fa5947b4ced9`.
The producer SHA-256 is
`48751f50a99e446e33b3c92d5f10b8ebb6342804728ea8fc50a037e4469f6614`.

### Consequence H7.5 [PROVED]

There is no zero-common-radical form space \(L\le\bigwedge^2V^*\) with
\(\omega(\Delta(L))\le7\) that contains a rank-four form but no rank-six
form.

**Proof.** Move a rank-four member of \(L\) to \(\beta_4\). For every
\(\gamma\in L\setminus\langle\beta_4\rangle\), the pencil
\(P_\gamma=\langle\beta_4,\gamma\rangle\) occurs in (H7.14). By (H7.5), it
cannot have an eight-clique. Lemma H7.4 therefore gives
\(\operatorname{rad}P_\gamma=R\), so \(\gamma(r,x)=0\) for every \(r\in R\)
and \(x\in V\). The same statement is automatic for
\(\gamma=0,\beta_4\). Hence

\[
R\le\bigcap_{\gamma\in L}\operatorname{rad}\gamma,
\]

contrary to the zero-common-radical hypothesis. \(\square\)

### Certificate reproduction [COMPUTED]

Both finite lemmas use only the Python standard library and the repository's
exact clique solver. From the repository root they are regenerated by

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-h7-r6-pycache \
python3 src/python/run_h7_c2_6_pencils.py \
  --output experiments/logs/h7_c2_6_rank6_pencils.json \
  --stdout-log experiments/logs/h7_c2_6_rank6_pencils.stdout.txt

PYTHONPYCACHEPREFIX=/tmp/erdos117-h7-r4-pycache \
python3 src/python/run_h7_c2_6_rank4_pencils.py \
  --output experiments/logs/h7_c2_6_rank4_pencils.json \
  --stdout-log experiments/logs/h7_c2_6_rank4_pencils.stdout.txt
```

The verification test
`ScalarSymplecticLogTests.test_h7_bounded_batches_and_c2_6_pencil_certificates`
recomputes both certificate payloads and compares them with the saved JSON.
Both producers and that targeted test were rerun during this audit without a
failure.

## 4. The all-rank-two branch

The last structural branch admits a computation-free treatment in dimension
six.

### Lemma H7.6 [PROVED]

Let \(L\le\bigwedge^2V^*\), where \(\dim V=6\), and suppose every nonzero
member of \(L\) has rank two. Then either

\[
L\le a\wedge V^*\quad\text{for some }0\ne a\in V^*,
\tag{H7.16}
\]

or

\[
L\le\bigwedge^2U_0\quad\text{for some three-dimensional }U_0\le V^*.
\tag{H7.17}
\]

If \(L\) has zero common radical, only (H7.16) is possible, it forces
\(L=a\wedge V^*\), and \(\Delta(L)\) has a 32-clique.

**Proof.** If \(L=0\), (H7.16) holds for any nonzero \(a\). If \(L\) has
dimension one, write its generator as \(a\wedge b\); then (H7.16) holds and
its four-dimensional radical is nonzero. We may therefore assume that
\(L\) contains at least two distinct nonzero forms.

A rank-two alternating form is decomposable, say
\(p=a\wedge b\), and has the intrinsic two-dimensional support
\(P_p=\langle a,b\rangle\le V^*\). For distinct nonzero \(p,q\in L\), the
form \(p+q\) is again nonzero of rank two. If \(P_p\cap P_q=0\), a basis
adapted to the two supports shows that \(p+q\) has rank four. The supports
also cannot coincide: \(\bigwedge^2P_p\) is one-dimensional, and over
\(\mathbb F_2\) it has only one nonzero vector. Therefore the supports of
the nonzero members of \(L\) are distinct pairwise line-intersecting planes.

Choose two of them as

\[
P_1=\langle a,b\rangle,\qquad
P_2=\langle a,c\rangle,\qquad
U_0=\langle a,b,c\rangle.
\]

If every support contains \(\langle a\rangle\), (H7.16) follows. Otherwise
choose \(P_3\) not containing \(a\). Its intersection lines with \(P_1\) and
\(P_2\) are distinct and span \(P_3\), so \(P_3\le U_0\). Any support not
containing \(a\) is contained in \(U_0\) by the same argument. A support
\(P=\langle a,d\rangle\) must meet \(P_3\) in a line different from
\(\langle a\rangle\), which forces \(d\in U_0\). Thus all supports lie in
\(U_0\), proving (H7.17).

In case (H7.17), the three-dimensional annihilator of \(U_0\) in \(V\) lies
in the radical of every member of \(L\), so the common radical is nonzero.
In case (H7.16), choose \(b_1,\ldots,b_k\) independent modulo
\(\langle a\rangle\) so that

\[
L=\langle a\wedge b_1,\ldots,a\wedge b_k\rangle.
\]

Its common radical is

\[
\ker a\cap\ker b_1\cap\cdots\cap\ker b_k,
\]

of dimension \(5-k\). Zero common radical forces \(k=5\), hence
\(L=a\wedge V^*\). Finally the affine hyperplane

\[
\mathcal A=\{v\in V:a(v)=1\}
\]

has 32 elements and is a clique. For distinct \(v,w\in\mathcal A\), choose
\(b\in V^*\) with \(b(v+w)=1\); then

\[
(a\wedge b)(v,w)=b(v)+b(w)=1.
\]

This proves every assertion. \(\square\)

The one-dimensional all-rank-two case is included: its common radical has
dimension four, so it never satisfies the exact-center condition.

## 5. Classification at cutoff seven for the quotient \(C_2^6\)

### Theorem H7.7 [PROVED]

Let \(L\le\bigwedge^2(\mathbb F_2^6)^*\) have zero common radical. If

\[
\omega(\Delta(L))\le7,
\]

then \(L\) is one-dimensional and generated by a nondegenerate alternating
form. Consequently

\[
\omega(\Delta(L))=7,\qquad \chi(\Delta(L))=9.
\tag{H7.18}
\]

This is a computer-assisted proof: the rank-six and rank-four pencil lemmas
are the finite certified inputs, while all reductions and the all-rank-two
branch are proved above.

**Proof.** If \(L\) contains a rank-six form, Consequence H7.3 says that it
is one-dimensional. If it contains no rank-six form but contains a
rank-four form, Consequence H7.5 contradicts zero common radical. If every
nonzero member has rank two, Lemma H7.6 gives a 32-clique. Thus only the
first case remains, and its generator is nondegenerate because the common
radical is zero.

For a nondegenerate scalar alternating form on \(\mathbb F_2^6\), a
pairwise nonorthogonal set of size \(r\) has Gram matrix with zero diagonal
and one off the diagonal. This matrix has rank \(r\) for even \(r\) and
\(r-1\) for odd \(r\), so \(r\le7\). Conversely the size-six matrix is
nondegenerate alternating and hence isometric to the given form; six basis
vectors with that Gram matrix, together with their sum, give a seven-clique.

For the chromatic number, every independent set spans a totally isotropic
subspace of dimension at most three. A color class therefore contains at
most seven nonzero vectors. The 63 nonzero vectors require at least nine
colors. A symplectic spread of nine three-dimensional totally isotropic
subspaces partitions the 63 nonzero vectors and gives nine colors. One
explicit construction identifies \(V\) with \(\mathbb F_8^2\) and takes the
nine one-dimensional \(\mathbb F_8\)-subspaces; the trace symplectic form
makes them totally isotropic. To spell out the identification, the form

\[
((u,v),(u',v'))\longmapsto
\operatorname{Tr}_{\mathbb F_8/\mathbb F_2}(uv'-u'v)
\]

is nondegenerate: if, for example, \(u\ne0\), choose \(t\) of nonzero trace
and take \(v'=u^{-1}t\). Every nondegenerate alternating form of the same
dimension has a symplectic basis and is therefore isometric to this one.
Thus \((\omega,\chi)=(7,9)\). \(\square\)

### Corollary H7.8 [PROVED]

If \(G/Z(G)\cong C_2^6\) and \(\nu(G)\le7\), then

\[
(\nu(G),a(G))=(7,9).
\]

**Proof.** Proposition H7.1 supplies a zero-common-radical \(L\), Theorem
H7.7 gives (H7.18), and (H7.4) transfers the two graph invariants back to
\(G\). \(\square\)

The binary scalar symplectic group \(S(2,3)\), equivalently the usual
extraspecial binary example \(E_3\), realizes this case. It also shows why a
claim that every zero-radical \(L\le\operatorname{Alt}(6,2)\) has an
eight-clique would be false: the one-dimensional nondegenerate space has
clique number seven.

## 6. The quotient \(C_4\times C_2^4\) cannot occur

The other large order-64 exterior-square obstruction is eliminated without
computation.

### Proposition H7.9 [PROVED]

No group \(G\) satisfies

\[
G/Z(G)\cong C_4\times C_2^4.
\]

**Proof.** Suppose otherwise, and choose \(x\in G\) whose central coset
\(xZ(G)\) generates the \(C_4\)-factor. Since the quotient is abelian, \(G\)
has class at most two. For arbitrary \(y\in G\), write

\[
yZ(G)=(xZ(G))^j\,uZ(G)
\]

with \(uZ(G)\) in the elementary abelian direct factor. Replacing \(u\) by
a representative, \(u^2\in Z(G)\). Central factors do not affect
commutators, and the class-two identities give

\[
[x^2,y]=[x,y]^2=[x,u]^2=[x,u^2]=1.
\]

Thus \(x^2\in Z(G)\). But \(x^2Z(G)=2(xZ(G))\) is the nonidentity element of
the order-two subgroup of the \(C_4\)-factor, a contradiction. \(\square\)

In exterior-square language, the same obstruction says that the nonzero
element \(2q\in C_4\times C_2^4\) lies in the radical of every possible
central-extension commutator pairing. The direct group proof above also
covers arbitrary, possibly infinite, \(G\).

## 7. Universal reduction to 738 finite exterior-square graphs

The preceding special arguments become a complete proof only after checking
that every possible center quotient has been included.  We give that bridge
in full, including the one-way obstruction used to remove most of the
difficult order-64 tail.

### Proposition H7.10 [PROVED]

If \(G\) is an arbitrary group with \(\nu(G)=7\), then

\[
Q=G/Z(G)\quad\text{is finite and}\quad |Q|\le81.
\tag{H7.19}
\]

**Proof.** The repository's self-contained conjugacy-class argument gives

\[
[G:Z(G)]\le(4\nu(G)^2)^{\nu(G)},
\]

so \(Q=G/Z(G)\) is finite before the external cover theorem is used.  Let
\(x_1,\ldots,x_7\) be a maximum pairwise noncommuting set.  The seven
centralizers \(C_G(x_i)\) cover \(G\), since an element outside
their union could be adjoined to the set.  The cover is irredundant because
\(x_i\notin C_G(x_j)\) for \(i\ne j\).  Its intersection is exactly
\(Z(G)\).  Indeed, if a noncentral \(y\) lay in the intersection, then all
seven \(x_i\) would lie in \(C_G(y)\), whereas repository Lemma CB.2 gives

\[
\nu(C_G(y))\le \nu(G)-2=5.
\]

Because each centralizer contains \(Z(G)\), their images in the finite group
\(Q\) form an irredundant seven-subgroup cover with trivial intersection.
Abdollahi--Jafarian Amiri, Theorem B (printed p. 292, proof pp. 299--300),
proves \(f(7)=81\): the intersection of an irredundant seven-subgroup cover
has index at most 81.  This is the load-bearing `[CITED-VERIFIED]` input.
Applying it inside \(Q\) gives \(|Q|\le81\).  Thus no question about the
source theorem's infinite-group scope enters the argument. \(\square\)

### Proposition H7.11 [PROVED]

Let \(Q\) be finite and let

\[
1\longrightarrow A\longrightarrow G\longrightarrow Q\longrightarrow1
\]

be a central extension.  There is a \(Q\)-equivariant homomorphism

\[
\kappa_G:Q\wedge Q\longrightarrow G',\qquad
q\wedge r\longmapsto[\widehat q,\widehat r].
\tag{H7.20}
\]

For \(K=\ker\kappa_G\), put \(q\sim_K r\) when \(q\ne r\) and
\(q\wedge r\notin K\).  This is exactly the noncommuting graph of \(G\)
compressed by its central cosets when \(Q=G/Z(G)\).  In that exact-center
case its radical is \(\{1\}\), and

\[
\nu(G)=\omega(\Delta_K),\qquad a(G)=\chi(\Delta_K).
\tag{H7.21}
\]

If \(S\twoheadrightarrow Q\) is one fixed Schur cover, then the
Brown--Johnson--Robertson isomorphism \(Q\wedge Q\cong S'\) transports
\(K\) to an \(S\)-normal subgroup of \(S'\).  Thus enumerating all such
normal subgroups is a safe exhaustive overcount of the possible graphs.

**Proof.** Lift-independence in (H7.20) follows because \(A\) is central.
Brown--Johnson--Robertson, Proposition 7 (printed p. 182), gives the
universal exterior-pairing factorization, and their Corollary 2 (printed
pp. 182--183) identifies the exterior square with the derived subgroup of a
Schur cover for finite \(Q\).  Equivariance makes the kernel normal.  The
edge equivalence follows directly from (H7.20).

If a vertex \(q=xZ(G)\) has no incident edge, then \(x\) commutes with every
element of \(G\), so \(q=1\); the converse is immediate.  Finally, one
representative per central coset preserves both directions of commutation.
A graph color class is a pairwise commuting set of cosets; the subgroup
generated by \(Z(G)\) and one representative of each of those cosets is
abelian and contains every element in the colored cosets.  Conversely the
images of the members of an abelian-subgroup cover are independent sets and
therefore give a coloring.  This proves (H7.21).
Enumerating all normal kernels can include kernels not realized by a central
extension, but such overcounting is harmless for a universal upper bound.
No homomorphism \(S\to G\), and no assertion \(G\cong S/K\), is used.
\(\square\)

### Lemma H7.12 (exterior-central obstruction) [PROVED]

Suppose \(1\ne q\in Q\) and

\[
q\wedge r=1\qquad\text{for every }r\in Q.
\tag{H7.22}
\]

Then no group has exact center quotient \(G/Z(G)\cong Q\).

**Proof.** In any central extension of \(Q\), (H7.20) sends (H7.22) to
\([\widehat q,\widehat r]=1\) for every \(r\).  Hence every lift of \(q\)
commutes with all of \(G\).  If the extension were the defining extension
of \(G/Z(G)\), this would force \(q=1\), a contradiction. \(\square\)

The lemma is deliberately one-way.  The proof below needs neither a general
criterion for capable groups nor an identification of an abstract
``epicentre''.  It needs only the explicitly certified zero exterior rows.

## 8. The ordinary bounded batches [COMPUTED]

GAP 4.16.0 with SmallGrp 1.5.4 gives exactly 738 isomorphism types of groups
of order at most 81.  The inventory
`experiments/logs/h7_quotient_inventory.json` checks the complete
SmallGroups serial range at every order.  Five bounded exports then scan 660
quotient types by Proposition H7.11:

| quotient range | types scanned | normal kernels | nonfaithful | eight-clique | exact candidates |
|:---|---:|---:|---:|---:|---:|
| orders 1--36, except \((32,51)\) | 161 | 23,527 | 18,231 | 4,979 | 317 |
| orders 37--63 | 157 | 9,657 | 6,724 | 2,933 | 0 |
| order 64, IDs 1--191 | 191 | 12,602 | 8,606 | 3,996 | 0 |
| orders 65--80 | 137 | 9,816 | 6,932 | 2,884 | 0 |
| order 81, except \((81,15)\) | 14 | 368 | 171 | 197 | 0 |
| **total** | **660** | **55,970** | **40,664** | **14,989** | **317** |

Every radical witness and every eight-clique is reparsed and checked.  The
317 remaining graphs are solved exactly, with record distribution

\[
\begin{array}{c|rrrrrr}
(\omega,\chi)&(1,1)&(3,3)&(4,4)&(5,5)&(6,6)&(7,7)\\ \hline
\text{records}&1&1&2&93&217&3.
\end{array}
\tag{H7.23}
\]

In particular every faithful graph in these batches with clique number at
most seven is 7-colorable.  The five aggregate certificates are
`experiments/logs/h7_exterior_1_36.json`,
`experiments/logs/h7_exterior_37_63.json`,
`experiments/logs/h7_exterior_64_1_191.json`,
`experiments/logs/h7_exterior_65_80.json`, and
`experiments/logs/h7_exterior_81.json`.  They check complete
kernel serial ranges against the 738-type inventory and report no failure.

The two deliberately delegated quotients outside those 660 types are

\[
\operatorname{SmallGroup}(32,51)=C_2^5,\qquad
\operatorname{SmallGroup}(81,15)=C_3^4.
\]

Corollary H6.2 proves that every exact-center commutator map on \(C_2^5\)
has a nine-clique, so the first quotient is impossible at cutoff seven as
well as cutoff six.  The second is treated in Section 12 below.

## 9. The order-64 tail and explicit zero rows

The ordinary order-64 batch ends at ID 191.  The remaining 76 IDs,
192--267, are partitioned without overlap as follows:

- 62 types have an explicit nonidentity element satisfying (H7.22);
- eleven types are handled by the generic character-dual certificate;
- IDs 192, 261, and 267 have separate certificates or structural proofs.

### Proposition H7.13 [COMPUTED]

None of the following 62 groups can be an exact quotient by a center:

\[
\begin{split}
&194,196,197,198,199,200,201,204,205,206,208,209,210,212,213,214,215,\\
&217,218,219,220,221,222,223,224,225,227,228,229,230,231,232,233,234,235,\\
&237,238,239,240,241,243,244,245,246,247,248,249,251,252,253,254,255,256,\\
&257,258,259,260,262,263,264,265,266,
\end{split}
\tag{H7.24}
\]

where every number denotes \(\operatorname{SmallGroup}(64,\cdot)\).

The GAP producer chooses an injectively pc-converted 2-Schur cover, checks
that the cover kernel is central and contained in the derived subgroup,
checks that each saved lift maps to its stated quotient element, and exports
the full 64-entry exterior-commutator row of every saved witness.  The Python
verifier checks the quotient and cover pc-presentation shapes, the saved
quotient and lift exponent vectors, exponent ranges, and
cover/kernel/exterior orders against the independent inventory, and that
every entry of each saved
universal exterior row is zero.  Under the audited commutator-compatible
isomorphism \(Q\wedge Q\cong S'\), this says exactly that the saved
nonidentity \(q\) satisfies (H7.22).  Lemma H7.12 then excludes the quotient.

For the five types 262--266 the certificate makes the common witness
especially transparent: in each displayed pc presentation it is
\(q=g_6\), with exponent vector \((0,0,0,0,0,1)\).  It is nonidentity and
its lift commutes with every cover generator.  Thus these five formerly
borderline quotients are excluded by an explicit universal witness, not by
an unproved capability classification.  The direct argument of Proposition
H7.9 independently excludes ID 260 and is consistent with its zero-row
witness; ID 260 is counted only once in (H7.24).

The canonical data are
`experiments/configs/h7_capability_order64.g`, the two raw TSV batches
`experiments/logs/h7_capability_192_260.tsv` and
`experiments/logs/h7_capability_261_267.tsv`, and the independently verified aggregate
`experiments/logs/h7_capability_order64.json`.

## 10. Character-annihilator duality

The remaining large exterior squares are scanned on the dual side.  We
record why this loses no kernels.

### Lemma H7.14 [PROVED]

Let \(E=Q\wedge Q\) be finite abelian, let
\(E^*=\operatorname{Hom}(E,\mathbb Q/\mathbb Z)\), and let \(K\le E\).
Define

\[
L=K^\perp=\{\lambda\in E^*: \lambda(K)=0\}.
\tag{H7.25}
\]

Then \(K\mapsto K^\perp\) is an inclusion-reversing bijection between
subgroups of \(E\) and subgroups of \(E^*\), with inverse
\(L\mapsto L^\perp\).  It is equivariant for the natural contragredient
action, so \(K\) is action invariant if and only if \(L\) is.  Moreover

\[
q\wedge r\notin K
\quad\Longleftrightarrow\quad
\lambda(q\wedge r)\ne0\text{ for some }\lambda\in L.
\tag{H7.26}
\]

Thus the graph of \(K\) is the union of the scalar graphs attached to the
characters in \(L\).  If this union has no eight-clique, every scalar graph
occurring in it has no eight-clique.

**Proof.** Characters of a finite abelian group separate cosets of every
subgroup, which gives \(K^{\perp\perp}=K\) and (H7.26).  Pullback under an
automorphism gives the action assertion.  The last sentence is ordinary
subgraph monotonicity. \(\square\)

### Proposition H7.15 [COMPUTED]

For the eleven IDs

\[
193,195,202,203,207,211,216,226,236,242,250,
\tag{H7.27}
\]

every action-invariant \(L\le (Q\wedge Q)^*\) whose union graph has no
eight-clique has a nonidentity radical vertex.  Hence none yields an exact
center quotient at cutoff seven.

The canonical GAP export records all \(64^2\) lifted commutators, the full
cover-conjugation action on \(Q\wedge Q\), and quotient automorphism
generators.  The standard-library verifier checks skew symmetry, generation
of the exterior square, bijectivity of every action, and transport of every
commutator.  It first classifies every scalar character exactly.  Starting
from the trivial subgroup, a breadth-first search adjoins each remaining
scalar-good character and takes its complete action-invariant closure.  A
child containing a scalar-bad character is already excluded by
monotonicity; a child whose union graph has an eight-clique is saved as a
verified boundary record; every other child is retained.  No quotient by
automorphisms is used in this load-bearing BFS.

Completeness follows by induction inside any target invariant subgroup
\(L\) whose union graph has no eight-clique.  If the search has reached a
proper invariant \(H<L\), choose \(\lambda\in L\setminus H\).  Because
\(L\) is invariant, the invariant closure of
\(H+\langle\lambda\rangle\) is still contained in \(L\).  Every one of its
characters is scalar-good, and its graph is a subgraph of the graph of
\(L\), so this child can be omitted neither by the scalar-bad test nor by an
eight-clique boundary.  Repeating reaches \(L\).  Hence every possible
no-eight target occurs among the retained records.

| ID | \(|E^*|\) | scalar-good characters (including zero) | retained no-eight \(L\)'s |
|---:|---:|---:|---:|
| 193 | 256 | 192 | 498 |
| 195 | 128 | 64 | 450 |
| 202 | 512 | 224 | 498 |
| 203 | 256 | 128 | 482 |
| 207 | 256 | 96 | 466 |
| 211 | 512 | 288 | 498 |
| 216 | 256 | 96 | 466 |
| 226 | 256 | 128 | 482 |
| 236 | 128 | 64 | 450 |
| 242 | 256 | 64 | 450 |
| 250 | 256 | 96 | 466 |

All 5,206 retained subgroups have radical size at least four, and there are
zero faithful candidates.  This includes ID 250, whose exterior square is
\(C_8\times C_2^5\); the verifier evaluates all characters in the common
target \(\mathbb Z/8\mathbb Z\), so no exponent-four reduction is being
assumed.  The complete aggregate is
`experiments/logs/h7_order64_dual.json`, produced by
`src/python/h7_order64_dual.py` from the eleven canonical raw exports
`experiments/logs/h7_order64_dual_{ID}.tsv`.

## 11. The two remaining special order-64 certificates

### Proposition H7.16 (ID 192) [COMPUTED]

Let \(Q=C_4^2\times C_2^2=\operatorname{SmallGroup}(64,192)\).  Then no
faithful exterior-kernel graph on \(Q\) has clique number at most seven.

Here \(E=Q\wedge Q\cong C_4\times C_2^5\).  Every subgroup is listed once
by its projection to the \(C_4\)-factor:

\[
0\times N,\qquad
(0\times N)+\langle(2,u)\rangle,\qquad
(0\times N)+\langle(1,u)\rangle,
\tag{H7.28}
\]

where \(N\le\mathbb F_2^5\), and in the last two cases \(u\) runs through
\(\mathbb F_2^5/N\).  The RREF/coset enumeration gives all 5,276 subgroups
exactly once.  Of them 2,925 have nontrivial radical, while all 2,351
faithful cases have saved verified eight-cliques.  The producer is
`src/python/h7_c4_2_c2_2.py` and the complete certificate is
`experiments/logs/h7_c4_2_c2_2.json`.

### Proposition H7.17 (ID 261) [COMPUTED]

Let

\[
Q=C_2^3\times D_8=\operatorname{SmallGroup}(64,261).
\]

Then no faithful exterior-kernel graph on \(Q\) has clique number at most
seven.

**Completeness reduction.** The chosen Schur cover gives

\[
E=Q\wedge Q\cong C_2^9\times C_4,
\tag{H7.29}
\]

and hence \(E^*\cong C_2^9\times C_4\).  The export contains 16 cover
conjugations and the complete \(64\times64\) exterior commutator table.  The
verifier checks that the commutators generate all 2,048 elements of \(E\)
and that each action transports every table entry.

Among all 2,048 characters, exactly 896 scalar graphs have an eight-clique.
The other 1,152 characters, including zero, have exact scalar clique-number
distribution

\[
155\text{ of }\omega=3,\qquad
884\text{ of }\omega=5,\qquad
112\text{ of }\omega=6,
\tag{H7.30}
\]

together with the zero character.  Write \(H\cong\mathbb F_2^{10}\) for
the 1,024 even characters.  The complete scalar-good set has the affine
form

\[
H\ \cup\ (x+U),
\tag{H7.31}
\]

where \(U\le H\) has dimension seven, the odd coset \(x+U\) has 128
elements, and

\[
d=2x\ne0,\qquad d\in U.
\tag{H7.32}
\]

These assertions are not inferred from counts: the saved RREF bases verify
equality of the two sets.

Let \(L\le E^*\) be a scalar-good subgroup containing an odd character
\(y=x+u\).  Put \(M=L\cap H\).  Since \(2y=d\), subgroup closure gives
\(\langle d\rangle\le M\).  For each \(m\in M\), both \(y\) and
\(y+m\) are odd members of \(L\), hence by (H7.31) both lie in the affine
coset \(x+U\).  Their difference is \(m\in U\), proving \(M\le U\).
Conversely, every choice

\[
\langle d\rangle\le M\le U,\qquad y\in x+U\pmod M
\tag{H7.33}
\]

gives the subgroup \(L=M\cup(y+M)\), and (H7.33) is unique.  On passing to
the six-dimensional quotient \(U/\langle d\rangle\), the exact number is

\[
\sum_{r=0}^{6}{6\brack r}_2\,2^{6-r}
=64+2016+10416+11160+2604+126+1
=26{,}387.
\tag{H7.34}
\]

The RREF/coset loop enumerates these 26,387 subgroups injectively and checks
that every one is invariant under all 16 actions.  Of them 26,323 have a
saved verified eight-clique; each of the remaining 64 has a saved nontrivial
radical.  There is no faithful candidate.

It remains to justify that no all-even \(L\le H\) was lost.  This requires
more than observing that all even characters annihilate a nonzero element
of \(E\).  The certificate stores the nonidentity quotient vertex 6, with
nonzero pc exponent vector, and verifies its entire commutator row to be

\[
\{0,2e_{10}\}.
\tag{H7.35}
\]

Every even character annihilates \(2e_{10}\).  Therefore vertex 6 is in the
radical of the union graph of every all-even \(L\), so none has the exact
center property.  This completes both parity branches.

The canonical chain is
`experiments/configs/h7_c2_3_d8_export.g`,
`experiments/logs/h7_c2_3_d8.tsv`,
`src/python/h7_c2_3_d8.py`, and
`experiments/logs/h7_c2_3_d8.json`.  An independent full rerun reproduced
the JSON exactly and rechecked every action and every commutator table entry.

ID 267 is \(C_2^6\), already disposed of by Theorem H7.7: its only faithful
graph at cutoff seven is the scalar symplectic graph, with
\((\omega,\chi)=(7,9)\).

## 12. The delegated quotient \(C_3^4\)

### Proposition H7.18 [COMPUTED]

Let \(Q=C_3^4=\operatorname{SmallGroup}(81,15)\).  Every faithful central
extension graph with clique number at most seven has chromatic number ten.
Indeed, up to \(\operatorname{GL}(4,3)\) there is exactly one eligible
commutator-form space, and it has

\[
(\omega,\chi)=(7,10).
\tag{H7.36}
\]

The verifier enumerates all 56,632 subspaces of the six-dimensional space
\(\operatorname{Alt}(4,3)\).  It finds 691 with nonzero common radical and
55,941 faithful subspaces.  The latter split into 16 checked
\(\operatorname{GL}(4,3)\)-orbits whose sizes sum to 55,941.  Exact clique
and coloring calculations on every representative leave one eligible orbit,
of size 234, with (H7.36); all other orbit representatives have clique
number at least ten.

The calculation uses the 40 projective points of \(\mathbb F_3^4\).  This
compression preserves both invariants: zero is isolated, and the two
nonzero vectors on each one-dimensional \(\mathbb F_3\)-line are independent
twins because multiplying by a nonzero scalar preserves whether an
alternating-form value is zero.  Therefore the exact values on the
40-vertex projective graph equal those on the full 81-coset graph.  The
producer and certificate are `src/python/h7_c3_4.py` and
`experiments/logs/h7_c3_4.json`.

## 13. Exact value of \(h(7)\)

### Theorem H7.19 [PROVED] (computer-assisted)

\[
h(7)=10.
\]

The upper bound uses the primary-source input \(f(7)=81\) marked
`[CITED-VERIFIED]`; all finite classifications and graph searches used after
that reduction are exact repository computations marked `[COMPUTED]`.

**Proof.** Let \(G\) satisfy \(\nu(G)\le7\).  If \(\nu(G)\le6\), Theorem
H6.3 gives \(a(G)\le6\).  Otherwise \(\nu(G)=7\), and Proposition H7.10
gives the finite center quotient \(Q=G/Z(G)\) of order at most 81.
Proposition H7.11 places its compressed graph among the exterior-kernel
graphs considered above and gives \(a(G)=\chi(\Delta_G)\).

The complete inventory has 738 quotient types, partitioned as

\[
660+2+62+11+3=738.
\tag{H7.37}
\]

The first 660 are the ordinary bounded batches of Section 8 and are in fact
7-colorable at cutoff seven.  The two batch delegations are \(C_2^5\),
which has a nine-clique in every exact-center realization, and \(C_3^4\),
which is 10-colorable by Proposition H7.18.  The 62 explicit exterior-zero
rows are impossible exact center quotients by Lemma H7.12.  The eleven
generic dual cases have no faithful graph at cutoff seven by Proposition
H7.15.  Of the final three cases, ID 192 has no faithful graph at cutoff
seven by Proposition H7.16, ID 261 has none by Proposition H7.17, and ID
267 is 9-colorable by Theorem H7.7.  These disjoint cases exhaust the
inventory, so \(a(G)\le10\).  Hence \(h(7)\le10\).

For the reverse inequality, Theorem CB.1 constructs the order-\(3^5\)
Heisenberg group \(S(3,2)\) and proves, without computational dependence,

\[
\nu(S(3,2))=7,
\qquad
a(S(3,2))=10.
\]

Thus \(h(7)\ge10\), completing the equality. \(\square\)

### Exhaustion audit [PROVED]

The arithmetic in (H7.37) is also checked against the five inventory bands:

\[
162+157+267+137+15=738.
\]

Within the order-64 band, IDs 1--191 occur in the ordinary batch and IDs
192--267 occur exactly once among the 62 zero-row exclusions, eleven generic
dual cases, and three specials.  No partial exploratory scan is used as a
load-bearing input.  All arguments apply to arbitrary original groups:
only the finite quotient \(G/Z(G)\) and its finite exterior square enter the
enumeration.
