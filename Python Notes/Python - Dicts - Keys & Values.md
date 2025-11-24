---
tags: [python, dicts, keys, values]
moc: [[Python - Dicts (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `.keys()`, `.values()`, `.items()` syntax."
  - "Understand: what each method returns and when to use."
  - "Apply: iterate over keys, values, or both."
  - "Analyze: search, filter, and check existence in dicts."
  - "Create: programs using dict methods to organize data."
---

# Python - Dicts - Keys & Values

## Concept
Access dict data using:
- **`.keys()`** — Get all keys as a list-like object
- **`.values()`** — Get all values as a list-like object
- **`.items()`** — Get all key-value pairs as tuples

## Getting Keys

```python
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 95}

# Get all keys
print(scores.keys())  # dict_keys(['Alice', 'Bob', 'Charlie'])

# Convert to list if needed
key_list = list(scores.keys())
print(key_list)  # ['Alice', 'Bob', 'Charlie']

# Check if key exists
if 'Alice' in scores.keys():
    print('Alice found!')

# Simpler: use 'in' directly on dict
if 'Alice' in scores:  # Same as above, more Pythonic
    print('Alice found!')
```

## Getting Values

```python
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 95}

# Get all values
print(scores.values())  # dict_values([90, 85, 95])

# Convert to list if needed
value_list = list(scores.values())
print(value_list)  # [90, 85, 95]

# Find maximum value
max_score = max(scores.values())
print(max_score)  # 95

# Sum all values
total = sum(scores.values())
print(total)  # 270

# Count occurrences
print(scores.values().count(90))  # Error! dict_values doesn't have .count()
# Convert to list first
scores_list = list(scores.values())
print(scores_list.count(90))  # 1
```

## Getting Items

```python
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 95}

# Get all items (key-value pairs as tuples)
print(scores.items())  # dict_items([('Alice', 90), ('Bob', 85), ...])

# Convert to list if needed
items_list = list(scores.items())
print(items_list)  # [('Alice', 90), ('Bob', 85), ('Charlie', 95)]

# Use for iteration
for name, score in scores.items():
    print(f'{name}: {score}')
```

## Real Examples

```python
# Example 1: Check which students passed (>80)
grades = {'Alice': 95, 'Bob': 78, 'Charlie': 85, 'David': 72}

print('Passed:')
for name in grades.keys():
    if grades[name] >= 80:
        print(f'  {name}')

# Better way (using .items()):
print('Passed:')
for name, grade in grades.items():
    if grade >= 80:
        print(f'  {name}')

# Example 2: Get all scores above average
all_scores = list(grades.values())
average = sum(all_scores) / len(all_scores)

print(f'Average: {average}')
for name, grade in grades.items():
    if grade >= average:
        print(f'{name}: {grade} (above average)')

# Example 3: Find the top scorer
scores = {'Alice': 95, 'Bob': 78, 'Charlie': 85}
top_name = None
top_score = -1

for name, score in scores.items():
    if score > top_score:
        top_score = score
        top_name = name

print(f'Top scorer: {top_name} with {top_score}')

# Example 4: Create lists of keys and values
inventory = {'apples': 50, 'bananas': 30, 'oranges': 20}

items = list(inventory.keys())
quantities = list(inventory.values())

print(f'Items: {items}')
print(f'Quantities: {quantities}')

# Example 5: Filter dict by values
prices = {'apple': 0.50, 'banana': 0.30, 'cherry': 1.50, 'date': 2.00}

expensive = {}
for item, price in prices.items():
    if price > 1.00:
        expensive[item] = price

print(expensive)  # {'cherry': 1.5, 'date': 2.0}
```

## Methods Comparison

| Method | Returns | Best For | Notes |
|--------|---------|----------|-------|
| `.keys()` | Key list | Check membership, iterate keys | Use `in` operator instead |
| `.values()` | Value list | Sum, max, min, filter values | Non-hashable, can have duplicates |
| `.items()` | Tuples of (key, value) | Most operations, iteration | Default for looping |

## Exercises by Bloom Level

- **Remember**: Call `.keys()`, `.values()`, `.items()`.
- **Understand**: What does each method return?
- **Apply**: Loop over keys and values; find max/min.
- **Analyze**: When use `.items()` vs separate loops?
- **Create**: Build programs that organize data using dict methods.

## Common Errors with Example Code

### Error 1: Forgetting dict_keys/dict_values are not lists
```python
# WRONG: Trying to use list methods on dict views
scores = {'Alice': 90, 'Bob': 85}

# This fails!
print(scores.keys()[0])  # TypeError: 'dict_keys' object is not subscriptable
print(scores.values().count(90))  # AttributeError: 'dict_values' has no attribute 'count'

# CORRECT: Convert to list first
key_list = list(scores.keys())
print(key_list[0])  # 'Alice'

value_list = list(scores.values())
print(value_list.count(90))  # 1
```

### Error 2: Assuming .keys() is needed to check membership
```python
# WRONG: Unnecessary use of .keys()
if 'Alice' in scores.keys():
    print('Found')

# CORRECT: Check directly on dict
if 'Alice' in scores:
    print('Found')
```

### Error 3: Confusing key existence with value existence
```python
# WRONG: Checking values like keys
scores = {'Alice': 90, 'Bob': 85}

if 90 in scores:  # Checks keys, not values!
    print('Found')  # Never prints

# CORRECT: Use .values() to check values
if 90 in scores.values():
    print('Found')  # Prints!
```

### Error 4: Modifying dict while iterating over .keys()/.values()
```python
# WRONG: Modifying dict during iteration
data = {'a': 1, 'b': 2, 'c': 3}

for key in data.keys():
    if key == 'b':
        del data[key]  # RuntimeError: dictionary changed size during iteration

# CORRECT: Convert to list first
for key in list(data.keys()):
    if key == 'b':
        del data[key]
```

### Error 5: Trying to use dict methods on other collections
```python
# WRONG: Not remembering these are dict-specific
items = ['a', 'b', 'c']

print(items.keys())  # AttributeError: 'list' has no attribute 'keys'

# CORRECT: Use appropriate methods
my_dict = {'a': 1, 'b': 2}
print(my_dict.keys())  # dict_keys(['a', 'b'])
```

## Tips
- Use **`in`** operator directly on dict for key checking (faster, clearer).
- Use **`.keys()`** to iterate over keys; `for key in dict` is more Pythonic.
- Use **`.values()`** for operations like sum, max, min on all values.
- Use **`.items()`** by default for iteration when you need both key and value.
- Convert to list with `list()` if you need indexing or list methods.
- Remember: dict_keys, dict_values, dict_items are **view objects**, not lists.

## Related Concepts
- [[Python - Dicts - Accessing Values]]
- [[Python - Dicts - Iteration]]
- [[Python - Dicts - Creation & Initialization]]
- [[Python - Conditionals - Membership Testing]]

## MOC
- Parent: [[Python - Dicts (MOC)]]
