---
layout: default
title: "Merge K Streams"
parent: "Heaps"
nav_order: 3
permalink: /09_heaps/03_merge_k_streams/

---

<div align="center">

# 🔀 Merge K Streams

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-6+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 02. Top K Problems](../02_top_k_problems/README.md) | **03. Merge K Streams** | [04. Two Heaps →](../04_two_heaps/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ K-way Merge Complexity

**Problem:** Merge k sorted lists with total n elements.

```math
\boxed{T(n, k) = O(n \log k)}
```

**Why?** Each element inserted and extracted once from heap of size k.

---

### 2️⃣ Comparison with Other Approaches

| Approach | Time | Space |
|----------|:----:|:-----:|
| Merge one by one | O(nk) | O(n) |
| Divide & Conquer | O(n log k) | O(log k) |
| Min-Heap | O(n log k) | O(k) |

---

### 3️⃣ K Smallest Pairs

**Problem:** Find k smallest sum pairs from two sorted arrays.

**Key Insight:** Start with (0,0), explore neighbors (i+1,j) and (i,j+1).

```math
\text{pairs to consider} \leq 2k
```

---

## 🎨 Visual Pattern Guide

<div align="center">

![Merge K Streams](./image/merge_k_streams.svg)

</div>

---

## 💻 Code Implementations

```python
import heapq

def mergeKLists(lists: list) -> 'ListNode':
    """
    Merge k sorted linked lists.
    
    Min-heap maintains smallest head from each list.
    
    Time: O(n log k), Space: O(k)
    """

    # Handle empty input
    heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    """
    Find k pairs with smallest sums.
    
    Start with (0,0), explore neighbors.
    
    Time: O(k log k), Space: O(k)
    """
    if not nums1 or not nums2:
        return []
    
    result = []
    visited = set()
    heap = [(nums1[0] + nums2[0], 0, 0)]
    visited.add((0, 0))
    
    while heap and len(result) < k:
        _, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])
        
        # Add neighbors
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))
        
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))
    
    return result

def kthSmallest(matrix: list[list[int]], k: int) -> int:
    """
    Kth smallest in sorted matrix.
    
    Treat as k-way merge of rows.
    
    Time: O(k log n), Space: O(n)
    """
    n = len(matrix)
    heap = [(matrix[i][0], i, 0) for i in range(n)]
    heapq.heapify(heap)
    
    for _ in range(k - 1):
        val, row, col = heapq.heappop(heap)
        if col + 1 < n:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
    
    return heap[0][0]

def smallestRange(nums: list[list[int]]) -> list[int]:
    """
    Smallest range covering one element from each list.
    
    Use heap to track current elements from each list.
    Track current max, minimize range.
    
    Time: O(n log k), Space: O(k)
    """

    # Initialize heap with first element from each list
    heap = []
    current_max = float('-inf')
    
    for i, arr in enumerate(nums):
        heapq.heappush(heap, (arr[0], i, 0))
        current_max = max(current_max, arr[0])
    
    result = [float('-inf'), float('inf')]
    
    while heap:
        current_min, list_idx, elem_idx = heapq.heappop(heap)
        
        # Update result if better range found
        if current_max - current_min < result[1] - result[0]:
            result = [current_min, current_max]
        
        # Move to next element in same list
        if elem_idx + 1 < len(nums[list_idx]):
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)
        else:
            break  # One list exhausted
    
    return result
```

---

## 🏆 LeetCode Problems

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 373 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | BFS + Heap | O(k log k) | O(k) |
| 378 | [Kth Smallest Element in Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | K-way Merge | O(k log n) | O(n) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Min-Heap | O(n log k) | O(k) |
| 632 | [Smallest Range Covering Elements](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Sliding Heap | O(n log k) | O(k) |

---

## 📚 References

| Resource | Link |
|----------|------|
| **K-way Merge** | [GeeksforGeeks](https://www.geeksforgeeks.org/merge-k-sorted-arrays/) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 02. Top K Problems](../02_top_k_problems/README.md) | **03. Merge K Streams** | [04. Two Heaps →](../04_two_heaps/README.md) |
