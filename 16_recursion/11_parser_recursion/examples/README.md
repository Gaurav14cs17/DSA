# Parser Recursion Examples

This folder contains detailed step-by-step explanations of parser recursion problems.

---

## 📚 Examples Index

| # | Problem | File | Difficulty | Key Concept |
|:-:|---------|------|:----------:|-------------|
| 1 | **Number of Atoms** (LC 726) | [📖 View](./number_of_atoms_explained.md) | 🔴 Hard | Nested groups with multipliers |
| 2 | **Decode String** (LC 394) | [📖 View](./decode_string_explained.md) | 🟡 Medium | Nested `k[string]` pattern |
| 3 | **Basic Calculator** (LC 224) | [📖 View](./basic_calculator_explained.md) | 🔴 Hard | Expression with parentheses |

---

## 🎯 What Each Example Covers

### 1. Number of Atoms (LeetCode 726)

**Input:** `"K4(ON(SO3)2)2"`  
**Output:** `"K4N2O14S4"`

```
What you'll learn:
+-- Grammar definition for chemical formulas
+-- Parsing atoms (e.g., "Mg", "Fe")
+-- Parsing numbers (e.g., "2", "12")
+-- Handling nested parentheses with multipliers
+-- Merging atom counts from recursive calls

```

**Diagrams Included:**

- Call Stack Visualization

- Decision Flowchart

- Parse Tree

- Position Pointer Animation

---

### 2. Decode String (LeetCode 394)

**Input:** `"3[a2[c]]"`  
**Output:** `"accaccacc"`

```
What you'll learn:
+-- Grammar for k[encoded_string]
+-- Accumulating repeat counts
+-- Nested bracket recursion
+-- String concatenation with repetition
+-- Return value propagation

```

---

### 3. Basic Calculator (LeetCode 224)

**Input:** `"(1+(4+5+2)-3)+(6+8)"`  
**Output:** `23`

```
What you'll learn:
+-- Expression grammar with precedence
+-- Handling + and - operators
+-- Parenthesized sub-expressions
+-- Unary operators (-, +)
+-- Operator precedence through grammar

```

---

## 📊 Visual Comparison

### When to RECURSE:

```
Number of Atoms:   Mg(OH)2
                      ↑
                    '(' → RECURSE

Decode String:     3[a2[c]]
                    ↑
                   '[' → RECURSE

Basic Calculator:  (1+(4+5))
                   ↑
                  '(' → RECURSE

```

### When to RETURN:

```
Number of Atoms:   Mg(OH)2
                       ↑
                     ')' → RETURN counts

Decode String:     3[a2[c]]
                        ↑
                       ']' → RETURN string

Basic Calculator:  (1+(4+5))
                          ↑
                         ')' → RETURN value

```

---

## 📐 Common Parser Pattern

All three problems follow the same structure:

```python
class Parser:
    def __init__(self, s: str):
        self.s = s
        self.pos = 0
    
    def parse(self):
        """Entry point."""
        return self.parseRule()
    
    def parseRule(self):
        """Main parsing rule."""
        result = initial_value
        
        while self.pos < len(self.s):
            char = self.s[self.pos]
            
            if is_trigger_for_recursion(char):
                # ★ RECURSE ★
                nested = self.parseRule()
                result = combine(result, nested)
            
            elif is_end_condition(char):
                # RETURN to parent
                return result
            
            else:
                # Process current character
                result = process(result, char)
                self.pos += 1
        
        return result

```

---

## 🔄 Comparison Table

| Aspect | Number of Atoms | Decode String | Basic Calculator |
|--------|:---------------:|:-------------:|:----------------:|
| **Nesting Trigger** | `(` | `[` | `(` |
| **Nesting End** | `)` | `]` | `)` |
| **Number Follows** | After `)` or Atom | Before `[` | N/A |
| **Returns** | `dict` | `str` | `int` |
| **Merge Operation** | Add counts | Concatenate × k | Evaluate operators |

---

## 🎓 Learning Path

**Recommended order:**

```
1. Decode String (easiest)
   +-- Simpler grammar
   +-- String result (easy to visualize)
   +-- Good introduction to pattern

2. Number of Atoms (medium)
   +-- Dictionary merging
   +-- Post-fix multipliers
   +-- Multiple token types

3. Basic Calculator (hardest)
   +-- Operator precedence
   +-- Multiple grammar rules
   +-- Mutual recursion

```

---

## 📁 Folder Structure

```
examples/
+-- README.md                          ← You are here
+-- number_of_atoms_explained.md       ← LeetCode 726
+-- decode_string_explained.md         ← LeetCode 394
+-- basic_calculator_explained.md      ← LeetCode 224

```

---

## 🔗 Back to Main

- [← Parser Recursion README](../)

- [← Recursion Main](../../)

---

<div align="center">

**Made with ❤️ for understanding Parser Recursion**

</div>

