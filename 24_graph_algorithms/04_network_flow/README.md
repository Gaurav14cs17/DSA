---
layout: default
title: "Network Flow"
parent: "Graph Algorithms"
nav_order: 4
permalink: /24_graph_algorithms/04_network_flow/
---

<div align="center">

# 🌊 Network Flow Algorithms

<p>
  <img src="https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-10+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 03. Topological Sort](../03_topological_sort/README.md) | **04. Network Flow** | [🏠 Home](../README.md) |

---

## 🎨 Visual Overview

<div align="center">

![Network Flow - Ford-Fulkerson / Edmonds-Karp](./images/network-flow.svg)

</div>

---

## 📐 Mathematical Foundations

### 1️⃣ Flow Network

**Flow network** $G = (V, E)$ with:
- Source $s \in V$
- Sink $t \in V$
- Capacity function $c: E \rightarrow \mathbb{R}^+$

**Flow** $f: E \rightarrow \mathbb{R}$ satisfies:

**Capacity constraint:**

```math
0 \leq f(u, v) \leq c(u, v) \quad \forall (u,v) \in E

```

**Flow conservation:**

```math
\sum_{v:(u,v) \in E} f(u,v) = \sum_{v:(v,u) \in E} f(v,u) \quad \forall u \in V \setminus \{s,t\}

```

---

### 2️⃣ Maximum Flow Problem

**Goal:** Maximize $|f| = \sum\_{v:(s,v) \in E} f(s,v)$

**Ford-Fulkerson Method:** Augment flow along paths until no augmenting path exists.

---

### 3️⃣ Residual Graph

**Residual capacity:**

```math
c_f(u,v) = \begin{cases}
c(u,v) - f(u,v) & \text{if } (u,v) \in E \\
f(v,u) & \text{if } (v,u) \in E \\
0 & \text{otherwise}
\end{cases}

```

**Augmenting path:** Path from $s$ to $t$ in residual graph with positive capacity.

---

### 4️⃣ Max-Flow Min-Cut Theorem

**Cut** $(S, T)$: Partition of $V$ with $s \in S$, $t \in T$.

**Capacity of cut:**

```math
c(S, T) = \sum_{u \in S, v \in T, (u,v) \in E} c(u,v)

```

**Theorem:**

```math
\max_{f \text{ flow}} |f| = \min_{(S,T) \text{ cut}} c(S,T)

```

---

### 5️⃣ Ford-Fulkerson Algorithm

**Method:**
1. Start with zero flow
2. While augmenting path exists in residual graph:
   - Find augmenting path (BFS or DFS)
   - Compute bottleneck capacity
   - Augment flow along path

**Time:** $O(E \cdot |f^*|)$ where $|f^*|$ is max flow value

**Issue:** Can be slow if capacities are irrational.

---

### 6️⃣ Edmonds-Karp Algorithm

**Ford-Fulkerson using BFS** for shortest augmenting path.

**Time:** $O(VE^2)$

**Guarantee:** At most $VE$ augmentations.

---

### 7️⃣ Dinic's Algorithm

**Level graph:** Use BFS to assign levels to vertices.

**Blocking flow:** Augment along shortest paths until no more paths at current level.

**Time:** $O(V^2 E)$ general, $O(E \sqrt{V})$ for unit capacity

---

### 8️⃣ Push-Relabel Algorithm

**Preflow:** Relax flow conservation at intermediate steps.

**Operations:**
- **Push:** Send excess flow to neighbor
- **Relabel:** Increase height of vertex

**Time:** $O(V^2 E)$ generic, $O(V^3)$ with heuristics

---

### 9️⃣ Bipartite Matching

**Maximum matching** in bipartite graph = **Maximum flow** with:
- Source connected to left partition (capacity 1)
- Right partition connected to sink (capacity 1)
- Original edges (capacity 1)

```math
\text{Max matching} = |f^*|

```

**König's Theorem:** In bipartite graph,

```math
\text{Max matching} = \text{Min vertex cover}

```

