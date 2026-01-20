---
layout: default
title: "Parentheses"
parent: "Stacks"
nav_order: 2
permalink: /04_stacks/02_parentheses/
---

<div align="center">

# 🔗 Parentheses Problems

<p>
  <img src="https://img.shields.io/badge/Difficulty-Easy_to_Hard-orange?style=for-the-badge" alt="Difficulty">
  <img src="https://img.shields.io/badge/Problems-15+-blue?style=for-the-badge" alt="Problems">
</p>

</div>

---

## 🎨 Visual Diagrams

<div align="center">

### ✅ Valid Parentheses

<img src="./images/valid_parentheses.svg" alt="Valid Parentheses" width="850"/>

*Stack-based matching for (), [], {} - LeetCode #20*

---

### 🌳 Generate Parentheses

<img src="./images/generate_parentheses.svg" alt="Generate Parentheses" width="900"/>

*Backtracking with Catalan numbers: C₃ = 5 valid combinations - LeetCode #22*

---

### 📏 Longest Valid Parentheses

<img src="./images/longest_valid_parentheses.svg" alt="Longest Valid Parentheses" width="850"/>

*Stack stores indices of unmatched positions - LeetCode #32*

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. Basic Stack](../01_basic_stack/README.md) | **02. Parentheses** | [03. Monotonic Stack →](../03_monotonic_stack/README.md) |

---

## 📐 Mathematical Foundations

### 1️⃣ Valid Parentheses Conditions

For string $S$ with brackets:

**Condition 1 (Balance):**

```math
\boxed{\sum_{i=0}^{n-1} \text{score}(S[i]) = 0}

```

Where:

- $\text{score}('(') = +1, \; \text{score}(')') = -1$

- $\text{score}('[') = +1, \; \text{score}(']') = -1$

- $\text{score}('\{') = +1, \; \text{score}('\}') = -1$

**Condition 2 (Prefix Non-negative):**

```math
\boxed{\forall k \in [0, n-1]: \sum_{i=0}^{k} \text{score}(S[i]) \geq 0}

```

**Proof:** If prefix sum becomes negative, we have more closing than opening brackets up to that point → invalid.

---

### 2️⃣ Stack Matching Correctness Proof

**Invariant:** Stack contains only unmatched opening brackets.

**Theorem:** String $S$ is valid iff stack is empty after processing.

**Proof by Induction:**

**Base:** Empty string → empty stack → valid ✓

**Inductive Step:**

- If $S[i]$ is opening bracket:
  - Push to stack → invariant maintained

- If $S[i]$ is closing bracket:
  - If stack empty → invalid (prefix sum would be negative)
  - If stack top matches → pop → invariant maintained
  - If stack top doesn't match → invalid (wrong type)

**Termination:**

- Valid string: all opens matched → empty stack

- Invalid string: unmatched opens remain → non-empty stack ∎

---

### 3️⃣ Minimum Additions Formula

**Problem:** Minimum insertions to make string valid.

```math
\boxed{\text{additions} = \text{unmatched_open} + \text{unmatched_close}}

```

**Proof:**

- Each unmatched `(` needs a matching `)`
- Each unmatched `)` needs a matching `(`
- These are independent → sum them ∎

**Example:**

```
Input: "(()"
Scan: ( → open=1, ( → open=2, ) → open=1
Result: open=1, close=0
Answer: 1 (need one more ')')

```

---

### 4️⃣ Longest Valid Parentheses - DP Formula

**Recurrence Relation:**

```math
\boxed{dp[i] = \begin{cases}
0 & \text{if } S[i] = '(' \\
dp[i-2] + 2 & \text{if } S[i-1] = '(' \text{ and } i \geq 1 \\
dp[i-1] + 2 + dp[j] & \text{if } j = i - dp[i-1] - 2 \geq 0 \text{ and } S[j+1] = '('
\end{cases}}

```

Where:

- $dp[i]$ = length of longest valid substring ending at index $i$

- Case 1: Opening bracket can't end a valid substring

- Case 2: Immediate pair `()`
- Case 3: Nested case `(...)`

---

### 5️⃣ Catalan Number Connection

**Number of valid strings with $n$ pairs:**

```math
\boxed{C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)! \cdot n!}}

```

