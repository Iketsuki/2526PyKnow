---
tags: [python, lists, slicing, indexing]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: slicing syntax `list[start:end:step]`."
  - "Understand: slicing extracts sub-lists without modifying original."
  - "Apply: use slicing for various ranges and steps."
  - "Analyze: negative indices and slice behavior."
---

# Python - Lists - Slicing

## Concept
**Slicing** — Extract a sub-list using syntax `[start:end:step]`. Returns a new list without modifying the original. End index is exclusive.

## Basic Slicing

```python
items = [0, 1, 2, 3, 4, 5]

# [start:end] - from start to end (exclusive)
print(items[1:4])      # [1, 2, 3]

# [:end] - from beginning to end
print(items[:3])       # [0, 1, 2]

# [start:] - from start to end
print(items[3:])       # [3, 4, 5]

# [:] - entire list (copy)
print(items[:])        # [0, 1, 2, 3, 4, 5]
```

## Slicing with Step

```python
items = [0, 1, 2, 3, 4, 5]

# [start:end:step] - with step size
print(items[::2])      # [0, 2, 4] (every 2nd item)
print(items[1::2])     # [1, 3, 5] (every 2nd, starting at 1)

# Negative step (reverse)
print(items[::-1])     # [5, 4, 3, 2, 1, 0]
print(items[5:0:-1])   # [5, 4, 3, 2, 1] (reverse, partial)
```

## Negative Indices

```python
items = [0, 1, 2, 3, 4, 5]

# Negative indices count from end
print(items[-1])       # 5 (last item)
print(items[-3:])      # [3, 4, 5] (last 3 items)
print(items[:-1])      # [0, 1, 2, 3, 4] (all but last)
```

## Real Examples

```python
# Example 1: Get first n items
items = ['apple', 'banana', 'cherry', 'date', 'elder']
first_3 = items[:3]
print(first_3)  # ['apple', 'banana', 'cherry']

# Example 2: Get last n items
last_2 = items[-2:]
print(last_2)  # ['date', 'elder']

# Example 3: Reverse a list
reversed_items = items[::-1]
print(reversed_items)  # ['elder', 'date', 'cherry', 'banana', 'apple']

# Example 4: Every other item
items = [1, 2, 3, 4, 5, 6, 7, 8]
every_other = items[::2]
print(every_other)  # [1, 3, 5, 7]

# Example 5: Middle portion
items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
middle = items[3:7]
print(middle)  # [3, 4, 5, 6]
```

## Exercises by Bloom Level

- **Remember**: Write a slice to get the first 3 items. Write a slice to reverse.
- **Understand**: What does `[1:]` do? What does `[::-1]` do?
- **Apply**: Extract every other item from a list.
- **Analyze**: Combine slicing with indexing.
- **Create**: Build a program that slices data dynamically.

## Common Errors with Example Code

### Error 1: Forgetting that end index is exclusive
```python
# WRONG: Expecting index 3 to be included
items = [0, 1, 2, 3, 4, 5]
result = items[0:3]  # Expects [0, 1, 2, 3]
# Actually gets [0, 1, 2] (index 3 NOT included!)

# CORRECT: Remember end is exclusive
result = items[0:4]  # [0, 1, 2, 3] (includes index 3)
```

### Error 2: Using slicing to modify list
```python
# WRONG: Slicing returns a copy, doesn't modify original
items = [1, 2, 3, 4, 5]
items[1:4]  # [2, 3, 4]
print(items)  # [1, 2, 3, 4, 5] (unchanged!)

# CORRECT: Assign to modify
items[1:4] = [10, 20, 30]
print(items)  # [1, 10, 20, 30, 5]
```

### Error 3: Confusing slice with single index
```python
# WRONG: Slice returns list, index returns element
items = [10, 20, 30, 40]
print(items[0])     # 10 (single element)
print(items[0:1])   # [10] (list with one element!)

# CORRECT: Know the difference
element = items[0]      # 10
sublist = items[0:1]    # [10]
```

### Error 4: Negative index in slice confusion
```python
# WRONG: Assuming [:-1] excludes last item
items = [0, 1, 2, 3, 4, 5]
result = items[:-1]  # [0, 1, 2, 3, 4] (correct)
result = items[-1:]  # [5] (just last item, not exclusive)

# CORRECT: Remember negative index rules
result = items[:-1]  # All but last
result = items[-2:]  # Last 2 items
```

### Error 5: Step of 0 or wrong direction
```python
# WRONG: Step can't be 0
items = [0, 1, 2, 3, 4]
result = items[::0]  # ValueError: slice step cannot be zero!

# WRONG: Positive step but backwards indices
result = items[5:0]  # [] (empty! can't go 5→0 with positive step)

# CORRECT: Use negative step for backwards
result = items[5:0:-1]  # [5, 4, 3, 2, 1]
```

## Tips
- End index is exclusive (not included).
- Negative indices count from the end.
- Slicing returns a new list (doesn't modify original).
- Use `[::-1]` to reverse a list.

## Related Concepts
- [[Python - Lists - Indexing & Edge Cases]]
- [[Python - Lists - Iteration & Looping]]
- [[Python - Strings - String Slicing & Indexing]]

## MOC
- Parent: [[Python - Lists (MOC)]]
