---
layout: default
title: "Basic BIT Operations"
parent: "Fenwick Tree (BIT)"
grand_parent: "Advanced Trees"
nav_order: 1
permalink: /27_advanced_trees/03_fenwick_tree/01_basic_bit/
---

<div align="center">

# 🔢 Basic BIT Operations

### *Basic BIT Operations*



<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-6-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 📊 Visual Overview

<div align="center">
<img src="./images/basic-bit.png" alt="Basic BIT Operations" width="100%">
</div>

---

## 🎯 At a Glance

| | |
|:---|:---|
| **Difficulty** | Medium |
| **Problems** | 6 |

> **How to use this page:** Start with the visual overview, scan **At a Glance**, then work through theory → walkthroughs → code.

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← Fenwick Tree](../README.md) | **01. Basic BIT** | [02. Inversion Counting →](../02_inversion_counting/README.md) |

---

## 📐 Core Concepts

### Point Update + Range Query

**Most common BIT usage:**

- Update single element: `O(log n)`
- Query prefix sum: `O(log n)`
- Query range sum: Two prefix sums

### Range Update + Point Query

**Using difference array:**

- Update range: `O(log n)`
- Query point: `O(log n)`

---

## 💻 Problems & Solutions

### 1. Range Sum Query - Mutable (LeetCode 307)

**Problem:** Support update and range sum queries.

![Range Sum Query Mutable](./images/range-sum-query-mutable.png)


---

### 2. Range Addition (LeetCode 370)

**Problem:** Efficiently handle multiple range additions.

![Range Addition](./images/range-addition.png)


---

### 3. Range Sum Query - Immutable (LeetCode 303)

**Problem:** Prefix sum (BIT overkill but good practice).

![Prefix Sum Query](./images/prefix-sum-query.png)


---

### 4. Design Stack With Increment Operation (LeetCode 1381)

**Problem:** Stack with efficient range increment.

![Stack With Increment](./images/stack-with-increment.png)


---

### 5. Process Restricted Friend Requests (LeetCode 2076)

**Problem:** Track friendships with restrictions.

![Friend Requests](./images/friend-requests.png)


---

### 6. Number of Subsequences (Custom)

**Problem:** Count subsequences with sum in range.

![Subsequences in Range](./images/subsequences-in-range.png)


---

## 📊 Problem Summary

| Problem | Difficulty | Key Technique |
|---------|:----------:|---------------|
| Range Sum Query - Mutable | Medium | Point update + range query |
| Range Addition | Medium | Difference array |
| Range Sum Query - Immutable | Easy | Prefix sum |
| Stack With Increment | Medium | Lazy propagation |
| Friend Requests | Hard | Union-Find + validation |
| Subsequences in Range | Hard | DP + BIT |

---

## 💡 Key Patterns

1. **Point Update + Range Query:** Standard BIT

2. **Range Update + Point Query:** Difference array + BIT

3. **Lazy Updates:** Defer computation until needed

4. **Coordinate Compression:** Map large values to small indices

5. **Multiple BITs:** Track different properties simultaneously

---
