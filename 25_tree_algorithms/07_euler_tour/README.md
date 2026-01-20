---
layout: default
title: "Euler Tour Techniques"
parent: "Tree Algorithms"
nav_order: 7
permalink: /25_tree_algorithms/07_euler_tour/
---

<div align="center">

# 🔄 Euler Tour Techniques

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-8+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 06. DSU on Tree](../06_dsu_on_tree/README.md) | **07. Euler Tour** | [🏠 Home](../README.md) |

---

## 📊 Visual Overview

<div align="center">
<img src="./images/euler-tour-diagram.svg" alt="Euler Tour Diagram" width="100%"/>
</div>

---

## 📐 Mathematical Foundations

### 1️⃣ Euler Tour Definition

**Euler Tour:** Flatten tree into array by recording entry/exit times in DFS.

**Two variants:**
1. **Node-based:** Record each node once (entry time only)
2. **Edge-based:** Record each node twice (entry and exit)

---

### 2️⃣ DFS Order (Flattening)

**DFS Order:** Assign each node a position based on DFS traversal.

**Properties:**
- Subtree occupies contiguous range

- Range $[\text{in}[v], \text{out}[v]]$ = subtree of $v$

- Enables range queries on subtrees

**Time:** $O(n)$ to build  
**Space:** $O(n)$

---

### 3️⃣ Subtree to Range Query

**Key transformation:**

```
Subtree query on v → Range query on [in[v], out[v]]

```

**Applications:**
- Subtree sum → Range sum

- Subtree update → Range update

- Subtree max/min → Range max/min

---

### 4️⃣ Path to Two Ranges

**Path from $u$ to $v$:**
- Can be split using LCA

- Convert to two ranges in Euler tour

- Union of ranges covers path

---

### 5️⃣ Complexity Analysis

| Operation | Without Euler Tour | With Euler Tour |
|-----------|:------------------:|:---------------:|
| **Subtree sum** | O(n) DFS | O(log n) |
| **Subtree update** | O(n) DFS | O(log n) |
| **Subtree max** | O(n) DFS | O(log n) |
| **Build** | - | O(n) |

---

### 6️⃣ Data Structures Used

**Combined with:**
- **Segment Tree:** Range queries/updates

- **Fenwick Tree:** Prefix sums

- **Sparse Table:** RMQ (read-only)

---

## 💻 Code Implementations

