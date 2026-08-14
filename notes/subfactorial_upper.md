# A CFSG-dependent subfactorial upper bound

This note replaces a false fixed-base route through the withdrawn
arXiv:2205.03389. That preprint is not used anywhere below.

## Primary inputs

### [CITED-VERIFIED] The BFC derived-subgroup bound

Guralnick--Maróti, *Average dimension of fixed point spaces with
applications*, *Advances in Mathematics* 226 (2011), 298--308, Theorem 1.8,
states that every \(b\)-BFC group with \(b>1\) satisfies

\[
 |G'|<b^{(7+\log_2 b)/2}.
\tag{SU.1}
\]

Here \(b\)-BFC means that every conjugacy class has size at most \(b\).
The authors explicitly state that this result depends on the Classification
of Finite Simple Groups through the cited Segal--Shalev work. We retain that
dependency rather than presenting (SU.1) as a CFSG-free theorem.

### [CITED-VERIFIED] The published abelian coset-cover bound

J. Nagy, P. P. Pach and I. Tomon, *Hyperplane covers of finite spaces and
applications*, *Transactions of the American Mathematical Society* 379
(2026), 137--156, Theorem 1.11 (author PDF p. 4, proof in Section 8,
pp. 14--16), proves that there is an absolute constant \(c_A>0\) such that
an irredundant \(k\)-coset cover, for \(k\ge2\),

\[
 A=\bigcup_{i=1}^k H_i x_i
\]

of an abelian group satisfies

\[
 \left[A:\bigcap_{i=1}^kH_i\right]
 \leq \exp\!\bigl(c_A k L(k)\bigr),
\tag{SU.2}
\]

where \(L(k)=\max\{1,\log\log k\}\).  A one-member cover has index one
and is trivial.  For \(k\ge3\), enlarging the absolute constant rewrites
this as the conventional \(\exp(O(k\log\log k))\) statement.
The source states the theorem for arbitrary abelian groups, invoking a
Neumann finiteness result before reducing finite abelian groups to
irredundant hyperplane covers of elementary abelian groups and then using a
quantitative arithmetic-set bound.  Our application first passes to the
repository's finite commutation model, so that external infinite-to-finite
step is not load-bearing here.

[PROVED] Two harmless source-level corrections were checked during the proof audit.
The final private witness in Lemma 5.4 is \((x_M,y_N)\), not the undefined
\((x_N,y_N)\). Also, denominators written as \(\log\log p\) must be
normalized for \(p=2,3\), for example by
\(\max\{1,\log\log p\}\); the elementary bound \(f_p(r)\geq r+1\)
absorbs those primes. Neither correction changes Theorem 1.11.

The authors' earlier arXiv:2111.13658 contains the same order of magnitude,
but the peer-reviewed theorem above is the load-bearing source. The distinct
arXiv:2205.03389 claimed \(2^{O(k)}\), was withdrawn after an error in its
main proof, and supplies no premise here.

## The derived center-index theorem

### [PROVED] Arbitrary-group upper bound

There is an absolute constant \(C>0\) such that every group \(G\) with
\(m=\nu(G)<\infty\) satisfies

\[
 [G:Z(G)]
 \leq \exp\!\bigl(Cm\log\log m\bigr)
 \qquad(m\geq3).
\tag{SU.3}
\]

Consequently,

\[
 h(n)\leq2^{O(n\log\log n)}.
\tag{SU.4}
\]

The constants are absolute, but the proof is CFSG-dependent through
(SU.1). In particular, (SU.3) is not a fixed-base \(c^m\) bound.

**Proof.** The exact finite commutation-model theorem first replaces an
arbitrary \(G\) by a finite group with the same central quotient, the same
\(\nu\), and the same \(a\). It is therefore enough to prove (SU.3) for
finite \(G\). The cases \(m\leq2\) are abelian, so assume \(m\geq3\).

The repository's self-contained conjugacy-class argument gives

\[
 b:=\max_{g\in G}|g^G|\leq4m^2.
\]

