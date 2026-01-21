---
layout: default
title: "Non-Comparison Sorts"
parent: "Sorting"
nav_order: 2
permalink: /14_sorting/02_non_comparison_sorts/
---

<div align="center">

# 🔢 Non-Comparison Sorting

![Non-Comparison Sorts](./images/non_comparison_sorts.svg)

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-5+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. Comparison Sorts](../01_comparison_sorts/README.md) | **02. Non-Comparison Sorts** | [03. Custom Sorting →](../03_custom_sorting/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Breaking the O(n log n) Barrier

Non-comparison sorts use:

- **Counting:** Values as indices

- **Radix:** Digit-by-digit processing

- **Bucket:** Distribution into ranges

$$T = O(n + k) \text{ or } O(d \cdot (n + k))$$

---

### 2️⃣ Counting Sort

**Condition:** Values in range $[0, k]$ where $k = O(n)$.

$$T = O(n + k), \quad S = O(k)$$

**Steps:**

1. Count occurrences of each value

2. Compute cumulative counts (positions)

3. Build output array

---

### 3️⃣ Radix Sort

**Sort by each digit:** LSD (Least Significant) to MSD.

$$T = O(d \cdot (n + k))$$

Where:

- $d$ = number of digits

- $k$ = base (radix)

For 32-bit integers with base 256: $d = 4$, $k = 256$.

---

### 4️⃣ Bucket Sort

**Distribute into buckets, sort each bucket.**

$$T = O(n + \frac{n^2}{k} + k) = O(n) \text{ if } k = O(n)$$

**Best for:** Uniformly distributed data.

---

### 5️⃣ Dutch National Flag

**Three-way partition** for values in {0, 1, 2}.

$$T = O(n), \quad S = O(1)$$

**Invariant:** 

- $[0, low)$: all 0s

- $[low, mid)$: all 1s

- $[high+1, n)$: all 2s

---

## 💻 Code Implementations

```python
def countingSort(arr: list[int]) -> list[int]:
    """
    Counting Sort for non-negative integers.
    
    Time: O(n + k), Space: O(n + k)
    """
    if not arr:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    # Count occurrences
    for num in arr:
        count[num] += 1
    
    # Build output
    result = []
    for num, freq in enumerate(count):
        result.extend([num] * freq)
    
    return result

def radixSort(arr: list[int]) -> list[int]:
    """
    Radix Sort (LSD).
    
    Time: O(d × (n + k)), Space: O(n + k)
    """
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        arr = countingSortByDigit(arr, exp)
        exp *= 10
    
    return arr

def countingSortByDigit(arr: list[int], exp: int) -> list[int]:
    """Sort by specific digit position."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count digits
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output (right to left for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]
    
    return output

def bucketSort(arr: list[float]) -> list[float]:
    """
    Bucket Sort for floats in [0, 1).
    
    Time: O(n) average, Space: O(n)
    """
    if not arr:
        return arr
    
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    # Distribute into buckets
    for num in arr:
        idx = int(num * n)
        buckets[idx].append(num)
    
    # Sort each bucket
    for bucket in buckets:
        bucket.sort()
    
    # Concatenate
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result

def sortColors(nums: list[int]) -> None:
    """
    Sort Colors / Dutch National Flag (LeetCode 75).
    
    Three-way partition for 0, 1, 2.
    
    Time: O(n), Space: O(1)
    """
    low, mid, high = 0, 0, len(nums) - 1
    
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

def maximumGap(nums: list[int]) -> int:
    """
    Maximum Gap (LeetCode 164).
    
    Bucket sort to find max gap in O(n).
    
    Time: O(n), Space: O(n)
    """
    if len(nums) < 2:
        return 0
    
    min_val, max_val = min(nums), max(nums)
    if min_val == max_val:
        return 0
    
    n = len(nums)
    bucket_size = max(1, (max_val - min_val) // (n - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1
    
    # bucket[i] = [min, max] in bucket
    buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
    
    for num in nums:
        idx = (num - min_val) // bucket_size
        buckets[idx][0] = min(buckets[idx][0], num)
        buckets[idx][1] = max(buckets[idx][1], num)
    
    # Max gap is between buckets (pigeonhole principle)
    max_gap = 0
    prev_max = min_val
    
    for bucket in buckets:
        if bucket[0] == float('inf'):
            continue
        max_gap = max(max_gap, bucket[0] - prev_max)
        prev_max = bucket[1]
    
    return max_gap

```

---

## 🏆 LeetCode Problems

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Dutch Flag | O(n) | O(1) |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Bucket Sort | O(n) | O(n) |
| 451 | [Sort Characters by Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | Bucket Sort | O(n) | O(n) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 164 | [Maximum Gap](https://leetcode.com/problems/maximum-gap/) | Bucket Sort | O(n) | O(n) |

---

## 📊 Non-Comparison Sort Selection

```
Non-Comparison Sort
        |
        +-- Small range integers → Counting Sort
        |
        +-- Large range, limited digits → Radix Sort
        |
        +-- Uniform floats [0,1) → Bucket Sort
        |
        +-- 3 values (0,1,2) → Dutch Flag

```

---

## 📚 References

| Resource | Link |
|----------|------|
| **Counting Sort** | [Wikipedia](https://en.wikipedia.org/wiki/Counting_sort) |
| **Radix Sort** | [Wikipedia](https://en.wikipedia.org/wiki/Radix_sort) |
| **Dutch Flag** | [Wikipedia](https://en.wikipedia.org/wiki/Dutch_national_flag_problem) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. Comparison Sorts](../01_comparison_sorts/README.md) | **02. Non-Comparison Sorts** | [03. Custom Sorting →](../03_custom_sorting/README.md) |
