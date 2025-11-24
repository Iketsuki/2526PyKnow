---
tags: [python, dicts, modification, methods]
moc: [[Python - Dicts (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: add, update, delete, clear dict items."
  - "Understand: dict methods (.pop(), .update(), .get(), .clear())."
  - "Apply: modify and maintain dict data safely."
  - "Analyze: when to use .pop() vs del, .update() vs assignment."
  - "Create: dict-based databases and data structures."
---

# Python - Dicts - Modification & Methods

## Concept
Modify dicts with:
- **Add/Update**: `d[key] = value`
- **Delete**: `del d[key]` or `d.pop(key)`
- **Clear**: `d.clear()`
- **Update multiple**: `d.update({key: value, ...})`

## Adding & Updating Items

```python
scores = {'Alice': 90}

# Add new item
scores['Bob'] = 85
print(scores)  # {'Alice': 90, 'Bob': 85}

# Update existing item
scores['Alice'] = 95
print(scores)  # {'Alice': 95, 'Bob': 85}

# Add multiple items at once
scores.update({'Charlie': 92, 'David': 88})
print(scores)  # {'Alice': 95, 'Bob': 85, 'Charlie': 92, 'David': 88}
```

## Deleting Items

```python
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 92}

# Method 1: del (removes item, raises KeyError if missing)
del scores['Bob']
print(scores)  # {'Alice': 90, 'Charlie': 92}

# Method 2: .pop() (removes and returns value, raises KeyError if missing)
score = scores.pop('Alice')
print(score)  # 90
print(scores)  # {'Charlie': 92}

# Method 3: .pop() with default (safe, returns default if missing)
score = scores.pop('NonExistent', None)
print(score)  # None (doesn't raise error)

# Method 4: .clear() (removes all items)
scores.clear()
print(scores)  # {}
```

## Dict Methods Reference

```python
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 92}

# .keys() — Get all keys
print(scores.keys())  # dict_keys(['Alice', 'Bob', 'Charlie'])

# .values() — Get all values
print(scores.values())  # dict_values([90, 85, 92])

# .items() — Get all key-value pairs
print(scores.items())  # dict_items([('Alice', 90), ('Bob', 85), ...])

# .get(key, default) — Get value safely
print(scores.get('Alice'))  # 90
print(scores.get('Bob', 0))  # 85
print(scores.get('NonExistent', 0))  # 0 (safe!)

# .pop(key, default) — Remove and return value
value = scores.pop('Alice', None)  # 90
print(scores)  # Removed Alice

# .update() — Add/update multiple items
scores.update({'Eve': 87, 'Alice': 95})
print(scores)  # {'Bob': 85, 'Charlie': 92, 'Eve': 87, 'Alice': 95}

# .clear() — Remove all items
scores.clear()
print(scores)  # {}

# .copy() — Create a shallow copy
original = {'Alice': 90, 'Bob': 85}
copy = original.copy()
copy['Alice'] = 100
print(original)  # {'Alice': 90, 'Bob': 85} (unchanged)
print(copy)  # {'Alice': 100, 'Bob': 85}

# .setdefault(key, default) — Get value or set if missing
scores = {}
scores.setdefault('Alice', 90)  # Sets if missing
print(scores)  # {'Alice': 90}
scores.setdefault('Alice', 100)  # Alice exists, no change
print(scores)  # {'Alice': 90}
```

## Real Examples

```python
# Example 1: Build a student grade database
students = {}

# Add students
students['Alice'] = 90
students['Bob'] = 85

# Update a grade
students['Bob'] = 87

# Add more students
students.update({'Charlie': 92, 'David': 78})

print(students)  # {'Alice': 90, 'Bob': 87, 'Charlie': 92, 'David': 78}

# Example 2: Remove failing students
passing = students.copy()
failing = []

for name in list(students.keys()):
    if students[name] < 80:
        failing.append(name)
        del passing[name]

print(f'Passing: {passing}')
print(f'Failing: {failing}')

# Example 3: Count word frequencies
text = 'apple banana apple cherry banana apple'
words = text.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)  # {'apple': 3, 'banana': 2, 'cherry': 1}

# Example 4: Safer version using .get()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)  # {'apple': 3, 'banana': 2, 'cherry': 1}

# Example 5: Merge multiple dicts
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'a': 100}  # Will override 'a'

merged = {}
merged.update(dict1)
merged.update(dict2)
merged.update(dict3)

print(merged)  # {'a': 100, 'b': 2, 'c': 3, 'd': 4}
```

## Exercises by Bloom Level

- **Remember**: Add an item; delete an item using `del` and `.pop()`.
- **Understand**: When should you use `.get()` vs direct access?
- **Apply**: Modify and maintain a dict-based database.
- **Analyze**: Compare `del` vs `.pop()` vs `.clear()`.
- **Create**: Build a word frequency counter using dicts.

## Common Errors with Example Code

### Error 1: Using direct access when key might not exist
```python
# WRONG: KeyError if key doesn't exist
scores = {'Alice': 90, 'Bob': 85}

print(scores['Charlie'])  # KeyError: 'Charlie'

# CORRECT: Use .get() for safe access
print(scores.get('Charlie'))  # None
print(scores.get('Charlie', 0))  # 0 (default value)
```

### Error 2: Confusing del vs .pop()
```python
# WRONG: Using del when you need the value
scores = {'Alice': 90, 'Bob': 85}

del scores['Alice']  # Deletes, but doesn't return value
# value = del scores['Alice']  # Syntax error!

# CORRECT: Use .pop() to remove and get value
value = scores.pop('Alice')  # Returns 90, deletes key
print(value)  # 90

# Or use del if you only need to remove
scores = {'Alice': 90, 'Bob': 85}
del scores['Bob']
# Value is gone, no way to get it
```

### Error 3: .pop() without default when key might not exist
```python
# WRONG: KeyError if key doesn't exist
scores = {'Alice': 90}

value = scores.pop('NonExistent')  # KeyError!

# CORRECT: Provide default
value = scores.pop('NonExistent', None)  # Returns None safely
value = scores.pop('NonExistent', 0)  # Returns 0
```

### Error 4: Forgetting that .update() overwrites keys
```python
# WRONG: Expecting .update() to merge safely
original = {'Alice': 90, 'Bob': 85}

original.update({'Alice': 100, 'Charlie': 92})
print(original)  # {'Alice': 100, 'Bob': 85, 'Charlie': 92}
# Alice was overwritten!

# CORRECT: Be aware of overwrites, use .copy() if needed
original = {'Alice': 90, 'Bob': 85}
backup = original.copy()
original.update({'Alice': 100})
print(original)  # {'Alice': 100, 'Bob': 85}
print(backup)  # {'Alice': 90, 'Bob': 85} (unchanged)
```

### Error 5: Modifying dict while iterating over .keys()
```python
# WRONG: Can't modify dict during iteration
data = {'a': 1, 'b': 2, 'c': 3}

for key in data.keys():
    del data[key]  # RuntimeError: dictionary changed size

# CORRECT: Convert to list first
for key in list(data.keys()):
    del data[key]

# OR: Create new dict instead of modifying
data = {'a': 1, 'b': 2, 'c': 3}
data = {k: v for k, v in data.items() if k != 'b'}
# data is now {'a': 1, 'c': 3}
```

## Methods Quick Reference

| Method | Purpose | Returns | Raises Error? |
|--------|---------|---------|---------------|
| `d[key] = value` | Add/update | — | — |
| `d.get(key, default)` | Safe access | value or default | No |
| `d.pop(key, default)` | Remove & return | value or default | No (if default given) |
| `del d[key]` | Remove | — | Yes (KeyError) |
| `d.clear()` | Remove all | — | — |
| `d.update(other)` | Merge/update | — | — |
| `d.copy()` | Shallow copy | New dict | — |
| `d.setdefault(key, default)` | Get or set | value | — |

## Tips
- Use **`.get()`** for safe value access (returns None by default).
- Use **`.pop()`** when you need to remove and use the value.
- Use **`del`** when you just need to remove (slightly faster).
- Always provide a **default in `.pop()`** if key might not exist.
- Use **`.copy()`** to avoid modifying the original dict.
- Use **`list(dict.keys())`** if you need to modify dict during iteration.

## Related Concepts
- [[Python - Dicts - Accessing Values]]
- [[Python - Dicts - Iteration]]
- [[Python - Dicts - Keys & Values]]
- [[Python - Error Handling - Try-Except Basics]]

## MOC
- Parent: [[Python - Dicts (MOC)]]
