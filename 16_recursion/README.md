---
layout: default
title: "Recursion"
nav_order: 25
has_children: true
permalink: /16_recursion/
---

<div align="center">

# 🔄 Recursion

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Medium-green?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Subtopics-3-blue?style=for-the-badge" alt="Subtopics">
  <img src="https://img.shields.io/badge/Problems-20+-orange?style=for-the-badge" alt="Problems">
</p>

**Solving problems by breaking them into smaller subproblems**

[⬅️ Previous: Searching](../15_searching/README.md) | [🏠 Home](../README.md) | [Next: Backtracking ➡️](../17_backtracking/README.md)

</div>

---

## 📐 Mathematical Foundation

### 1️⃣ Recursion Definition

A function that calls itself with a smaller input:

$$f(n) = g(f(n-1), n)$$

**Requirements:**
1. **Base case:** Termination condition
2. **Recursive case:** Problem reduction
3. **Progress:** Each call moves toward base case

---

### 2️⃣ Recurrence Relations

| Problem | Recurrence | Solution |
|---------|------------|----------|
| Factorial | $f(n) = n \cdot f(n-1)$ | O(n) |
| Fibonacci | $f(n) = f(n-1) + f(n-2)$ | O(2ⁿ) naive, O(n) memo |
| Binary Search | $T(n) = T(n/2) + O(1)$ | O(log n) |
| Merge Sort | $T(n) = 2T(n/2) + O(n)$ | O(n log n) |

---

### 3️⃣ Master Theorem

For recurrence $T(n) = aT(n/b) + f(n)$:

| Case | Condition | Result |
|------|-----------|--------|
| 1 | $f(n) = O(n^{\log_b a - \epsilon})$ | $T(n) = \Theta(n^{\log_b a})$ |
| 2 | $f(n) = \Theta(n^{\log_b a})$ | $T(n) = \Theta(n^{\log_b a} \log n)$ |
| 3 | $f(n) = \Omega(n^{\log_b a + \epsilon})$ | $T(n) = \Theta(f(n))$ |

---

### 4️⃣ Stack Space

**Recursive depth:** Maximum number of active frames.

$$\text{Space} = O(\text{depth} \times \text{frame size})$$

**Tail recursion:** Can be optimized to O(1) space (in some languages).

---

### 5️⃣ Tree Recursion

When function calls itself multiple times:

$$T(n) = T(n-1) + T(n-2) + \ldots$$

**Example:** Fibonacci without memoization → O(2ⁿ)

---

## 📂 Subtopics Navigation

| # | Topic | Problems | Link |
|:-:|-------|:--------:|------|
| 1 | Basic Recursion | 8+ | [📖 Go →](./01_basic_recursion/README.md) |
| 2 | Tree Recursion | 6+ | [📖 Go →](./02_tree_recursion/README.md) |
| 3 | Memoization | 8+ | [📖 Go →](./03_memoization/README.md) |

---

## 🎯 Key Patterns

### Linear Recursion

```python
def factorial(n: int) -> int:
    """
    Calculate n!
    
    Recurrence: f(n) = n × f(n-1)
    Base case: f(0) = 1
    
    Time: O(n), Space: O(n)
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sumArray(arr: list[int], i: int = 0) -> int:
    """
    Sum array elements recursively.
    
    Time: O(n), Space: O(n)
    """
    if i == len(arr):
        return 0
    return arr[i] + sumArray(arr, i + 1)
```

### Tail Recursion

```python
def factorialTail(n: int, acc: int = 1) -> int:
    """
    Tail-recursive factorial.
    
    Accumulator carries result.
    Can be optimized to O(1) space.
    """
    if n <= 1:
        return acc
    return factorialTail(n - 1, n * acc)
```

### Divide and Conquer

```python
def power(x: float, n: int) -> float:
    """
    Calculate x^n using fast exponentiation.
    
    Recurrence: x^n = (x^(n/2))² × x^(n%2)
    
    Time: O(log n), Space: O(log n)
    """
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x
```

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Linear | O(n+m) | O(n+m) |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linear | O(n) | O(n) |
| 231 | [Power of Two](https://leetcode.com/problems/power-of-two/) | Divide | O(log n) | O(log n) |
| 326 | [Power of Three](https://leetcode.com/problems/power-of-three/) | Divide | O(log n) | O(log n) |
| 509 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Tree/Memo | O(n) | O(n) |
| 700 | [Search in a BST](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Binary | O(h) | O(h) |

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | Linear | O(n) | O(n) |
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Divide | O(log n) | O(log n) |
| 779 | [K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) | Divide | O(n) | O(n) |
| 894 | [All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/) | Tree | O(2ⁿ) | O(2ⁿ) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Linear | O(n) | O(n/k) |
| 273 | [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/) | Divide | O(1) | O(1) |

---

## 📊 Recursion Pattern Decision

```
Recursion Problem
       │
       ├── Single subproblem → Linear recursion O(n)
       │
       ├── Two subproblems (same size) → Divide & Conquer
       │
       ├── Multiple overlapping subproblems → Add memoization
       │
       ├── Explore all possibilities → Backtracking
       │
       └── Deep recursion → Consider iterative + stack
```

---

## 📈 Recursion vs Iteration

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Readability | Often cleaner | Can be verbose |
| Space | O(depth) stack | O(1) possible |
| Performance | Function call overhead | Generally faster |
| Stack overflow | Risk with deep recursion | No risk |

---

## 📚 References

| Resource | Link |
|----------|------|
| **Recursion** | [Wikipedia](https://en.wikipedia.org/wiki/Recursion_(computer_science)) |
| **Master Theorem** | [Wikipedia](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) |
| **Tail Recursion** | [Wikipedia](https://en.wikipedia.org/wiki/Tail_call) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

[⬅️ Previous: Searching](../15_searching/README.md) | [🏠 Home](../README.md) | [Next: Backtracking ➡️](../17_backtracking/README.md)

</div>
