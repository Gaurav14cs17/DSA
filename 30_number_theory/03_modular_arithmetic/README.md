---
layout: default
title: "Modular Arithmetic"
parent: "Number Theory"
nav_order: 3
has_children: true
permalink: /30_number_theory/03_modular_arithmetic/
---

<div align="center">

# 🔄 Modular Arithmetic

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Subtopics-6-blue?style=for-the-badge" alt="Subtopics">
  <img src="https://img.shields.io/badge/Problems-28+-orange?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 02. Primes](../02_primes/README.md) | **03. Modular Arithmetic** | [04. Divisors →](../04_divisors/README.md) |

---

## 📂 Subtopics

<table>
<tr>
<td width="33%">

### [01. Basic Operations](./01_basic_operations/)

- Addition mod m

- Multiplication mod m

- Subtraction mod m

- Properties

- Modular congruence

</td>
<td width="33%">

### [02. Modular Inverse](./02_modular_inverse/)

- Extended GCD method

- Fermat's theorem method

- Euler's theorem method

- Applications

- When inverse exists

</td>
<td width="33%">

### [03. Fast Exponentiation](./03_fast_exponentiation/)

- Binary exponentiation

- Iterative method

- Recursive method

- Matrix exponentiation

- Applications

</td>
</tr>
<tr>
<td width="33%">

### [04. Fermat's Theorem](./04_fermats_theorem/)

- a^(p-1) ≡ 1 (mod p)

- Primality testing

- Computing inverses

- Proof and applications

- Euler's generalization

</td>
<td width="33%">

### [05. Euler's Theorem](./05_eulers_theorem/)

- a^φ(n) ≡ 1 (mod n)

- RSA cryptography

- Totient function

- Applications

- Advanced uses

</td>
<td width="33%">

### [06. Applications](./06_applications/)

- LeetCode problems

- Power computations

- Cryptography basics

- Competitive problems

- Real-world uses

</td>
</tr>
</table>

---

## 📋 Overview

**Modular arithmetic** is arithmetic for integers where numbers "wrap around" upon reaching a certain value (the modulus). It's fundamental to cryptography, hashing, and countless algorithmic problems.

**Core Concepts:**
- **Congruence:** a ≡ b (mod m) means m | (a - b)

- **Clock Arithmetic:** Like hours on a clock (mod 12 or 24)

- **Fast Operations:** Exponentiation in O(log n) time

- **Modular Inverse:** Division in modular systems

- **Applications:** RSA, hashing, competitive programming

**Why This Matters:**
- **Cryptography:** RSA encryption relies on modular arithmetic

- **Large Numbers:** Keep calculations manageable (mod 10⁹+7)

- **Cyclic Patterns:** Model repeating phenomena

- **Efficiency:** Fast exponentiation beats naive methods

- **Ubiquitous:** Appears in 30%+ of competitive problems

---

## 📐 Mathematical Foundation

### 1️⃣ Modular Congruence

**Definition:** a ≡ b (mod m) if m divides (a - b)

**Equivalently:**

```
a ≡ b (mod m) ⟺ a mod m = b mod m
                ⟺ a = b + km for some integer k

```

**Examples:**

```
17 ≡ 5 (mod 12)  because 17 - 5 = 12
-3 ≡ 7 (mod 10)  because -3 - 7 = -10
100 ≡ 0 (mod 10) because 100 - 0 = 100

```

**Properties:**
1. **Reflexive:** a ≡ a (mod m)
2. **Symmetric:** a ≡ b ⟹ b ≡ a (mod m)
3. **Transitive:** a ≡ b and b ≡ c ⟹ a ≡ c (mod m)

### 2️⃣ Modular Operations

**Addition:**

```
(a + b) mod m = ((a mod m) + (b mod m)) mod m

```

**Multiplication:**

```
(a × b) mod m = ((a mod m) × (b mod m)) mod m

```

**Subtraction:**

```
(a - b) mod m = ((a mod m) - (b mod m) + m) mod m

```

**Exponentiation:**

```
a^n mod m = ((a mod m)^n) mod m

```

**Division (Special):**

```
(a / b) mod m = (a × b^(-1)) mod m
where b^(-1) is modular inverse of b

```

### 3️⃣ Modular Inverse

**Definition:** The modular inverse of a modulo m is an integer x such that:

```
a × x ≡ 1 (mod m)

```

**Notation:** x = a^(-1) (mod m)

**Existence:** Inverse exists ⟺ gcd(a, m) = 1 (a and m are coprime)

