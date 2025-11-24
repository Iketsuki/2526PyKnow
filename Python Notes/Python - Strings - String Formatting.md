---
tags: [python, strings, formatting]
moc: [[Python - Strings (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: f-string syntax."
  - "Understand: when to use formatting."
  - "Apply: format strings with variables."
---

# Python - Strings - String Formatting

## Concept
Use f-strings for clean formatting: `f'text {variable}'` or older `'text {}'.format(var)`.

## Example Code
```python
name = 'Alice'
age = 15
print(f'{name} is {age} years old.')
print('{} is {} years old.'.format(name, age))
```

## Exercises by Bloom Level
- Remember: Write an f-string.
- Understand: Why use f-strings?
- Apply: Format multiple variables.
- Analyze: F-strings vs concatenation.
- Create: Build formatted output for data.

## Common Errors with Example Code

1) Forgetting the `f` prefix (no interpolation)

WRONG
```python
name = 'Alice'
print('Hello {name}')  # prints the literal {name}, not the value
```

CORRECT
```python
name = 'Alice'
print(f'Hello {name}')  # Hello Alice
```

2) Wrong format specifier for numbers

WRONG
```python
price = 3.14159
print(f'Price: {price:.2}')  # incorrect specifier, may raise ValueError
```

CORRECT
```python
price = 3.14159
print(f'Price: {price:.2f}')  # Price: 3.14
```

3) Nested quotes inside f-strings

WRONG
```python
name = "O'Connor"
print(f"Hello {name's}")  # SyntaxError or confusing quoting
```

CORRECT
```python
name = "O'Connor"
print(f"Hello {name}'s")   # Use correct quoting or escape
print(f'Hello {name}\'s')  # or escape the quote
```

## Related Concepts
- [[Python - Strings - Basics]]

## MOC
- Parent: [[Python - Strings (MOC)]]
