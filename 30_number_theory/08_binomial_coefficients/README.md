---
layout: default
title: "Binomial Coefficients"
parent: "Number Theory"
nav_order: 8
has_children: true
permalink: /30_number_theory/08_binomial_coefficients/
---

<div align="center">

# 🔢 Binomial Coefficients

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Medium-yellow?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-25+-blue?style=for-the-badge" alt="Problems">
</p>

**Counting Combinations and Pascal's Triangle**

*Fundamental to combinatorics and probability*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 07. Linear Diophantine](../07_linear_diophantine/README.md) | **08. Binomial Coefficients** | [09. Catalan Numbers →](../09_catalan_numbers/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Definition

**Binomial Coefficient:** "n choose k"

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

**Meaning:** Number of ways to choose k items from n items.

---

### 2️⃣ Key Properties

**Symmetry:** $\binom{n}{k} = \binom{n}{n-k}$

**Pascal's Rule:** $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$

**Sum of Row:** $\sum_{k=0}^{n} \binom{n}{k} = 2^n$

**Hockey Stick:** $\sum_{i=r}^{n} \binom{i}{r} = \binom{n+1}{r+1}$

---

### 3️⃣ Pascal's Triangle

```
                1
              1   1
            1   2   1
          1   3   3   1
        1   4   6   4   1
      1   5  10  10   5   1
    1   6  15  20  15   6   1
```

---

## 💻 Core Implementations

```python
def nCr_dp(n: int, k: int) -> int:
    """Compute C(n,k) using Pascal's triangle."""
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    
    # Only need previous row
    dp = [1] * (k + 1)
    for i in range(1, n - k + 1):
        for j in range(min(i, k), 0, -1):
            dp[j] += dp[j - 1]
    
    return dp[k]


def nCr_formula(n: int, k: int) -> int:
    """Compute C(n,k) using multiplicative formula."""
    if k > n or k < 0:
        return 0
    if k > n - k:
        k = n - k
    
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    
    return result


def nCr_mod(n: int, k: int, mod: int) -> int:
    """Compute C(n,k) mod p (prime) using Fermat's theorem."""
    if k > n or k < 0:
        return 0
    
    # Precompute factorials
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    # C(n,k) = n! / (k! * (n-k)!)
    return fact[n] * pow(fact[k], mod - 2, mod) % mod * pow(fact[n - k], mod - 2, mod) % mod


def pascals_triangle(n: int) -> list[list[int]]:
    """Generate first n rows of Pascal's triangle."""
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle


def binomial_theorem(a: int, b: int, n: int) -> int:
    """Compute (a + b)^n using binomial theorem."""
    result = 0
    for k in range(n + 1):
        result += nCr_formula(n, k) * (a ** (n - k)) * (b ** k)
    return result


# Precomputation for multiple queries
class BinomialCoeff:
    def __init__(self, max_n: int, mod: int = 10**9 + 7):
        self.mod = mod
        self.fact = [1] * (max_n + 1)
        self.inv_fact = [1] * (max_n + 1)
        
        for i in range(1, max_n + 1):
            self.fact[i] = self.fact[i - 1] * i % mod
        
        self.inv_fact[max_n] = pow(self.fact[max_n], mod - 2, mod)
        for i in range(max_n - 1, -1, -1):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % mod
    
    def nCr(self, n: int, r: int) -> int:
        if r > n or r < 0:
            return 0
        return self.fact[n] * self.inv_fact[r] % self.mod * self.inv_fact[n - r] % self.mod
```

---

## 🏆 LeetCode Problems

| # | Problem | Difficulty | Key Concept |
|:-:|---------|:----------:|-------------|
| 118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | 🟢 Easy | Generate triangle |
| 119 | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) | 🟢 Easy | Single row |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | 🟡 Medium | C(m+n-2, m-1) |
| 63 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | 🟡 Medium | DP with obstacles |
| 96 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | 🟡 Medium | Catalan numbers |

---

## 💡 Key Insights

> **Unique Paths:** Paths in m×n grid = C(m+n-2, m-1) = C(m+n-2, n-1)

> **Modular Computation:** Precompute factorials and inverse factorials for O(1) queries

> **Lucas' Theorem:** For prime p: $\binom{n}{k} \equiv \prod \binom{n_i}{k_i} \pmod{p}$ where $n_i, k_i$ are base-p digits

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 07. Linear Diophantine](../07_linear_diophantine/README.md) | **08. Binomial Coefficients** | [09. Catalan Numbers →](../09_catalan_numbers/README.md) |