**Methods to Find:**
1. **Extended GCD:** ax + my = 1, x is the inverse
2. **Fermat's Theorem:** If m is prime, a^(-1) ≡ a^(m-2) (mod m)
3. **Euler's Theorem:** a^(-1) ≡ a^(φ(m)-1) (mod m)

### 4️⃣ Important Theorems

**Fermat's Little Theorem:**
If p is prime and gcd(a, p) = 1:

```
a^(p-1) ≡ 1 (mod p)

```

**Corollary:** a^p ≡ a (mod p) for all a

**Euler's Theorem (Generalization):**
If gcd(a, n) = 1:

```
a^φ(n) ≡ 1 (mod n)

```

Where φ(n) is Euler's totient function

**Chinese Remainder Theorem:**
System of congruences with coprime moduli has unique solution modulo their product

---

## 💻 Core Implementations

### 1. Basic Modular Operations

```python
def mod_add(a, b, m):
    """
    Compute (a + b) mod m safely
    
    Time: O(1)
    Space: O(1)
    """
    return ((a % m) + (b % m)) % m

def mod_sub(a, b, m):
    """
    Compute (a - b) mod m safely
    
    Handles negative results correctly
    """
    return ((a % m) - (b % m) + m) % m

def mod_mul(a, b, m):
    """
    Compute (a × b) mod m safely
    
    For very large numbers, use:
    return ((a % m) * (b % m)) % m
    """
    return (a * b) % m

# Examples
print(mod_add(10**18, 10**18, 10**9 + 7))
print(mod_sub(5, 10, 7))  # -5 mod 7 = 2
print(mod_mul(10**9, 10**9, 10**9 + 7))

```

### 2. Fast Modular Exponentiation

```python
def pow_mod(base, exp, mod):
    """
    Compute (base^exp) % mod efficiently
    
    Binary exponentiation (exponentiation by squaring)
    
    Time: O(log exp)
    Space: O(1)
    
    Args:
        base: Base number
        exp: Exponent (non-negative)
        mod: Modulus
    
    Returns:
        (base^exp) % mod
    """
    result = 1
    base %= mod
    
    while exp > 0:
        # If exp is odd, multiply base with result
        if exp & 1:
            result = (result * base) % mod
        
        # Square the base
        base = (base * base) % mod
        
        # Divide exponent by 2
        exp >>= 1
    
    return result

# Examples
print(pow_mod(2, 100, 10**9 + 7))    # 2^100 mod (10^9+7)
print(pow_mod(3, 1000000, 10**9 + 7))  # Very large exponent
print(pow_mod(5, 0, 10**9 + 7))      # 1 (anything^0 = 1)

```

### 3. Recursive Fast Exponentiation

```python
def pow_mod_recursive(base, exp, mod):
    """
    Recursive version of fast exponentiation
    
    Time: O(log exp)
    Space: O(log exp) for call stack
    """
    if exp == 0:
        return 1
    
    if exp % 2 == 0:
        # Even exponent: (base^exp) = (base^2)^(exp/2)
        half = pow_mod_recursive(base, exp // 2, mod)
        return (half * half) % mod
    else:
        # Odd exponent: (base^exp) = base × base^(exp-1)
        return (base * pow_mod_recursive(base, exp - 1, mod)) % mod

```

### 4. Modular Inverse - Extended GCD

```python
def mod_inverse_gcd(a, m):
    """
    Find modular inverse using Extended GCD
    
    Time: O(log m)
    Space: O(log m)
    
    Returns: x where (a × x) ≡ 1 (mod m), or None if no inverse
    """
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
    
    gcd, x, _ = extended_gcd(a, m)
    
    if gcd != 1:
        return None  # Inverse doesn't exist
    
    return (x % m + m) % m

# Examples
print(mod_inverse_gcd(3, 11))   # 4, because 3×4 ≡ 1 (mod 11)
print(mod_inverse_gcd(5, 12))   # None, gcd(5,12)=1, so inverse exists
print(mod_inverse_gcd(7, 26))   # 15, because 7×15 ≡ 1 (mod 26)

```

### 5. Modular Inverse - Fermat's Theorem

```python
def mod_inverse_fermat(a, p):
    """
    Find modular inverse using Fermat's Little Theorem
    
    Works only when p is prime
    
    Time: O(log p)
    Space: O(1)
    
    Formula: a^(-1) ≡ a^(p-2) (mod p)
    
    Proof: a^(p-1) ≡ 1 (mod p)  [Fermat]
           a × a^(p-2) ≡ 1 (mod p)
    """
    if a % p == 0:
        return None  # No inverse
    
    return pow_mod(a, p - 2, p)

# Examples (p must be prime)
p = 10**9 + 7  # Common prime modulus
print(mod_inverse_fermat(2, p))
print(mod_inverse_fermat(3, p))
print(mod_inverse_fermat(5, p))

```

