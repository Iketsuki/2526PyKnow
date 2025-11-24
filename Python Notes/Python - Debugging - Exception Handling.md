---
tags: [python, debugging, exceptions]
moc: [[Python - Debugging (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: try-except syntax."
  - "Understand: how exceptions work."
  - "Apply: handle errors safely."
---

# Python - Debugging - Exception Handling (Try-Except)

## Concept
**Try-except** — catch errors gracefully instead of crashing. `try` block has code that might fail. `except` block runs if error occurs.

## Basic Try-Except

```python
# Without error handling (crashes)
age_str = '15'
age = int(age_str)  # Works
print(age)

age_str = 'fifteen'
age = int(age_str)  # Crashes! ValueError

# With error handling (safe)
try:
    age = int(age_str)
    print(age)
except ValueError:
    print('Please enter a number')
```

## Multiple Exception Types

```python
try:
    numbers = [1, 2, 3]
    result = int(input('Index: '))
    value = numbers[result]
    final = 10 / value
    print(final)
except ValueError:
    print('Please enter a valid number')
except IndexError:
    print('Index out of range')
except ZeroDivisionError:
    print('Cannot divide by zero')
```

## Generic Exception Handling

```python
try:
    # Risky code
    result = risky_function()
except Exception as e:
    # Catches most exceptions
    print(f'Error occurred: {e}')
```

## Else and Finally

```python
try:
    age = int(input('Age: '))
except ValueError:
    print('Invalid input')
else:
    # Runs only if no exception
    if age >= 18:
        print('You are an adult')
    else:
        print('You are a minor')
finally:
    # Runs regardless (cleanup)
    print('Thank you for using this program')
```

## Real-World: Safe File Reading

```python
try:
    with open('scores.txt', 'r') as f:
        scores = f.read()
    print(scores)
except FileNotFoundError:
    print('File not found. Creating new one...')
except IOError:
    print('Error reading file')
```

## Real-World: Input Validation

```python
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Please enter a valid number')

age = get_valid_int('Enter age: ')
print(f'Age: {age}')
```

## Real-World: Calculate Grade

```python
def calculate_grade(scores):
    try:
        if not scores:
            raise ValueError('Scores list cannot be empty')
        
        average = sum(scores) / len(scores)
        
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        else:
            return 'C'
    
    except TypeError:
        print('Scores must be numbers')
        return None
    except ZeroDivisionError:
        print('Cannot calculate with empty list')
        return None

print(calculate_grade([85, 90, 88]))  # B
print(calculate_grade([]))  # ValueError caught
print(calculate_grade(['a', 'b']))  # TypeError caught
```

## Raising Custom Exceptions

```python
def set_age(age):
    try:
        if age < 0:
            raise ValueError('Age cannot be negative')
        if age > 150:
            raise ValueError('Age seems unrealistic')
        return age
    except ValueError as e:
        print(f'Invalid age: {e}')
        return None

print(set_age(15))  # 15
print(set_age(-5))  # Error message
print(set_age(200))  # Error message
```

## Common Exceptions

```python
# ValueError - wrong type
int('hello')  # ValueError

# IndexError - list index out of range
items = [1, 2, 3]
items[10]  # IndexError

# KeyError - dict key not found
data = {'name': 'Alice'}
data['age']  # KeyError

# ZeroDivisionError - divide by zero
10 / 0  # ZeroDivisionError

# FileNotFoundError - file doesn't exist
open('nonexistent.txt')  # FileNotFoundError

# AttributeError - object has no attribute
text = 'hello'
text.invalid_method()  # AttributeError

# TypeError - wrong type for operation
'hello' + 5  # TypeError
```

## Traceback Information

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    import traceback
    
    print(f'Error: {e}')
    traceback.print_exc()
```

## Best Practices

```python
# GOOD: Specific exceptions
try:
    age = int(input('Age: '))
except ValueError:
    print('Please enter a number')

# BAD: Too generic
try:
    age = int(input('Age: '))
except:  # Catches everything!
    print('Error')

# BETTER: Multiple specific exceptions
try:
    age = int(input('Age: '))
except (ValueError, EOFError):
    print('Please enter a valid input')
```

## Exercises by Bloom Level
- Remember: What does `try-except` do?
- Understand: Why catch ValueError for int()?
- Apply: Add try-except to input validation.
- Analyze: Compare generic vs specific exceptions.
- Create: Build robust input function with error handling.

## Common Errors
- Catching Exception too broadly (use specific exceptions).
- Forgetting `except:` clause (indentation errors).
- Raising exception without message.

## Related Concepts
- [[Python - Debugging - Common Error Types]]
- [[Python - Debugging - Reading Tracebacks]]
- [[Python - IO - Error Handling in Input-Output]]

## MOC
- Parent: [[Python - Debugging (MOC)]]


[Python - Debugging - Common Error Types]: <Python - Debugging - Common Error Types.md> "Python - Debugging - Common Error Types"
[Python - Debugging - Reading Tracebacks]: <Python - Debugging - Reading Tracebacks.md> "Python - Debugging - Reading Tracebacks"
[Python - IO - Error Handling in Input-Output]: <Python - IO - Error Handling in Input-Output.md> "Python - IO - Error Handling in Input/Output"
[Python - Debugging (MOC)]: <../MOCs/Python - Debugging (MOC).md> "Python - Debugging (MOC)"
