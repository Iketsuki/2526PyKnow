---
tags: [python, debugging, try-except, exceptions, syntax]
moc: [[Python - Debugging (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: basic try-except-else-finally syntax."
  - "Understand: order and flow of exception handling blocks."
  - "Apply: catch specific exceptions without crashing."
---

# Python - Debugging - Try-Except Syntax

## Concept
Wrap risky code in `try` block; catch specific errors in `except` blocks without crashing. Controls program flow when errors occur.

## Basic Try-Except

```python
try:
    # Code that might raise an error
    age = int(input('Enter your age: '))
except ValueError:
    # Code that runs if ValueError occurs
    print('Please enter a valid number')
```

How it works:
1. Code in `try` block executes
2. If ValueError occurs, skip rest of try block, run `except` block
3. If no error, skip `except` block and continue

## Catching Specific Exceptions

Different errors need different handling:

```python
# ValueError: Converting string to number fails
try:
    age = int('not a number')
except ValueError:
    print('That is not a valid number')

# KeyError: Dictionary key doesn't exist
try:
    student = {'name': 'Alice'}
    print(student['age'])  # KeyError
except KeyError:
    print('Key not found in dictionary')

# IndexError: List index out of range
try:
    items = [1, 2, 3]
    print(items[10])  # IndexError
except IndexError:
    print('Index out of range')

# ZeroDivisionError: Divide by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
```

## Catching Multiple Exceptions

### Method 1: Separate except blocks

```python
try:
    x = int(input('Number: '))
    result = 10 / x
except ValueError:
    print('Invalid number')
except ZeroDivisionError:
    print('Cannot divide by zero')
```

### Method 2: Single except with tuple

```python
try:
    x = int(input('Number: '))
    result = 10 / x
except (ValueError, ZeroDivisionError):
    print('Invalid number or division by zero')
```

### Method 3: Catch all exceptions (NOT recommended)

```python
# Avoid this! Catches everything including program bugs
try:
    x = int(input('Number: '))
    result = 10 / x
except:
    print('An error occurred')
```

**Problem with bare `except`:** Catches KeyboardInterrupt, SystemExit, and bugs you didn't know about. Hard to debug.

## Try-Except-Else

`else` block runs **only if no exception occurs**:

```python
try:
    age = int(input('Age: '))
except ValueError:
    print('Invalid number')
else:
    # Only runs if no ValueError
    if age >= 18:
        print('You are an adult')
    else:
        print('You are a minor')
```

Use `else` to separate "error handling" from "success path":

```python
try:
    number = int(input('Enter number: '))
except ValueError:
    print('Invalid number')
else:
    result = 100 / number  # Only if int() succeeded
    print(f'Result: {result}')
```

## Try-Except-Finally

`finally` block runs **no matter what** (error or no error):

```python
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('File not found')
finally:
    file.close()  # Runs always
    print('Cleanup complete')
```

When to use `finally`:
- Closing files/connections
- Releasing resources
- Cleanup tasks that must happen

**Better approach:** Use `with` statement (handles cleanup automatically):

```python
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found')
# File closes automatically, no finally needed
```

## All Together: Try-Except-Else-Finally

```python
try:
    number = int(input('Enter number: '))
    result = 100 / number
except ValueError:
    print('Invalid number')
except ZeroDivisionError:
    print('Cannot divide by zero')
else:
    print(f'Result: {result}')  # Only if no exception
finally:
    print('Calculation complete')  # Always runs
```

Execution flow:
1. If ValueError → "Invalid number", then "Calculation complete"
2. If ZeroDivisionError → "Cannot divide by zero", then "Calculation complete"
3. If success → "Result: X", then "Calculation complete"

## Common Exceptions Reference

| Exception | When | Example |
|-----------|------|---------|
| `ValueError` | Wrong value type | `int('abc')` |
| `KeyError` | Dict key missing | `d['missing']` |
| `IndexError` | List index too high | `lst[100]` |
| `ZeroDivisionError` | Divide by zero | `10 / 0` |
| `FileNotFoundError` | File doesn't exist | `open('missing.txt')` |
| `AttributeError` | No attribute | `str.unknown()` |
| `TypeError` | Wrong type | `'5' + 5` |
| `NameError` | Variable undefined | `print(x)` if x not defined |

## Common Errors with Example Code

1) Catching too broad — bare `except` hides bugs

WRONG
```python
try:
    x = int(input('Number: '))
    result = 10 / x
except:  # Too broad, catches everything!
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

2) Not handling exception in except block (silent failure)

WRONG
```python
try:
    age = int(input('Age: '))
except ValueError:
    pass  # Program continues, age is undefined
    
print(f'Age: {age}')  # NameError or wrong value
```

CORRECT
```python
try:
    age = int(input('Age: '))
except ValueError:
    print('Invalid input, try again')
    age = 0  # Set default or re-prompt
    
print(f'Age: {age}')
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
# Check before accessing
if my_list:
    result = my_list[0]
else:
    result = None
```

## Tips
- **Catch specific exceptions** — not bare `except`
- **Use `else`** for code that depends on success
- **Use `finally`** for cleanup (prefer `with` for files)
- **Check first** if you can prevent an error
- Order matters: `try → except → else → finally`

## Related Concepts
- [[Python - Debugging - Exception Info]]
- [[Python - Debugging - Finally Blocks]]
- [[Python - Debugging - Reading Tracebacks]]
- [[Python - File IO - Context Managers]]

## MOC
- Parent: [[Python - Debugging (MOC)]]
