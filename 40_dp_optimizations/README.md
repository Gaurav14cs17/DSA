---
layout: default
title: "DP Optimizations"
nav_order: 42
has_children: true
permalink: /40_dp_optimizations/
---

<div align="center">

# ⚡ DP Optimizations

<p>
  <img src="https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Techniques-12+-blue?style=for-the-badge" alt="Techniques">
  <img src="https://img.shields.io/badge/Problems-60+-green?style=for-the-badge" alt="Problems">
</p>

**Master Advanced DP: From O(n³) to O(n) - Complete Guide**

*When standard DP is too slow, optimize like a pro*

</div>

---

## 📊 Visual Overview

<p align="center">
  <img src="./images/dp-optimizations.svg" alt="DP Optimizations Overview" width="100%">
</p>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← Approximation Algorithms](../39_approximation_algorithms/README.md) | **DP Optimizations** | End of DSA Journey 🎯 |

---

## 📂 Subtopics (11 Techniques)

<table>
<tr>
<td width="50%">

### [01. Space Optimization](./01_space_optimization/)
- Rolling arrays
- O(n²) → O(n) memory
- **Problems:** 12+

### [02. Monotonic Queue](./02_monotonic_queue/)
- Sliding window DP
- O(nk) → O(n)
- **Problems:** 13+

### [03. Convex Hull Trick](./03_convex_hull_trick/)
- Linear function optimization
- O(n²) → O(n log n)
- **Problems:** 8+

### [04. Li Chao Tree](./04_li_chao_tree/)
- Dynamic CHT
- Any order insertion
- **Problems:** Advanced

### [05. Divide & Conquer](./05_divide_conquer/)
- Monge property
- O(n²k) → O(nk log n)
- **Problems:** 5+

### [06. Knuth's Optimization](./06_knuth_optimization/)
- Quadrangle inequality
- O(n³) → O(n²)
- **Problems:** 10+

</td>
<td width="50%">

### [07. SOS DP](./07_sos_dp/)
- Sum over subsets
- O(3ⁿ) → O(n·2ⁿ)
- **Problems:** 4+

### [08. Matrix Exponentiation](./08_matrix_exponentiation/)
- Linear recurrence
- O(n) → O(log n)
- **Problems:** 5+

### [09. Aliens Trick](./09_aliens_trick/)
- Wqs binary search
- O(n²k) → O(n² log C)
- **Problems:** Advanced

### [10. Bitmask DP](./10_bitmask_dp/)
- State compression
- Subset enumeration
- **Problems:** 10+

### [11. Tree DP Rerooting](./11_tree_dp_rerooting/)
- All roots in O(n)
- Two-pass DFS
- **Problems:** Advanced

</td>
</tr>
</table>

---

## 📐 Mathematical Foundation

### When to Optimize DP?

**Standard DP Complexity:** O(number of states × transitions per state)

**Problem Signs:**
- ✅ TLE on large inputs (n > 10⁴)
- ✅ O(n²) or O(n³) recurrence
- ✅ Many redundant computations
- ✅ Transition has special structure

### Optimization Techniques Overview

| Technique | Condition | Speedup | Difficulty |
|-----------|-----------|---------|-----------|
| **Space Optimization** | Independent rows/layers | Memory only | ⭐ |
| **Monotonic Queue** | Range min/max queries | O(nk) → O(n) | ⭐⭐ |
| **Sliding Window** | Fixed window transitions | O(n²) → O(n) | ⭐⭐ |
| **Convex Hull Trick** | Linear functions max/min | O(n²) → O(n log n) | ⭐⭐⭐⭐ |
| **Li Chao Tree** | Dynamic line insertion | O(n²) → O(n log n) | ⭐⭐⭐⭐ |
| **Divide & Conquer** | Monge property | O(n²k) → O(nk log n) | ⭐⭐⭐⭐ |
| **Knuth's Optimization** | Quadrangle inequality | O(n³) → O(n²) | ⭐⭐⭐⭐ |
| **SOS DP** | Subset enumeration | O(3ⁿ) → O(n·2ⁿ) | ⭐⭐⭐ |
| **Matrix Exponentiation** | Linear recurrence | O(n) → O(log n) | ⭐⭐⭐ |
| **Aliens Trick** | Exactly k constraint | O(n²k) → O(n² log C) | ⭐⭐⭐⭐⭐ |

---

## 💻 Technique 1: Space Optimization

### Theory

**Observation:** Many 2D DP tables only depend on previous row.

```
dp[i][j] depends only on dp[i-1][*]
⟹ Keep only 2 rows: current and previous
```

**Space:** O(n²) → O(n)

### Implementation

```python
def space_optimized_dp(arr):
    """
    Example: Longest Common Subsequence
    
    Standard: O(n²) space
    Optimized: O(n) space
    """
    n = len(arr)
    
    # Standard version (O(n²) space)
    def standard():
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i-1][j-1] + 1 if i > 0 and j > 0 else 1
                else:
                    dp[i][j] = max(
                        dp[i-1][j] if i > 0 else 0,
                        dp[i][j-1] if j > 0 else 0
                    )
        return dp[n-1][n-1]
    
    # Optimized version (O(n) space)
    def optimized():
        prev = [0] * n
        curr = [0] * n
        
        for i in range(n):
            for j in range(n):
                if arr[i] == arr[j]:
                    curr[j] = prev[j-1] + 1 if j > 0 else 1
                else:
                    curr[j] = max(
                        prev[j],
                        curr[j-1] if j > 0 else 0
                    )
            prev, curr = curr, [0] * n
        
        return prev[n-1]
    
    return optimized()
```

### Visual Example

```
Original 2D DP (Fibonacci-like):
    0  1  2  3  4
  ┌──────────────
0 │ 0  1  1  2  3
1 │ 1  1  2  3  5
2 │ 1  2  3  5  8
3 │ 2  3  5  8 13

Space Optimized (only keep 2 rows):
prev: [2  3  5  8 13]
curr: [3  5  8 13 21]  ← Computing

Memory: 2n instead of n²
```

