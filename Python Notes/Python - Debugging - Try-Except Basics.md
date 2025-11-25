---
tags: [python, debugging, try-except, exceptions, error-handling]
moc: [[Python - Debugging (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `try-except` syntax."
  - "Understand: catching specific vs all exceptions."
  - "Apply: handle errors gracefully without crashing."
  - "Analyze: when to use try-except vs fix root cause."
  - "Create: robust input validation and error recovery."
---

# Python - Debugging - Try-Except Basics

## Overview
This page is a parent index for exception handling. Exception handling allows your program to continue running even when errors occur, by catching specific errors and responding gracefully.

For detailed atomic notes on specific exception handling topics, see the links below:

1. **[[Python - Debugging - Try-Except Syntax]]** — Basic try-except structure, catching specific exceptions, multiple except blocks, else clause
2. **[[Python - Debugging - Exception Info]]** — Using `as` to access error message, exception type, traceback, logging errors
3. **[[Python - Debugging - Finally Blocks]]** — Finally block for cleanup, context managers with `with`, resource management

## Quick Reference

```python
# Basic try-except
try:
    age = int(input('Age: '))
except ValueError:
    print('Invalid number')

# Multiple except blocks
try:
    x = int(input('Number: '))
    result = 10 / x
except ValueError:
    print('Invalid number')
except ZeroDivisionError:
    print('Cannot divide by zero')

# Capture exception info
try:
    age = int(input('Age: '))
except ValueError as e:
    print(f'Error: {e}')

# Finally for cleanup
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('File not found')
finally:
    file.close()

# Prefer 'with' for files
with open('data.txt', 'r') as file:
    content = file.read()
```

## Common Exception Types

| Exception | When | Example |
|-----------|------|---------|
| `ValueError` | Wrong value | `int('abc')` |
| `TypeError` | Wrong type | `'5' + 5` |
| `KeyError` | Missing dict key | `d['missing']` |
| `IndexError` | List index too high | `lst[100]` |
| `FileNotFoundError` | File missing | `open('missing.txt')` |
| `ZeroDivisionError` | Divide by zero | `10 / 0` |
| `AttributeError` | No attribute | `str.unknown()` |

## Real-World: Safe Input

```python
def get_integer(prompt):
    '''Keep prompting until valid integer entered'''
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Please enter a valid integer')

age = get_integer('Age: ')
```

## Real-World: Safe File Reading

```python
def read_file_safe(filename):
    '''Read file with error handling'''
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f'File {filename} not found')
        return None
    except PermissionError:
        print(f'No permission to read {filename}')
        return None

content = read_file_safe('data.txt')
```

## Real-World: Safe Dictionary Access

```python
def get_student_grade(grades, name):
    '''Get grade with fallback'''
    try:
        return grades[name]
    except KeyError:
        print(f'{name} not found')
        return None

grades = {'Alice': 90, 'Bob': 85}
grade = get_student_grade(grades, 'Charlie')  # None
```

## Common Errors with Example Code

1) Catching too broad — bare `except` hides bugs

WRONG
```python
try:
    x = int(input('Number: '))
    result = 10 / x
except:  # Catches everything!
    print('Something went wrong')
```

CORRECT
```python
try:
    x = int(input('Number: '))
    result = 10 / x
except ValueError:
    print('Invalid number')
except ZeroDivisionError:
    print('Cannot divide by zero')
```

2) Not using exception information

WRONG
```python
try:
    age = int(input('Age: '))
except ValueError:
    print('Error')  # Not helpful
```

CORRECT
```python
try:
    age = int(input('Age: '))
except ValueError as e:
    print(f'Error: {e}')  # Shows what went wrong
```

3) Using try-except when you should check first

WRONG
```python
try:
    result = my_list[0]
except IndexError:
    result = None
```

CORRECT
```python
if my_list:
    result = my_list[0]
else:
    result = None
```

## Atomic Exception Handling Notes

For in-depth coverage of specific exception handling concepts:

- **[[Python - Debugging - Try-Except Syntax]]** — try, except, else, finally keywords and flow
- **[[Python - Debugging - Exception Info]]** — accessing error messages, types, tracebacks
- **[[Python - Debugging - Finally Blocks]]** — cleanup patterns, resource management, context managers
- **[[Python - Debugging - Reading Tracebacks]]** — understanding error stack traces
- **[[Python - Debugging - Exception Handling]]** — advanced patterns

## Related Concepts
- [[Python - Debugging - Debugging Strategies]]
- [[Python - File IO - Context Managers]]
- [[Python - Debugging - Common Error Types]]

## MOC
- Parent: [[Python - Debugging (MOC)]]


[Python - Debugging - Exception Handling]: <Python - Debugging - Exception Handling.md> "Python - Debugging - Exception Handling (Try-Except)"
[Python - Debugging - Debugging Strategies]: <Python - Debugging - Debugging Strategies.md> "Python - Debugging - Debugging Strategies"
[Python - File IO - Context Managers]: <Python - File IO - Context Managers.md> "Python - File IO - Context Managers"
[Python - Debugging (MOC)]: <../MOCs/Python - Debugging (MOC).md> "Python - Debugging (MOC)"
