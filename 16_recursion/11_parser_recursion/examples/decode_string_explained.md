# Parser Recursion: Decode String (LeetCode 394)

## 🎯 Problem Statement

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is being repeated exactly k times.

### Examples:

| Input | Output | Explanation |
|-------|--------|-------------|
| `"3[a]"` | `"aaa"` | 'a' repeated 3 times |
| `"3[a2[c]]"` | `"accaccacc"` | Nested: '2[c]'='cc', then 'a'+'cc'='acc' × 3 |
| `"2[abc]3[cd]ef"` | `"abcabccdcdcdef"` | Multiple groups + letters |
| `"100[leetcode]"` | `"leetcode..."×100` | Large repetition |

---

## 📐 Grammar Definition

```
string  →  (letters | group)*
group   →  number '[' string ']'
number  →  digit+
letters →  letter+
```

### Grammar Rules Explained:

| Rule | Pattern | Meaning |
|------|---------|---------|
| **string** | `(letters \| group)*` | Zero or more letters or groups |
| **group** | `number '[' string ']'` | Number followed by bracketed content |
| **number** | `digit+` | One or more digits |
| **letters** | `letter+` | One or more letters |

---

## 🔍 Why Recursion?

```
3[a2[c]]
    ↑
 Nested brackets!
 
When we see '[', we RECURSE to decode what's inside.
```

### Recursion Flow:

```
decode("3[a2[c]]")
│
├─► Read '3'  →  k = 3
├─► See '['   →  RECURSE!
│   │
│   └─► decode("a2[c]")
│       │
│       ├─► Read 'a'  →  result = "a"
│       ├─► Read '2'  →  k = 2
│       ├─► See '['   →  RECURSE DEEPER!
│       │   │
│       │   └─► decode("c")
│       │       ├─► Read 'c'  →  result = "c"
│       │       └─► See ']'   →  RETURN "c"
│       │   │
│       │   result = "c" × 2 = "cc"
│       │
│       ├─► Add to result: "a" + "cc" = "acc"
│       └─► See ']'   →  RETURN "acc"
│   │
│   result = "acc" × 3 = "accaccacc"
│
└─► FINAL: "accaccacc"
```

---

## 💻 Complete Code with Comments

```python
def decodeString(s: str) -> str:
    """
    Decode String (LeetCode 394).
    
    Grammar:
        string  → (letters | group)*
        group   → number '[' string ']'
        number  → digit+
        letters → letter+
    
    Time:  O(output length)
    Space: O(nesting depth)
    """
    
    def parse(pos: int) -> tuple[str, int]:
        """
        Parse starting at position pos.
        
        Returns: (decoded_string, new_position)
        
        STOPS when:
          - End of string
          - Hits ']' (end of current group)
        """
        result = ""
        num = 0
        
        while pos < len(s):
            char = s[pos]
            
            if char.isdigit():
                # ┌─────────────────────────────┐
                # │ Accumulate the repeat count │
                # └─────────────────────────────┘
                # Example: "12[a]" → num becomes 12
                num = num * 10 + int(char)
                pos += 1
            
            elif char == '[':
                # ┌────────────────────────────────┐
                # │ Start of group → RECURSE       │
                # │ Parse content inside brackets  │
                # └────────────────────────────────┘
                pos += 1  # Skip '['
                nested_content, pos = parse(pos)  # ★ RECURSE ★
                result += num * nested_content    # Repeat num times
                num = 0                           # Reset for next group
            
            elif char == ']':
                # ┌──────────────────────────────────┐
                # │ End of current group → RETURN    │
                # │ Go back to parent recursion call │
                # └──────────────────────────────────┘
                pos += 1  # Skip ']'
                return result, pos
            
            else:
                # ┌─────────────────────────┐
                # │ Regular letter → append │
                # └─────────────────────────┘
                result += char
                pos += 1
        
        return result, pos
    
    decoded, _ = parse(0)
    return decoded
```

---

## 🔍 Step-by-Step Trace: `"3[a2[c]]"`

