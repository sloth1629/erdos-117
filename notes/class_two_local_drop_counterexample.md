# A class-two counterexample to linear local drop

Write \(\nu(G)\) for the largest size of a pairwise noncommuting subset of
\(G\).

## The group

[DISPROVED] Even for finite class-two \(2\)-groups, neither of the local
inequalities

\[
 [P:C_P(x)]\leq \nu(P)-\nu(C_P(x))
 \tag{LD.1}
\]

nor

\[
 [P:C_P(x)]\leq \nu(P)-\nu(C_P(x))+1
 \tag{LD.2}
\]

is valid.

Here is an explicit counterexample.  Put \(V=\mathbf F_2^5\), with ordered
basis \(e_0,\ldots,e_4\), and put \(W=\mathbf F_2^4\), with basis indexed by

\[
 E=((0,2),(0,4),(1,4),(3,4)).
\]

For \(u,v\in V\), define the normalized bilinear cocycle

\[
 c(u,v)=\sum_{(i,j)\in E}u_jv_i z_{ij}.
\]

On the set \(P=V\times W\), define

\[
 (u,s)(v,t)=(u+v,\ s+t+c(u,v)).
 \tag{LD.3}
\]

Bilinearity gives the cocycle identity, so (LD.3) is associative.  Its
commutator map is

\[
 \begin{aligned}
 \beta(u,v)&=c(u,v)+c(v,u)\\
 &=\bigl(
 u_0v_2+u_2v_0,
 u_0v_4+u_4v_0,
 u_1v_4+u_4v_1,
 u_3v_4+u_4v_3
 \bigr).
 \tag{LD.4}
 \end{aligned}
\]

Equivalently, \(P\) has generators
\(a_0,\ldots,a_4,z_{02},z_{04},z_{14},z_{34}\), all of order two, with the
\(z_{ij}\) central, with

\[
 [a_0,a_2]=z_{02},\quad [a_0,a_4]=z_{04},\quad
 [a_1,a_4]=z_{14},\quad [a_3,a_4]=z_{34},
 \tag{LD.5}
\]

and with all other basic commutators trivial.  The relations collect every
word to one of at most \(2^5 2^4\) normal forms, while the tuple model realizes
all \(2^5 2^4=512\) such forms.  Thus the presentation is consistent and has
exactly \(512\) elements.
The radical of \(\beta\) is zero: its four coordinates successively force
all five coordinates of a radical vector to vanish.  Hence

\[
 Z(P)=\{0\}\times W,\qquad |Z(P)|=16,
\]

and \(P\) has nilpotency class exactly two.

Take

\[
 x=(e_0+e_4,0).
\]

For clarity, this lift has \(x^2=(0,z_{04})\) and hence order four; the
counterexample does not require \(x\) to be an involution.

For \(y=(y_0,\ldots,y_4)\), formula (LD.4) gives

\[
 \beta(e_0+e_4,y)=(y_2,y_0+y_4,y_1,y_3).
\]

Thus its kernel is \(\{0,e_0+e_4\}\), and consequently

\[
 |C_P(x)|=2|W|=32,\qquad [P:C_P(x)]=16.
 \tag{LD.6}
\]

The restriction of \(\beta\) to that two-element kernel is zero, so
\(C_P(x)\) is abelian and \(\nu(C_P(x))=1\).

## Exact clique and coloring certificates

Identify \(v=(v_0,\ldots,v_4)\in V\) with the integer
\(\sum_i v_i2^i\).  Commutation in \(P\) depends only on the two projected
vectors in \(V\), and two elements in the same central coset commute.  The
following is a \(15\)-clique in the compressed graph:

\[
 \begin{aligned}
 F={}&\{v:v_4=1\text{ and }(v_2=0\text{ or }v_0=1)\}\\
    &\mathbin{\cup}\{e_1+e_2,e_0,e_0+e_2\}\\
 ={}&\{1,5,6,16,17,18,19,21,23,24,25,26,27,29,31\}.
 \tag{LD.7}
 \end{aligned}
\]

