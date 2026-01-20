---
layout: default
title: "Linear Diophantine Equations"
parent: "Number Theory"
nav_order: 7
has_children: true
permalink: /30_number_theory/07_linear_diophantine/

---

<div align="center">

# ➗ Linear Diophantine Equations

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-12+-blue?style=for-the-badge" alt="Problems">
</p>

**Integer Solutions to Linear Equations**

*The foundation of integer programming*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 06. Chinese Remainder](../06_chinese_remainder/README.md) | **07. Linear Diophantine** | [08. Binomial Coefficients →](../08_binomial_coefficients/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Basic Form

**Equation:** $ax + by = c$ where $a, b, c \in \mathbb{Z}$

**Goal:** Find integer solutions $(x, y)$

---

### 2️⃣ Existence of Solutions

**Theorem:** $ax + by = c$ has integer solutions **if and only if** $\gcd(a, b) | c$

**Proof:** By Bézout's identity, we can write $ax\_0 + by\_0 = \gcd(a,b)$. If $\gcd(a,b) | c$, then multiplying by $c/\gcd(a,b)$ gives a solution.

---

### 3️⃣ Finding Solutions

**Using Extended GCD:**
1. Compute $g, x\_0, y\_0$ such that $ax\_0 + by\_0 = g = \gcd(a,b)$
2. Check if $g | c$
3. Scale: $x = x\_0 \cdot (c/g)$, $y = y\_0 \cdot (c/g)$

---

### 4️⃣ General Solution

If $(x\_0, y\_0)$ is one solution, all solutions are:

$$
x = x_0 + k \cdot \frac{b}{\gcd(a,b)}, \quad y = y_0 - k \cdot \frac{a}{\gcd(a,b)}
$$

for any integer $k$.

---

### 5️⃣ Frobenius Number

For positive coprime $a, b$, the **Frobenius number** (largest integer NOT representable as $ax + by$ with $x, y \geq 0$):

$$
g(a, b) = ab - a - b
$$

---

## 💻 Code Implementations

```python
def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Returns (gcd, x, y) where ax + by = gcd."""
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def solve_diophantine(a: int, b: int, c: int) -> tuple[int, int] | None:
    """
    Solve ax + by = c for integers x, y.
    
    Returns one solution (x, y) or None if no solution.
    """
    g, x0, y0 = extended_gcd(abs(a), abs(b))
    
    if c % g != 0:
        return None
    
    x0 *= c // g
    y0 *= c // g
    
    # Adjust for negative coefficients
    if a < 0:
        x0 = -x0
    if b < 0:
        y0 = -y0
    
    return x0, y0

def all_solutions(a: int, b: int, c: int, k_range: range) -> list[tuple[int, int]]:
    """Get multiple solutions using parameter k."""
    base = solve_diophantine(a, b, c)
    if base is None:
        return []
    
    x0, y0 = base
    g = extended_gcd(abs(a), abs(b))[0]
    step_x = b // g
    step_y = -a // g
    
    return [(x0 + k * step_x, y0 + k * step_y) for k in k_range]

def positive_solutions(a: int, b: int, c: int) -> list[tuple[int, int]]:
    """Find all non-negative solutions (coin problem)."""
    base = solve_diophantine(a, b, c)
    if base is None:
        return []
    
    x0, y0 = base
    g = extended_gcd(abs(a), abs(b))[0]
    step_x = b // g
    step_y = -a // g
    
    solutions = []

    # Find range of k where both x, y >= 0
    k = 0
    while True:
        x = x0 + k * step_x
        y = y0 + k * step_y
        if x >= 0 and y >= 0:
            solutions.append((x, y))
        k += 1
        if x < 0 and step_x <= 0:
            break
        if y < 0 and step_y <= 0:
            break
        if k > 10**6:  # Safety limit
            break
    
    k = -1
    while True:
        x = x0 + k * step_x
        y = y0 + k * step_y
        if x >= 0 and y >= 0:
            solutions.append((x, y))
        k -= 1
        if x < 0 and step_x >= 0:
            break
        if y < 0 and step_y >= 0:
            break
        if k < -10**6:
            break
    
    return sorted(set(solutions))

def frobenius_number(a: int, b: int) -> int:
    """
    Largest integer not representable as ax + by (x,y >= 0).
    Requires gcd(a, b) = 1.
    """
    from math import gcd
    if gcd(a, b) != 1:
        return float('inf')  # Infinitely many non-representable
    return a * b - a - b

# Examples
print(solve_diophantine(3, 5, 7))  # One solution
print(frobenius_number(3, 5))  # 7
```

---

## 🏆 LeetCode Problems

| # | Problem | Difficulty | Key Concept |
|:-:|---------|:----------:|-------------|
| 1354 | [Construct Target Array With Multiple Sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums/) | 🔴 Hard | Linear combinations |
| 1250 | [Check If It Is a Good Array](https://leetcode.com/problems/check-if-it-is-a-good-array/) | 🔴 Hard | Bézout's identity |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | 🟡 Medium | Frobenius concept |

---

## 💡 Key Insights

> **Coin Problem:** Given coin denominations, Frobenius number tells us the largest amount that CANNOT be made.

> **Checking Feasibility:** Just check if gcd(a, b) divides c - no need to find actual solution.

> **Infinite Solutions:** If one solution exists, infinitely many exist (parametrized by k).

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 06. Chinese Remainder](../06_chinese_remainder/README.md) | **07. Linear Diophantine** | [08. Binomial Coefficients →](../08_binomial_coefficients/README.md) |

