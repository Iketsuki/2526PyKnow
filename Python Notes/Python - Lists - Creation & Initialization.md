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

## What is a List?

A **list** is a container that holds multiple items in order. Like a to-do list or a shopping list.

```python
names = ['Alice', 'Bob', 'Charlie']
scores = [95, 87, 92]
```

Lists use **square brackets** `[` and `]`.

## Creating a List

```python
# List of numbers
numbers = [1, 2, 3, 4]

# List of names
names = ['Alice', 'Bob', 'Charlie']

# Mixed list (numbers and words)
mixed = [1, 'apple', 2, 'banana']

# Empty list (no items yet)
empty = []
```

## Lists Can Hold Different Things

```python
# Numbers
scores = [95, 87, 92]

# Words
colors = ['red', 'blue', 'green']

# Mixed types
combo = [1, 'two', 3.0]

# Booleans
flags = [True, False, True]
```

## Real-World Examples

**Shopping List**
```python
shopping = ['milk', 'bread', 'eggs']
print(shopping)
```

**Scores**
```python
my_scores = [85, 92, 78, 88]
print(my_scores)
```

**To-Do List**
```python
tasks = ['homework', 'eat lunch', 'play outside']
print(tasks)
```

## Exercises by Bloom Level

- **Remember:** Create a list of 3 items.
- **Understand:** What's inside `['apple', 'banana']`?
- **Apply:** Make a list of your favorite games.
- **Create:** Build a list of your weekly tasks.

## Common Errors with Example Code

1) Using curved brackets `()` instead of square brackets `[]`

WRONG
```python
items = (1, 2, 3)
items.append(4)  # Error!
```

CORRECT
```python
items = [1, 2, 3]
items.append(4)
print(items)  # [1, 2, 3, 4]
```

2) Forgetting the brackets

WRONG
```python
numbers = 1, 2, 3  # This is not a list
```

CORRECT
```python
numbers = [1, 2, 3]  # This is a list
```

3) Spacing doesn't matter, but be consistent

```python
# These are all the same
names = ['Alice', 'Bob']
names = [ 'Alice' , 'Bob' ]
names = ['Alice','Bob']
```

## Tips
- Use **`[]`** to make a list
- Lists can hold **numbers, words, or mixed types**
- Empty list is **`[]`**

## Related Concepts
- [[Python - Lists - Indexing & Edge Cases]]
- [[Python - Lists - Add Methods]]

## MOC
- Parent: [[Python - Lists (MOC)]]

## MOC
- Parent: [[Python - Lists (MOC)]]
