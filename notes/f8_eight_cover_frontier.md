# Erdős Problem 117의 cutoff-eight 병목: irredundant eight-subgroup covers

**연구 메모 — 2026-08-14**
**범위:** 유한군의 irredundant subgroup covers, 특히
\[
f(8)=\max [G:D],\qquad D=\bigcap_{i=1}^{8}H_i.
\]
기존 저장소 파일은 사실·계산의 기준선으로만 사용했고, 이 메모에서 새로 쓰는 상계·환원·order-144 witness는 아래에 자립적으로 증명한다. 기존 저장소를 수정하거나 commit/push하지 않았다.

---

## 1. Verdict

### `[PROVED]`
\[
\boxed{144\le f(8)\le 25\,920.}
\]

더 정확히 다음 네 문장이 증명되었다.

1. **전역 상계.** 모든 유한군의 irredundant eight-subgroup cover에 대해
   \[
   [G:D]\le \max\{7^2,6^3\}\,5!=216\cdot120=25\,920.
   \]
   이는 문헌에서 Tomkinson에게 귀속되는 일반식의 \(n=8\) 특수화와 일치하지만, 접근하지 못한 1987년 원문을 black box로 쓰지 않고 여기서 완전히 재증명한다.

2. **general-to-maximal 환원.** core quotient 뒤 임의의 eight-cover는 다음 둘 중 하나다.
   - maximal subgroup으로의 어떤 확대가 redundant가 되어 즉시
     \([G:D]\le2\,880\)을 얻는다.
   - 또는 교집합과 index를 바꾸지 않고 유한 번 확대하여 **모든 여덟 member가 maximal인 core-free eight-cover**에 도달한다.

   따라서 \(B\ge2\,880\)에 대해 maximal/core-free case에서 \([G:D]\le B\)만 증명하면 general case에도 같은 상계가 따른다.

3. **maximal case의 한 주요 branch 완전 해결.** maximal/core-free eight-cover를 가진 \(G\)가 order two인 minimal normal subgroup \(U\cong C_2\)를 가지면
   \[
   [G:D]\le144.
   \]
   이 branch의 상계는 sharp하다.

4. **명시적 maximal/core-free lower witness.** order \(144\)의
   \[
   G=C_2^3\times(C_3^2\rtimes C_2),
   \]
   여기서 \(C_2\)가 \(C_3^2\)에 inversion으로 작용하는 군에, 네 개의 index-two maximal subgroup과 네 개의 index-three maximal subgroup을 좌표식으로 주어 irredundant eight-cover, trivial intersection을 검증했다. 따라서 \(f(8)\ge144\)이다.

**정확한 \(f(8)\)은 이 조사에서 찾거나 증명하지 못했다.** 특히 \(f(5),f(6),f(7)\)의 수열에서 외삽하지 않았다. \(f(8)=144\)는 현재의 증명 결론이 아니다.

---

## 2. Definition and reduction to core-free covers

### 2.1 정의

유한군 \(G\)와 proper subgroups \(H_1,\ldots,H_k\)에 대해
\[
G=H_1\cup\cdots\cup H_k
\]
이고 각 \(i\)마다
\[
H_i\not\subseteq\bigcup_{j\ne i}H_j
\]
이면 이를 irredundant \(k\)-cover라 한다. 각 \(H_i\)에는 다른 member에 속하지 않는 **private element**가 존재한다.

\[
D=\bigcap_{i=1}^{k}H_i,
\qquad
D_G=\bigcap_{g\in G}D^g
\]
라 두고
\[
f(k)=\max [G:D]
\]
를 취한다.

### 2.2 core quotient

#### Lemma 2.1 `[PROVED]`
\(N=D_G\)라 하자. 그러면
\[
\{H_i/N:1\le i\le k\}
\]
은 \(G/N\)의 irredundant \(k\)-cover이고 교집합은 \(D/N\)이며
\[
[G/N:D/N]=[G:D].
\]
또한 \(D/N\)은 \(G/N\)에서 core-free이다.

**증명.** \(N\le H_i\)이므로 quotient cover가 정의된다. 원 cover의 private element \(x_i\in H_i\setminus\bigcup_{j\ne i}H_j\)의 image가 다른 \(H_j/N\)에 들어가면 \(x_i\in H_jN=H_j\)가 되어 모순이다. 교집합과 index의 식은 즉시 따른다. \(D/N\)의 core는 \(D_G/N=1\)이다. \(\square\)

따라서 이하에서 필요하면 처음부터 \(D\)가 core-free라고 가정한다.

---

## 3. Primary-source audit

### 3.1 핵심 source matrix