### Initial State:
```
s = "3[a2[c]]"
pos = 0
```

### Execution Trace:

```
parse(pos=0)
│
├─► pos=0: char='3' is DIGIT
│   num = 0*10 + 3 = 3
│   pos = 1
│
├─► pos=1: char='[' 
│   ┌──────────────────────────┐
│   │ RECURSE into nested call │
│   └──────────────────────────┘
│   pos = 2  (skip '[')
│   │
│   └─► parse(pos=2)  [LEVEL 2]
│       │
│       ├─► pos=2: char='a' is LETTER
│       │   result = "" + "a" = "a"
│       │   pos = 3
│       │
│       ├─► pos=3: char='2' is DIGIT
│       │   num = 0*10 + 2 = 2
│       │   pos = 4
│       │
│       ├─► pos=4: char='['
│       │   ┌──────────────────────────┐
│       │   │ RECURSE into nested call │
│       │   └──────────────────────────┘
│       │   pos = 5  (skip '[')
│       │   │
│       │   └─► parse(pos=5)  [LEVEL 3]
│       │       │
│       │       ├─► pos=5: char='c' is LETTER
│       │       │   result = "" + "c" = "c"
│       │       │   pos = 6
│       │       │
│       │       ├─► pos=6: char=']'
│       │       │   ┌─────────────────────┐
│       │       │   │ End of group, RETURN │
│       │       │   └─────────────────────┘
│       │       │   pos = 7
│       │       │
│       │       └─► Returns ("c", 7)
│       │   
│       │   Back in LEVEL 2:
│       │   nested_content = "c"
│       │   result = "a" + 2 * "c" = "a" + "cc" = "acc"
│       │   num = 0
│       │   pos = 7
│       │
│       ├─► pos=7: char=']'
│       │   ┌─────────────────────┐
│       │   │ End of group, RETURN │
│       │   └─────────────────────┘
│       │   pos = 8
│       │
│       └─► Returns ("acc", 8)
│   
│   Back in LEVEL 1:
│   nested_content = "acc"
│   result = "" + 3 * "acc" = "accaccacc"
│   num = 0
│   pos = 8
│
├─► pos=8: end of string
│
└─► Returns ("accaccacc", 8)

FINAL: "accaccacc" ✓
```

---

## 📊 Visual Position Diagram

```
Position:   0    1    2    3    4    5    6    7
          ┌────┬────┬────┬────┬────┬────┬────┬────┐
String:   │ 3  │ [  │ a  │ 2  │ [  │ c  │ ]  │ ]  │
          └────┴────┴────┴────┴────┴────┴────┴────┘
            ▲
           pos=0  Start


Step 1: Read '3', num=3
          ┌────┬────┬────┬────┬────┬────┬────┬────┐
          │ 3  │ [  │ a  │ 2  │ [  │ c  │ ]  │ ]  │
          └────┴────┴────┴────┴────┴────┴────┴────┘
            ✓
                 ▲
                pos=1


Step 2: See '[' → RECURSE (Level 2)
          ┌────┬────┬────┬────┬────┬────┬────┬────┐
          │ 3  │ [  │ a  │ 2  │ [  │ c  │ ]  │ ]  │
          └────┴────┴────┴────┴────┴────┴────┴────┘
                 ▼
               ENTER
                      ▲
                     pos=2


Step 3: Read 'a', result="a"
          ┌────┬────┬────┬────┬────┬────┬────┬────┐
          │ 3  │ [  │ a  │ 2  │ [  │ c  │ ]  │ ]  │
          └────┴────┴────┴────┴────┴────┴────┴────┘
                     ✓
                           ▲
                          pos=3


Step 4: Read '2', num=2
          ┌────┬────┬────┬────┬────┬────┬────┬────┐
          │ 3  │ [  │ a  │ 2  │ [  │ c  │ ]  │ ]  │
          └────┴────┴────┴────┴────┴────┴────┴────┘
                           ✓
                                ▲
                               pos=4


Step 5: See '[' → RECURSE (Level 3)
          ┌────┬────┬────┬────┬────┬────┬────┬────┐
          │ 3  │ [  │ a  │ 2  │ [  │ c  │ ]  │ ]  │
          └────┴────┴────┴────┴────┴────┴────┴────┘
                                ▼
                              ENTER
                                     ▲
                                    pos=5


Step 6: Read 'c', result="c"
          ┌────┬────┬────┬────┬────┬────┬────┬────┐
          │ 3  │ [  │ a  │ 2  │ [  │ c  │ ]  │ ]  │
          └────┴────┴────┴────┴────┴────┴────┴────┘
                                     ✓
                                          ▲
                                         pos=6


Step 7: See ']' → RETURN from Level 3
          ┌────┬────┬────┬────┬────┬────┬────┬────┐
          │ 3  │ [  │ a  │ 2  │ [  │ c  │ ]  │ ]  │
          └────┴────┴────┴────┴────┴────┴────┴────┘
                                [────────]
                                 Returns "c"
                                               ▲
                                              pos=7
        Back in Level 2: result = "a" + 2×"c" = "acc"


Step 8: See ']' → RETURN from Level 2
          ┌────┬────┬────┬────┬────┬────┬────┬────┐
          │ 3  │ [  │ a  │ 2  │ [  │ c  │ ]  │ ]  │
          └────┴────┴────┴────┴────┴────┴────┴────┘
                 [───────────────────────────────]
                           Returns "acc"
                                                    ▲
                                                   pos=8
        Back in Level 1: result = 3×"acc" = "accaccacc"


FINAL: "accaccacc" ✓
```