**Recurrence Relation:**

```math
C_n = \sum_{i=0}^{n-1} C_i \cdot C_{n-1-i}

```

**First few Catalan numbers:**

| n | 0 | 1 | 2 | 3 | 4 | 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $C_n$ | 1 | 1 | 2 | 5 | 14 | 42 |

**Examples for $n=3$ ($C_3 = 5$):**

1. `((()))`
2. `(()())`
3. `(())()`
4. `()(())`
5. `()()()`

---

### 6️⃣ Asymptotic Growth

**Catalan Number Growth:**

```math
C_n \sim \frac{4^n}{n^{3/2}\sqrt{\pi}}

```

This means generating all valid parentheses has exponential time complexity!

---

## 🎨 Visual Algorithm Walkthroughs

### Valid Parentheses - Detailed Trace

```
Input: "({[]})"

+--------------------------------------------------------------------+

|  Algorithm: Push opens, pop and match closes                       |
+--------------------------------------------------------------------+
|  Index 0: char = '('                                               |
|  Action: Opening bracket → Push                                    |
|  Stack: ['(']                                                      |
|  Valid so far: ✓                                                   |
+--------------------------------------------------------------------+

|  Index 1: char = '{'                                               |
|  Action: Opening bracket → Push                                    |
|  Stack: ['(', '{']                                                 |
|  Valid so far: ✓                                                   |
+--------------------------------------------------------------------+

|  Index 2: char = '['                                               |
|  Action: Opening bracket → Push                                    |
|  Stack: ['(', '{', '[']                                            |
|  Valid so far: ✓                                                   |
+--------------------------------------------------------------------+

|  Index 3: char = ']'                                               |
|  Action: Closing bracket → Check top                               |
|  Top: '[', Matches? YES ✓                                          |
|  Pop and continue                                                  |
|  Stack: ['(', '{']                                                 |
|  Valid so far: ✓                                                   |
+--------------------------------------------------------------------+

|  Index 4: char = '}'                                               |
|  Action: Closing bracket → Check top                               |
|  Top: '{', Matches? YES ✓                                          |
|  Pop and continue                                                  |
|  Stack: ['(']                                                      |
|  Valid so far: ✓                                                   |
+--------------------------------------------------------------------+

|  Index 5: char = ')'                                               |
|  Action: Closing bracket → Check top                               |
|  Top: '(', Matches? YES ✓                                          |
|  Pop and continue                                                  |
|  Stack: []                                                         |
|  Valid so far: ✓                                                   |
+--------------------------------------------------------------------+

|  End of string                                                      |
|  Stack empty? YES ✓                                                |
|  Result: VALID ✓                                                   |
+--------------------------------------------------------------------+

Counterexample - Invalid: "([)]"

+--------------------------------------------------------------------+

|  Index 0: '(' → Stack: ['(']                                       |
|  Index 1: '[' → Stack: ['(', '[']                                  |
|  Index 2: ')' → Top is '[', doesn't match! ✗                       |
|  Result: INVALID ✗                                                 |
+--------------------------------------------------------------------+

```

---

### Minimum Add to Make Valid - Visual Trace

```
Input: "())"

+--------------------------------------------------------------------+

|  Algorithm: Track unmatched opens and closes                       |
+--------------------------------------------------------------------+
|  Variables: unmatched_open = 0, unmatched_close = 0                |
+--------------------------------------------------------------------+

|  Index 0: char = '('                                               |
|  Action: Opening bracket                                           |
|  unmatched_open = 1                                                |
+--------------------------------------------------------------------+

|  Index 1: char = ')'                                               |
|  Action: Closing bracket, have opens?                              |
|  unmatched_open > 0? YES                                           |
|  Match it: unmatched_open = 0                                      |
+--------------------------------------------------------------------+

|  Index 2: char = ')'                                               |
|  Action: Closing bracket, have opens?                              |
|  unmatched_open > 0? NO                                            |
|  This close has no match!                                          |
|  unmatched_close = 1                                               |
+--------------------------------------------------------------------+

|  End of string                                                      |
|  unmatched_open = 0 (need 0 more ')')                              |
|  unmatched_close = 1 (need 1 more '(')                             |
|  Total additions = 0 + 1 = 1                                       |
|                                                                    |
|  Answer: 1 (add one '(' at the beginning)                         |
|  Result: "(())" ✓                                                  |
+--------------------------------------------------------------------+

Another Example: "((("

+--------------------------------------------------------------------+

|  Process: ( → open=1, ( → open=2, ( → open=3                      |
|  End: unmatched_open = 3, unmatched_close = 0                      |
|  Total additions = 3                                               |
|  Answer: 3 (add three ')' at the end)                             |
|  Result: "((()))" ✓                                                |
+--------------------------------------------------------------------+

```

