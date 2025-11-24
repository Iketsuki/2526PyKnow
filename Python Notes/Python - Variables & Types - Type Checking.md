---
tags: [python, variables, types, checking]
moc: [[Python - Variables & Types (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: type() function."
  - "Understand: what type a value is."
  - "Apply: check types before operations."
---

# Python - Variables & Types - Type Checking

## Concept
**type()** returns the data type of a value. Use to check what kind of value you have before using it.

## Basic Type Checking

```python
x = 5
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>

name = 'Alice'
print(type(name))  # <class 'str'>

items = [1, 2, 3]
print(type(items))  # <class 'list'>

data = {'name': 'Bob'}
print(type(data))  # <class 'dict'>

is_ready = True
print(type(is_ready))  # <class 'bool'>
```

## Checking Before Operations

```python
# Safe division (check if divisor is number)
divisor = input('Enter divisor: ')

if type(divisor) == str:
    divisor = int(divisor)

if divisor != 0:
    result = 100 / divisor
    print(result)
else:
    print('Cannot divide by zero')
```

## Using isinstance() (Better Method)

```python
# isinstance() is cleaner for checking
age = 15

if isinstance(age, int):
    print('Age is a number')

if isinstance(age, (int, float)):  # Check multiple types
    print('Age is int or float')
```

## Real-World: Process User Input

```python
user_input = input('Enter a number: ')

if type(user_input) == str:
    try:
        number = int(user_input)
        print(f'Number is: {number}')
    except ValueError:
        print('Not a valid number')
```

## Real-World: List of Mixed Types

```python
data = [5, 'hello', 3.14, True, [1, 2]]

for item in data:
    print(f'{item} is {type(item).__name__}')
# Output:
# 5 is int
# hello is str
# 3.14 is float
# True is bool
# [1, 2] is list
```

## Type Name Shortcuts

```python
x = 5
print(type(x))  # <class 'int'>
print(type(x).__name__)  # 'int' (cleaner)

y = [1, 2]
print(type(y).__name__)  # 'list'
```

## Exercises by Bloom Level
- Remember: What does `type(5)` return?
- Understand: Why check type before operation?
- Apply: Use `isinstance()` to validate input.
- Analyze: Compare `type()` vs `isinstance()`.
- Create: Build input validator that checks types.

## Common Errors
- Confusing `type()` with `type(x) = int` (can't assign type).
- Forgetting that `type()` returns class, not string.
- `isinstance()` preferred over `type() ==` for flexibility.

## Related Concepts
- [[Python - Variables - Types Basics]]
- [[Python - IO - Input Types (Strings vs Numbers vs Lists)]]
- [[Python - Conditionals - Truthiness]]
- [[Python - Debugging - Common Error Types]]

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
