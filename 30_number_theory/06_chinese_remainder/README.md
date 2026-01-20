---
layout: default
title: "Chinese Remainder Theorem"
parent: "Number Theory"
nav_order: 6
has_children: true
permalink: /30_number_theory/06_chinese_remainder/
---

<div align="center">

# 🏛️ Chinese Remainder Theorem

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-10+-blue?style=for-the-badge" alt="Problems">
</p>

**Solving Systems of Linear Congruences**

*Ancient theorem with modern applications*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 05. Euler Totient](../05_euler_totient/README.md) | **06. Chinese Remainder** | [07. Linear Diophantine →](../07_linear_diophantine/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ The Theorem

**Statement:** Given pairwise coprime moduli $m\_1, m\_2, \ldots, m\_k$ and any integers $a\_1, a\_2, \ldots, a\_k$, the system:

```math
\begin{cases}
x \equiv a_1 \pmod{m_1} \\
x \equiv a_2 \pmod{m_2} \\
\vdots \\
x \equiv a_k \pmod{m_k}
\end{cases}

```

has a unique solution modulo $M = m\_1 \cdot m\_2 \cdots m\_k$.

---

### 2️⃣ Construction Formula

Let $M\_i = M / m\_i$ and $y\_i = M\_i^{-1} \pmod{m\_i}$

```math
x = \sum_{i=1}^{k} a_i \cdot M_i \cdot y_i \pmod{M}

```

---

### 3️⃣ Two Moduli Case

For $x \equiv a\_1 \pmod{m\_1}$ and $x \equiv a\_2 \pmod{m\_2}$:

```math
x = a_1 + m_1 \cdot \frac{(a_2 - a_1) \cdot m_1^{-1} \pmod{m_2}}{1} \pmod{m_1 \cdot m_2}

```

---

## 🎨 Visual Walkthrough

```
+-----------------------------------------------------------------+
| PROBLEM: Solve x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)   |
+-----------------------------------------------------------------+
| STEP 1: Compute M = 3 × 5 × 7 = 105                            |
|                                                                 |
| STEP 2: Compute M_i values                                     |
|   M₁ = 105/3 = 35                                              |
|   M₂ = 105/5 = 21                                              |
|   M₃ = 105/7 = 15                                              |
|                                                                 |
| STEP 3: Compute modular inverses y_i                           |
|   y₁ = 35⁻¹ (mod 3) = 2⁻¹ (mod 3) = 2                         |
|   y₂ = 21⁻¹ (mod 5) = 1⁻¹ (mod 5) = 1                         |
|   y₃ = 15⁻¹ (mod 7) = 1⁻¹ (mod 7) = 1                         |
|                                                                 |
| STEP 4: Compute x                                               |
|   x = 2×35×2 + 3×21×1 + 2×15×1                                 |
|     = 140 + 63 + 30                                            |
|     = 233                                                      |
|     = 233 mod 105 = 23                                         |
|                                                                 |
| VERIFY: 23 mod 3 = 2 ✓, 23 mod 5 = 3 ✓, 23 mod 7 = 2 ✓        |
+-----------------------------------------------------------------+

```

---

## 💻 Code Implementations

```python
def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Returns (gcd, x, y) where ax + by = gcd."""
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def mod_inverse(a: int, m: int) -> int:
    """Compute modular inverse of a mod m."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def chinese_remainder(remainders: list[int], moduli: list[int]) -> int:
    """
    Solve system of congruences using CRT.
    
    x ≡ remainders[i] (mod moduli[i])
    
    Time: O(n log M)
    Space: O(1)
    """
    M = 1
    for m in moduli:
        M *= m
    
    x = 0
    for a_i, m_i in zip(remainders, moduli):
        M_i = M // m_i
        y_i = mod_inverse(M_i, m_i)
        x += a_i * M_i * y_i
    
    return x % M

def crt_two_moduli(a1: int, m1: int, a2: int, m2: int) -> tuple[int, int]:
    """
    Solve x ≡ a1 (mod m1), x ≡ a2 (mod m2).
    
    Works for non-coprime moduli too (if solution exists).
    
    Returns (x, lcm(m1, m2)) or (None, None) if no solution.
    """
    from math import gcd
    
    g = gcd(m1, m2)
    if (a2 - a1) % g != 0:
        return None, None
    
    lcm = m1 * m2 // g
    _, x, _ = extended_gcd(m1, m2)
    
    diff = (a2 - a1) // g
    x = (a1 + m1 * x * diff) % lcm
    
    return x, lcm

# Example usage
print(chinese_remainder([2, 3, 2], [3, 5, 7]))  # 23

```

---

## 🏆 LeetCode Problems

| # | Problem | Difficulty | Key Concept |
|:-:|---------|:----------:|-------------|
| 1175 | [Prime Arrangements](https://leetcode.com/problems/prime-arrangements/) | 🟢 Easy | CRT counting |
| 458 | [Poor Pigs](https://leetcode.com/problems/poor-pigs/) | 🔴 Hard | Information theory |

---

## 💡 Key Insights

> **Existence Condition:** CRT requires pairwise coprime moduli. For general moduli, solution exists iff $a\_i \equiv a\_j \pmod{\gcd(m\_i, m\_j)}$ for all pairs.

> **Applications:** RSA speedup (computing mod p and mod q separately), hash collision avoidance, reconstructing large numbers

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 05. Euler Totient](../05_euler_totient/README.md) | **06. Chinese Remainder** | [07. Linear Diophantine →](../07_linear_diophantine/README.md) |

