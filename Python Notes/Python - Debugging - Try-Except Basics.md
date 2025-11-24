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

## Concept
Wrap risky code in `try` block; catch errors in `except` without crashing. Allows graceful error handling.

## Basic Syntax

```python
try:
    # Code that might raise an error
    age = int(input('Enter your age: '))
except ValueError:
    # Code that runs if error occurs
    print('Please enter a valid number')
```

## Catching Specific Exceptions

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

# FileNotFoundError: File doesn't exist
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found')

# AttributeError: Object doesn't have attribute
try:
    text = 'hello'
    text.unknown_method()
except AttributeError:
    print('Method does not exist')
```

## Catching Multiple Exceptions

```python
# Method 1: Separate except blocks
try:
    x = int(input('Number: '))
    result = 10 / x
except ValueError:
    print('Invalid number')
except ZeroDivisionError:
    print('Cannot divide by zero')

# Method 2: Single except with tuple
try:
    x = int(input('Number: '))
    result = 10 / x
except (ValueError, ZeroDivisionError):
    print('Invalid number or division by zero')

# Method 3: Catch all exceptions (not recommended)
try:
    x = int(input('Number: '))
    result = 10 / x
except:
    print('An error occurred')
```

## Accessing Exception Information

```python
# Access error message with 'as'
try:
    age = int('not a number')
except ValueError as e:
    print(f'Error: {e}')  # Error: invalid literal for int() with base 10: 'not a number'

# Full exception details
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f'Error type: {type(e).__name__}')
    print(f'Error message: {e}')
    import traceback
    traceback.print_exc()  # Full traceback
```

## Try-Except-Else-Finally

```python
# else: runs if no exception
try:
    age = int(input('Age: '))
except ValueError:
    print('Invalid number')
else:
    if age >= 18:
        print('You are an adult')
    else:
        print('You are a minor')

# finally: runs no matter what
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('File not found')
finally:
    file.close()  # Runs always, but use 'with' instead!

# All together
try:
    number = int(input('Enter number: '))
    result = 100 / number
except ValueError:
    print('Invalid number')
except ZeroDivisionError:
    print('Cannot divide by zero')
else:
    print(f'Result: {result}')
finally:
    print('Calculation complete')
```

## Real Examples

```python
# Example 1: Safe user input
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Please enter a valid integer')

age = get_integer('Age: ')

# Example 2: Safe dictionary access
def get_student_grade(grades, name):
    try:
        return grades[name]
    except KeyError:
        return 'Not found'

student_grades = {'Alice': 90, 'Bob': 85}
print(get_student_grade(student_grades, 'Charlie'))  # Not found

# Example 3: Safe file reading
def read_file_safe(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f'File {filename} not found')
        return None

content = read_file_safe('data.txt')

# Example 4: Data conversion with fallback
def parse_number(text):
    try:
        return float(text)
    except ValueError:
        try:
            return int(text)
        except ValueError:
            return 0  # Default value

print(parse_number('3.14'))  # 3.14
print(parse_number('42'))  # 42
print(parse_number('invalid'))  # 0

# Example 5: Safe list access
def get_item(items, index):
    try:
        return items[index]
    except IndexError:
        return None

numbers = [10, 20, 30]
print(get_item(numbers, 1))  # 20
print(get_item(numbers, 10))  # None
```

## Common Exception Types

| Exception | When It Occurs | Example |
|-----------|--------|---------|
| `ValueError` | Inappropriate value type | `int('abc')` |
| `TypeError` | Wrong type for operation | `'5' + 5` |
| `KeyError` | Dict key doesn't exist | `d['missing']` |
| `IndexError` | List index out of range | `lst[100]` |
| `FileNotFoundError` | File doesn't exist | `open('missing.txt')` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `AttributeError` | Attribute doesn't exist | `str.unknown_method()` |
| `NameError` | Variable not defined | `print(undefined_var)` |

## Exercises by Bloom Level

- **Remember**: Write a `try-except` statement.
- **Understand**: What happens if exception isn't caught?
- **Apply**: Catch specific errors and recover gracefully.
- **Analyze**: When use try-except vs fix root cause?
- **Create**: Build robust input validation and error handling.

## Common Errors with Example Code

### Error 1: Catching too broad (catching all exceptions)
```python
# WRONG: Catches everything, hides real bugs
try:
    x = int(input('Number: '))
    result = 10 / x
except:  # Too broad!
    print('Something went wrong')

# CORRECT: Catch specific exceptions
try:
    x = int(input('Number: '))
    result = 10 / x
except ValueError:
    print('Invalid number')
except ZeroDivisionError:
    print('Cannot divide by zero')
```

### Error 2: Not using the exception object
```python
# WRONG: Ignoring useful error information
try:
    age = int(input('Age: '))
except ValueError:
    print('Error')  # Not helpful to user

# CORRECT: Use exception information
try:
    age = int(input('Age: '))
except ValueError as e:
    print(f'Error: {e}')  # Shows specific problem
```

### Error 3: Using try-except when you should fix the bug
```python
# WRONG: Hiding the real problem
try:
    result = my_list[0]
except IndexError:
    result = None

# BETTER: Check if list is empty
if my_list:
    result = my_list[0]
else:
    result = None

# EVEN BETTER: Use default with .get() or similar
result = next(iter(my_list), None)
```

### Error 4: Forgetting to handle exception in except block
```python
# WRONG: Not recovering from error
try:
    age = int(input('Age: '))
except ValueError:
    pass  # Program continues with error, no recovery

# CORRECT: Handle the error or re-prompt
try:
    age = int(input('Age: '))
except ValueError:
    print('Invalid input, please try again')
    age = 0  # Or use default, or loop
```

### Error 5: Not using else or finally when appropriate
```python
# WRONG: Repeating logic
try:
    x = int(input('Number: '))
except ValueError:
    print('Invalid')
    if False:
        print('Dividing by', x)  # Awkward

# CORRECT: Use else for success path
try:
    x = int(input('Number: '))
except ValueError:
    print('Invalid')
else:
    print('Dividing by', x)  # Runs only if no error
```

## Tips
- **Always catch specific exceptions** (ValueError, KeyError, etc.).
- **Never use bare `except`** — it catches everything including bugs.
- Use **`as e`** to get error message: `except ValueError as e: print(e)`.
- Use **`else`** for code that runs only if no exception.
- Use **`finally`** for cleanup (but prefer `with` for files).
- **Try-except is for handling errors**, not for control flow.
- **Don't catch errors you can prevent** — check first if possible.

## Related Concepts
- [[Python - Debugging - Exception Handling]]
- [[Python - Debugging - Debugging Strategies]]
- [[Python - Error Handling - Reading Tracebacks]]
- [[Python - File IO - Context Managers]]

## MOC
- Parent: [[Python - Debugging (MOC)]]


[Python - Debugging - Exception Handling]: <Python - Debugging - Exception Handling.md> "Python - Debugging - Exception Handling (Try-Except)"
[Python - Debugging - Debugging Strategies]: <Python - Debugging - Debugging Strategies.md> "Python - Debugging - Debugging Strategies"
[Python - File IO - Context Managers]: <Python - File IO - Context Managers.md> "Python - File IO - Context Managers"
[Python - Debugging (MOC)]: <../MOCs/Python - Debugging (MOC).md> "Python - Debugging (MOC)"
