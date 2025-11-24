---
tags: [python, variables, types, conversion]
moc: [[Python - Variables & Types (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: conversion functions (int(), str(), float())."
  - "Understand: why conversion is needed."
  - "Apply: convert between types safely."
---

# Python - Variables & Types - Type Conversion

## Concept
**Type conversion** — change one data type to another. Functions: `int()`, `str()`, `float()`, `bool()`, `list()`, etc.

## Converting to Int

```python
# From string
num_str = '42'
num = int(num_str)
print(num)  # 42

# From float (truncates decimal)
decimal = 3.9
whole = int(decimal)
print(whole)  # 3 (not rounded, truncated)

# From boolean
true_val = True
as_int = int(true_val)
print(as_int)  # 1

false_val = False
as_int = int(false_val)
print(as_int)  # 0
```

## Converting to String

```python
# From int
age = 15
message = 'Age: ' + str(age)
print(message)  # Age: 15

# From float
score = 87.5
text = f'Score: {str(score)}'
print(text)  # Score: 87.5

# From boolean
is_ready = True
status = str(is_ready)
print(status)  # 'True'

# From list
items = [1, 2, 3]
as_str = str(items)
print(as_str)  # '[1, 2, 3]'
```

## Converting to Float

```python
# From string
price_str = '19.99'
price = float(price_str)
print(price)  # 19.99

# From int
count = 5
as_float = float(count)
print(as_float)  # 5.0

# From bool
is_active = True
as_float = float(is_active)
print(as_float)  # 1.0
```

## Converting to Boolean

```python
# Any value converts to bool
print(bool(1))  # True
print(bool(0))  # False
print(bool(''))  # False (empty string)
print(bool('hello'))  # True (non-empty string)
print(bool([]))  # False (empty list)
print(bool([1, 2]))  # True (non-empty list)
```

## Real-World: User Input (String → Numbers)

```python
# Input always returns string
age_str = input('Age: ')
age = int(age_str)  # Convert to int

if age >= 13:
    print('Can use social media')
```

## Real-World: Mixed Calculations

```python
# Combine different types
quantity = 5  # int
price = 12.50  # float
discount = 0.10  # float

total = quantity * price * (1 - discount)
print(f'Total: ${total:.2f}')  # Format as currency

# Or convert to string for display
total_str = str(total)
print('Total: $' + total_str)
```

## Real-World: Build Strings from Numbers

```python
scores = [85, 90, 78]

# Convert each score to string and join
message = 'Your scores: ' + ', '.join(str(s) for s in scores)
print(message)  # Your scores: 85, 90, 78
```

## Chaining Conversions

```python
# Convert multiple times
value = '3.14'
print(float(value))  # 3.14
print(int(float(value)))  # 3 (float → int)
print(str(int(float(value))))  # '3' (back to string)
```

## Error Cases

```python
# Invalid conversions raise errors
try:
    num = int('hello')  # ValueError!
except ValueError:
    print('Cannot convert "hello" to int')

try:
    num = float('not a number')  # ValueError!
except ValueError:
    print('Cannot convert to float')
```

## Safe Conversion

```python
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int('42'))  # 42
print(safe_int('hello'))  # 0 (default)
print(safe_int(None))  # 0
```

## Conversion with Default

```python
# Use or with defaults
age_str = input('Age: ')
age = int(age_str) if age_str else 0
print(age)
```

## Exercises by Bloom Level
- Remember: What does `int('5')` return?
- Understand: Why is input() always a string?
- Apply: Convert user input to number for calculation.
- Analyze: Compare `int()` vs `float()` conversions.
- Create: Build calculator with input conversion & error handling.

## Common Errors with Example Code

1) Using `int()` on a float-string like '3.14' (ValueError)

WRONG
```python
num = int('3.14')  # ValueError: invalid literal for int() with base 10
```

CORRECT
```python
num = float('3.14')  # 3.14
num_int = int(num)   # 3 (explicit conversion from float)
```

2) Not handling invalid input when converting

WRONG
```python
val = input('Enter number: ')
num = int(val)  # crashes if user types 'abc'
```

CORRECT
```python
val = input('Enter number: ')
try:
    num = int(val)
except ValueError:
    print('Please enter a valid integer')
    num = 0
```

3) Assuming conversions change values in-place or behave like casting in other languages

WRONG
```python
price = '9.99'
price.int()  # AttributeError: 'str' object has no attribute 'int'
```

CORRECT
```python
price = '9.99'
price = float(price)  # assign converted value back to variable
```

## Related Concepts
- [[Python - Variables & Types - Type Checking]]
- [[Python - IO - Input Types (Strings vs Numbers vs Lists)]]
- [[Python - Debugging - Common Error Types]]
- [[Python - Conditionals - Truthiness]]

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
