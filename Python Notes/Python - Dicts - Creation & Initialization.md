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

## What is a Dict?

A **dict** is a container that stores things by name, not by position.

Think of a real dictionary:
- A word (key) → its meaning (value)
- A name (key) → a phone number (value)

```python
scores = {'Alice': 90, 'Bob': 85}
person = {'name': 'Alice', 'age': 25}
```

## How to Create a Dict

Use curly braces `{}` with `key: value` pairs:

```python
# Empty dict
empty = {}

# Dict with data
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 78}

# Dict with different types
person = {
    'name': 'Alice',
    'age': 25,
    'active': True
}
```

## Dict Examples

**Scores by Name**
```python
grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}
```

**Contact Information**
```python
person = {
    'name': 'Alice',
    'phone': '555-1234',
    'email': 'alice@example.com'
}
```

**Word Counts**
```python
word_count = {'python': 3, 'java': 2, 'ruby': 1}
```

**Birthday List**
```python
birthdays = {
    'Alice': 'Jan 15',
    'Bob': 'Mar 20',
    'Charlie': 'Oct 5'
}
```

## How to Use a Dict

Access values by their key:

```python
person = {'name': 'Alice', 'age': 25}
print(person['name'])  # Alice
print(person['age'])   # 25

grades = {'Alice': 90, 'Bob': 85}
print(grades['Alice'])  # 90
```

## Exercises by Bloom Level

- **Remember:** Create a simple dict with 2 items.
- **Understand:** What is a key? What is a value?
- **Apply:** Create a dict about yourself (name, age, etc).
- **Create:** Build a phone number dictionary.

## Common Errors with Example Code

1) Using `=` instead of `:` between key and value

WRONG
```python
person = {'name' = 'Alice'}  # Error!
```

CORRECT
```python
person = {'name': 'Alice'}
```

2) Forgetting commas between pairs

WRONG
```python
person = {'name': 'Alice' 'age': 25}  # Error!
```

CORRECT
```python
person = {'name': 'Alice', 'age': 25}
```

3) Forgetting quotes around string keys and values

WRONG
```python
person = {name: Alice}  # Error - thinks they're variables
```

CORRECT
```python
person = {'name': 'Alice'}  # Strings are quoted
```

4) Numbers can be keys (no quotes needed)

```python
ages = {1: 'Alice', 2: 'Bob', 3: 'Charlie'}
print(ages[1])  # Alice
```

## Tips
- Use **`{key: value}`** syntax
- Keys are usually **strings** or **numbers**
- Keys must be **unique**
- Access values with **`dict[key]`**

## Real-World: Phone Book

```python
phones = {
    'Alice': '555-1001',
    'Bob': '555-1002',
    'Charlie': '555-1003'
}

print(phones['Alice'])  # 555-1001
```

## Related Concepts
- [[Python - Dicts - Accessing Values]]
- [[Python - Dicts - Methods & Operations]]
- [[Python - Data Structures - When to use lists vs dicts]]

## MOC
- Parent: [[Python - Dicts (MOC)]]

## MOC
- Parent: [[Python - Dicts (MOC)]]
