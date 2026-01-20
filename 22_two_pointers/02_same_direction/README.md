---
layout: default
title: "Same Direction"
parent: "Two Pointers"
nav_order: 2
permalink: /22_two_pointers/02_same_direction/
---

<div align="center">

# →→ Same Direction Pointers

### *The Reader-Writer Dance — Fast Explores, Slow Builds*

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Medium-green?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-12+-blue?style=for-the-badge" alt="Problems">
  <img src="https://img.shields.io/badge/Pattern-Slow_→_Fast_→-purple?style=for-the-badge" alt="Pattern">
</p>

*"One pointer reads, one pointer writes — elegance in motion."*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. Opposite Direction](../01_opposite_direction/README.md) | **02. Same Direction** | [03. Linked List →](../03_linked_list/README.md) |

---

## 🎯 What You'll Master

- In-place array modification techniques
- The fast-slow pointer pattern
- Dutch National Flag algorithm (3-way partition)
- Subsequence checking
- Merging sorted arrays

---

## 📊 Visual Diagrams

### Fast-Slow Pointer Pattern
![Fast-Slow Pointer](./images/fast-slow-pointer.svg)

### Dutch National Flag Algorithm
![Dutch National Flag](./images/dutch-national-flag.svg)

### Merge Sorted Arrays
![Merge Sorted Arrays](./images/merge-sorted-arrays.svg)

---

## 📐 Mathematical Foundations

### 1️⃣ The Reader-Writer Model

{: .highlight }
> **Slow pointer** = Write position (builds result)  
> **Fast pointer** = Read position (explores input)

#### Invariant

At any point, \([0, slow)\) contains the valid result built so far.

```
[Valid Result | To Process...]
 ↑            ↑
 0          slow            fast →
```

#### The Pattern

```python
slow = 0
for fast in range(n):
    if should_keep(arr[fast]):
        arr[slow] = arr[fast]
        slow += 1
return slow  # Length of result
```

---

### 2️⃣ Remove Duplicates — The Proof

{: .important }
> **Problem**: Remove duplicates from sorted array in-place. Return new length.

#### Algorithm

```python
slow = 1  # First element is always kept
for fast in range(1, n):
    if arr[fast] != arr[slow - 1]:  # New unique element
        arr[slow] = arr[fast]
        slow += 1
```

#### 🔍 Proof of Correctness

**Loop Invariant**: \([0, slow)\) contains all unique elements seen so far, in sorted order.

**Proof by induction**:

**Base case** (\(slow = 1\)): \([0, 1)\) contains \(arr[0]\), which is trivially unique.

**Inductive step**: Assume \([0, slow)\) contains \(k\) unique elements.

When \(fast\) points to element \(x\):
- If \(x = arr[slow-1]\): duplicate, skip (invariant preserved)
- If \(x \neq arr[slow-1]\): 
  - Since array is sorted and \(x > arr[slow-1]\)
  - \(x\) is different from all elements in \([0, slow)\)
  - Write \(x\) at position \(slow\), increment \(slow\)
  - Now \([0, slow)\) has \(k+1\) unique elements ∎

#### 📊 Visual Example

```
Initial: [1, 1, 2, 2, 2, 3, 4, 4]
          S
          F

Step 1:  F=1, arr[1]=1 = arr[S-1]=1, skip
         [1, 1, 2, 2, 2, 3, 4, 4]
          S
             F

Step 2:  F=2, arr[2]=2 ≠ arr[S-1]=1, write & advance S
         [1, 2, 2, 2, 2, 3, 4, 4]
             S
                F

Step 3:  F=3, arr[3]=2 = arr[S-1]=2, skip
Step 4:  F=4, arr[4]=2 = arr[S-1]=2, skip

Step 5:  F=5, arr[5]=3 ≠ arr[S-1]=2, write & advance S
         [1, 2, 3, 2, 2, 3, 4, 4]
                S
                         F

Step 6:  F=6, arr[6]=4 ≠ arr[S-1]=3, write & advance S
         [1, 2, 3, 4, 2, 3, 4, 4]
                   S
                            F

Step 7:  F=7, arr[7]=4 = arr[S-1]=4, skip

Result:  [1, 2, 3, 4, _, _, _, _]
                      S=4
         
         Return 4 (4 unique elements)
```

