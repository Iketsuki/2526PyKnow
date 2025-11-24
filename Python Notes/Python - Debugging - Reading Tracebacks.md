---
tags: [python, debugging, traceback, errors]
moc: [[Python - Debugging (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: parts of a traceback structure."
  - "Understand: how to read and interpret error messages."
  - "Apply: locate bugs from tracebacks effectively."
  - "Analyze: trace execution flow through multiple functions."
  - "Create: fix programs based on traceback information."
---

# Python - Debugging - Reading Tracebacks

## Concept
A **traceback** shows the error location, call stack, and error message. Read from **bottom-up**: the last line is the error type, the lines above show where it happened.

## Traceback Structure

```
Traceback (most recent call last):
  File "script.py", line 10, in <module>
    result = int(name)
ValueError: invalid literal for int() with base 10: 'Alice'
```

**Structure breakdown:**
- **"Traceback (most recent call last):"** — Indicates an error occurred
- **File "script.py", line 10** — Where the error happened
- **in <module>** — Which function (top level if `<module>`)
- **result = int(name)** — The actual code that failed
- **ValueError:** — The error type
- **invalid literal...** — The error message explaining what went wrong

## Real Traceback Examples

### Example 1: Simple TypeError
```
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    result = '5' + 5
TypeError: can only concatenate str (not "int") to str
```
**Meaning**: Line 3 tried to add string and number. Fix: `str(5)` or `int('5')`.

### Example 2: NameError (Undefined Variable)
```
Traceback (most recent call last):
  File "test.py", line 2, in <module>
    print(age)
NameError: name 'age' is not defined
```
**Meaning**: Variable `age` was never created. Fix: Define it first with `age = 25`.

### Example 3: KeyError (Missing Dictionary Key)
```
Traceback (most recent call last):
  File "test.py", line 4, in <module>
    print(student['grade'])
KeyError: 'grade'
```
**Meaning**: Dictionary doesn't have 'grade' key. Fix: Use `.get('grade', default)`.

### Example 4: IndexError (List Index Out of Range)
```
Traceback (most recent call last):
  File "test.py", line 2, in <module>
    print(items[10])
IndexError: list index out of range
```
**Meaning**: List doesn't have 10 items. Fix: Check length or use slicing.

### Example 5: Multi-Level Traceback (Multiple Functions)
```
Traceback (most recent call last):
  File "main.py", line 15, in <module>
    result = process(data)
  File "main.py", line 8, in process
    return validate(value)
  File "main.py", line 3, in validate
    return int(value)
ValueError: invalid literal for int() with base 10: 'abc'
```
**Reading order**: 
1. Start at bottom: **ValueError** on conversion
2. Trace up: `validate()` called `int(value)`
3. `validate()` was called from `process()`
4. `process()` was called from line 15 in main
5. **Fix**: Check value before converting to int

## Common Error Types

| Error | Cause | Example Fix |
|-------|-------|-------------|
| `ValueError` | Wrong value type | Check value before converting |
| `TypeError` | Wrong data type | Use correct type or convert |
| `KeyError` | Missing dict key | Use `.get()` with default |
| `IndexError` | List index too large | Check list length first |
| `NameError` | Variable not defined | Define variable first |
| `FileNotFoundError` | File doesn't exist | Check file path or create file |
| `ZeroDivisionError` | Divide by zero | Check divisor isn't 0 |
| `AttributeError` | Method doesn't exist | Check object has method |

## Reading Tracebacks Step-by-Step

```python
# Code that will error:
def divide(a, b):
    return a / b

def calculate(values):
    return divide(values[0], values[1])

calculate([10])  # Will error - not enough values

# Traceback:
# Traceback (most recent call last):
#   File "test.py", line 8, in <module>
#     calculate([10])
#   File "test.py", line 6, in calculate
#     return divide(values[0], values[1])
#   File "test.py", line 3, in divide
#     return a / b
# IndexError: list index out of range

# Reading process:
# 1. Bottom line shows: IndexError on list access
# 2. Move up: divide() called values[0] and values[1]
# 3. Move up: calculate() called divide() with a short list
# 4. Top: called from line 8: calculate([10])
# 5. FIX: Check list has 2 items before dividing
```

## Real-World Debugging Example

```python
# Problem code:
students = {'Alice': 90, 'Bob': 85}

def get_grade(name):
    return students[name]  # Line 4

def display_grades():
    names = ['Alice', 'Bob', 'Charlie']  # Charlie not in students
    for name in names:
        print(f'{name}: {get_grade(name)}')  # Line 9

display_grades()  # Runs but errors

# Traceback shows:
# Traceback (most recent call last):
#   File "test.py", line 12, in <module>
#     display_grades()
#   File "test.py", line 9, in display_grades
#     print(f'{name}: {get_grade(name)}')
#   File "test.py", line 4, in get_grade
#     return students[name]
# KeyError: 'Charlie'

# FIX option 1: Check name exists
def get_grade(name):
    return students.get(name, 'N/A')

# FIX option 2: Only use known names
def display_grades():
    names = students.keys()  # Only names in dict
    for name in names:
        print(f'{name}: {get_grade(name)}')
```

## Exercises by Bloom Level

- **Remember**: What's the last line of a traceback?
- **Understand**: Which line caused the error? What's the error type?
- **Apply**: Use traceback to locate and understand bugs.
- **Analyze**: Trace through multiple functions to find root cause.
- **Create**: Fix broken programs using traceback information.

## Common Errors with Example Code

### Error 1: Ignoring the traceback
```python
# WRONG: Not reading traceback carefully
# Error appears, you panic and change random code

# CORRECT: Read traceback methodically
# 1. Find error type (last line)
# 2. Find error location (file and line)
# 3. Look at code on that line
# 4. Trace back through function calls
# 5. Identify root cause
```

### Error 2: Confusing the error location
```python
# WRONG: Thinking the error is where it was called
def add(a, b):
    return a + b  # Error happens here

result = add('5', 10)  # But traceback shows THIS line
# Actually: error on line 2 (a + b), not line 4!

# CORRECT: Look at the deepest (bottom-most) file/line in traceback
```

### Error 3: Not understanding function call stack
```python
# WRONG: Missing that errors can happen in nested calls
def validate(value):
    return int(value)  # Line 1 - error here

def process(data):
    return validate(data)  # Line 4

process('invalid')  # Line 7

# Traceback shows:
#   File "test.py", line 7, in <module>
#     process('invalid')
#   File "test.py", line 4, in process
#     return validate(data)
#   File "test.py", line 1, in validate
#     return int(value)
# ValueError: ...

# CORRECT: Trace from top to bottom, understand call chain
```

### Error 4: Misreading error type
```python
# WRONG: Confusing similar-sounding errors
# KeyError vs IndexError
# TypeError vs ValueError

# CORRECT: Read the exact error type, then check error message
# Example:
# KeyError: 'username'  → dict key issue
# IndexError: list index out of range  → list access issue
```

### Error 5: Not providing enough context in error messages
```python
# When reporting errors, include:
# 1. Full traceback (copy-paste it)
# 2. Python version
# 3. What you were trying to do
# 4. Inputs that caused the error

# BAD report: "It doesn't work"
# GOOD report: (full traceback + steps to reproduce)
```

## Tips for Reading Tracebacks

- **Start at the bottom** — Last line is the actual error.
- **Read the error type** — ValueError, KeyError, IndexError, etc. tell you what went wrong.
- **Find the file and line** — That's where the error happened.
- **Work backwards** — Trace the function calls above the error.
- **Look for your code** — Don't worry about Python internal errors in traceback.
- **Identify the root cause** — Often several lines up from where error occurred.
- **Use line numbers** — Open file and go to exact line number shown.

## Related Concepts
- [[Python - Debugging - Debugging Strategies]]
- [[Python - Debugging - Print Debugging]]
- [[Python - Debugging - Try-Except Basics]]
- [[Python - Debugging - Common Error Types]]

## MOC
- Parent: [[Python - Debugging (MOC)]]
