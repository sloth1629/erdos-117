[COMPUTED] The finite certificates below are independently reproducible by
`src/verification/verify_dynamic_fractional_centralizer.py`.

# Exact finite models and a certified one-step no-go theorem

## 1. 공통 class-two construction

`V=\mathbb F_2^d`, `W=\mathbb F_2^r`라 하자. 대각이 0인 symmetric matrices

\[
A_1,\ldots,A_r\in M_d(\mathbb F_2)
\]

가 alternating bimap

\[
\beta(v,w)=\bigl(v^TA_1w,\ldots,v^TA_rw\bigr)
\]

을 정한다. `U_j`를 `A_j`의 strict upper triangle이라 하고

\[
c(v,w)=\bigl(v^TU_1w,\ldots,v^TU_rw\bigr)
\]

로 두면

\[
(v,z)(w,t)=(v+w,z+t+c(v,w))
\tag{1.1}
\]

은 `V\times W` 위의 finite class-two group law다. Bilinearity가 associativity를 주고

\[
[(v,z),(w,t)]=\bigl(0,\beta(v,w)\bigr).
\]

따라서 `\operatorname{rad}\beta=0`이면 center는 정확히 `\{0\}\times W`이고, compressed noncommuting graph의 정점은 `V\setminus\{0\}`이며

\[
v\sim w\iff\beta(v,w)\ne0.
\]

첨부 verifier는 두 model에서 (1.1)의 associativity, inverse, center, commutator relation을 full multiplication table로 다시 확인한다.

---

## 2. Model S: binary scalar symplectic rank 2

### 2.1 정의

`d=4`, `r=1`이고

\[
A=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
1&0&0&0\\
0&1&0&0
\end{pmatrix}.
\]

이에 대응하는 group은 order `32`, center order `2`다.

### 2.2 clique와 abelian fractional cover

Exact verifier와 표준 binary symplectic Gram-rank argument가

\[
\nu(G_S)=5
\]

를 준다. Certificate clique는

\[
\{2,8,11,14,15\}
\]

이다. 다음 다섯 totally isotropic planes가 `V`를 partition한다.

\[
\begin{aligned}
&\{0,1,2,3\},\quad
\{0,4,8,12\},\quad
\{0,5,10,15\},\\
&\{0,6,11,13\},\quad
\{0,7,9,14\}.
\end{aligned}
\]

따라서 primal cost는 5다. 위 5-clique의 각 vertex에 dual weight 1을 주면 모든 isotropic subspace가 그 support를 최대 하나만 포함하므로 matching dual cost도 5다. 즉

\[
\boxed{a_f(G_S)=5.}
\]

### 2.3 `\tau_{\rm cen}`, normalized local LP, dynamic value

각 nonzero `x\in V`의 centralizer quotient는 hyperplane

\[
K_x=x^\perp
\]

이고 `|K_x|=8`이다. 각 nonzero `h`는 정확히 7개의 `K_x`에 들어가며, 각 `K_x`는 정확히 7개의 nonzero vectors를 포함한다.

따라서 다음 primal/dual pair가 exact하다.

- Primal: 모든 15개 `K_x`에 weight `1/7`.
- Dual: 모든 nonzero `h`에 weight `1/7`, `0`에는 weight `0`.

양쪽 objective가 일치하여

\[
\boxed{\tau_{\rm cen}(G_S)=\frac{15}{7}.}
\]

각 child의 compressed graph는 `K_3`이므로

\[
\nu(C_G(x))=3,
\qquad
R(C_G(x))=3.
\]

그 결과 dynamic primal/dual cost는 centralizer capacity를 3배 한 같은 certificate로

\[
\boxed{R(G_S)=\frac{45}{7}.}
\]

이제 zero-error normalized local LP를

\[
\kappa(H):=
\min_{\lambda\in\mathcal T(H)}
\sum_x\lambda_x2^{-(\nu(H)-\nu(C_H(x)))/2}
\]

로 두자. 이 model에서는 모든 drop이 2이므로 cost가 `1/2`다. Primal weight `1/7`, dual weight `1/14`가 일치하여

\[
\boxed{\kappa(G_S)=\frac{15}{14}>1.}
\]

따라서

\[
\min_{\lambda\in\mathcal T(H)}
\sum_x\lambda_x2^{-\Delta_x/2}\le1
\]

이라는 가장 강한 one-node DFAL induction은 거짓이다. 이것은 finite local obstruction일 뿐, DFAL이나 Full FAL의 asymptotic 반례가 아니다.

---

## 3. Model M: order-64 mixed bimap

### 3.1 정의