---

### 3️⃣ Allow K Duplicates — Generalization

{: .note }
> Generalize to allow at most \(k\) copies of each element.

#### The Formula

Compare with element \(k\) positions back:

```math
\text{if } arr[fast] \neq arr[slow - k]: \text{ keep element}
```

#### Proof

If we're keeping at most \(k\) copies:
- \(arr[slow-k]\) through \(arr[slow-1]\) are the last \(k\) written elements
- If \(arr[fast] = arr[slow-k]\), then we already have \(k\) copies of this value
- If \(arr[fast] \neq arr[slow-k]\), we have fewer than \(k\) copies, safe to add

---

### 4️⃣ Dutch National Flag — 3-Way Partition

{: .highlight }
> Partition array into three regions in single pass: all 0s, all 1s, all 2s.

#### State Definition

We maintain three pointers:
- \(low\): boundary of 0s region
- \(mid\): current element being examined
- \(high\): boundary of 2s region

#### Invariant

```math
[0, low) = \text{all 0s}
[low, mid) = \text{all 1s}
[mid, high] = \text{unknown}
(high, n) = \text{all 2s}
```

#### Algorithm

```
while mid <= high:
    if arr[mid] == 0:
        swap(arr[low], arr[mid])
        low++, mid++
    elif arr[mid] == 1:
        mid++
    else:  # arr[mid] == 2
        swap(arr[mid], arr[high])
        high--
        # Don't increment mid (swapped element is unknown)
```

#### 🔍 Proof of Correctness

**Claim**: The invariant is maintained after each operation.

**Case arr[mid] = 0**:
- \(arr[low]\) is in the 1s region (or \(low = mid\))
- Swap puts 0 at correct position
- Both boundaries advance, maintaining invariant

**Case arr[mid] = 1**:
- Element already in correct region
- Just advance \(mid\)

**Case arr[mid] = 2**:
- Swap with \(high\), putting 2 at end
- Decrement \(high\) (2s region expands)
- Don't increment \(mid\) (new element at \(mid\) is unknown)

**Termination**: When \(mid > high\), unknown region is empty. ∎

#### 📊 Visual Example

```
Initial: [2, 0, 2, 1, 1, 0]
          L
          M
                         H

Step 1: arr[M]=2, swap with H
        [0, 0, 2, 1, 1, 2]
         L
         M
                      H

Step 2: arr[M]=0, swap with L (same pos), L++, M++
        [0, 0, 2, 1, 1, 2]
            L
            M
                      H

Step 3: arr[M]=0, swap with L, L++, M++
        [0, 0, 2, 1, 1, 2]
               L
               M
                      H

Step 4: arr[M]=2, swap with H, H--
        [0, 0, 1, 1, 2, 2]
               L
               M
                   H

Step 5: arr[M]=1, M++
        [0, 0, 1, 1, 2, 2]
               L
                  M
                   H

Step 6: arr[M]=1, M++
        [0, 0, 1, 1, 2, 2]
               L
                      M
                   H

M > H, done!

Result: [0, 0, 1, 1, 2, 2] ✓
```

---

### 5️⃣ Merge Sorted Arrays — From End

{: .important }
> Merge two sorted arrays into the first array (which has extra space).

#### The Insight

Merge from the **end** to avoid overwriting unprocessed elements.

#### Algorithm

```
p1 = m - 1  # Last element of nums1's actual data
p2 = n - 1  # Last element of nums2
p = m + n - 1  # Last position of merged array

while p2 >= 0:
    if p1 >= 0 and nums1[p1] > nums2[p2]:
        nums1[p] = nums1[p1]
        p1--
    else:
        nums1[p] = nums2[p2]
        p2--
    p--
```

