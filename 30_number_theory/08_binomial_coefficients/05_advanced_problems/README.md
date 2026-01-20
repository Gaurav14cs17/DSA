---
layout: default
title: "Advanced Binomial Problems"
parent: "Binomial Coefficients"
grand_parent: "Number Theory"
nav_order: 5
permalink: /30_number_theory/08_binomial_coefficients/05_advanced_problems/
---

<div align="center">

# 🎯 Advanced Binomial Problems

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Competition-Ready-blue?style=for-the-badge" alt="Competition">
</p>

**LeetCode & Competition Problems**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 04. Lucas](../04_lucas_application/README.md) | **05. Advanced** | [🏠 Binomial Home](../README.md) |

---

## 📊 Visual Diagram

<div align="center">

![Binomial Applications](./images/binomial_applications.svg)

</div>

---

## 🏆 LeetCode Problems

| # | Problem | Difficulty | Key |
|:-:|---------|:----------:|-----|
| 62 | Unique Paths | 🟡 Medium | C(m+n-2, m-1) |
| 1569 | Reorder Array Same BST | 🔴 Hard | Binomial + recursion |

---

## 💻 Solutions

### LeetCode 1569: Number of Ways to Reorder Array

```python
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        binom = BinomialMod(len(nums), MOD)
        
        def solve(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            ways = binom.nCr(len(left) + len(right), len(left))
            ways = ways * solve(left) % MOD
            ways = ways * solve(right) % MOD
            
            return ways
        
        return (solve(nums) - 1) % MOD

```

### Stars and Bars

```python
def stars_and_bars(n: int, k: int) -> int:
    """
    Ways to put n identical items into k distinct bins.
    
    C(n + k - 1, k - 1)
    """
    from math import comb
    return comb(n + k - 1, k - 1)

```

---

## 📚 Key Identities

- **Vandermonde:** $\sum\_k C(m,k)C(n,r-k) = C(m+n,r)$

- **Hockey Stick:** $\sum\_{i=r}^{n} C(i,r) = C(n+1,r+1)$

- **Sum of Row:** $\sum\_k C(n,k) = 2^n$

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 04. Lucas](../04_lucas_application/README.md) | **05. Advanced** | [🏠 Binomial Home](../README.md) |
