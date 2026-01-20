---
layout: default
title: "Single Pattern Matching"
parent: "Rabin-Karp Algorithm"
grand_parent: "String Algorithms"
nav_order: 2

---

# 🎯 Single Pattern Matching with Rabin-Karp

## 📊 Visual Overview

![Single Pattern Matching](./images/single-pattern.svg)

## 📊 Metadata
- **Difficulty:** ![Easy-Medium](https://img.shields.io/badge/Easy--Medium-yellow)
- **Time Complexity:** O(n + m) average
- **Space Complexity:** O(1)
- **Pattern:** Pattern Matching, Hash Comparison

---

## 🎯 Overview

Single pattern matching finds all occurrences of one pattern in text using rolling hash for O(1) window comparisons.

---

## 📐 Algorithm Steps

```
1. Compute hash of pattern: O(m)
2. Compute hash of first window: O(m)
3. For each position:
   a. Compare hashes: O(1)
   b. If match, verify string: O(m)
   c. Roll hash: O(1)
4. Total: O(n + m) average, O(nm) worst
```

---

## 💻 Implementations

### 1. Basic Pattern Matching

```python
def rabin_karp_search(text, pattern, base=31, mod=10**9 + 7):
    """
    Find all occurrences of pattern in text
    
    Time: O(n + m) average
    Space: O(1)
    
    Returns: List of starting indices
    """
    n, m = len(text), len(pattern)
    
    if m > n or m == 0:
        return []
    
    # Compute pattern hash
    pattern_hash = 0
    for c in pattern:
        pattern_hash = (pattern_hash * base + ord(c)) % mod
    
    # Precompute power = base^(m-1) mod
    power = pow(base, m - 1, mod)
    
    # Compute first window hash
    window_hash = 0
    for i in range(m):
        window_hash = (window_hash * base + ord(text[i])) % mod
    
    matches = []
    
    # Check all positions
    for i in range(n - m + 1):

        # Hash match - verify actual string
        if window_hash == pattern_hash:
            if text[i:i+m] == pattern:
                matches.append(i)
        
        # Roll hash to next position
        if i < n - m:

            # Remove leftmost
            window_hash = (window_hash - ord(text[i]) * power % mod + mod) % mod

            # Shift and add rightmost
            window_hash = (window_hash * base + ord(text[i+m])) % mod
    
    return matches

# Examples
text = "AABAACAADAABAABA"
pattern = "AABA"
print(rabin_karp_search(text, pattern))  # [0, 9, 12]
```

### 2. First Occurrence Only

```python
def find_first_occurrence_rk(text, pattern, base=31, mod=10**9 + 7):
    """
    Find first occurrence of pattern
    
    LeetCode 28: Implement strStr()
    
    Time: O(n + m) average
    Returns: Index of first occurrence, or -1
    """
    n, m = len(text), len(pattern)
    
    if m == 0:
        return 0
    if m > n:
        return -1
    
    # Pattern hash
    p_hash = 0
    for c in pattern:
        p_hash = (p_hash * base + ord(c)) % mod
    
    # Power
    power = pow(base, m - 1, mod)
    
    # Window hash
    w_hash = 0
    for i in range(m):
        w_hash = (w_hash * base + ord(text[i])) % mod
    
    # Search
    for i in range(n - m + 1):
        if w_hash == p_hash and text[i:i+m] == pattern:
            return i  # Found! Return immediately
        
        if i < n - m:
            w_hash = (w_hash - ord(text[i]) * power % mod + mod) % mod
            w_hash = (w_hash * base + ord(text[i+m])) % mod
    
    return -1

# Examples
print(find_first_occurrence_rk("hello", "ll"))    # 2
print(find_first_occurrence_rk("aaaaa", "bba"))   # -1
```

### 3. Count Occurrences (Overlapping)

```python
def count_pattern_rk(text, pattern):
    """
    Count all occurrences (including overlapping)
    
    Time: O(n + m) average
    """
    matches = rabin_karp_search(text, pattern)
    return len(matches)

# Example
text = "AABAACAADAABAABA"
pattern = "AABA"
print(f"Pattern '{pattern}' occurs {count_pattern_rk(text, pattern)} times")
```

### 4. Case-Insensitive Matching

```python
def rabin_karp_case_insensitive(text, pattern, base=31, mod=10**9 + 7):
    """
    Case-insensitive pattern matching
    
    Time: O(n + m)
    Space: O(n + m)
    """
    text_lower = text.lower()
    pattern_lower = pattern.lower()
    
    return rabin_karp_search(text_lower, pattern_lower, base, mod)

# Example
text = "Hello World, HELLO world"
pattern = "hello"
matches = rabin_karp_case_insensitive(text, pattern)
print(f"Found at: {matches}")  # [0, 13]
```

### 5. Pattern with Don't Care Characters

```python
def rabin_karp_wildcard(text, pattern, wildcard='?', base=31, mod=10**9 + 7):
    """
    Match pattern with wildcard characters
    
    '?' matches any single character
    
    Time: O(n * m) worst case (must verify each match)
    """
    n, m = len(text), len(pattern)
    
    if m > n:
        return []
    
    def matches_with_wildcard(text_substr, pattern):
        """Check if text matches pattern with wildcards"""
        for i in range(len(pattern)):
            if pattern[i] != wildcard and text_substr[i] != pattern[i]:
                return False
        return True
    
    matches = []
    
    # Compute hash only for non-wildcard positions
    pattern_positions = []
    pattern_chars = []
    
    for i, c in enumerate(pattern):
        if c != wildcard:
            pattern_positions.append(i)
            pattern_chars.append(ord(c))
    
    # If all wildcards, every position matches
    if not pattern_positions:
        return list(range(n - m + 1))
    
    # Search using partial hash
    for i in range(n - m + 1):
        if matches_with_wildcard(text[i:i+m], pattern):
            matches.append(i)
    
    return matches

# Example
text = "ABABDABAC"
pattern = "AB?D"
matches = rabin_karp_wildcard(text, pattern)
print(f"Pattern '{pattern}' found at: {matches}")
```

### 6. Longest Match

```python
def longest_matching_prefix(text, pattern, base=31, mod=10**9 + 7):
    """
    Find length of longest prefix of pattern that matches in text
    
    Time: O(n * m) worst case
    Space: O(1)
    
    Returns: (max_length, position)
    """
    n, m = len(text), len(pattern)
    max_len = 0
    best_pos = -1
    
    for length in range(1, m + 1):

        # Try to find pattern[:length] in text
        p_hash = 0
        for c in pattern[:length]:
            p_hash = (p_hash * base + ord(c)) % mod
        
        power = pow(base, length - 1, mod) if length > 1 else 1
        
        w_hash = 0
        if length <= n:
            for i in range(length):
                w_hash = (w_hash * base + ord(text[i])) % mod
        
        for i in range(n - length + 1):
            if w_hash == p_hash and text[i:i+length] == pattern[:length]:
                if length > max_len:
                    max_len = length
                    best_pos = i
                break
            
            if i < n - length:
                w_hash = (w_hash - ord(text[i]) * power % mod + mod) % mod
                w_hash = (w_hash * base + ord(text[i+length])) % mod
    
    return max_len, best_pos

# Example
text = "ABCDEFGH"
pattern = "CDEFXYZ"
length, pos = longest_matching_prefix(text, pattern)
print(f"Longest match: {length} chars at position {pos}")
```

### 7. Match with Mismatches

```python
def rabin_karp_k_mismatches(text, pattern, k, base=31, mod=10**9 + 7):
    """
    Find matches allowing up to k mismatches
    
    Time: O(n * m) - must verify each position
    Space: O(1)
    
    Returns: List of (position, num_mismatches)
    """
    n, m = len(text), len(pattern)
    
    if m > n:
        return []
    
    def count_mismatches(s1, s2):
        """Count character differences"""
        return sum(c1 != c2 for c1, c2 in zip(s1, s2))
    
    matches = []
    
    for i in range(n - m + 1):
        mismatches = count_mismatches(text[i:i+m], pattern)
        if mismatches <= k:
            matches.append((i, mismatches))
    
    return matches

# Example
text = "ABABDABAC"
pattern = "ABCD"
matches = rabin_karp_k_mismatches(text, pattern, k=2)
print("Matches with ≤2 mismatches:")
for pos, mm in matches:
    print(f"  Position {pos}: {mm} mismatches")
```

---

## 🧩 LeetCode Problems

### Easy
| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 28 | [Implement strStr()](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 🟢 Easy | First occurrence |
| 796 | [Rotate String](https://leetcode.com/problems/rotate-string/) | 🟢 Easy | Pattern in doubled |

### Medium
| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 686 | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) | 🟡 Medium | Pattern in repeated |
| 1668 | [Maximum Repeating Substring](https://leetcode.com/problems/maximum-repeating-substring/) | 🟡 Medium | Count consecutive |

---

## 💡 Solutions

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        LeetCode 28: Implement strStr()
        
        Returns index of first occurrence or -1
        """
        if not needle:
            return 0
        
        BASE, MOD = 31, 10**9 + 7
        n, m = len(haystack), len(needle)
        
        if m > n:
            return -1
        
        # Pattern hash
        p_hash = 0
        for c in needle:
            p_hash = (p_hash * BASE + ord(c)) % MOD
        
        # Power
        power = pow(BASE, m - 1, MOD)
        
        # Window hash
        w_hash = 0
        for i in range(m):
            w_hash = (w_hash * BASE + ord(haystack[i])) % MOD
        
        # Search
        for i in range(n - m + 1):
            if w_hash == p_hash:
                if haystack[i:i+m] == needle:
                    return i
            
            if i < n - m:
                w_hash = (w_hash - ord(haystack[i]) * power % MOD + MOD) % MOD
                w_hash = (w_hash * BASE + ord(haystack[i+m])) % MOD
        
        return -1
    
    def rotateString(self, s: str, goal: str) -> bool:
        """
        LeetCode 796: Rotate String
        
        Check if goal is rotation of s
        """
        if len(s) != len(goal):
            return False
        
        # goal is rotation iff goal is substring of s+s
        doubled = s + s
        return self.strStr(doubled, goal) != -1
    
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        LeetCode 686: Repeated String Match
        
        Find min repetitions of a to contain b as substring
        """

        # Minimum needed
        min_reps = (len(b) + len(a) - 1) // len(a)
        
        # Try min and min+1
        for reps in [min_reps, min_reps + 1]:
            repeated = a * reps
            if self.strStr(repeated, b) != -1:
                return reps
        
        return -1
```

---

## 💡 Key Insights

### Hash Verification

**Always verify string match after hash match:**
```python
if window_hash == pattern_hash:
    if text[i:i+m] == pattern:  # Verification
        matches.append(i)
```

**Why?**
- Hash collisions possible (small probability)
- Verification ensures correctness
- O(m) per verification, rare in practice

### Performance Tips

```python

# 1. Precompute power once
power = pow(BASE, m - 1, MOD)  # Do once

# 2. Handle modulo carefully
hash = (hash - old * power % MOD + MOD) % MOD  # +MOD for negative

# 3. Early termination
if found_all_needed:
    break  # Don't search entire text
```

### When Hash-Only Sufficient

```python

# In some problems, can skip verification:
✓ Finding ANY duplicate (first collision is fine)
✓ Approximate matching (small error acceptable)
✓ Statistical analysis

# But for exact matching:
✗ Always verify!
```

---

**Navigation:** [← Basic Rolling Hash](../01_basic_rolling_hash/) | [Rabin-Karp Overview](../README.md) | [Next: Multiple Patterns →](../03_multiple_patterns/)

