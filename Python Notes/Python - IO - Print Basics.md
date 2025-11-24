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

## Common Errors
- Confusing `print()` with string concatenation.
- Forgetting that `print()` always adds a newline at the end.

## Related Concepts
- [[Python - IO - Output Formatting]]
- [[Python - IO - Input Basics]]

## MOC
- Parent: [[Python - IO (MOC)]]
