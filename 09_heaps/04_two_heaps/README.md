---
layout: default
title: "Two Heaps"
parent: "Heaps"
nav_order: 4
permalink: /09_heaps/04_two_heaps/
---

<div align="center">

# ⚖️ Two Heaps Pattern

<p>
  <img src="https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-6+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next Topic |
|:------------|:----------:|--------:|
| [← 03. Merge K Streams](../03_merge_k_streams/README.md) | **04. Two Heaps** | [🏠 Heaps Home](../README.md) → [Graphs](../../10_graphs/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Median Tracking with Two Heaps

**Structure:**

- **Max-Heap (left):** Smaller half of elements

- **Min-Heap (right):** Larger half of elements

**Invariants:**

$$|left| = |right| \text{ or } |left| = |right| + 1
\max(left) \leq \min(right)$$

---

### 2️⃣ Median Formula

$$\text{median} = \begin{cases}
\max(left) & \text{if } |left| > |right| \\
\frac{\max(left) + \min(right)}{2} & \text{if } |left| = |right|
\end{cases}$$

---

### 3️⃣ Rebalancing

After insertion, if heaps are unbalanced:

```
If |left| > |right| + 1:
    Move max(left) to right

If |right| > |left|:
    Move min(right) to left

```

---

### 4️⃣ Time Complexity

| Operation | Time |
|-----------|:----:|
| addNum | O(log n) |
| findMedian | O(1) |

---

## 🎨 Visual Pattern Guide

<div align="center">

![Two Heaps Pattern](./image/two_heaps_pattern.svg)

</div>

---

## 💻 Code Implementations

```python
import heapq

class MedianFinder:
    """
    Find median from data stream using two heaps.
    
    Max-heap (left): smaller half, negated for max behavior
    Min-heap (right): larger half
    
    Invariant: |left| = |right| or |left| = |right| + 1
    """
    def __init__(self):
        self.left = []   # Max-heap (negated)
        self.right = []  # Min-heap
    
    def addNum(self, num: int) -> None:
        # Add to left (max-heap)
        heapq.heappush(self.left, -num)
        
        # Balance: ensure max(left) <= min(right)
        if self.right and -self.left[0] > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        
        # Balance sizes: left can be at most 1 larger
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
    
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2

def maxProfit(k: int, profits: list[int], capital: list[int], w: int) -> int:
    """
    IPO - Maximize capital with k projects.
    
    Two heaps:
    - Min-heap by capital (projects we can't afford yet)
    - Max-heap by profit (projects we can do)
    
    Time: O(n log n), Space: O(n)
    """
    n = len(profits)
    
    # Min-heap of (capital, profit) - projects we can't afford
    unavailable = [(capital[i], profits[i]) for i in range(n)]
    heapq.heapify(unavailable)
    
    # Max-heap of profits - projects we can afford
    available = []
    
    for _ in range(k):
        # Move all affordable projects to available
        while unavailable and unavailable[0][0] <= w:
            cap, profit = heapq.heappop(unavailable)
            heapq.heappush(available, -profit)
        
        # Take best available project
        if not available:
            break
        w += -heapq.heappop(available)
    
    return w

def medianSlidingWindow(nums: list[int], k: int) -> list[float]:
    """
    Sliding window median.
    
    Two heaps with lazy deletion.
    
    Time: O(n log k), Space: O(k)
    """
    from collections import defaultdict
    
    left = []   # Max-heap (negated)
    right = []  # Min-heap
    to_remove = defaultdict(int)  # Lazy deletion
    result = []
    
    def get_median():
        if k % 2 == 1:
            return -left[0]
        return (-left[0] + right[0]) / 2
    
    def rebalance():
        # Clean tops
        while left and to_remove[-left[0]]:
            to_remove[-left[0]] -= 1
            heapq.heappop(left)
        while right and to_remove[right[0]]:
            to_remove[right[0]] -= 1
            heapq.heappop(right)
    
    # Initialize first window
    for i in range(k):
        heapq.heappush(left, -nums[i])
    
    for _ in range(k // 2):
        heapq.heappush(right, -heapq.heappop(left))
    
    result.append(get_median())
    
    for i in range(k, len(nums)):
        out_num = nums[i - k]
        in_num = nums[i]
        
        to_remove[out_num] += 1
        balance = -1 if out_num <= -left[0] else 1
        
        if in_num <= -left[0]:
            heapq.heappush(left, -in_num)
            balance += 1
        else:
            heapq.heappush(right, in_num)
            balance -= 1
        
        # Rebalance
        if balance > 0:
            heapq.heappush(right, -heapq.heappop(left))
        elif balance < 0:
            heapq.heappush(left, -heapq.heappop(right))
        
        rebalance()
        result.append(get_median())
    
    return result

```

---

## 🏆 LeetCode Problems

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Two Heaps | O(log n) | O(n) |
| 480 | [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) | Two Heaps + Lazy Delete | O(n log k) | O(k) |
| 502 | [IPO](https://leetcode.com/problems/ipo/) | Two Heaps | O(n log n) | O(n) |

---

## 📊 Two Heaps Pattern

```
Need dynamic median/partition?
           |
           +-- Stream of numbers → Two Heaps
           |
           +-- Sliding window → Two Heaps + Lazy Delete
           |
           +-- Maximize with constraints → Two Heaps (available/unavailable)

```

---

## 📚 References

| Resource | Link |
|----------|------|
| **Two Heaps Pattern** | [LeetCode Guide](https://leetcode.com/discuss/study-guide/1360400/) |
| **Median Finding** | [GeeksforGeeks](https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next Topic |
|:------------|:----------:|--------:|
| [← 03. Merge K Streams](../03_merge_k_streams/README.md) | **04. Two Heaps** | [🏠 Heaps Home](../README.md) → [Graphs](../../10_graphs/README.md) |
