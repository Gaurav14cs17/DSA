---
layout: default
title: "Legendre's Formula"
parent: "Number Theory"
nav_order: 11
has_children: true
permalink: /31_number_theory/11_legendres_formula/
---

<div align="center">

# 📝 Legendre's Formula

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-10+-blue?style=for-the-badge" alt="Problems">
</p>

**Counting Prime Factors in Factorials**

*Trailing zeros, p-adic valuations, and more*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 10. Lucas Theorem](../10_lucas_theorem/README.md) | **11. Legendre's Formula** | [12. Wilson's Theorem →](../12_wilsons_theorem/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Legendre's Formula

**Statement:** The exponent of prime p in n! is:

$$\nu_p(n!) = \sum_{i=1}^{\infty} \left\lfloor \frac{n}{p^i} \right\rfloor = \frac{n - s_p(n)}{p - 1}$$

where $s_p(n)$ is the sum of digits of n in base p.

---

### 2️⃣ Trailing Zeros

**Trailing zeros in n!** = $\nu_5(n!)$ (since $10 = 2 \times 5$ and there are more 2s than 5s)

$$\text{trailing\_zeros}(n!) = \left\lfloor \frac{n}{5} \right\rfloor + \left\lfloor \frac{n}{25} \right\rfloor + \left\lfloor \frac{n}{125} \right\rfloor + \cdots$$

---

### 3️⃣ p-adic Valuation

**Definition:** $\nu_p(n)$ = largest power of p dividing n.

**Properties:**
- $\nu_p(ab) = \nu_p(a) + \nu_p(b)$
- $\nu_p(a + b) \geq \min(\nu_p(a), \nu_p(b))$
- $\nu_p(\binom{n}{k}) = \frac{s_p(k) + s_p(n-k) - s_p(n)}{p-1}$

---

## 🎨 Visual Walkthrough

```
┌─────────────────────────────────────────────────────────────────┐
│ TRAILING ZEROS IN 100!                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ Count multiples of 5, 25, 125, ...                             │
│                                                                 │
│ ⌊100/5⌋   = 20  (multiples of 5: 5,10,15,...,100)             │
│ ⌊100/25⌋  = 4   (multiples of 25: 25,50,75,100)               │
│ ⌊100/125⌋ = 0   (no multiples of 125 ≤ 100)                   │
│                                                                 │
│ Total = 20 + 4 + 0 = 24 trailing zeros                         │
│                                                                 │
│ Verification: 100! = ...00000000000000000000000                │
│                      └─────── 24 zeros ───────┘                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Code Implementations

```python
def legendre(n: int, p: int) -> int:
    """
    Compute the exponent of prime p in n!
    
    ν_p(n!) = Σ ⌊n/p^i⌋
    
    Time: O(log_p(n))
    Space: O(1)
    """
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count


def trailing_zeros(n: int) -> int:
    """
    LeetCode 172: Count trailing zeros in n!
    
    Trailing zeros = ν₅(n!)
    """
    count = 0
    power = 5
    while power <= n:
        count += n // power
        power *= 5
    return count


def p_adic_valuation(n: int, p: int) -> int:
    """Compute ν_p(n) - largest power of p dividing n."""
    if n == 0:
        return float('inf')
    
    count = 0
    while n % p == 0:
        count += 1
        n //= p
    return count


def prime_power_in_binomial(n: int, k: int, p: int) -> int:
    """
    Compute ν_p(C(n, k)) using Kummer's theorem.
    
    = number of carries when adding k and n-k in base p
    """
    return (legendre(n, p) - legendre(k, p) - legendre(n - k, p))


def factorial_without_prime(n: int, p: int, mod: int) -> int:
    """
    Compute n! / p^(ν_p(n!)) mod p
    
    Useful for computing C(n,k) mod p^e.
    """
    result = 1
    for i in range(1, n + 1):
        num = i
        while num % p == 0:
            num //= p
        result = result * num % mod
    return result


# LeetCode 172: Factorial Trailing Zeroes
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count


# Example: Trailing zeros in 1000!
print(trailing_zeros(1000))  # 249

# Example: Power of 2 in 10!
print(legendre(10, 2))  # 8 (10! = 2^8 × odd)
```

---

## 🏆 LeetCode Problems

| # | Problem | Difficulty | Key Concept |
|:-:|---------|:----------:|-------------|
| 172 | [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) | 🟡 Medium | Legendre's formula |
| 793 | [Preimage Size of Factorial Zeroes Function](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/) | 🔴 Hard | Inverse problem |

---

## 💡 Key Insights

> **Why 5 for trailing zeros?** 10 = 2 × 5, and there are always more factors of 2 than 5 in n!

> **Binary Representation:** $\nu_2(n!) = n - \text{popcount}(n)$

> **Kummer's Theorem:** $\nu_p(\binom{m}{n})$ = number of carries in base-p addition of n and m-n.

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 10. Lucas Theorem](../10_lucas_theorem/README.md) | **11. Legendre's Formula** | [12. Wilson's Theorem →](../12_wilsons_theorem/README.md) |
