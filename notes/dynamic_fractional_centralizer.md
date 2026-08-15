[PROVED] The LP identities and entropy telescope below are exact.

[UNVERIFIED] The required global sublinear bound on accumulated node charge is not proved.

# Dynamic centralizer recursion의 정확한 entropy telescope

## 1. 범위와 결론

이 문서는 기존의 max-child majorant를 사용하지 않고 정확한 dynamic LP

\[
R(H)=\min_{\lambda\in\mathcal T(H)}
\sum_{x\notin Z(H)}\lambda_xR(C_H(x))
\]

자체를 전개한다. 여기서 abelian terminal에는 `R(H)=1`을 두고, clique 수는 centralizer recursion에서 쓰인 convention에 따라 abelian group에서 `0`으로 둔다. 모든 logarithm은 밑이 2이다.

얻어지는 등식은 실제로 망원합하지만, 그 누적 entropy charge가 `o(\nu(G))`라는 보편 부등식은 이번 작업에서 증명되지 않았다. 따라서 아래 정리는 DFAL의 증명이 아니라, DFAL에서 정확히 제어해야 할 양을 max-child 손실 없이 식별한 정리다.

---

## 2. Dynamic LP의 정확한 dual

비가환 finite group `H`에서

\[
r_x:=R(C_H(x))\qquad(x\notin Z(H))
\]

라 쓰자. Dynamic recursion은 cost가 `r_x`인 finite set-cover LP다.

### Proposition 2.1 — dynamic primal/dual

\[
\boxed{
R(H)=
\max_{\rho:H\to\mathbb R_{\ge0}}
\left\{
\sum_{h\in H}\rho(h):
\sum_{h\in C_H(x)}\rho(h)\le r_x
\quad\forall x\notin Z(H)
\right\}.}
\]

### 증명

Primal constraint matrix의 `(h,x)` entry를 `1_{h\in C_H(x)}`로 두면 primal은

\[
\min\sum_x r_x\lambda_x,
\qquad
\sum_{x:h\in C_H(x)}\lambda_x\ge1,
\qquad \lambda_x\ge0.
\]

유한 LP의 표준 dual이 바로 위 식이다. Primal은 maximum noncommuting clique의 centralizers로 feasible이고, dual은 `0`으로 feasible이므로 finite LP strong duality가 적용된다. ∎

이 dual은 기존 `\tau_{\rm cen}` dual과 같은 incidence matrix를 쓰되, 각 centralizer의 capacity가 `1`이 아니라 정확히 child value `R(C_H(x))`라는 점이 핵심이다.

---

## 3. Gibbs/KL identity

`H`에서 dynamic-optimal primal solution `\lambda`를 하나 고정하고

\[
s_H:=\sum_x\lambda_x,
\qquad
q_x:=\frac{\lambda_x}{s_H},
\qquad
p_x:=\frac{\lambda_xr_x}{R(H)}
\]

로 둔다. `q`와 `p`는 모두 probability distribution이다. `p`는 실제 dynamic objective에서 각 child가 차지하는 cost 비율이다.

### Theorem 3.1 — exact log-sum/KL decomposition

\[
\boxed{
\log R(H)
=
\mathbb E_p\log r_x
+
\log s_H
-
D_2(p\Vert q).}
\tag{3.1}
\]

동치로

\[
\log R(H)
=
\mathbb E_p\log r_x
+H_2(p)+\mathbb E_p\log\lambda_x.
\tag{3.2}
\]

### 증명

`p_x=\lambda_xr_x/R(H)`이므로

\[
\log R(H)=\log\lambda_x+\log r_x-\log p_x
\]

를 `p`에 대해 평균하면 (3.2)를 얻는다. 또한

\[
\begin{aligned}
D_2(p\Vert q)
&=\sum_xp_x\log\frac{p_x}{q_x}\\
&=\sum_xp_x\log p_x-\sum_xp_x\log\lambda_x+\log s_H.
\end{aligned}
\]

이를 (3.2)에 대입하면 (3.1)이 된다. ∎

`D_2(p\Vert q)`는 max-child 처리에서 완전히 사라지는 음의 correction이다. Child values가 크게 불균일할수록 cost-tilted distribution `p`와 raw cover distribution `q`가 달라지고, 이 KL term이 커져 branch entropy를 상쇄한다.

---

## 4. clique budget을 포함한 정확한 potential

\[
F(H):=\log R(H)-\frac12\nu(H),
\qquad
\Delta_x:=\nu(H)-\nu(C_H(x))
\]

로 둔다. 기존 clique-drop lemma에 의해 `\Delta_x\ge2`다.

Theorem 3.1에 `\log r_x=F(C_H(x))+\nu(C_H(x))/2`를 넣으면 다음을 얻는다.

### Theorem 4.1 — one-node entropy telescope

\[
\boxed{
F(H)=\mathbb E_pF(C_H(x))+\eta(H),}
\tag{4.1}
\]

여기서 정확한 node charge는

