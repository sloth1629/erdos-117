[PROVED] The chain-ring family formulas below are computation-independent.

# 유한 chain ring Heisenberg 계열: 정확한 무한 audit

## 0. 목적과 판정

order-64 인증 모델에서 나타난

\[
\tau_{\rm cen}=3,\qquad \nu=6,\qquad P_{\rm cen}=9>2^{\nu/2}=8,
\qquad R_{\rm cen}=6
\]

패턴이 장기적으로 반복되어
\(\mathfrak D_{\rm cen}=\Omega(\nu)\)를 만드는지 확인한다.
그 자연스러운 전체 반복은 유한 chain ring 위 Heisenberg 군이다.
이 계열은 정확히 풀리며, 결론은 다음과 같다.

* max-child recursion은
  \(P_{\rm cen}(H_{q,m})=(q+1)^m\)이다.
* exact dynamic recursion은
  \(R_{\rm cen}(H_{q,m})=q^{m-1}(q+1)\)이다.
* clique number와 fractional abelian-cover optimum도
  \(q^{m-1}(q+1)\)이다.
* 따라서 이 자연 반복은 선형 defect obstruction이 아니다.
  특히 \(q=2,m=2\)에서만 보이는 양의 defect는 다음 층부터
  clique growth에 의해 상쇄된다.

이 문서는 계산에 의존하지 않는 완전한 증명을 적는다.

---

## 1. 군과 commutation model

\(q\)를 prime power,

\[
R_m=\mathbb F_q[\pi]/(\pi^m),\qquad J_m=\pi R_m
\]

라 하자. \(|R_m|=q^m\), \(|J_m|=q^{m-1}\)이다.
다음 Heisenberg 군을 둔다.

\[
H_{q,m}=R_m\times R_m\times R_m
\]

및

