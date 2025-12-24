---
layout: default
title: "Wilson's Theorem"
parent: "Number Theory"
nav_order: 12
has_children: true
permalink: /31_number_theory/12_wilsons_theorem/
---

<div align="center">

# 🎯 Wilson's Theorem

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Type-Primality_Test-green?style=for-the-badge" alt="Type">
</p>

**The Factorial Characterization of Primes**

*An elegant but impractical primality test*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 11. Legendre's Formula](../11_legendres_formula/README.md) | **12. Wilson's Theorem** | [🏠 Number Theory Home](../README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Wilson's Theorem

**Statement:** A natural number $p > 1$ is prime **if and only if**:

$$(p-1)! \equiv -1 \pmod{p}$$

**Equivalently:** $(p-1)! \equiv p - 1 \pmod{p}$

---

### 2️⃣ Proof Sketch

**If p is prime:**
- Numbers 1, 2, ..., p-1 form a group under multiplication mod p
- Each element except 1 and p-1 pairs with its multiplicative inverse
- So $(p-1)! \equiv 1 \times (p-1) \times (\text{paired products}) \equiv p-1 \pmod{p}$

**If p is composite:**
- Let p = ab where 1 < a, b < p
- Then a | (p-1)! but a ∤ (p-1), so $(p-1)! \not\equiv -1 \pmod{p}$

---

### 3️⃣ Generalizations

**For prime p and 0 ≤ k < p:**

$$(p - k)! \cdot (k-1)! \equiv (-1)^k \pmod{p}$$

---

## 💻 Code Implementations

```python
def wilson_primality_test(n: int) -> bool:
    """
    Check if n is prime using Wilson's theorem.
    
    WARNING: O(n) time - impractical for large n!
    Only for educational purposes.
    
    Time: O(n)
    Space: O(1)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    
    factorial = 1
    for i in range(2, n):
        factorial = (factorial * i) % n
    
    return factorial == n - 1


def factorial_mod_prime(p: int) -> int:
    """Compute (p-1)! mod p. Should be p-1 if p is prime."""
    if p < 2:
        return 0
    
    result = 1
    for i in range(2, p):
        result = result * i % p
    
    return result


def verify_wilson(limit: int = 100):
    """Verify Wilson's theorem for primes up to limit."""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for p in range(2, limit + 1):
        if is_prime(p):
            fact = factorial_mod_prime(p)
            assert fact == p - 1, f"Wilson failed for p={p}"
            print(f"p={p}: (p-1)! mod p = {fact} ≡ -1 (mod {p}) ✓")


# Example usage
print(wilson_primality_test(7))   # True: 6! = 720 ≡ 6 (mod 7) ✓
print(wilson_primality_test(10))  # False: 9! = 362880 ≡ 0 (mod 10)

# Why impractical: computing 10^9! mod (10^9+7) takes forever!
```

---

## 🎨 Visual Walkthrough

```
┌─────────────────────────────────────────────────────────────────┐
│ WILSON'S THEOREM FOR p = 7                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ Compute (7-1)! mod 7 = 6! mod 7                                │
│                                                                 │
│ 6! = 1 × 2 × 3 × 4 × 5 × 6 = 720                              │
│                                                                 │
│ 720 = 102 × 7 + 6                                              │
│ 720 mod 7 = 6 = 7 - 1 ✓                                        │
│                                                                 │
│ Why? Pair inverses:                                             │
│   2 × 4 ≡ 1 (mod 7)                                            │
│   3 × 5 ≡ 1 (mod 7)                                            │
│   1 and 6 are self-inverse (6 ≡ -1)                            │
│                                                                 │
│ So 6! ≡ 1 × 6 × (2×4) × (3×5) ≡ 1 × 6 × 1 × 1 ≡ 6 (mod 7)    │
│                                                                 │
│ 6 ≡ -1 (mod 7) ✓ Prime confirmed!                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏆 Related Problems

| # | Problem | Difficulty | Key Concept |
|:-:|---------|:----------:|-------------|
| 793 | [Preimage Size of Factorial Zeroes Function](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/) | 🔴 Hard | Factorial properties |

---

## 💡 Key Insights

> **Impractical Test:** Computing (n-1)! takes O(n) time - worse than trial division O(√n)!

> **Theoretical Value:** Wilson's theorem is beautiful for proving results, not computing.

> **Pairing Argument:** Key insight: in Z_p^*, each element pairs with its inverse except 1 and -1.

> **Composite Detection:** For composite n = ab, we have a | (n-1)! but a ∤ -1.

---

## 📚 References

| Resource | Link |
|----------|------|
| **Wikipedia** | [Wilson's Theorem](https://en.wikipedia.org/wiki/Wilson%27s_theorem) |
| **Brilliant** | [Wilson's Theorem](https://brilliant.org/wiki/wilsons-theorem/) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 11. Legendre's Formula](../11_legendres_formula/README.md) | **12. Wilson's Theorem** | [🏠 Number Theory Home](../README.md) |