Put \(D=G'\), \(d=|D|\), \(C=C_G(D)\), and \(A=Z(C)\). From (SU.1),

\[
 d<b^{(7+\log_2b)/2}.
\tag{SU.5}
\]

Conjugation on \(D\) has kernel \(C\), so

\[
 [G:C]\leq|\operatorname{Aut}D|.
\]

Every finite group of order \(d\) has a generating set of size at most
\(\log_2d\): adjoining a genuinely new generator at least doubles the
generated subgroup. An automorphism is determined by the images of those
generators. Hence

\[
 [G:C]\leq d^{\log_2d}.
\tag{SU.6}
\]

Since \(C'\leq G'=D\), while \(C\) centralizes \(D\), one has

\[
 C'\leq Z(C)=A.
\tag{SU.7}
\]

Thus \(C/A\) is abelian. If \(C\) is nonabelian, choose a maximum
noncommuting set \(x_1,\ldots,x_k\) in \(C\), where \(k=\nu(C)\leq m\).
Its element centralizers form an irredundant subgroup cover

\[
 C=\bigcup_{i=1}^k C_C(x_i),
 \qquad
 \bigcap_{i=1}^k C_C(x_i)=Z(C)=A.
\]

After quotienting by \(A\), this is an irredundant coset cover of the
abelian group \(C/A\) with trivial intersection. Applying (SU.2) gives

\[
 [C:A]\leq\exp\!\bigl(c_A m\log\log m\bigr).
\tag{SU.8}
\]

When \(C\) is abelian, (SU.8) holds trivially because \(C=A\).

It remains to compare \(A\) with \(Z(G)\). Let \(s=[G:C]\), and choose
\(g_1,\ldots,g_t\in G\) whose images generate \(G/C\), with

\[
 t\leq\log_2s.
\]

The subgroup \(D=G'\) is characteristic, so \(C=C_G(D)\) is characteristic
in \(G\), and hence so is \(A=Z(C)\).
Also \(Z(G)\leq A\), because \(Z(G)\leq C\) and it centralizes \(C\).
Therefore \([a,g_i]\in A\cap D\) for \(a\in A\). Because \(A\) is abelian,
the map

\[
 A\longrightarrow(A\cap D)^t,
 \qquad
 a\longmapsto([a,g_1],\ldots,[a,g_t])
\tag{SU.9}
\]

is a homomorphism. Its kernel is exactly \(Z(G)\): an element of \(A\)
already centralizes \(C\), and commuting with the chosen \(g_i\) makes it
commute with all of \(G\). Thus

\[
 [A:Z(G)]\leq d^t.
\tag{SU.10}
\]

For completeness, the polylogarithmic terms can be bounded explicitly.
Use natural logarithms and put \(L=\log(2m)\). Equations (SU.5)--(SU.6)
give, for \(m\geq3\),

\[
 u:=\log d<7L+\frac{2}{\log2}L^2\leq7L^2,
\]

and hence

\[
 \log[G:C]\leq\frac{u^2}{\log2}\leq71L^4,
 \qquad
 \log[A:Z(G)]\leq\frac{u^3}{(\log2)^2}\leq715L^6.
\tag{SU.11}
\]

Multiplying the three indices in (SU.6), (SU.8), and (SU.10) gives

\[
 \log[G:Z(G)]
 \leq c_A m\log\log m+786L^6.
\]

The exponential series gives \(L^6\leq6!e^L=1440m\). Since
\(\log\log m\geq\log\log3>0\) for \(m\geq3\), the linear term is absorbed
by an absolute multiple of \(m\log\log m\). This proves (SU.3).

Finally, a nonabelian group is covered by one abelian subgroup
\(\langle g,Z(G)\rangle\) for each nonidentity central coset, so

\[
 a(G)\leq[G:Z(G)]-1.
\]

Taking the supremum proves (SU.4). \(\square\)

## Scope and remaining obstruction

[UNVERIFIED] The bound \(2^{O(n\log\log n)}\) is the strongest
repository-audited universal upper bound currently reproduced from
accessible primary inputs. It improves the self-contained
\(e^{O(n\log n)}\) recurrence but does not reproduce Pyber's reported
fixed-base exponential theorem. No claim of novelty is made: a complete
forward search for this particular combination has not been completed.

[DISPROVED] Replacing (SU.2) by the withdrawn
arXiv:2205.03389 theorem would formally remove the \(\log\log n\) factor,
but that premise is invalid. The surviving 2026 theorem explicitly says
its hyperplane estimate is not strong enough to prove the \(2^{O(k)}\)
abelian-cover conjecture.