`d=4`, `r=2`이고

\[
A_1=
\begin{pmatrix}
0&1&1&1\\
1&0&0&0\\
1&0&0&1\\
1&0&1&0
\end{pmatrix},
\qquad
A_2=
\begin{pmatrix}
0&1&1&1\\
1&0&1&0\\
1&1&0&0\\
1&0&0&0
\end{pmatrix}.
\]

Radical은 0이고, (1.1)의 group `G_M`은 order `64`, center order `4`다.

### 3.2 exact clique number

Certificate clique

\[
\{7,8,9,13,14,15\}
\]

가 size 6이다. Dependency-free exact branch-and-bound가 7-clique가 없음을 확인하므로

\[
\boxed{\nu(G_M)=6.}
\]

### 3.3 centralizer inventory

중복을 합치면 quotient centralizer는 정확히 9개다.

#### Nonabelian children (`\nu=3`, dynamic value 3)

\[
\begin{aligned}
K_1&=\{0,1,2,3,8,9,10,11\},\\
K_2&=\{0,1,4,5,10,11,14,15\},\\
K_3&=\{0,1,6,7,10,11,12,13\}.
\end{aligned}
\]

각 `K_i`의 radical quotient는 4점이고 세 nonzero cosets가 `K_3`를 이룬다. 따라서 각 child는 `R=P=3`이다.

#### Abelian children (`\nu=0`, dynamic value 1)

\[
\begin{aligned}
L_1&=\{0,1,6,7\},&
L_2&=\{0,1,12,13\},\\
L_3&=\{0,2,8,10\},&
L_4&=\{0,3,9,10\},\\
L_5&=\{0,4,11,15\},&
L_6&=\{0,5,11,14\}.
\end{aligned}
\]

### 3.4 exact `\tau_{\rm cen}=3`

Primal은 `K_1,K_2,K_3`에 각각 weight 1을 준다. 이 세 sets가 `V`를 cover한다.

Dual은 vectors `2,5,6`에 각각 weight 1을 준다. 모든 9개 centralizer가 이 support를 최대 하나 포함한다. 따라서 primal과 dual objective가 모두 3이고

\[
\boxed{\tau_{\rm cen}(G_M)=3.}
\]

### 3.5 max-child는 실패하지만 dynamic LP는 정확히 성공한다

Max-child majorant는 nonabelian child를 택하여

\[
P_{\rm cen}(G_M)=3\cdot3=9.
\]

그러므로

\[
\boxed{\mathfrak D_{\rm cen}(G_M)=\log_2\frac98>0.}
\]

반면 dynamic primal은 `L_1,\ldots,L_6`에 각각 weight 1을 주며 cost가 6이다. Matching dynamic dual은

\[
\{2,3,4,5,6,12\}
\]

의 각 vector에 weight 1을 준다.

- Abelian-child centralizer는 support를 최대 하나 포함하므로 capacity 1 constraint를 만족한다.
- 각 nonabelian-child centralizer는 support를 정확히 두 개 포함하므로 capacity 3 constraint를 만족한다.

따라서

\[
\boxed{R(G_M)=6.}
\]

같은 여섯 `L_i`가 abelian primal cover이고 위 6-set은 clique dual이므로

\[
\boxed{a_f(G_M)=R(G_M)=6<8<9=P_{\rm cen}(G_M).}
\]

이것은 max-child의 양의 defect가 dynamic obstruction을 의미하지 않는다는 exact finite certificate다.

### 3.6 weighted local optimum

`L_i`의 drop은 6이므로 normalized cost는 `1/8`; `K_i`의 drop은 3이므로 cost는 `1/(2\sqrt2)`다. Primal은 여섯 `L_i`를 weight 1로 사용하여 value `6/8=3/4`를 준다.

Dual은 `\{2,3,4,5,6,12\}`에 각각 weight `1/8`을 준다. 각 `L_i`의 mass는 `1/8`, 각 `K_i`의 mass는 `1/4\le1/(2\sqrt2)`다. 따라서

\[
\boxed{\kappa(G_M)=\frac34.}
\]

Scalar model의 `15/14`와 대조하면, child-value variation을 유지하는 weighted recursion이 왜 필요한지 정확히 보인다.

---

## 4. Natural third-layer extension에 대한 전수 no-go

Model M의 bimap을 `\beta_0:V_0\times V_0\to W_0`라 하자. 여기서 `\dim V_0=4`, `\dim W_0=2`다.

다음 class의 모든 elementary class-two one-pair extension을 생각한다.

\[
\widetilde V=V_0\oplus\langle u,v\rangle,
\]

