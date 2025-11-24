---
tags: [python, lists, creation]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: list syntax `[]`."
  - "Understand: lists hold ordered items."
  - "Apply: create lists with various data types."
---

# Python - Lists - Creation & Initialization

## Concept
Lists are ordered, mutable collections created with square brackets `[]`. Items can be of any type and mix of types.

## Example Code
```python
numbers = [1, 2, 3, 4]
names = ['Alice', 'Bob', 'Charlie']
mixed = [1, 'two', 3.0, True]
empty = []
```

## Exercises by Bloom Level
- Remember: Create a list of 3 numbers.
- Understand: Why use a list instead of separate variables?
- Apply: Create a list of different types.
- Analyze: How many items does `[]` have?
- Create: Build a program that initializes lists for different data categories.

## Common Errors with Example Code

1) Using parentheses `()` instead of brackets `[]` (creates tuple)

WRONG
```python
items = (1, 2, 3)  # tuple, not list
items.append(4)  # AttributeError: 'tuple' object has no attribute 'append'
```

CORRECT
```python
items = [1, 2, 3]
items.append(4)
print(items)  # [1, 2, 3, 4]
```

2) Expecting list methods on immutable types (tuples)

WRONG
```python
t = (1, 2, 3)
t[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

CORRECT
```python
t = (1, 2, 3)
lst = list(t)  # convert to list
lst[0] = 10
print(lst)
```

3) Creating a list with a single value incorrectly

WRONG
```python
single = [None] * 3  # If mutable default, further pitfalls when used as default arg
```

CORRECT
```python
single = [None, None, None]
```

Short tips:
- Use `[]` to create lists, `()` for tuples.
- Convert tuples to lists if you need mutability: `list(t)`.
- Be explicit when creating multiple copies of mutable items (use list comprehensions for independent copies).

## Related Concepts
- [[Python - Lists - Indexing & Access]]

## MOC
- Parent: [[Python - Lists (MOC)]]
