---
layout: default
title: "Centroid Decomposition"
parent: "Tree Algorithms"
nav_order: 5
permalink: /25_tree_algorithms/05_centroid_decomposition/
---

<div align="center">

# 🎯 Centroid Decomposition

<p>
  <img src="https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-6+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 04. HLD](../04_heavy_light_decomposition/README.md) | **05. Centroid Decomposition** | [06. DSU on Tree →](../06_dsu_on_tree/README.md) |

---

## 📊 Visual Overview

<div align="center">
<img src="./images/centroid-decomposition-diagram.svg" alt="Centroid Decomposition Diagram" width="100%"/>
</div>

---

## 📐 Mathematical Foundations

### 1️⃣ Centroid Definition

**Centroid** of tree: Node whose removal results in no subtree with more than $n/2$ nodes.

**Key property:** Every tree has at least one centroid (at most two).

**Proof:** Start at any node, move to heaviest child until all children ≤ n/2.

---

### 2️⃣ Centroid Decomposition

**Recursively decompose tree:**
1. Find centroid of tree
2. Remove centroid
3. Recursively decompose resulting subtrees
4. Build centroid tree

**Depth of centroid tree:** $O(\log n)$

---

### 3️⃣ Centroid Tree Properties

**Structure:**
- Root = centroid of original tree

- Children = centroids of subtrees after removal

- Height = $O(\log n)$

- Each node appears once

**Path decomposition:** Any path passes through $O(\log n)$ centroids.

---

### 4️⃣ Applications

| Problem | Technique | Complexity |
|---------|-----------|:----------:|
| **k-th Path** | Centroid + counting | O(n log n) |
| **Paths with sum k** | Centroid + hash map | O(n log n) |
| **Closest colored node** | Centroid + BFS | O(n log n) |
| **Tree distances** | Centroid + DP | O(n log n) |

---

### 5️⃣ Algorithm Complexity

**Decomposition:** $O(n \log n)$

- Finding centroid: $O(n)$

- Depth: $O(\log n)$

- Total: $O(n) \times O(\log n) = O(n \log n)$

**Query:** Typically $O(\log n)$ to $O(\log^2 n)$

---

### 6️⃣ Distance Counting

**Count paths with specific property:**
1. Root at centroid
2. Count paths through centroid
3. Subtract paths entirely in one subtree
4. Recurse on subtrees

**Key insight:** Every path passes through exactly one centroid ancestor.

---

## 💻 Code Implementations

