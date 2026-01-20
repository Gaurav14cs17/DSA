---
layout: default
title: "GCD & LCM"
parent: "Number Theory"
nav_order: 1
permalink: /30_number_theory/01_gcd_lcm/
---

<div align="center">

# 🔢 GCD & LCM

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Medium-yellow?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-30+-blue?style=for-the-badge" alt="Problems">
</p>

**Greatest Common Divisor & Least Common Multiple**

*Master Euclidean algorithms and number theory fundamentals*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [🏠 Number Theory Home](../README.md) | **01. GCD & LCM** | [02. Primes →](../02_primes/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ GCD Definition & Properties

**Definition:** The Greatest Common Divisor (GCD) of two integers a and b is the largest positive integer d such that:
- $d \mid a$ (d divides a)
- $d \mid b$ (d divides b)
- For any other common divisor c: $c \leq d$

**Notation:** $\gcd(a, b)$ or $(a, b)$

**Key Properties:**

```math
\begin{align}
\gcd(a, b) &= \gcd(b, a) \quad \text{(Commutative)} \\
\gcd(a, \gcd(b, c)) &= \gcd(\gcd(a, b), c) \quad \text{(Associative)} \\
\gcd(a, 0) &= a \quad \text{(Identity)} \\
\gcd(a, 1) &= 1 \\
\gcd(a, b) &= 1 \iff \text{a and b are coprime}
\end{align}

```

---

### 2️⃣ Euclidean Algorithm

**Fundamental Theorem:**

```math
\gcd(a, b) = \gcd(b, a \bmod b)

```

**Proof:**
Let $d = \gcd(a, b)$. Then $a = d \cdot m$ and $b = d \cdot n$ for some integers $m, n$.

```math
\begin{align}
a \bmod b &= a - q \cdot b \quad \text{where } q = \lfloor a/b \rfloor \\
&= d \cdot m - q \cdot d \cdot n \\
&= d \cdot (m - q \cdot n)
\end{align}

```

So $d$ divides $(a \bmod b)$. By similar reasoning, any common divisor of $b$ and $(a \bmod b)$ also divides $a$ and $b$.

Therefore: $\gcd(a, b) = \gcd(b, a \bmod b)$ ∎

**Time Complexity (Lamé's Theorem):**

```math
T(a, b) = O(\log \min(a, b))

```

**Proof:** If $a > b$, then $a \bmod b < a/2$, so problem size halves every 2 steps at most. ∎

---

### 3️⃣ Extended Euclidean Algorithm

**Bézout's Identity:** For any integers $a, b$, there exist integers $x, y$ such that:

```math
a \cdot x + b \cdot y = \gcd(a, b)

```

**Algorithm:**

```
Base case: If b = 0, then gcd = a, x = 1, y = 0
Recursive case:
  (d, x₁, y₁) = ExtGCD(b, a mod b)
  x = y₁
  y = x₁ - ⌊a/b⌋ · y₁
  return (d, x, y)

```

**Applications:**
- Modular inverse
- Linear Diophantine equations
- Chinese Remainder Theorem
- RSA cryptography

---

### 4️⃣ LCM Definition & Formula

**Definition:** The Least Common Multiple (LCM) of two integers a and b is the smallest positive integer m such that:
- $a \mid m$ (a divides m)
- $b \mid m$ (b divides m)

**Fundamental Formula:**

```math
\text{lcm}(a, b) = \frac{a \times b}{\gcd(a, b)}

```

**Proof:**
Let $d = \gcd(a, b)$. Then $a = d \cdot x$ and $b = d \cdot y$ where $\gcd(x, y) = 1$.

The LCM must be $d \cdot x \cdot y$ (smallest number divisible by both):

```math
\text{lcm}(a, b) = d \cdot x \cdot y = \frac{(d \cdot x) \cdot (d \cdot y)}{d} = \frac{a \cdot b}{\gcd(a, b)}

```

∎

---

### 5️⃣ GCD and Prime Factorization

**Theorem:** If $a = p\_1^{a\_1} \cdot p\_2^{a\_2} \cdots p\_k^{a\_k}$ and $b = p\_1^{b\_1} \cdot p\_2^{b\_2} \cdots p\_k^{b\_k}$, then:

```
\begin{align}
\gcd(a, b) &= p_1^{\min(a_1, b_1)} \cdot p_2^{\min(a_2, b_2)} \cdots p_k^{\min(a_k, b_k)} \\
\text{lcm}(a, b) &= p_1^{\max(a_1, b_1)} \cdot p_2^{\max(a_2, b_2)} \cdots p_k^{\max(a_k, b_k)}
\end{align}

```math
**Example:**

```

\begin{align}
12 &= 2^2 \cdot 3^1 \\
18 &= 2^1 \cdot 3^2 \\
\gcd(12, 18) &= 2^{\min(2,1)} \cdot 3^{\min(1,2)} = 2^1 \cdot 3^1 = 6 \\
\text{lcm}(12, 18) &= 2^{\max(2,1)} \cdot 3^{\max(1,2)} = 2^2 \cdot 3^2 = 36
\end{align}

```math

---

## 🎨 Visual Walkthroughs

### Walkthrough 1: Euclidean Algorithm

```

+-----------------------------------------------------------------+

| PROBLEM: Find gcd(48, 18)                                       |
+-----------------------------------------------------------------+
| STEP-BY-STEP EXECUTION:                                         |
|                                                                  |
| Step 1: gcd(48, 18)                                             |
|   48 = 2 × 18 + 12                                              |
|   → gcd(48, 18) = gcd(18, 12)                                   |
|                                                                  |
|   Visual:                                                        |
|   48: ████████████████████ (remainder = 12)                     |
|   18: █████████                                                  |
|        █████████                                                 |
|        remainder: ██████                                         |
|                                                                  |
| Step 2: gcd(18, 12)                                             |
|   18 = 1 × 12 + 6                                               |
|   → gcd(18, 12) = gcd(12, 6)                                    |
|                                                                  |
|   Visual:                                                        |
|   18: █████████                                                  |
|   12: ██████                                                     |
|        remainder: ███                                            |
|                                                                  |
| Step 3: gcd(12, 6)                                              |
|   12 = 2 × 6 + 0                                                |
|   → gcd(12, 6) = gcd(6, 0) = 6                                  |
|                                                                  |
|   Visual:                                                        |
|   12: ██████                                                     |
|    6: ███                                                        |
|       ███                                                        |
|       remainder: 0 ✓                                             |
|                                                                  |
| RESULT: gcd(48, 18) = 6                                         |
|                                                                  |
| Verification:                                                    |
|   48 = 6 × 8  ✓                                                 |
|   18 = 6 × 3  ✓                                                 |
|   gcd(8, 3) = 1  ✓ (coprime)                                    |
+-----------------------------------------------------------------+

```

---

### Walkthrough 2: Extended GCD

```
+-----------------------------------------------------------------+

| PROBLEM: Find integers x, y such that 35x + 15y = gcd(35, 15)  |
+-----------------------------------------------------------------+
| FORWARD PHASE (Standard Euclidean):                             |
|                                                                  |
| 35 = 2 × 15 + 5   → gcd(35, 15) = gcd(15, 5)                   |
| 15 = 3 × 5 + 0    → gcd(15, 5) = gcd(5, 0) = 5                 |
|                                                                  |
| So gcd(35, 15) = 5                                              |
+-----------------------------------------------------------------+

| BACKWARD PHASE (Finding coefficients):                          |
|                                                                  |
| Base: 5 = 1 × 5 + 0 × 0   (x₀ = 1, y₀ = 0)                     |
|                                                                  |
| Step 1: Express 5 in terms of 15 and 5                          |
|   5 = 15 - 3 × 5                                                |
|   5 = 1 × 15 + (-3) × 5                                         |
|                                                                  |
| Step 2: Express 5 in terms of 35 and 15                         |
|   From earlier: 5 = 35 - 2 × 15                                 |
|   Substitute into equation from Step 1:                         |
|   5 = 1 × 15 + (-3) × (35 - 2 × 15)                             |
|   5 = 1 × 15 + (-3) × 35 + 6 × 15                               |
|   5 = (-3) × 35 + 7 × 15                                        |
|                                                                  |
| RESULT: x = -3, y = 7                                           |
|                                                                  |
| Verification:                                                    |
|   35 × (-3) + 15 × 7 = -105 + 105 = 0  ✗                       |
|   Wait, let me recalculate...                                   |
|                                                                  |
|   From 35 = 2 × 15 + 5:                                         |
|   5 = 35 - 2 × 15                                               |
|   5 = 1 × 35 + (-2) × 15                                        |
|                                                                  |
| CORRECT RESULT: x = 1, y = -2                                   |
|                                                                  |
| Verification:                                                    |
|   35 × 1 + 15 × (-2) = 35 - 30 = 5  ✓                          |
+-----------------------------------------------------------------+

```

---

## 💻 Core Implementations

### Implementation 1: Basic Euclidean Algorithm

```python
def gcd(a: int, b: int) -> int:
    """
    Compute GCD using Euclidean algorithm (iterative).
    
    Time: O(log min(a, b))
    Space: O(1)
    
    Example:
        gcd(48, 18) = 6
        gcd(7, 11) = 1
    """
    while b:
        a, b = b, a % b
    return a

def gcd_recursive(a: int, b: int) -> int:
    """
    Recursive implementation.
    
    Time: O(log min(a, b))
    Space: O(log min(a, b)) for call stack
    """
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

```

---

### Implementation 2: Extended Euclidean Algorithm

```python
def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclidean algorithm.
    
    Returns: (gcd, x, y) where a·x + b·y = gcd(a, b)
    
    Time: O(log min(a, b))
    Space: O(log min(a, b))
    
    Example:
        extended_gcd(35, 15) = (5, 1, -2)
        Verify: 35·1 + 15·(-2) = 35 - 30 = 5 ✓
    """
    if b == 0:
        return a, 1, 0
    
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd_val, x, y

def extended_gcd_iterative(a: int, b: int) -> tuple[int, int, int]:
    """
    Iterative version of extended GCD.
    
    More efficient (no recursion overhead).
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    return old_r, old_s, old_t

```

---

### Implementation 3: LCM Computation

```python
def lcm(a: int, b: int) -> int:
    """
    Compute LCM using GCD.
    
    Formula: lcm(a, b) = (a × b) / gcd(a, b)
    
    Time: O(log min(a, b))
    Space: O(1)
    
    Example:
        lcm(12, 18) = 36
        lcm(4, 6) = 12
    """
    return (a * b) // gcd(a, b)

def lcm_safe(a: int, b: int) -> int:
    """
    Overflow-safe version: divide before multiply.
    """
    return a // gcd(a, b) * b

```

---

### Implementation 4: GCD/LCM of Arrays

```python
from functools import reduce
from typing import List

def gcd_array(arr: List[int]) -> int:
    """
    Compute GCD of an array.
    
    Property: GCD is associative, so order doesn't matter.
    
    Time: O(n log(max element))
    Space: O(1)
    
    Example:
        gcd_array([12, 18, 24, 30]) = 6
    """
    return reduce(gcd, arr)

def lcm_array(arr: List[int]) -> int:
    """
    Compute LCM of an array.
    
    Example:
        lcm_array([4, 6, 8]) = 24
    """
    return reduce(lcm, arr)

```

---

### Implementation 5: Binary GCD (Stein's Algorithm)

```python
def binary_gcd(a: int, b: int) -> int:
    """
    Binary GCD algorithm using bitwise operations.
    
    Often faster than Euclidean on modern hardware.
    
    Algorithm:
    1. Find common power of 2
    2. Remove all factors of 2 from both numbers
    3. Subtract smaller from larger (preserves GCD)
    4. Multiply result by common power of 2
    
    Time: O(log min(a, b))
    Space: O(1)
    """
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Find common power of 2
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1
    
    # Remove remaining factors of 2 from a
    while (a & 1) == 0:
        a >>= 1
    
    while b != 0:
        # Remove factors of 2 from b
        while (b & 1) == 0:
            b >>= 1
        
        # Ensure a ≤ b
        if a > b:
            a, b = b, a
        
        b -= a
    
    return a << shift

```

---

## 🏆 LeetCode Problems

### 🟢 Easy (Foundation)

| # | Problem | Concept | Time |
|:-:|---------|---------|------|
| 1979 | [Find GCD of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | Basic GCD | O(n log m) |
| 1071 | [GCD of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | String GCD | O(n + m) |
| 914 | [X of a Kind in Deck](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/) | GCD application | O(n log m) |
| 2344 | [Minimum Operations to Make Array Equal II](https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/) | GCD check | O(n) |

### 🟡 Medium (Core Skills)

| # | Problem | Concept | Time |
|:-:|---------|---------|------|
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | LCM pattern | O(n) |
| 1201 | [Ugly Number III](https://leetcode.com/problems/ugly-number-iii/) | LCM + inclusion-exclusion | O(log n) |
| 878 | [Nth Magical Number](https://leetcode.com/problems/nth-magical-number/) | LCM + binary search | O(log²n) |
| 1015 | [Smallest Integer Divisible by K](https://leetcode.com/problems/smallest-integer-divisible-by-k/) | GCD/modular | O(K) |
| 2183 | [Count Array Pairs Divisible by K](https://leetcode.com/problems/count-array-pairs-divisible-by-k/) | GCD factorization | O(n√K) |
| 858 | [Mirror Reflection](https://leetcode.com/problems/mirror-reflection/) | GCD/LCM geometry | O(log n) |
| 592 | [Fraction Addition and Subtraction](https://leetcode.com/problems/fraction-addition-and-subtraction/) | LCM of denominators | O(n) |

### 🔴 Hard (Advanced)

| # | Problem | Concept | Time |
|:-:|---------|---------|------|
| 1842 | [Next Palindrome Using Same Digits](https://leetcode.com/problems/next-palindrome-using-same-digits/) | Complex logic | O(n) |
| 149 | [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | GCD for slope | O(n²) |
| 2543 | [Check if Point Is Reachable](https://leetcode.com/problems/check-if-point-is-reachable/) | GCD property | O(log n) |

---

## 🎓 Common Patterns & Applications

### Pattern 1: Simplify Fractions

```python
def simplify_fraction(num: int, den: int) -> tuple[int, int]:
    """
    Reduce fraction to lowest terms.
    
    Example: 12/18 → 2/3
    """
    g = gcd(num, den)
    return num // g, den // g

```

### Pattern 2: Modular Inverse

```python
def mod_inverse(a: int, m: int) -> int:
    """
    Find modular inverse of a modulo m.
    
    Returns x where (a · x) ≡ 1 (mod m)
    
    Exists only if gcd(a, m) = 1
    """
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None  # No inverse exists
    return x % m

```

### Pattern 3: Linear Diophantine Equations

```python
def solve_diophantine(a: int, b: int, c: int) -> tuple[int, int] | None:
    """
    Solve ax + by = c for integers x, y.
    
    Solution exists iff gcd(a, b) divides c.
    
    Returns one solution (x₀, y₀).
    General solution: x = x₀ + k(b/g), y = y₀ - k(a/g)
    """
    g, x0, y0 = extended_gcd(a, b)
    
    if c % g != 0:
        return None  # No solution
    
    # Scale solution
    scale = c // g
    return x0 * scale, y0 * scale

```

### Pattern 4: Coprimality Check

```python
def are_coprime(a: int, b: int) -> bool:
    """
    Check if two numbers are coprime (gcd = 1).
    """
    return gcd(a, b) == 1

def count_coprime_pairs(nums: List[int]) -> int:
    """
    Count pairs (i, j) where i < j and gcd(nums[i], nums[j]) = 1.
    """
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if are_coprime(nums[i], nums[j]):
                count += 1
    return count

```

### Pattern 5: LCM of Multiple Numbers

```python
def lcm_multiple(numbers: List[int]) -> int:
    """
    Compute LCM of multiple numbers.
    
    Use associativity: lcm(a, b, c) = lcm(lcm(a, b), c)
    """
    from functools import reduce
    return reduce(lambda x, y: x * y // gcd(x, y), numbers)

```

---

## 💡 Key Insights

> **Why Euclidean Algorithm is Fast:**  
> Each step reduces the problem size by at least half every 2 iterations. Worst case is consecutive Fibonacci numbers: gcd(F_{n+1}, F_n) takes n steps.

> **Extended GCD Applications:**  
> - **Modular Inverse:** $a \cdot x \equiv 1 \pmod{m}$ when $\gcd(a, m) = 1$
> - **Linear Congruences:** Solve $ax \equiv b \pmod{m}$
> - **Chinese Remainder Theorem:** Combine modular equations

> **GCD-LCM Relationship:**  
> $\gcd(a, b) \times \text{lcm}(a, b) = a \times b$

> **Optimization Tips:**  
> - Use $\text{lcm}(a, b) = a / \gcd(a,b) \times b$ to avoid overflow
> - Binary GCD is faster on some hardware (no division)
> - Python 3.9+: Use `math.gcd()` and `math.lcm()`

---

## 📚 References

| Resource | Link |
|----------|------|
| **CP-Algorithms** | [Euclidean Algorithm](https://cp-algorithms.com/algebra/euclid-algorithm.html) |
| **Brilliant** | [GCD & LCM](https://brilliant.org/wiki/greatest-common-divisor/) |
| **Khan Academy** | [Number Theory](https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples) |
| **CLRS** | Introduction to Algorithms (Chapter 31) |
| **Concrete Mathematics** | Knuth, Graham, Patashnik (Chapter 4) |

---

## 💭 Common Interview Questions

**Q: What's the time complexity of Euclidean algorithm?**  
A: O(log min(a, b)). Proven by Lamé's theorem - related to Fibonacci sequence.

**Q: How to find modular inverse?**  
A: Use extended GCD to find x where ax + my = 1, then x mod m is the inverse.

**Q: When does modular inverse exist?**  
A: Only when gcd(a, m) = 1 (a and m are coprime).

**Q: How to avoid overflow in LCM?**  
A: Use lcm(a, b) = a / gcd(a, b) × b instead of a × b / gcd(a, b).

**Q: What's Binary GCD?**  
A: Stein's algorithm using only subtraction and bit shifts, often faster than Euclidean.

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [🏠 Number Theory Home](../README.md) | **01. GCD & LCM** | [02. Primes →](../02_primes/README.md) |

```