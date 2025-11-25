---
tags: [python, lists, methods, add]
moc: [[Python - Lists (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: .append(), .insert(), .extend() syntax."
  - "Understand: difference between append and extend."
  - "Apply: add items to lists safely."
---

# Python - Lists - Add Methods

## Concept
Three ways to add items to a list: `.append()` adds one item to the end, `.insert()` adds at a specific index, `.extend()` adds multiple items and unpacks them.

## .append() — Add One Item to End

```python
scores = [85, 92]
scores.append(78)
print(scores)  # [85, 92, 78]

# Works with any value
items = [1, 2]
items.append("string")
items.append([3, 4])  # Adds list as single element
print(items)  # [1, 2, "string", [3, 4]]
```

## .insert() — Add at Specific Index

```python
scores = [85, 92, 78]
scores.insert(1, 88)  # Insert at index 1
print(scores)  # [85, 88, 92, 78]

# Insert at start (index 0)
scores.insert(0, 100)
print(scores)  # [100, 85, 88, 92, 78]

# Insert at end (same as append)
scores.insert(len(scores), 60)
print(scores)  # [..., 60]
```

## .extend() — Add Multiple Items

```python
items = [1, 2]
items.extend([3, 4])
print(items)  # [1, 2, 3, 4]

# Works with any iterable
items = ['a']
items.extend('bc')  # Unpacks string into chars
print(items)  # ['a', 'b', 'c']
```

## append() vs extend()

```python
lst = [1, 2]
lst.append([3, 4])
print(lst)  # [1, 2, [3, 4]] — nested list!

lst = [1, 2]
lst.extend([3, 4])
print(lst)  # [1, 2, 3, 4] — flat list
```

## Common Errors with Example Code

1) Using append() when you want extend() — creates nested list

WRONG
```python
items = [1, 2]
items.append([3, 4])
print(items)  # [1, 2, [3, 4]] — not what we wanted
```

CORRECT
```python
items = [1, 2]
items.extend([3, 4])
print(items)  # [1, 2, 3, 4]
```

2) Forgetting that append() returns None

WRONG
```python
items = [1, 2]
items = items.append(3)  # Returns None!
print(items)  # None (oops!)
```

CORRECT
```python
items = [1, 2]
items.append(3)  # Modifies list in place
print(items)  # [1, 2, 3]
```

3) Using insert() with invalid index — extends list instead of raising error

WRONG
```python
items = [1, 2]
items.insert(10, 99)  # Index 10 doesn't exist
print(items)  # [1, 2, 99] — appends instead of error
```

CORRECT
```python
# Insert uses safe behavior: clamps to list length
items = [1, 2]
items.insert(0, 0)  # Insert at start
print(items)  # [0, 1, 2]
```

## Related Concepts
- [[Python - Lists - Remove Methods]]
- [[Python - Lists - Common Patterns]]

## MOC
- Parent: [[Python - Lists (MOC)]]