| 상태 | 저자·제목 | 정확한 위치와 원문의 범위 | proof audit | 계산 공개성 |
|---|---|---|---|---|
| `[CITED-VERIFIED]` | M. J. Tomkinson, **“Groups as the Union of Proper Subgroups,”** *Math. Scand.* 81 (1997), 191–198, DOI `10.7146/math.scand.a-12873` | **Lemma 3.1, printed p. 193.** 유한군 \(G=M\cup H_1\cup\cdots\cup H_k\), \(M<G\), \(\beta_i=[G:H_i]\), \(\beta_1\le\cdots\le\beta_k\)이면 \(\beta_1\le k\). equality이면 모든 \(\beta_i=k\), 또 \(H_i\cap H_j\le M\). | 해당 페이지를 직접 읽음. 다만 논문은 이를 `[3, Lemma 3.3]`의 재진술로 놓고 이 lemma의 proof 자체는 주지 않는다. 본 메모 §4.1에서 독립 증명. | 해당 없음 |
| `[UNVERIFIED]` | M. J. Tomkinson, **“Groups Covered by Finitely Many Cosets or Subgroups,”** *Comm. Algebra* 15 (1987), 845–859, DOI `10.1080/00927878708823445` | 후대 문헌이 \(f(n)\)의 일반 상·하계를 이 논문에 귀속한다. | publisher metadata와 PDF endpoint는 확인했으나 full proof를 안정적으로 읽지 못했다. 따라서 정리 번호·proof를 원문 검증한 것으로 취급하지 않는다. | 알 수 없음 |
| `[CITED-VERIFIED]` | R. A. Bryce, V. Fedri, L. Serena, **“Covering Groups with Subgroups,”** *Bull. Austral. Math. Soc.* 55 (1997), 469–476, DOI `10.1017/S0004972700034109` | **Theorem 1.2, p. 470:** \(f(5)=16\). proof **pp. 475–476**. Proposition 2.3–2.4, p. 470에 three-/four-cover 결과도 정확히 재진술. | full official PDF와 proof를 읽음. | 계산 의존 없음 |
| `[CITED-VERIFIED]` / repository-reproved | A. Abdollahi, M. J. Ataei, S. M. Jafarian Amiri, A. Mohammadi Hassanabadi, **“Groups with a Maximal Irredundant 6-Cover,”** *Comm. Algebra* 33 (2005) | 저자들의 2004 extended abstract **Theorem D, printed p. 72:** \(f(6)=36\). journal abstract도 동일 결론. | journal full proof는 접근 불가. 저장소가 maximal/nonmaximal reduction과 finite leaves를 독립 재구성했다. 기존 분류의 \(S_3\times S_3\) item은 false positive이고, 진짜 order-36 witness는 `SmallGroup(36,13)`이다. | 원 논문 로그 없음; 저장소에는 현대 GAP와 독립 verifier가 있음 |
| `[CITED-VERIFIED]` | A. Abdollahi, S. M. Jafarian Amiri, **“On Groups with an Irredundant 7-Cover,”** *J. Pure Appl. Algebra* 209 (2007), 291–300, DOI `10.1016/j.jpaa.2006.05.021` | **Theorem A, pp. 291–292**, proof pp. 292–299: maximal/core-free seven-cover classification. **Theorem B, p. 292**, proof **pp. 299–300:** \(f(7)=81\). lower witness pp. 292–293. | complete published article를 읽음. | GAP 4.3 사용을 p. 293에 명시하지만 complete code/log/certificate는 없음 |
| `[CITED-VERIFIED]` | A. Abdollahi, M. J. Ataei, A. Mohammadi Hassanabadi, **“Minimal Blocking Sets in \(PG(n,2)\) and Covering Groups by Subgroups,”** *Comm. Algebra* 36 (2008), 365–380, DOI `10.1080/00927870701715639` | **Theorem 1.5, printed p. 366:** maximal irredundant core-free 8-cover를 가진 \(p\)-group은 정확히 \(C_3^4\) 또는 \(C_7^2\). | primary PDF의 theorem과 proof를 읽음. | 일부 finite classification에 GAP가 개입하지만 완전한 code/log/candidate certificate는 공개되지 않음 |
| `[CITED-VERIFIED]` | M. J. Ataei, **“\(C_8\)-Groups and Nilpotency Condition,”** *Int. J. Algebra* 4 (2010), 1057–1062 | **Theorem 2.1, printed p. 1059:** maximal irredundant core-free eight-cover group이 nilpotent iff \(C_3^4\) 또는 \(C_7^2\). | theorem과 이어지는 proof를 읽음. | 별도 certificate 없음 |
| `[CITED-VERIFIED]` | M. J. Ataei, **“Semisimplity Condition and Covering Groups by Subgroups,”** *Int. J. Algebra* 4 (2010), 1063–1068 | Proposition 1.3, Theorem 1.4에서 semisimple \(C_8\)-group의 작은 subgroup-index branch를 제한. | full short paper 읽음. | 일부 후속 분류와 결합되어야 하며 자체로 complete semisimple elimination 아님 |
| `[CITED-VERIFIED]` | M. J. Ataei, **“Covering Semisimple Groups by Subgroups,”** *Int. J. Algebra* 5 (2011), 661–665 | Proposition 1.3, Theorem 1.4, proof printed pp. 663–664: \(\alpha_3=5,6\) 관련 semisimple branches. | full paper 읽음. | 해당 proof는 주로 구조적이나 전체 semisimple \(C_8\) 분류는 아님 |
| `[CITED-VERIFIED]` | M. J. Ataei, **“Minimal Normal Subgroups and Semisimplity Condition,”** *Int. J. Algebra* 6 (2012), 179–183 | **Theorem 1.3–1.4, p. 180**, proof p. 182: semisimple \(C_8\), \(\alpha_2=7\) branch를 배제. | PDF와 critical pages를 읽음. | proof가 “by GAP”으로 subdirect products의 minimal-normal count를 결론내리나 code, candidate list, output/log가 없음. load-bearing universal proof로 사용하지 않음 |
| `[CITED-VERIFIED]` | M. J. Ataei, **“Subdirect Products and Covering Groups by Subgroups,”** *Int. J. Algebra* 7 (2013), 673–677 | **Theorem 2.1, pp. 674–675**: 선택된 subdirect-product families 중 \(C_8\)-groups 목록. order 144 사례도 나타난다. | theorem과 GAP 함수가 실린 proof를 읽음. | 함수는 주어진 group을 검사하지만 후보 생성의 completeness, saved output, logs, independent verifier가 없음. 본 메모의 144 witness는 이 목록에 의존하지 않음 |
| `[CITED-VERIFIED]` | Ataei의 2013–2018 index-pattern/primitive/subdirect-product papers | 특정 index multiset 또는 특정 ambient direct product에서의 \(C_8\)-group/non-\(C_8\)-group 목록. | 해당 theorem/proof pages를 읽음. | 대체로 GAP function과 결론만 있고 complete candidate-generation audit나 certificate가 없음 |
| `[UNVERIFIED]` | S. M. Jafarian Amiri, **“A Survey on Covering of a Group by Its Subgroups,”** *Mathematical Culture and Thought* 43(2) (2024), 121–146, DOI `10.30504/mct.2024.1467.2031` | printed **p. 125**에 \(f(3)=4,f(4)=9,f(5)=16,f(6)=36,f(7)=81\)과 Tomkinson의 일반 상·하계; **p. 126, Proposition 2.3**에 index lemma. | secondary survey를 읽었으나 원증명 대신 사용하지 않음. | 본 메모의 load-bearing edge가 아님 |

