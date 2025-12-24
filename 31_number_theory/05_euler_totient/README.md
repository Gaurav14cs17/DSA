---
layout: default
title: "Euler's Totient"
parent: "Number Theory"
nav_order: 5
has_children: true
permalink: /31_number_theory/05_euler_totient/
---

<div align="center">

# φ Euler's Totient Function

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-15+-blue?style=for-the-badge" alt="Problems">
</p>

**Counting Numbers Coprime to n**

*Essential for cryptography and number theory*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 04. Divisors](../04_divisors/README.md) | **05. Euler Totient** | [06. Chinese Remainder →](../06_chinese_remainder/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Definition

**Euler's Totient Function:** $\phi(n)$ = count of integers from 1 to n that are coprime to n.

$$\phi(n) = |\{k : 1 \leq k \leq n, \gcd(k, n) = 1\}|$$

---

### 2️⃣ Key Formulas

**For prime p:** $\phi(p) = p - 1$

**For prime power:** $\phi(p^k) = p^{k-1}(p-1) = p^k(1 - \frac{1}{p})$

**Multiplicative property:** If $\gcd(m, n) = 1$: $\phi(mn) = \phi(m)\phi(n)$

**General formula:** 
$$\phi(n) = n \prod_{p|n}\left(1 - \frac{1}{p}\right)$$

---

### 3️⃣ Important Properties

**Sum over divisors:** $\sum_{d|n} \phi(d) = n$

**Euler's Theorem:** If $\gcd(a, n) = 1$: $a^{\phi(n)} \equiv 1 \pmod{n}$

---

## 💻 Core Implementations

```python
def euler_phi(n: int) -> int:
    """
    Compute φ(n) using the product formula.
    
    Time: O(√n)
    Space: O(1)
    """
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            result -= result // p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result -= result // n
    return result


def phi_sieve(limit: int) -> list[int]:
    """
    Compute φ(i) for all i from 1 to limit.
    
    Time: O(n log log n)
    Space: O(n)
    """
    phi = list(range(limit + 1))
    
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
    
    return phi


def phi_sum_over_divisors(n: int) -> int:
    """Verify: Σ φ(d) for d|n equals n."""
    divisors = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            divisors.append(d)
            if d * d != n:
                divisors.append(n // d)
        d += 1
    return sum(euler_phi(d) for d in divisors)


# Example values
# φ(1)=1, φ(2)=1, φ(3)=2, φ(4)=2, φ(5)=4, φ(6)=2
# φ(7)=6, φ(8)=4, φ(9)=6, φ(10)=4, φ(12)=4
```

---

## 🏆 LeetCode Problems

| # | Problem | Difficulty | Key Concept |
|:-:|---------|:----------:|-------------|
| 372 | [Super Pow](https://leetcode.com/problems/super-pow/) | 🟡 Medium | Euler's theorem |
| 1808 | [Maximize Number of Nice Divisors](https://leetcode.com/problems/maximize-number-of-nice-divisors/) | 🔴 Hard | Totient application |

---

## 💡 Key Insights

> **φ(n) Growth:** On average, $\phi(n) \approx \frac{n}{\ln \ln n}$

> **φ(n) = n-1:** Only when n is prime

> **φ(2^k) = 2^{k-1}:** Powers of 2 have simple totients

> **RSA Connection:** Security relies on difficulty of computing φ(n) for n = pq

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 04. Divisors](../04_divisors/README.md) | **05. Euler Totient** | [06. Chinese Remainder →](../06_chinese_remainder/README.md) |

