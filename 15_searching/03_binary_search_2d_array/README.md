---
layout: default
title: "2D Array Search"
parent: "Searching"
nav_order: 3
permalink: /15_searching/03_binary_search_2d_array/
---

<div align="center">

# 🔢 Binary Search in 2D Arrays

![2D Matrix Search](./images/2d-matrix-search.svg)

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-5+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 02. BS on Answer](../02_binary_search_on_answer/README.md) | **03. 2D Array** | [04. Rotated Array →](../04_binary_search_rotated_array/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Flattened 2D Array

If matrix is row-major sorted:

```math
\text{1D index } k \Leftrightarrow \text{2D } (k / n, k \% n)
T = O(\log(m \times n))

```

---

### 2️⃣ Staircase Search

For row-sorted and column-sorted matrix:

**Start from top-right (or bottom-left):**

- If target < current: go left

- If target > current: go down

```math
T = O(m + n)

```

---

### 3️⃣ Kth Smallest in Sorted Matrix

**Binary search on value, count elements ≤ mid:**

```math
\text{count}(x) = \sum_{i} \text{elements in row } i \leq x
T = O(n \log(\max - \min))

```

---

## 💻 Code Implementations

```python
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search a 2D Matrix (LeetCode 74).
    
    Matrix is row-major sorted (flatten to 1D).
    
    Time: O(log(mn)), Space: O(1)
    """
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n, mid % n
        val = matrix[row][col]
        
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def searchMatrix2(matrix: list[list[int]], target: int) -> bool:
    """
    Search a 2D Matrix II (LeetCode 240).
    
    Rows and columns sorted separately.
    Staircase search from top-right.
    
    Time: O(m + n), Space: O(1)
    """
    if not matrix:
        return False
    
    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1
    
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False

def kthSmallest(matrix: list[list[int]], k: int) -> int:
    """
    Kth Smallest Element in Sorted Matrix (LeetCode 378).
    
    Binary search on value, count elements <= mid.
    
    Time: O(n × log(max-min)), Space: O(1)
    """
    n = len(matrix)
    
    def countLessEqual(target):
        """Count elements <= target using staircase."""
        count = 0
        row, col = n - 1, 0
        
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1
        
        return count
    
    left, right = matrix[0][0], matrix[n-1][n-1]
    
    while left < right:
        mid = (left + right) // 2
        if countLessEqual(mid) < k:
            left = mid + 1
        else:
            right = mid
    
    return left

def countNegatives(grid: list[list[int]]) -> int:
    """
    Count Negative Numbers (LeetCode 1351).
    
    Staircase from bottom-left.
    
    Time: O(m + n), Space: O(1)
    """
    m, n = len(grid), len(grid[0])
    row, col = m - 1, 0
    count = 0
    
    while row >= 0 and col < n:
        if grid[row][col] < 0:
            count += n - col  # All right elements negative
            row -= 1
        else:
            col += 1
    
    return count

```

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 1351 | [Count Negative Numbers](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) | Staircase | O(m+n) | O(1) |

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Flatten | O(log mn) | O(1) |
| 240 | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) | Staircase | O(m+n) | O(1) |
| 378 | [Kth Smallest in Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | BS + Count | O(n log d) | O(1) |

---

## 📊 2D Search Strategy

```
2D Matrix Search
       |
       +-- Row-major sorted → Flatten to 1D BS
       |
       +-- Row + Column sorted → Staircase O(m+n)
       |
       +-- Kth element → BS on value + count

```

---

## 📚 References

| Resource | Link |
|----------|------|
| **Matrix Search** | [GeeksforGeeks](https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 02. BS on Answer](../02_binary_search_on_answer/README.md) | **03. 2D Array** | [04. Rotated Array →](../04_binary_search_rotated_array/README.md) |
