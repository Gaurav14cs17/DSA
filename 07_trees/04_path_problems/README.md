---
layout: default
title: "Path Problems"
parent: "Trees"
nav_order: 4
permalink: /07_trees/04_path_problems/
---

<div align="center">

# 🛤️ Path Problems

![Path Problems Diagram](./images/path-problems.svg)

<p>
  <img src="https://img.shields.io/badge/Difficulty-Medium_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-10+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 03. Tree Properties](../03_tree_properties/README.md) | **04. Path Problems** | [05. LCA & Ancestor →](../05_lca_ancestor/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Path Types

**Root-to-Leaf Path:**

$$\text{path}(root, leaf) = [root, ..., leaf]$$

**Any-to-Any Path (through some node):**

$$\text{path}(u, v) = \text{path}(u, lca) + \text{path}(lca, v)$$

---

### 2️⃣ Path Sum (Root-to-Leaf)

**Check if path with sum $S$ exists:**

$$\text{hasPath}(node, S) = \begin{cases}
S = node.val & \text{if leaf} \\
\text{hasPath}(left, S - node.val) \lor \text{hasPath}(right, S - node.val) & \text{otherwise}
\end{cases}$$

---

### 3️⃣ Maximum Path Sum

**Key Insight:** Max path passes through some node as the "turning point."

$$\text{maxSum}(node) = node.val + \max(0, \text{gain}(left)) + \max(0, \text{gain}(right))$$

Where:

$$\text{gain}(node) = node.val + \max(\text{gain}(left), \text{gain}(right), 0)$$

**Global answer:** Maximum of `maxSum` over all nodes.

---

### 4️⃣ Path Sum with Prefix Sum

**Problem:** Count paths with sum $k$ (not necessarily root-to-leaf).

**Key Identity:**

$$\text{pathSum}(i, j) = prefix[j] - prefix[i-1] = k
prefix[i-1] = prefix[j] - k$$

Count previous prefixes that equal $prefix[j] - k$.

---

### 5️⃣ Binary Tree Paths

**All root-to-leaf paths:**

$$\text{paths}(node) = \bigcup_{leaf \in \text{leaves}} \text{path}(root, leaf)$$

---

## 💻 Code Implementations

