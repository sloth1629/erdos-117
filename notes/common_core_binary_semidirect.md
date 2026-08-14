# The binary Frattini residual is a \(C_3\)-by-\(2\) group

## [PROVED] Input and sharper conclusion

Assume the proved reduction in
notes/common_core_frattini_reduction.md, at frozen SHA-256
951a907c096e4a68b7dcc850954db04c051ea5fd7eeb3f830cd9fc1a1f92c4c6.
Thus a hypothetical unresolved finite solvable nonnilpotent exact quotient
\(Q=G/Z(G)\), with \(\nu(G)=8\) and \(a(G)>10\), satisfies

\[
1\ne P=\Phi(Q),\qquad
P\text{ is a }2\text{-group},\qquad
Q/P\cong C_2^a\times C_3^b\times S_3.
\tag{BS.1}
\]

Every minimal \(Q\)-normal subgroup in \(P\) is central of order two.
This note sharpens (BS.1) to

\[
\boxed{
Q\cong C_3\rtimes_\chi S,\qquad
\chi:S\twoheadrightarrow C_2,\qquad
\Phi(Q)=\Phi(S)=P\ne1,
}
\tag{BS.2}
\]

where \(S\) is a finite \(2\)-group and \(\chi\) acts by inversion on
\(C_3\). Moreover

\[
Q/P\cong C_2^a\times S_3,\qquad
|S|\le8192.
\tag{BS.3}
\]

Consequently every abelian common-core quotient from (CF.1) of the frozen
note is binary, and its exact possibilities are

\[
C_2^2,\qquad C_2^4,\qquad C_2^6.
\tag{BS.4}
\]

No exact commutator pairing is descended through \(Q\to Q/P\).

## [PROVED] Every chief factor inside \(P\) is central

Refine \(P\) to a \(Q\)-chief series

\[
1=P_0<P_1<\cdots<P_t=P.
\]

For each \(j\), the factor \(U=P_j/P_{j-1}\) lies in the center of the
nilpotent normal group \(P/P_{j-1}\). Indeed, a nontrivial normal subgroup
of a finite \(2\)-group meets its center, and minimal
\(Q/P_{j-1}\)-normality then gives all of \(U\).

Suppose \(U\) were noncentral in \(Q/P_{j-1}\). The complement-free affine
lemma (CF.6) says

\[
U\cong C_2^2,\qquad
(Q/P_{j-1})/C_{Q/P_{j-1}}(U)\cong C_3.
\tag{BS.5}
\]

Since \(P/P_{j-1}\) centralizes \(U\), the action in (BS.5) factors through
(BS.1). Every homomorphism

\[
C_2^a\times C_3^b\times S_3\longrightarrow C_3
\]

kills \(C_2^a\) and \(S_3\), so some element \(c\) of the central
\(C_3^b\)-factor acts nontrivially. Take a four-clique
\(y_1,\ldots,y_4\) in \(S_3\). The four quotient elements
\(cy_1,\ldots,cy_4\) remain pairwise noncommuting, and all act
fixed-point-freely on \(U\). Each corresponding \(U\)-coset contains a
four-clique, and the four fiber cliques are completely joined because their
images are already noncommuting. This gives a \(16\)-clique in
\(Q/P_{j-1}\). It lifts to a \(16\)-clique in \(Q\), contradicting
\(\nu(Q)\le\nu(G)=8\).

Therefore

\[
P_j/P_{j-1}\le Z(Q/P_{j-1})
\qquad(1\le j\le t).
\tag{BS.6}
\]

## [PROVED] Odd-order conjugation centralizes \(P\)

Let \(\mathcal A\le\operatorname {Aut}(P)\) stabilize the series above and
act trivially on every order-two factor. Then \(\mathcal A\) is a
\(2\)-group. A short induction proves this. Pass to \(P/P_1\) and use the
induction hypothesis. An automorphism in the remaining kernel is the
identity on \(P_1\) and modulo \(P_1\); since \(P_1\le Z(P)\), it has the
form

\[
x\longmapsto x\,\delta(x),
\qquad
\delta:P/P_1\longrightarrow P_1\cong C_2.
\]

This last kernel is an elementary abelian \(2\)-group. Iterating proves the
claim.

By (BS.6), the conjugation action on \(P\) of every odd-order subgroup of
\(Q\) lies in \(\mathcal A\). Its image has both odd order and
\(2\)-power order, and is therefore trivial:

\[
\boxed{\text{every odd-order subgroup of }Q\text{ centralizes }P.}
\tag{BS.7}
\]

## [PROVED] The factor \(C_3^b\) vanishes

Let

\[
\overline T=C_3^b\times A_3\cong C_3^{b+1}
\]

be the normal Sylow \(3\)-subgroup of \(Q/P\), and let \(N\) be its preimage
in \(Q\). Choose a Sylow \(3\)-subgroup \(T\) of \(N\). Since \(P\) is the
normal Sylow \(2\)-subgroup of \(N\),

