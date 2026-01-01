# Parser Recursion: Basic Calculator (LeetCode 224)

## 🎯 Problem Statement

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain:
- `+`, `-` operators
- `(`, `)` parentheses  
- Non-negative integers
- Spaces

### Examples:

| Input | Output | Explanation |
|-------|--------|-------------|
| `"1 + 1"` | `2` | Simple addition |
| `" 2-1 + 2 "` | `3` | Spaces ignored |
| `"(1+(4+5+2)-3)+(6+8)"` | `23` | Nested parentheses |
| `"-(2+3)"` | `-5` | Unary minus |

---

## 📐 Grammar Definition

```
expression → term (('+' | '-') term)*
term       → factor
factor     → number | '(' expression ')' | ('-' | '+') factor
number     → digit+
```

### Why This Grammar?

| Rule | Purpose |
|------|---------|
| **expression** | Handle `+` and `-` (lowest precedence) |
| **term** | Reserved for `*` and `/` (higher precedence) |
| **factor** | Handle numbers, parentheses, unary operators |

---

## 🔍 Why Recursion?

```
(1+(4+5+2)-3)+(6+8)
   ↑
 Nested parentheses!
 
When we see '(', we RECURSE to evaluate the inner expression.
```

### Recursion Flow:

```
evaluate("(1+(4+5+2)-3)+(6+8)")
│
├─► See '(' → RECURSE to evaluate inside
│   │
│   └─► evaluate("1+(4+5+2)-3")
│       │
│       ├─► 1
│       ├─► + 
│       ├─► See '(' → RECURSE DEEPER
│       │   │
│       │   └─► evaluate("4+5+2")
│       │       = 4 + 5 + 2 = 11
│       │
│       ├─► - 3
│       └─► Returns: 1 + 11 - 3 = 9
│   
│   First part = 9
│
├─► +
│
├─► See '(' → RECURSE
│   │
│   └─► evaluate("6+8")
│       = 6 + 8 = 14
│   
│   Second part = 14
│
└─► FINAL: 9 + 14 = 23
```

---

## 💻 Complete Code with Comments

```python
class Calculator:
    """
    Basic Calculator (LeetCode 224).
    
    Grammar:
        expression → term (('+' | '-') term)*
        term       → factor
        factor     → number | '(' expression ')' | ('-' | '+') factor
    
    Time:  O(n)
    Space: O(depth of nesting)
    """
    
    def __init__(self, s: str):
        self.s = s
        self.pos = 0
        self.n = len(s)
    
    def calculate(self) -> int:
        """Entry point: evaluate the expression."""
        return self.expression()
    
    def expression(self) -> int:
        """
        expression → term (('+' | '-') term)*
        
        Handles addition and subtraction.
        """
        result = self.term()
        
        while self.pos < self.n:
            self.skip_spaces()
            
            if self.pos >= self.n:
                break
            
            op = self.s[self.pos]
            
            if op not in '+-':
                break  # Not our operator, exit
            
            self.pos += 1  # Consume operator
            right = self.term()
            
            if op == '+':
                result += right
            else:
                result -= right
        
        return result
    
    def term(self) -> int:
        """
        term → factor
        
        In Basic Calculator, term = factor.
        Reserved for * / in more complex calculators.
        """
        return self.factor()
    
    def factor(self) -> int:
        """
        factor → number | '(' expression ')' | ('-' | '+') factor
        
        Handles:
          - Numbers
          - Parenthesized expressions (RECURSION)
          - Unary + and -
        """
        self.skip_spaces()
        
        if self.pos >= self.n:
            return 0
        
        char = self.s[self.pos]
        
        # ┌────────────────────────────────┐
        # │ Unary minus: -expr             │
        # │ Example: -(2+3) = -5           │
        # └────────────────────────────────┘
        if char == '-':
            self.pos += 1
            return -self.factor()  # ★ RECURSE ★
        
        # ┌────────────────────────────────┐
        # │ Unary plus: +expr              │
        # │ Just skip it                   │
        # └────────────────────────────────┘
        if char == '+':
            self.pos += 1
            return self.factor()  # ★ RECURSE ★
        
        # ┌────────────────────────────────────────────┐
        # │ Parenthesized expression: (expr)           │
        # │ RECURSE to evaluate what's inside          │
        # └────────────────────────────────────────────┘
        if char == '(':
            self.pos += 1  # Skip '('
            result = self.expression()  # ★ RECURSE ★
            self.skip_spaces()
            self.pos += 1  # Skip ')'
            return result
        
        # ┌────────────────────────────────┐
        # │ Number: one or more digits     │
        # └────────────────────────────────┘
        return self.number()
    
    def number(self) -> int:
        """
        number → digit+
        
        Parse an integer.
        """
        self.skip_spaces()
        
        num = 0
        while self.pos < self.n and self.s[self.pos].isdigit():
            num = num * 10 + int(self.s[self.pos])
            self.pos += 1
        
        return num
    
    def skip_spaces(self):
        """Skip whitespace characters."""
        while self.pos < self.n and self.s[self.pos] == ' ':
            self.pos += 1


def calculate(s: str) -> int:
    """Wrapper function for LeetCode."""
    return Calculator(s).calculate()
```

---

