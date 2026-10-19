# Online Softmax & FlashAttention

> **Loop fusion for attention** — learn how “online” (single-pass) algorithms turn multi-scan math into one streaming update, then apply that idea to **safe softmax** and **FlashAttention**.

All diagrams: [`assert/`](https://github.com/Gaurav14cs17/DSA/tree/main/41_loop_fusion_online/00_online_softmax_flashAtten/assert)

---

## Why this matters

Standard softmax / attention needs **several full passes** over the sequence (find max → sum exps → normalize → multiply by $V$). Each pass burns memory bandwidth.

An **online algorithm** keeps only a tiny **running state**. When a new value $x_i$ arrives, it applies a **correction factor** and updates that state — no re-read of past data.

```text
  state(i-1)  +  x_i  +  correction  →  state(i)
```

We build that pattern on four warm-ups, then use it for Online Softmax and FlashAttention.

---

## Roadmap

```text
  Warm-ups (intuition)              Softmax                    Attention
 ─────────────────────            ──────────                 ──────────
  ① Running average      ──┐
  ② Welford variance     ──┼──►  ⑤ Online safe softmax  ──►  ⑥ FlashAttention
  ③ Kadane max-subarray  ──┤         (fuse max + d)              (fuse m, d', o')
  ④ Top-2 maximum        ──┘
```

| Stage | Topic | Goal |
|-------|--------|------|
| **Warm-up** | [① Running average](#1-running-average-cumulative-mean) | Learn the basic online update: old state + correction |
| **Warm-up** | [② Welford variance](#2-welfords-online-variance) | Correct a dependent state when another statistic moves |
| **Warm-up** | [③ Kadane](#3-maximum-subarray-sum--kadanes-algorithm) | Keep two coupled running values (local + global) |
| **Warm-up** | [④ Top-2 max](#4-first--second-maximum-in-one-pass) | Maintain a running max and react when it changes |
| **Core** | [⑤ Online safe softmax](#5-online-safe-softmax) | Fuse find-max + denominator into one pass |
| **Goal** | [⑥ FlashAttention](#6-flashattention--fusing-softmax-and-av) | Fuse softmax and $AV$ into one streaming update |

---

## The online pattern (read once)

Every section below follows the same four boxes:

1. **Multi-pass problem** — what a naive algorithm does (and why it hurts)
2. **Running state** — what we store after seeing $i-1$ elements
3. **Correction / update** — how $x_i$ changes that state
4. **Single-pass result** — the final recurrence (time $O(N)$, usually space $O(1)$)

---

## 1. Running Average (Cumulative Mean)

<p align="center">
  <img src="assert/02.jpeg" alt="Calculating a Running Average (Cumulative Mean)" width="920"/>
</p>

<p align="center"><em>Figure 1 — From a full-sum average to a one-line online update.</em></p>

### Multi-pass problem

To get the average you normally need the whole sum first:

$$
A_N = \frac{1}{N}\sum_{i=1}^{N} x_i
$$

That means either buffer all $x_i$, or make a dedicated sum pass before you can report $A_N$.

### Running state

After $i-1$ values we only keep the current average:

$$
A_{i-1} = \frac{1}{i-1}\sum_{j=1}^{i-1} x_j
\quad\Longleftrightarrow\quad
\sum_{j=1}^{i-1} x_j = (i-1)\,A_{i-1}
$$

### Correction (derivation sketch)

$$
A_i
= \frac{1}{i}\Big[(i-1)A_{i-1} + x_i\Big]
= A_{i-1} + \frac{x_i - A_{i-1}}{i}
$$

Intuition: take the old average and add the new point’s **deviation**, spread over $i$ samples.

### Single-pass result

$$
\boxed{A_i = A_{i-1} + \dfrac{x_i - A_{i-1}}{i}}
$$

**Takeaway:** this is the template for every later algorithm — *old state + scaled correction*.

---

## 2. Welford’s Online Variance

<p align="center">
  <img src="assert/01.jpeg" alt="Calculating Variance with Welford's Algorithm" width="920"/>
</p>

<p align="center"><em>Figure 2 — Two-pass variance → Welford single-pass updates for $\mu$ and $M$.</em></p>

### Multi-pass problem

Classic variance needs two scans:

| Pass | Formula |
|------|---------|
| 1 — mean | $\displaystyle \mu = \frac{1}{n}\sum_{k=1}^{n} x_k$ |
| 2 — sum of squares | $\displaystyle M_n = \sum_{k=1}^{n}(x_k - \mu)^2$ |

You must store or re-stream every $x_k$.

### Running state (after $n-1$ points)

- count: $n-1$
- mean: $\mu_{n-1}$
- sum of squared deviations: $M_{n-1} = \sum_{k=1}^{n-1}(x_k - \mu_{n-1})^2$

### Correction

When $x_n$ arrives, the mean moves, so every old $(x_k - \mu)$ is wrong. After expanding and simplifying, the net change collapses to a product of two deviations (old mean vs new mean):

$$
\mu_n = \mu_{n-1} + \frac{x_n - \mu_{n-1}}{n}
$$

$$
M_n = M_{n-1} + (x_n - \mu_{n-1})(x_n - \mu_n)
$$

### Single-pass result

$$
\boxed{
\begin{aligned}
\mu_n &= \mu_{n-1} + \frac{x_n - \mu_{n-1}}{n} \\[4pt]
M_n &= M_{n-1} + (x_n - \mu_{n-1})(x_n - \mu_n)
\end{aligned}
}
$$

**Takeaway:** when a summary statistic depends on another running quantity (here $\mu$), the update must **correct** the dependent state — same idea as rescaling the softmax denominator when the max changes.

---

## 3. Maximum Subarray Sum — Kadane’s Algorithm

<p align="center">
  <img src="assert/03.jpeg" alt="Maximum Subarray Sum (Kadane's Algorithm)" width="920"/>
</p>

<p align="center"><em>Figure 3 — Brute-force all subarrays → $O(N)$ local/global running max.</em></p>

### Multi-pass problem

Find the contiguous subarray with largest sum:

$$
G_N = \max_{1\le j\le k\le N}\sum_{m=j}^{k} x_m
$$

- Naive: $O(N^3)$
- Better prefix tricks: still $O(N^2)$

### Running state

| Symbol | Meaning |
|--------|---------|
| $S_{i-1}$ | best sum among subarrays **ending at** $i-1$ |
| $G_{i-1}$ | best sum among **all** subarrays in the prefix |

### Correction

A subarray ending at $i$ either starts fresh at $i$, or extends the best ending at $i-1$:

$$
S_i = \max(x_i,\ S_{i-1} + x_i),\qquad
G_i = \max(G_{i-1},\ S_i)
$$

### Single-pass result

$$
\boxed{
\begin{aligned}
S_i &= \max(x_i,\ S_{i-1}+x_i) \\
G_i &= \max(G_{i-1},\ S_i)
\end{aligned}
}
\qquad
\text{Time }O(N),\ \text{Space }O(1)
$$

**Takeaway:** two coupled running values (local + global) already feel like Softmax’s $(m, d)$ pair.

---

## 4. First & Second Maximum in One Pass

<p align="center">
  <img src="assert/04.jpeg" alt="Finding the First and Second Maximum Elements" width="920"/>
</p>

<p align="center"><em>Figure 4 — Two-pass top-2 → one-pass piecewise update of $(m_1, m_2)$.</em></p>

### Multi-pass problem

1. Pass 1: $M_1 = \max(X)$
2. Pass 2: $M_2 = \max(X\setminus\{M_1\})$

Still $O(N)$, but **two full scans** and about $2N$ comparisons.

### Running state

For the prefix $X_{(i-1)} = \{x_1,\ldots,x_{i-1}\}$ keep:

- $m_{(1,i-1)}$ — current first max  
- $m_{(2,i-1)}$ — current second max  

### Correction (three cases for $x_i$)

| Case | Condition | New $(m_1,\ m_2)$ |
|------|-----------|-------------------|
| 1 | $x_i > m_{(1,i-1)}$ | $(x_i,\ m_{(1,i-1)})$ — old max demoted |
| 2 | $m_{(2,i-1)} < x_i \le m_{(1,i-1)}$ | $(m_{(1,i-1)},\ x_i)$ |
| 3 | $x_i \le m_{(2,i-1)}$ | unchanged |

### Single-pass result

$$
\boxed{
(m_{(1,i)}, m_{(2,i)}) =
\begin{cases}
(x_i,\ m_{(1,i-1)}) & x_i > m_{(1,i-1)} \\
(m_{(1,i-1)},\ x_i) & m_{(2,i-1)} < x_i \le m_{(1,i-1)} \\
(m_{(1,i-1)},\ m_{(2,i-1)}) & x_i \le m_{(2,i-1)}
\end{cases}
}
$$

**Takeaway:** maintaining a **running maximum** (and reacting when it changes) is exactly the skill Online Softmax needs.

---

## 5. Online Safe Softmax

Safe softmax subtracts the global max before `exp` so large logits do not overflow:

$$
a_i = \frac{e^{x_i - m_N}}{\sum_{k=1}^{N} e^{x_k - m_N}},\qquad m_N = \max_k x_k
$$

Naive code → **3 passes**. Online code fuses the first two.

### 5.1 Whiteboard derivation (step $i-1$ → $i$)

<p align="center">
  <img src="assert/05.jpeg" alt="Online Safe Softmax Denominator — time step by step" width="920"/>
</p>

<p align="center"><em>Figure 5a — Hand derivation of the denominator correction.</em></p>

**State at $i-1$:**

$$
m_{i-1} = \max_{j\le i-1} x_j,\qquad
d_{i-1} = \sum_{k=1}^{i-1} e^{x_k - m_{i-1}}
$$

**Goal at $i$:** $m_i = \max(m_{i-1}, x_i)$ and $d_i = \sum_{k=1}^{i} e^{x_k - m_i}$.

Rewrite old terms with the identity $x_k - m_i = (x_k - m_{i-1}) + (m_{i-1} - m_i)$:

$$
d_i
= e^{m_{i-1}-m_i}\,d_{i-1} + e^{x_i - m_i}
$$

If $m_i = m_{i-1}$, the factor is $1$ (no rescale). If $m_i = x_i > m_{i-1}$, every old contribution is multiplied by $e^{m_{i-1}-m_i} < 1$.

---

### 5.2 Infographic: full online safe softmax

<p align="center">
  <img src="assert/05_a.jpeg" alt="Online Safe Softmax Denominator Calculation" width="920"/>
</p>

<p align="center"><em>Figure 5b — Multi-pass vs single-pass safe softmax denominator.</em></p>

| | Multi-pass | Online |
|--|------------|--------|
| Pass 1 | find $m_N$ | — |
| Pass 2 | sum $e^{x_k-m_N}$ | fused with max |
| Init | — | $m_0=-\infty$, $d_0=0$ |
| Update | — | $m_i=\max(m_{i-1},x_i)$<br>$d_i=d_{i-1}e^{m_{i-1}-m_i}+e^{x_i-m_i}$ |
| Complexity | $O(N)$ time, **2+ scans** | $O(N)$ time, **1 scan**, $O(1)$ space |

---

### 5.3 Offline 3-pass Softmax (baseline)

<p align="center">
  <img src="assert/05_b.png" alt="Softmax offline three-pass algorithm and online derivation" width="920"/>
</p>

<p align="center"><em>Figure 5c — Left: classic 3-pass Softmax. Right: why $d'_i$ can track the true denominator online.</em></p>

```text
# Pass 1 — global max
m_0 = -∞
for i = 1 .. N:
    m_i = max(m_{i-1}, x_i)          # result: m_N

# Pass 2 — denominator with fixed m_N
d_0 = 0
for i = 1 .. N:
    d_i = d_{i-1} + exp(x_i - m_N)   # result: d_N

# Pass 3 — normalize
for i = 1 .. N:
    a_i = exp(x_i - m_N) / d_N
```

Online view uses a **local** sum $d'_i = \sum_{j=1}^{i} e^{x_j - m_i}$. At the end $d'_N = d_N$, and:

$$
d'_i = d'_{i-1}\,e^{m_{i-1}-m_i} + e^{x_i-m_i}
$$

---

### 5.4 Same story, another angle

<p align="center">
  <img src="assert/05_c.png" alt="Safe Softmax vs Online Softmax recurrence" width="920"/>
</p>

<p align="center"><em>Figure 5d — Safe Softmax passes (left) and the online recurrence for $d'_i$ (right).</em></p>

Key definitions:

- $d_i$ — partial sum using the **final** global max $m_N$ (needs a future value)
- $d'_i$ — partial sum using the **current** max $m_i$ (computeable online)
- At $i = N$: $d'_N = d_N$ ✓

---

### 5.5 Result: 3-pass → 2-pass Softmax

<p align="center">
  <img src="assert/05_d.png" alt="Three-pass Softmax vs Online two-pass Softmax" width="920"/>
</p>

<p align="center"><em>Figure 5e — Fusing find-max and sum-exp into one loop; only normalize remains as a second pass.</em></p>

**Online Softmax (2 passes):**

```text
# Fused pass — max + running denominator
m_0 = -∞;  d'_0 = 0
for i = 1 .. N:
    m_i  = max(m_{i-1}, x_i)
    d'_i = d'_{i-1} * exp(m_{i-1} - m_i) + exp(x_i - m_i)

# Normalize pass
for i = 1 .. N:
    a_i = exp(x_i - m_N) / d'_N
```

**Takeaway:** loop fusion already cut one full memory scan. FlashAttention goes further and folds $AV$ into the same stream.

---

## 6. FlashAttention — Fusing Softmax and $AV$

For one query row:

$$
S = QK^\top,\quad
A = \mathrm{Softmax}(S),\quad
O = AV
$$

with scores $x_i = q\,k_i^\top$. We never want to materialize the full $N\times N$ matrix $A$.

### 6.1 Attention + online softmax (setup)

<p align="center">
  <img src="assert/05_e.png" alt="Attention definitions with online softmax updates" width="920"/>
</p>

<p align="center"><em>Figure 6a — $S=QK^\top$, $A=\mathrm{Softmax}(S)$, $O=AV$, plus online $(m,d')$ updates.</em></p>

Initializations: $m_0 = -\infty$, $d'_0 = 0$, and later $o'_0 = 0$.

---

### 6.2 Two-pass attention with online stats

<p align="center">
  <img src="assert/05_f.png" alt="Two-pass online softmax attention algorithm" width="920"/>
</p>

<p align="center"><em>Figure 6b — Pass 1 collects $(m_N, d'_N)$; Pass 2 builds $o_N = \sum a_i v_i$.</em></p>

```text
# Pass 1 — scores + running max/denominator
m_0 = -∞;  d'_0 = 0
for i = 1 .. N:
    x_i  = q · k_iᵀ
    m_i  = max(m_{i-1}, x_i)
    d'_i = d'_{i-1} * exp(m_{i-1} - m_i) + exp(x_i - m_i)

# Pass 2 — weighted sum of values
o_0 = 0
for i = 1 .. N:
    a_i = exp(x_i - m_N) / d'_N
    o_i = o_{i-1} + a_i * v_i
return o_N
```

Still two passes over $V$ (or you must buffer scores). FlashAttention’s insight: also keep a **running output** and rescale it.

---

### 6.3 Why the output needs a correction factor

<p align="center">
  <img src="assert/05_g.png" alt="Deriving the partial output rescaling for online attention" width="920"/>
</p>

<p align="center"><em>Figure 6c — Algebra that inserts the rescale so old $v_j$ stay correct under new $(m_i, d'_i)$.</em></p>

Partial output after $i$ tokens (normalized with **current** stats):

$$
o'_i = \sum_{j=1}^{i}\frac{e^{x_j - m_i}}{d'_i}\,v_j
$$

When $(m,d')$ change, previous weights must be multiplied by the same correction that was applied to the denominator.

---

### 6.4 Clean recurrence for $o'_i$

<p align="center">
  <img src="assert/05_h.png" alt="Online output update from o'_{i-1} to o'_i" width="920"/>
</p>

<p align="center"><em>Figure 6d — Highlighted $o'_{i-1}$ term and the closed-form online update.</em></p>

$$
\boxed{
o'_i
=
o'_{i-1}\cdot\frac{d'_{i-1}}{d'_i}\,e^{m_{i-1}-m_i}
\;+\;
\frac{e^{x_i-m_i}}{d'_i}\,v_i
}
$$

Two pieces:

1. **Rescale** everything already accumulated ($o'_{i-1}$)
2. **Add** the new contribution from $v_i$

---

### 6.5 Fully fused single-pass FlashAttention update

<p align="center">
  <img src="assert/05_i.png" alt="Fully fused single-pass online Softmax attention" width="920"/>
</p>

<p align="center"><em>Figure 6e — One loop updates $m$, $d'$, and $o'$ together; return $o'_N$.</em></p>

```text
m_0 = -∞;  d'_0 = 0;  o'_0 = 0

for i = 1 .. N:
    x_i  = q · k_iᵀ
    m_i  = max(m_{i-1}, x_i)
    d'_i = d'_{i-1} * exp(m_{i-1} - m_i) + exp(x_i - m_i)
    o'_i = o'_{i-1} * (d'_{i-1} / d'_i) * exp(m_{i-1} - m_i)
         + (exp(x_i - m_i) / d'_i) * v_i

return o'_N
```

| Property | Standard attention | Fused online update |
|----------|--------------------|---------------------|
| Store full $A$ | Yes ($N\times N$) | No |
| Passes over $K,V$ | Several | **One** (per tile / stream) |
| Extra state / query | — | Only $(m,\ d',\ o')$ |
| Numerical stability | Needs global max | Running max + rescale |

This is the algorithmic heart of **FlashAttention-style loop fusion** (the production kernels also tile for GPU SRAM; the math above is the online core).

---

## Cheatsheet

| Topic | Running state | Correction idea |
|-------|---------------|-----------------|
| Mean | $A_{i-1}$ | add $(x_i-A_{i-1})/i$ |
| Variance | $(\mu_{n-1}, M_{n-1})$ | update $\mu$, then $M$ with $(x-\mu_{\text{old}})(x-\mu_{\text{new}})$ |
| Kadane | $(S_{i-1}, G_{i-1})$ | extend or restart local max |
| Top-2 | $(m_1, m_2)$ | case split on where $x_i$ sits |
| Softmax | $(m_{i-1}, d_{i-1})$ | multiply $d$ by $e^{m_{i-1}-m_i}$ |
| Attention | $(m, d', o')$ | rescale **both** $d'$ and $o'$, then add new $v_i$ |
