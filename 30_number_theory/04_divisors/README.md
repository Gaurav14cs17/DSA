---
layout: default
title: "Divisors"
parent: "Number Theory"
nav_order: 4
has_children: true
permalink: /30_number_theory/04_divisors/
---

<div align="center">

# 📊 Divisors

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Medium-yellow?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-20+-blue?style=for-the-badge" alt="Problems">
</p>

**Counting, Summing, and Understanding Divisors**

*Master divisor functions and their applications*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 03. Modular Arithmetic](../03_modular_arithmetic/README.md) | **04. Divisors** | [05. Euler Totient →](../05_euler_totient/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Divisor Count Function τ(n)

**Definition:** $\tau(n)$ = number of positive divisors of n.

**Formula:** If $n = p\_1^{a\_1} \cdots p\_k^{a\_k}$:

```math
\tau(n) = (a_1 + 1)(a_2 + 1) \cdots (a_k + 1)

```

**Examples:**

- $\tau(12) = \tau(2^2 \cdot 3^1) = (2+1)(1+1) = 6$

- Divisors of 12: 1, 2, 3, 4, 6, 12

---

### 2️⃣ Divisor Sum Function σ(n)

**Definition:** $\sigma(n)$ = sum of positive divisors of n.

**Formula:** If $n = p\_1^{a\_1} \cdots p\_k^{a\_k}$:

```math
\sigma(n) = \prod_{i=1}^{k} \frac{p_i^{a_i+1} - 1}{p_i - 1}

```

**Examples:**

- $\sigma(12) = 1+2+3+4+6+12 = 28$

---

### 3️⃣ Perfect Numbers

**Definition:** n is perfect if $\sigma(n) = 2n$ (sum of proper divisors = n).

**Examples:** 6, 28, 496, 8128

**Euclid-Euler Theorem:** Even perfect numbers have form $2^{p-1}(2^p - 1)$ where $2^p - 1$ is prime (Mersenne prime).

---

## 💻 Core Implementations

```python
def count_divisors(n: int) -> int:
    """Count divisors using τ(n) = ∏(aᵢ + 1)."""
    count = 1
    d = 2
    while d * d <= n:
        exp = 0
        while n % d == 0:
            exp += 1
            n //= d
        count *= (exp + 1)
        d += 1
    if n > 1:
        count *= 2
    return count

def sum_divisors(n: int) -> int:
    """Sum divisors using σ(n) formula."""
    result = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            power_sum = 1
            p_power = 1
            while n % d == 0:
                p_power *= d
                power_sum += p_power
                n //= d
            result *= power_sum
        d += 1
    if n > 1:
        result *= (1 + n)
    return result

def get_divisors(n: int) -> list[int]:
    """Get all divisors of n."""
    divisors = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            divisors.append(d)
            if d * d != n:
                divisors.append(n // d)
        d += 1
    return sorted(divisors)

def is_perfect(n: int) -> bool:
    """Check if n is a perfect number."""
    return sum_divisors(n) == 2 * n

def sieve_divisor_count(limit: int) -> list[int]:
    """Compute τ(i) for all i from 1 to limit."""
    tau = [0] * (limit + 1)
    for d in range(1, limit + 1):
        for multiple in range(d, limit + 1, d):
            tau[multiple] += 1
    return tau

```

---

## 🏆 LeetCode Problems

| # | Problem | Difficulty | Key Concept |
|:-:|---------|:----------:|-------------|
| 1390 | [Four Divisors](https://leetcode.com/problems/four-divisors/) | 🟡 Medium | Divisor counting |
| 507 | [Perfect Number](https://leetcode.com/problems/perfect-number/) | 🟢 Easy | Sum of divisors |
| 1492 | [The kth Factor of n](https://leetcode.com/problems/the-kth-factor-of-n/) | 🟡 Medium | Finding divisors |
| 1952 | [Three Divisors](https://leetcode.com/problems/three-divisors/) | 🟢 Easy | Perfect squares of primes |

---

## 💡 Key Insights

> **Highly Composite Numbers:** Numbers with many divisors: 1, 2, 4, 6, 12, 24, 36, 48, 60, 120...

> **Average Number of Divisors:** $\sum\_{i=1}^{n} \tau(i) \approx n \ln n$

> **Maximum Divisors for n ≤ 10^9:** About 1344 divisors (for 735134400)

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 03. Modular Arithmetic](../03_modular_arithmetic/README.md) | **04. Divisors** | [05. Euler Totient →](../05_euler_totient/README.md) |

