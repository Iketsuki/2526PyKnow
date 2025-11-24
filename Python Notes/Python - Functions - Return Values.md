---
tags: [python, functions, return]
moc: [[Python - Functions (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `return` syntax."
  - "Understand: functions send back values."
  - "Apply: use return values in code."
---

# Python - Functions - Return Values

## Concept
Use `return` to send a value back from a function. Functions without explicit returns return `None`.

## Example Code
```python
def square(x):
    return x * x

result = square(5)
print(result)           # 25
```

## Exercises by Bloom Level
- Remember: Write a function that returns a value.
- Understand: What happens if you don't return?
- Apply: Build a function that returns a computed value.
- Analyze: Compare functions with/without returns.
- Create: Chain function calls together.

## Common Errors with Example Code

1) Using `print()` instead of `return` (no return value)

WRONG
```python
def square(x):
    print(x * x)  # Prints, but returns None

result = square(5)
print(result)  # None (not 25!)
print(result + 1)  # TypeError: unsupported operand type(s)
```

CORRECT
```python
def square(x):
    return x * x  # Return the value

result = square(5)
print(result)  # 25
print(result + 1)  # 26
```

2) Forgetting `return` statement (function returns None)

WRONG
```python
def add(a, b):
    total = a + b
    # Forgot return!

result = add(3, 5)
print(result)  # None
```

CORRECT
```python
def add(a, b):
    total = a + b
    return total  # Explicitly return

result = add(3, 5)
print(result)  # 8
```

3) Code after `return` never executes (unreachable code)

WRONG
```python
def divide(a, b):
    return a / b
    print('Done')  # Never runs!
```

CORRECT
```python
def divide(a, b):
    if b == 0:
        return None
    return a / b
    # Code before return still runs
```

Short tips:
- Use `return` to send a value back from a function.
- Don't confuse `print()` with `return`.
- Code after `return` is unreachable.
- Functions without explicit `return` return `None`.

## Related Concepts
- [[Python - Functions - Definition Basics]]

## MOC
- Parent: [[Python - Functions (MOC)]]