For two distinct vectors in the first set, a difference in coordinate
\(0\), \(1\), or \(3\) is witnessed by the corresponding edge to coordinate
\(4\).  If those coordinates agree, the vectors differ in coordinate \(2\);
admissibility then makes the \((0,2)\) coordinate of \(\beta\) nonzero.  The
three added vectors meet the first set through coordinate \((1,4)\) or
\((0,4)\), and meet each other through coordinate \((0,2)\).  Hence every
two members of \(F\) fail to commute.

Here is a partition of all \(32\) vectors into \(15\) commuting classes:

\[
 \begin{array}{llll}
 \{0,17\},&\{19\},&\{21\},&\{23\},\\
 \{25\},&\{27\},&\{29\},&\{31\},\\
 \{4,16,20\},&\{18,22\},&\{24,28\},&\{26,30\},\\
 \{1,2,3,8,9,10,11\},&\{5,7,13,15\},&\{6,12,14\}.
 \end{array}
 \tag{LD.8}
\]

The seven singleton classes need no check.  For the remaining classes:

- \(\{4,16,20\}=\langle e_2,e_4\rangle\setminus\{0\}\) is isotropic;
- the next three pairs have the form \(\{u,u+e_2\}\), where
  \(u\in\{e_1+e_4,e_3+e_4,e_1+e_3+e_4\}\), and \(e_2\) pairs only with
  the absent coordinate \(e_0\);
- \(\{1,2,3,8,9,10,11\}=\langle e_0,e_1,e_3\rangle\setminus\{0\}\) is
  isotropic;
- \(\{5,7,13,15\}=e_0+e_2+\langle e_1,e_3\rangle\), whose pairwise
  differences are orthogonal to the base point and to one another; and
- \(\{6,12,14\}\) lies in the isotropic space
  \(\langle e_1,e_2,e_3\rangle\).

Thus every displayed class is pairwise commuting.  Their sizes are

\[
 2,1,1,1,1,1,1,1,3,2,2,2,7,4,3,
\]

which sum to \(32\); the displayed integers are distinct and cover
\(0,\ldots,31\).  Each class contains exactly one member of \(F\).  Thus
(LD.8) is a proper \(15\)-coloring of the noncommuting graph, while (LD.7)
is a \(15\)-clique.  Lifting each class \(D\subseteq V\) to
\(D\times W\) gives a pairwise commuting subset, and these lifted classes
partition \(P\).  Therefore

\[
 \nu(P)=15.
 \tag{LD.9}
\]

Combining (LD.6) and (LD.9) gives

\[
 16>15-1+1=15>15-1=14,
\]

which disproves both (LD.1) and (LD.2).

## A failed surjectivity shortcut

[DISPROVED] It is not true that, for every maximum clique
\(Y=\{a_1,\ldots,a_r\}\) in \(C_P(x)\), one has

\[
 P=C_P(x)\left(\bigcap_{i=1}^r C_P(a_i)\right).
 \tag{LD.10}
\]

In the example above, \(C_P(x)\) is abelian, so \(Y=\{x\}\) is a maximum
clique.  But then the intersection in (LD.10) is \(C_P(x)\), and the
right-hand side is the proper subgroup \(C_P(x)\) of order \(32\).  This
rules out the unconditional surjectivity step; it does not rule out a more
careful existential choice of a clique in special cases.

## The surviving local candidate

[UNVERIFIED] The weaker quadratic drop-sensitive inequality

\[
 [P:C_P(x)]
 \leq 4\bigl(\nu(P)-\nu(C_P(x))+1\bigr)^2
 \tag{LD.11}
\]

has neither been proved nor refuted.  The present example satisfies it and
therefore supplies no evidence beyond eliminating the two linear versions.

## [COMPUTED] Independent finite check

The proof above uses explicit witnesses rather than an optimizer.  The
dependency-free verifier independently checks the cocycle identity, the
presentation data, the center and centralizer inside all \(512\) tuples, all
\(105\) clique pairs, and every pair in every coloring class:

```bash
PYTHONPYCACHEPREFIX=/tmp/erdos117-class2-local-pycache \
python3 src/verification/verify_class_two_local_drop_counterexample.py

PYTHONPYCACHEPREFIX=/tmp/erdos117-class2-local-test-pycache \
python3 -m unittest \
  src.verification.test_class_two_local_drop_counterexample -v
```