#### 🔍 Proof

**Claim**: No unprocessed element is overwritten.

At any point:
- We've filled positions \((p, m+n)\) with largest elements
- Remaining positions \([0, p]\) need \(p1+1\) elements from nums1 and \(p2+1\) from nums2
- \(p = p1 + p2 + 1\) (exactly enough space!)

Since \(p \geq p1\) always, we never overwrite unprocessed nums1 elements. ∎

---

### 6️⃣ Subsequence Check

{: .note }
> Check if string \(s\) is a subsequence of string \(t\).

#### Algorithm

Use pointer \(i\) for \(s\), iterate through \(t\):

```python
i = 0
for c in t:
    if i < len(s) and c == s[i]:
        i += 1
return i == len(s)
```

#### Time Complexity

\(O(|t|)\) — single pass through \(t\).

---

## 📊 Visual Diagrams

### Fast-Slow Pointer Model

```
+-------------------------------------------------------------+
|           SAME DIRECTION POINTER MODEL                      |
+-------------------------------------------------------------+
|                                                             |
|   Array: [a, b, c, d, e, f, g, h, i, j]                    |
|                                                             |
|   Phase 1: Initial                                          |
|   [a, b, c, d, e, f, g, h, i, j]                           |
|    ↑                                                        |
|   S,F                                                       |
|                                                             |
|   Phase 2: Processing                                       |
|   [✓, ✓, ✓, _, _, _, g, h, i, j]                          |
|             ↑        ↑                                      |
|             S        F                                      |
|   Valid     |        |                                      |
|   result ---+        +-- Exploring                         |
|                                                             |
|   Phase 3: Complete                                         |
|   [✓, ✓, ✓, ✓, ✓, _, _, _, _, _]                          |
|                   ↑                 ↑                       |
|                   S                 F (done)                |
|                                                             |
|   Return S = length of valid result                        |
|                                                             |
+-------------------------------------------------------------+
```

### Dutch National Flag Regions

```
+-------------------------------------------------------------+
|                 DUTCH NATIONAL FLAG                         |
+-------------------------------------------------------------+
|                                                             |
|   Array State:                                              |
|                                                             |
|   [0, 0, 0 | 1, 1, 1 | ?, ?, ? | 2, 2, 2]                  |
|    \_____/   \_____/   \_____/   \_____/                   |
|      0s        1s      unknown     2s                       |
|                                                             |
|   Pointers:                                                 |
|            ↑         ↑         ↑                            |
|           low       mid       high                          |
|                                                             |
|   Invariants:                                               |
|   • [0, low)     → all 0s                                  |
|   • [low, mid)   → all 1s                                  |
|   • [mid, high]  → unknown (to process)                    |
|   • (high, n)    → all 2s                                  |
|                                                             |
|   When mid > high, unknown region empty → DONE             |
|                                                             |
+-------------------------------------------------------------+
```

### Merge From End

```
Initial:
nums1 = [1, 3, 5, 0, 0, 0]  m = 3
                     p1↑        p↑
nums2 = [2, 4, 6]  n = 3
              p2↑

Step 1: nums1[p1]=5 vs nums2[p2]=6 → 6 wins
nums1 = [1, 3, 5, 0, 0, 6]
                  p1↑  p↑
nums2 = [2, 4, 6]
           p2↑

Step 2: 5 vs 4 → 5 wins
nums1 = [1, 3, 5, 0, 5, 6]
               p1↑p↑

Step 3: 3 vs 4 → 4 wins
nums1 = [1, 3, 5, 4, 5, 6]
               ↑
              p1,p

Step 4: 3 vs 2 → 3 wins
nums1 = [1, 3, 3, 4, 5, 6]
            ↑
           p1,p

Step 5: 1 vs 2 → 2 wins
nums1 = [1, 2, 3, 4, 5, 6]
         ↑
        p1,p

p2 < 0, done!
Result: [1, 2, 3, 4, 5, 6] ✓
```