\[
N=PT,\qquad P\cap T=1.
\]

Equation (BS.7) says that \(T\) centralizes \(P\). Hence

\[
N=P\times T.
\]

In particular \(T\) is the unique Sylow \(3\)-subgroup of \(N\), so it is
characteristic in the normal subgroup \(N\) and therefore normal in \(Q\).
Projection induces a \(Q\)-equivariant isomorphism

\[
T\xrightarrow{\;\sim\;}\overline T.
\tag{BS.8}
\]

Under (BS.8), the inverse image \(T_0\cong C_3^b\) of the central factor in
\(\overline T\) is central in \(Q\). If \(b>0\), it contains a central
minimal normal subgroup of order three. This contradicts the proved
central-layer forcing theorem (CF.18), which says that a central minimal
normal subgroup in the residual must have order two. Thus

\[
b=0,\qquad Q/P\cong C_2^a\times S_3.
\tag{BS.9}
\]

## [PROVED] Splitting and identifying the Frattini subgroup

Now \(T\cong C_3\) is the normal Sylow \(3\)-subgroup of \(Q\). Let \(S\)
be a Sylow \(2\)-subgroup. Order considerations give

\[
Q=T\rtimes S.
\]

The conjugation action \(S\to\operatorname {Aut}(T)\cong C_2\) is
surjective, since (BS.9) has an \(S_3\)-factor. Denote it by \(\chi\).

We next prove

\[
\Phi(Q)=\Phi(S).
\tag{BS.10}
\]

The normal \(2\)-subgroup \(P=\Phi(Q)\) lies in the Sylow \(2\)-subgroup
\(S\). Every maximal subgroup \(M<S\) has index two. The subgroup \(TM\)
therefore has index two in \(Q\) and is maximal. Thus \(P\le TM\), while
\(P\le S\), and the internal semidirect product gives \(TM\cap S=M\).
Consequently \(P\le M\) for every maximal \(M<S\), and hence

\[
P\le\Phi(S).
\tag{BS.11}
\]

Conversely, \(\Phi(S)\le\ker\chi\), because the kernel of the nontrivial
map \(\chi:S\to C_2\) is maximal. Thus \(\Phi(S)\) centralizes \(T\).
Let \(M\) be any maximal subgroup of \(Q\).

- If \(T\le M\), then \(M/T\) is maximal in \(Q/T\cong S\), so
  \(\Phi(S)\le M\).
- If \(T\nleq M\), maximality gives \(MT=Q\), while \(M\cap T=1\).
  Hence \(M\) is a Sylow \(2\)-subgroup and has the form \(S^t\) for some
  \(t\in T\). Since \(\Phi(S)\) centralizes \(T\), it lies in \(S^t=M\).

Thus \(\Phi(S)\) lies in every maximal subgroup of \(Q\), giving the reverse
inclusion in (BS.10). Equations (BS.9)--(BS.11) prove (BS.2).

## [PROVED] Explicit order and common-core bounds

Write \(|P|=2^s\), with \(s\ge1\). Since

\[
S/P\cong C_2^{a+1},
\]

one has

\[
|S|=2^{s+a+1}.
\]

The factorial center-index bound \(|Q|\le8!=40\,320\) now gives

\[
3|S|\le40\,320.
\]

The largest power of two satisfying this inequality is \(2^{13}=8192\);
this proves the order bound in (BS.3).

Finally, every maximal subgroup of \(Q\) contains \(P=\Phi(Q)\), so the
choice-dependent core \(R\) in (CF.1) contains \(P\). Hence \(Q/R\) is a
quotient of \(C_2^a\times S_3\). If it is abelian, the one-prime lemma
(CF.22) makes it elementary abelian. Its only possible prime is two,
because \(S_3\) has no nontrivial \(3\)-group quotient and the central
factor is binary. The binary private-vector argument (CF.23) then gives
exactly (BS.4).

If \(Q/R\) is nonabelian, the graph-of-a-normal-subgroup argument from the
frozen note gives

\[
Q/R\cong C_2^{a'}\times S_3
\qquad(0\le a'\le a).
\tag{BS.12}
\]

## [UNVERIFIED] Remaining endpoint

The problem is not yet closed. The exact remaining nonnilpotent data are

\[
Q=C_3\rtimes_\chi S,\qquad
1\ne\Phi(S)=\Phi(Q),\qquad |S|\le8192,
\tag{BS.13}
\]

where \(S\) is a finite \(2\)-group, \(\chi:S\twoheadrightarrow C_2\), and
the eight original exact clique-centralizers still cut
\(\Phi(S)\) in a cover with trivial intersection. The next step is to use
the \(2\)-group structure and the specified character to bound or color the
exact central-extension graph. No assertion that commutation descends or
lifts through \(Q\to Q/\Phi(Q)\) is made.
