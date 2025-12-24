---
layout: default
title: "Combinations"
parent: "Combinatorics"
nav_order: 2
permalink: /32_combinatorics/02_combinations/
---

<div align="center">

# 🎯 Combinations

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Hard-green?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-25+-blue?style=for-the-badge" alt="Problems">
</p>

**Selections Where Order Doesn't Matter**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. Permutations](../01_permutations/README.md) | **02. Combinations** | [03. Special Sequences →](../03_special_sequences/README.md) |

---

## 📐 Mathematical Foundations

### Combination Formula

$$\binom{n}{r} = C(n,r) = \frac{n!}{r!(n-r)!}$$

**Key Properties:**
- $\binom{n}{r} = \binom{n}{n-r}$ (Symmetry)
- $\binom{n}{0} = \binom{n}{n} = 1$
- $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$ (Pascal's Identity)

### Pascal's Triangle

```
Row 0:                    1
Row 1:                  1   1
Row 2:                1   2   1
Row 3:              1   3   3   1
Row 4:            1   4   6   4   1
Row 5:          1   5  10  10   5   1

Entry at row n, position r = C(n,r)
```

---

## 💻 Core Implementations

### nCr Calculation

```python
def nCr(n: int, r: int) -> int:
    """
    Calculate C(n,r) efficiently.
    
    Optimization: Use smaller of r and n-r
    
    Time: O(min(r, n-r))
    Space: O(1)
    """
    if r > n - r:
        r = n - r
    
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    
    return result


def nCr_mod(n: int, r: int, mod: int) -> int:
    """
    Calculate C(n,r) mod m using Pascal's triangle.
    
    Time: O(n×r)
    Space: O(r)
    """
    if r > n:
        return 0
    
    dp = [0] * (r + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            dp[j] = (dp[j] + dp[j - 1]) % mod
    
    return dp[r]
```

### Generate All Combinations

```python
def combine(n: int, k: int) -> List[List[int]]:
    """
    Generate all k-combinations from 1 to n.
    
    Time: O(C(n,k) × k)
    Space: O(C(n,k) × k)
    """
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        # Optimization: only iterate through valid choices
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(1, [])
    return result
```

### Pascal's Triangle Generation

```python
def generate_pascal(numRows: int) -> List[List[int]]:
    """
    Generate first numRows of Pascal's triangle.
    
    Time: O(n²)
    Space: O(n²)
    """
    if numRows == 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle
```

---

## 🏆 LeetCode Problems

### 🟢 Easy
| # | Problem | Concept |
|:-:|---------|---------|
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Fibonacci |
| 118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | Generate triangle |
| 119 | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) | Space optimized |

### 🟡 Medium
| # | Problem | Concept |
|:-:|---------|---------|
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | With repetition |
| 40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | No repetition |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Grid = nCr |
| 77 | [Combinations](https://leetcode.com/problems/combinations/) | Basic generation |
| 216 | [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) | Fixed size |
| 377 | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) | Order matters |

### 🔴 Hard
| # | Problem | Concept |
|:-:|---------|---------|
| 1735 | [Count Ways to Make Array](https://leetcode.com/problems/count-ways-to-make-array-with-product/) | Prime factorization |
| 1994 | [Number of Good Subsets](https://leetcode.com/problems/the-number-of-good-subsets/) | Bitmask + nCr |
| 2338 | [Count Ideal Arrays](https://leetcode.com/problems/count-the-number-of-ideal-arrays/) | Stars and bars |

---

## 💡 Key Insights

> **Combinations vs Permutations:**  
> - {A,B,C} = {C,A,B} in combinations  
> - ABC ≠ CAB in permutations

> **When to Use:**  
> - Selecting items
> - Subsets
> - Grid paths
> - "Choose k from n"

> **Optimization:**  
> - Use C(n,r) = C(n, n-r)
> - Pascal's triangle for multiple queries
> - Modular arithmetic for large values

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. Permutations](../01_permutations/README.md) | **02. Combinations** | [03. Special Sequences →](../03_special_sequences/README.md) |