---

### Longest Valid Parentheses - Stack Method

```
Input: ")()())"

+--------------------------------------------------------------------+

|  Algorithm: Stack stores indices of unmatched positions            |
|  Key Insight: Valid substring = gap between unmatched positions    |
+--------------------------------------------------------------------+

|  Initialize: stack = [-1]  (base for length calculation)           |
|              max_length = 0                                        |
+--------------------------------------------------------------------+

|  Index 0: char = ')'                                               |
|  Stack: [-1]                                                       |
|  Pop → stack empty!                                                |
|  This ')' is unmatched, becomes new base                           |
|  Push 0                                                            |
|  Stack: [0]                                                        |
|  max_length = 0                                                    |
+--------------------------------------------------------------------+

|  Index 1: char = '('                                               |
|  Push index                                                        |
|  Stack: [0, 1]                                                     |
|  max_length = 0                                                    |
+--------------------------------------------------------------------+

|  Index 2: char = ')'                                               |
|  Pop (matched with '(' at index 1)                                 |
|  Stack: [0]                                                        |
|  Length = 2 - 0 = 2                                                |
|  max_length = 2                                                    |
+--------------------------------------------------------------------+

|  Index 3: char = '('                                               |
|  Push index                                                        |
|  Stack: [0, 3]                                                     |
|  max_length = 2                                                    |
+--------------------------------------------------------------------+

|  Index 4: char = ')'                                               |
|  Pop (matched with '(' at index 3)                                 |
|  Stack: [0]                                                        |
|  Length = 4 - 0 = 4                                                |
|  max_length = 4  ← Updated!                                        |
+--------------------------------------------------------------------+

|  Index 5: char = ')'                                               |
|  Pop → stack becomes empty                                         |
|  This ')' is unmatched, becomes new base                           |
|  Push 5                                                            |
|  Stack: [5]                                                        |
|  max_length = 4                                                    |
+--------------------------------------------------------------------+

|  End of string                                                      |
|  Answer: 4 (substring "()()" from index 1 to 4)                   |
|                                                                    |
|  Visual:                                                           |
|  ) ( ) ( ) )                                                       |
|  0 1 2 3 4 5                                                       |
|  x [-----] x                                                       |
|    valid!                                                          |
+--------------------------------------------------------------------+

```

---

### Generate Parentheses - Backtracking Tree

```
n = 3 (generate all valid combinations with 3 pairs)

+--------------------------------------------------------------------+

|  Decision Tree: At each node, decide to add '(' or ')'             |
|  Constraints: open < n, close < open                               |
+--------------------------------------------------------------------+

|                                                                    |
|                          ""                                        |
|                        (0, 0)                                      |
|                          |                                         |
|                    "(" (1, 0)                                      |
|                     /       \                                      |
|                    /         \                                     |
|            "((" (2, 0)    "()" (1, 1)                             |
|             /      \        /      \                               |
|            /        \      /        \                              |
|      "(((" (3,0) "(()" (2,1) "()(" (2,1) "(())" (1,2)            |
|         |          |        |           ✓                         |
|         |          |        |         DONE!                       |
|         |          |        |                                     |
|    "((())" "(()()" "()(()"                                         |
|      (3,1)    (2,2)   (3,1)                                        |
|        |       ✓       |                                          |
|        |     DONE!     |                                          |
|        |               |                                          |
|   "((()))" "()(()"                                                 |
|     (3,2)    (3,1)                                                 |
|      |        |                                                   |
|      |   "()(())"                                                 |
|      |     (3,2)                                                  |
|      |      |                                                     |
|   "((()))" "()(())"                                                |
|     (3,3)   (3,3)                                                  |
|      ✓       ✓                                                    |
|    DONE!   DONE!                                                  |
|                                                                    |
|  Continue right branch...                                         |
|                                                                    |
|  "()()(" (2,2)                                                     |
|      |                                                             |
|  "()()()" (3,3) ✓ DONE!                                           |
+--------------------------------------------------------------------+

|  All 5 valid combinations (C₃ = 5):                               |
|  1. ((()))                                                        |
|  2. (()())                                                        |
|  3. (())()                                                        |
|  4. ()(())                                                        |
|  5. ()()()                                                        |
+--------------------------------------------------------------------+

Algorithm Logic:

- Start with empty string, open=0, close=0
- At each step:
  * If open < n: can add '('
  * If close < open: can add ')'

- Base case: length == 2n → add to result

```

