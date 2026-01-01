---
layout: default
title: "Permutations"
parent: "Combinatorics"
nav_order: 1
permalink: /31_combinatorics/01_permutations/
---

<div align="center">

# 🔄 Permutations

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-20+-blue?style=for-the-badge" alt="Problems">
</p>

**Arrangements Where Order Matters**

*Master all permutation patterns and algorithms*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [🏠 Combinatorics Home](../README.md) | **01. Permutations** | [02. Combinations →](../02_combinations/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Permutation Definition

**Definition:** A permutation is an arrangement of objects in a specific order.

For set $S = \{a, b, c\}$:
- Permutations: ABC, ACB, BAC, BCA, CAB, CBA (6 total)
- Order matters: ABC ≠ BAC

---

### 2️⃣ Permutation Formulas

**Full Permutation (n distinct objects):**

$$P(n) = n!$$

**Proof:** 
- First position: n choices
- Second position: n-1 choices
- Continue... last position: 1 choice
- Total: $n \times (n-1) \times \cdots \times 1 = n!$ ∎

**r-Permutation (r from n):**

$$P(n, r) = \frac{n!}{(n-r)!}$$

**Permutations with Repetition:**

If object $i$ appears $n_i$ times:

$$P = \frac{n!}{n_1! \times n_2! \times \cdots \times n_k!}$$

**Example:** Permutations of "AABBC":
$$\frac{5!}{2! \times 2! \times 1!} = \frac{120}{4} = 30$$

---

### 3️⃣ Circular Permutations

**Theorem:** $n$ distinct objects arranged in a circle have $(n-1)!$ permutations.

**Proof:**
- Linear arrangements: $n!$
- Each circular arrangement corresponds to $n$ linear arrangements (rotations)
- Circular permutations: $\frac{n!}{n} = (n-1)!$ ∎

---

### 4️⃣ Derangements

**Definition:** Permutation where no element appears in its original position.

**Formula:**

$$D_n = n! \sum_{i=0}^{n} \frac{(-1)^i}{i!} \approx \frac{n!}{e}$$

**Recurrence:**

$$D_n = (n-1)(D_{n-1} + D_{n-2})$$

**First few:** $D_0=1, D_1=0, D_2=1, D_3=2, D_4=9, D_5=44$

---

## 🎨 Visual Walkthrough

### Pattern: Generate All Permutations (Backtracking)

```
┌────────────────────────────────────────────────────────────────┐
│ PROBLEM: Generate all permutations of [1,2,3]                  │
├────────────────────────────────────────────────────────────────┤
│ STEP-BY-STEP BACKTRACKING TREE:                                │
│                                                                 │
│                         []                                      │
│                    ╱    |    ╲                                  │
│                  1      2      3                                │
│                ╱  ╲   ╱  ╲   ╱  ╲                               │
│              12   13  21  23  31  32                            │
│              │    │   │   │   │   │                             │
│             123  132 213 231 312 321                            │
│                                                                 │
│ Execution Trace:                                                │
│                                                                 │
│ path=[], remaining=[1,2,3]                                      │
│   Choose 1: path=[1], remaining=[2,3]                           │
│     Choose 2: path=[1,2], remaining=[3]                         │
│       Choose 3: path=[1,2,3], remaining=[] → OUTPUT: [1,2,3]    │
│       Backtrack                                                 │
│     Choose 3: path=[1,3], remaining=[2]                         │
│       Choose 2: path=[1,3,2], remaining=[] → OUTPUT: [1,3,2]    │
│       Backtrack                                                 │
│   Choose 2: path=[2], remaining=[1,3]                           │
│     ... (similar process)                                       │
│                                                                 │
│ Total permutations: 3! = 6                                      │
│ Time complexity: O(n×n!)                                        │
│   - n! permutations                                             │
│   - Each takes O(n) to construct                                │
└────────────────────────────────────────────────────────────────┘
```

---

### Pattern: Next Permutation Algorithm

```
┌────────────────────────────────────────────────────────────────┐
│ PROBLEM: Find next lexicographically greater permutation       │
│ INPUT: [1, 5, 8, 4, 7, 6, 5, 3, 1]                            │
├────────────────────────────────────────────────────────────────┤
│ STEP 1: Find Pivot (rightmost i where arr[i] < arr[i+1])      │
│                                                                 │
│  [1, 5, 8, 4, 7, 6, 5, 3, 1]                                   │
│           ↑   ↑                                                 │
│           4 < 7  (pivot found at index 3)                       │
│                                                                 │
│  Why? Everything after pivot is descending                      │
│  [7, 6, 5, 3, 1] is in reverse order                           │
├────────────────────────────────────────────────────────────────┤
│ STEP 2: Find Successor (rightmost j where arr[j] > pivot)     │
│                                                                 │
│  [1, 5, 8, 4, 7, 6, 5, 3, 1]                                   │
│           ↑       ↑                                             │
│         pivot=4  successor=5                                    │
│                                                                 │
│  Scan from right: 1<4, 3<4, 5>4 ✓ (found!)                     │
├────────────────────────────────────────────────────────────────┤
│ STEP 3: Swap pivot and successor                               │
│                                                                 │
│  [1, 5, 8, 5, 7, 6, 4, 3, 1]                                   │
│           ↑       ↑                                             │
│        swapped these                                            │
├────────────────────────────────────────────────────────────────┤
│ STEP 4: Reverse suffix (after pivot position)                  │
│                                                                 │
│  Suffix: [7, 6, 4, 3, 1]                                       │
│  Reversed: [1, 3, 4, 6, 7]                                     │
│                                                                 │
│  Result: [1, 5, 8, 5, 1, 3, 4, 6, 7]                           │
│                                                                 │
│ Why reverse? To get smallest arrangement of suffix             │
└────────────────────────────────────────────────────────────────┘
```

---

## 💻 Code Implementations

### Implementation 1: Generate All Permutations

```python
def permute(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations using backtracking.
    
    Time: O(n×n!)
    - Generate n! permutations
    - Each takes O(n) to build
    
    Space: O(n!) for result + O(n) recursion stack
    """
    result = []
    
    def backtrack(path, remaining):
        # Base case: no more elements to choose
        if not remaining:
            result.append(path[:])
            return
        
        # Try each remaining element
        for i in range(len(remaining)):
            # Choose element i
            path.append(remaining[i])
            
            # Explore with remaining elements (excluding i)
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(path, new_remaining)
            
            # Unchoose (backtrack)
            path.pop()
    
    backtrack([], nums)
    return result


def permute_swap(nums: List[int]) -> List[List[int]]:
    """
    Generate permutations using swap technique.
    More space-efficient as we swap in-place.
    
    Time: O(n×n!), Space: O(n) recursion
    """
    result = []
    
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            # Swap current with start position
            nums[start], nums[i] = nums[i], nums[start]
            
            # Recurse on rest
            backtrack(start + 1)
            
            # Backtrack (swap back)
            nums[start], nums[i] = nums[i], nums[start]
    
    backtrack(0)
    return result
```

---

### Implementation 2: Permutations with Duplicates

```python
def permuteUnique(nums: List[int]) -> List[List[int]]:
    """
    Generate unique permutations when array has duplicates.
    
    Key insight: Skip duplicate choices at same recursion level.
    
    Time: O(n×n!/k₁!k₂!...kₙ!)
    where kᵢ is frequency of element i
    
    Space: O(n)
    """
    result = []
    nums.sort()  # Sort to group duplicates together
    used = [False] * len(nums)
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            # Skip if already used
            if used[i]:
                continue
            
            # Skip duplicates at same level
            # If nums[i] == nums[i-1] and nums[i-1] not used,
            # then nums[i] would create duplicate permutation
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            
            # Choose
            path.append(nums[i])
            used[i] = True
            
            # Explore
            backtrack(path)
            
            # Unchoose
            path.pop()
            used[i] = False
    
    backtrack([])
    return result
```

---

### Implementation 3: Next Permutation

```python
def nextPermutation(nums: List[int]) -> None:
    """
    Rearrange to next lexicographically greater permutation in-place.
    
    Algorithm:
    1. Find pivot: rightmost i where nums[i] < nums[i+1]
    2. Find successor: rightmost j where nums[j] > nums[i]
    3. Swap nums[i] and nums[j]
    4. Reverse nums[i+1:]
    
    Time: O(n), Space: O(1)
    
    Example: [1,3,5,4,2] → [1,4,2,3,5]
    """
    n = len(nums)
    
    # Step 1: Find pivot
    pivot = n - 2
    while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
        pivot -= 1
    
    # If pivot found (not last permutation)
    if pivot >= 0:
        # Step 2: Find successor
        successor = n - 1
        while nums[successor] <= nums[pivot]:
            successor -= 1
        
        # Step 3: Swap
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
    
    # Step 4: Reverse suffix to get smallest arrangement
    left, right = pivot + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

---

### Implementation 4: Kth Permutation

```python
def getPermutation(n: int, k: int) -> str:
    """
    Find kth permutation sequence of numbers 1 to n.
    
    Approach: Build permutation digit by digit using factorial.
    
    For n=4:
    - 0-5 start with 1 (0! to 5!)
    - 6-11 start with 2
    - 12-17 start with 3
    - 18-23 start with 4
    
    Each block has (n-1)! permutations.
    
    Time: O(n²), Space: O(n)
    """
    import math
    
    numbers = list(range(1, n + 1))
    k -= 1  # Convert to 0-indexed
    result = []
    
    for i in range(n, 0, -1):
        # How many permutations per block at this level
        factorial = math.factorial(i - 1)
        
        # Which block does k fall into?
        index = k // factorial
        result.append(str(numbers[index]))
        
        # Remove chosen number
        numbers.pop(index)
        
        # Update k for next iteration
        k %= factorial
    
    return ''.join(result)
```

---

### Implementation 5: Count Permutations with Pattern

```python
def numPermutations(word: str) -> int:
    """
    Count distinct permutations of word with repeated characters.
    
    Formula: n! / (n₁! × n₂! × ... × nₖ!)
    
    Example: "AABB" → 4!/(2!×2!) = 6
    
    Time: O(n), Space: O(1)
    """
    from collections import Counter
    import math
    
    MOD = 10**9 + 7
    
    n = len(word)
    freq = Counter(word)
    
    # Calculate n!
    numerator = math.factorial(n)
    
    # Calculate product of factorials of frequencies
    denominator = 1
    for count in freq.values():
        denominator *= math.factorial(count)
    
    return numerator // denominator
```

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Key Concept | Time |
|:-:|---------|-------------|------|
| 509 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Sequence pattern | O(n) |

### 🟡 Medium

| # | Problem | Key Concept | Time |
|:-:|---------|-------------|------|
| 31 | [Next Permutation](https://leetcode.com/problems/next-permutation/) | Lexicographic order | O(n) |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | Backtracking | O(n×n!) |
| 47 | [Permutations II](https://leetcode.com/problems/permutations-ii/) | Handle duplicates | O(n×n!) |
| 60 | [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) | Factorial system | O(n²) |
| 267 | [Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/) | Palindrome constraint | O(n×n!) |
| 266 | [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) | Check possibility | O(n) |
| 484 | [Find Permutation](https://leetcode.com/problems/find-permutation/) | Greedy construction | O(n) |
| 526 | [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/) | Constraint backtracking | O(n!) |
| 556 | [Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) | Next permutation variant | O(log n) |
| 1850 | [Minimum Adjacent Swaps to Reach Kth Smallest](https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/) | Permutation + swaps | O(n²) |

### 🔴 Hard

| # | Problem | Key Concept | Time |
|:-:|---------|-------------|------|
| 629 | [K Inverse Pairs Array](https://leetcode.com/problems/k-inverse-pairs-array/) | DP counting | O(n×k) |
| 1467 | [Probability of a Two Boxes Having Same Balls](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/) | Multinomial | O(2^n) |
| 1850 | [Minimum Swaps to Reach Kth Smallest](https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/) | Permutation ordering | O(n²) |
| 1916 | [Count Ways to Build Rooms](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/) | Tree permutations | O(n) |
| 2514 | [Count Anagrams](https://leetcode.com/problems/count-anagrams/) | Multiset permutations | O(n) |

---

## 🎓 Common Patterns

### Pattern 1: Backtracking Template

```python
def permutation_backtrack(elements):
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            # Choose
            path.append(remaining[i])
            # Explore
            backtrack(path, remaining[:i] + remaining[i+1:])
            # Unchoose
            path.pop()
    
    backtrack([], elements)
    return result
```

### Pattern 2: Skip Duplicates

```python
# When handling duplicates, sort first
nums.sort()

# Then skip duplicates at same level
if i > start and nums[i] == nums[i-1]:
    continue
```

### Pattern 3: Factorial Number System

```python
# Kth permutation using factorial
def kth_permutation(n, k):
    factorial = [1]
    for i in range(1, n):
        factorial.append(factorial[-1] * i)
    
    k -= 1
    result = []
    numbers = list(range(1, n+1))
    
    for i in range(n-1, -1, -1):
        index = k // factorial[i]
        result.append(numbers[index])
        numbers.pop(index)
        k %= factorial[i]
    
    return result
```

---

## 💡 Key Insights

> **When to Use Permutations:**  
> - Order matters
> - Arrangements, sequences, orderings
> - "All possible arrangements"

> **Optimization Tips:**  
> - Sort for duplicate handling
> - Use factorial for kth permutation
> - Swap in-place for space efficiency

> **Time Complexity:**  
> - Generating all: O(n×n!)
> - Next permutation: O(n)
> - Kth permutation: O(n²)

---

## 📚 References

| Resource | Link |
|----------|------|
| **Permutation Algorithms** | [Wikipedia](https://en.wikipedia.org/wiki/Permutation#Algorithms_to_generate_permutations) |
| **Next Permutation** | [CP-Algorithms](https://cp-algorithms.com/combinatorics/generating_combinations.html) |
| **Factorial Number System** | [OEIS](https://oeis.org/A007623) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [🏠 Combinatorics Home](../README.md) | **01. Permutations** | [02. Combinations →](../02_combinations/README.md) |

