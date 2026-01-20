---
layout: default
title: "Prime Problem Applications"
parent: "Prime Numbers"
grand_parent: "Number Theory"
nav_order: 6
permalink: /30_number_theory/02_primes/06_applications/
---

<div align="center">

# 🏆 Prime Problem Applications

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-20+-blue?style=for-the-badge" alt="Problems">
</p>

**Advanced Prime Problems & Competition Patterns**

*LeetCode solutions, multiplicative functions, and more*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 05. Prime Applications](../05_prime_applications/README.md) | **06. Applications** | [🏠 Primes Home](../README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Multiplicative Functions

A function $f: \mathbb{Z}^+ \to \mathbb{C}$ is **multiplicative** if:

```math
f(mn) = f(m) \cdot f(n) \quad \text{when } \gcd(m, n) = 1

```

**Important Multiplicative Functions:**

| Function | Definition | Formula |
|----------|------------|---------|
| $\tau(n)$ | Divisor count | $\prod(a_i + 1)$ |
| $\sigma(n)$ | Divisor sum | $\prod\frac{p_i^{a_i+1}-1}{p_i-1}$ |
| $\phi(n)$ | Euler's totient | $n\prod(1-\frac{1}{p_i})$ |
| $\mu(n)$ | Möbius function | $(-1)^k$ or 0 |

---

### 2️⃣ Möbius Function

**Definition:**

```math
\mu(n) = \begin{cases}
1 & \text{if } n = 1 \\
(-1)^k & \text{if } n \text{ is product of } k \text{ distinct primes} \\
0 & \text{if } n \text{ has squared prime factor}
\end{cases}

```

**Key Property (Möbius Inversion):**
If $g(n) = \sum_{d|n} f(d)$, then $f(n) = \sum_{d|n} \mu(d) \cdot g(n/d)$

---

### 3️⃣ Euler's Totient Properties

**Formula:** $\phi(n) = n \prod_{p|n} \left(1 - \frac{1}{p}\right)$

**Properties:**

- $\phi(p) = p - 1$ for prime $p$

- $\phi(p^k) = p^{k-1}(p-1)$

- $\sum_{d|n} \phi(d) = n$

- $a^{\phi(n)} \equiv 1 \pmod{n}$ if $\gcd(a,n) = 1$ (Euler's theorem)

---

## 📊 Visual Diagram

<div align="center">

![Miller-Rabin Primality Test](./images/miller_rabin.svg)

</div>

---

## 🎨 Visual Walkthroughs

### Walkthrough 1: Euler's Totient Sieve

```
+-----------------------------------------------------------------+
| COMPUTE φ(n) FOR ALL n UP TO 12                                |
+-----------------------------------------------------------------+
| INITIAL: φ[i] = i for all i                                    |
|                                                                 |
|   n:    1  2  3  4  5  6  7  8  9 10 11 12                    |
|   φ:    1  2  3  4  5  6  7  8  9 10 11 12                    |
|                                                                 |
| STEP 1: p = 2 (prime), update multiples                        |
|   For j = 2, 4, 6, 8, 10, 12:                                  |
|   φ[j] = φ[j] - φ[j]/2 = φ[j] × (1 - 1/2) = φ[j]/2           |
|                                                                 |
|   n:    1  2  3  4  5  6  7  8  9 10 11 12                    |
|   φ:    1  1  3  2  5  3  7  4  9  5 11  6                    |
|                                                                 |
| STEP 2: p = 3 (prime), update multiples                        |
|   For j = 3, 6, 9, 12:                                         |
|   φ[j] = φ[j] - φ[j]/3 = φ[j] × (1 - 1/3) = φ[j] × 2/3       |
|                                                                 |
|   n:    1  2  3  4  5  6  7  8  9 10 11 12                    |
|   φ:    1  1  2  2  5  2  7  4  6  5 11  4                    |
|                                                                 |
| STEP 3: p = 5 (prime), update multiples                        |
|   For j = 5, 10:                                               |
|   φ[j] = φ[j] × (1 - 1/5) = φ[j] × 4/5                        |
|                                                                 |
|   n:    1  2  3  4  5  6  7  8  9 10 11 12                    |
|   φ:    1  1  2  2  4  2  6  4  6  4 10  4                    |
|                                                                 |
| Continue for 7, 11...                                          |
|                                                                 |
| FINAL:                                                          |
|   φ:    1  1  2  2  4  2  6  4  6  4 10  4                    |
|                                                                 |
| VERIFICATION: φ(12) = 4                                         |
|   Numbers coprime to 12: 1, 5, 7, 11 → count = 4 ✓             |
+-----------------------------------------------------------------+

```

---

### Walkthrough 2: Union-Find with Prime Factorization

```
+-----------------------------------------------------------------+
| LEETCODE 952: Largest Component Size by Common Factor          |
+-----------------------------------------------------------------+
| PROBLEM: Connect numbers sharing a prime factor                |
|                                                                 |
| INPUT: nums = [4, 6, 15, 35]                                   |
|                                                                 |
| STEP 1: Factorize each number                                  |
|   4 = 2²       → primes: {2}                                   |
|   6 = 2 × 3    → primes: {2, 3}                                |
|   15 = 3 × 5   → primes: {3, 5}                                |
|   35 = 5 × 7   → primes: {5, 7}                                |
|                                                                 |
| STEP 2: Union numbers sharing primes                           |
|                                                                 |
|   4 and 6 share prime 2 → UNION(4, 6)                          |
|   6 and 15 share prime 3 → UNION(6, 15)                        |
|   15 and 35 share prime 5 → UNION(15, 35)                      |
|                                                                 |
|   Connections:                                                  |
|     4 --- 6 --- 15 --- 35                                      |
|      (2)   (3)    (5)                                          |
|                                                                 |
| STEP 3: Find largest component                                 |
|   All 4 numbers are connected!                                 |
|   Component size = 4                                           |
|                                                                 |
| RESULT: 4                                                       |
+-----------------------------------------------------------------+

```

---

## 💻 Code Implementations

### Implementation 1: Euler's Totient Sieve

```python
def euler_phi_sieve(n: int) -> list[int]:
    """
    Compute Euler's totient φ(i) for all i from 1 to n.
    
    Time: O(n log log n)
    Space: O(n)
    
    Examples:
        >>> euler_phi_sieve(12)
        [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4]
    """
    phi = list(range(n + 1))
    
    for i in range(2, n + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    
    return phi

```

---

### Implementation 2: Möbius Function Sieve

```python
def mobius_sieve(n: int) -> list[int]:
    """
    Compute Möbius function μ(i) for all i from 1 to n.
    
    μ(n) = 0 if n has squared prime factor
    μ(n) = (-1)^k if n is product of k distinct primes
    
    Time: O(n log log n)
    Space: O(n)
    
    Examples:
        >>> mobius_sieve(10)
        [0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1]
    """
    mu = [1] * (n + 1)
    mu[0] = 0
    is_prime = [True] * (n + 1)
    
    for i in range(2, n + 1):
        if is_prime[i]:
            # i is prime
            for j in range(i, n + 1, i):
                is_prime[j] = (j == i)
                mu[j] *= -1
            
            # Mark numbers with i² as factor
            for j in range(i * i, n + 1, i * i):
                mu[j] = 0
    
    return mu

```

---

### Implementation 3: LeetCode 952 - Largest Component

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        """
        Connect numbers sharing a prime factor, find largest component.
        
        Time: O(n × √max(nums) × α(n))
        Space: O(max(nums))
        """
        max_val = max(nums)
        uf = UnionFind(max_val + 1)
        
        for num in nums:
            # Factorize and union with each prime factor
            d = 2
            temp = num
            while d * d <= temp:
                if temp % d == 0:
                    uf.union(num, d)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                uf.union(num, temp)
        
        # Count component sizes
        from collections import Counter
        roots = Counter(uf.find(num) for num in nums)
        return max(roots.values())

```

---

### Implementation 4: Divisor Count for Array

```python
def count_divisors_array(nums: list[int]) -> list[int]:
    """
    Count divisors for each number in array.
    
    Uses sieve-like approach for efficiency when max(nums) is bounded.
    
    Time: O(max_val log max_val)
    Space: O(max_val)
    """
    if not nums:
        return []
    
    max_val = max(nums)
    divisor_count = [0] * (max_val + 1)
    
    # For each d, add 1 to all multiples
    for d in range(1, max_val + 1):
        for multiple in range(d, max_val + 1, d):
            divisor_count[multiple] += 1
    
    return [divisor_count[n] for n in nums]

```

---

### Implementation 5: GCD Sum Formula

```python
def gcd_sum(n: int) -> int:
    """
    Compute Σ gcd(i, n) for i = 1 to n.
    
    Formula: Σ d × φ(n/d) for all divisors d of n
    
    Time: O(√n × log n)
    Space: O(1)
    
    Examples:
        >>> gcd_sum(12)
        40
    """
    def euler_phi(x: int) -> int:
        result = x
        p = 2
        while p * p <= x:
            if x % p == 0:
                result -= result // p
                while x % p == 0:
                    x //= p
            p += 1
        if x > 1:
            result -= result // x
        return result
    
    # Find all divisors of n
    divisors = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            divisors.append(d)
            if d * d != n:
                divisors.append(n // d)
        d += 1
    
    # Sum d × φ(n/d)
    return sum(d * euler_phi(n // d) for d in divisors)

```

---

### Implementation 6: k-Almost Primes

```python
def count_k_almost_primes(n: int, k: int) -> int:
    """
    Count k-almost primes up to n.
    
    k-almost prime: exactly k prime factors (with multiplicity)
    1-almost primes = primes
    2-almost primes = semiprimes
    
    Time: O(n log log n)
    Space: O(n)
    
    Examples:
        >>> count_k_almost_primes(100, 1)  # primes
        25
        >>> count_k_almost_primes(100, 2)  # semiprimes
        34
    """
    # Compute SPF
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    
    # Count prime factors for each number
    count = 0
    for i in range(2, n + 1):
        num_factors = 0
        temp = i
        while temp > 1:
            num_factors += 1
            temp //= spf[temp]
        if num_factors == k:
            count += 1
    
    return count

```

---

### Implementation 7: Primorial

```python
def primorial(n: int) -> int:
    """
    Compute primorial: product of all primes ≤ n.
    
    p_n# = 2 × 3 × 5 × 7 × 11 × ...
    
    Time: O(n log log n)
    Space: O(n)
    
    Examples:
        >>> primorial(10)
        210  # 2×3×5×7
        >>> primorial(20)
        9699690
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    result = 1
    for i in range(2, n + 1):
        if is_prime[i]:
            result *= i
    
    return result

```

---

### Implementation 8: Count Numbers with k Distinct Prime Factors

```python
def count_with_k_distinct_primes(n: int, k: int) -> int:
    """
    Count numbers up to n with exactly k distinct prime factors.
    
    Uses ω(n) function.
    
    Time: O(n log log n)
    Space: O(n)
    """
    # omega[i] = number of distinct prime factors of i
    omega = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if omega[i] == 0:  # i is prime
            for j in range(i, n + 1, i):
                omega[j] += 1
    
    return sum(1 for i in range(2, n + 1) if omega[i] == k)

```

---

## 🏆 LeetCode Problems

### 🟡 Medium

| # | Problem | Key Concept | Time |
|:-:|---------|-------------|------|
| 204 | [Count Primes](https://leetcode.com/problems/count-primes/) | Sieve | O(n log log n) |
| 2183 | [Count Pairs Divisible by K](https://leetcode.com/problems/count-array-pairs-divisible-by-k/) | GCD + factorization | O(n√K) |
| 2507 | [Smallest Value After Replacing](https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/) | Prime factorization | O(√n log n) |

### 🔴 Hard

| # | Problem | Key Concept | Time |
|:-:|---------|-------------|------|
| 952 | [Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/) | Union-Find + factorization | O(n√m) |
| 1819 | [Number of Different Subsequences GCDs](https://leetcode.com/problems/number-of-different-subsequences-gcds/) | GCD properties | O(n log n) |

---

## 💻 Competition Problem Patterns

### Pattern 1: Factor-Based Grouping

```python
def group_by_prime_factors(nums: list[int]) -> dict[int, list[int]]:
    """Group numbers by their prime factors using Union-Find."""
    from collections import defaultdict
    
    max_val = max(nums)
    uf = UnionFind(max_val + 1)
    
    for num in nums:
        d = 2
        temp = num
        while d * d <= temp:
            if temp % d == 0:
                uf.union(num, d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            uf.union(num, temp)
    
    groups = defaultdict(list)
    for num in nums:
        groups[uf.find(num)].append(num)
    
    return dict(groups)

```

### Pattern 2: Inclusion-Exclusion with Primes

```python
def count_divisible_by_any(n: int, primes: list[int]) -> int:
    """
    Count numbers from 1 to n divisible by at least one prime in list.
    
    Uses inclusion-exclusion principle.
    """
    total = 0
    
    for mask in range(1, 1 << len(primes)):
        product = 1
        bits = bin(mask).count('1')
        
        for i in range(len(primes)):
            if mask & (1 << i):
                product *= primes[i]
                if product > n:
                    break
        
        if product <= n:
            if bits % 2 == 1:
                total += n // product
            else:
                total -= n // product
    
    return total

```

### Pattern 3: Multiplicative Function Computation

```python
def compute_multiplicative(n: int, prime_val, combine):
    """
    Generic multiplicative function computation.
    
    prime_val(p, e) returns f(p^e) for prime p and exponent e
    combine(a, b) returns f(a*b) for coprime a, b
    """
    result = [1] * (n + 1)
    spf = list(range(n + 1))
    
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    
    for i in range(2, n + 1):
        if spf[i] == i:  # i is prime
            result[i] = prime_val(i, 1)
        else:
            p = spf[i]
            e = 0
            temp = i
            while temp % p == 0:
                e += 1
                temp //= p
            
            result[i] = combine(prime_val(p, e), result[temp])
    
    return result

```

---

## 💡 Key Insights

> **Multiplicative Functions:**  
> Can be computed efficiently using sieve:
> - Compute at primes: f(p)
> - Compute at prime powers: f(p^k)
> - Combine using multiplicativity: f(mn) = f(m)f(n)

> **Union-Find + Factorization:**  
> Powerful pattern for grouping elements by shared prime factors.  
> Used in component problems, graph connectivity.

> **Inclusion-Exclusion:**  
> Count with alternating sum over subsets.  
> Essential for "divisible by at least one of" problems.

> **Möbius Inversion:**  
> If $g(n) = \sum_{d|n} f(d)$, then $f(n) = \sum_{d|n} \mu(d)g(n/d)$  
> Useful for inverting summation relations.

---

## 📊 Function Values Table

| n | τ(n) | σ(n) | φ(n) | μ(n) | ω(n) | Ω(n) |
|---|------|------|------|------|------|------|
| 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 2 | 2 | 3 | 1 | -1 | 1 | 1 |
| 6 | 4 | 12 | 2 | 1 | 2 | 2 |
| 12 | 6 | 28 | 4 | 0 | 2 | 3 |
| 30 | 8 | 72 | 8 | -1 | 3 | 3 |
| 60 | 12 | 168 | 16 | 0 | 3 | 4 |

Where:

- τ = divisor count

- σ = divisor sum  

- φ = Euler's totient

- μ = Möbius function

- ω = distinct prime factors

- Ω = total prime factors (with multiplicity)

---

## 📚 References

| Resource | Link |
|----------|------|
| **CP-Algorithms** | [Multiplicative Functions](https://cp-algorithms.com/algebra/phi-function.html) |
| **Wikipedia** | [Möbius Function](https://en.wikipedia.org/wiki/M%C3%B6bius_function) |
| **OEIS** | [Euler Totient A000010](https://oeis.org/A000010) |
| **OEIS** | [Möbius A008683](https://oeis.org/A008683) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 05. Prime Applications](../05_prime_applications/README.md) | **06. Applications** | [🏠 Primes Home](../README.md) |