```python
from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class EulerTour:
    """
    Euler Tour of tree for efficient subtree queries.
    
    Converts tree to array where subtrees are contiguous ranges.
    """
    
    def __init__(self, n: int, edges: List[List[int]], root: int = 0):
        """
        Args:
            n: number of nodes (0 to n-1)
            edges: list of [u, v] edges
            root: root node
        """
        self.n = n
        self.root = root
        
        # Build adjacency list
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        # Euler tour arrays
        self.in_time = [0] * n  # Entry time
        self.out_time = [0] * n  # Exit time
        self.euler = []  # Euler tour sequence
        self.depth = [0] * n
        self.parent = [-1] * n
        
        self.timer = 0
        
        # Build Euler tour
        self._dfs(root, -1, 0)
    
    def _dfs(self, u: int, p: int, d: int):
        """Build Euler tour using DFS."""
        self.parent[u] = p
        self.depth[u] = d
        self.in_time[u] = self.timer
        self.euler.append(u)
        self.timer += 1
        
        for v in self.graph[u]:
            if v != p:
                self._dfs(v, u, d + 1)
        
        self.out_time[u] = self.timer - 1
    
    def get_subtree_range(self, node: int) -> tuple:
        """Get range [l, r] representing subtree of node."""
        return (self.in_time[node], self.out_time[node])
    
    def is_ancestor(self, u: int, v: int) -> bool:
        """Check if u is ancestor of v."""
        return (self.in_time[u] <= self.in_time[v] and 
                self.out_time[v] <= self.out_time[u])

class FenwickTree:
    """Fenwick Tree (Binary Indexed Tree) for prefix sums."""
    
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, idx: int, delta: int):
        """Add delta to position idx."""
        idx += 1  # 1-indexed
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)
    
    def query(self, idx: int) -> int:
        """Query prefix sum [0, idx]."""
        idx += 1  # 1-indexed
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)
        return result
    
    def range_query(self, left: int, right: int) -> int:
        """Query sum in range [left, right]."""
        if left > 0:
            return self.query(right) - self.query(left - 1)
        return self.query(right)

class SubtreeQueries:
    """
    Efficient subtree queries using Euler tour + Fenwick tree.
    
    Supports:
    - Subtree sum in O(log n)
    - Node update in O(log n)
    - Subtree update in O(log n) with difference array
    """
    
    def __init__(self, n: int, edges: List[List[int]], 
                 values: List[int], root: int = 0):
        """
        Args:
            n: number of nodes
            edges: tree edges
            values: initial node values
            root: root node
        """
        self.euler = EulerTour(n, edges, root)
        self.fenwick = FenwickTree(n)
        
        # Initialize Fenwick tree with values
        for i in range(n):
            pos = self.euler.in_time[i]
            self.fenwick.update(pos, values[i])
    
    def update_node(self, node: int, new_value: int, old_value: int):
        """
        Update single node value.
        
        Time: O(log n)
        """
        pos = self.euler.in_time[node]
        self.fenwick.update(pos, new_value - old_value)
    
    def query_subtree(self, node: int) -> int:
        """
        Query sum of subtree rooted at node.
        
        Time: O(log n)
        """
        left, right = self.euler.get_subtree_range(node)
        return self.fenwick.range_query(left, right)

class EulerTourBinaryTree:
    """
    Euler tour for binary tree (recording entry and exit).
    
    Each node appears twice in tour.
    """
    
    def __init__(self, root: Optional[TreeNode]):
        self.tour = []
        self.depth = []
        self.first_occurrence = {}
        self._build(root, 0)
    
    def _build(self, node: Optional[TreeNode], d: int):
        """Build Euler tour with entry/exit."""
        if not node:
            return
        
        # Entry
        if node not in self.first_occurrence:
            self.first_occurrence[node] = len(self.tour)
        self.tour.append(node)
        self.depth.append(d)
        
        # Left subtree
        if node.left:
            self._build(node.left, d + 1)
            self.tour.append(node)
            self.depth.append(d)
        
        # Right subtree
        if node.right:
            self._build(node.right, d + 1)
            self.tour.append(node)
            self.depth.append(d)

# ============= Advanced Applications =============

class PathQueries:
    """
    Path queries using Euler tour.
    
    Supports path sum/max/min queries.
    """
    
    def __init__(self, n: int, edges: List[List[int]], 
                 values: List[int], root: int = 0):
        self.euler = EulerTour(n, edges, root)
        self.values = values
        
        # Build LCA data structure (binary lifting)
        import math
        self.LOG = math.ceil(math.log2(n)) + 1
        self.up = [[-1] * self.LOG for _ in range(n)]
        
        # Build binary lifting table
        for i in range(n):
            self.up[i][0] = self.euler.parent[i]
        
        for k in range(1, self.LOG):
            for v in range(n):
                if self.up[v][k - 1] != -1:
                    self.up[v][k] = self.up[self.up[v][k - 1]][k - 1]
    
    def lca(self, u: int, v: int) -> int:
        """Find LCA of u and v."""
        if self.euler.depth[u] < self.euler.depth[v]:
            u, v = v, u
        
        # Bring u to same level as v
        diff = self.euler.depth[u] - self.euler.depth[v]
        for k in range(self.LOG):
            if (diff >> k) & 1:
                u = self.up[u][k]
        
        if u == v:
            return u
        
        # Binary search for LCA
        for k in range(self.LOG - 1, -1, -1):
            if self.up[u][k] != self.up[v][k]:
                u = self.up[u][k]
                v = self.up[v][k]
        
        return self.up[u][0]
    
    def path_sum(self, u: int, v: int) -> int:
        """Compute sum on path from u to v."""
        lca_node = self.lca(u, v)
        
        # Sum from u to lca
        total = 0
        curr = u
        while curr != lca_node:
            total += self.values[curr]
            curr = self.euler.parent[curr]
        
        # Sum from v to lca
        curr = v
        while curr != lca_node:
            total += self.values[curr]
            curr = self.euler.parent[curr]
        
        # Add lca
        total += self.values[lca_node]
        
        return total

# ============= Example Usage =============

def example_subtree_queries():
    """Example: Subtree sum queries"""
    n = 7
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
    values = [1, 2, 3, 4, 5, 6, 7]
    
    sq = SubtreeQueries(n, edges, values)
    
    print("Initial subtree sums:")
    for i in range(n):
        print(f"  Subtree of {i}: {sq.query_subtree(i)}")
    
    # Update node 1
    sq.update_node(1, 10, 2)
    print(f"\nAfter updating node 1 to 10:")
    print(f"  Subtree of 0: {sq.query_subtree(0)}")
    print(f"  Subtree of 1: {sq.query_subtree(1)}")

def flatten_tree_to_array(root: TreeNode) -> List[int]:
    """
    Flatten binary tree to array using DFS order.
    
    Time: O(n), Space: O(n)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result

def subtree_size_queries(n: int, edges: List[List[int]], 
                        queries: List[int]) -> List[int]:
    """
    Answer subtree size queries efficiently.
    
    Time: O(n + q), Space: O(n)
    """
    euler = EulerTour(n, edges)
    
    result = []
    for node in queries:
        left, right = euler.get_subtree_range(node)
        size = right - left + 1
        result.append(size)
    
    return result

def ancestor_queries(n: int, edges: List[List[int]], 
                    queries: List[List[int]]) -> List[bool]:
    """
    Check if u is ancestor of v for multiple queries.
    
    Time: O(n + q), Space: O(n)
    """
    euler = EulerTour(n, edges)
    
    result = []
    for u, v in queries:
        result.append(euler.is_ancestor(u, v))
    
    return result

```