## 🔍 Step-by-Step Trace: `"(1+(4+5+2)-3)"`

### Initial State:
```
s = "(1+(4+5+2)-3)"
pos = 0
```

### Execution Trace:

```
expression() starts
│
└─► term() → factor()
    │
    ├─► pos=0: char='(' → Parenthesized!
    │   pos = 1 (skip '(')
    │   │
    │   └─► expression()  [LEVEL 2]
    │       │
    │       ├─► term() → factor() → number()
    │       │   Read '1', pos = 2
    │       │   result = 1
    │       │
    │       ├─► pos=2: char='+' → Continue loop
    │       │   pos = 3 (skip '+')
    │       │   │
    │       │   └─► term() → factor()
    │       │       │
    │       │       ├─► pos=3: char='(' → Parenthesized!
    │       │       │   pos = 4 (skip '(')
    │       │       │   │
    │       │       │   └─► expression()  [LEVEL 3]
    │       │       │       │
    │       │       │       ├─► 4 (number)
    │       │       │       ├─► + 5 = 9
    │       │       │       ├─► + 2 = 11
    │       │       │       ├─► pos=10: char=')' → Exit loop
    │       │       │       └─► Returns 11
    │       │       │   
    │       │       │   pos = 11 (skip ')')
    │       │       │   Returns 11
    │       │   
    │       │   result = 1 + 11 = 12
    │       │
    │       ├─► pos=11: char='-' → Continue loop
    │       │   pos = 12 (skip '-')
    │       │   │
    │       │   └─► term() → factor() → number()
    │       │       Read '3', pos = 13
    │       │       Returns 3
    │       │
    │       │   result = 12 - 3 = 9
    │       │
    │       ├─► pos=13: char=')' → Exit loop
    │       └─► Returns 9
    │   
    │   pos = 14 (skip ')')
    │   Returns 9
    
FINAL: 9 ✓
```

---

## 📊 Visual Grammar Tree

```
                    expression
                        │
            ┌───────────┼───────────┐
            │           │           │
          term         "+"        term
            │                       │
         factor                   factor
            │                       │
    "(" expression ")"        "(" expression ")"
            │                       │
     1 + (4+5+2) - 3              6 + 8
            │                       │
            9                      14
                    
                    = 9 + 14 = 23
```

---

## 📊 Operator Precedence

```
                  PRECEDENCE
                      │
    LOWEST ───────────┼───────────► HIGHEST
                      │
                      │
    ┌─────────────────┼─────────────────────┐
    │                 │                     │
    │    + -          │    * /              │  ( ) numbers
    │  (expression)   │   (term)            │   (factor)
    │                 │                     │
    │  evaluated      │  evaluated          │  evaluated
    │  LAST           │  next               │  FIRST
    │                 │                     │
    └─────────────────┼─────────────────────┘
                      │
                      
    Example: 1 + 2 * 3
    
    Grammar: expression → term + term
                           ↓       ↓
                           1    term
                                  ↓
                               2 * 3 = 6
    
    Result: 1 + 6 = 7 ✓
```

---

## 🎓 Key Insights

### 1. Grammar → Functions

| Grammar Rule | Function | Handles |
|--------------|----------|---------|
| `expression → term (('+'\|'-') term)*` | `expression()` | `+`, `-` |
| `term → factor` | `term()` | Reserved for `*`, `/` |
| `factor → number \| '(' expr ')' \| unary` | `factor()` | Numbers, parens, unary |

### 2. Three Types of Recursion

```python
# 1. Unary Operators (recursive factor)
if char == '-':
    return -self.factor()  # RECURSE

# 2. Parentheses (recursive expression)
if char == '(':
    self.pos += 1
    result = self.expression()  # RECURSE
    self.pos += 1
    return result

# 3. Implicit Recursion (expression → term → factor → expression)
# The grammar itself is mutually recursive
```

### 3. Handling Edge Cases

| Case | Input | How Handled |
|------|-------|-------------|
| Spaces | `" 1 + 2 "` | `skip_spaces()` |
| Unary minus | `"-5"` | `factor()` handles `-` |
| Nested | `"((1))"` | Multiple recursion |
| Empty parens | Not valid | Grammar prevents |

---

## ⏱️ Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(n) | Each character visited once |
| **Space** | O(depth) | Recursion depth = nesting level |

---

## 🏆 Related Problems

| # | Problem | Difference |
|:-:|---------|------------|
| 227 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Adds `*` `/`, no parens |
| 772 | [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) | Full: `+ - * / ( )` |
| 770 | [Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/) | Variables! |

---

## 📊 Comparison with Other Calculators

| Feature | LC 224 | LC 227 | LC 772 |
|---------|:------:|:------:|:------:|
| `+` `-` | ✅ | ✅ | ✅ |
| `*` `/` | ❌ | ✅ | ✅ |
| `( )` | ✅ | ❌ | ✅ |
| Unary | ✅ | ❌ | ✅ |

---

## 🔗 See Also

- [Decode String Explained](./decode_string_explained.md) - Similar recursion pattern
- [Number of Atoms Explained](./number_of_atoms_explained.md) - Parsing chemical formulas
- [Parser Recursion README](../) - Full topic overview

---

<div align="center">

**Made with ❤️ for understanding Parser Recursion**

</div>

