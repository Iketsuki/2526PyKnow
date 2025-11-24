---
tags: [python, io, print]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: `print()` syntax and basic usage."
  - "Understand: how print sends text to the screen."
  - "Apply: print multiple values and understand separators."
---

# Python - IO - Print Basics

## Concept
`print()` is the fundamental way to display output. It takes one or more values, converts them to strings, and displays them.

## Syntax
```python
print(value1, value2, ..., sep=' ', end='\n')
```

## Example Code
```python
print('Hello, World!')
print('Name:', 'Alice')
print(1, 2, 3)
print('A', 'B', 'C', sep='-')
```

## Exercises by Bloom Level
- Remember: Write a simple print statement.
- Understand: What does `sep` do?
- Apply: Print your name, age, and city on one line separated by commas.
- Analyze: What's the difference between `print(1, 2)` and `print('1' + '2')`?
- Create: Write a function that prints a formatted greeting with multiple values.

## Common Errors with Example Code

1) Confusing `print()` with string concatenation (silent bugs)

WRONG
```python
print('Age: ' + 25)  # TypeError: can only concatenate str (not "int") to str
```

CORRECT
```python
print('Age:', 25)  # Separate with comma
# OR
print(f'Age: {25}')  # Use f-string
```

2) Not understanding the difference between `sep` and `+` (formatting)

WRONG
```python
print('A' + 'B' + 'C')  # 'ABC' (concatenated, no space)
```

CORRECT
```python
print('A', 'B', 'C')  # A B C (space-separated by default)
print('A', 'B', 'C', sep='-')  # A-B-C (custom separator)
```

3) Forgetting that `print()` adds newline by default (layout issues)

WRONG
```python
print('Loading', end='')
# Some code
print('Done')
# Prints on separate lines (forgot newline)
```

CORRECT
```python
print('Loading', end='')  # No newline
print('.', end='')  # Appends to same line
print('Done')  # Now on new line
```

Short tips:
- Use comma to separate values, not `+`.
- Use `sep=` to change the separator between values.
- Use `end=` to change the line ending (default is `\n`).

## Related Concepts
- [[Python - IO - Output Formatting]]
- [[Python - IO - Input Basics]]

## MOC
- Parent: [[Python - IO (MOC)]]
