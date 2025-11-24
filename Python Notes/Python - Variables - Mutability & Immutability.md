---
tags: [python, variables, mutability, immutability]
moc: [[Python - Variables & Types (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: which types are mutable vs immutable."
  - "Understand: how mutability affects data changes."
  - "Apply: recognize when types can/cannot be modified."
  - "Analyze: why immutability matters for programming."
---

# Python - Variables - Mutability & Immutability

## Concept
**Mutable** types (lists, dicts, sets) can be changed after creation. **Immutable** types (str, int, bool, tuple) cannot be changed; reassigning creates new values.

## Mutable vs Immutable

```python
# MUTABLE: Lists can be changed
numbers = [1, 2, 3]
numbers[0] = 99            # Changes the list directly
numbers.append(4)          # Modifies original
print(numbers)             # [99, 2, 3, 4]

# IMMUTABLE: Strings cannot be changed
text = 'hello'
# text[0] = 'H'           # TypeError! Cannot modify
text = 'Hello'             # Reassign creates NEW value
```

## Mutable Types

```python
# Lists - can be changed
items = [1, 2, 3]
items[0] = 99          # Change element
items.append(4)        # Add element
items.remove(2)        # Remove element

# Dicts - can be changed
person = {'name': 'Alice', 'age': 25}
person['age'] = 26     # Modify value
person['email'] = 'alice@example.com'  # Add pair
del person['age']      # Remove pair

# Sets - can be changed
colors = {'red', 'blue', 'green'}
colors.add('yellow')   # Add element
colors.remove('red')   # Remove element
```

## Immutable Types

```python
# Strings - cannot be changed
text = 'hello'
# text[0] = 'H'  # TypeError!
# Instead, create new string
text = 'Hello'  # Reassign

# Numbers - cannot be changed
x = 5
# x += 1  # Actually creates NEW number (reassigns x)
x = x + 1

# Tuples - cannot be changed
coords = (1, 2, 3)
# coords[0] = 10  # TypeError!

# Booleans - cannot be changed
is_active = True
# is_active[0] = False  # TypeError! (and makes no sense)
is_active = False  # Reassign
```

## Mutable vs Immutable: Function Arguments

```python
# MUTABLE: Function can modify original list
def add_to_list(items):
    items.append(99)

my_list = [1, 2, 3]
add_to_list(my_list)
print(my_list)  # [1, 2, 3, 99] - MODIFIED!

# IMMUTABLE: Function cannot modify original string
def change_text(text):
    text = 'goodbye'  # Only changes local variable
    return text

my_text = 'hello'
result = change_text(my_text)
print(my_text)   # 'hello' - UNCHANGED
print(result)    # 'goodbye'
```

## Real Examples

```python
# Example 1: Mutable lists in loops
scores = [85, 90, 78, 92]
for i in range(len(scores)):
    scores[i] = scores[i] + 5  # Modify in place
print(scores)  # [90, 95, 83, 97]

# Example 2: Immutable strings need reassignment
name = 'alice'
name = name.capitalize()  # Reassign (create new string)
print(name)  # 'Alice'

# Example 3: Tuple vs List
# Tuple (immutable)
point = (10, 20)
# point[0] = 15  # Error!

# List (mutable)
point = [10, 20]
point[0] = 15  # Works!
```

## Exercises by Bloom Level

- **Remember**: List two mutable and two immutable types.
- **Understand**: What happens if you try to change an immutable value?
- **Apply**: Demonstrate mutability with lists and strings.
- **Analyze**: Why might immutable types be useful?
- **Create**: Show how to "change" strings by reassigning.

## Common Errors with Example Code

### Error 1: Trying to modify immutable string
```python
# WRONG: Can't change a character in a string
text = 'hello'
text[0] = 'H'  # TypeError: str object does not support item assignment!

# CORRECT: Create new string and reassign
text = 'H' + text[1:]  # 'Hello'

# BETTER: Use string methods
text = text.capitalize()  # 'Hello'
```

### Error 2: Forgetting that list modifications affect original
```python
# WRONG: Assuming copy is separate
original = [1, 2, 3]
copy = original  # This is NOT a copy! Same reference!
copy[0] = 99
print(original)  # [99, 2, 3] - MODIFIED!

# CORRECT: Make actual copy
original = [1, 2, 3]
copy = original[:]  # Slice creates copy
copy[0] = 99
print(original)  # [1, 2, 3] - unchanged
```

### Error 3: Confusing tuple with list syntax
```python
# WRONG: Parentheses don't always make immutable
t = (1)  # This is just (int 1), NOT a tuple!
print(type(t))  # <class 'int'>

# CORRECT: Single element tuple needs trailing comma
t = (1,)  # Now it's a tuple
print(type(t))  # <class 'tuple'>

# Multiple elements work fine
t = (1, 2, 3)  # Clearly a tuple
```

### Error 4: Trying to use immutable as mutable in function
```python
# WRONG: Expecting string to be modified by function
def uppercase_name(name):
    name = name.upper()
    # name[0] = name[0].upper()  # Would error anyway!

username = 'alice'
uppercase_name(username)
print(username)  # 'alice' (unchanged!)

# CORRECT: Return the modified value
def uppercase_name(name):
    return name.upper()

username = 'alice'
username = uppercase_name(username)
print(username)  # 'ALICE'
```

### Error 5: Using mutable default arguments
```python
# WRONG: Mutable default is shared across calls!
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - not fresh! 
print(add_item(3))  # [1, 2, 3]

# CORRECT: Use None as default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2] - fresh list!
print(add_item(3))  # [3]
```

## Summary Table

| Type | Mutable | Example |
|------|---------|---------|
| List | ✓ | `[1, 2, 3]` |
| Dict | ✓ | `{'key': 'value'}` |
| Set | ✓ | `{1, 2, 3}` |
| String | ✗ | `'hello'` |
| Tuple | ✗ | `(1, 2, 3)` |
| Int | ✗ | `42` |
| Float | ✗ | `3.14` |
| Bool | ✗ | `True` |

## Related Concepts
- [[Python - Strings - String Immutability]]
- [[Python - Variables - Naming Conventions]]
- [[Python - Lists - Methods & Operations]]

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
