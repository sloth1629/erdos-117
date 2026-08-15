# Integrated asymptotic reductions from the Pro research pass

This note records only results that survived algebraic audit.  It separates
unconditional theorems from interfaces whose hypotheses are still open.
Throughout, logarithms in estimates are base two unless stated otherwise.

## 1. Binary active-codomain collapse

Let

\[
 \beta:V\times V\longrightarrow W
\]

be alternating and bilinear over \(\mathbf F _2\).  Discard unused output
coordinates, put \(d=\dim V\), \(r=\dim W\), \(N=\nu(\beta)\), and

\[
 b(x)=\operatorname {rank}(y\mapsto\beta(x,y)),\qquad b=\max_x b(x).
\]

`[PROVED]` The commuting graph on \(V\setminus\{0\}\) and the random-order
independent-set lemma give the exact local-rank profile inequality

\[
 N\ge\sum_{x\ne0}\frac1{2^{d-b(x)}-1}.                 \tag{1.1}
\]

Indeed the closed commuting neighborhood of \(x\ne0\) has
\(2^{d-b(x)}-1\) vertices, while every finite graph satisfies
\(\alpha\ge\sum_v1/(\deg(v)+1)\).

Put \(T=\lceil\log_2(4N)\rceil\).  Equation (1.1) implies that fewer than
\(2^{d-2}\) vectors have local rank at least \(T\).  The complementary set
has density greater than one half, hence sums to all of \(V\).  Rank
subadditivity applied to \(B_z=B_x+B_y\) therefore proves

\[
 \boxed{b\le2T-2}.                                      \tag{1.2}
\]

`[CITED-VERIFIED]` Apply Skutin's Theorem 1.3 to the two-step nilpotent Lie
algebra \(V\oplus W\), with bracket \([x,y]=\beta(x,y)\).  Taking the
high-breadth set to be empty gives the following explicit corollary.  If the
maximum breadth is \(b\), put \(n=b+1\).  Were
\(\dim[V,V]>n(n-1)/2\), Theorem 1.3 would say that the empty high-breadth
set cannot be covered by two proper subalgebras, one of codimension at least
two.  But \(0\) and any one-dimensional central subalgebra provide such a
cover; the abelian case is immediate.  Hence

\[
 \dim[V,V]=r\le \frac{b(b+1)}2.
\]

Consequently

\[
 \boxed{r\le(T-1)(2T-1)<2T^2=O((\log N)^2)}.           \tag{1.3}
\]

The external input is A. A. Skutin, *Proof of a Conjecture of Wiegold for
Nilpotent Lie Algebras*, Sbornik: Mathematics 211 (2020), Theorem 1.3,
DOI `10.1070/SM9350`.  The withdrawn exponential irredundant-cover preprint
is not used.

`[PROVED]` The exterior-square map \(V\times V\to\Lambda^2V\) has
\(N=2^d-1\) and \(r=\binom d2\).  Thus the logarithmic-square order in
(1.3) cannot in general be replaced by \(O(\log N)\).

## 2. A regular commuting-operator range

Factor the joint radical of \(\beta\); this preserves both \(N\) and the
isotropic-subspace cover number \(a(\beta)\).  Suppose some scalarization

\[
 b_0=\lambda_0\beta
\]

is nondegenerate on the quotient, of dimension \(2m\).  For each
\(\lambda\in W^*\), define the unique operator \(A_\lambda\) by

\[
 (\lambda\beta)(x,y)=b_0(A_\lambda x,y).                \tag{2.1}
\]

Every \(A_\lambda\) is \(b_0\)-self-adjoint.

`[PROVED]` If the \(A_\lambda\) commute, or if they are simultaneously
triangularizable over \(\mathbf F _2\), they have a common invariant
Lagrangian \(L\).

For the commuting case, the unital algebra they generate is commutative and
self-adjoint.  A minimal nonzero module \(S\) is one-dimensional over a
finite residue field \(E\).  On \(S\), self-adjointness writes the form as
\(b(xs,ys)=\ell(xy)\).  Alternation gives \(\ell(x^2)=0\), and Frobenius is
bijective on \(E\), so \(S\) is isotropic.  Then \(S^\perp/S\) is invariant
and induction supplies the Lagrangian.  In the triangular case the first
line of a common invariant flag is isotropic; the same quotient induction
works.  Equation (2.1) then shows \(\beta(L,L)=0\).