\[
\boxed{
\eta(H):=
\log s_H-D_2(p\Vert q)
-\frac12\mathbb E_p\Delta_x.}
\tag{4.2}
\]

이다.

### Corollary 4.2 — path expectation identity

각 nonabelian state `K`에서 dynamic-optimal solution 하나를 고정하고, transition

\[
K\longmapsto C_K(x)
\]

을 해당 state의 `p^K_x` 확률로 선택한다. Centralizer는 proper subgroup이므로 이 Markov chain은 첫 abelian state에서 유한 시간 안에 멈춘다. 그러면

\[
\boxed{
\log R(G)-\frac12\nu(G)
=
\mathbb E\sum_{i=0}^{T-1}\eta(H_i).}
\tag{4.3}
\]

### 증명

(4.1)을 각 state에서 조건부 기대값으로 적용하고 tower property를 반복한다. Terminal `H_T`는 abelian이므로 `R(H_T)=1`, `\nu(H_T)=0`, 따라서 `F(H_T)=0`이다. ∎

따라서 Dynamic FAL을 이 lane에서 끝내는 정확한 충분조건은

\[
\boxed{
\mathbb E\sum_{i<T}\eta(H_i)=o(\nu(G))}
\tag{4.4}
\]

이다. 이것은 max over chains가 아니라 **dynamic-optimal cost-tilted path의 기대값**이다.

---

## 5. max-child defect와의 정확한 차이

고정된 feasible `\lambda`에 대해

\[
\log\sum_x\lambda_xr_x
=
\mathbb E_p\log r_x+\log\sum_x\lambda_x-D_2(p\Vert q).
\]

Max-child 단계는 우변을

\[
\max_x\log r_x+
\log\sum_x\lambda_x
\]

로 바꾼다. 즉 동시에

1. `\mathbb E_p\log r_x`를 `\max_x\log r_x`로 올리고,
2. nonnegative KL correction `D_2(p\Vert q)`를 버린다.

또한 `P_{\rm cen}`은 `\tau_{\rm cen}`-optimal cover를 쓰지만, exact dynamic optimum은 총 weight `s_H`가 더 크더라도 값싼 child들만 선택할 수 있다. 따라서 `s_H`를 항상 `\tau_{\rm cen}(H)`로 바꾸는 것도 정당하지 않다.

---

## 6. 두 exact model에서의 작동

### 6.1 Binary scalar symplectic rank 2

첨부 certificate의 order-32 group에서는

\[
\nu=5,
\qquad
\tau_{\rm cen}=\frac{15}{7},
\qquad
R(\text{모든 child})=3,
\qquad
R(G)=\frac{45}{7}.
\]

Root에서 `p=q`이므로 KL correction은 0이고 `\Delta=2`다. 따라서

\[
\eta(G)=\log\frac{15}{7}-1>0.
\]

그 다음 `K_3` child에서는

\[
\eta=\log3-\frac32>0.
\]

두 charge의 합은 정확히

\[
\log\frac{45}{7}-\frac52.
\]

이 예는 node charge가 항상 nonpositive라는 강화가 거짓임을 exact rational LP certificate로 보인다.

### 6.2 Mixed order-64 model

두 번째 model에서는

\[
\nu=6,
\qquad
\tau_{\rm cen}=3,
\qquad
P_{\rm cen}=3\cdot3=9>2^{6/2}=8.
\]

따라서 max-child defect는

\[
\mathfrak D_{\rm cen}(G)=\log\frac98>0.
\]

그러나 exact dynamic LP는 여섯 개의 abelian-child centralizers만 weight `1`로 사용하여

\[
R(G)=6.
\]

이 solution에서는 `s_H=6`, `p=q`, 모든 선택 child의 `\Delta=6`이므로

\[
\eta(G)=\log6-3<0.
\]

더 나아가 같은 여섯 abelian subgroups가 primal cover를 이루고, 6-clique가 matching dual을 주므로

\[
a_f(G)=R(G)=6<8<9=P_{\rm cen}(G).
\]

즉 이 finite model에서 양의 max-child defect는 실제 dynamic obstruction이 아니라 **잘못된 child를 최대값으로 보낸 데서 생긴 인공 손실**이다.

---

## 7. 정확히 남은 전역 명제

이번 작업으로 다음 두 강화가 모두 거짓임이 확인되었다.

\[
\min_{\lambda\in\mathcal T(H)}
\sum_x\lambda_x2^{-\Delta_x/2}\le1
\quad\text{for every }H,
\]

그리고

\[
\eta(H)\le0
\quad\text{at every dynamic node}.
\]

첫 번째는 scalar rank-2 model에서 optimum이 `15/14`; 두 번째도 같은 model에서 양의 charge를 가진다.

따라서 DFAL을 완성하려면 finite positive charges를 허용하되, (4.3)의 dynamic-optimal path expectation에서 그 총합이 sublinear임을 보여야 한다. 현재 package는 그 전역 상계를 주장하지 않는다.