```python
from typing import List, Set, Dict, Tuple
from collections import defaultdict, Counter

class CentroidDecomposition:
    """
    Centroid Decomposition of tree.
    
    Applications:
    - Count paths with specific properties
    - Distance queries
    - K-th path problems
    """
    
    def __init__(self, n: int, edges: List[List[int]]):
        """
        Args:
            n: number of nodes (0 to n-1)
            edges: list of [u, v] edges
        """
        self.n = n
        
        # Build adjacency list
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        # Centroid tree
        self.centroid_parent = [-1] * n
        self.removed = [False] * n
        self.subtree_size = [0] * n
        
        # Build centroid decomposition
        self._decompose(0, -1)
    
    def _get_subtree_size(self, u: int, parent: int) -> int:
        """Calculate subtree size."""
        self.subtree_size[u] = 1
        for v in self.graph[u]:
            if v != parent and not self.removed[v]:
                self.subtree_size[u] += self._get_subtree_size(v, u)
        return self.subtree_size[u]
    
    def _find_centroid(self, u: int, parent: int, tree_size: int) -> int:
        """Find centroid of tree."""
        for v in self.graph[u]:
            if v != parent and not self.removed[v]:
                if self.subtree_size[v] > tree_size // 2:
                    return self._find_centroid(v, u, tree_size)
        return u
    
    def _decompose(self, u: int, parent: int):
        """Recursively decompose tree."""
        # Get tree size and find centroid
        tree_size = self._get_subtree_size(u, -1)
        centroid = self._find_centroid(u, -1, tree_size)
        
        # Mark as removed and set parent in centroid tree
        self.removed[centroid] = True
        self.centroid_parent[centroid] = parent
        
        # Recursively decompose subtrees
        for v in self.graph[centroid]:
            if not self.removed[v]:
                self._decompose(v, centroid)

def count_paths_with_sum_k(n: int, edges: List[List[int]], 
                           values: List[int], k: int) -> int:
    """
    Count paths with sum equal to k.
    
    Using centroid decomposition.
    
    Time: O(n log n), Space: O(n)
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    removed = [False] * n
    subtree_size = [0] * n
    result = 0
    
    def get_size(u: int, parent: int) -> int:
        subtree_size[u] = 1
        for v in graph[u]:
            if v != parent and not removed[v]:
                subtree_size[u] += get_size(v, u)
        return subtree_size[u]
    
    def find_centroid(u: int, parent: int, tree_size: int) -> int:
        for v in graph[u]:
            if v != parent and not removed[v]:
                if subtree_size[v] > tree_size // 2:
                    return find_centroid(v, u, tree_size)
        return u
    
    def get_paths(u: int, parent: int, current_sum: int, paths: List[int]):
        """Get all path sums from centroid."""
        paths.append(current_sum)
        for v in graph[u]:
            if v != parent and not removed[v]:
                get_paths(v, u, current_sum + values[v], paths)
    
    def count_pairs(centroid: int):
        """Count valid pairs through centroid."""
        nonlocal result
        
        # Count paths starting from centroid
        total_paths = Counter([values[centroid]])
        result += total_paths[k]
        
        for child in graph[centroid]:
            if not removed[child]:
                # Get paths in this subtree
                child_paths = []
                get_paths(child, centroid, values[centroid] + values[child], child_paths)
                
                # Count pairs with total_paths
                for path_sum in child_paths:
                    needed = k - path_sum
                    result += total_paths[needed]
                
                # Add to total_paths
                for path_sum in child_paths:
                    total_paths[path_sum] += 1
    
    def decompose(u: int):
        """Centroid decomposition."""
        tree_size = get_size(u, -1)
        centroid = find_centroid(u, -1, tree_size)
        
        removed[centroid] = True
        count_pairs(centroid)
        
        for v in graph[centroid]:
            if not removed[v]:
                decompose(v)
    
    decompose(0)
    return result

def find_k_distant_pairs(n: int, edges: List[List[int]], k: int) -> int:
    """
    LeetCode 2977: Count pairs of nodes with distance k.
    
    Using centroid decomposition.
    
    Time: O(n log n), Space: O(n)
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    removed = [False] * n
    subtree_size = [0] * n
    count = 0
    
    def get_size(u: int, parent: int) -> int:
        subtree_size[u] = 1
        for v in graph[u]:
            if v != parent and not removed[v]:
                subtree_size[u] += get_size(v, u)
        return subtree_size[u]
    
    def find_centroid(u: int, parent: int, tree_size: int) -> int:
        for v in graph[u]:
            if v != parent and not removed[v]:
                if subtree_size[v] > tree_size // 2:
                    return find_centroid(v, u, tree_size)
        return u
    
    def get_distances(u: int, parent: int, dist: int, distances: List[int]):
        """Get distances from centroid to all nodes in subtree."""
        distances.append(dist)
        for v in graph[u]:
            if v != parent and not removed[v]:
                get_distances(v, u, dist + 1, distances)
    
    def count_pairs_through_centroid(centroid: int):
        """Count pairs with distance k through centroid."""
        nonlocal count
        
        all_distances = Counter([0])  # Distance 0 for centroid itself
        
        for child in graph[centroid]:
            if not removed[child]:
                child_distances = []
                get_distances(child, centroid, 1, child_distances)
                
                # Count pairs between this subtree and previous subtrees
                for d in child_distances:
                    needed = k - d
                    count += all_distances[needed]
                
                # Add to all_distances
                for d in child_distances:
                    all_distances[d] += 1
    
    def decompose(u: int):
        tree_size = get_size(u, -1)
        centroid = find_centroid(u, -1, tree_size)
        
        removed[centroid] = True
        count_pairs_through_centroid(centroid)
        
        for v in graph[centroid]:
            if not removed[v]:
                decompose(v)
    
    decompose(0)
    return count

class DistanceQueries:
    """
    Handle distance queries using centroid decomposition.
    
    Preprocess: O(n log n)
    Query: O(log n)
    """
    
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        self.removed = [False] * n
        self.subtree_size = [0] * n
        self.centroid_parent = [-1] * n
        
        # For each node, store distances to all centroid ancestors
        self.dist_to_ancestors = [dict() for _ in range(n)]
        
        self._decompose(0, -1)
    
    def _get_size(self, u: int, parent: int) -> int:
        self.subtree_size[u] = 1
        for v in self.graph[u]:
            if v != parent and not self.removed[v]:
                self.subtree_size[u] += self._get_size(v, u)
        return self.subtree_size[u]
    
    def _find_centroid(self, u: int, parent: int, tree_size: int) -> int:
        for v in self.graph[u]:
            if v != parent and not self.removed[v]:
                if self.subtree_size[v] > tree_size // 2:
                    return self._find_centroid(v, u, tree_size)
        return u
    
    def _compute_distances(self, u: int, centroid: int, parent: int, dist: int):
        """Compute distances from centroid to all nodes."""
        self.dist_to_ancestors[u][centroid] = dist
        for v in self.graph[u]:
            if v != parent and not self.removed[v]:
                self._compute_distances(v, centroid, u, dist + 1)
    
    def _decompose(self, u: int, parent: int):
        tree_size = self._get_size(u, -1)
        centroid = self._find_centroid(u, -1, tree_size)
        
        self.removed[centroid] = True
        self.centroid_parent[centroid] = parent
        
        # Compute distances from centroid to all nodes in subtree
        self._compute_distances(centroid, centroid, -1, 0)
        
        for v in self.graph[centroid]:
            if not self.removed[v]:
                self._decompose(v, centroid)
    
    def distance(self, u: int, v: int) -> int:
        """
        Query distance between u and v.
        
        Time: O(log n)
        """
        min_dist = float('inf')
        
        # Walk up centroid tree
        curr = u
        while curr != -1:
            if curr in self.dist_to_ancestors[u] and curr in self.dist_to_ancestors[v]:
                dist = self.dist_to_ancestors[u][curr] + self.dist_to_ancestors[v][curr]
                min_dist = min(min_dist, dist)
            curr = self.centroid_parent[curr]
        
        return min_dist

# ============= Example Usage =============

def example_count_paths():
    """Example: Count paths with sum k"""
    n = 5
    edges = [[0, 1], [0, 2], [1, 3], [1, 4]]
    values = [1, 2, 3, 4, 5]
    k = 6
    
    count = count_paths_with_sum_k(n, edges, values, k)
    print(f"Paths with sum {k}: {count}")

def example_distance_queries():
    """Example: Distance queries"""
    n = 5
    edges = [[0, 1], [0, 2], [1, 3], [1, 4]]
    
    dq = DistanceQueries(n, edges)
    
    print(f"Distance(3, 4): {dq.distance(3, 4)}")  # 2
    print(f"Distance(3, 2): {dq.distance(3, 2)}")  # 3

```