---

### Minimum Remove to Make Valid - Two Pass

```
Input: "lee(t(c)o)de)"

+--------------------------------------------------------------------+

|  Strategy: Mark invalid brackets, then build result                |
+--------------------------------------------------------------------+
|  Pass 1: Mark unmatched closing brackets                          |
|  --------------------------------------------------------------    |
|  l  e  e  (  t  (  c  )  o  )  d  e  )                            |
|  0  1  2  3  4  5  6  7  8  9 10 11 12                            |
|                                       ↑                            |
|                              unmatched! mark for removal           |
|                                                                    |
|  Stack trace for Pass 1:                                          |
|  Index 3: '(' → stack = [3]                                        |
|  Index 5: '(' → stack = [3, 5]                                     |
|  Index 7: ')' → pop 5, stack = [3]                                 |
|  Index 9: ')' → pop 3, stack = []                                  |
|  Index 12: ')' → stack empty! Mark 12 for removal                  |
|                                                                    |
|  to_remove = {12}                                                 |
+--------------------------------------------------------------------+

|  Pass 2: Mark unmatched opening brackets                          |
|  --------------------------------------------------------------    |
|  Process right to left:                                           |
|  Index 9: ')' → close = 1                                          |
|  Index 7: ')' → close = 2                                          |
|  Index 5: '(' → close > 0, close = 1                               |
|  Index 3: '(' → close > 0, close = 0                               |
|                                                                    |
|  All opening brackets matched! No more to remove.                 |
|  to_remove = {12}                                                 |
+--------------------------------------------------------------------+

|  Pass 3: Build result, skipping marked indices                    |
|  --------------------------------------------------------------    |
|  l  e  e  (  t  (  c  )  o  )  d  e  [)]  ← Skip                  |
|  0  1  2  3  4  5  6  7  8  9 10 11  12                            |
|  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓   ✗                          |
|                                                                    |
|  Result: "lee(t(c)o)de" ✓                                          |
+--------------------------------------------------------------------+

```

---

## 💻 Code Implementations

