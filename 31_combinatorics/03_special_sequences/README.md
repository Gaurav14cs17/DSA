---
layout: default
title: "Special Sequences"
parent: "Combinatorics"
nav_order: 3
permalink: /31_combinatorics/03_special_sequences/
---

<div align="center">

# ✨ Special Sequences

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-15+-blue?style=for-the-badge" alt="Problems">
</p>

**Catalan, Fibonacci, and Other Famous Sequences**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 02. Combinations](../02_combinations/README.md) | **03. Special Sequences** | [🏠 Combinatorics Home](../README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Catalan Numbers

**Formula:**

```math
C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)!n!}

```

**Recurrence:**

```math
C_0 = 1, \quad C_n = \sum_{i=0}^{n-1} C_i \cdot C_{n-1-i}

```

**Sequence:** 1, 1, 2, 5, 14, 42, 132, 429, 1430, ...

**Applications:**
- Valid parentheses with n pairs
- Number of BSTs with n nodes
- Ways to triangulate (n+2)-gon
- Paths in n×n grid not crossing diagonal

---

### 2️⃣ Fibonacci Numbers

**Definition:**

```math
F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2}

```

**Sequence:** 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

**Closed Form (Binet's Formula):**

```math
F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}

```

where $\phi = \frac{1+\sqrt{5}}{2}$ (golden ratio), $\psi = \frac{1-\sqrt{5}}{2}$

---

### 3️⃣ Bell Numbers

**Definition:** Number of ways to partition set of n elements.

```math
B_0 = 1, \quad B_n = \sum_{k=0}^{n-1} \binom{n-1}{k} B_k

```

**Sequence:** 1, 1, 2, 5, 15, 52, 203, 877, ...

---

### 4️⃣ Stirling Numbers

**First Kind** $S(n,k)$: Number of permutations of n elements with k cycles.

**Second Kind** $S(n,k)$: Ways to partition n elements into k non-empty subsets.

```math
S(n,k) = k \cdot S(n-1,k) + S(n-1,k-1)

```

---

## 💻 Core Implementations

### Catalan Numbers

```python
def catalan(n: int) -> int:
    """
    Calculate nth Catalan number using formula.
    
    C(n) = (2n)! / ((n+1)! × n!)
         = C(2n, n) / (n+1)
    
    Time: O(n), Space: O(1)
    """
    result = 1
    for i in range(n):
        result = result * (2 * n - i) // (i + 1)
    return result // (n + 1)

def catalan_dp(n: int) -> List[int]:
    """
    Generate first n Catalan numbers using DP.
    
    C(n) = sum(C(i) × C(n-1-i)) for i in [0, n-1]
    
    Time: O(n²), Space: O(n)
    """
    if n == 0:
        return []
    
    cat = [0] * (n + 1)
    cat[0] = cat[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i):
            cat[i] += cat[j] * cat[i - 1 - j]
    
    return cat[1:]

```

### Fibonacci Variants

```python
def fibonacci(n: int) -> int:
    """
    Calculate nth Fibonacci number.
    
    Time: O(n), Space: O(1)
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr

def fibonacci_matrix(n: int) -> int:
    """
    Calculate Fibonacci using matrix exponentiation.
    
    [F(n+1) F(n)  ] = [1 1]^n
    [F(n)   F(n-1)]   [1 0]
    
    Time: O(log n), Space: O(1)
    """
    def matrix_mult(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], 
             A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], 
             A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]
    
    def matrix_power(mat, n):
        if n == 1:
            return mat
        if n % 2 == 0:
            half = matrix_power(mat, n // 2)
            return matrix_mult(half, half)
        return matrix_mult(mat, matrix_power(mat, n - 1))
    
    if n <= 1:
        return n
    
    result = matrix_power([[1, 1], [1, 0]], n)
    return result[0][1]

```

### Tribonacci

```python
def tribonacci(n: int) -> int:
    """
    T(n) = T(n-1) + T(n-2) + T(n-3)
    T(0) = 0, T(1) = T(2) = 1
    
    Time: O(n), Space: O(1)
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    
    return c

```

---

## 🎨 Visual Patterns

### Catalan Applications

```
n=3 Catalan = 5

Valid Parentheses:
()()()  ()(())  (())()  (()())  ((()))

Binary Search Trees (n=3 nodes: 1,2,3):
  1        1          2        3      3
   \        \        / \      /      /
    2        3      1   3    1      2
     \      /                 \    /
      3    2                   2  1

Triangulations of Pentagon:
[5 different ways to divide pentagon into triangles]

```

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Sequence |
|:-:|---------|----------|
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Fibonacci |
| 509 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Fibonacci |
| 1137 | [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | Tribonacci |

### 🟡 Medium

| # | Problem | Sequence |
|:-:|---------|----------|
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Catalan |
| 95 | [Unique BSTs II](https://leetcode.com/problems/unique-binary-search-trees-ii/) | Catalan |
| 96 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | Catalan |
| 873 | [Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/) | Fibonacci |
| 842 | [Split Array into Fibonacci Sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence/) | Fibonacci |
| 1414 | [Find Min Fibonacci Numbers Sum](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/) | Fibonacci |

### 🔴 Hard

| # | Problem | Sequence |
|:-:|---------|----------|
| 1411 | [Number of Ways to Paint N×3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/) | Recurrence |
| 1643 | [Kth Smallest Instructions](https://leetcode.com/problems/kth-smallest-instructions/) | Catalan-like |

---

## 💡 Key Insights

> **Catalan Recognition:**  
> - Balanced/valid sequences
> - Trees/triangulations
> - Paths below diagonal
> - Nested structures

> **Fibonacci Recognition:**  
> - Steps/climbs
> - Tiling problems
> - Sequences with 2-step recurrence

> **Optimization:**  
> - Matrix exponentiation for log time
> - DP for avoiding recomputation
> - Closed form when available

---

## 📚 References

| Sequence | Resource | Link |
|----------|----------|------|
| **Catalan** | OEIS | [A000108](https://oeis.org/A000108) |
| **Fibonacci** | OEIS | [A000045](https://oeis.org/A000045) |
| **Bell** | OEIS | [A000110](https://oeis.org/A000110) |
| **Stirling** | OEIS | [A008277](https://oeis.org/A008277) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 02. Combinations](../02_combinations/README.md) | **03. Special Sequences** | [🏠 Combinatorics Home](../README.md) |

