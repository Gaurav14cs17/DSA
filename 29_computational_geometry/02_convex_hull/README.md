---
layout: default
title: "Convex Hull"
parent: "Computational Geometry"
nav_order: 2
---

# 🔺 Convex Hull Algorithms

## 📊 Metadata
- **Difficulty:** ![Hard](https://img.shields.io/badge/Hard-red)
- **Time Complexity:** O(n log n) optimal
- **Space Complexity:** O(n)
- **Algorithms:** Graham's Scan, Jarvis March, QuickHull, Andrew's

---

## 🎯 Overview

**Convex Hull:** Smallest convex polygon containing all given points. Fundamental problem in computational geometry.

---

## 📊 Visual Overview

![Convex Hull Algorithms](./images/convex-hull.svg)

*Graham's Scan step-by-step visualization with algorithm comparison*

---

## 📐 Mathematical Foundation

### Convex Set

**Definition:** Set S is convex if for any two points p, q ∈ S, the line segment pq is entirely in S.

```
Mathematically:
∀p, q ∈ S, ∀λ ∈ [0,1]: λp + (1-λ)q ∈ S
```

### Convex Hull Properties

```
1. Unique: Convex hull is unique for any point set
2. Minimum perimeter: Has shortest perimeter enclosing all points
3. Subset: Hull points are subset of input points
4. At most n vertices: For n input points
5. At least 3 vertices: For non-collinear points
```

---

## 💻 Implementations

### 1. Graham's Scan

```python
from math import atan2, pi

def convex_hull_graham(points):
    """
    Graham's Scan algorithm for convex hull
    
    Time: O(n log n)
    Space: O(n)
    
    Steps:
    1. Find pivot (lowest point)
    2. Sort by polar angle
    3. Process points, maintaining left turns only
    
    Returns: Points on convex hull (counter-clockwise)
    """
    n = len(points)
    if n < 3:
        return points
    
    # Find pivot: lowest point (leftmost if tie)
    pivot = min(points, key=lambda p: (p.y, p.x))
    
    # Sort by polar angle
    def polar_angle_key(p):
        if p == pivot:
            return (-pi, 0)
        angle = atan2(p.y - pivot.y, p.x - pivot.x)
        dist_sq = (p.x - pivot.x)**2 + (p.y - pivot.y)**2
        return (angle, dist_sq)
    
    sorted_points = sorted(points, key=polar_angle_key)
    
    # Build hull
    hull = []
    
    for p in sorted_points:
        # Remove points making right turn
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    
    return hull

# Helper function
def cross_product(o, a, b):
    """Cross product of vectors OA and OB"""
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
```

### 2. Jarvis March (Gift Wrapping)

```python
def convex_hull_jarvis(points):
    """
    Jarvis March (Gift Wrapping) algorithm
    
    Time: O(nh) where h = hull size
    Space: O(h)
    
    Good when h << n (few hull points)
    
    Algorithm:
    1. Start from leftmost point
    2. Find most counter-clockwise point
    3. Repeat until back to start
    """
    n = len(points)
    if n < 3:
        return points
    
    # Find leftmost point
    leftmost = min(points, key=lambda p: (p.x, p.y))
    
    hull = []
    current = leftmost
    
    while True:
        hull.append(current)
        next_point = points[0]
        
        # Find most counter-clockwise point
        for candidate in points[1:]:
            if candidate == current:
                continue
            
            cross = cross_product(current, next_point, candidate)
            
            # More counter-clockwise or collinear but farther
            if (cross > 0 or 
                (cross == 0 and 
                 current.distance_squared(candidate) > current.distance_squared(next_point))):
                next_point = candidate
        
        current = next_point
        
        # Back to start
        if current == leftmost:
            break
    
    return hull
```

### 3. Andrew's Monotone Chain

```python
def convex_hull_andrew(points):
    """
    Andrew's Monotone Chain algorithm
    
    Time: O(n log n)
    Space: O(n)
    
    Simpler implementation than Graham's Scan
    
    Algorithm:
    1. Sort points by x-coordinate
    2. Build lower hull (left to right)
    3. Build upper hull (right to left)
    """
    points = sorted(set(points), key=lambda p: (p.x, p.y))
    
    if len(points) < 3:
        return points
    
    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    # Concatenate (remove last point of each half - duplicates)
    return lower[:-1] + upper[:-1]
```

### 4. QuickHull (Divide and Conquer)

```python
def convex_hull_quickhull(points):
    """
    QuickHull algorithm (similar to QuickSort)
    
    Time: O(n log n) average, O(n²) worst
    Space: O(n)
    
    Recursive divide and conquer approach
    """
    if len(points) < 3:
        return points
    
    # Find extreme points
    min_x = min(points, key=lambda p: p.x)
    max_x = max(points, key=lambda p: p.x)
    
    hull = []
    
    # Find hull points on both sides
    hull.extend(quick_hull_recursive(points, min_x, max_x))
    hull.extend(quick_hull_recursive(points, max_x, min_x))
    
    return hull

def quick_hull_recursive(points, p1, p2):
    """Recursive helper for QuickHull"""
    # Find points to the left of line p1-p2
    left_points = []
    max_dist = 0
    farthest = None
    
    for p in points:
        if p == p1 or p == p2:
            continue
        
        # Check if point is to the left
        cross = cross_product(p1, p2, p)
        
        if cross > 0:
            left_points.append(p)
            dist = abs(cross)
            
            if dist > max_dist:
                max_dist = dist
                farthest = p
    
    # Base case: no points to the left
    if not farthest:
        return [p1]
    
    # Recursive case: find hull points in two segments
    hull = []
    hull.extend(quick_hull_recursive(left_points, p1, farthest))
    hull.extend(quick_hull_recursive(left_points, farthest, p2))
    
    return hull
```

### 5. Convex Hull Applications

```python
def hull_area(hull):
    """
    Calculate area of convex hull
    
    Uses Shoelace formula
    Time: O(n)
    """
    n = len(hull)
    if n < 3:
        return 0
    
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += hull[i].x * hull[j].y
        area -= hull[j].x * hull[i].y
    
    return abs(area) / 2

def hull_perimeter(hull):
    """
    Calculate perimeter of convex hull
    
    Time: O(n)
    """
    if len(hull) < 2:
        return 0
    
    perimeter = 0
    n = len(hull)
    
    for i in range(n):
        j = (i + 1) % n
        perimeter += hull[i].distance(hull[j])
    
    return perimeter

def point_in_convex_hull(point, hull):
    """
    Check if point is inside convex hull
    
    For convex polygons, all cross products should have same sign
    
    Time: O(n)
    """
    n = len(hull)
    if n < 3:
        return False
    
    # Get sign of first cross product
    first_sign = None
    
    for i in range(n):
        j = (i + 1) % n
        cross = cross_product(hull[i], hull[j], point)
        
        if abs(cross) < 1e-9:  # On edge
            continue
        
        if first_sign is None:
            first_sign = cross > 0
        elif (cross > 0) != first_sign:
            return False
    
    return True
```

---

## 🧩 LeetCode Problems

| # | Problem | Difficulty | Algorithm |
|---|---------|------------|-----------|
| 587 | [Erect the Fence](https://leetcode.com/problems/erect-the-fence/) | 🔴 Hard | Any convex hull |
| 973 | [K Closest Points](https://leetcode.com/problems/k-closest-points-to-origin/) | 🟡 Medium | Partial hull |
| 892 | [Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/) | 🟢 Easy | 3D hull concept |

---

## 💡 Algorithm Comparison

| Algorithm | Time | Space | Best When |
|-----------|:----:|:-----:|-----------|
| **Graham's Scan** | O(n log n) | O(n) | General purpose |
| **Jarvis March** | O(nh) | O(h) | h << n (few hull points) |
| **Andrew's** | O(n log n) | O(n) | Simpler implementation |
| **QuickHull** | O(n log n) avg | O(n) | Divide & conquer preference |

**Recommendation:** Andrew's Monotone Chain for simplicity and reliability.

---

**Navigation:** [← Geometric Primitives](../01_geometric_primitives/) | [Next: Line Intersection →](../03_line_intersection/)

