---
layout: default
title: "Prime Numbers"
parent: "Number Theory"
nav_order: 2
has_children: true
permalink: /31_number_theory/02_primes/
---

<div align="center">

# 🔍 Prime Numbers

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-35+-blue?style=for-the-badge" alt="Problems">
</p>

**The Atoms of Mathematics**

*Master primality testing, sieve algorithms, and factorization techniques*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. GCD & LCM](../01_gcd_lcm/README.md) | **02. Primes** | [03. Modular Arithmetic →](../03_modular_arithmetic/README.md) |

---

## 📂 Subtopics

<table>
<tr>
<td width="33%">

### [01. Primality Testing](./01_primality_testing/)
- Trial division O(√n)
- Optimized 6k±1 check
- Miller-Rabin test
- Fermat primality test
- Deterministic witnesses

</td>
<td width="33%">

### [02. Sieve of Eratosthenes](./02_sieve_eratosthenes/)
- Basic sieve O(n log log n)
- Space optimization
- Linear sieve O(n)
- Bitset implementation
- SPF computation

</td>
<td width="33%">

### [03. Prime Factorization](./03_prime_factorization/)
- Trial division method
- Using SPF for O(log n)
- Divisor counting
- Divisor sum formula
- Applications

</td>
</tr>
<tr>
<td width="33%">

### [04. Segmented Sieve](./04_segmented_sieve/)
- Primes in range [L, R]
- Memory efficient
- Block-based sieve
- Prime counting π(n)
- Large range handling

</td>
<td width="33%">

### [05. Prime Applications](./05_prime_applications/)
- Ugly numbers
- Prime gaps & twins
- Goldbach conjecture
- Sophie Germain primes
- Sum of primes

</td>
<td width="33%">

### [06. Applications](./06_applications/)
- LeetCode problems
- Multiplicative functions
- Euler's totient sieve
- Möbius function
- Competition patterns

</td>
</tr>
</table>

---

## 📐 Mathematical Foundations

### 1️⃣ Prime Definition

**Definition:** A prime number $p > 1$ is an integer with exactly two positive divisors: 1 and $p$.

**First 25 Primes:**
```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
53, 59, 61, 67, 71, 73, 79, 83, 89, 97
```

**Key Properties:**
- **Only even prime:** 2
- **Infinite count:** Euclid's proof (~300 BC)
- **Density:** $\pi(n) \approx \frac{n}{\ln n}$ (Prime Number Theorem)
- **Coprime:** $\gcd(p, q) = 1$ for distinct primes

---

### 2️⃣ Fundamental Theorem of Arithmetic

**Theorem:** Every integer $n > 1$ can be expressed **uniquely** as:

$$n = p_1^{a_1} \times p_2^{a_2} \times \cdots \times p_k^{a_k}$$

where $p_1 < p_2 < \cdots < p_k$ are primes and $a_i \geq 1$.

**Example:**
$$\begin{align}
360 &= 2^3 \times 3^2 \times 5^1 \\
&= 8 \times 9 \times 5 = 360
\end{align}$$

**Applications:**
- **Count divisors:** $\tau(n) = (a_1+1)(a_2+1)\cdots(a_k+1)$
- **Sum of divisors:** $\sigma(n) = \prod \frac{p_i^{a_i+1} - 1}{p_i - 1}$
- **Euler's totient:** $\phi(n) = n \prod \left(1 - \frac{1}{p_i}\right)$

---

### 3️⃣ Prime Number Theorem

**Statement:** The prime counting function satisfies:

$$\pi(n) \sim \frac{n}{\ln n}$$

**Precise Version:**

$$\lim_{n \to \infty} \frac{\pi(n) \cdot \ln n}{n} = 1$$

**Practical Approximations:**

| $n$ | $\pi(n)$ | $n/\ln n$ | Ratio |
|-----|----------|-----------|-------|
| $10^3$ | 168 | 145 | 1.16 |
| $10^6$ | 78,498 | 72,382 | 1.08 |
| $10^9$ | 50,847,534 | 48,254,942 | 1.05 |

