---
layout: default
title: "Basic Array Operations"
parent: "Arrays"
nav_order: 1
permalink: /01_arrays/01_basic_operations/
---

<div align="center">

# 🔧 Basic Array Operations

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Medium-green?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-15+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [🏠 Arrays Home](../README.md) | **01. Basic Operations** | [02. Subarray Problems →](../02_subarray_problems/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Array Access Time Complexity

**Theorem:** Array access is O(1).

**Proof:**

```math
\text{Address}(A[i]) = \text{Base} + i \times \text{sizeof(element)}

```

Operations: 1 multiplication + 1 addition = constant time ∎

---

### 2️⃣ Two Pointers Complexity

**Theorem:** Two opposite-direction pointers complete in O(n).

**Proof:**
- Let $d = right - left$ (initial distance)

- Each iteration: $d$ decreases by at least 1
- Maximum iterations: $d\_{initial} = n - 1$

- Therefore: O(n) ∎

**Convergence Formula:**

```math
\text{Iterations} = \frac{n}{2} \text{ (for symmetric operations)}

```

---

### 3️⃣ Dutch National Flag Invariants

**Three-way partition maintains:**

```math
\begin{aligned}
A[0..low-1] &= \{0\} \\
A[low..mid-1] &= \{1\} \\
A[mid..high] &= \text{unknown} \\
A[high+1..n-1] &= \{2\}
\end{aligned}

```

**Correctness Proof:**
- Invariant holds initially (all regions empty)

- Each operation preserves invariant

- When $mid > high$: no unknown elements remain ∎

---

### 4️⃣ Array Rotation Formula

**Right rotation by k positions:**

```math
A'[i] = A[(i - k + n) \mod n]

```

**Reversal Algorithm Correctness:**

```math
\text{Rev}(\text{Rev}(A[0..n-k-1]) \| \text{Rev}(A[n-k..n-1])) = A[n-k..n-1] \| A[0..n-k-1]

```

**Proof:**
1. $\text{Rev}(A) = [a\_n, a\_{n-1}, \ldots, a\_1]$
2. $\text{Rev}(A[0..k-1]) = [a\_k, \ldots, a\_1]$
3. $\text{Rev}(A[k..n-1]) = [a\_n, \ldots, a\_{k+1}]$
4. Combined: $[a\_{n-k+1}, \ldots, a\_n, a\_1, \ldots, a\_{n-k}]$ ∎

---

### 5️⃣ Floyd's Cycle Detection Mathematics

**For array where $f(x) = nums[x]$:**

**Theorem:** If duplicate exists, cycle exists.

**Proof by Pigeonhole:**
- n+1 values in range [1, n]

- At least one value repeats

- Repeated value = cycle entry point ∎

**Meeting Point Formula:**

```math
\text{slow travels: } \mu + \lambda k_1
\text{fast travels: } \mu + \lambda k_2 = 2(\mu + \lambda k_1)

```

Where $\mu$ = distance to cycle, $\lambda$ = cycle length.

---

## 🎨 Visual Diagrams

<div align="center">

### Two Pointers Technique
![Two Pointers](./images/two_pointers.svg)

### Array Rotation (Three Reversals)
![Array Rotation](./images/array_rotation.svg)

### Dutch National Flag Algorithm
![Dutch National Flag](./images/dutch_flag.svg)

### Dutch National Flag (Detailed)
![Dutch National Flag Detailed](./images/dutch_national_flag.svg)

### Floyd's Cycle Detection
![Floyd's Cycle](./images/floyds_cycle.svg)

</div>

---

## 🎨 Visual Algorithm Walkthroughs

### Remove Duplicates from Sorted Array

```
Input: [1, 1, 2, 2, 2, 3, 3]

+-----------------------------------------------------------------------+

|  Two Pointers: write (i) and read (j)                                 |
+-----------------------------------------------------------------------+
|                                                                       |
|  Initial: i=0, j=1                                                    |
|  +---+---+---+---+---+---+---+                                       |
|  | 1 | 1 | 2 | 2 | 2 | 3 | 3 |                                       |
|  +---+---+---+---+---+---+---+                                       |
|    i   j                                                              |
|                                                                       |
|  j=1: A[1]=1 = A[i]=1 → Skip duplicate                               |
|  j=2: A[2]=2 ≠ A[i]=1 → i++, copy                                    |
|  +---+---+---+---+---+---+---+                                       |
|  | 1 | 2 | 2 | 2 | 2 | 3 | 3 |                                       |
|  +---+---+---+---+---+---+---+                                       |
|        i       j                                                      |
|                                                                       |
|  j=3,4: A[j]=2 = A[i]=2 → Skip                                       |
|  j=5: A[5]=3 ≠ A[i]=2 → i++, copy                                    |
|  +---+---+---+---+---+---+---+                                       |
|  | 1 | 2 | 3 | 2 | 2 | 3 | 3 |                                       |
|  +---+---+---+---+---+---+---+                                       |
|            i               j                                          |
|                                                                       |
|  Result: First 3 elements [1, 2, 3] are unique                       |
|  Return: i + 1 = 3                                                    |
+-----------------------------------------------------------------------+

```

### Rotate Array (Three Reversals)

```
Input: [1, 2, 3, 4, 5, 6, 7], k = 3

+-----------------------------------------------------------------------+

|  Step 1: Reverse entire array                                         |
|  +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+     |
|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | → | 7 | 6 | 5 | 4 | 3 | 2 | 1 |     |
|  +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+     |
+-----------------------------------------------------------------------+

|  Step 2: Reverse first k elements [0, k-1]                           |
|  +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+     |
|  | 7 | 6 | 5 | 4 | 3 | 2 | 1 | → | 5 | 6 | 7 | 4 | 3 | 2 | 1 |     |
|  +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+     |
|    ↑-------↑                                                          |
|    reverse this part                                                  |
+-----------------------------------------------------------------------+

|  Step 3: Reverse remaining [k, n-1]                                   |
|  +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+     |
|  | 5 | 6 | 7 | 4 | 3 | 2 | 1 | → | 5 | 6 | 7 | 1 | 2 | 3 | 4 | ✓   |
|  +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+     |
|              ↑---------------↑                                        |
|              reverse this part                                        |
+-----------------------------------------------------------------------+

```

### Dutch National Flag (Sort Colors)

```
Input: [2, 0, 2, 1, 1, 0]

+-----------------------------------------------------------------------+

|  Three pointers: low, mid, high                                       |
|                                                                       |
|  Invariant:                                                           |
|  [0...low-1] = 0s | [low...mid-1] = 1s | [mid...high] = ? | [high+1...] = 2s |
+-----------------------------------------------------------------------+

|  Initial: low=0, mid=0, high=5                                        |
|  +---+---+---+---+---+---+                                           |
|  | 2 | 0 | 2 | 1 | 1 | 0 |                                           |
|  +---+---+---+---+---+---+                                           |
|   lm                   h                                              |
|                                                                       |
|  A[mid]=2 → swap(mid, high), high--                                  |
|  +---+---+---+---+---+---+                                           |
|  | 0 | 0 | 2 | 1 | 1 | 2 |                                           |
|  +---+---+---+---+---+---+                                           |
|   lm               h                                                  |
|                                                                       |
|  A[mid]=0 → swap(low, mid), low++, mid++                             |
|  +---+---+---+---+---+---+                                           |
|  | 0 | 0 | 2 | 1 | 1 | 2 |                                           |
|  +---+---+---+---+---+---+                                           |
|       l   m       h                                                   |
|                                                                       |
|  Continue... Final: [0, 0, 1, 1, 2, 2] ✓                             |
+-----------------------------------------------------------------------+

```

---

## 💻 Code with Mathematical Comments

```python
def removeDuplicates(nums: list[int]) -> int:
    """
    Remove duplicates from sorted array.
    
    Mathematical Invariant:
    After processing index j: nums[0..i] contains unique elements
    
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    i = 0  # Write pointer
    for j in range(1, len(nums)):  # Read pointer
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1  # Length = last index + 1

def rotate(nums: list[int], k: int) -> None:
    """
    Rotate array right by k positions.
    
    Mathematical Formula: new_pos[i] = (i + k) mod n
    Algorithm: Three reversals (O(1) space)
    
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    k = k % n  # Handle k > n
    
    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    reverse(0, n - 1)    # Reverse all
    reverse(0, k - 1)    # Reverse first k
    reverse(k, n - 1)    # Reverse rest

def sortColors(nums: list[int]) -> None:
    """
    Dutch National Flag - sort 0s, 1s, 2s.
    
    Invariant maintained:
    [0..low-1]=0s, [low..mid-1]=1s, [mid..high]=unknown, [high+1..n-1]=2s
    
    Time: O(n), Space: O(1)
    """
    low = mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

def findDuplicate(nums: list[int]) -> int:
    """
    Find duplicate using Floyd's Cycle Detection.
    
    Mathematical Basis:
    - Values in [1, n], array size n+1
    - Pigeonhole: at least one duplicate exists
    - Treat value as next index → linked list with cycle
    
    Time: O(n), Space: O(1)
    """
    # Phase 1: Find meeting point
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find cycle entrance
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

```

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Technique | Time | Space |
|:-:|---------|-----------|:----:|:-----:|
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Two Pointers | O(n) | O(1) |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) | Two Pointers | O(n) | O(1) |
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) | Carry Propagation | O(n) | O(1) |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Reverse Fill | O(m+n) | O(1) |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | XOR Property | O(n) | O(1) |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Two Pointers | O(n) | O(1) |
| 448 | [Find Disappeared Numbers](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | Index as Hash | O(n) | O(1) |

### 🟡 Medium

| # | Problem | Technique | Time | Space |
|:-:|---------|-----------|:----:|:-----:|
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Dutch Flag | O(n) | O(1) |
| 80 | [Remove Duplicates II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | Two Pointers | O(n) | O(1) |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | Three Reversals | O(n) | O(1) |
| 238 | [Product Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Prefix × Suffix | O(n) | O(1) |
| 287 | [Find Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Floyd's Cycle | O(n) | O(1) |

### 🔴 Hard

| # | Problem | Technique | Time | Space |
|:-:|---------|-----------|:----:|:-----:|
| 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | Index as Hash | O(n) | O(1) |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Two Pointers | O(n) | O(1) |
| 135 | [Candy](https://leetcode.com/problems/candy/) | Two Pass | O(n) | O(n) |

---

## 💡 Key Insights & Pro Tips

> **🎯 Two Pointers Technique**  
> Use opposite-direction pointers for palindromes and sorted arrays. Use same-direction pointers (slow/fast) for duplicates and partitioning.

> **⚡ In-Place Algorithms**  
> When asked to use O(1) space, think about: (1) Using array indices as markers, (2) Swapping elements, (3) Using the sign bit for flags.

> **🔄 Rotation Trick**  
> Three reversals = one rotation. This works because reverse is self-inverse: Rev(Rev(A)) = A.

> **📊 Dutch Flag Pattern**  
> Any 3-way partition problem can use this technique: maintain 4 regions with 3 pointers.

> **🔍 Floyd's Cycle Detection**  
> When array values can be treated as "next indices", you have an implicit linked list. Perfect for duplicate detection.

---

## 🎓 Pattern Recognition Guide

### When to Use Each Technique

| Pattern | When to Use | Example Problems |
|---------|-------------|------------------|
| **Two Pointers (opposite)** | Sorted array, find pair/triplet | Two Sum II, Container With Water |
| **Two Pointers (same dir)** | Remove duplicates, partition | Remove Duplicates, Move Zeroes |
| **Dutch Flag** | 3-way partition, sort 0-1-2 | Sort Colors, 3-Way Quicksort |
| **Array as Hash** | Values in [1,n], find duplicates | Find Duplicate, Missing Number |
| **Reversal** | Rotate array, reverse string | Rotate Array, Reverse Words |
| **Floyd's Cycle** | Linked list via array indices | Find Duplicate Number |

---

## 🎯 Complexity Analysis Summary

### Space Optimization Techniques

| Technique | Space | Trade-off |
|-----------|:-----:|-----------|
| **Extra Array** | O(n) | Simple, safe |
| **Two Pointers** | O(1) | Modify in-place |
| **Index as Hash** | O(1) | Requires value constraints |
| **Bit Manipulation** | O(1) | Limited to flags |

### Time Complexity Patterns

```
Nested loops:           O(n²)  → Try two pointers → O(n)
Linear scan:            O(n)   → Best possible
Multiple passes:        O(kn)  → k constants → O(n)
Sort then scan:         O(n log n) → Often good solution

```

---

## 📚 References & Learning Resources

### 📖 Core Concepts

| Resource | Description | Link |
|----------|-------------|------|
| **Two Pointers Technique** | Comprehensive guide | [GeeksforGeeks](https://www.geeksforgeeks.org/two-pointers-technique/) |
| **Dutch National Flag** | Original problem by Dijkstra | [Wikipedia](https://en.wikipedia.org/wiki/Dutch_national_flag_problem) |
| **Floyd's Cycle Detection** | Tortoise and hare algorithm | [Wikipedia](https://en.wikipedia.org/wiki/Cycle_detection) |

### 🎥 Video Tutorials

| Resource | Topic | Link |
|----------|-------|------|
| **NeetCode** | Two pointers explained | [YouTube](https://www.youtube.com/watch?v=cQ1Oz4ckceM) |
| **Back To Back SWE** | Floyd's cycle detection | [YouTube](https://www.youtube.com/watch?v=PvrxZaH_eZ4) |
| **Tushar Roy** | Dutch national flag | [YouTube](https://www.youtube.com/watch?v=BOt1DAvR0zI) |

### 📝 Interactive Practice

| Platform | Problem Set | Link |
|----------|-------------|------|
| **LeetCode** | Two pointers tag | [Problems](https://leetcode.com/tag/two-pointers/) |
| **HackerRank** | Array manipulation | [Practice](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=arrays) |
| **InterviewBit** | Arrays problems | [Practice](https://www.interviewbit.com/courses/programming/topics/arrays/) |

### 🔬 Advanced Reading

| Resource | Topic | Link |
|----------|-------|------|
| **Bentley's Programming Pearls** | Column 2: Aha! Algorithms | [PDF](https://www.cs.cmu.edu/~15451-f17/Handouts/bentley1984.pdf) |
| **TAOCP Volume 3** | Sorting and searching | [Knuth](https://www-cs-faculty.stanford.edu/~knuth/taocp.html) |

---

## 🎯 Practice Roadmap

### Beginner Level (Start Here!)
1. **Remove Duplicates** (#26) - Learn two pointers
2. **Move Zeroes** (#283) - Practice partitioning
3. **Merge Sorted Array** (#88) - Master reverse fill

### Intermediate Level
4. **Rotate Array** (#189) - Understand reversals
5. **Sort Colors** (#75) - Master Dutch Flag
6. **Remove Element** (#27) - Combine techniques

### Advanced Level
7. **Find Duplicate** (#287) - Learn Floyd's algorithm
8. **First Missing Positive** (#41) - Index as hash
9. **Trapping Rain Water** (#42) - Two pointers mastery

### Mastery Challenge

- Solve each problem in < 15 minutes

- Optimize to O(1) space

- Explain your approach to someone else

---

## 💭 Common Interview Questions

**Q: Why use two pointers instead of extra space?**  
A: O(1) space is often required in system-level programming where memory is limited. It also shows algorithmic maturity.

**Q: When can't we use two pointers?**  
A: When we need to preserve original array state, or when elements aren't sortable/comparable.

**Q: Why is Floyd's cycle detection better than hash set?**  
A: O(1) space vs O(n) space. Critical in memory-constrained environments.

---

<div align="center">

### 🎓 Master This Section First!

*Basic operations form the foundation for all advanced array techniques.*

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

[⬅️ Arrays Home](../README.md) | [➡️ Subarray Problems](../02_subarray_problems/README.md)

---

*Keep practicing! Consistency > Intensity* 💪

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [🏠 Arrays Home](../README.md) | **01. Basic Operations** | [02. Subarray Problems →](../02_subarray_problems/README.md) |
