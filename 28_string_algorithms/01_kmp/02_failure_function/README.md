---
layout: default
title: "Failure Function"
parent: "KMP Algorithm"
grand_parent: "String Algorithms"
nav_order: 2
---

# 📊 KMP Failure Function (π-array)

## 📊 Visual Overview

![Failure Function](./images/failure-function.svg)

## 📊 Metadata
- **Difficulty:** ![Medium](https://img.shields.io/badge/Medium-orange)
- **Time Complexity:** O(m)
- **Space Complexity:** O(m)
- **Pattern:** Prefix Analysis, Border Properties

---

## 🎯 Overview

The **failure function** (also called **prefix function** or **π-array**) is the heart of KMP. It encodes information about the pattern's structure to enable efficient matching.

---

## 📐 Mathematical Foundation

### Definition

For pattern P of length m:

```
π[i] = max{ k : 0 ≤ k < i and P[0..k-1] = P[i-k+1..i] }
     = length of longest proper prefix of P[0..i]
       that is also a suffix of P[0..i]

```

**Proper prefix:** Prefix that is not the entire substring.

### Border Concept

**Border** of string s: A string that is both a prefix and suffix of s.

```
For "ABCAB":
Borders: "", "AB"
Longest proper border: "AB" (length 2)
π[4] = 2

```

### Key Properties

**Property 1: Border Chain**

```
All borders can be found by following π:
border₀ = P[0..π[m-1]-1]
border₁ = P[0..π[π[m-1]-1]-1]
...
border_k = P[0..π^k[m-1]-1] until π^k = 0

```

**Property 2: Monotonicity**

```
π[i] ≤ π[i-1] + 1 for all i > 0

Proof: If P[0..k-1] = P[i-k+1..i], then
       P[0..k-2] = P[i-k+1..i-1]
       So π[i] ≤ k = π[i-1] + 1

```

**Property 3: Number of Borders**

```
String of length n has at most O(log n) borders on average

Worst case: O(n) borders
Example: "aaa...a" has n borders

```

---

## 💻 Implementations

### 1. Basic Failure Function

```python
def compute_failure_function(pattern):
    """
    Compute KMP failure function (π-array)
    
    Time: O(m) - amortized
    Space: O(m)
    
    Returns: List where pi[i] = length of longest proper border of P[0..i]
    """
    m = len(pattern)
    pi = [0] * m
    
    if m == 0:
        return pi
    
    # pi[0] = 0 by definition
    k = 0  # Length of current border
    
    for i in range(1, m):
        # Fall back through border chain
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k - 1]
        
        # Extend border if characters match
        if pattern[k] == pattern[i]:
            k += 1
        
        pi[i] = k
    
    return pi

# Example with visualization
def compute_failure_function_verbose(pattern):
    """Compute with step-by-step output"""
    m = len(pattern)
    pi = [0] * m
    
    print(f"Pattern: {pattern}")
    print(f"Index:   {''.join(str(i%10) for i in range(m))}")
    print()
    
    k = 0
    
    for i in range(1, m):
        print(f"Step {i}: comparing pattern[{k}]='{pattern[k]}' with pattern[{i}]='{pattern[i]}'", end="")
        
        # Fall back
        original_k = k
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k - 1]
            print(f"\n  Fallback: k={original_k} → k={k}", end="")
        
        # Extend
        if pattern[k] == pattern[i]:
            k += 1
            print(f" → Match! k={k}")
        else:
            print(f" → No match, k=0")
        
        pi[i] = k
        
        # Show current border
        if k > 0:
            prefix = pattern[:k]
            suffix = pattern[i-k+1:i+1]
            print(f"  Border: '{prefix}' = '{suffix}'")
    
    print(f"\nπ array: {pi}")
    return pi

# Example
compute_failure_function_verbose("ABABCABAA")

```

### 2. Failure Function with Border Enumeration

```python
def compute_pi_with_borders(pattern):
    """
    Compute π and enumerate all borders
    
    Time: O(m + total_borders)
    Space: O(m + total_borders)
    
    Returns: (pi_array, list_of_borders_at_each_position)
    """
    m = len(pattern)
    pi = compute_failure_function(pattern)
    
    # Enumerate borders at each position
    all_borders = []
    
    for i in range(m):
        borders = []
        k = pi[i]
        
        while k > 0:
            borders.append(pattern[0:k])
            k = pi[k - 1]
        
        all_borders.append(borders)
    
    return pi, all_borders

# Example
pattern = "ABABCABAA"
pi, borders = compute_pi_with_borders(pattern)

for i in range(len(pattern)):
    print(f"Position {i} ('{pattern[:i+1]}'): π={pi[i]}, borders={borders[i]}")

```

### 3. Optimized Failure Function (with Path Compression)

```python
def compute_failure_function_optimized(pattern):
    """
    Optimized version with explicit path compression tracking
    
    Time: O(m) - still amortized but more explicit
    Space: O(m)
    """
    m = len(pattern)
    pi = [0] * m
    
    k = 0
    comparisons = 0  # Track for complexity analysis
    
    for i in range(1, m):
        # Path compression: jump through border chain
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k - 1]
            comparisons += 1
        
        if pattern[k] == pattern[i]:
            k += 1
            comparisons += 1
        
        pi[i] = k
    
    print(f"Total comparisons: {comparisons} (O(m) where m={m})")
    return pi

# Example showing linear time
pattern = "A" * 100
pi = compute_failure_function_optimized(pattern)

```

### 4. Failure Function for Specific Applications

```python
def compute_pi_with_statistics(pattern):
    """
    Compute π with statistical information
    
    Returns: dict with pi array and statistics
    """
    m = len(pattern)
    pi = compute_failure_function(pattern)
    
    # Compute statistics
    max_border = max(pi) if pi else 0
    avg_border = sum(pi) / m if m > 0 else 0
    
    # Count unique borders
    unique_borders = len(set(pi))
    
    # Find positions with maximum border
    max_positions = [i for i, val in enumerate(pi) if val == max_border]
    
    return {
        'pi': pi,
        'max_border_length': max_border,
        'avg_border_length': avg_border,
        'unique_borders': unique_borders,
        'max_border_positions': max_positions
    }

# Example
pattern = "ABABCABAA"
stats = compute_pi_with_statistics(pattern)
print(f"Pattern: {pattern}")
print(f"Statistics: {stats}")

```

---

## 🎯 Applications of Failure Function

### 1. Check if String Has Period

```python
def has_period(s):
    """
    Check if string can be formed by repeating a substring
    
    Time: O(n)
    Space: O(n)
    
    Uses: If π[n-1] > 0 and n % (n - π[n-1]) == 0,
          then s has period (n - π[n-1])
    """
    n = len(s)
    pi = compute_failure_function(s)
    
    if pi[n-1] == 0:
        return False, None
    
    period_length = n - pi[n-1]
    
    if n % period_length == 0:
        period = s[:period_length]
        return True, period
    
    return False, None

# Examples
print(has_period("abcabcabc"))    # (True, "abc")
print(has_period("abcabcab"))     # (False, None)
print(has_period("aaaa"))         # (True, "a")

```

### 2. Find All Borders

```python
def find_all_borders(s):
    """
    Find all borders of string
    
    Time: O(n + k) where k = number of borders
    Space: O(k)
    
    Returns: List of border lengths (excluding 0)
    """
    n = len(s)
    pi = compute_failure_function(s)
    
    borders = []
    k = pi[n-1]
    
    while k > 0:
        borders.append(k)
        k = pi[k - 1]
    
    return borders

# Example
s = "ABABAB"
borders = find_all_borders(s)
print(f"String: {s}")
print(f"Border lengths: {borders}")
print(f"Borders: {[s[:b] for b in borders]}")

```

### 3. Minimum Characters to Add for Palindrome

```python
def min_chars_for_palindrome(s):
    """
    Find minimum characters to add to end to make palindrome
    
    Time: O(n)
    Space: O(n)
    
    Approach: Find longest prefix that matches suffix of reverse
    """
    n = len(s)
    # Create: s + '#' + reverse(s)
    rev = s[::-1]
    combined = s + '#' + rev
    
    pi = compute_failure_function(combined)
    
    # π[end] tells longest prefix of s that matches suffix of reverse
    longest_prefix_palindrome = pi[-1]
    
    # Need to add (n - longest_prefix_palindrome) characters
    chars_to_add = n - longest_prefix_palindrome
    
    return chars_to_add, rev[:chars_to_add]

# Example
s = "aacecaa"
count, chars = min_chars_for_palindrome(s)
print(f"String: {s}")
print(f"Add {count} chars: {chars}")
print(f"Result: {s + chars}")  # "aacecaaa" → palindrome "aacecaaa"

```

### 4. Longest Happy Prefix (LeetCode 1392)

```python
def longest_happy_prefix(s):
    """
    Find longest prefix that is also suffix (but not entire string)
    
    Time: O(n)
    Space: O(n)
    
    LeetCode 1392: Longest Happy Prefix
    """
    pi = compute_failure_function(s)
    length = pi[-1]  # Longest proper border
    return s[:length]

# Examples
print(longest_happy_prefix("level"))       # "l"
print(longest_happy_prefix("ababab"))      # "abab"
print(longest_happy_prefix("leetcodeleet"))# "leet"
print(longest_happy_prefix("a"))           # ""

```

### 5. String Compression Analysis

```python
def analyze_repetition_structure(s):
    """
    Analyze repetition structure using failure function
    
    Time: O(n)
    Space: O(n)
    
    Returns: Information about repetitive structure
    """
    n = len(s)
    pi = compute_failure_function(s)
    
    # Check if entirely repeating
    has_period, period = has_period(s)
    
    # Find all repeating prefixes
    repeating_prefixes = []
    for i in range(n):
        prefix_len = i + 1
        if pi[i] > 0:
            border_len = pi[i]
            period_len = prefix_len - border_len
            
            if prefix_len % period_len == 0:
                repeating_prefixes.append({
                    'end': i,
                    'length': prefix_len,
                    'period': s[:period_len],
                    'repetitions': prefix_len // period_len
                })
    
    return {
        'has_overall_period': has_period,
        'overall_period': period,
        'repeating_prefixes': repeating_prefixes,
        'longest_border': pi[n-1]
    }

# Example
s = "abcabcabcab"
analysis = analyze_repetition_structure(s)
print(f"String: {s}")
print(f"Analysis: {analysis}")

```

### 6. Pattern Preprocessing for Multiple Texts

```python
class KMPMatcher:
    """
    Preprocess pattern once, use for multiple texts
    
    Amortizes preprocessing cost over multiple matches
    """
    
    def __init__(self, pattern):
        self.pattern = pattern
        self.m = len(pattern)
        self.pi = compute_failure_function(pattern)
    
    def search(self, text):
        """Search in new text using preprocessed pattern"""
        n = len(text)
        matches = []
        
        i = j = 0
        while i < n:
            if text[i] == self.pattern[j]:
                i += 1
                j += 1
            
            if j == self.m:
                matches.append(i - j)
                j = self.pi[j - 1]
            elif i < n and text[i] != self.pattern[j]:
                if j != 0:
                    j = self.pi[j - 1]
                else:
                    i += 1
        
        return matches
    
    def get_border_info(self):
        """Get border information"""
        borders = []
        k = self.pi[self.m - 1]
        
        while k > 0:
            borders.append(self.pattern[:k])
            k = self.pi[k - 1]
        
        return borders

# Example: Search same pattern in multiple texts
matcher = KMPMatcher("ABABCABAB")

texts = [
    "ABABDABACDABABCABAB",
    "XYZABABCABABABC",
    "ABABCABAB"
]

for idx, text in enumerate(texts):
    matches = matcher.search(text)
    print(f"Text {idx}: {len(matches)} matches at {matches}")

```

---

## 🧩 LeetCode Problems

### Medium

| # | Problem | Difficulty | Approach |
|---|---------|------------|----------|
| 1392 | [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) | 🟡 Medium | Direct π[n-1] |
| 459 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | 🟡 Medium | Check periodicity |
| 214 | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | 🟡 Medium | π on s+'#'+reverse(s) |

### Solutions

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        LeetCode 1392: Longest Happy Prefix
        
        Return longest proper prefix that is also suffix
        """
        def compute_pi(pattern):
            m = len(pattern)
            pi = [0] * m
            k = 0
            
            for i in range(1, m):
                while k > 0 and pattern[k] != pattern[i]:
                    k = pi[k - 1]
                
                if pattern[k] == pattern[i]:
                    k += 1
                
                pi[i] = k
            
            return pi
        
        pi = compute_pi(s)
        return s[:pi[-1]]
    
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        LeetCode 459: Repeated Substring Pattern
        
        Check if string can be constructed by repeating substring
        """
        def compute_pi(pattern):
            m = len(pattern)
            pi = [0] * m
            k = 0
            
            for i in range(1, m):
                while k > 0 and pattern[k] != pattern[i]:
                    k = pi[k - 1]
                
                if pattern[k] == pattern[i]:
                    k += 1
                
                pi[i] = k
            
            return pi
        
        n = len(s)
        pi = compute_pi(s)
        
        # Check if has period
        if pi[n-1] == 0:
            return False
        
        period_len = n - pi[n-1]
        
        return n % period_len == 0
    
    def shortestPalindrome(self, s: str) -> str:
        """
        LeetCode 214: Shortest Palindrome
        
        Add minimum chars to front to make palindrome
        """
        def compute_pi(pattern):
            m = len(pattern)
            pi = [0] * m
            k = 0
            
            for i in range(1, m):
                while k > 0 and pattern[k] != pattern[i]:
                    k = pi[k - 1]
                
                if pattern[k] == pattern[i]:
                    k += 1
                
                pi[i] = k
            
            return pi
        
        # Find longest palindrome prefix
        rev = s[::-1]
        combined = s + '#' + rev
        
        pi = compute_pi(combined)
        
        # π[-1] = longest prefix of s that matches suffix of reverse
        palindrome_prefix_len = pi[-1]
        
        # Add reverse of remaining suffix to front
        to_add = s[palindrome_prefix_len:]
        
        return to_add[::-1] + s

```

---

## 💡 Key Insights

### Why π Computation is O(m)

**Potential Function Analysis:**

```
Define Φ = k (current border length)

For each iteration i:
- k increases by at most 1: ΔΦ ≤ 1
- While loop decreases k: ΔΦ < 0
- Initial Φ = 0, Final Φ ≤ m

Total increase in Φ = O(m)
Total decrease in Φ = O(m)
Therefore total operations = O(m)

```

### Border Properties

1. **Transitive closure:** 
   If b is border of s and b' is border of b, then b' is border of s

2. **Nested structure:**
   All borders form a chain: π[n-1] → π[π[n-1]-1] → ...

3. **Logarithmic average:**
   Average number of borders per position: O(log n)

---

**Navigation:** [← Basic Matching](../01_basic_pattern_matching/) | [KMP Overview](../README.md) | [Next: String Period →](../03_string_period/)