```python
def isValid(s: str) -> bool:
    """
    Check if parentheses/brackets are valid.
    
    Algorithm:
    - Opening bracket → push to stack
    - Closing bracket → check if matches top, pop if yes
    - End: stack must be empty
    
    Time: O(n), Space: O(n)
    """
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            # Opening bracket
            stack.append(char)
        else:
            # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

def isValidOptimized(s: str) -> bool:
    """
    Optimized: Return early on obvious failures.
    
    Optimizations:
    - Odd length → impossible to balance
    - Closing bracket when stack empty → immediate false
    """
    # Optimization 1: Odd length impossible
    if len(s) % 2 != 0:
        return False
    
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            # Optimization 2: Early return
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

def minAddToMakeValid(s: str) -> int:
    """
    Minimum insertions to make parentheses valid.
    
    Algorithm:
    - Track unmatched opens and closes
    - Each '(' increments open count
    - Each ')' decrements open if available, else increments close count
    
    Time: O(n), Space: O(1)
    """
    unmatched_open = 0  # Need ')' for these
    unmatched_close = 0  # Need '(' for these
    
    for char in s:
        if char == '(':
            unmatched_open += 1
        elif unmatched_open > 0:
            # Match with previous '('
            unmatched_open -= 1
        else:
            # No '(' to match, this ')' is orphaned
            unmatched_close += 1
    
    return unmatched_open + unmatched_close

def minRemoveToMakeValid(s: str) -> str:
    """
    Remove minimum brackets to make valid.
    
    Two-pass algorithm:
    1. Mark unmatched brackets
    2. Build result without marked indices
    
    Time: O(n), Space: O(n)
    """
    # Pass 1: Identify brackets to remove
    to_remove = set()
    stack = []
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()  # Matched
            else:
                to_remove.add(i)  # Unmatched ')'
    
    # Unmatched '(' remaining in stack
    to_remove.update(stack)
    
    # Pass 2: Build result
    return ''.join(char for i, char in enumerate(s) if i not in to_remove)

def longestValidParentheses(s: str) -> int:
    """
    Find length of longest valid parentheses substring.
    
    Stack approach:
    - Stack stores indices of unmatched brackets
    - Initialize with -1 (base for length calculation)
    - Valid length = current_index - stack_top
    
    Time: O(n), Space: O(n)
    """
    stack = [-1]  # Base index
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                # Calculate length using base
                max_length = max(max_length, i - stack[-1])
            else:
                # Stack empty, this ')' is unmatched
                stack.append(i)  # New base
    
    return max_length

def longestValidParenthesesDP(s: str) -> int:
    """
    DP approach for longest valid parentheses.
    
    dp[i] = length of longest valid ending at i
    
    Time: O(n), Space: O(n)
    """
    n = len(s)
    if n < 2:
        return 0
    
    dp = [0] * n
    max_length = 0
    
    for i in range(1, n):
        if s[i] == ')':
            if s[i-1] == '(':
                # Case: ...()
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                # Case: ...))
                dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] - 2] if i - dp[i-1] - 2 >= 0 else 0)
            
            max_length = max(max_length, dp[i])
    
    return max_length

def generateParenthesis(n: int) -> list[str]:
    """
    Generate all valid combinations of n pairs.
    
    Backtracking with constraints:
    - Can add '(' if open_count < n
    - Can add ')' if close_count < open_count
    
    Time: O(4ⁿ/√n) - nth Catalan number
    Space: O(n) - recursion depth
    """
    result = []
    
    def backtrack(current: str, open_count: int, close_count: int):
        # Base case: complete string
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Add '(' if we haven't used all n opening brackets
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        # Add ')' if it won't make string invalid
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result

def maxDepth(s: str) -> int:
    """
    Find maximum nesting depth of parentheses.
    
    Algorithm: Track current depth, update maximum
    
    Time: O(n), Space: O(1)
    """
    max_depth = 0
    current_depth = 0
    
    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1
    
    return max_depth

def checkValidString(s: str) -> bool:
    """
    Valid parentheses with wildcard '*' (can be '(', ')', or empty).
    
    Strategy: Track range of possible open brackets
    - low: minimum possible open brackets
    - high: maximum possible open brackets
    
    Valid if range [low, high] contains 0 and stays non-negative
    
    Time: O(n), Space: O(1)
    """
    low = high = 0
    
    for char in s:
        if char == '(':
            low += 1
            high += 1
        elif char == ')':
            low = max(0, low - 1)  # Can't go below 0
            high -= 1
        else:  # '*'
            low = max(0, low - 1)  # Treat as ')'
            high += 1  # Treat as '('
        
        # If high < 0, too many ')'
        if high < 0:
            return False
    
    # Valid if can balance (low == 0)
    return low == 0

def reverseParentheses(s: str) -> str:
    """
    Reverse substrings in each pair of matching parentheses.
    
    Example: "(ed(et(oc))el)" → "leetcode"
    
    Stack approach: Store strings, reverse when closing bracket found
    
    Time: O(n²), Space: O(n)
    """
    stack = ['']
    
    for char in s:
        if char == '(':
            stack.append('')  # New level
        elif char == ')':
            # Reverse current level and append to previous
            current = stack.pop()
            stack[-1] += current[::-1]
        else:
            stack[-1] += char
    
    return stack[0]

def scoreOfParentheses(s: str) -> int:
    """
    Calculate score: () = 1, AB = A + B, (A) = 2 * A
    
    Example: "(())" = 2, "()()" = 2
    
    Stack approach: Track scores at each depth
    
    Time: O(n), Space: O(n)
    """
    stack = [0]
    
    for char in s:
        if char == '(':
            stack.append(0)  # New depth
        else:
            score = stack.pop()
            # () → 1, (A) → 2*A
            stack[-1] += max(2 * score, 1)
    
    return stack[0]

```