\[
(x,y,z)(x',y',z')
=(x+x',\ y+y',\ z+z'+xy').
\]

직접 계산하면

\[
[(x,y,z),(x',y',z')]
=(0,0,xy'-x'y).
\]

따라서

\[
Z(H_{q,m})=\{(0,0,z):z\in R_m\}
\]

이고 compressed commutation model은 \(R_m^2\) 위의 alternating form

\[
B((x,y),(x',y'))=xy'-x'y
\]

이다. 즉 서로 다른 center coset들은 정확히 determinant가 nonzero일 때
noncommute한다.

이 문서에서는 abelian terminal의 clique number를 0으로 두는 입력 packet의
convention을 따른다.

---

## 2. projective-line cover와 exact clique

### Theorem 2.1

\[
\boxed{
\nu(H_{q,m})
=a_f(H_{q,m})
=q^{m-1}(q+1).
}
\]

### 증명: commuting cover

chain ring의 projective line은 다음 free rank-one submodules로 쓸 수 있다.

\[
\mathcal L=
\{R_m(1,a):a\in R_m\}
\ \cup\
\{R_m(b,1):b\in J_m\}.
\]

개수는

\[
|R_m|+|J_m|=q^m+q^{m-1}=q^{m-1}(q+1).
\]

각 line은 determinant가 identically zero이므로 commuting set이다.
또 모든 nonzero \((x,y)\in R_m^2\)는 이들 중 하나에 속한다.
실제로 \(x,y\)의 최소 valuation을 뽑아 primitive pair로 만든 뒤,
첫 좌표가 unit이면 \(R_m(1,a)\), 그렇지 않으면 둘째 좌표가 unit이고
\(R_m(b,1)\)이며 이때 \(b\in J_m\)이다.

따라서 위 line들의 preimage는 abelian subgroup cover이고

\[
a_f(H_{q,m})\le q^{m-1}(q+1).
\]

### 증명: matching clique

다음 representatives를 잡는다.

\[
\mathcal S=
\{(1,a):a\in R_m\}
\ \cup\
\{(b,1):b\in J_m\}.
\]

첫 family 안의 서로 다른 두 원소의 determinant는 \(a'-a\ne0\),
둘째 family 안에서는 \(b-b'\ne0\)이다. Cross pair의 determinant는

\[
1-ab
\]

꼴이고 \(ab\in J_m\)이므로 이는 unit, 특히 nonzero다.
따라서 \(\mathcal S\)는 크기 \(q^{m-1}(q+1)\)의 pairwise-noncommuting
clique다.

clique dual lower bound와 위 abelian cover upper bound가 일치하므로
\(\nu=a_f=q^{m-1}(q+1)\)이다. ∎

---

## 3. centralizer-cover LP의 exact primal/dual

### Theorem 3.1

\[
\boxed{\tau_{\rm cen}(H_{q,m})=q+1.}
\]

### Primal feasibility

\(\mathbb P^1(\mathbb F_q)\)의 각 direction \(u\)에 대해 한 lift를 잡고

\[
x_u=\pi^{m-1}u\in R_m^2
\]

라 하자. \(x_u^\perp\)는 residue \(\bar v\in\mathbb F_q^2\)가
\(u\)와 orthogonal인 모든 \(v\)를 포함한다. 2차원 alternating space에서 nonzero residue vector는 정확히 한
projective direction과 orthogonal이고 zero residue vector는 모든 direction과
orthogonal이다. 따라서 이 \(q+1\) centralizers는 \(R_m^2\) 전체를 덮는다.
각각 weight 1을 주면 primal cost는 \(q+1\)이다.

### Dual feasibility

서로 다른 residue directions를 나타내는 primitive vectors

\[
\{u:u\in\mathbb P^1(\mathbb F_q)\}
\]

에 각각 dual weight 1을 준다. 서로 다른 두 lift \(u,v\)의 determinant는
unit이다. 따라서 nonzero \(x\)가 두 lift와 동시에 orthogonal이면,
\(u,v\)가 \(R_m^2\)의 basis이므로 \(x=0\)이어야 한다.
즉 어떤 noncentral element centralizer도 dual support를 둘 이상 포함하지
못한다. 모든 dual constraint는 1 이하이고 총 dual mass는 \(q+1\)이다.

Primal과 dual 값이 일치하므로 결론이 따른다. ∎

---

## 4. 모든 child의 정확한 형식

nonzero \(v\in R_m^2\)의 valuation을

\[
\operatorname{val}(v)=k,
\qquad 0\le k\le m-1,
\]

즉 \(v=\pi^k u\)이고 \(u\)가 primitive인 유일한 \(k\)로 둔다.
Primitive pair는 \(GL_2(R_m)\)의 한 basis vector로 완성되므로,
unit determinant coordinate change 후 \(v=\pi^k(1,0)\)만 보면 충분하다.

그 orthogonal은

\[
K_k=\{(a,b):\pi^k b=0\}
=R_m\times \pi^{m-k}R_m.
\]

restriction의 radical은

\[
\operatorname{rad}(B|_{K_k})
=\pi^kR_m\times\{0\}.
\]

\(b=\pi^{m-k}c\)로 쓰면

\[
(a,\pi^{m-k}c)
\longmapsto
(a\bmod \pi^k,\ c\bmod\pi^k)
\]

가 radical quotient를 \(R_k^2\)와 identify한다. 또한

\[
B((a,\pi^{m-k}c),(a',\pi^{m-k}c'))
=\pi^{m-k}(ac'-a'c),
\]

이므로 왼쪽이 \(R_m\)에서 0인 것과
\(ac'-a'c\)가 \(R_k\)에서 0인 것이 동치다.

따라서 valuation \(k\) 원소의 centralizer가 갖는 compressed commutation
model은 정확히 \(H_{q,k}\)의 model이다. 같은 center coset 안의 원소들은
동일한 centralizer와 동일한 recursive child를 가지므로, duplicate variables와
duplicate constraints를 합치면 \(\tau_{\rm cen},R_{\rm cen},P_{\rm cen}\)은 이
compressed model만으로 결정된다. 따라서 이 child의 세 recursion 값도
\(H_{q,k}\)의 값과 같다. \(k=0\)이면 child는 abelian이다.
특히 \(\pi^{m-1}(1,0)\)을 고르면

\[
H_{q,m}\longrightarrow H_{q,m-1}
\]

인 full-depth chain이 생긴다.

---

## 5. exact max-child recursion과 defect

\(P_m=P_{\rm cen}(H_{q,m})\), \(P_0=1\)이라 하자.
앞 절과 \(\tau_{\rm cen}=q+1\)에 의해

\[
P_m=(q+1)\max_{0\le k<m}P_k.
\]

귀납적으로 \(P_k=(q+1)^k\)이고 단조 증가하므로

\[
\boxed{P_{\rm cen}(H_{q,m})=(q+1)^m.}
\]

따라서

\[
\boxed{
\mathfrak D_{\rm cen}(H_{q,m})
=m\log_2(q+1)-\frac12q^{m-1}(q+1).
}
\]

특히 binary dual-number case \((q,m)=(2,2)\)에서는

\[
\mathfrak D_{\rm cen}
=2\log_2 3-3
=\log_2(9/8)>0.
\]

그러나 fixed \(q\)에서 \(m\to\infty\)이면

\[
\frac{\mathfrak D_{\rm cen}(H_{q,m})}
{\nu(H_{q,m})}
\longrightarrow -\frac12.
\]

따라서 이 자연스러운 반복은
\(\mathfrak D_{\rm cen}=\Omega(\nu)\)인 양의 obstruction family가 아니다.

---

## 6. exact dynamic recursion

### Theorem 6.1

\[
\boxed{
R_{\rm cen}(H_{q,m})
=a_f(H_{q,m})
=q^{m-1}(q+1).
}
\]

### 증명

Theorem 2.1과 일반 composition theorem으로

\[
q^{m-1}(q+1)=a_f(H_{q,m})\le R_{\rm cen}(H_{q,m}).
\]

반대로 각 projective line \(L\in\mathcal L\)의 primitive generator
\(u_L\)를 하나 고른다. Primitive vector의 centralizer는 정확히 그 free
rank-one line의 preimage이고 abelian이다. 모든 line-centralizer에 weight
1을 주면 \(H_{q,m}\) 전체를 cover하고, 모든 child cost는 1이다. 따라서

\[
R_{\rm cen}(H_{q,m})
\le |\mathcal L|
=q^{m-1}(q+1).
\]

양쪽이 일치한다. ∎

이 family에서는 \(\tau\)-optimal cover가 깊은 nilpotent child를 선택해
max-child 값을 만들지만, dynamic optimum은 더 큰 총 weight를 가진
primitive-line cover를 선택하여 즉시 abelian leaves로 끝낸다.
order-64 모델의 \(P=9\), \(R=6\) 차이는 이 일반 현상의 첫 nontrivial
instance다.

---

## 7. order-64 인증 모델과의 명시적 일치

\(q=2,m=2\)에서 coordinates를

\[
x=x_0+x_1\pi,\qquad y=y_0+y_1\pi
\]

로 쓰면 determinant의 constant/\(\pi\) coefficients는 두 alternating
forms \(B_0,B_1\)을 준다. Basis order
\((x_0,x_1,y_0,y_1)\)에서

\[
B_0:\ (0,2),
\qquad
B_1:\ (0,3),(1,2)
\]

가 nonzero off-diagonal pairs다.

`certificates.json`의 mixed model matrices \(M_0,M_1\)은 다음 binary
basis matrix

\[
P=
\begin{pmatrix}
0&0&1&0\\
1&0&0&0\\
0&1&1&1\\
0&0&0&1
\end{pmatrix}
\]

에 대해

\[
M_0=P^TB_1P,
\qquad
M_1=P^T(B_0+B_1)P
\]

을 만족한다. 따라서 두 models는 domain과 codomain의 invertible linear
change 아래 같은 commutation geometry다. 이 identity는
`verify_certificate.py`가 exact mod-2 arithmetic으로 재검사한다.

---

## 8. 이 family가 말해 주는 정확한 경계

1. \(\tau_{\rm cen}=3\)이고 clique drop이 3인 양의 local defect가 두 번
   나타나는 현상은 실제이며 우연한 solver artifact가 아니다.
2. 그러나 이를 가장 자연스럽게 계속 연장하면 clique number가
   \(3\cdot2^{m-1}\)로 증가한다.
3. max-child defect는 선형 양수가 되지 않고 결국 큰 음수가 된다.
4. dynamic LP는 모든 \(m\)에서 exact fractional optimum을 회수한다.

따라서 이 계열은 Goal C의 obstruction이 아니라,
“작은 양의 local defect를 그대로 반복하면 된다”는 후보 obstruction을
정확히 제거하는 무한-family audit이다.
