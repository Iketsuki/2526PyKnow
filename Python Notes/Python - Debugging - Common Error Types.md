---
tags: [python, debugging, errors, exception-types]
moc: [[Python - Debugging (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: common error types and causes."
  - "Understand: what each error type means."
  - "Apply: recognize and categorize errors."
  - "Analyze: error messages and fix strategies."
  - "Create: error-aware code with proper handling."
---

# Python - Debugging - Common Error Types

## Concept
Python has many error types. Understanding what each means helps debug faster.

## Syntax Errors (Before Running)

```python
# SyntaxError: Missing colon
if x == 5
    print(x)
# SyntaxError: invalid syntax

# SyntaxError: Mismatched parentheses
result = (1 + 2 * 3
# SyntaxError: unexpected EOF

# SyntaxError: Invalid operator
result = 5 ** ** 2
# SyntaxError: invalid syntax
```

## Name & Attribute Errors

```python
# NameError: Variable not defined
print(age)
# NameError: name 'age' is not defined

# NameError: Typo in variable
x = 10
print(X)  # Capital X, but defined lowercase x
# NameError: name 'X' is not defined

# AttributeError: Method doesn't exist
text = 'hello'
text.unknown_method()
# AttributeError: 'str' object has no attribute 'unknown_method'

# AttributeError: Wrong object type
num = 5
num.append(10)  # Numbers don't have append()
# AttributeError: 'int' object has no attribute 'append'
```

## Type Errors

```python
# TypeError: Unsupported operation
result = '5' + 5  # Can't add string and number
# TypeError: can only concatenate str (not "int") to str

# TypeError: Wrong argument count
def add(a, b):
    return a + b

add(5)  # Missing argument
# TypeError: add() missing 1 required positional argument: 'b'

# TypeError: Unpacking wrong type
a, b = 5  # Can't unpack number
# TypeError: cannot unpack non-iterable int object
```

## Value Errors

```python
# ValueError: Can't convert value
num = int('hello')
# ValueError: invalid literal for int() with base 10: 'hello'

# ValueError: Wrong number of values
a, b, c = [1, 2]  # 3 targets but only 2 values
# ValueError: not enough values to unpack (expected 3, got 2)

# ValueError: Unpacking wrong count
x, y = [1, 2, 3]
# ValueError: too many values to unpack (expected 2)
```

## Index & Key Errors

```python
# IndexError: List index out of range
items = [1, 2, 3]
print(items[10])
# IndexError: list index out of range

# IndexError: String index out of range
text = 'hello'
print(text[100])
# IndexError: string index out of range

# KeyError: Dictionary key doesn't exist
student = {'name': 'Alice'}
print(student['age'])
# KeyError: 'age'

# KeyError: Typo in key
data = {'count': 10}
print(data['cnt'])  # Typo!
# KeyError: 'cnt'
```

## Math Errors

```python
# ZeroDivisionError: Divide by zero
result = 10 / 0
# ZeroDivisionError: division by zero

# FloatingPointError: Math operation fails
import math
math.log(0)  # Log of zero is undefined
# ValueError: math domain error
```

## File & Module Errors

```python
# FileNotFoundError: File doesn't exist
with open('missing.txt', 'r') as f:
    content = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'

# ModuleNotFoundError / ImportError: Module not found
import unknown_module
# ModuleNotFoundError: No module named 'unknown_module'

# ImportError: Specific import fails
from math import unknown_function
# ImportError: cannot import name 'unknown_function' from 'math'
```

## Real Examples with Errors

```python
# Example 1: Multiple errors in sequence
def process(data):
    # NameError if data not defined
    value = data['count']  # KeyError if 'count' not in dict
    result = 100 / value  # ZeroDivisionError if value is 0
    return result

# Example 2: Type errors in calculation
numbers = [1, 2, '3', 4]  # Mixed types!
total = sum(numbers)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Example 3: Index errors in loop
items = [10, 20, 30]
for i in range(5):  # Goes beyond list size
    print(items[i])  # IndexError on 4th iteration
```

## Error Type Summary

| Error | Cause | Example |
|-------|-------|---------|
| `SyntaxError` | Code structure problem | Missing colon, parenthesis mismatch |
| `NameError` | Variable/function not defined | Typo, scope issue |
| `AttributeError` | Object doesn't have attribute | `5.append()` |
| `TypeError` | Wrong data type | `'5' + 5` |
| `ValueError` | Wrong value for operation | `int('abc')` |
| `IndexError` | List index out of range | `lst[100]` |
| `KeyError` | Dictionary key missing | `d['missing']` |
| `ZeroDivisionError` | Divide by zero | `10 / 0` |
| `FileNotFoundError` | File doesn't exist | `open('missing.txt')` |
| `ModuleNotFoundError` | Module not installed/found | `import xyz` |

## Exercises by Bloom Level

- **Remember**: Name 5 common error types.
- **Understand**: What causes TypeError vs ValueError?
- **Apply**: Identify error types in code.
- **Analyze**: Fix errors based on error messages.
- **Create**: Write code that prevents and handles errors.

## Common Errors with Example Code

### Error 1: Confusing similar-sounding error types
```python
# WRONG: Mixing up KeyError and AttributeError
# KeyError is for dicts, AttributeError is for objects
d = {'name': 'Alice'}
d.name  # AttributeError: 'dict' object has no attribute 'name'
d['missing']  # KeyError: 'missing'

# CORRECT: Use appropriate method
print(d['name'])  # KeyError if missing
print(d.get('name', 'Unknown'))  # Safe dict access
```

### Error 2: Not checking before indexing
```python
# WRONG: Assuming list has enough items
data = [1, 2]
print(data[5])  # IndexError!

# CORRECT: Check length
if len(data) > 5:
    print(data[5])

# OR: Use slicing (safe)
print(data[5:6])  # Returns [] (empty), not error
```

### Error 3: Type assumptions
```python
# WRONG: Assuming value is number
value = '10'
result = value * 2  # '1010' not 20!

# CORRECT: Check or convert type
value = int('10')
result = value * 2  # 20
```

### Error 4: Missing imports
```python
# WRONG: Using module without importing
result = sqrt(16)
# NameError: name 'sqrt' is not defined

# CORRECT: Import first
from math import sqrt
result = sqrt(16)

# OR:
import math
result = math.sqrt(16)
```

### Error 5: Variable scope issues
```python
# WRONG: Using variable outside scope
if True:
    x = 10

print(x)  # This works in Python (scope is function-level)

# But in function:
def test():
    if True:
        y = 10
    print(y)  # Still works (loop/if don't create scope)

# CORRECT: Understand Python's scope rules
```

## Error Prevention Tips

```python
# ✓ Check before accessing
if key in data:
    value = data[key]

# ✓ Check type
if isinstance(value, int):
    result = value + 5

# ✓ Use safe methods
value = d.get('key', default)

# ✓ Validate input
if len(items) > 0:
    first = items[0]

# ✓ Handle conversions
try:
    num = int(value)
except ValueError:
    num = 0  # Default
```

## Tips
- **Read the error message** — It tells you what went wrong and where.
- **Look at the last line** of traceback for the actual error type.
- **Common mistakes**: Typos in variables, wrong types, missing keys/indices.
- **Prevent errors** — Check before accessing, validate input, use safe methods.
- **Use try-except** for expected errors (conversions, file access).

## Related Concepts
- [[Python - Debugging - Reading Tracebacks]]
- [[Python - Debugging - Try-Except Basics]]
- [[Python - Debugging - Debugging Strategies]]

## MOC
- Parent: [[Python - Debugging (MOC)]]