### Problems

| # | Problem | Space Reduction |
|:-:|---------|----------------|
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | O(mn) → O(n) |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | O(mn) → O(n) |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | O(nk) → O(k) |
| 518 | [Coin Change II](https://leetcode.com/problems/coin-change-2/) | O(nk) → O(k) |

---

## 💻 Technique 2: Monotonic Queue Optimization

### Theory

**Problem Pattern:**
```
dp[i] = min/max(dp[j] + cost(j, i)) for j ∈ [i-k, i-1]
```

**Key Insight:** Use deque to maintain min/max in sliding window.

**Complexity:** O(nk) → O(n)

### Implementation

```python
from collections import deque

class MonotonicQueueDP:
    def constrained_subset_sum(self, nums, k):
        """
        LeetCode 1425: Constrained Subsequence Sum
        
        dp[i] = max(dp[j]) + nums[i] for j ∈ [i-k, i-1]
        Standard: O(nk)
        Optimized: O(n) with monotonic deque
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        # Deque stores indices in decreasing dp value order
        dq = deque([0])
        
        for i in range(1, n):
            # Remove indices outside window [i-k, i-1]
            while dq and dq[0] < i - k:
                dq.popleft()
            
            # Best value is at front
            dp[i] = nums[i] + max(0, dp[dq[0]])
            
            # Maintain decreasing order
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            
            dq.append(i)
        
        return max(dp)
    
    def jump_game_vi(self, nums, k):
        """
        LeetCode 1696: Jump Game VI
        
        dp[i] = max(dp[j]) + nums[i] for j ∈ [i-k, i-1]
        """
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        
        dq = deque([0])
        
        for i in range(1, n):
            # Remove out-of-range
            while dq and dq[0] < i - k:
                dq.popleft()
            
            dp[i] = nums[i] + dp[dq[0]]
            
            # Keep decreasing order
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)
        
        return dp[n - 1]
```

### Visual Walkthrough

```
Example: nums = [10, -2, -10, -5, 20], k = 2

Initial: dp = [10, _, _, _, _]
         dq = [0]

i=1: Window [0,0], max_dp = 10
     dp[1] = -2 + 10 = 8
     dq = [0, 1]  (8 < 10, don't remove)
     
i=2: Window [0,1], max_dp = 10
     dp[2] = -10 + 10 = 0
     dq = [0, 1, 2]  (0 < 8, don't remove)
     
i=3: Window [1,2], max_dp = 8 (removed index 0)
     dp[3] = -5 + 8 = 3
     dq = [1, 2, 3]
     
i=4: Window [2,3], max_dp = 3
     dp[4] = 20 + 3 = 23
     Remove 1,2,3 (all < 23)
     dq = [4]

Final: dp = [10, 8, 0, 3, 23]
Answer: 23
```

### Problems (Monotonic Queue)

| # | Problem | Difficulty | Pattern |
|:-:|---------|-----------|---------|
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | ⭐⭐⭐ | Basic template |
| 1425 | [Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/) | ⭐⭐⭐⭐ | Range max DP |
| 1696 | [Jump Game VI](https://leetcode.com/problems/jump-game-vi/) | ⭐⭐⭐ | Jump DP |
| 1499 | [Max Value of Equation](https://leetcode.com/problems/max-value-of-equation/) | ⭐⭐⭐⭐ | Transform to y-x form |
| 862 | [Shortest Subarray Sum ≥ K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | ⭐⭐⭐⭐ | Prefix sum + deque |

---

## 💻 Technique 3: Convex Hull Trick (CHT)

### Theory

**Problem Pattern:**
```
dp[i] = min/max(m[j] × x[i] + b[j]) for all j < i
```

Where m[j], b[j] are from previous DP states, x[i] is current query point.

**Geometric Interpretation:**
- Each DP state j defines a line: y = m[j]·x + b[j]
- We want lower (or upper) envelope of these lines
- Query at x[i] returns minimum (or maximum) y value

**Complexity:** O(n²) → O(n log n) or O(n) with special properties

### Implementation (Basic CHT)

```python
class ConvexHullTrick:
    """
    Maintain lower envelope of lines for minimum queries.
    
    Requirements for O(n):
    - Lines added with decreasing slope (m[i] ≥ m[i+1])
    - Queries with increasing x values
    
    General case: O(n log n)
    """
    def __init__(self):
        self.lines = []  # List of (m, b) tuples
    
    def _bad(self, l1, l2, l3):
        """
        Check if line l2 is redundant (never optimal).
        
        l2 is bad if its intersection with l1 is after
        its intersection with l3.
        
        Intersection of (m1,b1) and (m2,b2): x = (b2-b1)/(m1-m2)
        """
        # (b3-b1)/(m1-m3) >= (b2-b1)/(m1-m2)
        # Cross multiply to avoid division
        return ((l3[1] - l1[1]) * (l1[0] - l2[0]) >= 
                (l2[1] - l1[1]) * (l1[0] - l3[0]))
    
    def add_line(self, m, b):
        """
        Add line y = mx + b.
        
        For minimum: m should be decreasing
        For maximum: m should be increasing (or negate all)
        
        Time: O(1) amortized
        """
        new_line = (m, b)
        
        # Remove lines that become suboptimal
        while len(self.lines) >= 2 and self._bad(
            self.lines[-2], self.lines[-1], new_line):
            self.lines.pop()
        
        self.lines.append(new_line)
    
    def query(self, x):
        """
        Find minimum value at x among all lines.
        
        Time: O(log n) binary search, O(1) if x increasing
        """
        if not self.lines:
            return float('inf')
        
        # For increasing x, can use pointer (O(1))
        # Here we use binary search for general case
        
        left, right = 0, len(self.lines) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare mid and mid+1
            val_mid = self.lines[mid][0] * x + self.lines[mid][1]
            val_next = self.lines[mid + 1][0] * x + self.lines[mid + 1][1]
            
            if val_mid >= val_next:
                left = mid + 1
            else:
                right = mid
        
        m, b = self.lines[left]
        return m * x + b
    
    def query_linear(self, x, ptr):
        """
        Query with increasing x using pointer.
        
        Time: O(1) amortized
        Returns: (value, new_pointer)
        """
        ptr = max(0, min(ptr, len(self.lines) - 1))
        
        # Move pointer right while next line is better
        while (ptr < len(self.lines) - 1 and
               self.lines[ptr][0] * x + self.lines[ptr][1] >=
               self.lines[ptr + 1][0] * x + self.lines[ptr + 1][1]):
            ptr += 1
        
        m, b = self.lines[ptr]
        return m * x + b, ptr
```

### Example Problem: Minimum Cost to Split Array

```python
def min_cost_split(arr):
    """
    Split array into groups. Cost of group = (sum)²
    Find minimum total cost.
    
    dp[i] = min(dp[j] + (sum[i] - sum[j])²) for j < i
    
    Expand: dp[j] + sum[i]² - 2·sum[i]·sum[j] + sum[j]²
          = (dp[j] + sum[j]²) - 2·sum[j]·sum[i] + sum[i]²
          =      b[j]         +  m[j] · x[i]   + sum[i]²
    
    Where: m[j] = -2·sum[j], b[j] = dp[j] + sum[j]², x[i] = sum[i]
    """
    n = len(arr)
    
    # Compute prefix sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    # CHT for minimum
    cht = ConvexHullTrick()
    dp = [0] * (n + 1)
    
    # Base case
    cht.add_line(0, 0)  # m=0, b=0
    
    ptr = 0
    for i in range(1, n + 1):
        x = prefix[i]
        
        # Query CHT
        dp[i], ptr = cht.query_linear(x, ptr)
        dp[i] += x * x
        
        # Add new line for future queries
        m = -2 * prefix[i]
        b = dp[i] + prefix[i] ** 2
        cht.add_line(m, b)
    
    return dp[n]
```

### Visual Example (CHT)

```
Lines: L1: y = -2x + 10
       L2: y = -1x + 8
       L3: y = 0x + 5

    y
    │
 10 ├─────╲                L1 (m=-2)
    │      ╲╲
  8 ├───────╲╲─────        L2 (m=-1)
    │        ╲╲╲╲╲
  5 ├─────────╲╲╲╲───────  L3 (m=0)
    │          ╲╲╲╲╲╲╲╲
    └────────────────────── x
    0   1   2   3   4   5

Lower Envelope:
- x ∈ [0, 2]: L1 optimal
- x ∈ [2, 3]: L2 optimal
- x ∈ [3, ∞): L3 optimal

CHT maintains only [L1, L2, L3] (convex hull)
```

### Problems (Convex Hull Trick)

| # | Problem | Difficulty | Form |
|:-:|---------|-----------|------|
| 1687 | [Delivering Boxes](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/) | ⭐⭐⭐⭐ | Splitting with costs |
| 2617 | [Minimum Number of Visited Cells](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/) | ⭐⭐⭐⭐ | Grid DP |

---

## 💻 Technique 4: Li Chao Tree

### Theory

**Problem:** Dynamic CHT where lines can be added in any order and queries are online.

**Li Chao Tree:** Segment tree variant that stores best line for each range.

**Complexity:**
- Insert line: O(log C) where C is coordinate range
- Query: O(log C)

### Implementation

```python
class LiChaoTree:
    """
    Dynamic Convex Hull Trick using segment tree.
    
    Handles:
    - Lines added in any order (no monotonicity required)
    - Online queries
    - Point updates
    """
    def __init__(self, x_min, x_max):
        self.x_min = x_min
        self.x_max = x_max
        self.tree = {}  # Sparse segment tree
    
    def _eval(self, line, x):
        """Evaluate line at x."""
        if line is None:
            return float('inf')
        m, b = line
        return m * x + b
    
    def _better(self, l1, l2, x):
        """Return better line at point x."""
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        return l1 if self._eval(l1, x) <= self._eval(l2, x) else l2
    
    def add_line(self, m, b, node_id=1, l=None, r=None):
        """
        Add line y = mx + b.
        
        Time: O(log C)
        """
        if l is None:
            l, r = self.x_min, self.x_max
        
        mid = (l + r) // 2
        line = (m, b)
        
        # Get current line at this node
        curr = self.tree.get(node_id)
        
        # Base case: leaf or no current line
        if l == r:
            self.tree[node_id] = self._better(curr, line, l)
            return
        
        if curr is None:
            self.tree[node_id] = line
            return
        
        # Determine which line is better at mid
        curr_better = self._eval(curr, mid) <= self._eval(line, mid)
        
        # Keep better line at mid
        if not curr_better:
            curr, line = line, curr
            self.tree[node_id] = curr
        
        # Recursively insert the other line
        curr_left_better = self._eval(curr, l) <= self._eval(line, l)
        
        if not curr_left_better:
            # Line better on left, recurse left
            self.add_line(line[0], line[1], 2 * node_id, l, mid)
        else:
            # Line better on right, recurse right
            self.add_line(line[0], line[1], 2 * node_id + 1, mid + 1, r)
    
    def query(self, x, node_id=1, l=None, r=None):
        """
        Find minimum value at x.
        
        Time: O(log C)
        """
        if l is None:
            l, r = self.x_min, self.x_max
        
        if node_id not in self.tree:
            return float('inf')
        
        result = self._eval(self.tree[node_id], x)
        
        if l == r:
            return result
        
        mid = (l + r) // 2
        
        if x <= mid:
            return min(result, self.query(x, 2 * node_id, l, mid))
        else:
            return min(result, self.query(x, 2 * node_id + 1, mid + 1, r))
```

### Problems (Li Chao Tree)

| # | Problem | Difficulty | Why Li Chao |
|:-:|---------|-----------|-------------|
| [CF 932F](https://codeforces.com/contest/932/problem/F) | Tree DP | ⭐⭐⭐⭐⭐ | Dynamic line insertion |

---

## 💻 Technique 5: Divide & Conquer Optimization

### Theory

**Condition:** Monotone optimal split point
```
opt[i][j] ≤ opt[i][j+1]
```

This is satisfied when cost matrix satisfies **Monge property**.

**Monge Property (Quadrangle Inequality):**
```
cost[a][c] + cost[b][d] ≤ cost[a][d] + cost[b][c]
for all a ≤ b ≤ c ≤ d
```

**Complexity:** O(n²k) → O(nk log n)

### Implementation

```python
def divide_conquer_dp(arr, K):
    """
    Partition array into exactly K groups minimizing cost.
    
    dp[k][i] = min cost to partition arr[0:i+1] into k groups
    dp[k][i] = min(dp[k-1][j] + cost[j+1][i]) for j < i
    
    With Monge property: opt[k][i] ≤ opt[k][i+1]
    
    Standard: O(n²K)
    Optimized: O(nK log n)
    """
    n = len(arr)
    
    # Precompute costs O(n²)
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            # Example: cost = sum of elements
            cost[i][j] = sum(arr[i:j+1])
    
    # DP table
    dp = [[float('inf')] * n for _ in range(K + 1)]
    
    # Base case: 0 groups for 0 elements
    for i in range(n):
        dp[1][i] = cost[0][i]
    
    def solve(k, left, right, opt_left, opt_right):
        """
        Compute dp[k][left:right+1].
        
        Know that opt[k][i] is in [opt_left, opt_right].
        """
        if left > right:
            return
        
        mid = (left + right) // 2
        best_cost = float('inf')
        best_opt = opt_left
        
        # Find best split for dp[k][mid]
        for j in range(opt_left, min(mid, opt_right) + 1):
            curr = dp[k - 1][j] + cost[j + 1][mid]
            if curr < best_cost:
                best_cost = curr
                best_opt = j
        
        dp[k][mid] = best_cost
        
        # Recurse on halves with tighter bounds
        solve(k, left, mid - 1, opt_left, best_opt)
        solve(k, mid + 1, right, best_opt, opt_right)
    
    # Compute each level
    for k in range(2, K + 1):
        solve(k, 0, n - 1, 0, n - 1)
    
    return dp[K][n - 1]
```

### Visual Example

```
Array: [1, 2, 3, 4, 5], K = 2

Standard DP: For each (k, i), try all j < i
┌─────────────────────────────────┐
│ dp[2][4] = ?                     │
│                                  │
│ Try j=0: dp[1][0] + cost[1][4]  │
│ Try j=1: dp[1][1] + cost[2][4]  │
│ Try j=2: dp[1][2] + cost[3][4]  │
│ Try j=3: dp[1][3] + cost[4][4]  │
└─────────────────────────────────┘

D&C Optimization: Binary search on optimal j
┌──────────────────────────────────┐
│ opt[2][0] ≤ opt[2][2] ≤ opt[2][4] │
│                                   │
│ Compute mid=2 first, find opt    │
│ Use opt to bound left/right      │
│                                   │
│ Left: opt[2][0..1] ∈ [0, opt[2]] │
│ Right: opt[2][3..4] ∈ [opt[2], 4]│
└───────────────────────────────────┘

Reduces O(n²) work to O(n log n) per level!
```

### Problems (Divide & Conquer)

| # | Problem | Difficulty | Property |
|:-:|---------|-----------|----------|
| 410 | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | ⭐⭐⭐⭐ | Minimize maximum |
| 1478 | [Allocate Mailboxes](https://leetcode.com/problems/allocate-mailboxes/) | ⭐⭐⭐⭐ | Median cost (Monge) |
| 1335 | [Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) | ⭐⭐⭐⭐ | Daily max cost |

---

## 💻 Technique 6: Knuth's Optimization

### Theory

**Conditions (both required):**
1. **Quadrangle Inequality:**
   ```
   cost[a][c] + cost[b][d] ≤ cost[a][d] + cost[b][c]
   for a ≤ b ≤ c ≤ d
   ```

2. **Monotonicity:**
   ```
   cost[b][c] ≤ cost[a][d] for a ≤ b ≤ c ≤ d
   ```

**Result:** `opt[i][j-1] ≤ opt[i][j] ≤ opt[i+1][j]`

**Complexity:** O(n³) → O(n²)

### Implementation

```python
def knuth_optimization(arr):
    """
    Optimal substructure with range costs.
    
    Recurrence:
    dp[i][j] = min(dp[i][k] + dp[k+1][j] + cost[i][j])
               for k ∈ [i, j-1]
    
    With Knuth: k ∈ [opt[i][j-1], opt[i+1][j]]
    
    Standard: O(n³)
    Optimized: O(n²)
    """
    n = len(arr)
    
    # Precompute costs
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            cost[i][j] = sum(arr[i:j+1])
    
    # Verify quadrangle inequality (optional check)
    def check_quadrangle():
        for a in range(n):
            for b in range(a, n):
                for c in range(b, n):
                    for d in range(c, n):
                        if cost[a][c] + cost[b][d] > cost[a][d] + cost[b][c]:
                            return False
        return True
    
    # DP with optimization
    dp = [[float('inf')] * n for _ in range(n)]
    opt = [[0] * n for _ in range(n)]
    
    # Base case: single elements
    for i in range(n):
        dp[i][i] = cost[i][i]
        opt[i][i] = i
    
    # Fill by increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Search range: [opt[i][j-1], opt[i+1][j]]
            start = opt[i][j - 1] if j > i else i
            end = opt[i + 1][j] if i + 1 < n else j - 1
            
            for k in range(start, min(end, j - 1) + 1):
                curr = dp[i][k] + dp[k + 1][j] + cost[i][j]
                if curr < dp[i][j]:
                    dp[i][j] = curr
                    opt[i][j] = k
    
    return dp[0][n - 1]
```

### Proof Sketch

**Why opt is monotone:**

```
Assume opt[i][j] < opt[i][j-1]  (contradiction)

Let k* = opt[i][j], k' = opt[i][j-1]
So k* < k'

By definition:
dp[i][k*] + dp[k*+1][j] + cost[i][j]  (optimal for [i,j])
< dp[i][k'] + dp[k'+1][j] + cost[i][j]

Also:
dp[i][k'] + dp[k'+1][j-1] + cost[i][j-1]  (optimal for [i,j-1])
≤ dp[i][k*] + dp[k*+1][j-1] + cost[i][j-1]

Adding these inequalities and using quadrangle inequality
leads to contradiction!

Therefore: opt[i][j-1] ≤ opt[i][j]
```

### Problems (Knuth's Optimization)

| # | Problem | Difficulty | Structure |
|:-:|---------|-----------|-----------|
| 312 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | ⭐⭐⭐⭐ | Interval DP |
| 1000 | [Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/) | ⭐⭐⭐⭐ | K-merge groups |
| 1547 | [Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) | ⭐⭐⭐⭐ | Range cut cost |
| 664 | [Strange Printer](https://leetcode.com/problems/strange-printer/) | ⭐⭐⭐⭐ | Printing intervals |
| 546 | [Remove Boxes](https://leetcode.com/problems/remove-boxes/) | ⭐⭐⭐⭐⭐ | 3D DP |

---

## 💻 Technique 7: SOS (Sum over Subsets) DP

### Theory

**Problem:** For each mask, compute sum over all its subsets.

```
dp[mask] = Σ f[submask] for all submask ⊆ mask
```

**Naive:** O(3ⁿ) - for each mask, iterate all 2ⁿ subsets
**SOS DP:** O(n·2ⁿ) - iterate bits

### Implementation

```python
def sos_dp(arr):
    """
    Sum Over Subsets Dynamic Programming.
    
    Given f[mask] for all masks in [0, 2^n),
    compute dp[mask] = sum(f[submask]) for all submask ⊆ mask
    
    Naive: O(3^n)
    SOS DP: O(n * 2^n)
    """
    n = len(arr)
    MAX_MASK = 1 << n
    
    # Initialize with given values
    dp = [[0] * MAX_MASK for _ in range(n + 1)]
    
    for mask in range(MAX_MASK):
        dp[0][mask] = arr[mask]
    
    # Iterate over bits
    for i in range(n):
        for mask in range(MAX_MASK):
            dp[i + 1][mask] = dp[i][mask]
            
            # If i-th bit is set, add contribution without i-th bit
            if mask & (1 << i):
                dp[i + 1][mask] += dp[i][mask ^ (1 << i)]
    
    return dp[n]
```

### Space-Optimized SOS DP

```python
def sos_dp_optimized(arr):
    """
    Space-optimized version: O(2^n) space.
    """
    n = len(arr).bit_length() - 1
    MAX_MASK = 1 << n
    
    dp = arr[:]
    
    for i in range(n):
        for mask in range(MAX_MASK):
            if mask & (1 << i):
                dp[mask] += dp[mask ^ (1 << i)]
    
    return dp
```

### Visual Example

```
n = 3, arr = [1, 2, 3, 4, 5, 6, 7, 8]
Indices:     000 001 010 011 100 101 110 111

Goal: dp[mask] = sum of arr[submask] for submask ⊆ mask

Example: mask = 101 (binary)
Subsets: 000, 001, 100, 101
dp[101] = arr[000] + arr[001] + arr[100] + arr[101]
        = 1 + 2 + 5 + 6 = 14

SOS DP Process:
i=0 (bit 0):
  dp[001] += dp[000]  (1+2=3)
  dp[011] += dp[010]  (3+4=7)
  dp[101] += dp[100]  (5+6=11)
  dp[111] += dp[110]  (7+8=15)

i=1 (bit 1):
  dp[010] += dp[000]  (3+1=4)
  dp[011] += dp[001]  (7+3=10)
  dp[110] += dp[100]  (7+5=12)
  dp[111] += dp[101]  (15+11=26)

i=2 (bit 2):
  dp[100] += dp[000]  (5+1=6)
  dp[101] += dp[001]  (11+3=14)
  dp[110] += dp[010]  (12+4=16)
  dp[111] += dp[011]  (26+10=36)

Final: dp = [1, 3, 4, 10, 6, 14, 16, 36]
```

### Problems (SOS DP)

| # | Problem | Difficulty | Application |
|:-:|---------|-----------|-------------|
| 898 | [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/) | ⭐⭐ | Count distinct ORs |
| 1986 | [Minimum Number of Work Sessions](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) | ⭐⭐⭐ | Partition with bitmask |

---

## 💻 Technique 8: Matrix Exponentiation

### Theory

**Problem:** Linear recurrence with large n

```
f(n) = c₁·f(n-1) + c₂·f(n-2) + ... + cₖ·f(n-k)
```

**Matrix Form:**
```
[f(n)  ]   [c₁ c₂ ... cₖ] [f(n-1)]
[f(n-1)]   [1  0  ... 0 ] [f(n-2)]
[f(n-2)] = [0  1  ... 0 ] [f(n-3)]
[...   ]   [...       ...] [...   ]
[f(n-k+1)] [0  0  ... 0 ] [f(n-k)]
```

**Solution:** Compute Aⁿ using binary exponentiation

**Complexity:** O(n) → O(k³ log n)

### Implementation

```python
class MatrixExponentiation:
    def __init__(self, k):
        """k = size of matrix (dimension)."""
        self.k = k
        self.MOD = 10**9 + 7
    
    def multiply(self, A, B):
        """Matrix multiplication O(k³)."""
        k = len(A)
        C = [[0] * k for _ in range(k)]
        
        for i in range(k):
            for j in range(k):
                for p in range(k):
                    C[i][j] = (C[i][j] + A[i][p] * B[p][j]) % self.MOD
        
        return C
    
    def power(self, A, n):
        """
        Compute A^n using binary exponentiation.
        
        Time: O(k³ log n)
        """
        k = len(A)
        
        # Identity matrix
        result = [[1 if i == j else 0 for j in range(k)] 
                  for i in range(k)]
        
        base = [row[:] for row in A]  # Copy
        
        while n > 0:
            if n % 2 == 1:
                result = self.multiply(result, base)
            base = self.multiply(base, base)
            n //= 2
        
        return result
    
    def fibonacci(self, n):
        """
        Compute n-th Fibonacci number.
        
        f(n) = f(n-1) + f(n-2)
        
        Matrix: [f(n)  ] = [1 1] [f(n-1)]
                [f(n-1)]   [1 0] [f(n-2)]
        """
        if n <= 1:
            return n
        
        A = [[1, 1], [1, 0]]
        A_n = self.power(A, n - 1)
        
        # [f(n), f(n-1)]^T = A^(n-1) * [f(1), f(0)]^T
        return A_n[0][0]  # f(1)=1, f(0)=0
    
    def tribonacci(self, n):
        """
        f(n) = f(n-1) + f(n-2) + f(n-3)
        
        Matrix: [f(n)  ]   [1 1 1] [f(n-1)]
                [f(n-1)] = [1 0 0] [f(n-2)]
                [f(n-2)]   [0 1 0] [f(n-3)]
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        A = [[1, 1, 1],
             [1, 0, 0],
             [0, 1, 0]]
        
        A_n = self.power(A, n - 2)
        
        # f(2)=1, f(1)=1, f(0)=0
        return A_n[0][0] + A_n[0][1]
```

### Problems (Matrix Exponentiation)

| # | Problem | Difficulty | Recurrence |
|:-:|---------|-----------|------------|
| 509 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | ⭐ | f(n) = f(n-1) + f(n-2) |
| 1137 | [N-th Tribonacci](https://leetcode.com/problems/n-th-tribonacci-number/) | ⭐ | f(n) = f(n-1) + f(n-2) + f(n-3) |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | ⭐ | Same as Fibonacci |
| 552 | [Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/) | ⭐⭐⭐⭐ | State machine |

---

## 💻 Technique 9: Aliens Trick (Wqs Binary Search)

### Theory

**Problem:** Partition into **exactly** k groups minimizing cost.

**Challenge:** "Exactly k" constraint makes DP expensive.

**Solution:** Binary search on penalty λ per group.

```
Define: g(λ) = min cost + λ × (number of groups)
Binary search λ until number of groups = k
```

**Complexity:** O(n²k) → O(n² log C)

### Implementation

```python
def aliens_trick(arr, k):
    """
    Partition into exactly k groups minimizing cost.
    
    Trick: Binary search on Lagrange multiplier λ.
    
    Standard: O(n²k) 
    Optimized: O(n² log C) where C = max cost
    """
    n = len(arr)
    
    def dp_with_penalty(lam):
        """
        Solve without "exactly k" constraint.
        
        Add penalty λ for each group.
        Returns: (num_groups, cost - k*λ)
        """
        dp = [float('inf')] * n
        count = [0] * n
        
        for i in range(n):
            # Option 1: Start new group at i
            cost_i = compute_cost(arr[0:i+1]) + lam
            dp[i] = cost_i
            count[i] = 1
            
            # Option 2: Extend from previous
            for j in range(i):
                cost_j = dp[j] + compute_cost(arr[j+1:i+1]) + lam
                if cost_j < dp[i]:
                    dp[i] = cost_j
                    count[i] = count[j] + 1
        
        return count[n-1], dp[n-1]
    
    def compute_cost(subarray):
        """Example: sum of squares."""
        return sum(x**2 for x in subarray)
    
    # Binary search on λ
    left, right = 0, sum(x**2 for x in arr)
    
    best_cost = float('inf')
    
    while right - left > 1e-9:
        mid = (left + right) / 2
        groups, cost = dp_with_penalty(mid)
        
        if groups <= k:
            # Too few groups, decrease penalty
            right = mid
            if groups == k:
                best_cost = cost + k * mid
        else:
            # Too many groups, increase penalty
            left = mid
    
    return best_cost
```

### Why It Works

**Intuition:** Cost curve is **convex** in number of groups.

```
Cost
  │     ╱
  │    ╱
  │   ╱
  │  ╱    ← Convex envelope
  │ ╱
  │╱
  └────────────── # Groups
  1  2  3  4  5

For each λ, find tangent point
Binary search λ to hit k groups
```

**Formal:** Lagrangian relaxation + convexity guarantee convergence.

### Problems (Aliens Trick)

| # | Problem | Difficulty | Constraint |
|:-:|---------|-----------|-----------|
| 410 | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | ⭐⭐⭐⭐ | Exactly m subarrays |
| 1478 | [Allocate Mailboxes](https://leetcode.com/problems/allocate-mailboxes/) | ⭐⭐⭐⭐ | Exactly k mailboxes |

---

## 💻 Technique 10: Bitmasking DP Optimizations

### Theory

**Standard Bitmask DP:** O(n·2ⁿ) or O(n²·2ⁿ)

**Optimizations:**
1. **Profile DP:** O(n·m·2^m) for n×m grid
2. **Broken Profile:** Faster constant factor
3. **Inclusion-Exclusion:** Reduce states

### Implementation (Broken Profile DP)

```python
def tiling_2xn(n):
    """
    Count ways to tile 2×n board with 1×2 dominoes.
    
    Profile DP: Track which cells in current column are filled.
    
    Standard: O(2^(2n))
    Optimized: O(n·2²) = O(4n)
    """
    # State: bitmask of current column (2 bits)
    # 00: both empty, 01: top filled, 10: bottom filled, 11: both filled
    
    dp = [0] * 4
    dp[0] = 1  # Both empty initially
    
    for col in range(n):
        next_dp = [0] * 4
        
        for mask in range(4):
            if dp[mask] == 0:
                continue
            
            # Try all transitions
            # 1. Place vertical domino (both become filled)
            if mask == 0:
                next_dp[3] += dp[mask]
            
            # 2. Place two horizontal dominoes
            if mask == 0:
                next_dp[0] += dp[mask]
            
            # 3. Top filled, place horizontal at bottom
            if mask == 1:
                next_dp[2] += dp[mask]
            
            # 4. Bottom filled, place horizontal at top
            if mask == 2:
                next_dp[1] += dp[mask]
            
            # 5. Both filled, move to next column
            if mask == 3:
                next_dp[0] += dp[mask]
        
        dp = next_dp
    
    return dp[3]  # Both cells filled in last column
```

---

## 💻 Technique 11: DP on Trees Optimizations

### Technique: Rerooting

**Problem:** Compute DP for each node as root.

**Naive:** Run tree DP from each node - O(n²)
**Rerooting:** Compute answer for all roots in O(n)

### Implementation

```python
def rerooting_dp(graph, n):
    """
    Compute tree DP with each node as root.
    
    Standard: O(n²) - run DP from each root
    Rerooting: O(n) - smart reuse of computation
    
    Example: Max distance from each node
    """
    # Step 1: DFS from arbitrary root (node 0)
    dp_down = [0] * n  # Max distance going down
    
    def dfs_down(u, parent):
        max_dist = 0
        for v in graph[u]:
            if v != parent:
                max_dist = max(max_dist, 1 + dfs_down(v, u))
        dp_down[u] = max_dist
        return dp_down[u]
    
    dfs_down(0, -1)
    
    # Step 2: DFS to reroot
    dp_up = [0] * n  # Max distance going up
    answer = [0] * n
    
    def dfs_up(u, parent, up_value):
        dp_up[u] = up_value
        answer[u] = max(dp_down[u], dp_up[u])
        
        # Find two largest children
        children_values = []
        for v in graph[u]:
            if v != parent:
                children_values.append((dp_down[v] + 1, v))
        
        children_values.sort(reverse=True)
        
        for v in graph[u]:
            if v != parent:
                # Compute up value for child v
                # Best path through u to other subtree
                if children_values[0][1] == v:
                    best_other = children_values[1][0] if len(children_values) > 1 else 0
                else:
                    best_other = children_values[0][0]
                
                new_up = max(up_value, best_other) + 1
                dfs_up(v, u, new_up)
    
    dfs_up(0, -1, 0)
    
    return answer
```

---

## 📊 Complete Problem List

### 🌟 Must-Solve (Top 20)

| # | Problem | Optimization | Difficulty |
|:-:|---------|-------------|-----------|
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Monotonic Deque | ⭐⭐⭐ |
| 1425 | [Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/) | Monotonic Queue | ⭐⭐⭐⭐ |
| 1696 | [Jump Game VI](https://leetcode.com/problems/jump-game-vi/) | Monotonic Queue | ⭐⭐⭐ |
| 410 | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | D&C or Aliens | ⭐⭐⭐⭐ |
| 1478 | [Allocate Mailboxes](https://leetcode.com/problems/allocate-mailboxes/) | D&C | ⭐⭐⭐⭐ |
| 312 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Knuth | ⭐⭐⭐⭐ |
| 1000 | [Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/) | Knuth | ⭐⭐⭐⭐ |
| 1547 | [Minimum Cost to Cut Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) | Knuth | ⭐⭐⭐⭐ |
| 664 | [Strange Printer](https://leetcode.com/problems/strange-printer/) | Knuth | ⭐⭐⭐⭐ |
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Space Opt | ⭐⭐ |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Space Opt | ⭐⭐ |
| 509 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Matrix Exp | ⭐ |
| 1137 | [N-th Tribonacci](https://leetcode.com/problems/n-th-tribonacci-number/) | Matrix Exp | ⭐ |
| 898 | [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/) | SOS DP | ⭐⭐ |
| 1687 | [Delivering Boxes](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/) | CHT | ⭐⭐⭐⭐ |
| 1499 | [Max Value of Equation](https://leetcode.com/problems/max-value-of-equation/) | Monotonic Queue | ⭐⭐⭐⭐ |
| 862 | [Shortest Subarray Sum ≥ K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | Monotonic Deque | ⭐⭐⭐⭐ |
| 1335 | [Minimum Difficulty](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) | D&C | ⭐⭐⭐⭐ |
| 546 | [Remove Boxes](https://leetcode.com/problems/remove-boxes/) | Knuth 3D | ⭐⭐⭐⭐⭐ |
| 552 | [Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/) | Matrix Exp | ⭐⭐⭐⭐ |

### Additional Problems (40+)

**Monotonic Queue (10):**
- 739. Daily Temperatures
- 901. Online Stock Span
- 907. Sum of Subarray Minimums
- 1475. Final Prices With Special Discount
- 1673. Find Most Competitive Subsequence

**Space Optimization (8):**
- 198. House Robber
- 213. House Robber II
- 300. Longest Increasing Subsequence
- 322. Coin Change
- 416. Partition Equal Subset Sum
- 494. Target Sum
- 518. Coin Change II
- 1049. Last Stone Weight II

**Knuth's Optimization (6):**
- 96. Unique Binary Search Trees
- 95. Unique Binary Search Trees II
- 1039. Minimum Score Triangulation
- 1312. Minimum Insertion Steps for Palindrome

**Matrix Exponentiation (5):**
- 70. Climbing Stairs
- 91. Decode Ways
- 746. Min Cost Climbing Stairs
- 790. Domino and Tromino Tiling

**Bitmask DP (8):**
- 464. Can I Win
- 473. Matchsticks to Square
- 526. Beautiful Arrangement
- 698. Partition to K Equal Sum Subsets
- 847. Shortest Path Visiting All Nodes
- 943. Find Shortest Superstring
- 980. Unique Paths III
- 1986. Minimum Work Sessions

---

## 🎯 Decision Tree

```
┌─────────────────────────────────────────────┐
│ Identify DP bottleneck                     │
└──────────────┬──────────────────────────────┘
               │
      ┌────────┴────────┐
      │ What type?      │
      └────────┬────────┘
               │
   ┌───────────┼───────────┐
   │           │           │
   ▼           ▼           ▼
┌─────────┐ ┌─────────┐ ┌──────────┐
│ States  │ │ Trans-  │ │ Linear   │
│ too big?│ │ itions? │ │ recur?   │
└────┬────┘ └────┬────┘ └────┬─────┘
     │           │           │
     ▼           ▼           ▼
 Space Opt   Range min/  Matrix Exp
 SOS DP      max? →      
 Bitmask     Mono Queue  
             
             Linear      Exactly k?
             func? →     → Aliens
             CHT/        
             Li Chao     
             
             Monge? →    Quad ineq?
             D&C DP      → Knuth
```

---

## 📊 Practice Roadmap (4 Weeks)

### Week 1: Foundation
**Goal:** Master basic optimizations

- [ ] 72. Edit Distance (Space)
- [ ] 1143. LCS (Space)
- [ ] 239. Sliding Window Max (Monotonic)
- [ ] 1425. Constrained Sum (Monotonic Queue)
- [ ] 1696. Jump Game VI (Monotonic Queue)

### Week 2: Advanced Techniques
**Goal:** CHT and D&C

- [ ] 1499. Max Value of Equation (Transform + Deque)
- [ ] 862. Shortest Subarray (Deque)
- [ ] 410. Split Array (D&C or Aliens)
- [ ] 1478. Allocate Mailboxes (D&C)
- [ ] 1335. Minimum Difficulty (D&C)

### Week 3: Knuth & Matrix
**Goal:** Complex optimizations

- [ ] 312. Burst Balloons (Knuth)
- [ ] 1000. Merge Stones (Knuth)
- [ ] 1547. Cut Stick (Knuth)
- [ ] 664. Strange Printer (Knuth)
- [ ] 509/1137. Fibonacci/Tribonacci (Matrix)
- [ ] 552. Attendance Record (Matrix)

### Week 4: Special Techniques
**Goal:** SOS, Aliens, Bitmask

- [ ] 898. Bitwise ORs (SOS)
- [ ] 1986. Work Sessions (Bitmask)
- [ ] 847. Shortest Path All Nodes (Bitmask)
- [ ] 546. Remove Boxes (3D Knuth) ⭐
- [ ] Practice mixed problems

---

## 🔍 Interview Tips

### Recognition Patterns

| If you see... | Consider... |
|---------------|-------------|
| "minimize/maximize over window of size k" | Monotonic Queue |
| "partition into exactly k groups" | D&C DP or Aliens Trick |
| "range DP with cost[i][j]" | Check Knuth conditions |
| "O(n²) transitions, all linear functions" | Convex Hull Trick |
| "iterate all subsets/submasks" | SOS DP |
| "large n, linear recurrence" | Matrix Exponentiation |
| "2D DP, only use previous row" | Space Optimization |

### Common Mistakes

❌ **Wrong monotonic deque order** - Increasing for min, decreasing for max
❌ **Not checking Monge/Quadrangle inequality** - Optimizations won't work
❌ **Off-by-one in Knuth bounds** - opt[i][j-1] vs opt[i+1][j]
❌ **Incorrect line addition order in CHT** - Must be sorted by slope
❌ **Forgetting base cases in recursion** - D&C needs proper initialization
❌ **SOS DP wrong iteration order** - Must iterate bits, then masks

### Debugging Strategies

1. **Verify optimization conditions**
   - Print cost matrix, check Monge
   - Verify slope ordering for CHT

2. **Test on small inputs**
   - Compare optimized vs naive
   - Check edge cases (k=1, k=n)

3. **Visualize transitions**
   - Draw state graph
   - Track opt values in Knuth

---

## 📚 References & Resources

| Topic | Resource | Link |
|-------|----------|------|
| **Monotonic Queue** | CP-Algorithms | [Link](https://cp-algorithms.com/data_structures/stack_queue_modification.html) |
| **Convex Hull Trick** | WCIPEG | [Link](https://wcipeg.com/wiki/Convex_hull_trick) |
| **D&C Optimization** | Codeforces | [Link](https://codeforces.com/blog/entry/8219) |
| **Knuth Optimization** | IOI Paper | [Link](https://www.iarcs.org.in/inoi/online-study-material/topics/dp-opt.php) |
| **SOS DP** | Codeforces | [Link](https://codeforces.com/blog/entry/45223) |
| **Aliens Trick** | Codeforces | [Link](https://codeforces.com/blog/entry/49691) |
| **Li Chao Tree** | CP-Algorithms | [Link](https://cp-algorithms.com/geometry/convex_hull_trick.html) |

---

## 💡 Key Insights

> **Monotonic Queue:** Each element enters and leaves deque exactly once → O(1) amortized.

> **CHT Geometry:** Lines form convex hull. Query = find tangent at x. Lower envelope for min, upper for max.

> **Monge Property:** Intuition = "crossing is bad". Closer splits are better.

> **Quadrangle Inequality:** Merging adjacent ranges cheaper than crossing ranges.

> **SOS DP Magic:** Process one bit at a time. Transforms O(3ⁿ) to O(n·2ⁿ).

> **Aliens Trick:** Add cost penalty λ per group. Binary search λ to hit exactly k groups.

> **Matrix Power:** Linear recurrence → Matrix multiplication. Binary exp gives O(log n).

> **Space Optimization:** If dp[i] only depends on dp[i-1], keep 2 rows instead of n.

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← Approximation Algorithms](../39_approximation_algorithms/README.md) | **DP Optimizations** | 🏁 **DSA Journey Complete!** 🎉 |

---

<div align="center">

## 🎓 Congratulations!

You've mastered the most advanced DP optimization techniques!

**Your DP Arsenal:**
- 🎯 11 Optimization Techniques
- 💻 Production-Ready Implementations
- 📝 60+ LeetCode Problems
- 🧮 Mathematical Proofs
- ⚡ From O(n³) to O(n log n)

**These techniques separate good programmers from great ones!** 🚀

Continue practicing and ace those competitive programming contests and interviews!

</div>
