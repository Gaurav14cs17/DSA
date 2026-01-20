---
layout: default
title: "Lazy Propagation"
parent: "Segment Tree Advanced"
grand_parent: "Advanced Trees"
nav_order: 1
permalink: /27_advanced_trees/07_segment_tree_advanced/01_lazy_propagation/
---

<div align="center">

# ⏱️ Lazy Propagation

<p>
  <img src="https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-10-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← Segment Tree Advanced](../README.md) | **01. Lazy Propagation** | [02. 2D Segment Tree →](../02_2d_segment_tree/README.md) |

---

## 📊 Visual Overview

<div align="center">
<img src="./images/lazy-propagation.svg" alt="Lazy Propagation" width="100%">
</div>

---

## 📐 Core Concept

**Lazy Propagation:** Defer updates until absolutely necessary.

**Key Idea:** Mark nodes with pending updates, propagate only when querying or further updating.

**Operations:** Both range update and range query in $O(\log n)$.

---

## 💻 Implementation

```python
class SegmentTreeLazy:
    """
    Segment Tree with Lazy Propagation for range updates.
    
    Time: O(log n) per operation
    """
    
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)
    
    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2*node+1, start, mid)
            self._build(arr, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def _push(self, node, start, end):
        """Propagate lazy value to children."""
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            
            if start != end:
                self.lazy[2*node+1] += self.lazy[node]
                self.lazy[2*node+2] += self.lazy[node]
            
            self.lazy[node] = 0
    
    def update_range(self, l, r, val):
        """Add val to range [l, r]."""
        self._update_range(0, 0, self.n-1, l, r, val)
    
    def _update_range(self, node, start, end, l, r, val):
        self._push(node, start, end)
        
        if start > r or end < l:
            return
        
        if l <= start and end <= r:
            self.lazy[node] += val
            self._push(node, start, end)
            return
        
        mid = (start + end) // 2
        self._update_range(2*node+1, start, mid, l, r, val)
        self._update_range(2*node+2, mid+1, end, l, r, val)
        
        self._push(2*node+1, start, mid)
        self._push(2*node+2, mid+1, end)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def query_range(self, l, r):
        """Sum of range [l, r]."""
        return self._query_range(0, 0, self.n-1, l, r)
    
    def _query_range(self, node, start, end, l, r):
        if start > r or end < l:
            return 0
        
        self._push(node, start, end)
        
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        return (self._query_range(2*node+1, start, mid, l, r) +
                self._query_range(2*node+2, mid+1, end, l, r))
```

---

## 📋 Problems

| # | Problem | Difficulty | Technique |
|---|---------|:----------:|-----------|
| 307 | Range Sum Query - Mutable | Medium | Basic lazy |
| 370 | Range Addition | Medium | Range update |
| 732 | My Calendar III | Hard | Lazy counting |
| 715 | Range Module | Hard | Assignment lazy |
| 2569 | Handling Sum Queries | Hard | Flip operation |
| 1622 | Fancy Sequence | Hard | Multiple ops |
| - | Range Assignment | Hard | Set operation |
| - | Range Flip | Hard | Binary toggle |
| - | Range Multiply | Hard | Mult + add |
| - | Sqrt Decomposition | Hard | Block updates |

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← Segment Tree Advanced](../README.md) | **01. Lazy Propagation** | [02. 2D Segment Tree →](../02_2d_segment_tree/README.md) |