---

### 🔟 Minimum Cut Applications

**Minimum cut** found by max-flow:
- After max-flow, run BFS/DFS from source in residual graph
- $S$ = reachable vertices, $T$ = unreachable vertices
- Cut edges: $(u, v)$ where $u \in S, v \in T$

---

## 💻 Code Implementations

```python
from collections import deque, defaultdict
from typing import List, Dict, Set, Tuple

class MaxFlow:
    """Maximum Flow using Edmonds-Karp (BFS-based Ford-Fulkerson)."""
    
    def __init__(self, n: int):
        """
        Initialize flow network.
        
        Args:
            n: number of vertices (0 to n-1)
        """
        self.n = n
        self.graph = defaultdict(lambda: defaultdict(int))
    
    def add_edge(self, u: int, v: int, capacity: int):
        """Add directed edge with capacity."""
        self.graph[u][v] += capacity
    
    def bfs(self, source: int, sink: int, parent: Dict[int, int]) -> bool:
        """
        BFS to find augmenting path in residual graph.
        
        Returns True if path exists, fills parent array.
        """
        visited = set([source])
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            for v in self.graph[u]:
                if v not in visited and self.graph[u][v] > 0:
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
        
        return False
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute maximum flow using Edmonds-Karp.
        
        Time: O(VE²), Space: O(V+E)
        """
        parent = {}
        max_flow_value = 0
        
        # While augmenting path exists
        while self.bfs(source, sink, parent):
            # Find bottleneck capacity
            path_flow = float('inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = u
            
            # Augment flow along path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u
            
            max_flow_value += path_flow
            parent = {}
        
        return max_flow_value
    
    def min_cut(self, source: int, sink: int) -> Tuple[int, Set[Tuple[int, int]]]:
        """
        Find minimum cut after computing max flow.
        
        Returns: (cut_value, cut_edges)
        """
        # Compute max flow first
        flow_value = self.max_flow(source, sink)
        
        # Find reachable vertices from source in residual graph
        visited = set([source])
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if v not in visited and self.graph[u][v] > 0:
                    visited.add(v)
                    queue.append(v)
        
        # Cut edges: from reachable to non-reachable
        cut_edges = set()
        for u in visited:
            for v in self.graph[u]:
                if v not in visited:
                    cut_edges.add((u, v))
        
        return flow_value, cut_edges

class Dinic:
    """Dinic's algorithm for maximum flow."""
    
    def __init__(self, n: int):
        self.n = n
        self.graph = defaultdict(lambda: defaultdict(int))
    
    def add_edge(self, u: int, v: int, capacity: int):
        self.graph[u][v] += capacity
    
    def bfs(self, source: int, sink: int, level: List[int]) -> bool:
        """Build level graph using BFS."""
        level[:] = [-1] * self.n
        level[source] = 0
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if level[v] < 0 and self.graph[u][v] > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        
        return level[sink] >= 0
    
    def dfs(self, u: int, sink: int, flow: int, level: List[int], 
            start: List[int]) -> int:
        """Send flow using DFS in level graph."""
        if u == sink:
            return flow
        
        for i in range(start[u], len(list(self.graph[u].keys()))):
            v = list(self.graph[u].keys())[i]
            start[u] = i
            
            if level[v] == level[u] + 1 and self.graph[u][v] > 0:
                curr_flow = min(flow, self.graph[u][v])
                temp_flow = self.dfs(v, sink, curr_flow, level, start)
                
                if temp_flow > 0:
                    self.graph[u][v] -= temp_flow
                    self.graph[v][u] += temp_flow
                    return temp_flow
        
        return 0
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute maximum flow using Dinic's algorithm.
        
        Time: O(V²E), Space: O(V+E)
        """
        if source == sink:
            return 0
        
        total_flow = 0
        level = [-1] * self.n
        
        while self.bfs(source, sink, level):
            start = [0] * self.n
            while True:
                flow = self.dfs(source, sink, float('inf'), level, start)
                if flow == 0:
                    break
                total_flow += flow
        
        return total_flow

def bipartite_matching(n1: int, n2: int, edges: List[Tuple[int, int]]) -> int:
    """
    Maximum bipartite matching using max flow.
    
    Args:
        n1: size of left partition (0 to n1-1)
        n2: size of right partition (0 to n2-1)
        edges: list of (left, right) edges
    
    Returns:
        Size of maximum matching
    
    Time: O(VE²), Space: O(V+E)
    """
    # Vertices: 0=source, 1..n1=left, n1+1..n1+n2=right, n1+n2+1=sink
    source = 0
    sink = n1 + n2 + 1
    flow = MaxFlow(n1 + n2 + 2)
    
    # Source to left partition
    for i in range(1, n1 + 1):
        flow.add_edge(source, i, 1)
    
    # Left to right
    for left, right in edges:
        flow.add_edge(left + 1, n1 + right + 1, 1)
    
    # Right to sink
    for i in range(n1 + 1, n1 + n2 + 1):
        flow.add_edge(i, sink, 1)
    
    return flow.max_flow(source, sink)

# ============= LeetCode Problems =============

def maxFlow(n: int, edges: List[List[int]], source: int, sink: int) -> int:
    """
    LeetCode 2850: Minimum Moves to Spread Stones
    
    Can be modeled as maximum flow problem.
    
    Time: O(VE²), Space: O(V+E)
    """
    flow = MaxFlow(n)
    for u, v, capacity in edges:
        flow.add_edge(u, v, capacity)
    return flow.max_flow(source, sink)

def findMaximizedCapital(k: int, w: int, profits: List[int], 
                         capital: List[int]) -> int:
    """
    LeetCode 502: IPO
    
    Not directly network flow, but greedy with heap.
    Included for comparison of problem types.
    
    Time: O(n log n), Space: O(n)
    """
    import heapq
    
    # Projects: (capital_needed, profit)
    projects = sorted(zip(capital, profits))
    available = []  # Max heap of profits
    idx = 0
    
    for _ in range(k):
        # Add all affordable projects
        while idx < len(projects) and projects[idx][0] <= w:
            heapq.heappush(available, -projects[idx][1])  # Max heap
            idx += 1
        
        if not available:
            break
        
        # Pick most profitable
        w += -heapq.heappop(available)
    
    return w

def maximumInvitations(grid: List[List[int]]) -> int:
    """
    LeetCode 1820: Maximum Number of Accepted Invitations
    
    Maximum bipartite matching problem.
    
    Time: O(mn · (m+n)), Space: O(m+n)
    """
    m, n = len(grid), len(grid[0])
    
    # boys: 0 to m-1, girls: 0 to n-1
    match_girl = [-1] * n  # match_girl[j] = boy matched to girl j
    
    def dfs(boy: int, visited: Set[int]) -> bool:
        """Try to find augmenting path for boy."""
        for girl in range(n):
            if grid[boy][girl] == 1 and girl not in visited:
                visited.add(girl)
                
                # If girl unmatched or can find alternate match for current partner
                if match_girl[girl] == -1 or dfs(match_girl[girl], visited):
                    match_girl[girl] = boy
                    return True
        
        return False
    
    matching = 0
    for boy in range(m):
        if dfs(boy, set()):
            matching += 1
    
    return matching

def minCut(s: str) -> int:
    """
    LeetCode 132: Palindrome Partitioning II
    
    Not network flow, but DP problem.
    Name is similar to "min-cut" but different problem.
    
    Time: O(n²), Space: O(n²)
    """
    n = len(s)
    
    # is_palindrome[i][j] = True if s[i:j+1] is palindrome
    is_palindrome = [[False] * n for _ in range(n)]
    
    for i in range(n):
        is_palindrome[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                is_palindrome[i][j] = (length == 2 or is_palindrome[i + 1][j - 1])
    
    # dp[i] = minimum cuts needed for s[0:i+1]
    dp = [float('inf')] * n
    
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_palindrome[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[n - 1]

def minCostMaxFlow(n: int, edges: List[List[int]], source: int, 
                   sink: int, max_flow: int) -> int:
    """
    Minimum Cost Maximum Flow (MCMF).
    
    Find cheapest way to send max_flow units from source to sink.
    
    Uses Bellman-Ford for shortest augmenting path.
    
    Time: O(flow · VE), Space: O(V+E)
    """
    graph = defaultdict(lambda: defaultdict(lambda: [0, 0]))  # [capacity, cost]
    
    for u, v, capacity, cost in edges:
        graph[u][v] = [capacity, cost]
    
    total_cost = 0
    flow_sent = 0
    
    while flow_sent < max_flow:
        # Find shortest path (minimum cost) using Bellman-Ford
        dist = defaultdict(lambda: float('inf'))
        dist[source] = 0
        parent = {}
        
        # Bellman-Ford
        for _ in range(n - 1):
            for u in graph:
                for v in graph[u]:
                    cap, cost = graph[u][v]
                    if cap > 0 and dist[u] + cost < dist[v]:
                        dist[v] = dist[u] + cost
                        parent[v] = u
        
        # If no path to sink
        if dist[sink] == float('inf'):
            break
        
        # Find bottleneck
        path_flow = max_flow - flow_sent
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v][0])
            v = u
        
        # Augment flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v][0] -= path_flow
            graph[v][u][0] += path_flow
            graph[v][u][1] = -graph[u][v][1]
            total_cost += path_flow * graph[u][v][1]
            v = u
        
        flow_sent += path_flow
    
    return total_cost if flow_sent == max_flow else -1

```

