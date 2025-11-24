---
tags: [python, lists, indexing]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: indexing syntax `list[i]`."
  - "Understand: lists are zero-indexed."
  - "Apply: access items by position."
---

# Python - Lists - Indexing & Access

## Concept
Access list items by position using zero-based indexing. Negative indices count from the end.

## Example Code
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])      # apple
print(fruits[1])      # banana
print(fruits[-1])     # cherry (last)
print(fruits[-2])     # banana (second-to-last)
```

## Exercises by Bloom Level
- Remember: What is the first item in `[1, 2, 3]`?
- Understand: What does a negative index do?
- Apply: Write code to access the 3rd item in a list.
- Analyze: What happens if you access an out-of-bounds index?
- Create: Build a program that accesses list items dynamically.

## Common Errors with Example Code

1) Forgetting zero-based indexing (off-by-one error)

WRONG
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[1])  # Expecting 'apple', but got 'banana'!
# Index 0 is first, 1 is second
```

CORRECT
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])  # apple (first)
print(fruits[1])  # banana (second)
print(fruits[2])  # cherry (third)
```

2) Index out of range (IndexError)

WRONG
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[5])  # IndexError: list index out of range
```

CORRECT
```python
fruits = ['apple', 'banana', 'cherry']
if len(fruits) > 2:
    print(fruits[2])  # cherry
else:
    print('Index out of range')
```

3) Negative indices behaving unexpectedly (wrong end item)

WRONG
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[-1])  # cherry (last)
print(fruits[-4])  # IndexError (only 3 items!)
```

CORRECT
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[-1])  # cherry (last)
print(fruits[-2])  # banana (second-to-last)
print(fruits[-3])  # apple (third-to-last, same as [0])
```

Short tips:
- First item is at index 0, not 1.
- Use negative indices to count from the end.
- Always check that the index is within range.

## Related Concepts
- [[Python - Lists - Slicing]]

## MOC
- Parent: [[Python - Lists (MOC)]]