---

## 💻 Code Implementations

```python
def removeDuplicates(nums: list[int]) -> int:
    """
    Remove Duplicates from Sorted Array (LeetCode 26).
    
    Keep one copy of each unique element.
    
    Time: O(n), Space: O(1)
    
    Example:
    >>> nums = [1, 1, 2]
    >>> removeDuplicates(nums)
    2
    >>> nums[:2]
    [1, 2]
    """
    if not nums:
        return 0
    
    slow = 1  # Position to write next unique element
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow

def removeDuplicatesII(nums: list[int]) -> int:
    """
    Remove Duplicates II - Allow at most 2 copies (LeetCode 80).
    
    Generalized: compare with element k positions back.
    
    Time: O(n), Space: O(1)
    
    Example:
    >>> nums = [1, 1, 1, 2, 2, 3]
    >>> removeDuplicatesII(nums)
    5
    >>> nums[:5]
    [1, 1, 2, 2, 3]
    """
    if len(nums) <= 2:
        return len(nums)
    
    k = 2  # Allow at most k copies
    slow = k
    
    for fast in range(k, len(nums)):
        if nums[fast] != nums[slow - k]:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow

def removeElement(nums: list[int], val: int) -> int:
    """
    Remove Element (LeetCode 27).
    
    Remove all occurrences of val in-place.
    
    Time: O(n), Space: O(1)
    
    Example:
    >>> nums = [3, 2, 2, 3]
    >>> removeElement(nums, 3)
    2
    """
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow

def moveZeroes(nums: list[int]) -> None:
    """
    Move Zeroes (LeetCode 283).
    
    Move all 0s to end while maintaining order of non-zeros.
    
    Time: O(n), Space: O(1)
    
    Example:
    >>> nums = [0, 1, 0, 3, 12]
    >>> moveZeroes(nums)
    >>> nums
    [1, 3, 12, 0, 0]
    """
    slow = 0  # Position to write next non-zero
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            # Swap to maintain elements (not just overwrite)
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

def sortColors(nums: list[int]) -> None:
    """
    Sort Colors - Dutch National Flag (LeetCode 75).
    
    Sort array containing only 0, 1, 2 in single pass.
    
    Time: O(n), Space: O(1)
    
    Example:
    >>> nums = [2, 0, 2, 1, 1, 0]
    >>> sortColors(nums)
    >>> nums
    [0, 0, 1, 1, 2, 2]
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
            # Don't increment mid - need to check swapped element

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge Sorted Array (LeetCode 88).
    
    Merge nums2 into nums1 (which has space for both).
    Key: Merge from end to avoid overwriting.
    
    Time: O(m + n), Space: O(1)
    
    Example:
    >>> nums1 = [1, 2, 3, 0, 0, 0]
    >>> merge(nums1, 3, [2, 5, 6], 3)
    >>> nums1
    [1, 2, 2, 3, 5, 6]
    """
    p1 = m - 1      # Last element of nums1's data
    p2 = n - 1      # Last element of nums2
    p = m + n - 1   # Last position of merged array
    
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

def isSubsequence(s: str, t: str) -> bool:
    """
    Is Subsequence (LeetCode 392).
    
    Check if s is subsequence of t.
    
    Time: O(|t|), Space: O(1)
    
    Example:
    >>> isSubsequence("abc", "ahbgdc")
    True
    >>> isSubsequence("axc", "ahbgdc")
    False
    """
    i = 0  # Pointer for s
    
    for c in t:
        if i < len(s) and c == s[i]:
            i += 1
    
    return i == len(s)

def partition(nums: list[int], predicate) -> int:
    """
    Generic partition: move elements satisfying predicate to front.
    
    Time: O(n), Space: O(1)
    
    Example:
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> partition(nums, lambda x: x % 2 == 0)  # Move evens to front
    3
    >>> nums[:3]  # First 3 are even (order may vary)
    """
    slow = 0
    
    for fast in range(len(nums)):
        if predicate(nums[fast]):
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    
    return slow

def rotate(nums: list[int], k: int) -> None:
    """
    Rotate Array (LeetCode 189).
    
    Rotate right by k steps using three reversals.
    
    [1,2,3,4,5,6,7] k=3
    → Reverse all: [7,6,5,4,3,2,1]
    → Reverse [0,k): [5,6,7,4,3,2,1]
    → Reverse [k,n): [5,6,7,1,2,3,4] ✓
    
    Time: O(n), Space: O(1)
    """
    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    n = len(nums)
    k = k % n  # Handle k > n
    
    reverse(0, n - 1)    # Reverse entire array
    reverse(0, k - 1)    # Reverse first k elements
    reverse(k, n - 1)    # Reverse remaining elements

def findMaxConsecutiveOnes(nums: list[int]) -> int:
    """
    Max Consecutive Ones (LeetCode 485).
    
    Find maximum consecutive 1s.
    
    Time: O(n), Space: O(1)
    """
    max_count = count = 0
    
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    
    return max_count
```

