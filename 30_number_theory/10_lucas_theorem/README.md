---
layout: default
title: "Lucas' Theorem"
parent: "Number Theory"
nav_order: 10
has_children: true
permalink: /30_number_theory/10_lucas_theorem/
---

<div align="center">

# 🔮 Lucas' Theorem

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Applications-Large_Binomials-blue?style=for-the-badge" alt="Applications">
</p>

**Computing Binomial Coefficients Modulo Prime**

*Essential for large n, k with small prime modulus*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 09. Catalan Numbers](../09_catalan_numbers/README.md) | **10. Lucas Theorem** | [11. Legendre's Formula →](../11_legendres_formula/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Lucas' Theorem

**Statement:** For prime p and non-negative integers m, n:

```math
\binom{m}{n} \equiv \prod_{i=0}^{k} \binom{m_i}{n_i} \pmod{p}

```

where $m = \sum m_i p^i$ and $n = \sum n_i p^i$ are base-p representations.

---

### 2️⃣ Special Cases

**If $n_i > m_i$ for any i:** $\binom{m}{n} \equiv 0 \pmod{p}$

**Small p:** For $p = 2$, the binomial is odd iff n is a "submask" of m in binary.

---

### 3️⃣ Sierpiński Triangle Connection

The pattern of odd entries in Pascal's triangle forms a Sierpiński triangle - this is a direct consequence of Lucas' theorem with p = 2.

---

## 💻 Code Implementations

```python
def lucas(m: int, n: int, p: int) -> int:
    """
    Compute C(m, n) mod p using Lucas' theorem.
    
    Works for very large m, n when p is small prime.
    
    Time: O(log_p(m) × p)
    Space: O(p)
    """
    if n > m:
        return 0
    
    # Precompute factorials and inverses mod p
    fact = [1] * p
    for i in range(1, p):
        fact[i] = fact[i - 1] * i % p
    
    inv_fact = [1] * p
    inv_fact[p - 1] = pow(fact[p - 1], p - 2, p)
    for i in range(p - 2, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % p
    
    def small_nCr(a: int, b: int) -> int:
        if b > a or b < 0:
            return 0
        return fact[a] * inv_fact[b] % p * inv_fact[a - b] % p
    
    result = 1
    while m > 0 or n > 0:
        m_i = m % p
        n_i = n % p
        result = result * small_nCr(m_i, n_i) % p
        m //= p
        n //= p
    
    return result

def lucas_simple(m: int, n: int, p: int) -> int:
    """Simpler Lucas implementation (slower but clearer)."""
    def nCr_small(a: int, b: int) -> int:
        if b > a:
            return 0
        if b == 0:
            return 1
        return nCr_small(a - 1, b - 1) * a // b
    
    if n == 0:
        return 1
    return (nCr_small(m % p, n % p) * lucas_simple(m // p, n // p, p)) % p

def is_binomial_odd(m: int, n: int) -> bool:
    """
    Check if C(m, n) is odd using Lucas' theorem.
    
    C(m, n) is odd iff (n & m) == n (n is submask of m).
    """
    return (n & m) == n

def count_odd_in_row(n: int) -> int:
    """
    Count odd entries in nth row of Pascal's triangle.
    
    Equals 2^(popcount(n)) by Lucas' theorem.
    """
    return 1 << bin(n).count('1')

# Example: C(1000000, 500000) mod 13
print(lucas(1000000, 500000, 13))

# Example: Is C(10, 3) odd?
# 10 = 1010₂, 3 = 0011₂
# 3 & 10 = 0010 ≠ 3, so C(10, 3) = 120 is even ✓
print(is_binomial_odd(10, 3))  # False

```

---

## 🏆 LeetCode Problems

| # | Problem | Difficulty | Key Concept |
|:-:|---------|:----------:|-------------|
| 118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | 🟢 Easy | Pattern observation |
| 119 | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) | 🟢 Easy | Row computation |

---

## 💡 Key Insights

> **When to Use Lucas:** When n, m are huge (10^18) but p is small (< 10^6).

> **Factorial Precomputation:** Only need factorials up to p-1.

> **Sierpiński Pattern:** C(m, n) mod 2 = 1 iff n is binary submask of m.

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 09. Catalan Numbers](../09_catalan_numbers/README.md) | **10. Lucas Theorem** | [11. Legendre's Formula →](../11_legendres_formula/README.md) |

