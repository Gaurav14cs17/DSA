# Online Softmax & FlashAttention — Loop Fusion

A visual walkthrough of **online (single-pass) algorithms**, building from classic running statistics up to **Online Safe Softmax** and the fused attention update used in **FlashAttention**.

The core idea is the same everywhere: keep a small **running state**, apply a **correction factor** when a new element arrives, and avoid re-scanning the full sequence.

Diagrams live in [`assert/`](https://github.com/Gaurav14cs17/DSA/tree/main/41_loop_fusion_online/00_online_softmax_flashAtten/assert).

---

## Table of Contents

1. [Running Average (Cumulative Mean)](#1-running-average-cumulative-mean)
2. [Welford’s Variance](#2-welfords-variance)
3. [Maximum Subarray Sum (Kadane)](#3-maximum-subarray-sum-kadane)
4. [First & Second Maximum](#4-first--second-maximum)
5. [Online Safe Softmax](#5-online-safe-softmax)
6. [From Softmax to FlashAttention](#6-from-softmax-to-flashattention)

---

## 1. Running Average (Cumulative Mean)

![Calculating a Running Average](assert/02.jpeg)

**Multi-pass problem.** The average needs a full sum first:

$$
A_N = \frac{1}{N}\sum_{i=1}^{N} x_i
$$

**Running state.** After $i-1$ elements we only keep $A_{i-1}$.

**Single-pass update** (old average + distributed deviation):

$$
A_i = A_{i-1} + \frac{x_i - A_{i-1}}{i}
$$

This is the template for every online algorithm that follows: update state from $(i-1)$ → $i$ without revisiting past data.

---

## 2. Welford’s Variance

![Calculating Variance (Welford's Algorithm)](assert/01.jpeg)

**Multi-pass problem.**

- Pass 1: mean $\mu = \frac{1}{n}\sum x_k$
- Pass 2: $M_n = \sum (x_k - \mu)^2$

That forces storing or re-reading all $x_k$.

**Running state at step $n-1$:** count, mean $\mu_{n-1}$, and sum of squares $M_{n-1}$.

**Single-pass updates:**

$$
\mu_n = \mu_{n-1} + \frac{x_n - \mu_{n-1}}{n}
$$

$$
M_n = M_{n-1} + (x_n - \mu_{n-1})(x_n - \mu_n)
$$

Same pattern as the running mean: a correction that absorbs the change in $\mu$ when $x_n$ arrives.

---

## 3. Maximum Subarray Sum (Kadane)

![Maximum Subarray Sum (Kadane's Algorithm)](assert/03.jpeg)

**Multi-pass problem.** Brute-force over all contiguous subarrays:

$$
G_N = \max_{1 \le j \le k \le N} \sum_{m=j}^{k} x_m
$$

Naive $O(N^3)$ / optimized $O(N^2)$.

**Running state.**

- Local max ending at $i-1$: $S_{i-1}$
- Global max up to $i-1$: $G_{i-1}$

**Single-pass updates** — $O(N)$ time, $O(1)$ space:

$$
S_i = \max(x_i,\ S_{i-1} + x_i)
$$

$$
G_i = \max(G_{i-1},\ S_i)
$$

---

## 4. First & Second Maximum

![Finding the First & Second Maximum Elements](assert/04.jpeg)

**Multi-pass problem.** Find $M_1 = \max(X)$, then scan again for $M_2 = \max(X \setminus \{M_1\})$ — still $O(N)$, but two full passes and $2N$ comparisons.

**Running state.** Keep $(m_{(1,i-1)},\ m_{(2,i-1)})$ for the prefix seen so far.

**Piecewise single-pass update:**

$$
(m_{(1,i)},\ m_{(2,i)}) =
\begin{cases}
(x_i,\ m_{(1,i-1)}) & \text{if } x_i > m_{(1,i-1)} \\
(m_{(1,i-1)},\ x_i) & \text{if } m_{(2,i-1)} < x_i \le m_{(1,i-1)} \\
(m_{(1,i-1)},\ m_{(2,i-1)}) & \text{if } x_i \le m_{(2,i-1)}
\end{cases}
$$

$O(N)$ time with one pass, $O(1)$ space. Tracking a running max (and corrections when it changes) is exactly what Online Softmax needs next.

---

## 5. Online Safe Softmax

### 5a. Denominator calculation

![Online Safe Softmax — Denominator](assert/05_a.jpeg)

**Multi-pass safe softmax.**

1. Pass 1: $m_N = \max_k x_k$ (stability)
2. Pass 2: $d_N = \sum_k e^{x_k - m_N}$

**Running state:** $m_{i-1}$ and $d_{i-1} = \sum_{k=1}^{i-1} e^{x_k - m_{i-1}}$.

**Single-pass updates** (init $m_0 = -\infty$, $d_0 = 0$):

$$
m_i = \max(m_{i-1},\ x_i)
$$

$$
d_i = d_{i-1}\cdot e^{m_{i-1} - m_i} + e^{x_i - m_i}
$$

When a new max appears, $e^{m_{i-1}-m_i}$ rescales the old sum so the denominator stays consistent with the new max.

### 5b–5d. Offline (3-pass) vs online (2-pass)

![Softmax offline vs online derivation](assert/05_b.png)

![Softmax safe offline vs online](assert/05_c.png)

![Softmax 3-pass vs online 2-pass](assert/05_d.png)

**Offline (3 passes):**

| Pass | What it does |
|------|----------------|
| 1 | $m_i = \max(m_{i-1}, x_i)$ → global $m_N$ |
| 2 | $d_i = d_{i-1} + e^{x_i - m_N}$ → $d_N$ |
| 3 | $a_i = e^{x_i - m_N} / d_N$ |

**Online (2 passes):** fuse max + denominator into one loop:

$$
d'_i = d'_{i-1}\, e^{m_{i-1} - m_i} + e^{x_i - m_i}
$$

At the end, $d'_N = d_N$. Then one more pass writes $a_i$. Fewer memory scans — the same loop-fusion idea FlashAttention relies on.

---

## 6. From Softmax to FlashAttention

Attention for a single query row:

$$
S = QK^\top,\quad A = \mathrm{Softmax}(S),\quad O = AV
$$

with $x_i = q\,k_i^\top$ and scores $S = \{x_1,\ldots,x_N\}$.

### 6a–6b. Online softmax inside attention (two-pass view)

![Attention + online softmax](assert/05_e.png)

![Online softmax two-pass attention](assert/05_f.png)

**Pass 1 — running max & denominator:**

```text
m_0 = -∞,  d'_0 = 0
for i = 1 .. N:
    x_i  = q · k_iᵀ
    m_i  = max(m_{i-1}, x_i)
    d'_i = d'_{i-1} · exp(m_{i-1} - m_i) + exp(x_i - m_i)
```

**Pass 2 — accumulate output:**

```text
o_0 = 0
for i = 1 .. N:
    a_i = exp(x_i - m_N) / d'_N
    o_i = o_{i-1} + a_i · v_i
return o_N
```

### 6c–6d. Rescaling the partial output

![Partial output rescaling derivation](assert/05_g.png)

![Online output update o'_{i-1} → o'_i](assert/05_h.png)

To fuse softmax and $AV$ further, also keep a **running output** $o'_i$ and rescale it when $(m, d')$ change:

$$
o'_i =
o'_{i-1}\cdot\frac{d'_{i-1}}{d'_i}\,e^{m_{i-1}-m_i}
\;+\;
\frac{e^{x_i - m_i}}{d'_i}\,v_i
$$

Previous contributions stay correct under the new max / normalizer without storing the full attention row.

### 6e. Fully fused single-pass update

![FlashAttention single-pass online softmax](assert/05_i.png)

```text
m_0 = -∞,  d'_0 = 0,  o'_0 = 0
for i = 1 .. N:
    x_i  = q · k_iᵀ
    m_i  = max(m_{i-1}, x_i)
    d'_i = d'_{i-1} · exp(m_{i-1} - m_i) + exp(x_i - m_i)
    o'_i = o'_{i-1} · (d'_{i-1} / d'_i) · exp(m_{i-1} - m_i)
         + (exp(x_i - m_i) / d'_i) · v_i
return o'_N
```

One pass over keys/values, $O(1)$ extra state per query row, no materialization of the full $N\times N$ attention matrix — the algorithmic core of FlashAttention-style loop fusion.

---

## Summary

| Topic | Multi-pass pain | Online fix |
|-------|-----------------|------------|
| Mean | Need full sum first | $A_i = A_{i-1} + (x_i - A_{i-1})/i$ |
| Variance | Mean pass + squares pass | Welford: update $\mu$ and $M$ together |
| Max subarray | All $(j,k)$ pairs | Kadane local/global max |
| Top-2 max | Two scans | Piecewise running $(m_1, m_2)$ |
| Softmax | Max → sum → normalize | Rescale $d$ with $e^{m_{i-1}-m_i}$ |
| Attention | Full $S$, $A$, then $AV$ | Fuse into online $(m, d', o')$ |

**Assets:** [assert/ on GitHub](https://github.com/Gaurav14cs17/DSA/tree/main/41_loop_fusion_online/00_online_softmax_flashAtten/assert)