`[PROVED]` Splitting each of the \(2^m\) affine cosets of \(L\) by the
fibres of \(u\mapsto\beta(x,u)\) uses at most \(2^r\) isotropic sets per
coset.  Their spans are isotropic, so

\[
 a(\beta)\le2^{m+r}.                                    \tag{2.2}
\]

A nondegenerate binary alternating form of dimension \(2m\) contains a
\((2m+1)\)-clique: realize the all-off-diagonal-one Gram matrix and append
the sum of its \(2m\) basis vectors.  Hence \(N\ge2m+1\), and

\[
 \boxed{\log_2 a(\beta)\le N/2+r-1/2}.                 \tag{2.3}
\]

Combining (1.3) and (2.3) gives

\[
 \log_2a(\beta)\le N/2+O((\log N)^2)                  \tag{2.4}
\]

for this regular commuting/triangularizable range.  This is a genuine
higher-codomain theorem, but it does not cover singular pencils or
noncommuting self-adjoint operator algebras.

## 3. Integral and fractional covers

`[PROVED]` For every finite graph with \(v\) vertices,

\[
 \chi_f\le\chi\le(2+\ln v)\chi_f.                     \tag{3.1}
\]

Given a fractional coloring of cost \(\tau\), some independent set covers
at least a \(1/\tau\) fraction of the currently uncovered vertices.
Greedy repetition for \(\lceil\tau\ln v\rceil\) steps leaves at most one
vertex, proving (3.1).

`[PROVED]` Applied to the compressed noncommuting graph of a finite group,
the factorial center-index bound \(|G:Z(G)|\le\nu(G)!\) gives

\[
 0\le\log(a(G)-1)-\log(a_f(G)-1)=O(\log\nu(G)).        \tag{3.2}
\]

Thus integral versus fractional abelian covering is never an asymptotic
linear obstruction.  In the binary alternating model one can also use
\(d\le r(N-1)\), obtained by injecting the radical-free domain into the
direct sum of the scalar-form images, together with (1.3).

## 4. The critical \(p\)-group ledger

The following statements concern a finite \(p\)-group \(P\),
\(m=\nu(P)\), and a maximal abelian normal subgroup \(A\) with
\(C_P(A)=A\).  Put \(Q=P/A\).

`[PROVED]` If \(S\subseteq Q\) is a pairwise noncommuting clique and

\[
 w(q)=[A:C_A(x)]=|[A,x]|,
\]

where \(x\) lifts \(q\), then

\[
 \boxed{\sum_{q\in S}w(q)\le m}.                       \tag{4.1}
\]

For a fixed coset \(xA\), a transversal of \(A/C_A(x)\) is a clique;
different quotient-clique cosets remain cross-noncommuting under arbitrary
translations.  This proves (4.1).

`[PROVED]` Faithfulness of the cyclic group \(\langle q\rangle\) on \(A\)
gives a regular orbit, because the subgroups of a cyclic \(p\)-group are
linearly ordered.  Therefore

\[
 o(q)\le w(q),\qquad \exp Q\le m.                      \tag{4.2}
\]

If \(D_j(q)=(q-1)^jA\) and \(\delta_A(q)\) is the last nonzero depth, each
nonzero step drops by at least a factor \(p\).  Hence

\[
 p^{\delta_A(q)}\le w(q),\qquad
 \sum_{q\in S}p^{\delta_A(q)}\le m.                   \tag{4.3}
\]

`[PROVED]` If \(E\trianglelefteq Q\) and \(E\cong C_p^2\), then
\([Q:C_Q(E)]\le p\).  If \(C_Q(E)\) is abelian, direct centralizer counting
gives

\[
 \nu(Q)=|C_Q(E):Z(Q)|+1,
\]

so \(|Q:Z(Q)|\le m-p\).  Otherwise one reaches, at a cost of only one
\(p\)-factor, a nonabelian subgroup with central \(C_p^2\).  The latter is
one of the genuine residual regimes.

### 4.1 Scalar-visible critical sections