---

## 🏆 Related LeetCode Problems

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 1305 | [All Elements in Two BSTs](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/) | Inorder | O(n+m) | O(n+m) |
| 2003 | [Smallest Missing Value](https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/) | DFS Order | O(n) | O(n) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 2322 | [Minimum Score After Removals](https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/) | Subtree ranges | O(n²) | O(n) |

---

## 📊 When to Use Euler Tour

```
Tree Query Problem
     |
     +-- Subtree queries
     |   +-- Many queries → Euler Tour + Segment/Fenwick Tree
     |       Examples: subtree sum, max, min
     |
     +-- Ancestor checking
     |   +-- in[u] ≤ in[v] ≤ out[v] ≤ out[u]
     |
     +-- LCA with RMQ
         +-- Euler tour + depth → RMQ for LCA

```

---

## 🎯 Key Insights

1. **Subtree = contiguous range** in DFS order
2. **Enables range data structures** on trees
3. **O(1) ancestor checking** with in/out times
4. **Combined with segment tree** for updates
5. **Foundation for HLD** and other advanced techniques

---

## 📚 References

| Resource | Link |
|----------|------|
| **Euler Tour** | [CP-Algorithms](https://cp-algorithms.com/graph/euler_path.html) |
| **DFS Order** | [Codeforces](https://codeforces.com/blog/entry/18369) |
| **Tree Flattening** | [GeeksforGeeks](https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 06. DSU on Tree](../06_dsu_on_tree/README.md) | **07. Euler Tour** | [🏠 Home](../README.md) |