```python
def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    """
    Check if root-to-leaf path with given sum exists.
    
    Subtract node value, check if leaf reached with sum 0.
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return False
    
    targetSum -= root.val
    
    # Check if leaf
    if not root.left and not root.right:
        return targetSum == 0
    
    return (hasPathSum(root.left, targetSum) or 
            hasPathSum(root.right, targetSum))

def pathSum(root: TreeNode, targetSum: int) -> list[list[int]]:
    """
    Find all root-to-leaf paths with given sum.
    
    Backtracking with path tracking.
    
    Time: O(n²), Space: O(n)
    """
    result = []
    
    def dfs(node, remaining, path):
        if not node:
            return
        
        path.append(node.val)
        remaining -= node.val
        
        if not node.left and not node.right and remaining == 0:
            result.append(path[:])
        else:
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)
        
        path.pop()  # Backtrack
    
    dfs(root, targetSum, [])
    return result

def maxPathSum(root: TreeNode) -> int:
    """
    Maximum path sum (any node to any node).
    
    For each node: max path through it as turning point.
    Gain = max contribution from one side.
    
    Time: O(n), Space: O(h)
    """
    max_sum = [float('-inf')]
    
    def gain(node):
        if not node:
            return 0
        
        # Max gain from left/right (take 0 if negative)
        left_gain = max(gain(node.left), 0)
        right_gain = max(gain(node.right), 0)
        
        # Path through this node as turning point
        path_sum = node.val + left_gain + right_gain
        max_sum[0] = max(max_sum[0], path_sum)
        
        # Return max gain from this node
        return node.val + max(left_gain, right_gain)
    
    gain(root)
    return max_sum[0]

def pathSumIII(root: TreeNode, targetSum: int) -> int:
    """
    Count paths with sum = target (not necessarily root-to-leaf).
    
    Use prefix sum: count previous prefixes that equal prefix - target.
    
    Time: O(n), Space: O(h)
    """
    from collections import defaultdict
    
    count = [0]
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    
    def dfs(node, prefix_sum):
        if not node:
            return
        
        prefix_sum += node.val
        
        # Count paths ending here
        count[0] += prefix_count[prefix_sum - targetSum]
        
        # Add current prefix
        prefix_count[prefix_sum] += 1
        
        dfs(node.left, prefix_sum)
        dfs(node.right, prefix_sum)
        
        # Backtrack
        prefix_count[prefix_sum] -= 1
    
    dfs(root, 0)
    return count[0]

def binaryTreePaths(root: TreeNode) -> list[str]:
    """
    All root-to-leaf paths as strings.
    
    Time: O(n), Space: O(n)
    """
    if not root:
        return []
    
    result = []
    
    def dfs(node, path):
        if not node.left and not node.right:
            result.append(path)
            return
        
        if node.left:
            dfs(node.left, path + "->" + str(node.left.val))
        if node.right:
            dfs(node.right, path + "->" + str(node.right.val))
    
    dfs(root, str(root.val))
    return result

def sumNumbers(root: TreeNode) -> int:
    """
    Sum of all root-to-leaf numbers.
    
    Each path forms a number: 1->2->3 = 123
    
    Time: O(n), Space: O(h)
    """
    def dfs(node, current_num):
        if not node:
            return 0
        
        current_num = current_num * 10 + node.val
        
        if not node.left and not node.right:
            return current_num
        
        return dfs(node.left, current_num) + dfs(node.right, current_num)
    
    return dfs(root, 0)

```

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | DFS | O(n) | O(h) |
| 257 | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | DFS | O(n) | O(n) |

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 113 | [Path Sum II](https://leetcode.com/problems/path-sum-ii/) | Backtracking | O(n²) | O(n) |
| 129 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | DFS | O(n) | O(h) |
| 437 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Prefix Sum | O(n) | O(h) |
| 666 | [Path Sum IV](https://leetcode.com/problems/path-sum-iv/) | Map Representation | O(n) | O(n) |
| 988 | [Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/) | DFS | O(n) | O(n) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Gain Calculation | O(n) | O(h) |

---

---

## 🎨 Visual Algorithm Walkthrough

### Maximum Path Sum (#124)

```
Tree:
      -10
      /  \
     9    20
         /  \
        15   7

For each node, calculate:
  gain = val + max(gain(left), gain(right), 0)
  path_through = val + max(0, gain(left)) + max(0, gain(right))

Node 9:
  gain = 9
  path_through = 9
  max_so_far = 9

Node 15:
  gain = 15
  path_through = 15
  max_so_far = 15

Node 7:
  gain = 7
  path_through = 7
  max_so_far = 15

Node 20:
  gain(left) = 15, gain(right) = 7
  gain = 20 + max(15, 7) = 35
  path_through = 20 + 15 + 7 = 42 ✓
  max_so_far = 42

Node -10:
  gain(left) = 9, gain(right) = 35
  gain = -10 + 35 = 25
  path_through = -10 + 9 + 35 = 34
  max_so_far = 42

Result: 42 (path: 15 → 20 → 7)

```

### Path Sum III (#437)

```
Tree:      targetSum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Prefix sum approach:
Current path: [10]
  prefix_sum = 10
  count += prefix_count[10-8=2] = 0

Current path: [10, 5]
  prefix_sum = 15
  count += prefix_count[15-8=7] = 0

Current path: [10, 5, 3]
  prefix_sum = 18
  count += prefix_count[18-8=10] = 1 ✓ (path: 5→3)

Current path: [10, 5, 3, 3]
  prefix_sum = 21
  count += prefix_count[21-8=13] = 0

Backtrack and explore other paths...

Paths found:

1. 10 → 5 → 3 (sum=18)... wait, we want exactly 8
2. 5 → 3 (sum=8) ✓

3. 10 → -3 → 11 (sum=18)... no

4. -3 → 11 (sum=8) ✓

Result: 3 paths with sum=8

```

### Path Sum II (#113)

```
Tree:      targetSum = 22
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

DFS with backtracking:

Path 1: [5, 4, 11, 7]
  sum = 27 ≠ 22 ✗

Path 2: [5, 4, 11, 2]
  sum = 22 ✓
  Add to result

Path 3: [5, 8, 13]
  sum = 26 ≠ 22 ✗

Path 4: [5, 8, 4, 1]
  sum = 18 ≠ 22 ✗

Result: [[5, 4, 11, 2]]

```

---

## 💡 Pattern Recognition Guide

| Problem Keywords | Pattern | Example |
|-----------------|---------|---------|
| "path sum equals k" | DFS with target | #112 |
| "all paths with sum k" | Backtracking | #113 |
| "any-to-any path sum" | Prefix sum | #437 |
| "maximum path sum" | Gain calculation | #124 |
| "root-to-leaf paths" | DFS with path | #257 |
| "sum of path numbers" | Build number | #129 |

---

## 📚 References & Learning Resources

### 📖 Core Concepts

| Resource | Topic | Link |
|----------|-------|------|
| **GeeksforGeeks** | Path problems | [Tutorial](https://www.geeksforgeeks.org/print-paths-root-specified-sum-binary-tree/) |
| **GeeksforGeeks** | Maximum path sum | [Tutorial](https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/) |
| **LeetCode** | Path Sum III explanation | [Discussion](https://leetcode.com/problems/path-sum-iii/) |

### 📺 Video Tutorials

| Creator | Topic | Link |
|---------|-------|------|
| **NeetCode** | Maximum Path Sum | [YouTube](https://www.youtube.com/watch?v=Hr5cWUld4vU) |
| **NeetCode** | Path Sum III | [YouTube](https://www.youtube.com/watch?v=uZzvivFkgtM) |
| **Back To Back SWE** | Path problems | [YouTube](https://www.youtube.com/watch?v=GF4McxL3bMg) |

### 🎯 Practice Collections

| Platform | Focus | Link |
|----------|-------|------|
| **LeetCode** | Path sum tag | [Problems](https://leetcode.com/tag/tree/) |
| **HackerRank** | Tree path problems | [Practice](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=trees) |

### 🔬 Advanced Topics

| Topic | Description | Link |
|-------|-------------|------|
| **Prefix Sum in Trees** | Any-to-any paths | [Tutorial](https://www.geeksforgeeks.org/count-paths-with-given-sum-in-a-binary-tree/) |
| **Backtracking in Trees** | All paths enumeration | [Article](https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/) |

### 📊 Visualization

| Tool | Purpose | Link |
|------|---------|------|
| **VisuAlgo** | Tree paths | [Website](https://visualgo.net/en/bst) |

---

## 💡 Pro Tips

> **🎯 Path Sum = Subtract:** Instead of tracking sum, subtract node value from target. Check if 0 at leaf!

> **⚡ Max Path = Gain + Global:** For each node: gain (one direction) vs path_through (both directions). Track global max!

> **🔍 Prefix Sum for Any-to-Any:** Use hash map to count prefix sums. `count[prefix - k]` gives paths ending at current node!

> **📊 Backtracking for All Paths:** Add node, recurse, remove node (backtrack). Copies full path when reaching leaf!

> **🌊 Build Number = 10×parent + current:** For paths like 1→2→3 = 123, use `num*10 + val` recursively!

---

## 🎖️ Practice Roadmap

**Week 1: Basic Path Problems**

1. Solve #112 (Path Sum) - DFS foundation

2. Solve #257 (Binary Tree Paths) - All paths

3. Solve #129 (Sum Numbers) - Build number pattern

**Week 2: Advanced Path Problems**

4. Solve #113 (Path Sum II) - Backtracking for all paths

5. Solve #437 (Path Sum III) - Prefix sum technique

6. Solve #124 (Max Path Sum) - Gain calculation

**Week 3: Practice & Master**

7. Solve #988 (Smallest String) - Lexicographic paths

8. Review all patterns and optimize solutions

---

## ❓ Interview Q&A

**Q: What's the difference between Path Sum I, II, and III?**  
A: I: Check if exists (boolean). II: Find all paths (backtracking). III: Count any-to-any paths (prefix sum).

**Q: Why use prefix sum for Path Sum III?**  
A: Allows checking any-to-any paths in O(n). For each node, `count[prefix - k]` gives paths ending there with sum k!

**Q: How to calculate max path sum efficiently?**  
A: For each node: calculate gain (one direction) for recursion, but check `val + left_gain + right_gain` for global max!

**Q: Why backtrack in Path Sum II?**  
A: Need to enumerate all valid paths. Add node, explore, remove node (backtrack) to try other paths!

**Q: How to handle negative values in max path sum?**  
A: Use `max(0, gain)` when adding to path. Negative contributions can be ignored!

---

## 🔥 Key Insights

- **Root-to-Leaf:** DFS with target subtraction

- **All Paths:** Backtracking with path tracking

- **Any-to-Any:** Prefix sum in hash map

- **Max Path Sum:** Gain (one way) vs path_through (both ways)

- **Build Numbers:** `num = num * 10 + val` pattern

---

<div align="center">

**Made with ❤️ for the coding community by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 03. Tree Properties](../03_tree_properties/README.md) | **04. Path Problems** | [05. LCA & Ancestor →](../05_lca_ancestor/README.md) |
