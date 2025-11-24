---
tags: [python, lists, comprehension]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: list comprehension syntax."
  - "Understand: how comprehensions work."
  - "Apply: use comprehensions to build lists."
---

# Python - Lists - List Comprehension

## Concept
**List comprehension** — compact way to create lists from loops/conditions. Syntax: `[expression for item in iterable]`

## Basic Comprehension

```python
# Traditional way
squares = []
for x in range(5):
    squares.append(x ** 2)

print(squares)  # [0, 1, 4, 9, 16]

# Comprehension way (one line)
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

## With Condition (Filter)

```python
# Traditional way
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

print(evens)  # [0, 2, 4, 6, 8]

# Comprehension way
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

## Transformation + Filter

```python
# Get squares of even numbers
result = [x ** 2 for x in range(10) if x % 2 == 0]
print(result)  # [0, 4, 16, 36, 64]

# Get uppercased names longer than 3 chars
names = ['Alice', 'Bob', 'Charlie', 'Amy', 'David']
filtered = [name.upper() for name in names if len(name) > 3]
print(filtered)  # ['ALICE', 'CHARLIE', 'DAVID']
```

## From String

```python
# Get each character
chars = [c for c in 'Python']
print(chars)  # ['P', 'y', 't', 'h', 'o', 'n']

# Get lowercase
lower_chars = [c.lower() for c in 'HELLO']
print(lower_chars)  # ['h', 'e', 'l', 'l', 'o']
```

## From Another List

```python
# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)  # [2, 4, 6, 8, 10]

# Convert to strings
ids = [1, 2, 3]
str_ids = [str(id) for id in ids]
print(str_ids)  # ['1', '2', '3']
```

## Real-World: Processing Data

```python
# Extract ages from tuples
students = [('Alice', 15), ('Bob', 14), ('Charlie', 15)]

ages = [age for name, age in students]
print(ages)  # [15, 14, 15]

# Get names of 15-year-olds
names_15 = [name for name, age in students if age == 15]
print(names_15)  # ['Alice', 'Charlie']
```

## Real-World: Clean Data

```python
# Remove empty strings
data = ['apple', '', 'banana', '', 'cherry']
cleaned = [item for item in data if item]
print(cleaned)  # ['apple', 'banana', 'cherry']

# Remove duplicates while preserving order
items = [1, 2, 2, 3, 1, 4]
unique = []
unique_comp = [x for x in items if not (x in unique or unique.append(x))]
# Better approach:
unique = list(dict.fromkeys(items))
print(unique)  # [1, 2, 3, 4]
```

## Nested Comprehension (2D)

```python
# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create 2D grid
grid = [[x * y for x in range(1, 4)] for y in range(1, 4)]
print(grid)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

## Comprehension vs Loop

```python
# Loop: multi-line, mutable state
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

# Comprehension: one-line, declarative
evens = [x for x in range(10) if x % 2 == 0]

# Both equivalent, comprehension usually more Pythonic
```

## When NOT to Use Comprehension

```python
# DON'T: Too complex
# bad = [complex_calculation(x) for x in items if condition(x) and other(x)]

# DO: Use loop for readability
result = []
for item in items:
    if condition(item) and other(item):
        result.append(complex_calculation(item))
```

## Dict Comprehension (Similar)

```python
# Create dict from list
numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x**2 for x in numbers}
print(squared_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16}
```

## Set Comprehension (Similar)

```python
# Create set from list (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3]
unique_set = {x for x in numbers}
print(unique_set)  # {1, 2, 3}

# With transformation
squares = {x**2 for x in range(5)}
print(squares)  # {0, 1, 4, 9, 16}
```

## Exercises by Bloom Level
- Remember: What's list comprehension syntax?
- Understand: How is it equivalent to loop?
- Apply: Use comprehension to square numbers.
- Analyze: Compare readability: loop vs comprehension.
- Create: Build comprehension with nested loop.

## Common Errors
- Wrong syntax: `[for x in range(5) x**2]` (expression first).
- Overcomplicating: if too complex, use loop instead.
- Nested confusion: `[x for row in matrix for x in row]` order matters.

## Related Concepts
- [[Python - Lists - Common Patterns]]
- [[Python - Loops - For vs While]]
- [[Python - Functions - Lambda Functions]]

## MOC
- Parent: [[Python - Lists (MOC)]]