### 3.2 문헌에서 확인된 것과 확인되지 않은 것

- 2024 survey는 exact values를 **\(7\)까지만** 나열하고, \(8\)-cover는 “special conditions” 아래의 부분 결과만 언급한다.
- 검색한 accessible primary corpus에서 “\(f(8)=\cdots\)”라는 exact theorem이나 모든 maximal/core-free \(C_8\)-group의 reproducible complete classification은 찾지 못했다.
- “Semisimple Groups with a Maximal Irredundant 8-Cover”라는 conference item은 검색되지만 공개 페이지 자체가 **초록 또는 extended abstract만 제공**한다고 명시한다. proof-bearing full text를 읽지 못했으므로 `[UNVERIFIED]`이다.
- 기존 \(f(6)\) 분류의 실제 false positive가 이미 확인되어 있으므로, GAP code·로그·후보 exhaustiveness가 없는 \(C_8\) 목록을 universal upper bound의 load-bearing edge로 사용하지 않았다.

---

## 4. Best upper bound

### 4.1 complement-index lemma

#### Lemma 4.1 `[PROVED]`
유한군 \(G\), proper subgroup \(M<G\), subgroups \(U_1,\ldots,U_k\)가
\[
G=M\cup U_1\cup\cdots\cup U_k
\]
를 만족한다고 하자. \(\beta_i=[G:U_i]\)라 하면
\[
\sum_{i=1}^{k}\frac1{\beta_i}\ge1.
\]
따라서 \(\min_i\beta_i\le k\). equality \(\min_i\beta_i=k\)이면 모든 \(\beta_i=k\)이고
\[
U_i\cap U_j\le M\qquad(i\ne j).
\]

**증명.** \(m=[G:M]\), \(r_i=[U_i:U_i\cap M]\)라 두면 \(r_i\le m\)이고
\[
|U_i\setminus M|
=\frac{|G|}{\beta_i}\left(1-\frac1{r_i}\right)
\le \frac{|G|}{\beta_i}\left(1-\frac1m\right)
=\frac{|G\setminus M|}{\beta_i}.
\]
\(G\setminus M\subseteq\bigcup_i(U_i\setminus M)\)이므로
\[
|G\setminus M|
\le\sum_i|U_i\setminus M|
\le |G\setminus M|\sum_i\frac1{\beta_i},
\]
첫 결론이 따른다. 모든 \(\beta_i\ge k\)이면 우변의 합은 \(\le1\)이므로 equality가 강제되고 모든 \(\beta_i=k\)이다. union bound에서도 equality이므로 \(U_i\setminus M\)들은 pairwise disjoint하다. 따라서 \(U_i\cap U_j\)의 원소가 \(M\) 밖에 있을 수 없다. \(\square\)

이는 Tomkinson (1997), Lemma 3.1, printed p. 193의 정확한 내용에 대한 독립 증명이다.

### 4.2 factorial intersection lemma

#### Lemma 4.2 `[PROVED]`
\[
G=H_1g_1\cup\cdots\cup H_ng_n
\]
이 irredundant right-coset cover이고 \(D=\bigcap_iH_i\)라 하자. 임의의 permutation \(\rho\)와 \(0\le r\le n-1\)에 대해
\[
\left[\bigcap_{i=1}^{n-r}H_{\rho(i)}:D\right]\le r!.
\]

**증명.** \(r\)에 대한 귀납법이다. \(r=0\)은 자명하다. 선택된 첫 \(n-r\) coset들의 union은 전체가 아니다. 그렇지 않으면 full cover가 irredundant가 아니다. 그 union 밖의 \(x\)를 택하고
\[
K=\bigcap_{i=1}^{n-r}H_{\rho(i)}
\]
라 하자. \(k\in K\)에 대해 \(kx\)는 선택된 coset 중 어느 것에도 들어가지 않으므로 \(Kx\)는 남은 \(r\) coset들로 덮인다. 각 nonempty intersection
\[
Kx\cap H_jg_j
\]
은 \(Kx\) 안에서 \(K\cap H_j\)의 coset이다. 귀납가정에 의해
\[
[K\cap H_j:D]\le(r-1)!.
\]
따라서 \(Kx\), 즉 \(K\)는 최대 \(r(r-1)!=r!\)개의 \(D\)-coset으로 덮인다. \(\square\)

### 4.3 general bound

#### Theorem 4.3 `[PROVED]`
모든 \(n\ge3\)와 모든 irredundant \(n\)-subgroup cover에 대해
\[
[G:D]
\le
\max\{(n-1)^2,(n-2)^3\}(n-3)!.
\tag{4.1}
\]
특히
\[
\boxed{f(8)\le25\,920.}
\]

**증명.** \(\alpha_i=[G:H_i]\)라 하고
\[
\alpha_1\le\alpha_2\le\cdots\le\alpha_n
\]
으로 relabel한다.

먼저 Lemma 4.1을 \(M=H_1\), \(U_i=H_{i+1}\)에 적용하면
\[
\alpha_2\le n-1.
\]

**Case 1: \(\alpha_2=n-1\).** equality case에서
\[
\alpha_2=\cdots=\alpha_n=n-1,
\qquad
H_i\cap H_j\le H_1\quad(2\le i<j\le n).
\]
따라서 \(K=H_2\cap H_3=H_1\cap H_2\cap H_3\)이고
\[
[G:K]\le [G:H_2][G:H_3]=(n-1)^2.
\]
Lemma 4.2에서 세 subgroup의 intersection을 택하면
\[
[K:D]\le(n-3)!.
\]
그러므로
\[
[G:D]\le(n-1)^2(n-3)!.
\]