---

### 4️⃣ Primality Testing Overview

| Method | Time Complexity | Deterministic? | Best For |
|--------|----------------|----------------|----------|
| **Trial Division** | $O(\sqrt{n})$ | ✅ Yes | Small $n$ |
| **Optimized Trial** | $O(\sqrt{n}/3)$ | ✅ Yes | Small $n$ |
| **Fermat Test** | $O(k \log n)$ | ❌ No | Quick check |
| **Miller-Rabin** | $O(k \log^3 n)$ | ❌/✅ | Large $n$ |
| **AKS** | $O(\log^6 n)$ | ✅ Yes | Theoretical |

---

## 🎨 Visual Walkthroughs

### Walkthrough 1: Sieve of Eratosthenes

```
┌─────────────────────────────────────────────────────────────────┐
│ PROBLEM: Find all primes up to 30                              │
├─────────────────────────────────────────────────────────────────┤
│ INITIAL STATE (all marked as potential primes):                │
│                                                                 │
│    2  3  4  5  6  7  8  9 10 11 12 13 14 15                   │
│   16 17 18 19 20 21 22 23 24 25 26 27 28 29 30                │
│                                                                 │
│ STEP 1: Process p = 2 (mark multiples starting from 2² = 4)   │
│                                                                 │
│    2  3  ×  5  ×  7  ×  9  × 11  × 13  × 15                   │
│    × 17  × 19  × 21  × 23  × 25  × 27  × 29  ×                │
│                                                                 │
│ STEP 2: Process p = 3 (mark multiples starting from 3² = 9)   │
│                                                                 │
│    2  3  ×  5  ×  7  ×  ×  × 11  × 13  ×  ×                   │
│    × 17  × 19  ×  ×  × 23  × 25  ×  ×  × 29  ×                │
│                                                                 │
│ STEP 3: Process p = 5 (mark multiples starting from 5² = 25)  │
│                                                                 │
│    2  3  ×  5  ×  7  ×  ×  × 11  × 13  ×  ×                   │
│    × 17  × 19  ×  ×  × 23  ×  ×  ×  ×  × 29  ×                │
│                                                                 │
│ DONE: √30 ≈ 5.5, so we stop at p = 5                          │
│                                                                 │
│ PRIMES: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29                    │
│ COUNT: 10 primes up to 30                                      │
└─────────────────────────────────────────────────────────────────┘
```

---

### Walkthrough 2: Trial Division Primality Test

```
┌─────────────────────────────────────────────────────────────────┐
│ PROBLEM: Is 97 prime?                                          │
├─────────────────────────────────────────────────────────────────┤
│ ALGORITHM: Check divisibility by all integers from 2 to √97    │
│                                                                 │
│ √97 ≈ 9.85, so check divisors up to 9                         │
│                                                                 │
│ Check d = 2:  97 % 2 = 1  ✗ (not divisible)                   │
│ Check d = 3:  97 % 3 = 1  ✗ (not divisible)                   │
│ Check d = 4:  Skip (composite, covered by 2)                   │
│ Check d = 5:  97 % 5 = 2  ✗ (not divisible)                   │
│ Check d = 6:  Skip (composite, covered by 2,3)                 │
│ Check d = 7:  97 % 7 = 6  ✗ (not divisible)                   │
│ Check d = 8:  Skip (composite, covered by 2)                   │
│ Check d = 9:  97 % 9 = 7  ✗ (not divisible)                   │
│                                                                 │
│ OPTIMIZATION: Only check 2, 3, then 6k±1 pattern              │
│                                                                 │
│ Check: 2, 3, 5, 7 (all primes up to √97)                      │
│                                                                 │
│ RESULT: 97 is PRIME ✓                                          │
└─────────────────────────────────────────────────────────────────┘
```

---

