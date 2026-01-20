---
layout: default
title: "1D DP"
parent: "Dynamic Programming"
nav_order: 1
permalink: /18_dynamic_programming/01_1d_dp/
---

<div align="center">

# 📈 1D Dynamic Programming

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Medium-green?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-15+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [🏠 DP Home](../README.md) | **01. 1D DP** | [02. 2D DP →](../02_2d_dp/README.md) |

---

## 📊 Visual Guide

<div align="center">
  <img src="images/1d-dp.svg" alt="1D DP Visualization" width="100%">
</div>

---

## 📐 Mathematical Foundations

### 1️⃣ General Form

```math
dp[i] = f(dp[i-1], dp[i-2], \ldots, dp[0])

```

**Space optimization:** If only last k values needed, use O(k) space.

---

### 2️⃣ Common Recurrences

| Problem | Recurrence |
|---------|------------|
| Fibonacci | $dp[i] = dp[i-1] + dp[i-2]$ |
| Climbing Stairs | $dp[i] = dp[i-1] + dp[i-2]$ |
| House Robber | $dp[i] = \max(dp[i-1], dp[i-2] + nums[i])$ |
| Coin Change | $dp[a] = \min(dp[a-c] + 1)$ for all coins $c$ |

---

## 💻 Code Implementations

```python
def climbStairs(n: int) -> int:
    """
    Climbing Stairs (LeetCode 70).
    
    dp[i] = ways to reach step i
    
    Time: O(n), Space: O(1)
    """
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr

def rob(nums: list[int]) -> int:
    """
    House Robber (LeetCode 198).
    
    Can't rob adjacent houses.
    
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev, curr = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        prev, curr = curr, max(curr, prev + nums[i])
    return curr

def coinChange(coins: list[int], amount: int) -> int:
    """
    Coin Change (LeetCode 322).
    
    Minimum coins to make amount.
    
    Time: O(amount × n), Space: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def lengthOfLIS(nums: list[int]) -> int:
    """
    Longest Increasing Subsequence (LeetCode 300).
    
    O(n²) DP approach.
    
    Time: O(n²), Space: O(n)
    """
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def maxSubArray(nums: list[int]) -> int:
    """
    Maximum Subarray / Kadane's (LeetCode 53).
    
    Time: O(n), Space: O(1)
    """
    max_sum = curr_sum = nums[0]
    
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

def wordBreak(s: str, wordDict: list[str]) -> bool:
    """
    Word Break (LeetCode 139).
    
    dp[i] = can segment s[0:i]
    
    Time: O(n²), Space: O(n)
    """
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]

```

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Recurrence | Time | Space |
|:-:|---------|------------|:----:|:-----:|
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | dp[i] = dp[i-1] + dp[i-2] | O(n) | O(1) |
| 121 | [Best Time to Buy Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Track min | O(n) | O(1) |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | max(skip, take) | O(n) | O(1) |
| 746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | min cost | O(n) | O(1) |

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Kadane | O(n) | O(1) |
| 91 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | dp[i-1] + dp[i-2] | O(n) | O(1) |
| 139 | [Word Break](https://leetcode.com/problems/word-break/) | Check all splits | O(n²) | O(n) |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Track min/max | O(n) | O(1) |
| 213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Circular | O(n) | O(1) |
| 300 | [LIS](https://leetcode.com/problems/longest-increasing-subsequence/) | DP or Binary | O(n log n) | O(n) |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | Unbounded | O(n×a) | O(a) |

---

## 📚 References

| Resource | Link |
|----------|------|
| **1D DP** | [GeeksforGeeks](https://www.geeksforgeeks.org/dynamic-programming/) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [🏠 DP Home](../README.md) | **01. 1D DP** | [02. 2D DP →](../02_2d_dp/README.md) |
