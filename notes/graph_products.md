# Direct Products and Graph Capacities

This note is Workstream D's independent derivation. It uses finite graphs unless stated otherwise.

## The exact graph product

### Lemma D.1 `[PROVED]`

For groups \(G,H\),

\[
\Gamma_{G\times H}=\Gamma_G\vee\Gamma_H,
\]

where the disjunctive (OR, co-normal) product \(X\vee Y\) has vertex set \(V(X)\times V(Y)\), with distinct \((x,y),(x',y')\) adjacent exactly when \(x\sim_Xx'\) or \(y\sim_Yy'\).

**Proof.** In a direct product,

\[
[(g,h),(g',h')]=([g,g'],[h,h']).
\]

The two product elements fail to commute exactly when at least one coordinate commutator is nontrivial, which is precisely OR adjacency. \(\square\)

Because \(Z(G\times H)=Z(G)\times Z(H)\), the same identity holds for the central-coset compressed graphs after the natural identification

\[
(G\times H)/Z(G\times H)\cong G/Z(G)\times H/Z(H).
\]

## One-shot inequalities

### Proposition D.2 `[PROVED]`

For finite graphs \(X,Y\),

\[
\omega(X\vee Y)\geq \omega(X)\omega(Y),\qquad
\chi(X\vee Y)\leq \chi(X)\chi(Y),
\]

and

\[
\alpha(X\vee Y)=\alpha(X)\alpha(Y).
\]

**Proof.** Products of cliques are cliques, and pairs of proper colors give a proper product coloring. If \(A\) is independent in \(X\vee Y\), each coordinate projection of \(A\) is independent, so \(|A|\leq\alpha(X)\alpha(Y)\). The product of maximum independent sets attains equality. \(\square\)

Consequently,

\[
\nu(G\times H)\geq\nu(G)\nu(H),\qquad
a(G\times H)\leq a(G)a(H).
\]

Neither displayed inequality is to be upgraded to equality without a proof for the particular group family.

## Fractional chromatic number

Let \(\chi_f(X)\) be the fractional set-cover number of the vertices by independent sets.

### Proposition D.3 `[PROVED]`

For finite graphs,

\[
\chi_f(X\vee Y)=\chi_f(X)\chi_f(Y).
\]

**Proof.** If \((p_I)\) and \((q_J)\) are fractional colorings of \(X\) and \(Y\), assign weight \(p_Iq_J\) to the independent set \(I\times J\). This gives the upper bound.

For the reverse inequality, use the dual linear program. Let nonnegative vertex weights \((u_x)\), \((v_y)\) be dual-optimal for \(X,Y\), so every independent set has total weight at most one. Give \((x,y)\) weight \(u_xv_y\). If \(K\) is independent in \(X\vee Y\), both coordinate projections are independent and \(K\) lies in their Cartesian product. Hence

\[
\sum_{(x,y)\in K}u_xv_y
\leq
\left(\sum_{x\in\pi_XK}u_x\right)
\left(\sum_{y\in\pi_YK}v_y\right)
\leq1.
\]

Thus the product dual solution is feasible and has objective \(\chi_f(X)\chi_f(Y)\). \(\square\)

### Proposition D.4 `[PROVED]`

For every nonempty finite graph \(X\),

\[
\lim_{k\to\infty}\chi(X^{\vee k})^{1/k}=\chi_f(X).
\]

**Proof.** Fractional multiplicativity and \(\chi_f\leq\chi\) give the lower bound. For any graph \(Y\) on \(N\) vertices, the greedy set-cover argument gives

\[
\chi(Y)\leq(1+\log N)\chi_f(Y).
\]

Indeed, if \(r\) vertices remain and a fractional cover has total weight \(t\), some independent set covers at least \(r/t\) of them; iterating and then covering the final remainder yields the stated bound. Apply this to \(Y=X^{\vee k}\), which has \(|V(X)|^k\) vertices, and use Proposition D.3:

\[
\chi(X^{\vee k})
\leq(1+k\log|V(X)|)\chi_f(X)^k.
\]

The prefactor has \(k\)-th root tending to one. \(\square\)

Therefore, for every finite group \(G\),

\[
\lim_{k\to\infty}a(G^k)^{1/k}=\chi_f(\Gamma_G).
\]

The same value is obtained from the central-coset compressed graph because independent twin blow-ups do not change either integral or fractional chromatic number.

## Clique growth and Shannon capacity

### Proposition D.5 `[PROVED]`

For a finite graph \(X\), the limit

\[
\lim_{k\to\infty}\omega(X^{\vee k})^{1/k}
\]

exists and equals the Shannon capacity \(\Theta(\overline X)\), with the convention

\[
\Theta(Y)=\lim_{k\to\infty}\alpha(Y^{\boxtimes k})^{1/k}.
\]

**Proof.** The complement identity

\[
\overline{X\vee Y}=\overline X\boxtimes\overline Y
\]

follows directly from the definitions: two distinct product vertices are nonadjacent in the OR product exactly when, in each coordinate, they are equal or adjacent in the relevant complement. Hence

\[
\omega(X^{\vee k})=\alpha(\overline X^{\boxtimes k}).
\]

Products of cliques show supermultiplicativity of \(\omega(X^{\vee k})\); Fekete's lemma applied to its logarithm gives existence of the finite exponential rate. \(\square\)

Thus, for every finite group \(G\),

\[
\lim_{k\to\infty}\nu(G^k)^{1/k}=\Theta(\overline{\Gamma_G}).
\]

## Consequence for the global Erdős problem

### Observation D.6 `[PROVED]`

Fix a finite nonabelian group \(G\), and put

\[
\phi=\chi_f(\Gamma_G),\qquad
\theta=\Theta(\overline{\Gamma_G}).
\]

Then \(\theta\geq\omega(\Gamma_G)\geq3\), and along direct powers,

\[
a(G^k)=\phi^{k+o(k)},\qquad
\nu(G^k)=\theta^{k+o(k)}.
\]

Consequently direct powers of one fixed seed yield only the polynomial-scale relation

\[
a(G^k)=\nu(G^k)^{\log\phi/\log\theta+o(1)}.
\]

They cannot by themselves explain an exponential lower bound \(h(n)\geq c^n\) with \(c>1\). The exponential construction must vary its commutator geometry with \(n\); central products leading to one scalar-valued alternating form do exactly this, whereas ordinary direct products retain coordinatewise commutator constraints.

## Audit warnings

- OR-product chromatic number is only submultiplicative in general; the exact asymptotic rate is fractional chromatic number.
- OR-product clique number is only supermultiplicative in general; its rate is a Shannon capacity, not generally the one-shot clique number.
- These fixed-seed limits do not imply existence of \(\lim h(n)^{1/n}\).
- Full element graphs and central-coset compressed graphs agree for \(\omega\) and \(\chi\), but clone blow-ups must be checked separately for any new invariant.