### Walkthrough 3: Prime Factorization

```
┌─────────────────────────────────────────────────────────────────┐
│ PROBLEM: Factorize 360                                         │
├─────────────────────────────────────────────────────────────────┤
│ STEP-BY-STEP:                                                   │
│                                                                 │
│ Start: n = 360                                                  │
│                                                                 │
│ ┌─────────────────────────────────────────────────────────┐    │
│ │ d = 2: 360 ÷ 2 = 180  (360 = 2 × 180)                  │    │
│ │ d = 2: 180 ÷ 2 = 90   (360 = 2² × 90)                  │    │
│ │ d = 2: 90 ÷ 2 = 45    (360 = 2³ × 45)                  │    │
│ │ d = 2: 45 % 2 ≠ 0     → move to next divisor           │    │
│ └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│ ┌─────────────────────────────────────────────────────────┐    │
│ │ d = 3: 45 ÷ 3 = 15    (360 = 2³ × 3 × 15)              │    │
│ │ d = 3: 15 ÷ 3 = 5     (360 = 2³ × 3² × 5)              │    │
│ │ d = 3: 5 % 3 ≠ 0      → move to next divisor           │    │
│ └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│ ┌─────────────────────────────────────────────────────────┐    │
│ │ d = 4: Skip (4² > 5)                                   │    │
│ │ Remaining: 5 > 1      → 5 is prime factor              │    │
│ └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│ RESULT: 360 = 2³ × 3² × 5¹                                     │
│                                                                 │
│ VERIFICATION:                                                   │
│   8 × 9 × 5 = 72 × 5 = 360 ✓                                  │
│                                                                 │
│ DIVISOR COUNT:                                                  │
│   τ(360) = (3+1)(2+1)(1+1) = 4 × 3 × 2 = 24 divisors          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Core Implementations

### Implementation 1: Primality Test (Trial Division)

```python
def is_prime(n: int) -> bool:
    """
    Check if n is prime using trial division.
    
    Time: O(√n)
    Space: O(1)
    
    Examples:
        >>> is_prime(17)
        True
        >>> is_prime(100)
        False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to √n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True
```

---

### Implementation 2: Optimized Primality (6k±1)

```python
def is_prime_optimized(n: int) -> bool:
    """
    Optimized primality test using 6k±1 property.
    
    All primes > 3 are of form 6k±1.
    
    Time: O(√n / 3) in best case
    Space: O(1)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check numbers of form 6k±1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True
```

---

### Implementation 3: Sieve of Eratosthenes

```python
def sieve_of_eratosthenes(n: int) -> list[int]:
    """
    Generate all primes up to n.
    
    Time: O(n log log n)
    Space: O(n)
    
    Examples:
        >>> sieve_of_eratosthenes(30)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples starting from i²
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]
```

---

### Implementation 4: Linear Sieve with SPF

```python
def linear_sieve(n: int) -> tuple[list[int], list[int]]:
    """
    Linear time sieve with smallest prime factor.
    
    Time: O(n)
    Space: O(n)
    
    Returns: (primes, spf) where spf[i] = smallest prime factor of i
    """
    spf = [0] * (n + 1)  # Smallest prime factor
    primes = []
    
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        
        for p in primes:
            if p * i > n:
                break
            spf[p * i] = p
            if i % p == 0:
                break  # Key optimization
    
    return primes, spf


def factorize_with_spf(n: int, spf: list[int]) -> dict[int, int]:
    """
    Factorize n using precomputed SPF in O(log n).
    """
    factors = {}
    while n > 1:
        p = spf[n]
        factors[p] = factors.get(p, 0) + 1
        n //= p
    return factors
```

---

### Implementation 5: Miller-Rabin Primality Test

```python
import random

def miller_rabin(n: int, k: int = 10) -> bool:
    """
    Miller-Rabin probabilistic primality test.
    
    Time: O(k log³ n)
    Space: O(1)
    Error probability: < 4^(-k)
    
    Args:
        n: Number to test
        k: Number of rounds (higher = more accurate)
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r × d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True
```

---

### Implementation 6: Prime Factorization

```python
def prime_factorize(n: int) -> dict[int, int]:
    """
    Find prime factorization of n.
    
    Time: O(√n)
    Space: O(log n)
    
    Returns: dict {prime: exponent}
    
    Example:
        >>> prime_factorize(360)
        {2: 3, 3: 2, 5: 1}
    """
    factors = {}
    
    # Check for 2
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    
    # Check odd factors
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 2
    
    # Remaining prime factor
    if n > 1:
        factors[n] = 1
    
    return factors