그리고 임의의 codomain `\widetilde W`에 대해

\[
\widetilde\beta|_{V_0\times V_0}=\beta_0,
\qquad
\widetilde\beta(u,V_0)=0,
\qquad
z:=\widetilde\beta(u,v)\ne0.
\tag{4.1}
\]

그러면

\[
C_{\widetilde V}(u)=V_0\oplus\langle u\rangle,
\]

`u`는 이 restriction의 radical이고 compressed child는 정확히 Model M이다. 따라서 child clique number는 6이다.

### Theorem 4.1 — certified no-third-layer theorem

(4.1)을 만족하는 모든 extension에 대해

\[
\boxed{\nu(\widetilde\beta)\ge10.}
\]

특히 이 class에서는 `u`-centralizer step의 clique drop이 적어도 4이므로, Model M의 두 번 연속된 `(\tau,\Delta)=(3,3)`형 positive-defect pattern을 세 번째로 그대로 반복할 수 없다.

### 계산 환원

Codomain에 linear projection을 취해도 projected pairing이 nonzero인 pair는 원래 pairing도 nonzero다. 따라서 projected graph의 clique는 원래 graph의 clique다.

`W_0`에 injective이고 `z`를 죽이지 않는 projection

\[
\pi:\widetilde W\to\mathbb F_2^3
\]

을 택한다. Basis를 고르면 모든 projected extension은

\[
\begin{aligned}
\beta'((a,\alpha,\epsilon),(b,\gamma,\delta))
={}&\beta_0(a,b)
 +(\alpha\delta+\epsilon\gamma)z\\
&+\epsilon L(b)+\delta L(a)
\end{aligned}
\tag{4.2}
\]

꼴이다. 여기서

\[
z\in\mathbb F_2^3\setminus\{0\},
\qquad
L:V_0\to\mathbb F_2^3
\]

는 임의의 linear map이다. 따라서 정확히

\[
7\cdot2^{3\cdot4}=7\cdot4096=28{,}672
\]

cases가 있다.

Dependency-free verifier는 모든 case에서 exact target-clique search를 수행하고, 각각 explicit 10-clique를 찾은 뒤 모든 45 pairs를 다시 검사한다. 전체 witness stream의 SHA-256은

```text
51350b8afcaae75d302efbf08522c6f9b5a77a29f939d1212d07e1f8ecbc9140
```

이다.

### 범위 제한

이 theorem은 다음을 주장하지 않는다.

- arbitrary class-two extension의 완전한 분류;
- higher-class group에서 같은 반복이 불가능하다는 정리;
- `\mathfrak D_{\rm cen}=o(\nu)`의 보편 증명;
- Full FAL.

그 대신 가장 직접적인 binary elementary one-pair 반복 class를 완전히 소진하여, finite positive defect를 단순 block-extension으로 선형화하는 시도가 실패함을 인증한다.

---

## 5. Mixed model의 무한 exact extension

order-64 mixed model은 고립된 예가 아니다. 이는

\[
R_2=\mathbb F_2[\pi]/(\pi^2)
\]

위 rank-one Heisenberg group의 commutation geometry와 linearly equivalent하다.
더 일반적으로

\[
H_{q,m}=\operatorname{Heis}_3(\mathbb F_q[\pi]/(\pi^m))
\]

에 대해 다음 값들이 정확하다.

\[
\boxed{
\begin{aligned}
\nu(H_{q,m})=a_f(H_{q,m})=R_{\rm cen}(H_{q,m})
   &=q^{m-1}(q+1),\\
\tau_{\rm cen}(H_{q,m})&=q+1,\\
P_{\rm cen}(H_{q,m})&=(q+1)^m,\\
\mathfrak D_{\rm cen}(H_{q,m})
   &=m\log_2(q+1)-\frac12q^{m-1}(q+1).
\end{aligned}}
\]

완전한 primal/dual, projective-line clique/cover, 모든 child의 valuation
classification 및 dynamic proof는 `CHAIN_RING_FAMILY.md`에 있다.

이 정리는 mixed model의 양의 max-child defect가 자연 반복에서 선형
obstruction으로 성장하지 않음을 보인다. Binary case의 clique number는

\[
3,6,12,24,\ldots
\]

로 증가하며, deepest centralizer chain의 각 node에서 \(\tau=3\)이지만
available clique budget은 지수적으로 커진다. 표준 라이브러리 verifier는
\(m=1,2,3,4\)의 clique, commuting-line cover, \(\tau\) primal/dual, child
commutation equivalence와 order-64 basis change를 전수 확인한다.
