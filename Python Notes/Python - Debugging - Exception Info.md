---
tags: [python, debugging, try-except, exceptions, error-info]
moc: [[Python - Debugging (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: `as` keyword for accessing exception object."
  - "Understand: exception attributes (message, type, traceback)."
  - "Apply: extract and use error information for debugging."
---

# Python - Debugging - Exception Info

## Concept
Use `as` keyword to capture exception object and access error message, type, and traceback for debugging.

## Accessing Exception with `as`

```python
try:
    age = int('not a number')
except ValueError as e:
    print(f'Error: {e}')
    # Output: Error: invalid literal for int() with base 10: 'not a number'
```

The `e` variable holds the exception object:

```python
try:
    student = {'name': 'Alice'}
    print(student['age'])
except KeyError as e:
    print(f'Missing key: {e}')  # Output: Missing key: 'age'
```

## Getting Exception Type

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f'Error type: {type(e).__name__}')  # Output: ZeroDivisionError
    print(f'Error message: {e}')  # Output: division by zero
```

Useful for logging or conditional handling:

```python
try:
    items = [1, 2, 3]
    print(items[10])
except Exception as e:
    error_type = type(e).__name__
    if error_type == 'IndexError':
        print('Index out of range')
    else:
        print(f'Unexpected error: {error_type}')
```

## Printing Full Traceback

`traceback` module shows complete error chain:

```python
import traceback

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f'Error: {e}')
    traceback.print_exc()  # Prints full stack trace
```

Output:
```
Error: division by zero
Traceback (most recent call last):
  File "script.py", line 3, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

Capture traceback as string:

```python
import traceback

try:
    x = int('invalid')
except ValueError as e:
    error_message = traceback.format_exc()
    print('Full error:')
    print(error_message)
    # Can save to log file, send to server, etc.
```

## Accessing Exception Attributes

```python
try:
    file = open('missing.txt', 'r')
except FileNotFoundError as e:
    print(f'Exception type: {type(e)}')
    print(f'Error args: {e.args}')
    print(f'Error message: {str(e)}')
```

Common exception attributes:

```python
try:
    age = int('not a number')
except ValueError as e:
    print(f'Type: {type(e).__name__}')  # ValueError
    print(f'Message: {str(e)}')  # Error message
    print(f'Args: {e.args}')  # Tuple of arguments
```

## Real-World: User Input Validation

```python
def get_positive_integer(prompt):
    '''Keep prompting until valid positive integer entered'''
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError('Must be positive')
            return value
        except ValueError as e:
            print(f'Invalid input: {e}')
            print('Please try again')
```

Usage:
```python
age = get_positive_integer('Enter age: ')
```

## Real-World: Safe Dictionary Access

```python
def get_value_safe(dictionary, key, default=None):
    '''Get value from dict with detailed error info'''
    try:
        return dictionary[key]
    except KeyError as e:
        print(f'Key {e} not found in dictionary')
        print(f'Available keys: {list(dictionary.keys())}')
        return default
    except TypeError as e:
        print(f'Dictionary error: {e}')
        return default

grades = {'Alice': 95, 'Bob': 87}
print(get_value_safe(grades, 'Charlie'))
# Output: Key 'Charlie' not found in dictionary
# Output: Available keys: ['Alice', 'Bob']
# Output: None
```

## Real-World: File Operations with Error Details

```python
def read_file_with_info(filename):
    '''Read file with detailed error reporting'''
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        print(f'File not found: {e}')
        return None
    except PermissionError as e:
        print(f'Permission denied: {e}')
        return None
    except Exception as e:
        print(f'Unexpected error ({type(e).__name__}): {e}')
        return None

content = read_file_with_info('data.txt')
```

## Real-World: Logging Errors

```python
import traceback
import datetime

def log_error(error_message):
    '''Log error to file with timestamp and traceback'''
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('error.log', 'a') as log_file:
        log_file.write(f'\n[{timestamp}] {error_message}\n')
        log_file.write(traceback.format_exc())

try:
    result = 10 / 0
except ZeroDivisionError as e:
    log_error(f'Math error: {e}')
    print('Error logged. Please contact support.')
```

## Common Errors with Example Code

1) Not using `as` — missing error information

WRONG
```python
try:
    age = int(input('Age: '))
except ValueError:
    print('Invalid input')  # No info about what was invalid
```

CORRECT
```python
try:
    age = int(input('Age: '))
except ValueError as e:
    print(f'Invalid input: {e}')  # Shows the actual error
```

2) Catching all exceptions without context

WRONG
```python
try:
    result = compute_something()
except Exception:
    print('Something went wrong')  # No clue what happened
```

CORRECT
```python
try:
    result = compute_something()
except Exception as e:
    print(f'Error ({type(e).__name__}): {e}')
    traceback.print_exc()  # Shows where it failed
```

3) Using string representation when you need exception object

WRONG
```python
try:
    items = [1, 2, 3]
    print(items[10])
except IndexError as error_string:  # 'as' binds object, not string
    # Error: object is Exception, not string
    print(error_string.upper())  # AttributeError
```

CORRECT
```python
try:
    items = [1, 2, 3]
    print(items[10])
except IndexError as e:
    print(f'Error: {e}')  # Properly convert to string
    print(type(e).__name__)  # Get type
```

## Tips
- Use **`as e`** to capture exception object
- **`str(e)` or `{e}`** for error message
- **`type(e).__name__`** for exception type
- **`traceback.print_exc()`** for full stack trace
- **`e.args`** for raw exception arguments
- Log errors with traceback for debugging

## Related Concepts
- [[Python - Debugging - Try-Except Syntax]]
- [[Python - Debugging - Finally Blocks]]
- [[Python - Debugging - Reading Tracebacks]]

## MOC
- Parent: [[Python - Debugging (MOC)]]