### 6. Modular Division

```python
def mod_div(a, b, m):
    """
    Compute (a / b) mod m
    
    Equivalent to: a × b^(-1) mod m
    
    Time: O(log m)
    Space: O(1)
    """
    b_inv = mod_inverse_fermat(b, m)  # Assuming m is prime
    
    if b_inv is None:
        return None  # Division not possible
    
    return (a * b_inv) % m

# Example
print(mod_div(10, 2, 10**9 + 7))  # 5
print(mod_div(7, 3, 10**9 + 7))   # 7 × (3^-1) mod (10^9+7)

```

### 7. Matrix Exponentiation

```python
def matrix_mult_mod(A, B, mod):
    """
    Multiply two 2×2 matrices modulo mod
    
    Time: O(1) for 2×2, O(n³) for n×n
    """
    n = len(A)
    C = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    
    return C

def matrix_pow_mod(M, exp, mod):
    """
    Compute M^exp mod mod using fast exponentiation
    
    Time: O(n³ log exp) for n×n matrix
    
    Applications: Fibonacci, recurrence relations
    """
    n = len(M)
    # Identity matrix
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    while exp > 0:
        if exp & 1:
            result = matrix_mult_mod(result, M, mod)
        
        M = matrix_mult_mod(M, M, mod)
        exp >>= 1
    
    return result

# Example: Fibonacci using matrix exponentiation
def fibonacci_mod(n, mod):
    """
    Compute F(n) mod mod in O(log n)
    
    Uses: [[F(n+1), F(n)], [F(n), F(n-1)]] = [[1,1],[1,0]]^n
    """
    if n == 0:
        return 0
    
    M = [[1, 1], [1, 0]]
    result = matrix_pow_mod(M, n, mod)
    
    return result[0][1]

print(fibonacci_mod(100, 10**9 + 7))

```

---

## 🎯 Quick Reference

### Complexity Table

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| **Addition** | O(1) | O(1) | Direct |
| **Multiplication** | O(1) | O(1) | Direct |
| **Exponentiation** | O(log n) | O(1) | Binary method |
| **Inverse (GCD)** | O(log m) | O(log m) | Extended GCD |
| **Inverse (Fermat)** | O(log p) | O(1) | Prime modulus only |
| **Matrix Power** | O(n³ log k) | O(n²) | n×n matrix |

### Common Patterns

**Pattern 1: Large Power Modulo**

```python
def solve_power(a, b, mod):
    """Compute a^b mod mod"""
    return pow(a, b, mod)  # Python built-in is optimized

```

**Pattern 2: Factorial Modulo**

```python
def factorial_mod(n, mod):
    """Compute n! mod mod"""
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % mod
    return result

```

**Pattern 3: Combinations Modulo**

```python
def nCr_mod(n, r, mod):
    """
    Compute C(n, r) mod mod
    Uses: nCr = n! / (r! × (n-r)!)
    """
    if r > n or r < 0:
        return 0
    
    # Compute factorial
    num = 1
    for i in range(n, n - r, -1):
        num = (num * i) % mod
    
    # Compute denominator
    den = factorial_mod(r, mod)
    
    # Divide using modular inverse
    return (num * mod_inverse_fermat(den, mod)) % mod

```

---

## 🏆 Practice Problems

### LeetCode Problems

