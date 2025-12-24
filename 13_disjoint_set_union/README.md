---
layout: default
title: "Disjoint Set Union"
nav_order: 22
has_children: false
permalink: /13_disjoint_set_union/
---

<div align="center">

# 🔗 Disjoint Set Union (DSU)

**See [Union-Find](../12_union_find/README.md) for complete documentation.**

</div>

---

## Quick Reference

DSU (Disjoint Set Union) is also known as **Union-Find**.

### Key Operations

| Operation | Complexity |
|-----------|:----------:|
| `find(x)` | O(α(n)) ≈ O(1) |
| `union(x, y)` | O(α(n)) ≈ O(1) |
| `connected(x, y)` | O(α(n)) ≈ O(1) |

### Optimizations

1. **Path Compression:** Flatten tree during find
2. **Union by Rank/Size:** Attach smaller tree to larger

---

[📖 Full Documentation →](../12_union_find/README.md)

---

<div align="center">

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

</div>
