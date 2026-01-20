---
layout: default
title: "Catalan Numbers"
parent: "Number Theory"
nav_order: 9
has_children: true
permalink: /30_number_theory/09_catalan_numbers/
---

<div align="center">

# 🌳 Catalan Numbers

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-15+-blue?style=for-the-badge" alt="Problems">
</p>

**The Magic Sequence That Counts Everything**

*BSTs, parentheses, paths, and polygons*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 08. Binomial Coefficients](../08_binomial_coefficients/README.md) | **09. Catalan Numbers** | [10. Lucas Theorem →](../10_lucas_theorem/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Definition

**nth Catalan Number:**

```math
C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)!n!}

```

**First values:** 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862...

---

### 2️⃣ Recurrence Relation

```math
C_n = \sum_{i=0}^{n-1} C_i \cdot C_{n-1-i}
C_n = \frac{2(2n-1)}{n+1} C_{n-1}

```

---

### 3️⃣ Things Catalan Numbers Count

| Problem | Count |
|---------|-------|
| Valid parentheses with n pairs | $C_n$ |
| Binary trees with n+1 leaves | $C_n$ |
| Full binary trees with n internal nodes | $C_n$ |
| Unique BSTs with n nodes | $C_n$ |
| Paths from (0,0) to (n,n) staying below diagonal | $C_n$ |
| Ways to triangulate (n+2)-gon | $C_n$ |
| Non-crossing partitions of n points | $C_n$ |

---

## 🎨 Visual Walkthrough

```
+-----------------------------------------------------------------+
| CATALAN NUMBERS AND BST COUNTING                               |
+-----------------------------------------------------------------+
|                                                                 |
| n = 3: C₃ = 5 unique BSTs with nodes {1, 2, 3}                |
|                                                                 |
|     1         1           2           3       3                 |
|      \         \         / \         /       /                  |
|       2         3       1   3       2       1                   |
|        \       /                   /         \                  |
|         3     2                   1           2                 |
|                                                                 |
| Recurrence: C₃ = C₀×C₂ + C₁×C₁ + C₂×C₀                        |
|                = 1×2 + 1×1 + 2×1                               |
|                = 2 + 1 + 2 = 5 ✓                               |
+-----------------------------------------------------------------+

```

---

## 💻 Code Implementations

```python
def catalan_dp(n: int) -> int:
    """Compute nth Catalan number using DP."""
    if n <= 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    
    return dp[n]

def catalan_formula(n: int) -> int:
    """Compute nth Catalan using binomial formula."""
    # C_n = C(2n, n) / (n + 1)
    result = 1
    for i in range(n):
        result = result * (2 * n - i) // (i + 1)
    return result // (n + 1)

def catalan_mod(n: int, mod: int) -> int:
    """Compute nth Catalan mod prime."""
    # C_n = C(2n, n) * inverse(n+1) mod p
    
    # Compute C(2n, n)
    num = 1
    for i in range(n + 1, 2 * n + 1):
        num = num * i % mod
    
    den = 1
    for i in range(1, n + 1):
        den = den * i % mod
    
    binomial = num * pow(den, mod - 2, mod) % mod
    return binomial * pow(n + 1, mod - 2, mod) % mod

def num_trees(n: int) -> int:
    """LeetCode 96: Unique Binary Search Trees."""
    return catalan_dp(n)

def generate_parentheses(n: int) -> list[str]:
    """LeetCode 22: Generate valid parentheses (C_n combinations)."""
    result = []
    
    def backtrack(s: str, open_count: int, close_count: int):
        if len(s) == 2 * n:
            result.append(s)
            return
        
        if open_count < n:
            backtrack(s + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(s + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result

# Verify: len(generate_parentheses(n)) == catalan_dp(n)

```

---

## 🏆 LeetCode Problems

| # | Problem | Difficulty | Key Concept |
|:-:|---------|:----------:|-------------|
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | 🟡 Medium | C_n valid sequences |
| 96 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | 🟡 Medium | Catalan recurrence |
| 95 | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) | 🟡 Medium | Generate all BSTs |
| 894 | [All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/) | 🟡 Medium | Full binary trees |

---

## 💡 Key Insights

> **Growth Rate:** $C_n \approx \frac{4^n}{n^{3/2}\sqrt{\pi}}$

> **BST Counting:** Root can be any of n nodes; left subtree has i nodes, right has n-1-i nodes.

> **Ballot Problem:** Catalan = paths that never go above diagonal.

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 08. Binomial Coefficients](../08_binomial_coefficients/README.md) | **09. Catalan Numbers** | [10. Lucas Theorem →](../10_lucas_theorem/README.md) |

