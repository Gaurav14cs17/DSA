---
layout: default
title: "Minimum Spanning Tree"
parent: "Graphs"
nav_order: 7
permalink: /10_graphs/07_mst/

---

<div align="center">

# 🌲 Minimum Spanning Tree

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-5+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next Topic |
|:------------|:----------:|--------:|
| [← 06. Cycle Detection](../06_cycle_detection/README.md) | **07. MST** | [🏠 Graphs Home](../README.md) → [Tries](../../11_tries/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ MST Definition

**Spanning Tree:** Subgraph that connects all vertices with minimum edges.

**Minimum Spanning Tree:** Spanning tree with minimum total edge weight.

```math
\text{MST weight} = \sum_{e \in T} w(e) \text{ is minimized}
```

---

### 2️⃣ MST Properties

| Property | Description |
|----------|-------------|
| **Edges** | Exactly $V - 1$ edges |
| **Unique** | Unique if all edge weights distinct |
| **Cut Property** | Min-weight edge crossing any cut is in MST |
| **Cycle Property** | Max-weight edge in any cycle is NOT in MST |

---

### 3️⃣ Kruskal's Algorithm

1. Sort edges by weight
2. Add edges that don't form cycle (Union-Find)
3. Stop when $V - 1$ edges added

```math
T = O(E \log E) = O(E \log V)
```

---

### 4️⃣ Prim's Algorithm

1. Start from any vertex
2. Add minimum-weight edge connecting tree to non-tree vertex
3. Repeat until all vertices included

```math
T = O((V + E) \log V) \text{ with binary heap}
T = O(E + V \log V) \text{ with Fibonacci heap}
```

---

### 5️⃣ Cut Property

**Theorem:** For any cut $(S, V-S)$, the minimum-weight edge crossing the cut is in some MST.

**Proof:** If not, we can swap it with a heavier edge → lower weight tree. Contradiction. ∎

---

## 🎨 Visual Diagrams

<div align="center">

![Kruskal's Algorithm](./images/kruskal_algorithm.svg)

*Kruskal's MST Algorithm with Union-Find*

</div>

---

## 💻 Code Implementations

```python
import heapq

class UnionFind:
    """Union-Find for Kruskal's algorithm."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal(n: int, edges: list) -> int:
    """
    Kruskal's MST Algorithm.
    
    Sort edges, add non-cycle edges using Union-Find.
    
    Time: O(E log E), Space: O(V)
    """
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(n)
    
    mst_weight = 0
    edges_used = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            mst_weight += w
            edges_used += 1
            if edges_used == n - 1:
                break
    
    return mst_weight if edges_used == n - 1 else -1

def prim(n: int, adj: list) -> int:
    """
    Prim's MST Algorithm.
    
    Greedy: always add minimum edge to tree.
    
    Time: O((V+E) log V), Space: O(V)
    """
    visited = [False] * n
    pq = [(0, 0)]  # (weight, vertex)
    mst_weight = 0
    edges_used = 0
    
    while pq and edges_used < n:
        w, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
        mst_weight += w
        edges_used += 1
        
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))
    
    return mst_weight if edges_used == n else -1

def minCostConnectPoints(points: list[list[int]]) -> int:
    """
    Min Cost to Connect All Points (LeetCode 1584).
    
    MST with Manhattan distance as edge weight.
    
    Time: O(n² log n), Space: O(n²)
    """
    n = len(points)
    
    # Build edges with Manhattan distance
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((i, j, dist))
    
    return kruskal(n, edges)

def minCostConnectPointsPrim(points: list[list[int]]) -> int:
    """
    Min Cost to Connect Points using Prim's.
    
    Optimized for dense graphs (E = V²).
    
    Time: O(n²), Space: O(n)
    """
    n = len(points)
    visited = [False] * n
    min_dist = [float('inf')] * n
    min_dist[0] = 0
    
    total_cost = 0
    
    for _ in range(n):

        # Find minimum unvisited vertex
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                u = i
        
        visited[u] = True
        total_cost += min_dist[u]
        
        # Update distances
        for v in range(n):
            if not visited[v]:
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                min_dist[v] = min(min_dist[v], dist)
    
    return total_cost
```

---

## 🏆 LeetCode Problems

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 1135 | [Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) | Kruskal/Prim | O(E log E) | O(V) |
| 1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | MST | O(n² log n) | O(n²) |
| 1631 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Modified MST | O(mn log mn) | O(mn) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 1489 | [Find Critical and Pseudo-Critical Edges](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-mst/) | MST Analysis | O(E² log V) | O(E) |

---

## 📊 MST Algorithm Selection

```
MST Problem
     |
     +-- Sparse graph (E ≈ V) → Kruskal's O(E log E)
     |
     +-- Dense graph (E ≈ V²) → Prim's O(V²)
     |
     +-- Edge-by-edge processing → Kruskal's with Union-Find
```

---

## 📚 References

| Resource | Link |
|----------|------|
| **Kruskal's Algorithm** | [Wikipedia](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) |
| **Prim's Algorithm** | [Wikipedia](https://en.wikipedia.org/wiki/Prim%27s_algorithm) |
| **MST** | [GeeksforGeeks](https://www.geeksforgeeks.org/minimum-spanning-tree/) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next Topic |
|:------------|:----------:|--------:|
| [← 06. Cycle Detection](../06_cycle_detection/README.md) | **07. MST** | [🏠 Graphs Home](../README.md) → [Tries](../../11_tries/README.md) |