---

## 🎯 Pattern Summary

| Problem | Technique | Key Insight |
|---------|-----------|-------------|
| Remove Duplicates | Compare with slow-1 | Slow lags behind |
| Allow K Copies | Compare with slow-k | Generalized comparison |
| Remove Element | Filter by condition | Keep non-matching |
| Move Zeroes | Swap to front | Maintain relative order |
| Sort Colors | 3-way partition | Three pointers |
| Merge Arrays | Fill from end | Avoid overwriting |
| Subsequence | Match characters | Greedy matching |

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Technique | Time | Space |
|:-:|---------|-----------|:----:|:-----:|
| 26 | [Remove Duplicates](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Slow-Fast | O(n) | O(1) |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) | Filter | O(n) | O(1) |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | From End | O(m+n) | O(1) |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Swap | O(n) | O(1) |
| 392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Greedy | O(n) | O(1) |
| 485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Counter | O(n) | O(1) |

### 🟡 Medium

| # | Problem | Technique | Time | Space |
|:-:|---------|-----------|:----:|:-----:|
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Dutch Flag | O(n) | O(1) |
| 80 | [Remove Duplicates II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | Slow-Fast | O(n) | O(1) |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | 3 Reversals | O(n) | O(1) |
| 443 | [String Compression](https://leetcode.com/problems/string-compression/) | Read-Write | O(n) | O(1) |

---

## 💡 Interview Tips

### Pattern Recognition

| Signal | Pattern to Use |
|--------|----------------|
| "in-place" | Same direction |
| "remove" / "filter" | Slow-fast |
| "partition" | Dutch flag |
| "merge" | From end (if overlap) |
| "subsequence" | Greedy matching |

### Common Mistakes

| Mistake | Fix |
|---------|-----|
| Overwriting unread data | Process from appropriate end |
| Off-by-one in boundary | Carefully define open/closed intervals |
| Not handling empty input | Check length first |
| Wrong comparison index | Draw out the invariant |

---

## 📚 References

| Resource | Description | Link |
|----------|-------------|------|
| **Dutch National Flag** | Dijkstra's algorithm | [🔗 Wikipedia](https://en.wikipedia.org/wiki/Dutch_national_flag_problem) |
| **In-place Algorithms** | Space-efficient techniques | [🔗 Wikipedia](https://en.wikipedia.org/wiki/In-place_algorithm) |
| **Array Rotation** | Multiple methods | [🔗 GFG](https://www.geeksforgeeks.org/array-rotation/) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

*"Slow and steady builds the result."*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. Opposite Direction](../01_opposite_direction/README.md) | **02. Same Direction** | [03. Linked List →](../03_linked_list/README.md) |