Suppose a class-two section \(C\) has elementary
\(V=C/Z(C)\), \(W=C'\), commutator map \(\kappa:V\times V\to W\), and a
maximal jointly isotropic subspace \(U\).  For
\(0\ne\lambda\in W^*\), write

\[
 \operatorname {rank}(\lambda\kappa)=2r_\lambda,
\quad e=\log_p|P:CA|,
\quad s_\lambda=\dim(V/U)-r_\lambda.
\]

`[PROVED]` The exact entropy identity and scalar clique charge give

\[
 \boxed{\log_2|Q|
 \le m/2+(e+s_\lambda)\log_2p}.                        \tag{4.4}
\]

The scalar charge used here is explicit.  A rank-\(r\) symplectic space has
a \((pr+1)\)-clique by repeated projective-line splicing for \(p=2\) or
\(p\ge5\); this is at least \(2r\log_2p\).  For \(p=3\), splice the
13-point rank-three partial ovoid with rank-one four-point blocks.  The
13-point seed is both the repository's independently certified
\(S(3,3)\) clique and the construction of Ceria--De Beule--Pavese--Smaldore,
Theorem 3.7.  Thus \(r_\lambda\log_2p\le m/2\), while
\(\log_p|Q|=r_\lambda+s_\lambda+e\).

Thus it suffices to find a scalar projection with
\(e+s_\lambda=O(\log_p(m+1))\).  No such projection is yet known in full
generality.

### 4.2 Coupled elementary action and cocycle

For vector spaces \(V,L,W\) over \(\mathbf F_p\), with
\(L\le\operatorname {Hom}(V,W)\), consider

\[
 B_\beta((v,T),(v',S))=T(v')-S(v)+\beta(T,S).          \tag{4.5}
\]

For \(0\ne\phi\in W^*\), put

\[
 a_\phi(T)=\phi T,quad d_\phi=\operatorname {rank}a_\phi,
\quad K_\phi=\ker a_\phi,
\quad c_\phi=\operatorname {rank}(\phi\beta|_{K_\phi}).
\]

`[PROVED]` A hyperbolic splitting followed by a shear on \(K_\phi\) gives
the exact scalar rank formula

\[
 \operatorname {rank}(\phi B_\beta)=2d_\phi+c_\phi.   \tag{4.6}
\]

Scalar symplectic clique constructions then imply

\[
 \boxed{m\ge2\log_2p\,(d_\phi+c_\phi/2)}.             \tag{4.7}
\]

In particular, if one scalar output separates all of \(L\), then

\[
 \boxed{\log_2|Q|\le m/2}.                             \tag{4.8}
\]

This includes a common one-dimensional output line with arbitrary central
cocycle.  Conversely, every candidate exceeding \(m/2\) must have a large
kernel \(K_\phi\) for every scalar direction; this is the precise
kernel-lattice concentration obstruction.

### 4.3 Orthogonally split full-evaluation blocks

Let \(R_i=\mathbf Z/p^{a_i}\mathbf Z\),
\(X_i=R_i^{n_i}\), \(Y_i=R_i^{r_i}\), and
\(U_i=\operatorname {Hom}_{R_i}(X_i,Y_i)\).  Set

\[
 P=(Y\oplus X)\rtimes U,
\quad (y,x,u)(y',x',u')=(y+y'+u(x'),x+x',u+u').
\]

`[PROVED]` If \(\sum_i a_in_i\ge2\) and
\(\sum_i n_ir_i\ge2\), then

\[
 Z(P)=P'=Y,quad C_P(Y\oplus X)=Y\oplus X,
\]

every maximal subgroup is nonabelian, \(Q\cong U\) contains a normal
\(C_p^2\), and an explicit rooted orthogonal-splice clique proves

\[
 \boxed{\log_2|Q|\le\nu(P)/2}.                         \tag{4.9}
\]

Thus full rectangular evaluation blocks are not counterexamples.  Proper
operator spaces, shared outputs across blocks, non-split cross-cocycles,
and nonabelian quotients remain.

## 5. Uniform conditional transfer

Let \(e(t)=o(t)\) be one function, uniform in the prime.

`[PROVED]` Assume every finite nonabelian \(p\)-group satisfies

\[
 \log_2|P:Z(P)|\le\nu(P)/2+e(\nu(P)).                 \tag{5.1}
\]

Define

\[
 R_e(M)=\max\left\{\sum_i e_+(n_i): n_i\ge3,
                               \prod_i n_i\le M\right\}.
\]

Splitting the indices at a fixed threshold proves

\[
 R_e(M)\le\theta_e(T)M+B_e(T)\lfloor\log_3M\rfloor=o(M).
\]

For the nonabelian Sylow factors \(P_i\) of a finite nilpotent group,
\(\prod_i\nu(P_i)\le\nu(F)\), while center indices multiply.  Hence

\[
 \boxed{\log_2|F:Z(F)|
 \le\nu(F)/2+R_e(\nu(F))}.                            \tag{5.2}
\]

If there are at least two nonabelian Sylow factors, the linear coefficient
improves to \(1/3\).  The same argument works for \(a(P)\) using only
\(a(F)\le\prod_i a(P_i)\); it never assumes clique or chromatic
multiplicativity.

`[PROVED]` Assume instead the uniform nilpotent envelope

\[
 \log_2|F:Z(F)|\le\nu(F)/2+\eta_{\rm nil}(\nu(F)),
 \qquad \eta_{\rm nil}=o(n).                          \tag{5.3}
\]

The audited Fitting-action estimate, the radical-free semisimple envelope,
and exact solvable-radical lifting then give, for every finite group,

\[
 \log_2a(G)\le \nu(G)/2+widehat\eta_{\rm nil}(\nu(G))
   +4(\log_2\nu(G))^2+\log_2\nu(G)+\Sigma_{\rm ss}(\nu(G)), \tag{5.4}
\]

where the running envelope \(\widehat\eta_{\rm nil}=o(n)\) and the
CFSG-dependent radical-free envelope \(\Sigma_{\rm ss}=o(n)\).  Thus (5.3)
would imply the universal \(\sqrt2\)-base upper bound.

`[UNVERIFIED]` Hypothesis (5.1), equivalently the required uniform
\(p\)-group/nilpotent input up to the transfers above, is not proved.  This
is now the principal global bottleneck.  Equations (5.2)--(5.4) are
conditional implications, not a solution of Erdős 117.

## 6. Rate regularization

For nonabelian groups put

\[
 p(G)=\ln(a(G)-1),\qquad q(G)=\nu(G)-1,
\]

and \(b(t)=\ln(h(t+1)-1)\).  Let
\(\rho_\infty=\limsup b(t)/t\).

`[PROVED]` The limit \(b(t)/t\) exists exactly when there are
\(t_j\to\infty\) with

\[
 t_{j+1}/t_j\to1,qquad b(t_j)/t_j\to\rho_\infty.     \tag{6.1}
\]

This follows immediately by squeezing every \(t\in[t_j,t_{j+1})\) using
monotonicity.  It is an exact criterion, not a construction of such a
sequence.

`[PROVED]` The logarithmic integral/fractional gap in (3.2) allows the same
criterion and any triangular near-extremal transfer theorem to be stated in
terms of fractional covers with only \(o(q)\) loss.

`[UNVERIFIED]` No group-theoretic amplifier realizing the mesh-dense
near-extremizers is known.  Therefore existence of
\(\lim h(n)^{1/n}\) remains open even after the analytic regularization.

## 7. Exact frontier after integration

`[PROVED]` The Pro pass closes the following large ranges without changing
the already proved exact values through eight:

1. binary higher-codomain maps have active codomain
   \(O((\log N)^2)\);
2. regular scalarizations with commuting or triangularizable operator
   algebra satisfy the \(N/2+o(N)\) exponent;
3. integral versus fractional covering costs only \(O(\log N)\) in the
   exponent;
4. full-evaluation, one-scalar-separable, shallow single-operator, and
   several normal-\(C_p^2\) critical branches obey the target half-rate.

`[UNVERIFIED]` The surviving obstruction is a prime-uniform high-rank
\(p\)-group estimate: mixed higher-class/operator directions can share
output and alternate scalar kernels so that no one projection pays all of
the quotient entropy.  Closing that one uniform interface would propagate
through the proved nilpotent, solvable, semisimple, integral-rounding, and
rate-composition results above.  It would still establish an asymptotic
theorem rather than all exact values \(h(n)\) for \(n\ge9\).
