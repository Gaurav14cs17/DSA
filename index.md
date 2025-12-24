---
layout: default
title: Home
nav_order: 1
description: "DSA - Data Structures and Algorithms comprehensive study guide with mathematical foundations"
permalink: /
---

<div align="center">

# 🎯 Data Structures & Algorithms

![DSA Banner](/assets/images/dsa-banner.svg)

<p class="fs-6 fw-300">
A comprehensive guide to mastering DSA with mathematical proofs, visual explanations, and LeetCode solutions.
</p>

![DSA](https://img.shields.io/badge/Topics-42-blue?style=for-the-badge)
![Problems](https://img.shields.io/badge/LeetCode-500+-green?style=for-the-badge)
![Author](https://img.shields.io/badge/Author-Gaurav_Goswami-purple?style=for-the-badge)

</div>

---

## 📐 Mathematical Foundation

This guide emphasizes **mathematical rigor** with:

- ✅ Formal definitions and theorems
- ✅ Complexity proofs
- ✅ Visual algorithm traces
- ✅ Decision trees for pattern selection

---

## 🗂️ Topics at a Glance

### 📦 Core Data Structures

<div class="topic-grid">

| Topic | Subtopics | Difficulty |
|:------|:---------:|:----------:|
| [📦 Arrays](./01_arrays/) | 5 | 🟢 |
| [📝 Strings](./02_strings/) | 4 | 🟢 |
| [🔗 Linked Lists](./03_linked_lists/) | 3 | 🟢 |
| [📚 Stacks](./04_stacks/) | 4 | 🟡 |
| [📬 Queues](./05_queues/) | 3 | 🟡 |
| [#️⃣ Hash Tables](./06_hash_tables/) | 3 | 🟢 |
| [🌲 Trees](./07_trees/) | 5 | 🟡 |
| [🔍 BST](./08_binary_search_trees/) | 3 | 🟡 |
| [⛰️ Heaps](./09_heaps/) | 4 | 🟡 |
| [🔗 Graphs](./10_graphs/) | 7 | 🔴 |
| [🔤 Tries](./11_tries/) | 3 | 🟡 |

</div>

### 🧮 Algorithms

| Topic | Key Concepts | Difficulty |
|:------|:-------------|:----------:|
| [📊 Sorting](./14_sorting/) | QuickSort, MergeSort, HeapSort | 🟢 |
| [🔍 Binary Search](./15_searching/) | Search on Answer, Rotated Arrays | 🟡 |
| [🔄 Recursion](./16_recursion/) | Base Case, Recursive Leap of Faith | 🟡 |
| [🔙 Backtracking](./17_backtracking/) | Subsets, Permutations, N-Queens | 🟡 |
| [🎯 Dynamic Programming](./18_dynamic_programming/) | Knapsack, LCS, State Machine | 🔴 |
| [🤑 Greedy](./19_greedy_algorithms/) | Interval Scheduling, Huffman | 🟡 |
| [✂️ Divide & Conquer](./20_divide_and_conquer/) | Merge Sort Pattern | 🟡 |
| [💻 Bit Manipulation](./21_bit_manipulation/) | XOR Tricks, Bitmasks | 🟡 |

### 🎯 Problem-Solving Patterns

| Pattern | When to Use | Difficulty |
|:--------|:------------|:----------:|
| [👆👇 Two Pointers](./22_two_pointers/) | Sorted arrays, pair finding | 🟢 |
| [🪟 Sliding Window](./23_sliding_window/) | Subarray/substring optimization | 🟡 |

---

## ⚡ Quick Reference

### Time Complexity Cheat Sheet

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

### Master Theorem

For $T(n) = aT(n/b) + f(n)$:

| Case | Condition | Complexity |
|:----:|:----------|:----------:|
| 1 | $f(n) = O(n^{\log_b a - \epsilon})$ | $\Theta(n^{\log_b a})$ |
| 2 | $f(n) = \Theta(n^{\log_b a})$ | $\Theta(n^{\log_b a} \log n)$ |
| 3 | $f(n) = \Omega(n^{\log_b a + \epsilon})$ | $\Theta(f(n))$ |

---

## 🚀 Learning Path

```
Week 1-2: Arrays, Strings, Two Pointers
    ↓
Week 3-4: Linked Lists, Stacks, Queues
    ↓
Week 5-6: Trees, BST, Heaps
    ↓
Week 7-8: Graphs, BFS, DFS
    ↓
Week 9-10: Binary Search, Sorting
    ↓
Week 11-12: Recursion, Backtracking
    ↓
Week 13-16: Dynamic Programming
    ↓
Week 17+: Advanced Topics
```

---

## 📚 Resources

| Resource | Description |
|:---------|:------------|
| [LeetCode](https://leetcode.com) | Practice problems |
| [NeetCode](https://neetcode.io) | Curated roadmap |
| [CP-Algorithms](https://cp-algorithms.com) | Advanced algorithms |

---

<div align="center">

## 👤 Author

**Gaurav Goswami**

[![GitHub](https://img.shields.io/badge/GitHub-Gaurav14cs17-blue?style=flat-square&logo=github)](https://github.com/Gaurav14cs17)

---

**⭐ Star this repo if you find it helpful!**

Made with ❤️ for the DSA community

</div>
