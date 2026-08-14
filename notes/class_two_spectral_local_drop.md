# QLD spectral-overlap 정리의 적대적 감사와 faithful binary 영역의 강화

이 문서는 다음 부분정리를 독립 재구성하고 강화한 통합본이다. 아래의
“첨부 정리”라는 표현은 이 절에 적은 정리를 가리킨다.

## 설정과 원 weighted theorem

유한 class-two \(p\)-group \(P\)와 \(x\notin Z(P)\)에 대해

\[
H=C_P(x),\quad m=\nu(P),\quad c=\nu(H),\quad
\delta=m-c,\quad D=[x,P],\quad q=|D|=[P:H]
\]

로 둔다. Full quadratic local-drop conjecture, 즉 QLD는

\[
q\le4(\delta+1)^2
\tag{QLD}
\]

이다. 이 문서는 QLD 전체를 증명하지 않는다.

군 준동형 \(\Theta:P'\to E\)를 택하되
\(E=\Theta(D)\cong\mathbf F_p^d\), \(|E|=Q=p^d>1\)이라 하자. 기저
\(e_1,\ldots,e_d\)와 \(\Theta([x,y_j])=e_j\)인 lift \(y_j\in P\)를
택하고

\[
y(u)=y_1^{u_1}\cdots y_d^{u_d}
\qquad(u\in\mathbf F_p^d)
\]

로 둔다. \(A\subseteq H\)는 크기 \(c\)인 최대 noncommuting clique이고,

\[
T_a(u)=\Theta([a,y(u)])\qquad(a\in A)
\]

로 둔다. \(J\subseteq A\)와 각 \(a\in J\)에 대한 \(\mathbf F_p\) 위의
확률분포 \(\pi_a\)를 택하고, \(u\ne0\)에 대해

\[
\eta_{a,\pi_a}(u)=
\begin{cases}
1-\pi_a(-\lambda),&T_a(u)=\lambda u\text{ for some }\lambda\in\mathbf F_p,\\
1,&T_a(u)\notin\mathbf F_pu,
\end{cases}
\qquad
W_{J,\pi}(u)=\prod_{a\in J}\eta_{a,\pi_a}(u).
\]

\(d=\ell p+r\), \(0\le r<p\)로 쓰고

\[
\gamma_{p,d}
=\frac{(p-r)p^{-\ell}+rp^{-\ell-1}}p.
\tag{1}
\]

### [PROVED] Weighted spectral-shift inequality

위의 모든 선택에 대해

\[
\boxed{
\delta\ge
\left\lceil
\gamma_{p,d}\sum_{u\ne0}W_{J,\pi}(u)
\right\rceil-(c-|J|).
}
\tag{2}
\]

특히 \(\gamma_{p,d}\ge Q^{-1/p}\)이다. 이 명제는 \(P\)나 \(D\)가
exponent \(p\)라고 가정하지 않으며, \(H\)가 비가환이어도 성립한다.

\(T_a\)가 \(\mathbf F_p\)의 모든 고유값을 가지면 saturated라 하고

\[
\mathcal S=\{a\in A:\operatorname{Spec}_p(T_a)=\mathbf F_p\},
\qquad s=|\mathcal S|,
\]

\[
t_R(u)=|\{a\in R:T_a(u)\in\mathbf F_pu\}|
\qquad(R\subseteq\mathcal S)
\tag{4}
\]

로 둔다. (2)에 균등분포와 missing-eigenvalue shift를 넣으면

\[
\delta\ge
\max_{R\subseteq\mathcal S}
\left\{
\left\lceil\gamma_{p,d}\sum_{u\ne0}
\left(1-\frac1p\right)^{t_R(u)}\right\rceil-(s-|R|)
\right\},
\tag{5}
\]

\[
\delta\ge B_{p,d}(Q)-s,
\qquad
B_{p,d}(Q)=\left\lceil(Q-1)\gamma_{p,d}\right\rceil,
\tag{6}
\]

그리고

\[
\delta\ge
\left\lceil\gamma_{p,d}\sum_{u\ne0}
\left(1-\frac1p\right)^{t_{\mathcal S}(u)}\right\rceil
\tag{7}
\]

을 얻는다. \(\Theta|_D\)가 단사인 faithful 경우에는 \(Q=q\)이고,
다음 조건만으로도 QLD가 성립한다.

\[
s\le B_{p,d}(q)+1-\left\lceil\frac{\sqrt q}{2}\right\rceil.
\tag{12}
\]

Faithful elementary quotient가 존재할 정확한 필요충분조건은 아래에서
증명하는 \(D\cap(P')^p=1\)이다. \(x\in Z(P)\)인 경계에서는
\((q,\delta)=(1,0)\)이므로 QLD가 자명하다.

**Source provenance.** 원 partial-theorem attachment와 hostile audit의
SHA-256은 각각

```text
7e5323ec9e12cd635a33b7ec4c4c876d332173c10b8d11cd12464348abbb811a  qld_spectral_shift_partial_theorem.txt
65ca3e888c74b336f9f8c65763882b667a3425906cd4f69a8d7d9cca2208dd48  QLD_HOSTILE_AUDIT_AND_REFINEMENT.md
```

이다. 이 통합본은 저장소의 evidence label과 현재 artifact 경로에 맞게
정규화했다.

## 0. 결론 요약

**[PROVED]** 첨부된 weighted spectral-shift 정리의 핵심 부등식

\[
\delta\ge
\left\lceil\gamma_{p,d}
\sum_{u\ne0}W_{J,\pi}(u)\right\rceil-(c-|J|)
\]

에는 치명적인 논리적 공백이 없다. 임의 지수 class-two 군에서의 선형화, affine-layer 공식, Caro–Wei 제한, 정확한 \(\gamma_{p,d}\), 독립적인 \(x\)-shift, 천장 처리, faithful 조건의 사용 방향이 모두 성립한다.

**[PROVED]** 다만 기존 포화형 (5)–(7)은 포화 연산자의 \(0/1\) 고유공간 **라벨을 버리고 균등 shift만 사용**하므로 상당히 비최적이다. 정리 (2)에 deterministic shift를 직접 대입하면 다음의 더 강한 방향성 고유공간 합집합 부등식을 얻는다.

\[
\boxed{
\delta\ge
\left\lceil
\gamma_{2,d}\bigl(q-1-|\bigcup_{a\in\mathcal S}E_a^{\varepsilon_a,\times}|\bigr)
\right\rceil
}
\tag{O}
\]

여기서 \(E_a^\lambda=\ker(T_a-\lambda I)\), \(E_a^{\lambda,\times}=E_a^\lambda\setminus\{0\}\), 그리고 \(\varepsilon_a\in\{0,1\}\)는 각 포화 연산자마다 독립적으로 선택한다.

**[PROVED]** \(h_a=\min\{\dim E_a^0,\dim E_a^1\}\)라 하면

\[
\boxed{
\delta\ge
\left\lceil
\gamma_{2,d}
\left(q-1-
\sum_{a\in\mathcal S}(2^{h_a}-1)
\right)_+
\right\rceil .
}
\tag{O1}
\]

특히 \(h_a\le\lfloor d/2\rfloor\)이므로

\[
\boxed{
\delta\ge
\left\lceil
\gamma_{2,d}
\left(q-1-s(2^{\lfloor d/2\rfloor}-1)
\right)_+
\right\rceil .
}
\tag{O2}
\]

**[PROVED]** 짝수 \(d\ge4\), \(n=\sqrt q=2^{d/2}\)에서는 (O2)가

\[
s\le \frac n2+2
\quad\Longrightarrow\quad
\delta\ge\frac n2-1
\quad\Longrightarrow\quad
q\le4(\delta+1)^2
\]

를 준다. 따라서 faithful binary QLD 반례는 기존의 \(s\ge n/2+2\)가 아니라 반드시

\[
\boxed{s\ge n/2+3}
\]

을 만족해야 한다.

**[PROVED]** 기존 (16)–(18)은 옳지만 천장과 \(\delta\)의 정수성을 끝까지 사용하지 않아 약하다. \(L=\lceil\sqrt q/2\rceil-1\)라 두면 QLD 반례는 \(\delta\le L-1\)이고, 따라서

\[
\boxed{
\sum_{u\ne0}2^{-t_{\mathcal S}(u)}
\le \frac{L-1}{\gamma_{2,d}}.
}
\tag{I}
\]

짝수 \(d\), \(n=\sqrt q\)에서는

\[
\boxed{
\sum_{u\ne0}2^{-t_{\mathcal S}(u)}
\le \frac q2-2\sqrt q,
\qquad
|\{u\ne0:t_{\mathcal S}(u)\ge2\}|
\ge4\sqrt q-1.
}
\tag{I-even}
\]

이는 첨부 정리의 \(q/2-\sqrt q\), \(2\sqrt q-1\)보다 강하다.

**[PROVED]** \(q=64\)인 faithful binary 경우에는 더 강한 global-clique 논증이 가능하다. QLD 반례라면 \(\delta=2\)이고, 모든 서로 다른 비영 방향 \(u,v\in\mathbf F_2^6\)를 어떤 포화 연산자가 서로 반대 고유값으로 분리해야 한다. 이 pair-separation 조건은 최소 \(41\)개의 포화 연산자를 요구한다. 따라서

\[
\boxed{q=64,\ Q=q,\ c=\nu(H)\le40\quad\Longrightarrow\quad\text{QLD}.}
\]

**[COMPUTED]** 반면, 기존의 **라벨 없는** robust-overlap 조건 자체는 실제 한 alternating commutator map과 최대 \(H\)-clique에서 발생할 수 있다. 아래에 order \(32768\), class two, \(q=32\), \(c=5\)인 normalized-cocycle 예를 주며, 그 예는 기존 (13), (16), (18)의 robust 조건을 만족하지만 oriented shift로 즉시 제거된다. 따라서 “한 교환자 map에서 동시에 나옴”, “최대 \(H\)-clique에서 인덱싱됨”, “class-two bilinearity”만으로 라벨 없는 overlap을 금지하는 전략은 성립하지 않는다.

**[PROVED]** 이 결과는 full QLD나 Erdős Problem 117의 해결을 주장하지 않는다. faithful binary 영역에서 가장 작은 정확한 잔여 장애물은 아래 §8의 \(q=64,c\ge41,\delta=2\) pair-separating eigenspace system이며, arbitrary-exponent에서 elementary quotient에 보이지 않는 층은 별도로 남는다.

---

## 1. 첨부 정리의 적대적 재구성

### 1.1 임의 지수에서 \(T_a\)의 선형성

**[PROVED]** Class two에서 모든 교환자는 중심에 있으므로

\[
[a,y_1^{u_1}\cdots y_d^{u_d}]
=
\prod_{j=1}^d[a,y_j]^{u_j}.
\]

\(E\)의 지수가 \(p\)이므로 지수의 carry는 \(\Theta\) 뒤에서 사라지고

\[
T_a(u)=\sum_j u_j\Theta([a,y_j])
\]

가 된다. 따라서 \(P\)나 \(D\)가 exponent \(p\)일 필요 없이 \(T_a\)는 \(\mathbf F_p\)-선형이다. 단면 \(u\mapsto y(u)\)가 군 준동형일 필요도 없다.

**[PROVED]** 같은 전개로

\[
F(u,v)=\Theta([y(u),y(v)])
=
\sum_{i,j}u_iv_j\Theta([y_i,y_j])
\]

는 alternating bilinear map이다. 특히 \(F(u,u)=0\)이다.

### 1.2 affine layer 공식과 닫힌 이웃

**[PROVED]** 일반적인 두 layer 원소에 대해

\[
\Theta([x^\alpha y(u),x^\beta y(v)])
=
\alpha v-\beta u+F(u,v).
\tag{1.2.1}
\]

같은 layer \(\alpha=\beta\)에서는

\[
\Theta([x^\alpha y(u),x^\alpha y(v)])
=
\alpha(v-u)+F(u,v).
\]

\(v=u+w\)로 쓰면 \((F_u+\alpha I)w\)이고, 따라서 projected-commuting graph \(\Gamma_\alpha\)에서

\[
N_{\Gamma_\alpha}[u]
=u+\ker(F_u+\alpha I),
\qquad
|N_{\Gamma_\alpha}[u]|=p^{k_\alpha(u)}.
\]

### 1.3 Caro–Wei의 부분집합 제한

**[PROVED]** 유도부분그래프 \(\Gamma_\alpha[S]\)에서

\[
\deg_{\Gamma_\alpha[S]}(u)+1
\le p^{k_\alpha(u)}.
\]

Caro–Wei에 의해

\[
\alpha(\Gamma_\alpha[S])
\ge
\sum_{u\in S}\frac1{\deg_S(u)+1}
\ge
\sum_{u\in S}p^{-k_\alpha(u)}.
\]

이 독립집합은 projected commutator가 비영인 집합이므로 실제 군에서도 pairwise noncommuting이다. 증명은 projected commuting을 actual commuting으로 잘못 역추론하지 않는다.

### 1.4 정확한 \(\gamma_{p,d}\)

**[PROVED]** 고정 \(u\ne0\)에 대해 \(\ker(F_u+\alpha I)\)들은 서로 다른 고유값의 고유공간이므로 직합이고

\[
\sum_{\alpha\in\mathbf F_p}k_\alpha(u)\le d.
\]

또한 \(F_u(u)=F(u,u)=0\)이므로

\[
k_0(u)\ge1.
\]

고정된 정수합 아래 convex 함수 \(p^{-k}\)의 합은 차원들을 가능한 한 균등하게 배분할 때 최소이다. \(d=\ell p+r\), \(0\le r<p\)이면

\[
\gamma_{p,d}
=
\frac{(p-r)p^{-\ell}+rp^{-\ell-1}}p.
\]

\(d<p\)일 때도 \(k_0=1\)을 \(r=d\)개의 1 중 하나로 배치할 수 있으므로 제약과 양립한다. 따라서 첨부된 정확한 정수 상수는 맞다.

### 1.5 최대 clique의 독립적인 \(x\)-shift

**[PROVED]** \(a\in H\)이면

\[
\Theta([a x^r,x^\alpha y(u)])=T_a(u)+ru.
\]

서로 다른 \(a,b\in A\)에 대해 shift를 독립적으로 골라도

\[
[a x^r,b x^s]=[a,b]\ne1
\]

이므로 old clique는 보존된다. 또한 \(a x^r\in H\)이고 \(u\ne0\)인 affine 원소는 \(H\) 밖이므로 원소 중복도 없다.

### 1.6 천장과 기존 귀결

**[PROVED]** 기대값이 \(M\) 이상이면 어떤 실제 \((\alpha,\mathbf r)\)에서 Caro–Wei 실수 하한이 \(M\) 이상이고, clique 크기는 정수이므로 \(\lceil M\rceil\)을 얻는다. 첨부 정리 (2)의 천장 위치는 맞다.

**[PROVED]** \(s=0\), \(s\le\delta+1\), 그리고 (12)의 충분조건에 대한 계산은 모두 유효하다. 특히

\[
\delta+s+1>
q^{1-1/p}
\]

의 strict inequality는 \(+1>q^{-1/p}\)에서 나온다.

**[PROVED]** 다만 binary 반례 부분에서는

\[
q>4(\delta+1)^2
\]

와 \(\delta\in\mathbf Z\)를 끝까지 사용하면 §3의 더 강한 (I)를 얻는다. 따라서 기존 (16)–(18)은 거짓이 아니라 비최적이다.

### 1.7 faithful 조건의 정확한 범위

**[PROVED]** 고정된 \(\Theta\)에 대해

\[
Q=q
\quad\Longleftrightarrow\quad
\ker\Theta\cap D=1.
\]

**[PROVED]** faithful elementary quotient가 존재할 필요충분조건은

\[
\boxed{D\cap(P')^p=1.}
\tag{1.7.1}
\]

필요성은 exponent-\(p\) 군으로 가는 모든 homomorphism이 \((P')^p\)를 죽인다는 사실에서 따른다. 역으로 (1.7.1)이면 자연사상

\[
P'\longrightarrow P'/(P')^p
\]

이 \(D\) 위에서 단사이다. 그 image \(\bar D\)에 대한 선형 retraction을 택해 합성하면 faithful \(\Theta:P'\to\bar D\)를 얻는다.

**[PROVED]** 따라서 faithful 경우에는 \(D\) 자체가 elementary abelian이어야 한다. 첨부 정리의 “\(P'\)가 elementary abelian” 및 “\(D\)가 elementary direct summand”는 올바른 충분조건이며, (1.7.1)이 정확한 판정이다.

---

## 2. 새 방향성 eigenspace-union 정리

### 2.1 정확한 정리

**[PROVED]** \(p=2\), \(Q=q=2^d\)라 하자. 각 \(a\in\mathcal S\)와 \(\lambda\in\{0,1\}\)에 대해

\[
E_a^\lambda=\ker(T_a-\lambda I),
\qquad
E_a^{\lambda,\times}=E_a^\lambda\setminus\{0\}
\]

로 둔다. 임의의 선택 \(\varepsilon=(\varepsilon_a)_{a\in\mathcal S}\)에 대해 (O)가 성립한다.

### 2.2 증명

**[PROVED]** \(a\notin\mathcal S\)에는 missing eigenvalue \(\mu_a\)가 있으므로 deterministic shift \(r_a=\mu_a\)를 택하면 모든 \(u\ne0\)에 대해 \(T_a(u)+r_au\ne0\)이다.

**[PROVED]** \(a\in\mathcal S\)에는 \(r_a=\varepsilon_a\)를 택한다. 이 old vertex와 projected commute하는 비영 방향은 정확히 \(E_a^{\varepsilon_a,\times}\)이다. 따라서 정리 (2)에 \(J=A\)와 point-mass 분포들을 넣으면

\[
W_{A,\pi}(u)
=
\mathbf1\left
\{u\notin\bigcup_{a\in\mathcal S}E_a^{\varepsilon_a,\times}
\right\}
\]

이고 penalty \(c-|J|\)는 0이다. 이것이 (O)를 준다.

**[PROVED]** 각 \(a\)에서 더 작은 고유공간을 고르면 합집합 크기는

\[
\left|\bigcup_aE_a^{\varepsilon_a,\times}\right|
\le
\sum_a(2^{h_a}-1)
\]

이므로 (O1)이 따른다. 서로 다른 고유공간의 차원합이 \(d\) 이하이므로 \(h_a\le\lfloor d/2\rfloor\), 따라서 (O2)가 따른다.

### 2.3 기존 충분범위와의 비교

**[COMPUTED]** 다음 표는 첨부 정리 (12)가 보장하던 최대 \(s\)와 (O2)가 보장하는 최대 \(s\)를 비교한다.

| \(d\) | \(q\) | 기존 최대 \(s\) | oriented-union 최대 \(s\) |
|---:|---:|---:|---:|
| 4 | 16 | 3 | 4 |
| 5 | 32 | 4 | 8 |
| 6 | 64 | 5 | 6 |
| 7 | 128 | 7 | 12 |
| 8 | 256 | 9 | 10 |
| 9 | 512 | 13 | 19 |
| 10 | 1024 | 17 | 18 |
| 11 | 2048 | 26 | 37 |
| 12 | 4096 | 33 | 34 |
| 13 | 8192 | 51 | 70 |
| 14 | 16384 | 65 | 66 |
| 15 | 32768 | 102 | 138 |

**[PROVED]** 짝수 \(d\)에서는 정확히 한 단계가 개선된다. \(n=\sqrt q\)라 하면 기존 충분조건은 \(s\le n/2+1\), 새 조건은

\[
s\le n/2+2.
\]

**[PROVED]** 홀수 \(d\)에서는 고유공간의 작은 쪽이 \(2^{(d-1)/2}-1\)개 비영 벡터밖에 포함하지 못한다는 사실 때문에 개선폭이 더 크다.

---

## 3. binary overlap 부등식의 정수 강화

\[
L_d=\left\lceil\frac{\sqrt q}{2}\right\rceil-1
\]

로 둔다. 이는 QLD를 보장하는 최소 정수 \(\delta\)이다.

**[PROVED]** QLD가 실패하면 \(\delta\le L_d-1\)이다. (7)에서

\[
\delta\ge
\left\lceil
\gamma_{2,d}
\sum_{u\ne0}2^{-t_{\mathcal S}(u)}
\right\rceil
\]

이므로 (I)가 따른다.

**[PROVED]** 따라서

\[
|\{u\ne0:t(u)=0\}|
\le
\left\lfloor\frac{L_d-1}{\gamma_{2,d}}\right\rfloor
\]

이고

\[
|\{u\ne0:t(u)\ge2\}|
\ge
q-1-
\left\lfloor\frac{2(L_d-1)}{\gamma_{2,d}}\right\rfloor.
\]

**[PROVED]** 방향성 버전 (O)을 같은 방식으로 사용하면 QLD 반례에서 모든 orientation \(\varepsilon\)가

\[
\boxed{
\left|\bigcup_{a\in\mathcal S}E_a^{\varepsilon_a,\times}\right|
\ge
q-1-
\left\lfloor\frac{L_d-1}{\gamma_{2,d}}\right\rfloor
}
\tag{C}
\]

을 만족해야 한다. 이는 “많은 방향에서 두 eigenspace가 겹친다”보다 강한, eigenvalue 라벨을 보존하는 transversal-cover 조건이다.

**[PROVED]** 짝수 \(d\), \(n=\sqrt q\)에서는

\[
L_d-1=n/2-2,
\qquad
\gamma_{2,d}=1/n,
\]

이므로 모든 orientation이 적어도

\[
\boxed{q/2+2\sqrt q-1}
\]

개의 비영 방향을 덮어야 한다.

---

## 4. cyclic-shift lemma와 \(q\le32\)의 폐쇄

**[PROVED]** \(e=\exp D\)라 하자. \([x,y]=z\)가 order \(e\)인 \(y\)를 택한다. 최대 \(H\)-clique \(A\)의 각 \(a\)에 대해

\[
[a x^r,x^j y]=[a,y]z^r
\]

가 1이 되지 않도록 \(r=r_a\pmod e\)를 고를 수 있다. 금지되는 \(r\)은 최대 하나이고 \(e\ge2\)이다.

**[PROVED]** \(\{a x^{r_a}:a\in A\}\)는 여전히 \(c\)-clique이고

\[
\{x^j y:0\le j<e\}
\]

는 \([x^i y,x^j y]=z^{i-j}\)에 의해 \(e\)-clique이다. 두 부분 사이도 모두 noncommuting이므로

\[
\boxed{\delta\ge\exp D.}
\tag{E}
\]

**[PROVED]** faithful binary 경우 \(D\)는 elementary abelian이고 \(\exp D=2\)이므로 \(\delta\ge2\)이다. 따라서 \(q\le32\)에서는

\[
q\le32\le4(2+1)^2=36
\]

이고 QLD가 성립한다.

---

## 5. 첫 짝수 잔여값 \(q=64\): pair separation과 \(s\ge41\)

### 5.1 \(\delta=2\)

**[PROVED]** \(q=64\)에서 QLD가 실패하면 \(\delta\le2\). (E)에 의해 \(\delta\ge2\)이므로

\[
\boxed{\delta=2.}
\]

### 5.2 모든 방향쌍의 opposite-eigenvalue separation

**[PROVED]** 서로 다른 \(u,v\in E^\times\)를 고른다. 어떤 포화 연산자도 \(u,v\)를 서로 다른 고유값으로 보지 않는다고 가정한다.

**[PROVED]** 각 old vertex에 대해 다음과 같이 shift를 고를 수 있다.

- unsaturated \(T_a\): missing eigenvalue shift를 사용하여 모든 방향을 피한다;
- saturated \(T_a\): \(u\) 또는 \(v\)가 eigenvector이면 그 eigenvalue와 반대 shift를 택한다. 두 방향이 모두 eigenvector이면 가정에 의해 eigenvalue가 같으므로 하나의 shift가 둘 다 피한다.

따라서 shifted maximum \(H\)-clique 전체가 \(u,v\) 두 방향과 projected-noncommuting이 된다.

**[PROVED]** 세 outside 원소

\[
y(u),\qquad xy(u),\qquad x^\beta y(v)
\]

중 적절한 \(\beta\in\{0,1\}\)를 택하면 pairwise noncommuting이다. 첫 두 원소의 projected commutator는 \(u\ne0\)이다. 나머지 두 commutator는

\[
F(u,v)+\beta u,
\qquad
F(u,v)+v+\beta u.
\]

\(\beta=0\)이 실패하려면 \(F(u,v)\in\{0,v\}\), \(\beta=1\)이 실패하려면 \(F(u,v)\in\{u,u+v\}\)여야 한다. 두 집합은 서로소이므로 적어도 한 \(\beta\)가 성공한다.

**[PROVED]** 그러면 크기 \(c+3\)인 clique가 생겨 \(\delta=2\)와 모순이다. 따라서 모든 unordered pair \(\{u,v\}\subset E^\times\)에 대해 어떤 \(a\in\mathcal S\)가

\[
u\in E_a^0,\ v\in E_a^1
\quad\text{또는}\quad
u\in E_a^1,\ v\in E_a^0
\]

를 만족한다.

**[PROVED]** 동치로, saturated eigenspace pair들은 \(E^\times\)의 모든 두 점을 분리한다. 따라서 어떤 orientation으로 각 연산자의 한 eigenspace를 골라도 덮이지 않은 방향은 최대 하나이다. 특히

\[
\sum_{u\ne0}2^{-t_{\mathcal S}(u)}\le1.
\]

### 5.3 용량 계산과 40개 경우의 제거

**[PROVED]** 한 포화 연산자의 고유공간 차원을 \(k_0,k_1\)이라 하면 이 연산자가 분리할 수 있는 unordered pair 수는

\[
(2^{k_0}-1)(2^{k_1}-1).
\]

\(k_0,k_1\ge1\), \(k_0+k_1\le6\)이므로 최대값은 \((7)(7)=49\)이다. 총 pair 수는

\[
\binom{63}{2}=1953.
\]

따라서 우선 \(s\ge40\)이다.

**[PROVED]** \(s=40\)이라 가정하면 총 최대용량은 \(1960\)이고 slack은 7뿐이다. 차원형별 최대용량은

\[
(1,5):31,
\qquad
(2,4):45,
\qquad
(3,3):49.
\]

따라서 가능한 경우는 다음 둘뿐이다.

1. 40개 모두 \((3,3)\);
2. 39개가 \((3,3)\), 하나가 \((2,4)\).

**[PROVED]** 첫 경우, 한 방향은 각 포함 연산자에서 최대 7개의 다른 방향과 분리되므로 62개 모두를 분리하려면 최소 9개 연산자에 포함되어야 한다. 필요한 point-operator incidence는 \(63\cdot9=567\)인데 공급량은 \(40\cdot14=560\)뿐이다.

**[PROVED]** 둘째 경우, 특별한 \((2,4)\) 연산자의 3점 쪽에 있는 점은 balanced 연산자 7개가 추가로 필요하고, 15점 쪽의 점은 9개, 특별 연산자 밖의 45점도 9개가 필요하다. 필요한 balanced incidence는

\[
3\cdot7+15\cdot9+45\cdot9=561
\]

인데 39개 balanced 연산자의 공급량은 \(39\cdot14=546\)이다.

**[PROVED]** 따라서

\[
\boxed{s\ge41.}
\]

**[PROVED]** \(s\le c\)이므로 \(q=64\), \(Q=q\), \(c\le40\)인 모든 경우에 QLD가 성립한다.

---

## 6. 라벨 없는 robust overlap의 실제 군 실현

### 6.1 normalized multiplication law

\[
V=\mathbf F_2^{10},
\qquad
W=\mathbf F_2^5
\]

로 두고, \(V\)의 순서 있는 기저를

\[
x,a_1,a_2,a_3,a_4,y_0,y_1,y_2,y_3,y_4
\]

로 둔다. \(W\)의 기저는 \(e_0,\ldots,e_4\)이다.

**[PROVED]** alternating bilinear map \(\beta:V\times V\to W\)를 다음 기본값으로 정의한다.

\[
\beta(x,y_j)=e_j,
\]

\[
\beta(a_i,a_j)=e_0\quad(1\le i<j\le4),
\]

\[
\beta(a_i,y_i)=e_i\quad(1\le i\le4),
\]

나머지 기본값은 0이다.

**[PROVED]** 순서 있는 기저를 \(b_0,\ldots,b_9\)라 쓰고

\[
c(v,w)=
\sum_{i<j}v_jw_i\,\beta(b_i,b_j)
\]

로 두면 \(c\)는 normalized bilinear cocycle이고

\[
c(v,w)+c(w,v)=\beta(v,w).
\]

따라서

\[
(v,z)(w,t)=
(v+w,z+t+c(v,w))
\]

는 characteristic two에서 올바른 normalized multiplication law이다. alternating map 자체를 cocycle로 사용하지 않았다.

### 6.2 군 자료

**[COMPUTED]** 이 군은 order

\[
|P|=2^{10+5}=32768
\]

이고, \(\beta\)의 radical은 0이므로

\[
Z(P)=W,
\qquad |Z(P)|=32,
\]

nilpotency class는 정확히 2이다.

**[PROVED]** \(D=[x,P]=W\)이므로

\[
q=|D|=32,
\qquad P'=D.
\]

**[PROVED]** \(H=C_P(x)\)의 비중심 quotient는 \(U=\langle a_1,\ldots,a_4\rangle\)이고, 그 alternating scalar form의 Gram matrix는 대각 0, 비대각 1이다. 집합

\[
A=\{a_1,a_2,a_3,a_4,a_1+a_2+a_3+a_4\}
\]

는 5-clique이다. pairwise-nonorthogonal \(r\)-tuple의 Gram matrix rank는 \(r\) (짝수 \(r\)) 또는 \(r-1\) (홀수 \(r\))이므로 \(r\le5\). 따라서

\[
\nu(H)=5.
\]

### 6.3 spectral data

**[PROVED]** 자연 basis와 lift에 대해

\[
T_{a_i}=\operatorname{diag}(0,0,\ldots,1_i,\ldots,0),
\]

그리고

\[
T_{a_1+\cdots+a_4}=\operatorname{diag}(0,1,1,1,1).
\]

다섯 연산자는 모두 saturated이다.

**[COMPUTED]** 비영 \(u\in\mathbf F_2^5\)에 대한 \(t(u)\) 분포는

\[
\begin{array}{c|ccccc}
t&0&1&2&3&5\\\hline
\#u&1&5&10&10&5
\end{array}
\]

이고

\[
\sum_{u\ne0}2^{-t(u)}=\frac{237}{32},
\qquad
|\{u:t(u)\ge2\}|=25.
\]

**[PROVED]** \(q=32\), \(B_{2,5}=6\)이므로

\[
s=5>7-\frac{\sqrt{32}}2,
\]

\[
\frac{237}{32}<16-\sqrt{32},
\]

\[
25>2\sqrt{32}-1.
\]

따라서 첨부 정리의 라벨 없는 robust-overlap 조건들이 실제 최대 \(H\)-clique에서 동시에 실현된다.

**[PROVED]** 그러나 각 연산자의 더 작은 eigenspace를 고르면 다섯 coordinate line만 나쁜 집합이 된다. 따라서 31개 비영 방향 중 26개가 남고

\[
\delta\ge
\left\lceil\frac3{16}\cdot26\right\rceil
=5
\]

가 (O)에서 즉시 나온다.

**[PROVED]** 실제로 \(F=0\)이므로 affine layer

\[
\{x y(u):u\in\mathbf F_2^5\}
\]

자체가 32-clique이다. 따라서 \(m\ge32\), \(c=5\), \(\delta\ge27\)이고 QLD와는 거리가 멀다.

**[PROVED]** 이 예는 robust overlap이 group-realizability 때문에 자동으로 사라진다는 주장을 반박하지만, QLD 반례는 아니다.

---

## 7. 첨부된 order-512 선형 local-drop 반례의 검증

**[COMPUTED]** 첨부된 `verify_class_two_local_drop_counterexample.py`와 regression test를 실행했고 모두 통과했다. 인증값은

\[
|P|=512,
\quad |Z(P)|=16,
\quad q=16,
\quad \nu(P)=15,
\quad \nu(H)=1,
\quad \delta=14.
\]

따라서 \(q\le\delta\)와 \(q\le\delta+1\)은 모두 실패한다.

**[PROVED]** 이 예에서는

\[
16\le4(14+1)^2
\]

이므로 QLD를 반박하지 않는다. 또한 triangular normalized cocycle과 15-clique/15-class commuting partition이 모두 인증되어 characteristic-two cocycle 오류나 optimizer-only upper bound 문제는 없다.

### 7.1 원 packet의 embedded spectral stress verifier

**[UNVERIFIED]** 원 audit에서는 partial-theorem attachment의 §5 코드
블록을 추출해 66개의 nonzero dual subspace 전부에서 동일한 outcome과
worst ratio \(2/9\)를 재현했다고 보고했다. 그러나 standalone source와
일치하는 provenance hash가 없으므로 이 계산은 저장소 `[COMPUTED]`
증거로 승격하지 않는다. 본 문서의 proved theorem은 이 stress test에
의존하지 않는다.

**[DISPROVED]** 다만 문서에 적힌 SHA-256

`d8b9bfa4bb9d1e82402ffa693b61797df4f4aa71bf09e6c7bff214c23fcde2ef`

은 packet 안의 코드 블록 자체의 hash와 일치하지 않는다. 코드 첫 개행을 제거하고 LF로 저장한 실행 파일의 hash는

`dd9d1b77615132615d18d5f0195908c55f1d6a0a51fa48f6bf0a08ea82d21301`

이고, fence 내부 raw text의 hash는

`226a9ddb8525e179b3bab199d41e633d4d5432f5462c15770a06f7a1b9e38b0a`

이다. 원래 링크된 standalone 파일이 packet에 없으므로, 계산 결과는 재현되지만 기재된 provenance hash는 이 packet만으로 인증되지 않는다.

---

## 8. 가장 작은 정확한 잔여 장애물

**[PROVED]** faithful binary 영역에서 \(q\le32\)는 (E)로 닫힌다.

**[PROVED]** 다음 값 \(q=64\)에서 \(c\le40\)도 닫힌다.

**[PROVED]** 따라서 이 분석 뒤의 가장 작은 정확한 잔여 후보는 다음 자료를 동시에 갖는 실제 군이다.

\[
q=Q=64,
\qquad
D\cong\mathbf F_2^6,
\qquad
\delta=2,
\qquad
c\ge41.
\]

그리고 모든 허용되는 faithful projection/basis/lift/maximum clique 선택에서 다음이 유지되어야 한다.

1. 포화 연산자가 최소 41개이다.
2. 그 \(0/1\) eigenspace pair들이 63개 비영 방향의 모든 unordered pair를 opposite labels로 분리한다.
3. 각 eigenspace orientation은 63개 방향 중 적어도 62개를 덮는다.
4. 그 연산자들은 실제 한 alternating commutator map에서 동시에 나오며, 인덱스 원소들은 maximum \(H\)-clique를 이룬다.
5. 전역적으로 \(\nu(P)=\nu(H)+2\)라는 정확한 upper certificate가 존재한다.

**[CONJECTURE]** 이러한 pair-separating eigenspace system과 maximum-clique 조건의 동시 실현은 불가능할 가능성이 높다. 이를 보이려면 단순한 unlabeled overlap 수가 아니라, direct-sum eigenspace pair가 만드는 partial binary separation code와 maximum-clique 교환자 자료를 결합해야 한다.

**[PROVED]** 이 문서는 full QLD, 보편적 \(q\le C^\delta\), arbitrary-exponent invisible layers, 또는 Erdős Problem 117을 해결했다고 주장하지 않는다.