---

## 📊 Call Stack Visualization

```
┌─────────────────────────────────────────────────────────────┐
│                     CALL STACK GROWTH                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  TIME ─────────────────────────────────────────────►         │
│                                                              │
│                              ┌─────────────┐                 │
│                              │  parse(5)   │                 │
│                              │  result="c" │                 │
│                      ┌───────┼─────────────┤                 │
│                      │  parse(2)           │                 │
│                      │  result="acc"       │                 │
│              ┌───────┼─────────────────────┤                 │
│              │  parse(0)                   │                 │
│              │  result="accaccacc"         │                 │
│  ════════════╧═════════════════════════════╧══════════════   │
│              PUSH    PUSH    POP     POP                     │
│               ↓       ↓       ↓       ↓                      │
│  Level:       1       2       3       2→1                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎓 Key Insights

### 1. Grammar → Code

| Grammar Rule | Code Section |
|--------------|--------------|
| `string → (letters \| group)*` | `while pos < len(s)` loop |
| `group → number '[' string ']'` | `if char == '['` branch |
| `number → digit+` | `if char.isdigit()` branch |
| `letters → letter+` | `else` (regular letter) |

### 2. Recursion Pattern

```python
if char == '[':
    pos += 1                         # Skip '['
    nested, pos = parse(pos)         # ★ RECURSE ★
    result += num * nested           # Repeat
    num = 0                          # Reset
```

### 3. When to Recurse vs Stop

| Character | Action |
|-----------|--------|
| `0-9` | Accumulate number |
| `[` | **RECURSE** (enter nested level) |
| `]` | **RETURN** (exit current level) |
| `a-zA-Z` | Append to result |

---

## ⏱️ Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(output length) | Each output char produced once |
| **Space** | O(depth × max_string) | Recursion + intermediate strings |

---

## 🏆 Related Problems

| # | Problem | Similarity |
|:-:|---------|------------|
| 726 | [Number of Atoms](https://leetcode.com/problems/number-of-atoms/) | Same pattern, different tokens |
| 385 | [Mini Parser](https://leetcode.com/problems/mini-parser/) | Nested lists |
| 341 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Nested iteration |

---

## 🔗 See Also

- [Number of Atoms Explained](./number_of_atoms_explained.md) - Similar pattern with chemical formulas
- [Basic Calculator Explained](./basic_calculator_explained.md) - Expression parsing
- [Parser Recursion README](../) - Full topic overview

---

<div align="center">

**Made with ❤️ for understanding Parser Recursion**

</div>

