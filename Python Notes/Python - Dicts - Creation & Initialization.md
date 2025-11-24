---
tags: [python, dicts, creation, initialization]
moc: [[Python - Dicts (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: dict syntax `{key: value}`."
  - "Understand: dictionaries store key-value pairs."
  - "Apply: create dicts and initialize with data."
  - "Analyze: when to use dicts vs lists."
---

# Python - Dicts - Creation & Initialization

## Concept
**Dictionaries** store key-value pairs using the syntax `{key: value}`. Keys must be unique, values can be anything.

## Basic Creation

```python
# Empty dict
empty = {}

# Dict with initial values
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 78}

# Dict with various value types
person = {
    'name': 'Alice',
    'age': 25,
    'scores': [90, 85, 88],
    'active': True
}
```

## Different Creation Methods

```python
# Method 1: Literal syntax (most common)
user = {'name': 'Bob', 'email': 'bob@example.com'}

# Method 2: dict() constructor
user = dict(name='Bob', email='bob@example.com')

# Method 3: From list of tuples
pairs = [('name', 'Bob'), ('email', 'bob@example.com')]
user = dict(pairs)

# Method 4: Using .fromkeys() (all same value)
keys = ['a', 'b', 'c']
empty_dict = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}
```

## Real Examples

```python
# Example 1: Student grades
grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}
print(grades['Alice'])  # 'A'

# Example 2: Contact information
contact = {
    'name': 'Alice',
    'phone': '555-1234',
    'email': 'alice@example.com'
}

# Example 3: Nested dict (dict within dict)
students = {
    'alice': {'age': 20, 'major': 'CS'},
    'bob': {'age': 21, 'major': 'Math'}
}

# Example 4: Counting occurrences
word_count = {'python': 3, 'java': 2, 'ruby': 1}
```

## Exercises by Bloom Level

- **Remember**: Create a simple dict. Create empty dict.
- **Understand**: What are keys vs values? What types can keys be?
- **Apply**: Create a dict with mixed types. Add initial values.
- **Analyze**: Why use dicts vs lists?
- **Create**: Build data structures with dicts (phonebook, inventory, etc.).

## Common Errors with Example Code

### Error 1: Using mutable types as keys
```python
# WRONG: Lists can't be dictionary keys (mutable)
scores = {['Alice', 'Bob']: [90, 85]}  # TypeError: unhashable type

# CORRECT: Use immutable types for keys (strings, numbers, tuples)
scores = {('Alice', 'Bob'): [90, 85]}  # Tuple as key (immutable)
scores = {'Alice': 90, 'Bob': 85}  # String keys (most common)
```

### Error 2: Forgetting colons between key and value
```python
# WRONG: Using = instead of :
student = {'name' = 'Alice', 'age' = 25}  # SyntaxError!

# CORRECT: Use colons in dict literal
student = {'name': 'Alice', 'age': 25}
```

### Error 3: Forgetting commas between pairs
```python
# WRONG: Missing comma
person = {'name': 'Alice' 'age': 25}  # SyntaxError!

# CORRECT: Commas separate pairs
person = {'name': 'Alice', 'age': 25}
```

### Error 4: Using quotes inconsistently
```python
# WORKS: All string keys and values
data = {'name': 'Alice', 'city': 'NYC'}

# WRONG: Unquoted key (treated as variable name, causes error)
name_var = 'Alice'
data = {name_var: 'Alice'}  # Key is actually 'Alice' (value of name_var)

# CORRECT: If you want string literal as key
data = {'name_var': 'Alice'}  # 'name_var' is the key
```

### Error 5: Assuming dicts are ordered (pre-Python 3.7)
```python
# In Python 3.7+, dicts maintain insertion order
d = {'z': 1, 'a': 2, 'm': 3}
print(list(d.keys()))  # ['z', 'a', 'm'] (order is preserved)

# But in older Python, order wasn't guaranteed
# Use OrderedDict if you need guaranteed order in older versions
from collections import OrderedDict
d = OrderedDict([('z', 1), ('a', 2)])
```

## Tips
- Keys must be immutable (strings, numbers, tuples).
- Keys must be unique (duplicates overwrite).
- Values can be any type (mutable or immutable).
- Use descriptive key names.

## Related Concepts
- [[Python - Dicts - Accessing Values]]
- [[Python - Dicts - Keys & Values]]
- [[Python - Dicts - Modification & Methods]]

## MOC
- Parent: [[Python - Dicts (MOC)]]