| Problem | Difficulty | Key Concept | Link |
|---------|-----------|-------------|------|
| Pow(x, n) | Medium | Fast exponentiation | [LeetCode 50](https://leetcode.com/problems/powx-n/) |
| Super Pow | Medium | Modular exponentiation | [LeetCode 372](https://leetcode.com/problems/super-pow/) |
| Count Good Numbers | Medium | Fast power | [LeetCode 1922](https://leetcode.com/problems/count-good-numbers/) |
| Nth Digit | Medium | Modular arithmetic | [LeetCode 400](https://leetcode.com/problems/nth-digit/) |
| Valid Square | Medium | Modular distance | [LeetCode 593](https://leetcode.com/problems/valid-square/) |

### Classic Problems

```python
# Problem 1: Last Digit of a^b
def last_digit(a, b):
    """
    Find last digit of a^b
    
    Equivalent to: a^b mod 10
    """
    return pow_mod(a, b, 10)

print(last_digit(2, 100))  # 6

# Problem 2: Modular Fibonacci
def fib_mod(n, mod):
    """Compute F(n) mod mod efficiently"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % mod
    
    return b

# Or use matrix method for O(log n)
print(fibonacci_mod(10**6, 10**9 + 7))

# Problem 3: Catalan Number Modulo
def catalan_mod(n, mod):
    """
    Compute C(n) = C(2n, n) / (n+1) mod mod
    
    C(2n, n) = (2n)! / (n! × n!)
    """
    # Compute C(2n, n)
    num = 1
    for i in range(n + 1, 2 * n + 1):
        num = (num * i) % mod
    
    den = factorial_mod(n, mod)
    
    # C(2n, n) / (n+1)
    numer = (num * mod_inverse_fermat(den, mod)) % mod
    return (numer * mod_inverse_fermat(n + 1, mod)) % mod

# Problem 4: Check Congruence
def are_congruent(a, b, m):
    """Check if a ≡ b (mod m)"""
    return (a % m) == (b % m)

print(are_congruent(17, 5, 12))  # True
print(are_congruent(100, 10, 9))  # True

```

---

## 💡 Key Insights

### 1. Why Fast Exponentiation Works

**Naive Approach:** O(n) multiplications

```
a^8 = a × a × a × a × a × a × a × a

```

**Fast Approach:** O(log n) multiplications

```
a^8 = ((a^2)^2)^2
    = ((a×a)^2)^2

```

**Binary Representation:**

```
a^13 = a^(1101₂)
     = a^8 × a^4 × a^1
     = a^(2³) × a^(2²) × a^(2⁰)

```

### 2. Modular Inverse Applications

**Fraction Modulo:**

```
(a/b) mod m = (a × b⁻¹) mod m

```

**Solving Linear Congruences:**

```
ax ≡ b (mod m)
x ≡ b × a⁻¹ (mod m)

```

**Combinations Modulo:**

```
C(n,r) = n! / (r! × (n-r)!)
       ≡ n! × (r!)⁻¹ × ((n-r)!)⁻¹ (mod p)

```

### 3. When to Use Which Method

**Fermat's Theorem (a^(p-2)):**
✅ Fast, simple
✅ Works when modulus is prime
❌ Fails for composite modulus

**Extended GCD:**
✅ Works for any coprime pair
✅ More general
❌ Slightly more complex
❌ Recursive overhead

### 4. Common Moduli in Competitive Programming

```python
MOD1 = 10**9 + 7   # 1000000007 (prime)
MOD2 = 10**9 + 9   # 1000000009 (prime)
MOD3 = 998244353   # Prime, has primitive root

```

**Why these?**
- Prime (Fermat works)

- Fits in 32-bit integer

- No overflow when multiplying two numbers < MOD

---

## 📚 Additional Resources

### Theory

- [CP-Algorithms: Modular Arithmetic](https://cp-algorithms.com/algebra/module-inverse.html)

- [Brilliant: Modular Arithmetic](https://brilliant.org/wiki/modular-arithmetic/)

- [Khan Academy: Modular Arithmetic](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic)

### Practice

- **Codeforces:** Modular arithmetic tag

- **AtCoder:** Math problems

- **Project Euler:** Many modular problems

### Books

- **Concrete Mathematics** - Chapter 4
- **Introduction to Algorithms** - Chapter 31

---

## 🗂️ Topics Covered

1. **[Basic Operations](./01_basic_operations/)** - Add, multiply, subtract (5 problems)
2. **[Modular Inverse](./02_modular_inverse/)** - GCD, Fermat methods (6 problems)
3. **[Fast Exponentiation](./03_fast_exponentiation/)** - Binary method (6 problems)
4. **[Fermat's Theorem](./04_fermats_theorem/)** - Applications (4 problems)
5. **[Euler's Theorem](./05_eulers_theorem/)** - RSA, totient (4 problems)
6. **[Applications](./06_applications/)** - Competitive problems (3 problems)

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 02. Primes](../02_primes/README.md) | **03. Modular Arithmetic** | [04. Divisors →](../04_divisors/README.md) |

---

## 🗺️ Subtopic Navigation

1. [Basic Operations →](./01_basic_operations/)
2. [Modular Inverse →](./02_modular_inverse/)
3. [Fast Exponentiation →](./03_fast_exponentiation/)
4. [Fermat's Theorem →](./04_fermats_theorem/)
5. [Euler's Theorem →](./05_eulers_theorem/)
6. [Applications →](./06_applications/)

