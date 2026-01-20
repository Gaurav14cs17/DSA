---
layout: default
title: "Divide and Conquer"
nav_order: 29
has_children: true
permalink: /20_divide_and_conquer/

---

<div align="center">

# ⚔️ Divide and Conquer

![Divide and Conquer Overview](./images/dnc-overview.svg)

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Subtopics-3-blue?style=for-the-badge" alt="Subtopics">
  <img src="https://img.shields.io/badge/Problems-20+-orange?style=for-the-badge" alt="Problems">
</p>

**Divide → Conquer → Combine**

[⬅️ Previous: Greedy Algorithms](../19_greedy_algorithms/README.md) | [🏠 Home](../README.md) | [Next: Bit Manipulation ➡️](../21_bit_manipulation/README.md)

</div>

---

## 🖼️ Visual Overview

<div align="center">
  <img src="./images/divide-conquer.svg" alt="Divide and Conquer Paradigm" width="100%">
</div>

---

## 📐 Mathematical Foundation

### 1️⃣ D&C Paradigm

1. **Divide:** Split problem into smaller subproblems
2. **Conquer:** Solve subproblems recursively
3. **Combine:** Merge solutions into final answer

---

### 2️⃣ Master Theorem

For recurrence $T(n) = aT(n/b) + f(n)$:

| Case | Condition | Complexity |
|------|-----------|------------|
| 1 | $f(n) = O(n^{\log\_b a - \epsilon})$ | $T(n) = \Theta(n^{\log\_b a})$ |
| 2 | $f(n) = \Theta(n^{\log\_b a})$ | $T(n) = \Theta(n^{\log\_b a} \log n)$ |
| 3 | $f(n) = \Omega(n^{\log\_b a + \epsilon})$ | $T(n) = \Theta(f(n))$ |

---

### 3️⃣ Common Recurrences

| Algorithm | Recurrence | Complexity |
|-----------|------------|------------|
| Binary Search | $T(n) = T(n/2) + O(1)$ | $O(\log n)$ |
| Merge Sort | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ |
| Quick Sort (avg) | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ |
| Strassen's | $T(n) = 7T(n/2) + O(n^2)$ | $O(n^{2.81})$ |
| Karatsuba | $T(n) = 3T(n/2) + O(n)$ | $O(n^{1.58})$ |

---

### 4️⃣ Merge Sort Analysis

```math
T(n) = 2T(n/2) + cn
```

**Recursion tree:**
- Level 0: $cn$
- Level 1: $2 \times c(n/2) = cn$
- Level k: $cn$
- Height: $\log n$

```math
T(n) = cn \times \log n = O(n \log n)
```

---

## 📂 Subtopics Navigation

| # | Topic | Problems | Link |
|:-:|-------|:--------:|------|
| 1 | Merge Sort Pattern | 8+ | [📖 Go →](./01_merge_sort_pattern/README.md) |
| 2 | Quick Select | 6+ | [📖 Go →](./02_quick_select/README.md) |
| 3 | Binary Search D&C | 6+ | [📖 Go →](./03_binary_search_dc/README.md) |

---

## 🎯 Key Patterns

### Merge Sort Pattern

```python
def mergeSort(arr: list[int]) -> list[int]:
    """
    Classic Merge Sort.
    
    Time: O(n log n), Space: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Quick Select

```python
def quickSelect(arr: list[int], k: int) -> int:
    """
    Find kth smallest element.
    
    Average: O(n), Worst: O(n²)
    """
    import random
    
    def partition(left, right, pivot_idx):
        pivot = arr[pivot_idx]
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
        store = left
        
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store], arr[i] = arr[i], arr[store]
                store += 1
        
        arr[store], arr[right] = arr[right], arr[store]
        return store
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        pivot_idx = random.randint(left, right)
        pivot_idx = partition(left, right, pivot_idx)
        
        if pivot_idx == k:
            return arr[k]
        elif pivot_idx < k:
            left = pivot_idx + 1
        else:
            right = pivot_idx - 1
    
    return arr[k]
```

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | D&C / Boyer-Moore | O(n log n) | O(log n) |

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | D&C | O(n log n) | O(log n) |
| 215 | [Kth Largest](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Quick Select | O(n) avg | O(1) |
| 240 | [Search 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) | D&C | O(m+n) | O(1) |
| 912 | [Sort an Array](https://leetcode.com/problems/sort-an-array/) | Merge Sort | O(n log n) | O(n) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Binary Search | O(log min(m,n)) | O(1) |
| 23 | [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | D&C Merge | O(n log k) | O(log k) |
| 315 | [Count Smaller After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Merge Sort | O(n log n) | O(n) |
| 493 | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | Merge Sort | O(n log n) | O(n) |

---

## 📊 D&C Pattern Decision

<div align="center">
  <img src="./images/dc-patterns.svg" alt="D&C Pattern Decision Tree" width="100%">
</div>

---

## 📚 References

| Resource | Link |
|----------|------|
| **Divide and Conquer** | [Wikipedia](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm) |
| **Master Theorem** | [Wikipedia](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) |
| **CLRS Book** | Introduction to Algorithms, Chapter 4 |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

[⬅️ Previous: Greedy Algorithms](../19_greedy_algorithms/README.md) | [🏠 Home](../README.md) | [Next: Bit Manipulation ➡️](../21_bit_manipulation/README.md)

</div>