---

## 🏆 Related LeetCode Problems

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 2049 | [Count Nodes With Highest Score](https://leetcode.com/problems/count-nodes-with-the-highest-score/) | Tree decomposition | O(n) | O(n) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 1617 | [Count Subtrees With Max Distance](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/) | Centroid + bitmask | O(n² 2ⁿ) | O(2ⁿ) |
| 2277 | [Closest Node to Path in Tree](https://leetcode.com/problems/closest-node-to-path-in-tree/) | Centroid decomp | O(n log n) | O(n log n) |
| 2791 | [Count Paths That Can Form Palindrome](https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/) | Centroid + XOR | O(n log n) | O(n) |

---

## 📊 When to Use Centroid Decomposition

```
Tree Problem
     |
     +-- Path counting with property → Centroid decomposition
     |   Examples: sum = k, length = k
     |
     +-- Distance queries
     |   +-- Multiple queries → Centroid + precompute
     |
     +-- Divide and conquer on tree
         +-- Needs O(log n) depth → Centroid decomposition

```

---

## 🎯 Key Insights

1. **Centroid removes balanced part** of tree
2. **Every path** passes through O(log n) centroids
3. **Decomposition depth** = O(log n)
4. **Total complexity** typically O(n log n)
5. **Powerful for path problems** that are hard otherwise

---

## 📚 References

| Resource | Link |
|----------|------|
| **Centroid Decomposition** | [CP-Algorithms](https://cp-algorithms.com/graph/centroid_decomposition.html) |
| **Tutorial** | [Codeforces](https://codeforces.com/blog/entry/81661) |
| **Video** | [Errichto](https://www.youtube.com/watch?v=nzF_9bjDzdc) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 04. HLD](../04_heavy_light_decomposition/README.md) | **05. Centroid Decomposition** | [06. DSU on Tree →](../06_dsu_on_tree/README.md) |

