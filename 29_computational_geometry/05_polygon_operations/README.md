---
layout: default
title: "Polygon Operations"
parent: "Computational Geometry"
nav_order: 5
---
<div align="center">

# 🔷 Polygon Operations

### *Area, perimeter, and point-in-polygon tests*

<p><img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge" alt="Difficulty"></p>

[🏠 Computational Geometry](../README.md)

</div>

---



## 📊 Visual Overview

![Polygon Operations](./images/polygon-operations.png)

*Shoelace formula for area calculation and ear clipping triangulation*

---

## 🎯 At a Glance

| | |
|:---|:---|
| **In one line** | Polygon operations compute properties and perform transformations on polygons. |
| **Typical time** | O(n) for area, O(n²) for triangulation |
| **Typical space** | O(n) |
| **Topics** | Area, Perimeter, Triangulation, Boolean Operations |

> **How to use this page:** Start with the visual overview, scan **At a Glance**, then work through theory → walkthroughs → code.
## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← Polygon Operations](../05_polygon_operations/README.md) | **05. Polygon Operations** | [Closest Pair →](../06_closest_pair/README.md) |

---


---

## 🎯 Overview

Polygon operations compute properties and perform transformations on polygons.

---

## 📐 Mathematical Foundation

### Shoelace Formula (Area)

**For polygon with vertices (x₀, y₀), (x₁, y₁), ..., (xₙ₋₁, yₙ₋₁):**

![Shoelace Formula](./images/shoelace-formula.png)

*Shoelace area formula with signed area (positive CCW, negative CW)*

---

## 💻 Implementations

### 1. Polygon Area (Shoelace Formula)

![Polygon Area Walkthrough](./images/polygon-area-walkthrough.png)

*Shoelace formula implementation with signed area variant — O(n)*

### 2. Polygon Perimeter

![Polygon Perimeter Walkthrough](./images/polygon-perimeter-walkthrough.png)

*Sum of edge distances including wrap-around — O(n)*

### 3. Polygon Centroid

![Polygon Centroid Walkthrough](./images/polygon-centroid-walkthrough.png)

*Center of mass using weighted cross products — O(n)*

### 4. Polygon Triangulation (Ear Clipping)

![Ear Clipping Walkthrough](./images/ear-clipping-walkthrough.png)

*Identify and clip ear vertices until triangle remains — O(n²)*

### 5. Rectangle Overlap

![Rectangle Overlap Walkthrough](./images/rectangle-overlap-walkthrough.png)

*Axis-aligned rectangle overlap test and intersection area*

---

## 🧩 LeetCode Problems

| # | Problem | Difficulty |
|---|---------|------------|
| 223 | [Rectangle Area](https://leetcode.com/problems/rectangle-area/) | 🟡 Medium |
| 836 | [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) | 🟢 Easy |
| 850 | [Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/) | 🔴 Hard |
| 593 | [Valid Square](https://leetcode.com/problems/valid-square/) | 🟡 Medium |

---

## 📚 References & Learning Resources

### 📖 Core Concepts

| Resource | Description | Link |
|----------|-------------|------|
| **Polygon Area** | GeeksforGeeks | [Shoelace formula](https://www.geeksforgeeks.org/area-of-a-polygon-with-given-n-ordered-vertices/) |
| **Computational Geometry** | CP-Algorithms | [Geometry](https://cp-algorithms.com/geometry/) |

### 📝 Practice

| Platform | Focus | Link |
|----------|-------|------|
| **LeetCode** | Geometry tag | [Problems](https://leetcode.com/tag/geometry/) |

---

**Navigation:** [← Point Location](../04_point_location/) | [Next: Closest Pair →](../06_closest_pair/)