**Case 2: \(\alpha_2\le n-2\).** \(L=\langle H_1,H_2\rangle\)라 하자.

- \(L<G\)이면
  \[
  G=L\cup H_3\cup\cdots\cup H_n.
  \]
  Lemma 4.1로 \(\alpha_3\le n-2\). \(K=H_1\cap H_2\cap H_3\)에 대해
  \[
  [G:K]\le\alpha_1\alpha_2\alpha_3\le(n-2)^3,
  \]
  Lemma 4.2로 \([K:D]\le(n-3)!\)이다.

- \(L=G\)이면 \(K=H_1\cap H_2\)에 대해
  \[
  [G:K]\le\alpha_1\alpha_2\le(n-2)^2,
  \]
  그리고 Lemma 4.2로
  \[
  [K:D]\le(n-2)!=(n-2)(n-3)!.
  \]
  따라서 역시
  \[
  [G:D]\le(n-2)^3(n-3)!.
  \]

두 case를 합치면 (4.1)이 증명된다. \(n=8\)을 대입하면
\[
\max\{49,216\}\cdot120=25\,920.
\]
\(\square\)

### 4.4 상계의 source status

2024 survey의 printed p. 125는 Tomkinson (1987)에게 정확히 (4.1)을 귀속한다. 그러나 1987 full proof를 읽지 못했으므로 이 메모의 evidence label은 `[CITED-VERIFIED]`가 아니라 **독립 `[PROVED]`**이다. 1997 primary paper p. 193에서 사용되는 index lemma의 정확한 statement는 확인했고, 그 lemma도 위에서 재증명했다.

---

## 5. Best lower bound

### 5.1 explicit group