---

## 🏆 LeetCode Problems

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 1820 | [Maximum Number of Accepted Invitations](https://leetcode.com/problems/maximum-number-of-accepted-invitations/) | Bipartite Matching | O(mn(m+n)) | O(m+n) |
| 2077 | [Paths in Maze That Lead to Same Room](https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/) | Graph Theory | O(E²/V) | O(V+E) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 1671 | [Minimum Number of Removals](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) | DP (not flow) | O(n log n) | O(n) |
| 2323 | [Find Minimum Time to Finish All Jobs II](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/) | Greedy | O(n log n) | O(1) |
| 2850 | [Minimum Moves to Spread Stones](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/) | Flow/Assignment | O(n!·n²) | O(n²) |

---

## 📊 Algorithm Selection

```
Network Flow Problem
     |
     +-- General max flow
     |   +-- Small graph → Ford-Fulkerson O(E·|f*|)
     |   +-- Integer capacities → Edmonds-Karp O(VE²)
     |   +-- Best performance → Dinic O(V²E)
     |
     +-- Unit capacities → Dinic O(E√V)
     |
     +-- Bipartite matching → Max flow with capacity 1
     |
     +-- Min cost max flow → Bellman-Ford + augmenting paths
     |
     +-- Min cut → Max flow + BFS in residual graph

```

---

## 🎯 Key Insights

1. **Max-flow = Min-cut** fundamental theorem
2. **Bipartite matching** reduces to max flow
3. **Residual graph** crucial for finding augmenting paths
4. **Edmonds-Karp** guarantees polynomial time
5. **Dinic's algorithm** often fastest in practice
6. **Push-relabel** good for dense graphs

---

## 📚 References

| Resource | Link |
|----------|------|
| **Maximum Flow** | [Wikipedia](https://en.wikipedia.org/wiki/Maximum_flow_problem) |
| **Ford-Fulkerson** | [Wikipedia](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm) |
| **Dinic's Algorithm** | [Wikipedia](https://en.wikipedia.org/wiki/Dinic%27s_algorithm) |
| **Bipartite Matching** | [Wikipedia](https://en.wikipedia.org/wiki/Matching_(graph_theory)) |
| **Min-Cut Max-Flow** | [Wikipedia](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem) |

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 03. Topological Sort](../03_topological_sort/README.md) | **04. Network Flow** | [🏠 Home](../README.md) |