---

## 🏆 LeetCode Problems

### 🟢 Easy

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack Match | O(n) | O(n) |
| 1021 | [Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/) | Counter | O(n) | O(n) |
| 1614 | [Maximum Nesting Depth](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) | Counter | O(n) | O(1) |

### 🟡 Medium

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Backtracking | O(4ⁿ/√n) | O(n) |
| 678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Range Tracking | O(n) | O(1) |
| 856 | [Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/) | Stack | O(n) | O(n) |
| 921 | [Minimum Add to Make Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | Counter | O(n) | O(1) |
| 1190 | [Reverse Substrings Between Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/) | Stack | O(n²) | O(n) |
| 1249 | [Minimum Remove to Make Valid](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | Two Pass | O(n) | O(n) |
| 1541 | [Minimum Insertions to Balance](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/) | Counter | O(n) | O(1) |

### 🔴 Hard

| # | Problem | Pattern | Time | Space |
|:-:|---------|---------|:----:|:-----:|
| 32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | Stack/DP | O(n) | O(n) |
| 301 | [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) | BFS/DFS | O(2ⁿ) | O(n) |
| 591 | [Tag Validator](https://leetcode.com/problems/tag-validator/) | Stack | O(n) | O(n) |

---

## 💡 Key Insights & Pro Tips

> **🎯 Stack vs Counter**  
> Single type `()`: Use counter (O(1) space). Multiple types `()[]{}`: Need stack to track order!

> **⚡ Two Conditions for Validity**  
> (1) Equal opens and closes, (2) Prefix sum never negative. Both necessary!

> **🔄 Longest Valid Trick**  
> Stack stores indices of *unmatched* positions. Gaps between = valid substrings!

> **📊 Generation Constraints**  
> Can add `(` if `open < n`. Can add `)` if `close < open`. Maintains validity throughout!

> **🔍 Wildcard Strategy**  
> Track range [low, high] of possible open brackets. Wildcard expands range.

> **💰 Two-Pass Pattern**  
> Mark invalid indices first pass, build result second pass. Cleaner than one-pass!

---

## 🎓 Pattern Recognition Guide

### Identifying Parentheses Patterns

| Problem Contains... | Pattern | Technique | Example |
|--------------------|---------|-----------|---------|
| "valid parentheses" | Matching | Stack | #20 |
| "minimum add/remove" | Balance | Counter | #921, #1249 |
| "longest valid" | Substring | Stack indices | #32 |
| "generate all" | Enumeration | Backtracking | #22 |
| "with wildcard *" | Ambiguity | Range tracking | #678 |
| "nesting depth" | Levels | Counter | #1614 |
| "reverse between" | Nested operations | Stack | #1190 |
| "score/value" | Calculation | Stack | #856 |

---

## 🧮 Complexity Analysis

### Algorithm Comparison

| Problem | Naive | Optimized | Key Insight |
|---------|:-----:|:---------:|-------------|
| **Valid** | O(n²) check all | **O(n) stack** | One pass sufficient |
| **Min Add** | O(n) with stack | **O(1) counter** | Don't need order |
| **Longest Valid** | O(n²) DP | **O(n) stack** | Track indices |
| **Generate** | O(2^(2n)) all | **O(4ⁿ/√n)** | Prune invalid early |

---

## 📚 References & Learning Resources

### 📖 Core Concepts

| Resource | Topic | Link |
|----------|-------|------|
| **GeeksforGeeks** | Balanced parentheses | [Tutorial](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/) |
| **Wikipedia** | Dyck language | [Article](https://en.wikipedia.org/wiki/Dyck_language) |
| **CP Algorithms** | Bracket sequences | [Guide](https://cp-algorithms.com/combinatorics/bracket_sequences.html) |
| **OEIS** | Catalan numbers | [A000108](https://oeis.org/A000108) |

### 🎥 Video Tutorials

| Creator | Topic | Link |
|---------|-------|------|
| **NeetCode** | Valid Parentheses | [YouTube](https://www.youtube.com/watch?v=WTzjTskDFMg) |
| **NeetCode** | Generate Parentheses | [YouTube](https://www.youtube.com/watch?v=s9fokUqJ76A) |
| **NeetCode** | Longest Valid | [YouTube](https://www.youtube.com/watch?v=VdQuwtEd10M) |
| **Back To Back SWE** | Complete guide | [YouTube](https://www.youtube.com/watch?v=qC5DYX89HJg) |
| **Tech Dose** | Multiple problems | [YouTube](https://www.youtube.com/watch?v=QZOLb0xHB_Q) |

### 📝 Interactive Learning

| Platform | Focus | Link |
|----------|-------|------|
| **VisuAlgo** | Stack visualization | [Website](https://visualgo.net/en/list) |
| **Algorithm Visualizer** | Backtracking tree | [Website](https://algorithm-visualizer.org/) |

---

## 🎯 Practice Roadmap

### Week 1: Fundamentals

1. **Valid Parentheses** (#20) - Master stack pattern

2. **Min Add to Make Valid** (#921) - Learn counter approach

3. **Max Nesting Depth** (#1614) - Simple depth tracking

### Week 2: Intermediate

4. **Generate Parentheses** (#22) - Master backtracking

5. **Min Remove to Make Valid** (#1249) - Two-pass technique

6. **Valid Parenthesis String** (#678) - Range tracking with wildcards

### Week 3: Advanced

7. **Longest Valid Parentheses** (#32) - Stack with indices

8. **Remove Invalid Parentheses** (#301) - BFS/DFS approach

9. **Score of Parentheses** (#856) - Calculation with stack

### Mastery Challenge

- Solve each problem in < 15 minutes

- Implement both stack and O(1) space solutions where possible

- Explain Catalan number connection

---

## 💭 Common Interview Questions

**Q: Why can't we use just a counter for multiple bracket types?**  
A: Because order matters. `([)]` has balanced counts but is invalid. Stack tracks the nesting order!

**Q: What's the connection to Catalan numbers?**  
A: Valid parentheses with n pairs = nth Catalan number. Related to many combinatorial problems!

**Q: How to solve longest valid in O(1) space?**  
A: Two passes (left-to-right and right-to-left) tracking open/close counts. Tricky but elegant!

**Q: Why is generate parentheses O(4ⁿ/√n)?**  
A: It's the nth Catalan number (number of valid strings). Each string takes O(n) to build.

**Q: When to use stack vs counter?**  
A: Stack for multiple types or when order matters. Counter for single type with just validity check.

---

## 🧩 Common Pitfalls & Solutions

### Pitfall 1: Not Checking Stack Empty

```python
# ❌ WRONG: May crash
if pairs[stack.pop()] != char:
    return False

# ✅ CORRECT: Check first
if not stack or pairs[stack.pop()] != char:
    return False

```

### Pitfall 2: Forgetting Base Case

```python
# ❌ WRONG: No base in stack
stack = []  # Crash on first valid ')'

# ✅ CORRECT: Base index
stack = [-1]  # Enables length calculation

```

### Pitfall 3: Wrong Backtracking Constraint

```python
# ❌ WRONG: Allows invalid intermediate
if close_count <= n:  # Too permissive!
    backtrack(current + ')')

# ✅ CORRECT: Maintain validity
if close_count < open_count:  # Always valid
    backtrack(current + ')')

```

---

<div align="center">

### 🔗 Master Parentheses: From Validation to Generation

*Stack matching, Catalan numbers, and backtracking - three pillars of parentheses problems*

**Made with ❤️ by [Gaurav Goswami](https://github.com/Gaurav14cs17)**

[⬅️ Basic Stack](../01_basic_stack/README.md) | [➡️ Monotonic Stack](../03_monotonic_stack/README.md)

---

*"Balance is key: opens must precede closes, totals must match."*  
*Start with Valid Parentheses (#20) today!* 🚀

</div>

---

## 🧭 Navigation

| ⬅️ Previous | 📂 Current | ➡️ Next |
|:------------|:----------:|--------:|
| [← 01. Basic Stack](../01_basic_stack/README.md) | **02. Parentheses** | [03. Monotonic Stack →](../03_monotonic_stack/README.md) |