\[
A=\mathbf F_2^3,
\qquad
V=\mathbf F_3^2,
\qquad
B=V\rtimes\langle t\rangle,
\]
여기서 \(t^2=1\), \(tvt^{-1}=-v\). 두고
\[
G=A\times B.
\]
원소를
\[
g=(a_0,a_1,a_2,x,y,\epsilon),
\]
\(a_i,\epsilon\in\mathbf F_2\), \(x,y\in\mathbf F_3\)로 쓴다. 곱은
\[
(a,v,\epsilon)(a',v',\epsilon')
=(a+a',\;v+(-1)^\epsilon v',\;\epsilon+\epsilon').
\tag{5.1}
\]
따라서 \(|G|=2^3\cdot3^2\cdot2=144\).

### 5.2 eight maximal subgroups

다음 여덟 subgroup을 잡는다.

\[
\begin{array}{ll}
H_1: a_2=0,&H_2:a_1=0,\\
H_3:a_0=0,&H_4:a_0+a_1+a_2+\epsilon=0\pmod2,\\[2mm]
K_1:x=0,&K_2:x+y=0\pmod3,\\
K_3:x+2y=0\pmod3,&K_4:y=\epsilon\quad(\mathbf F_3\text{에서}).
\end{array}
\tag{5.2}
\]

- \(H_1,\ldots,H_4\)는 \(G\to C_2\) homomorphism들의 kernel이므로 index two이고 maximal이다.
- \(K_1,K_2,K_3\)는 nonzero linear form \(\ell:V\to\mathbf F_3\)에 대한 surjection
  \[
  G\twoheadrightarrow \mathbf F_3\rtimes C_2,
  \quad(a,v,\epsilon)\mapsto(\ell(v),\epsilon)
  \]
  에서 reflection subgroup \(\{(0,0),(0,1)\}\)의 preimage이다.
- \(K_4\)는 \(\ell(x,y)=y\)를 쓰고 reflection subgroup \(\{(0,0),(1,1)\}\)의 preimage이다.

따라서 \(K_i\)는 index three이고 maximal이다.

### 5.3 union

한 원소가 \(H_1,H_2,H_3\) 모두 밖에 있으면
\[
(a_0,a_1,a_2)=(1,1,1).
\]
그 원소가 \(H_4\)도 밖에 있으려면 \(\epsilon=0\)이다. 이때 \(K_1,\ldots,K_4\)의 조건은 \(V=\mathbf F_3^2\)의 네 projective lines
\[
x=0,
\quad x+y=0,
\quad x+2y=0,
\quad y=0
\]
이고, 이 네 line은 \(V\) 전체를 덮는다. 따라서 (5.2)의 여덟 subgroup의 union은 \(G\)이다.

### 5.4 intersection

\(H_1\cap H_2\cap H_3\)에서 \(a_0=a_1=a_2=0\), 이어 \(H_4\)에서 \(\epsilon=0\). \(K_1\)에서 \(x=0\), \(K_2\)에서 \(y=0\). 따라서
\[
D=H_1\cap\cdots\cap H_4\cap K_1\cap\cdots\cap K_4=1.
\]

### 5.5 private elements

좌표 순서를 \((a_0,a_1,a_2,x,y,\epsilon)\)로 할 때 다음은 각각의 private element이다.

| member | private element |
|---|---|
| \(H_1\) | \((1,1,0,1,0,1)\) |
| \(H_2\) | \((1,0,1,1,0,1)\) |
| \(H_3\) | \((0,1,1,1,0,1)\) |
| \(H_4\) | \((1,1,1,1,0,1)\) |
| \(K_1\) | \((1,1,1,0,1,0)\) |
| \(K_2\) | \((1,1,1,1,2,0)\) |
| \(K_3\) | \((1,1,1,1,1,0)\) |
| \(K_4\) | \((1,1,1,1,0,0)\) |

직접 대입하면 각 원소는 표시된 subgroup에만 속한다. 따라서 cover는 irredundant이다.

#### Theorem 5.1 `[PROVED]`
(5.2)는 order-144 group \(G\)의 maximal irredundant core-free eight-cover이다. 따라서
\[
\boxed{f(8)\ge144.}
\]

### 5.6 historical consistency, but not dependency

Tomkinson의 product construction은
\[
f(m+n-1)\ge f(m)f(n)
\]
을 준다고 2024 survey p. 125–126이 보고한다. \(m=5,n=4\)와 \(f(5)=16,f(4)=9\)를 대입해도 144가 나온다. 그러나 그 direct-product witness의 한 member는 일반적으로 maximal이 아니다. 위의 (5.2)는 lower bound뿐 아니라 **maximal/core-free branch에서도 144가 실제로 발생**함을 좌표 수준에서 보인다.

---

## 6. Proof or exact structural reduction

### 6.1 complete nonmaximal reduction

#### Theorem 6.1 `[PROVED]`
\(G=H_1\cup\cdots\cup H_8\)이 irredundant이고 \(D=\bigcap_iH_i\)가 core-free라고 하자. 그러면 다음 중 하나가 성립한다.

1. \([G:D]\le2\,880\); 또는
2. 교집합 \(D\)와 index \([G:D]\)를 보존하면서 members를 차례로 확대하여, 모든 여덟 member가 maximal subgroup인 irredundant eight-cover를 얻는다.

**증명.** nonmaximal \(H_1\)을 maximal subgroup \(M\)으로 확대한다.

원 cover의 다른 일곱 subgroup의 intersection은 \(D\)이다. 실제로 Lemma 4.2에서 \(r=1\)이면
\[
\left[\bigcap_{i=2}^{8}H_i:D\right]\le1.
\]
따라서 확대 cover가 irredundant이면 그 intersection은
\[
M\cap\bigcap_{i=2}^{8}H_i=M\cap D=D
\]
이고 maximal member 수가 하나 증가한다.

확대 cover가 redundant이면 minimal subcover를 택한다. 원래 \(H_1\)의 private element는 \(M\)에 속하고 나머지 일곱 subgroup에는 속하지 않으므로 이 subcover는 반드시 \(M\)을 포함한다. 두 proper subgroup의 union은 group이 아니고, 확대된 eight-cover는 redundant이므로 subcover size \(j\)는
\[
3\le j\le7.
\]
relabel하여
\[
G=M\cup H_2\cup\cdots\cup H_j,
\qquad
D_1=M\cap H_2\cap\cdots\cap H_j
\]
라 하자. 그러면
\[
[G:D_1]\le f(j).
\]
또한
\[
D\le D_1\le H_2\cap\cdots\cap H_j.
\]
마지막 intersection은 원 eight-cover의 \(j-1\) members의 intersection이므로 Lemma 4.2에서 \(r=8-(j-1)=9-j\)를 써서
\[
[D_1:D]\le(9-j)!.
\]
따라서
\[
[G:D]\le f(j)(9-j)!.
\]
검증된 \(f(3)=4,f(4)=9,f(5)=16,f(6)=36,f(7)=81\)을 대입하면

| essential subcover size \(j\) | bound |
|---:|---:|
| 7 | \(81\cdot2!=162\) |
| 6 | \(36\cdot3!=216\) |
| 5 | \(16\cdot4!=384\) |
| 4 | \(9\cdot5!=1\,080\) |
| 3 | \(4\cdot6!=2\,880\) |

이다. redundant branch가 한 번이라도 나오면 첫 결론이다. 그렇지 않으면 최대 여덟 번의 enlargement 뒤 모든 member가 maximal이 되고 intersection은 계속 \(D\)이다. \(\square\)

#### Corollary 6.2 `[PROVED]`
\(B\ge2\,880\)이고 모든 maximal/core-free irredundant eight-cover에 대해 \([G:D]\le B\)라면, 모든 irredundant eight-cover에 대해 같은 상계가 성립한다.

이 환원은 단순히 \(f(j)(8-j)!\)를 곱한 것이 아니다. enlargement 뒤 intersection 보존, minimal subcover에 \(M\)이 반드시 포함됨, 그리고 원 eight-cover에서 선택된 \(j-1\) subgroup intersection에 factorial lemma를 적용하는 점이 핵심이다.

### 6.2 abelian minimal normal subgroup: finite parameter reduction

#### Proposition 6.3 `[PROVED]`
모든 \(H_i\)가 maximal이고 \(D\)가 core-free인 irredundant eight-cover를 생각하자. \(U\)가 abelian minimal normal subgroup이면, \(U\)를 포함하지 않는 cover members의 수를 \(r\), 포함하는 수를 \(t=8-r\)라 할 때
\[
|U|\le r\le7,
\qquad
1\le t\le 8-|U|.
\]
특히
\[
|U|\in\{2,3,4,5,7\}.
\]

**증명.** core-free이므로 모든 \(H_i\)가 \(U\)를 포함할 수 없다. \(M\)이 \(U\not\le M\)인 maximal member이면 \(G=UM\). \(U\cap M\)은 \(U\)와 \(M\) 양쪽에 의해 normalized되므로 \(G\)-normal이고, \(U\)의 minimality로 \(U\cap M=1\). 따라서 \(M\)은 \(U\)의 complement이다.

모든 member가 complement이면 \(1\ne u\in U\)가 아무 member에도 속하지 않으므로 \(t\ge1\), 따라서 \(r\le7\).

한 complement \(M\)의 private element \(x\in M\)을 택한다. \(G=U\rtimes M\)로 보고 \(x\)의 projection을 \(m\in M\)이라 하자. \(x\)가 \(U\)를 포함하는 모든 member를 피하므로 entire fiber \(Um\)도 그 members를 피한다. 각 complement는 projection \(G\to G/U\)의 각 fiber와 정확히 한 점에서 만난다. \(|U|\)개의 fiber points를 \(r\)개의 complement가 덮어야 하므로 \(r\ge|U|\). \(|U|\)는 prime power이고 \(2\le|U|\le7\)이므로 결론이 따른다. \(\square\)

따라서 affine branch는 적어도 \(|U|=2,3,4,5,7\)의 유한한 socle-size 목록으로 줄어든다. 다만 complements는 \(1\)-cocycles이고 action/cocycle orbits가 남으므로 이것만으로 finite group list가 완성되는 것은 아니다.

### 6.3 the \(U\cong C_2\) branch

#### Theorem 6.4 `[PROVED]`
maximal/core-free irredundant eight-cover를 가진 \(G\)가 minimal normal subgroup \(U\cong C_2\)를 가지면
\[
[G:D]\le144.
\]

**증명.** \(\operatorname{Aut}(C_2)=1\)이므로 \(U\le Z(G)\). \(U\)를 포함하지 않는 한 complement를 \(H\)라 택하면
\[
G=U\times H.
\]
\(U\)를 포함하지 않는 \(r\)개 members는 \(H\to U\) homomorphism들의 graphs이다. 하나를 zero map의 graph \(H\)로 놓고 나머지를 \(\lambda_2,\ldots,\lambda_r\)라 쓰자. 두고
\[
K=\bigcap_{j=2}^{r}\ker\lambda_j.
\]
그러면
\[
[H:K]\le2^{r-1}.
\tag{6.1}
\]
\(U\)를 포함하는 \(t=8-r\)개 members는
\[
U\times L_1,\ldots,U\times L_t
\]
형태다.

\(h\in K\)이면 \((1,h)\), 여기서 \(1\)은 \(U\)의 nonidentity element, 는 어느 complement에도 속하지 않는다. 따라서
\[
K=\bigcup_{i=1}^{t}(K\cap L_i).
\tag{6.2}
\]
각 \(U\times L_i\)의 private point는 zero-graph complement \(H\)를 피하므로 nontrivial \(U\)-coordinate를 가진다. 다른 graph complements를 피하려면 그 \(H\)-coordinate가 \(K\)에 속해야 한다. 다른 \(U\times L_j\)들을 피하는 조건까지 합치면, 각 \(K\cap L_i\)에는 induced cover에서의 private point가 있다. 따라서 \(t\ge2\)일 때 (6.2)는 irredundant이다. \(t=2\)는 group을 두 proper subgroups로 덮는 모순이므로 불가능하다.

- \(t=1\), 즉 \(r=7\)이면 (6.2)에서 \(K\le L_1\). 따라서 \(D\cong K\)이고
  \[
  [G:D]=2[H:K]\le2^7=128.
  \]
- \(t\ge3\)이면 induced \(t\)-cover의 intersection을
  \[
  D_H=K\cap L_1\cap\cdots\cap L_t
  \]
  라 할 때 \([K:D_H]\le f(t)\), 그리고 \(D=\{0\}\times D_H\). 따라서
  \[
  [G:D]
  =2[H:K][K:D_H]
  \le2^r f(8-r).
  \]
  가능한 값은

  | \(r\) | \(t\) | bound |
  |---:|---:|---:|
  | 2 | 6 | \(2^2\cdot36=144\) |
  | 3 | 5 | \(2^3\cdot16=128\) |
  | 4 | 4 | \(2^4\cdot9=144\) |
  | 5 | 3 | \(2^5\cdot4=128\) |

따라서 항상 \([G:D]\le144\). \(\square\)

(5.2)의 witness에서 \(U=\langle(1,0,0,0,0,0)\rangle\cong C_2\)를 택하면 central minimal normal이고, 정확히 두 cover member가 \(U\)를 포함하지 않는다. 그 witness가 index 144를 가지므로 이 branch의 bound는 sharp하다.

---

## 7. Computational evidence

### 7.1 status and scope

#### `[COMPUTED]` explicit witness verification

- **언어/버전:** Python 3.9.6, standard library only.
- **GAP/SmallGrp:** 사용하지 않음.
- **검사 범위:** order-144 group (5.1)의 모든 144 elements와 (5.2)의 정확히 여덟 explicit subsets. 후보 탐색이나 bounded-order classification이 아니다.
- **group 검증:** identity와 inverse 전수검사, \(144^3=2\,985\,984\) triples에 대한 full associativity 검사.
- **subgroup 검증:** 각 subset에 대해 identity, inverse closure, multiplication closure 전수검사.
- **cover 검증:** union cardinality 144.
- **intersection 검증:** identity singleton.
- **irredundancy 검증:** 각 member의 private set을 정확히 계산; 각 private set의 크기는 2.
- **maximality:** subgroup sizes \(72,72,72,72,48,48,48,48\), indices \(2,2,2,2,3,3,3,3\); prime index.
- **실행시간:** 약 3.2초.

Artifacts:

- `src/verification/verify_f8_order144_witness.py`
- `src/verification/test_f8_eight_cover_frontier.py`
- `experiments/logs/f8_order144_witness_verification.txt`

SHA-256:

```text
0c0f9fd78f2f3cb6adf00c5d2314432ff48a63a712320cc123c5cd2e5e2d8b9c  src/verification/verify_f8_order144_witness.py
8e0644b1921843ca6ae8975bc32c7497e3f12fee14112e43f22669048785f53e  src/verification/test_f8_eight_cover_frontier.py
add904ddf9257571151f33e371f73c3806a2e005db685f97441be677a4db854d  experiments/logs/f8_order144_witness_verification.txt
```

### 7.2 기존 저장소의 bounded computation

기존 certificate는 \(|Q|=|G/Z(G)|\le81\)인 738 quotient types의 cutoff-eight extension graphs를 모두 처리하며, 그 범위 안에서는 최대 abelian-cover number가 10이고 \(a>10\) 사례가 없다. 그러나 그 계산은 명시적으로 **order-at-most-81 slice**일 뿐, global \(h(8)\) upper bound가 아니다.

본 메모는 이 계산을 universal \(f(8)\) 주장에 사용하지 않는다. 새 전역 index bound는 순수한 cover argument인 Theorem 4.3에서 나온다.

---

## 8. Exact consequence for \(h(8)\)

\(\nu(G)=8\)이고 \(X=\{x_1,\ldots,x_8\}\)가 maximum pairwise-noncommuting set이면
\[
G=\bigcup_{i=1}^{8}C_G(x_i)
\]
이고 cover는 irredundant이다. 저장소의 two-step centralizer-drop lemma
\[
\nu(C_G(y))\le\nu(G)-2
\qquad(y\notin Z(G))
\]
에 의해
\[
\bigcap_{i=1}^{8}C_G(x_i)=Z(G).
\]
따라서 Theorem 4.3을 이 centralizer cover에 적용하면 다음을 얻는다.

#### Corollary 8.1 `[PROVED]`
모든 group \(G\)에 대해
\[
\nu(G)=8
\quad\Longrightarrow\quad
\boxed{[G:Z(G)]\le25\,920.}
\]

원래 group이 infinite일 수 있어도 저장소의 finite-center-quotient reduction 뒤 finite quotient의 eight-cover에 적용하면 된다.

기존 저장소는 \(h(7)=10\)을 증명했으므로 monotonicity로
\[
h(8)\ge10.
\]
또 order-at-most-81 slice에서 \(a>10\)이 없으므로, \(h(8)\le10\)에 대한 counterexample가 존재한다면 반드시
\[
\nu(G)=8,
\qquad
82\le |G/Z(G)|\le25\,920
\]
를 만족한다.

따라서 cutoff-eight computation은 이제 무한한 quotient-order 문제는 아니다. 다만 \(25\,920\) 이하의 모든 가능한 center quotient와 모든 exact central-extension commutation graphs를 처리하는 것은 현재 certificate보다 훨씬 큰 별도 분류 문제다. 이 메모는 \(h(8)=10\)을 증명하지 않는다.

---

## 9. Adversarial audit

1. **1987 Tomkinson 원문을 읽은 것처럼 쓰지 않았다.** 일반 bound의 역사적 귀속은 secondary source에서 확인했지만, load-bearing proof는 §4에 전부 적었다.
2. **\(f(5),f(6),f(7)\)에서 수열 외삽을 하지 않았다.** 144는 explicit witness와 independent verifier에서, 25,920은 theorem proof에서 나온다.
3. **“nonmaximal case \(\le2\,880\)”이라고 무조건 말하지 않는다.** 정확한 결론은: nonmaximal member를 확대했을 때 redundant branch가 나오면 \(\le2\,880\); 그렇지 않으면 같은 \(D\)를 유지한 maximal cover로 이동한다.
4. **core-free와 trivial intersection을 구분했다.** quotient reduction에서는 intersection이 core-free일 뿐 반드시 trivial은 아니다. order-144 witness에서는 실제로 trivial이다.
5. **maximal cover와 irredundant cover를 구분했다.** 여기서 “maximal”은 각 cover member가 maximal subgroup이라는 뜻이다.
6. **minimal-number cover와 irredundant cover를 섞지 않았다.** \(\sigma(G)\)에 관한 결과는 \(f(8)\)의 직접 근거가 아니다.
7. **coset-cover와 subgroup-cover를 구분했다.** factorial lemma는 더 일반적인 coset-cover form으로 증명했지만 적용은 subgroup cover에 한다.
8. **partial \(C_8\) lists를 complete classification으로 승격하지 않았다.** 여러 papers는 특정 primitive/subdirect/index branch만 다루고, GAP 함수는 주어진 후보를 검사할 뿐 전체 후보 생성의 completeness를 인증하지 않는다.
9. **2012 semisimple proof의 GAP gap을 숨기지 않았다.** code/log/candidate list가 없으므로 그 branch를 universal theorem의 load-bearing edge로 쓰지 않았다.
10. **bounded computation을 global theorem으로 승격하지 않았다.** \(|Q|\le81\) certificate는 그대로 bounded result다.
11. **철회된 Nagy–Pach–Tomon arXiv:2205.03389의 \(2^{O(k)}\), \(20^k\) 주장을 사용하지 않았다.** 2026 출판 논문의 abelian coset-cover 결과도 exact \(f(8)\)에는 사용하지 않았다.
12. **order-144 lower witness는 문헌의 GAP output에 의존하지 않는다.** group law, subgroups, union, intersection, private points가 모두 이 메모에 명시되어 있고 standard-library verifier가 전수검사한다.

---

## 10. Remaining minimum obstruction

현재 남은 최소 load-bearing obstruction은 다음과 같이 정확히 표현할 수 있다.

> **Maximal/core-free eight-cover problem, excluding the solved central \(C_2\)-socle branch.**
> 모든 cover member가 maximal이고 \(D\)가 core-free인 irredundant eight-cover에서, minimal normal subgroup이 order two가 아닌 경우 \([G:D]\le B\)를 sharp하게 제한하라.

Proposition 6.3에 의해 abelian minimal-normal branch의 socle size는
\[
|U|\in\{3,4,5,7\}
\]
만 남는다. 각 경우에는 다음이 필요하다.

- \(G=U\rtimes H\)의 faithful irreducible action 후보;
- complements를 나타내는 \(1\)-cocycle orbits;
- \(U\)-containing maximal subgroups가 quotient \(H\)에서 만드는 induced cover;
- private-fiber constraint와 core-free intersection의 결합;
- diagonal/subdirect realizations의 완전하고 재현 가능한 enumeration.

nonabelian minimal-normal branch에는 semisimple 또는 여러 simple factors의 subdirect/diagonal action이 남는다. 기존 short papers가 index-specific pruning을 주지만, 다음 둘 중 하나가 필요하다.

1. proof-bearing semisimple elimination을 처음부터 재구성; 또는
2. primitive representations와 subdirect products를 유한 후보군으로 축약한 뒤, 후보 생성부터 cover/intersection 검사까지 공개된 code·logs·independent certificates로 닫기.

정확값 \(144\)를 증명하려면 결국 위 모든 remaining maximal branches에서
\[
[G:D]\le144
\]
를 보여야 한다. 현재 메모는 central \(C_2\)-minimal-normal branch에서만 이를 sharp하게 증명한다.

---

## 11. Negative search log

### 11.1 검색어

다음 exact/variant queries를 영어로 반복했다.

- `"irredundant 8-cover" group`
- `"irredundant eight cover" finite groups`
- `"groups covered by eight subgroups"`
- `"maximal irredundant core-free 8-cover"`
- `"f(8)" subgroup covers`
- `"C_8-cover" group theory`
- `"union of eight proper subgroups"`
- `"intersection index irredundant cover"`
- `"Semisimple Groups with a Maximal Irredundant 8-Cover"`
- Tomkinson 1987/1997, Bryce–Fedri–Serena, Abdollahi–Jafarian Amiri, Abdollahi–Ataei–Jafarian Amiri–Mohammadi Hassanabadi의 forward citations
- Ataei, Alencar, Berkovich, Persian/Portuguese thesis와 university repository 조합

또한 \(C_8\)이 cyclic group \(C_8\)을 뜻하는 결과, coset covers, minimal covering number \(\sigma(G)\), prescribed centralizer-count papers를 제외하며 검색했다.

### 11.2 확인했으나 exact \(f(8)\)을 주지 않은 자료

1. **Tomkinson (1987).** general upper/lower bound의 원출처로 지목되지만 exact \(f(8)\) theorem은 검색 metadata/후대 인용에서 확인되지 않았고 full proof도 접근하지 못했다.
2. **Tomkinson (1997).** index lemma와 seven-proper-subgroup union 문제를 다룬다. exact \(f(8)\) 없음.
3. **2008 p-group paper.** maximal/core-free \(C_8\)-groups 중 \(p\)-groups를 \(C_3^4,C_7^2\)로 분류한다. general solvable/semisimple cases를 닫지 않는다.
4. **Ataei (2010), nilpotency.** nilpotent iff 위 두 groups. nonnilpotent maximal cases가 남는다.
5. **Ataei (2010, 2011, 2012), semisimple papers.** 특정 index branches를 제한/배제하지만 complete reproducible semisimple classification을 제공하지 않는다. 2012의 한 핵심 step은 unarchived GAP assertion이다.
6. **Ataei (2013–2018), subdirect/primitive/index-condition papers.** 특정 ambient products 또는 index multisets의 positive/negative lists. general \(f(8)\) 상계나 exact value가 아니다.
7. **38th Iranian Mathematics Conference item.** 제목은 complete semisimple result를 시사하지만 공개 source는 abstract/extended abstract뿐이라고 명시한다. proof를 읽지 못했으므로 `[UNVERIFIED]`.
8. **2024 Persian survey.** exact values는 \(f(3)\)부터 \(f(7)\)까지만 기록하고, \(8\)-cover는 special-condition literature만 언급한다. general Tomkinson bounds는 기록한다.
9. **Alencar의 2011 Portuguese dissertation.** six-cover proof reconstruction에는 유용하지만 \(f(8)\) exact theorem 없음.
10. **Saccochi의 2015 Portuguese dissertation.** Erdős/Pyber/Isaacs chain에는 유용하지만 exact subgroup-cover \(f(8)\)을 주지 않는다.

### 11.3 negative conclusion의 강도

`[UNVERIFIED]` **2026-08-14까지 이 감사에서 검색·열람한 범위에서는 exact \(f(8)\) primary theorem을 찾지 못했다.** 이는 문헌에 그러한 결과가 절대로 없다는 증명이 아니며 novelty claim도 아니다.

---

## References and stable access points

1. M. J. Tomkinson, “Groups Covered by Finitely Many Cosets or Subgroups,” *Communications in Algebra* 15 (1987), 845–859. DOI: `10.1080/00927878708823445`.
2. M. J. Tomkinson, “Groups as the Union of Proper Subgroups,” *Mathematica Scandinavica* 81 (1997), 191–198. DOI: `10.7146/math.scand.a-12873`.
3. R. A. Bryce, V. Fedri, L. Serena, “Covering Groups with Subgroups,” *Bulletin of the Australian Mathematical Society* 55 (1997), 469–476. DOI: `10.1017/S0004972700034109`.
4. A. Abdollahi, M. J. Ataei, S. M. Jafarian Amiri, A. Mohammadi Hassanabadi, “Groups with a Maximal Irredundant 6-Cover,” *Communications in Algebra* 33 (2005). DOI: `10.1081/AGB-200066157`.
5. A. Abdollahi, S. M. Jafarian Amiri, “On Groups with an Irredundant 7-Cover,” *Journal of Pure and Applied Algebra* 209 (2007), 291–300. DOI: `10.1016/j.jpaa.2006.05.021`.
6. A. Abdollahi, M. J. Ataei, A. Mohammadi Hassanabadi, “Minimal Blocking Sets in \(PG(n,2)\) and Covering Groups by Subgroups,” *Communications in Algebra* 36 (2008), 365–380. DOI: `10.1080/00927870701715639`.
7. M. J. Ataei, “\(C_8\)-Groups and Nilpotency Condition,” *International Journal of Algebra* 4 (2010), 1057–1062. Public PDF: `https://m-hikari.com/ija/ija-2010/ija-21-24-2010/ataeiIJA21-24-2010-1.pdf`.
8. M. J. Ataei, “Covering Semisimple Groups by Subgroups,” *International Journal of Algebra* 5 (2011), 661–665. Public PDF: `https://www.m-hikari.com/ija/ija-2011/ija-13-16-2011/ataeyIJA13-16-2011.pdf`.
9. M. J. Ataei, “Minimal Normal Subgroups and Semisimplity Condition,” *International Journal of Algebra* 6 (2012), 179–183.
10. M. J. Ataei, “Subdirect Products and Covering Groups by Subgroups,” *International Journal of Algebra* 7 (2013), 673–677. Public PDF: `https://www.m-hikari.com/ija/ija-2013/ija-13-16-2013/ataeiIJA13-16-2013-1.pdf`.
11. S. M. Jafarian Amiri, “A Survey on Covering of a Group by Its Subgroups,” *Mathematical Culture and Thought* 43(2) (2024), 121–146. DOI: `10.30504/mct.2024.1467.2031`.