```

---

### Implementation 7: Segmented Sieve

```python
def segmented_sieve(L: int, R: int) -> list[int]:
    """
    Find all primes in range [L, R].
    
    Time: O((R-L) log log R + √R)
    Space: O(√R + (R-L))
    
    Efficient for large ranges where R >> L.
    """
    # Generate small primes up to √R
    limit = int(R**0.5) + 1
    is_prime_small = [True] * (limit + 1)
    is_prime_small[0] = is_prime_small[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime_small[i]:
            for j in range(i*i, limit + 1, i):
                is_prime_small[j] = False
    
    small_primes = [i for i in range(2, limit + 1) if is_prime_small[i]]
    
    # Sieve the range [L, R]
    size = R - L + 1
    is_prime = [True] * size
    
    # Handle 0 and 1
    if L <= 1:
        for i in range(max(0, 1 - L + 1)):
            if L + i <= 1:
                is_prime[i] = False
    
    for p in small_primes:
        # First multiple of p >= L
        start = max(p * p, ((L + p - 1) // p) * p)
        for j in range(start, R + 1, p):
            is_prime[j - L] = False
    
    return [L + i for i in range(size) if is_prime[i] and L + i >= 2]
```

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Key Concept | Time |
|:-:|---------|-------------|------|
| 204 | [Count Primes](https://leetcode.com/problems/count-primes/) | Sieve of Eratosthenes | O(n log log n) |
| 263 | [Ugly Number](https://leetcode.com/problems/ugly-number/) | Prime factor check | O(log n) |
| 762 | [Prime Number of Set Bits](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) | Precompute small primes | O(n) |
| 2614 | [Prime In Diagonal](https://leetcode.com/problems/prime-in-diagonal/) | Primality test | O(n√m) |

### 🟡 Medium

| # | Problem | Key Concept | Time |
|:-:|---------|-------------|------|
| 264 | [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) | Generate sequence | O(n) |
| 313 | [Super Ugly Number](https://leetcode.com/problems/super-ugly-number/) | Multiple primes + heap | O(nk) |
| 866 | [Prime Palindrome](https://leetcode.com/problems/prime-palindrome/) | Generate + test | O(n^0.5 log n) |
| 1390 | [Four Divisors](https://leetcode.com/problems/four-divisors/) | Divisor counting | O(n√m) |
| 2523 | [Closest Prime Numbers in Range](https://leetcode.com/problems/closest-prime-numbers-in-range/) | Segmented sieve | O((R-L) log log R) |
| 2601 | [Prime Subtraction Operation](https://leetcode.com/problems/prime-subtraction-operation/) | Precompute primes | O(n log m) |
| 2761 | [Prime Pairs With Target Sum](https://leetcode.com/problems/prime-pairs-with-target-sum/) | Sieve + two-sum | O(n log log n) |

### 🔴 Hard

| # | Problem | Key Concept | Time |
|:-:|---------|-------------|------|
| 952 | [Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/) | Union-Find + factorization | O(n√m) |
| 483 | [Smallest Good Base](https://leetcode.com/problems/smallest-good-base/) | Prime representation | O(log²n) |

---

## 🎓 Common Patterns & Applications

### Pattern 1: Count Primes (LeetCode 204)

```python
def count_primes(n: int) -> int:
    """Count primes less than n."""
    if n <= 2:
        return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    
    return sum(is_prime)
```

### Pattern 2: Divisor Count from Factorization

```python
def count_divisors(n: int) -> int:
    """
    Count divisors using τ(n) = ∏(aᵢ + 1).
    
    Time: O(√n)
    """
    if n == 1:
        return 1
    
    count = 1
    d = 2
    
    while d * d <= n:
        exp = 0
        while n % d == 0:
            exp += 1
            n //= d
        count *= (exp + 1)
        d += 1
    
    if n > 1:
        count *= 2  # Remaining prime factor
    
    return count
```

### Pattern 3: Euler's Totient Sieve

```python
def euler_phi_sieve(n: int) -> list[int]:
    """
    Compute φ(i) for all i from 1 to n.
    
    Time: O(n log log n)
    Space: O(n)
    """
    phi = list(range(n + 1))
    
    for i in range(2, n + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    
    return phi
```

### Pattern 4: Goldbach Partition

```python
def goldbach_partition(n: int) -> tuple[int, int] | None:
    """
    Express even n as sum of two primes.
    """
    if n <= 2 or n % 2 == 1:
        return None
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    for p in range(2, n // 2 + 1):
        if is_prime[p] and is_prime[n - p]:
            return (p, n - p)
    
    return None
```

---

## 💡 Key Insights

> **Why √n is Sufficient:**  
> If $n = a \times b$ and $a, b > \sqrt{n}$, then $a \times b > n$. Contradiction!  
> So every composite $n$ has a factor $\leq \sqrt{n}$.

> **Sieve Optimization:**  
> Start marking from $p^2$ because smaller multiples $2p, 3p, \ldots, (p-1)p$ were already marked by smaller primes.

> **Linear Sieve Key:**  
> Each composite is marked exactly once by its smallest prime factor, achieving O(n) time.

> **Miller-Rabin Accuracy:**  
> With k rounds, error probability is $< 4^{-k}$. With k=10, this is $< 10^{-6}$.

> **Carmichael Numbers:**  
> Composites that pass Fermat test for all coprime bases (e.g., 561, 1105, 1729).  
> Miller-Rabin detects these correctly!

---

## 📚 References

| Resource | Link |
|----------|------|
| **CP-Algorithms** | [Primality Tests](https://cp-algorithms.com/algebra/primality_tests.html) |
| **CP-Algorithms** | [Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html) |
| **Wikipedia** | [Prime Number Theorem](https://en.wikipedia.org/wiki/Prime_number_theorem) |
| **OEIS** | [Prime Numbers A000040](https://oeis.org/A000040) |
| **Project Euler** | [Prime-Related Problems](https://projecteuler.net/) |

---

## 💭 Common Interview Questions

**Q: Why is Sieve O(n log log n)?**  
A: The sum $\sum_{p \leq n} n/p$ over primes equals $n \cdot \sum 1/p \approx n \ln \ln n$.

**Q: When to use segmented sieve?**  
A: When R is very large (10⁹+) but R-L is manageable (≤10⁶). Uses only O(√R + (R-L)) space.

**Q: What's the advantage of linear sieve?**  
A: O(n) time instead of O(n log log n), and also computes smallest prime factor for O(log n) factorization.

**Q: How does Miller-Rabin detect Carmichael numbers?**  
A: It checks a stronger condition: if $n$ is prime and $n-1 = 2^r \cdot d$, then for witness $a$, either $a^d \equiv 1$ or $a^{2^j d} \equiv -1$ for some $j$.

**Q: What's the largest prime gap for n ≤ 10⁹?**  
A: The maximum gap is 282 (between 436273009 and 436273291). Average gap is about $\ln n \approx 21$.

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. GCD & LCM](../01_gcd_lcm/README.md) | **02. Primes** | [03. Modular Arithmetic →](../03_modular_arithmetic/README.md) |
