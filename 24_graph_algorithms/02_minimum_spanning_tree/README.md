---
layout: default
title: "Minimum Spanning Tree"
parent: "Graph Algorithms"
nav_order: 2
permalink: /24_graph_algorithms/02_minimum_spanning_tree/

---

<div align="center">

# 🌳 Minimum Spanning Tree (MST)

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-8+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. Shortest Path](../01_shortest_path/README.md) | **02. MST** | [03. Topological Sort →](../03_topological_sort/README.md) |

---

## 🎨 Visual Overview

<div align="center">

![Minimum Spanning Tree - Kruskal's Algorithm](./images/mst-kruskal.svg)

</div>

---

## 📐 Mathematical Foundations

### 1️⃣ MST Definition

**Spanning Tree:** Connected acyclic subgraph containing all vertices.

**Minimum Spanning Tree:** Spanning tree with minimum total edge weight.

```math
\text{MST}(G) = \arg\min_{T \text{ spanning}} \sum_{e \in T} w(e)
```

**Properties:**
- Has exactly $V - 1$ edges
- Unique if all edge weights distinct
- May have multiple MSTs if edge weights repeat

---

### 2️⃣ Cut Property

**Cut:** Partition of vertices into two sets $(S, V \setminus S)$.

**Cut edges:** Edges with one endpoint in $S$, other in $V \setminus S$.

**Cut Property:** Minimum weight edge crossing any cut is in some MST.

This property proves correctness of both Kruskal's and Prim's.

---

### 3️⃣ Cycle Property

**Cycle Property:** Maximum weight edge in any cycle is NOT in any MST.

**Proof:** Removing it and adding lighter edge from cut creates lighter spanning tree.

---

### 4️⃣ Kruskal's Algorithm

**Greedy approach:** Sort edges, add if doesn't create cycle.

**Algorithm:**
1. Sort all edges by weight
2. Initialize Union-Find
3. For each edge $(u, v, w)$ in sorted order:
   - If $\text{find}(u) \neq \text{find}(v)$: add edge, union sets

**Time Complexity:**

```math
T = O(E \log E) = O(E \log V)
```

- Sorting: $O(E \log E)$
- Union-Find operations: $O(E \cdot \alpha(V)) \approx O(E)$

---

### 5️⃣ Prim's Algorithm

**Greedy approach:** Grow tree from arbitrary vertex.

**Algorithm:**
1. Start with arbitrary vertex
2. Repeatedly add minimum weight edge connecting tree to non-tree vertex

**Time Complexity:**

| Implementation | Time |
|----------------|:----:|
| Array | O(V²) |
| Binary Heap | O(E log V) |
| Fibonacci Heap | O(E + V log V) |

---

### 6️⃣ Borůvka's Algorithm

**Parallel-friendly MST algorithm.**

**Algorithm:**
1. Each vertex is a component
2. Find cheapest edge from each component
3. Add all these edges (merge components)
4. Repeat until one component

**Time:** $O(E \log V)$

**Advantage:** Can be parallelized efficiently.

---

### 7️⃣ When to Use Which?

| Scenario | Algorithm | Reason |
|----------|-----------|--------|
| **Dense graph** | Prim's with array | O(V²) better than O(E log V) |
| **Sparse graph** | Kruskal's | Fewer edges to sort |
| **Online edges** | Prim's | Don't need all edges upfront |
| **Parallel** | Borůvka's | Parallelizable steps |

---

## 💻 Code Implementations

```python
from typing import List, Tuple
import heapq

class UnionFind:
    """Union-Find (Disjoint Set Union) with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        """Find with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """Union by rank. Returns True if union happened."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        return True

def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Kruskal's Algorithm for MST.
    
    Args:
        n: number of vertices (0 to n-1)
        edges: list of (u, v, weight)
    
    Returns:
        (total_weight, mst_edges)
    
    Time: O(E log E), Space: O(V)
    """

    # Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])
    
    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0
    
    for u, v, w in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            
            # Early termination: MST has V-1 edges
            if len(mst_edges) == n - 1:
                break
    
    return total_weight, mst_edges

def prim(n: int, edges: List[Tuple[int, int, int]], start: int = 0) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Prim's Algorithm for MST using priority queue.
    
    Args:
        n: number of vertices (0 to n-1)
        edges: list of (u, v, weight)
        start: starting vertex (default 0)
    
    Returns:
        (total_weight, mst_edges)
    
    Time: O(E log V), Space: O(V + E)
    """

    # Build adjacency list
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    visited = set([start])
    mst_edges = []
    total_weight = 0
    
    # Priority queue: (weight, from_vertex, to_vertex)
    pq = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(pq)
    
    while pq and len(visited) < n:
        w, u, v = heapq.heappop(pq)
        
        if v in visited:
            continue
        
        visited.add(v)
        mst_edges.append((u, v, w))
        total_weight += w
        
        # Add edges from newly added vertex
        for neighbor, weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(pq, (weight, v, neighbor))
    
    return total_weight, mst_edges

def prim_dense(n: int, adj_matrix: List[List[int]]) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Prim's Algorithm optimized for dense graphs using adjacency matrix.
    
    Args:
        n: number of vertices
        adj_matrix: n×n matrix, adj_matrix[i][j] = weight (INF if no edge)
    
    Returns:
        (total_weight, mst_edges)
    
    Time: O(V²), Space: O(V)
    """
    INF = float('inf')
    visited = [False] * n
    min_edge = [INF] * n
    parent = [-1] * n
    
    # Start from vertex 0
    min_edge[0] = 0
    mst_edges = []
    total_weight = 0
    
    for _ in range(n):

        # Find minimum edge to unvisited vertex
        u = -1
        for v in range(n):
            if not visited[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        visited[u] = True
        total_weight += min_edge[u]
        
        if parent[u] != -1:
            mst_edges.append((parent[u], u))
        
        # Update minimum edges
        for v in range(n):
            if not visited[v] and adj_matrix[u][v] < min_edge[v]:
                min_edge[v] = adj_matrix[u][v]
                parent[v] = u
    
    return total_weight, mst_edges

# ============= LeetCode Problems =============

def minCostConnectPoints(points: List[List[int]]) -> int:
    """
    LeetCode 1584: Min Cost to Connect All Points
    
    MST with Manhattan distance as edge weight.
    Using Prim's algorithm.
    
    Time: O(n² log n), Space: O(n²)
    """
    n = len(points)
    
    def manhattan(i: int, j: int) -> int:
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
    
    visited = set([0])
    pq = [(manhattan(0, i), i) for i in range(1, n)]
    heapq.heapify(pq)
    total_cost = 0
    
    while len(visited) < n:
        cost, v = heapq.heappop(pq)
        
        if v in visited:
            continue
        
        visited.add(v)
        total_cost += cost
        
        # Add edges from v to unvisited vertices
        for u in range(n):
            if u not in visited:
                heapq.heappush(pq, (manhattan(v, u), u))
    
    return total_cost

def minCostConnectPointsKruskal(points: List[List[int]]) -> int:
    """
    LeetCode 1584: Using Kruskal's algorithm.
    
    Time: O(n² log n), Space: O(n²)
    """
    n = len(points)
    
    def manhattan(i: int, j: int) -> int:
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
    
    # Generate all edges
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((manhattan(i, j), i, j))
    
    # Sort by weight
    edges.sort()
    
    uf = UnionFind(n)
    total_cost = 0
    edges_added = 0
    
    for cost, u, v in edges:
        if uf.union(u, v):
            total_cost += cost
            edges_added += 1
            if edges_added == n - 1:
                break
    
    return total_cost

def findCriticalAndPseudoCriticalEdges(n: int, edges: List[List[int]]) -> List[List[int]]:
    """
    LeetCode 1489: Find Critical and Pseudo-Critical Edges in MST
    
    Critical edge: MST weight increases if removed
    Pseudo-critical: Can be in some MST but not critical
    
    Time: O(E² · α(V)), Space: O(E)
    """

    # Add index to edges
    indexed_edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
    indexed_edges.sort(key=lambda x: x[2])
    
    def find_mst_weight(exclude_idx: int = -1, include_idx: int = -1) -> int:
        """Find MST weight with constraints."""
        uf = UnionFind(n)
        weight = 0
        edges_count = 0
        
        # Include edge if specified
        if include_idx != -1:
            u, v, w, _ = indexed_edges[include_idx]
            uf.union(u, v)
            weight += w
            edges_count += 1
        
        # Add other edges
        for u, v, w, idx in indexed_edges:
            if idx == exclude_idx:
                continue
            if uf.union(u, v):
                weight += w
                edges_count += 1
                if edges_count == n - 1:
                    break
        
        return weight if edges_count == n - 1 else float('inf')
    
    # Find normal MST weight
    normal_mst = find_mst_weight()
    
    critical = []
    pseudo_critical = []
    
    for i in range(len(edges)):

        # Check if critical: MST weight increases without it
        if find_mst_weight(exclude_idx=i) > normal_mst:
            critical.append(i)

        # Check if pseudo-critical: can be included without increasing weight
        elif find_mst_weight(include_idx=i) == normal_mst:
            pseudo_critical.append(i)
    
    return [critical, pseudo_critical]

def minimumCost(n: int, connections: List[List[int]]) -> int:
    """
    LeetCode 1135: Connecting Cities With Minimum Cost
    
    Standard MST problem.
    
    Time: O(E log E), Space: O(V)
    """
    connections.sort(key=lambda x: x[2])
    
    uf = UnionFind(n + 1)  # cities numbered 1 to n
    total_cost = 0
    edges_added = 0
    
    for u, v, cost in connections:
        if uf.union(u, v):
            total_cost += cost
            edges_added += 1
            if edges_added == n - 1:
                return total_cost
    
    return -1  # Cannot connect all cities

def maxNumEdgesToRemove(n: int, edges: List[List[int]]) -> int:
    """
    LeetCode 1579: Remove Max Number of Edges to Keep Graph Fully Traversable
    
    Two MSTs (for Alice and Bob) with shared edges.
    
    Time: O(E · α(V)), Space: O(V)
    """
    uf_alice = UnionFind(n + 1)
    uf_bob = UnionFind(n + 1)
    edges_used = 0
    
    # Process type 3 edges first (both can use)
    for typ, u, v in edges:
        if typ == 3:
            alice_union = uf_alice.union(u, v)
            bob_union = uf_bob.union(u, v)
            if alice_union or bob_union:
                edges_used += 1
    
    # Process type 1 (Alice only) and type 2 (Bob only)
    for typ, u, v in edges:
        if typ == 1:
            if uf_alice.union(u, v):
                edges_used += 1
        elif typ == 2:
            if uf_bob.union(u, v):
                edges_used += 1
    
    # Check if both graphs are fully connected
    alice_components = len(set(uf_alice.find(i) for i in range(1, n + 1)))
    bob_components = len(set(uf_bob.find(i) for i in range(1, n + 1)))
    
    if alice_components != 1 or bob_components != 1:
        return -1
    
    return len(edges) - edges_used
```

---

## 🏆 LeetCode Problems

### 🟡 Medium

| # | Problem | Algorithm | Time | Space |
|:-:|---------|-----------|:----:|:-----:|
| 1135 | [Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) | Kruskal's | O(E log E) | O(V) |
| 1168 | [Optimize Water Distribution](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) | MST with virtual node | O(E log E) | O(V) |
| 1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Prim's | O(n² log n) | O(n²) |

### 🔴 Hard

| # | Problem | Algorithm | Time | Space |
|:-:|---------|-----------|:----:|:-----:|
| 1489 | [Critical and Pseudo-Critical Edges](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) | Multiple MSTs | O(E²·α(V)) | O(E) |
| 1579 | [Remove Max Edges Keep Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) | Two MSTs | O(E·α(V)) | O(V) |

---

## 📊 Algorithm Comparison

```
MST Problem
     |
     +-- Sparse graph (E << V²) → Kruskal's O(E log V)
     |
     +-- Dense graph (E ≈ V²) → Prim's with array O(V²)
     |
     +-- Online/incremental edges → Prim's
     |
     +-- Need parallelization → Borůvka's O(E log V)
```

---

## 🎯 Key Insights

1. **MST is unique** if all edge weights are distinct
2. **Both Kruskal's and Prim's** are greedy and optimal
3. **Union-Find** essential for Kruskal's efficiency
4. **Prim's with heap** better for dense graphs when using array
5. **Cut property** proves correctness of both algorithms

---

## 📚 References

| Resource | Link |
|----------|------|
| **Kruskal's Algorithm** | [Wikipedia](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) |
| **Prim's Algorithm** | [Wikipedia](https://en.wikipedia.org/wiki/Prim%27s_algorithm) |
| **MST Algorithms** | [GeeksforGeeks](https://www.geeksforgeeks.org/minimum-spanning-tree/) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. Shortest Path](../01_shortest_path/README.md) | **02. MST** | [03. Topological Sort →](../03_topological_sort/README.md) |

