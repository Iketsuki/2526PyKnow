---
tags: [python, dicts, access, keys, values]
moc: [[Python - Dicts (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: access syntax `d[key]` and `.get(key)`."
  - "Understand: what happens if key is missing."
  - "Apply: safely access dictionary values."
  - "Analyze: when to use bracket vs .get()."
---

# Python - Dicts - Accessing Values

## Concept
Access values with `d[key]` or use `.get(key)` to safely get values without errors if the key is missing.

## Basic Access

```python
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 78}

# Access with bracket notation
print(scores['Alice'])      # 90
print(scores['Bob'])        # 85

# This raises KeyError if key missing
print(scores['David'])      # KeyError!
```

## Safe Access with .get()

```python
scores = {'Alice': 90, 'Bob': 85}

# .get() returns None if key missing (no error)
print(scores.get('Alice'))      # 90
print(scores.get('Charlie'))    # None (no KeyError!)

# Provide default value
print(scores.get('David', 0))   # 0 (custom default)
print(scores.get('Eve', 'N/A')) # 'N/A'
```

## Real Examples

```python
# Example 1: Student grades lookup
grades = {
    'Alice': 'A',
    'Bob': 'B',
    'Charlie': 'C'
}

# Safe lookup with default
student = 'David'
grade = grades.get(student, 'Not found')
print(f'{student}: {grade}')  # David: Not found

# Example 2: Configuration with defaults
config = {'theme': 'dark', 'lang': 'en'}
print(config.get('theme', 'light'))     # dark
print(config.get('sound', True))        # True (default)

# Example 3: Checking if key exists
user_data = {'name': 'Alice', 'age': 25}
if 'email' in user_data:
    print(user_data['email'])
else:
    print('No email on file')
```

## Exercises by Bloom Level

- **Remember**: Access a dict value with `[key]`. Use `.get(key)`.
- **Understand**: Difference between `[key]` and `.get(key)`?
- **Apply**: Safely get values with defaults.
- **Analyze**: What if key doesn't exist with `[key]`? How to prevent?
- **Create**: Build lookup programs (phonebook, inventory, etc.).

## Common Errors with Example Code

### Error 1: KeyError when key doesn't exist
```python
# WRONG: Assumes key exists
user = {'name': 'Alice', 'age': 25}
print(user['email'])  # KeyError: 'email' doesn't exist!

# CORRECT: Use .get() for safety
print(user.get('email'))  # None (no error)
print(user.get('email', 'Not provided'))  # 'Not provided'

# ALSO CORRECT: Check first
if 'email' in user:
    print(user['email'])
else:
    print('No email')
```

### Error 2: Not using default value in .get()
```python
# WRONG: .get() without default may return None
config = {'theme': 'dark'}
mode = config.get('mode')  # None (might cause bugs later)

if mode == 'light':  # False (mode is None)
    print('Light mode')

# CORRECT: Provide default
mode = config.get('mode', 'light')
if mode == 'light':
    print('Light mode')  # Prints if not set
```

### Error 3: Confusing dictionary with list indexing
```python
# WRONG: Using integer index on dict (wrong!)
person = {'name': 'Alice', 'age': 25}
print(person[0])  # KeyError: 0 (dicts use keys, not indices)

# CORRECT: Use keys
print(person['name'])  # Alice

# If you need index:
items = list(person.keys())
print(items[0])  # 'name'
```

### Error 4: Modifying dict while iterating (with access)
```python
# WRONG: Accessing may cause issues if dict changes
scores = {'Alice': 90, 'Bob': 85}
for name in scores:
    if scores[name] < 90:
        scores[name] = 90  # Can cause issues in some cases

# CORRECT: Iterate over copy of keys
scores = {'Alice': 90, 'Bob': 85}
for name in list(scores.keys()):
    if scores[name] < 90:
        scores[name] = 90
```

### Error 5: Assuming .get() with list works like with dicts
```python
# WRONG: Lists don't have .get()
items = [1, 2, 3]
print(items.get(0))  # AttributeError: list has no get()

# CORRECT: Lists need bracket access or safe approach
print(items[0])  # 1

# Safe list access (no get method):
index = 5
if index < len(items):
    print(items[index])
else:
    print('Index out of range')
```

## MOC
- Parent: [[Python - Dicts (MOC)]]
