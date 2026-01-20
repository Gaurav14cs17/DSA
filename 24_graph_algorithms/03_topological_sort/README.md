---
layout: default
title: "Topological Sort"
parent: "Graph Algorithms"
nav_order: 3
permalink: /24_graph_algorithms/03_topological_sort/
---

<div align="center">

# 📋 Topological Sort

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-10+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 02. MST](../02_minimum_spanning_tree/README.md) | **03. Topological Sort** | [04. Network Flow →](../04_network_flow/README.md) |

---

## 🎨 Visual Overview

<div align="center">

![Topological Sort - Kahn's Algorithm](./images/topological-sort.svg)

</div>

---

## 📐 Mathematical Foundations

### 1️⃣ Definition

**Topological ordering** of DAG $G = (V, E)$:

```math
\text{Linear ordering } v_1, v_2, \ldots, v_n \text{ where } (v_i, v_j) \in E \Rightarrow i < j

```

**Key property:** Every directed edge goes from earlier to later in the ordering.

**Existence:** Topological sort exists **if and only if** graph is a **DAG** (Directed Acyclic Graph).

---

### 2️⃣ Uniqueness

**Multiple orderings** may exist for same DAG.

**Example:**

```
A → C
B → C

```
Valid orderings: `[A, B, C]`, `[B, A, C]`

**Unique ordering** exists iff there's a Hamiltonian path.

---

### 3️⃣ Kahn's Algorithm (BFS-based)

**Intuition:** Process vertices with no incoming edges first.

**Algorithm:**
1. Compute in-degree for all vertices
2. Add all vertices with in-degree 0 to queue
3. While queue not empty:
   - Remove vertex $u$, add to result
   - Decrease in-degree of all neighbors
   - If neighbor's in-degree becomes 0, add to queue

**Time:** $O(V + E)$  
**Space:** $O(V)$

**Cycle Detection:** If result has fewer than $V$ vertices, cycle exists.

---

### 4️⃣ DFS-based Topological Sort

**Post-order DFS:** Vertex added to result after all descendants processed.

**Topological order = Reverse of finish order**

```math
\text{topo\_order} = \text{reverse}(\text{post\_order})

```

**Proof:** If $(u, v) \in E$, then $\text{finish}[u] > \text{finish}[v]$ in DFS.

**States:**
- **White (0):** Unvisited

- **Gray (1):** Visiting (in current DFS path)

- **Black (2):** Visited (finished)

**Cycle Detection:** If we reach a **gray** vertex, cycle exists.

---

### 5️⃣ Applications

| Application | Description |
|-------------|-------------|
| **Course Prerequisites** | Schedule courses respecting prerequisites |
| **Build Systems** | Compile dependencies in order |
| **Task Scheduling** | Execute tasks with dependencies |
| **Deadlock Detection** | Find circular dependencies |
| **Spreadsheet Formulas** | Evaluate cells in dependency order |

---

### 6️⃣ Lexicographically Smallest Topological Sort

Use **min-heap** instead of queue in Kahn's algorithm.

**Time:** $O(V \log V + E)$

Always pick the smallest available vertex.

---

### 7️⃣ All Topological Sorts

**Backtracking approach:**
- Try each vertex with in-degree 0
- Recursively generate orderings

**Time:** $O(V! \times E)$ in worst case (exponential)

---

## 💻 Code Implementations

```python
from collections import deque, defaultdict
from typing import List, Set, Tuple
import heapq

def topological_sort_kahn(n: int, edges: List[List[int]]) -> List[int]:
    """
    Kahn's Algorithm - BFS-based topological sort.
    
    Args:
        n: number of vertices (0 to n-1)
        edges: list of [u, v] representing edge u → v
    
    Returns:
        Topological ordering (empty list if cycle exists)
    
    Time: O(V+E), Space: O(V+E)
    """
    graph = defaultdict(list)
    in_degree = [0] * n
    
    # Build graph
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Start with vertices having in-degree 0
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        # Reduce in-degree of neighbors
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Check if valid topological order exists (no cycle)
    return result if len(result) == n else []

def topological_sort_dfs(n: int, edges: List[List[int]]) -> List[int]:
    """
    DFS-based topological sort.
    
    Returns reverse of post-order DFS.
    
    Time: O(V+E), Space: O(V+E)
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    # States: 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * n
    result = []
    has_cycle = False
    
    def dfs(u: int) -> None:
        nonlocal has_cycle
        if has_cycle:
            return
        
        if state[u] == 1:  # Back edge - cycle detected
            has_cycle = True
            return
        
        if state[u] == 2:  # Already processed
            return
        
        state[u] = 1  # Mark as visiting
        
        for v in graph[u]:
            dfs(v)
        
        state[u] = 2  # Mark as visited
        result.append(u)
    
    # Run DFS from all unvisited vertices
    for i in range(n):
        if state[i] == 0:
            dfs(i)
    
    if has_cycle:
        return []
    
    return result[::-1]  # Reverse post-order

def has_cycle_directed(n: int, edges: List[List[int]]) -> bool:
    """
    Detect cycle in directed graph using DFS.
    
    Time: O(V+E), Space: O(V+E)
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    state = [0] * n  # 0: unvisited, 1: visiting, 2: visited
    
    def dfs(u: int) -> bool:
        if state[u] == 1:  # Back edge - cycle
            return True
        if state[u] == 2:  # Already checked
            return False
        
        state[u] = 1
        for v in graph[u]:
            if dfs(v):
                return True
        state[u] = 2
        return False
    
    for i in range(n):
        if state[i] == 0:
            if dfs(i):
                return True
    
    return False

def lexicographical_topological_sort(n: int, edges: List[List[int]]) -> List[int]:
    """
    Lexicographically smallest topological ordering.
    
    Use min-heap instead of queue in Kahn's algorithm.
    
    Time: O(V log V + E), Space: O(V+E)
    """
    graph = defaultdict(list)
    in_degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Min-heap for lexicographically smallest
    heap = [i for i in range(n) if in_degree[i] == 0]
    heapq.heapify(heap)
    result = []
    
    while heap:
        u = heapq.heappop(heap)
        result.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)
    
    return result if len(result) == n else []

def all_topological_sorts(n: int, edges: List[List[int]]) -> List[List[int]]:
    """
    Generate all possible topological orderings.
    
    Using backtracking.
    
    Time: O(V! × E) worst case
    """
    graph = defaultdict(list)
    in_degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    result = []
    current = []
    visited = [False] * n
    
    def backtrack():
        if len(current) == n:
            result.append(current[:])
            return
        
        for u in range(n):
            if not visited[u] and in_degree[u] == 0:
                # Choose u
                visited[u] = True
                current.append(u)
                
                # Reduce in-degree of neighbors
                for v in graph[u]:
                    in_degree[v] -= 1
                
                backtrack()
                
                # Backtrack
                for v in graph[u]:
                    in_degree[v] += 1
                current.pop()
                visited[u] = False
    
    backtrack()
    return result

# ============= LeetCode Problems =============

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    LeetCode 207: Course Schedule
    
    Check if valid topological order exists (no cycle).
    
    Time: O(V+E), Space: O(V+E)
    """
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    count = 0
    
    while queue:
        u = queue.popleft()
        count += 1
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return count == numCourses

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    LeetCode 210: Course Schedule II
    
    Return a valid topological ordering.
    
    Time: O(V+E), Space: O(V+E)
    """
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return result if len(result) == numCourses else []

def alienOrder(words: List[str]) -> str:
    """
    LeetCode 269: Alien Dictionary
    
    Build graph from word comparisons, then topological sort.
    
    Time: O(C) where C = total characters
    Space: O(1) - at most 26 letters
    """
    # Build graph
    graph = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}
    
    # Compare adjacent words
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        
        # Invalid case: prefix comes after longer word
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        
        # Find first different character
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break
    
    # Topological sort
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []
    
    while queue:
        c = queue.popleft()
        result.append(c)
        
        for neighbor in graph[c]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if valid ordering (no cycle)
    if len(result) != len(in_degree):
        return ""
    
    return "".join(result)

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    """
    LeetCode 310: Minimum Height Trees
    
    Find centroids by removing leaves layer by layer.
    Similar to topological sort for undirected graph.
    
    Time: O(V), Space: O(V)
    """
    if n <= 2:
        return list(range(n))
    
    # Build adjacency list
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    # Initialize leaves (degree 1)
    leaves = deque([i for i in range(n) if len(graph[i]) == 1])
    remaining = n
    
    # Remove leaves layer by layer
    while remaining > 2:
        leaf_count = len(leaves)
        remaining -= leaf_count
        
        for _ in range(leaf_count):
            leaf = leaves.popleft()
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            
            if len(graph[neighbor]) == 1:
                leaves.append(neighbor)
    
    return list(leaves)

def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    """
    LeetCode 802: Find Eventual Safe States
    
    Safe node: all paths lead to terminal node (out-degree 0).
    
    Reverse graph and do topological sort.
    
    Time: O(V+E), Space: O(V+E)
    """
    n = len(graph)
    reverse_graph = defaultdict(list)
    out_degree = [0] * n
    
    # Build reverse graph
    for u in range(n):
        for v in graph[u]:
            reverse_graph[v].append(u)
        out_degree[u] = len(graph[u])
    
    # Start with terminal nodes (out-degree 0)
    queue = deque([i for i in range(n) if out_degree[i] == 0])
    safe = []
    
    while queue:
        u = queue.popleft()
        safe.append(u)
        
        for v in reverse_graph[u]:
            out_degree[v] -= 1
            if out_degree[v] == 0:
                queue.append(v)
    
    return sorted(safe)

def sortItems(n: int, m: int, group: List[int], 
              beforeItems: List[List[int]]) -> List[int]:
    """
    LeetCode 1203: Sort Items by Groups Respecting Dependencies
    
    Two-level topological sort: groups and items within groups.
    
    Time: O(V+E), Space: O(V+E)
    """
    # Assign unique group to items without group
    group_id = m
    for i in range(n):
        if group[i] == -1:
            group[i] = group_id
            group_id += 1
    
    # Build graphs
    item_graph = defaultdict(list)
    item_indegree = [0] * n
    group_graph = defaultdict(list)
    group_indegree = [0] * group_id
    
    for i in range(n):
        for j in beforeItems[i]:
            item_graph[j].append(i)
            item_indegree[i] += 1
            
            if group[i] != group[j]:
                group_graph[group[j]].append(group[i])
                group_indegree[group[i]] += 1
    
    # Topological sort helper
    def topo_sort(graph, indegree, nodes):
        queue = deque([i for i in nodes if indegree[i] == 0])
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        return result if len(result) == len(nodes) else []
    
    # Sort groups
    sorted_groups = topo_sort(group_graph, group_indegree, range(group_id))
    if not sorted_groups:
        return []
    
    # Sort items within each group
    group_items = defaultdict(list)
    for i in range(n):
        group_items[group[i]].append(i)
    
    result = []
    for g in sorted_groups:
        items = group_items[g]
        sorted_items = topo_sort(item_graph, item_indegree, items)
        if len(sorted_items) != len(items):
            return []
        result.extend(sorted_items)
    
    return result

```

---

## 🏆 LeetCode Problems

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Kahn's Algorithm | O(V+E) | O(V+E) |
| 210 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Topological Sort | O(V+E) | O(V+E) |
| 310 | [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) | Leaf Removal | O(V) | O(V) |
| 444 | [Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction/) | Unique Topo Sort | O(V+E) | O(V+E) |
| 802 | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | Reverse Topological | O(V+E) | O(V) |
| 1136 | [Parallel Courses](https://leetcode.com/problems/parallel-courses/) | Level-wise Topo | O(V+E) | O(V+E) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 269 | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Build Graph + Topo | O(C) | O(1) |
| 1203 | [Sort Items by Groups](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/) | Two-level Topo | O(V+E) | O(V+E) |
| 1591 | [Strange Printer II](https://leetcode.com/problems/strange-printer-ii/) | Topological Sort | O(mnc) | O(c²) |

---

## 📊 Algorithm Selection

```
Topological Sort
     |
     +-- Standard ordering → Kahn's (BFS) O(V+E)
     |
     +-- Need DFS → DFS-based O(V+E)
     |
     +-- Lexicographically smallest → Min-heap Kahn's O(V log V + E)
     |
     +-- Detect cycle → DFS with colors
     |
     +-- All orderings → Backtracking O(V!)

```

---

## 🎯 Key Insights

1. **Topological sort exists iff DAG** (no cycles)
2. **Kahn's algorithm** natural for level-by-level processing
3. **DFS approach** simpler code, post-order reversed
4. **Cycle detection** built into both algorithms
5. **Many applications** in scheduling and dependency resolution

---

## 📚 References

| Resource | Link |
|----------|------|
| **Topological Sort** | [Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting) |
| **Kahn's Algorithm** | [GeeksforGeeks](https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/) |
| **DAG** | [Wikipedia](https://en.wikipedia.org/wiki/Directed_acyclic_graph) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 02. MST](../02_minimum_spanning_tree/README.md) | **03. Topological Sort** | [04. Network Flow →](../04_network_flow/README.md) |

