---
layout: default
title: "Basic Pattern Matching"
parent: "KMP Algorithm"
grand_parent: "String Algorithms"
nav_order: 1
---

# 🎯 Basic Pattern Matching with KMP

## 📊 Visual Overview

![Basic Pattern Matching](./images/basic-pattern-matching.svg)

## 📊 Metadata

- **Difficulty:** ![Easy-Medium](https://img.shields.io/badge/Easy--Medium-yellow)

- **Time Complexity:** O(n + m)

- **Space Complexity:** O(m)

- **Pattern:** String Matching, Linear Scanning

---

## 🎯 Overview

Basic pattern matching problems using KMP algorithm - finding occurrences, counting matches, and handling edge cases.

---

## 📐 Core Concepts

### Problem Statement

Given:

- Text T of length n

- Pattern P of length m

Find: All positions where P occurs in T

**Naive Approach:** O(nm)
**KMP Approach:** O(n + m)

### KMP Key Idea

```
When mismatch occurs:

- Don't restart from next position in text

- Use failure function to skip ahead

- Each text character examined at most once

```

---

## 💻 Implementations

### 1. Find All Occurrences

```python
def find_all_occurrences(text, pattern):
    """
    Find all positions where pattern occurs in text
    
    Time: O(n + m)
    Space: O(m)
    
    Args:
        text: String to search in
        pattern: Pattern to find
    
    Returns:
        List of starting indices (0-indexed)
    """
    def compute_lps(pattern):
        """Compute longest proper prefix which is suffix"""
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    n, m = len(text), len(pattern)
    
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []
    
    lps = compute_lps(pattern)
    matches = []
    
    i = 0  # Index for text
    j = 0  # Index for pattern
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches

# Example
text = "ABABDABACDABABCABAB"
pattern = "AB"
print(find_all_occurrences(text, pattern))
# Output: [0, 2, 5, 10, 12, 17]

```

### 2. Find First Occurrence

```python
def find_first_occurrence(text, pattern):
    """
    Find first occurrence of pattern (like strStr())
    
    LeetCode 28: Implement strStr()
    
    Time: O(n + m)
    Space: O(m)
    
    Returns: Index of first occurrence, or -1 if not found
    """
    def compute_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        
        for i in range(1, m):
            while length > 0 and pattern[i] != pattern[length]:
                length = lps[length - 1]
            
            if pattern[i] == pattern[length]:
                length += 1
            
            lps[i] = length
        
        return lps
    
    n, m = len(text), len(pattern)
    
    if m == 0:
        return 0
    if m > n:
        return -1
    
    lps = compute_lps(pattern)
    
    i = j = 0
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            return i - j  # Found! Return immediately
        
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1

# Example
print(find_first_occurrence("hello", "ll"))      # 2
print(find_first_occurrence("aaaaa", "bba"))     # -1
print(find_first_occurrence("", ""))             # 0

```

### 3. Count Occurrences

```python
def count_pattern_occurrences(text, pattern, overlapping=True):
    """
    Count number of times pattern appears
    
    Time: O(n + m)
    Space: O(m)
    
    Args:
        text: Text to search in
        pattern: Pattern to count
        overlapping: If True, count overlapping occurrences
    
    Returns: Number of occurrences
    """
    if overlapping:
        return len(find_all_occurrences(text, pattern))
    
    # Non-overlapping: greedy approach
    def compute_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        
        for i in range(1, m):
            while length > 0 and pattern[i] != pattern[length]:
                length = lps[length - 1]
            
            if pattern[i] == pattern[length]:
                length += 1
            
            lps[i] = length
        
        return lps
    
    n, m = len(text), len(pattern)
    
    if m == 0 or m > n:
        return 0
    
    lps = compute_lps(pattern)
    count = 0
    i = j = 0
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            count += 1
            j = 0  # Reset for non-overlapping
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return count

# Examples
text = "AABAACAADAABAABA"
pattern = "AABA"

print(count_pattern_occurrences(text, pattern, overlapping=True))   # 3
print(count_pattern_occurrences(text, pattern, overlapping=False))  # 2

```

### 4. Check if Pattern Exists

```python
def contains_pattern(text, pattern):
    """
    Check if pattern exists in text
    
    Time: O(n + m)
    Space: O(m)
    
    Returns: Boolean
    """
    return find_first_occurrence(text, pattern) != -1

# Example
print(contains_pattern("hello world", "world"))  # True
print(contains_pattern("hello world", "abc"))    # False

```

### 5. Find Last Occurrence

```python
def find_last_occurrence(text, pattern):
    """
    Find last occurrence of pattern
    
    Time: O(n + m)
    Space: O(m)
    
    Returns: Index of last occurrence, or -1
    """
    matches = find_all_occurrences(text, pattern)
    return matches[-1] if matches else -1

# Example
text = "ABABDABACDABABCABAB"
pattern = "AB"
print(find_last_occurrence(text, pattern))  # 17

```

### 6. Find All with Context

```python
def find_with_context(text, pattern, context_size=5):
    """
    Find all occurrences and return with surrounding context
    
    Time: O(n + m)
    Space: O(m + k·context) where k = matches
    
    Returns: List of (index, context_string) tuples
    """
    matches = find_all_occurrences(text, pattern)
    results = []
    
    for idx in matches:
        start = max(0, idx - context_size)
        end = min(len(text), idx + len(pattern) + context_size)
        context = text[start:end]
        
        results.append((idx, context))
    
    return results

# Example
text = "The quick brown fox jumps over the lazy dog"
pattern = "the"

matches = find_with_context(text.lower(), pattern, context_size=3)
for idx, context in matches:
    print(f"Match at {idx}: '...{context}...'")

```

### 7. Multiple Text Search

```python
def search_in_multiple_texts(texts, pattern):
    """
    Search pattern in multiple texts
    
    Time: O((n₁ + n₂ + ... + nₖ) + m)
    Space: O(m)
    
    Returns: Dict mapping text_index -> list of positions
    """
    results = {}
    
    for text_idx, text in enumerate(texts):
        matches = find_all_occurrences(text, pattern)
        if matches:
            results[text_idx] = matches
    
    return results

# Example
texts = [
    "ABABDABACDABABCABAB",
    "ABCDEFGHI",
    "ABABABABAB"
]

pattern = "AB"
results = search_in_multiple_texts(texts, pattern)
print(results)
# {0: [0, 2, 5, 10, 12, 17], 1: [0], 2: [0, 2, 4, 6, 8]}

```

---

## 🧩 LeetCode Problems

### Easy

| # | Problem | Difficulty | Solution |
|---|---------|------------|----------|
| 28 | [Find Index of First Occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 🟢 Easy | `find_first_occurrence` |
| 796 | [Rotate String](https://leetcode.com/problems/rotate-string/) | 🟢 Easy | Pattern in doubled string |
| 459 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | 🟢 Easy | Uses LPS properties |

### Medium

| # | Problem | Difficulty | Solution |
|---|---------|------------|----------|
| 686 | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) | 🟡 Medium | KMP with repetition |
| 1668 | [Maximum Repeating Substring](https://leetcode.com/problems/maximum-repeating-substring/) | 🟡 Medium | Count occurrences |

---

## 💡 Solutions to LeetCode Problems

### Problem 28: Implement strStr()

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Implement strStr() using KMP
        
        Returns index of first occurrence or -1
        """
        if not needle:
            return 0
        
        def build_lps(pattern):
            m = len(pattern)
            lps = [0] * m
            length = 0
            
            for i in range(1, m):
                while length > 0 and pattern[i] != pattern[length]:
                    length = lps[length - 1]
                
                if pattern[i] == pattern[length]:
                    length += 1
                
                lps[i] = length
            
            return lps
        
        n, m = len(haystack), len(needle)
        
        if m > n:
            return -1
        
        lps = build_lps(needle)
        
        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == m:
                return i - j
            
            elif i < n and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1

```

### Problem 796: Rotate String

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Check if goal is rotation of s
        
        Key insight: If goal is rotation of s,
        then goal is substring of s + s
        
        Time: O(n)
        """
        if len(s) != len(goal):
            return False
        
        doubled = s + s
        return self.strStr(doubled, goal) != -1
    
    def strStr(self, text, pattern):
        """KMP implementation"""
        if not pattern:
            return 0
        
        def build_lps(p):
            m = len(p)
            lps = [0] * m
            length = 0
            
            for i in range(1, m):
                while length > 0 and p[i] != p[length]:
                    length = lps[length - 1]
                
                if p[i] == p[length]:
                    length += 1
                
                lps[i] = length
            
            return lps
        
        n, m = len(text), len(pattern)
        if m > n:
            return -1
        
        lps = build_lps(pattern)
        i = j = 0
        
        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
            
            if j == m:
                return i - j
            
            elif i < n and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1

```

### Problem 686: Repeated String Match

```python
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        Find minimum repetitions of 'a' needed so that 'b' is substring
        
        Time: O(n + m)
        Space: O(n)
        """
        # Minimum repetitions needed
        min_reps = (len(b) + len(a) - 1) // len(a)
        
        # Try min_reps and min_reps + 1
        for reps in [min_reps, min_reps + 1]:
            repeated = a * reps
            if self.kmp_search(repeated, b):
                return reps
        
        return -1
    
    def kmp_search(self, text, pattern):
        """Check if pattern exists in text using KMP"""
        def build_lps(p):
            m = len(p)
            lps = [0] * m
            length = 0
            
            for i in range(1, m):
                while length > 0 and p[i] != p[length]:
                    length = lps[length - 1]
                
                if p[i] == p[length]:
                    length += 1
                
                lps[i] = length
            
            return lps
        
        if not pattern:
            return True
        
        n, m = len(text), len(pattern)
        if m > n:
            return False
        
        lps = build_lps(pattern)
        i = j = 0
        
        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
            
            if j == m:
                return True
            
            elif i < n and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return False

```

---

## 🎓 Advanced Patterns

### Pattern Matching with Wildcards

```python
def kmp_with_wildcard(text, pattern, wildcard='?'):
    """
    KMP where '?' matches any single character
    
    Time: O(n + m)
    Space: O(m)
    """
    def build_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        
        for i in range(1, m):
            while length > 0 and pattern[i] != pattern[length] and \
                  pattern[i] != wildcard and pattern[length] != wildcard:
                length = lps[length - 1]
            
            if pattern[i] == pattern[length] or \
               pattern[i] == wildcard or pattern[length] == wildcard:
                length += 1
            
            lps[i] = length
        
        return lps
    
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []
    
    lps = build_lps(pattern)
    matches = []
    i = j = 0
    
    while i < n:
        if text[i] == pattern[j] or pattern[j] == wildcard:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j] and pattern[j] != wildcard:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches

# Example
text = "ABABDABACDABABCABAB"
pattern = "AB??CA"
print(kmp_with_wildcard(text, pattern))

```

### Case-Insensitive Matching

```python
def kmp_case_insensitive(text, pattern):
    """
    Case-insensitive pattern matching
    
    Time: O(n + m)
    Space: O(n + m)
    """
    text_lower = text.lower()
    pattern_lower = pattern.lower()
    return find_all_occurrences(text_lower, pattern_lower)

# Example
text = "Hello World, hello world"
pattern = "HELLO"
print(kmp_case_insensitive(text, pattern))  # [0, 13]

```

---

## 💡 Key Insights

1. **Always handle edge cases:**
   - Empty pattern
   - Empty text
   - Pattern longer than text

2. **LPS array is key:**
   - Encodes pattern structure
   - Enables O(n) matching
   - Computed in O(m) time

3. **Text examined once:**
   - Index i never decreases
   - Guarantees linear time

4. **Overlapping vs Non-overlapping:**
   - Overlapping: use LPS after match
   - Non-overlapping: reset to 0 after match

---

**Navigation:** [← KMP Overview](../README.md) | [Next: Failure Function →](../02_failure_function/)

