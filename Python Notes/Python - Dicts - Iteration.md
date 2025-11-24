---
tags: [python, dicts, iteration, loops]
moc: [[Python - Dicts (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: loop syntax for dicts (.items(), .keys(), .values())."
  - "Understand: iteration over keys, values, or both."
  - "Apply: process and filter dict data during iteration."
  - "Analyze: when to use each iteration method."
  - "Create: programs that process and report dict data."
---

# Python - Dicts - Iteration

## Concept
Iterate dicts using:
- `for key in dict` — loop over keys only
- `for key, value in dict.items()` — loop over key-value pairs
- `for value in dict.values()` — loop over values only
- `for key in dict.keys()` — explicitly loop over keys

## Basic Iteration (Keys Only)

```python
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 95}

# Loop over keys
for name in scores:
    print(f'Name: {name}')
# Output:
# Name: Alice
# Name: Bob
# Name: Charlie

# Get values by accessing dict with key
for name in scores:
    print(f'{name}: {scores[name]}')
# Output:
# Alice: 90
# Bob: 85
# Charlie: 95
```

## Iteration with .items() (Keys & Values)

```python
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 95}

# Cleaner way: unpack both
for name, score in scores.items():
    print(f'{name}: {score}')
# Output:
# Alice: 90
# Bob: 85
# Charlie: 95
```

## Iteration with .values() (Values Only)

```python
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 95}

# Loop over values only
for score in scores.values():
    print(f'Score: {score}')
# Output:
# Score: 90
# Score: 85
# Score: 95

# Sum all scores
total = 0
for score in scores.values():
    total += score
print(f'Total: {total}')  # Total: 270
```

## Iteration with .keys() (Keys Explicitly)

```python
scores = {'Alice': 90, 'Bob': 85}

# Explicit: for key in dict.keys() is same as for key in dict
for key in scores.keys():
    print(key)
# Output: Alice, Bob

# But this is more explicit for readability
for key in scores:  # Same thing, more Pythonic
    print(key)
```

## Real Examples

```python
# Example 1: Display student grades with formatting
grades = {'Alice': 95, 'Bob': 78, 'Charlie': 92}

for name, grade in grades.items():
    if grade >= 90:
        level = 'Excellent'
    elif grade >= 80:
        level = 'Good'
    else:
        level = 'Needs Improvement'
    print(f'{name}: {grade} ({level})')

# Example 2: Find highest value
scores = {'team_a': 45, 'team_b': 32, 'team_c': 48}
highest_team = None
highest_score = 0

for team, score in scores.items():
    if score > highest_score:
        highest_score = score
        highest_team = team

print(f'{highest_team} won with {highest_score}')

# Example 3: Count occurrences (dict as counter)
fruits = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counts = {}

for fruit in fruits:
    if fruit in counts:
        counts[fruit] += 1
    else:
        counts[fruit] = 1

for fruit, count in counts.items():
    print(f'{fruit}: {count}')

# Example 4: Build new dict from iteration
prices = {'apple': 0.50, 'banana': 0.30, 'cherry': 0.60}
discounted = {}

for item, price in prices.items():
    discounted[item] = price * 0.9  # 10% off

for item, price in discounted.items():
    print(f'{item}: ${price:.2f}')
```

## Iteration Methods Comparison

| Method | What You Get | Best For |
|--------|-------------|----------|
| `for key in dict` | Keys only | Need to look up values or just keys |
| `for key, value in dict.items()` | Both key and value | Most common, need both |
| `for value in dict.values()` | Values only | Just need values (summing, finding max) |
| `for key in dict.keys()` | Keys only | Explicit/readable, rarely needed |

## Exercises by Bloom Level

- **Remember**: Write a dict loop using `.items()`.
- **Understand**: Difference between `for key in dict` vs `.items()`?
- **Apply**: Loop and display or filter student grades.
- **Analyze**: When is `.values()` better than `.items()`?
- **Create**: Build a program that processes dict data (counts, sums, filters).

## Common Errors with Example Code

### Error 1: Forgetting to unpack .items()
```python
# WRONG: Not unpacking the tuple
grades = {'Alice': 95, 'Bob': 78}

for item in grades.items():
    print(item)  # ('Alice', 95), ('Bob', 78) - tuples!

# CORRECT: Unpack both
for name, grade in grades.items():
    print(f'{name}: {grade}')  # Alice: 95, Bob: 78
```

### Error 2: Trying to loop over values when you need keys
```python
# WRONG: Can't get name from .values()
scores = {'Alice': 90, 'Bob': 85}

for score in scores.values():
    print(f'{score}: name?')  # Can't access name!

# CORRECT: Use .items() if you need both
for name, score in scores.items():
    print(f'{name}: {score}')
```

### Error 3: Modifying dict while iterating (can cause errors)
```python
# WRONG: Deleting from dict during iteration
student_scores = {'Alice': 90, 'Bob': 78, 'Charlie': 85}

for name, score in student_scores.items():
    if score < 80:
        del student_scores[name]  # RuntimeError!

# CORRECT: Iterate over copy or collect to remove
student_scores = {'Alice': 90, 'Bob': 78, 'Charlie': 85}

for name, score in list(student_scores.items()):  # list() makes copy
    if score < 80:
        del student_scores[name]

# Or better: collect items to remove first
to_remove = [name for name, score in student_scores.items() if score < 80]
for name in to_remove:
    del student_scores[name]
```

### Error 4: Using .keys() when .items() is clearer
```python
# WRONG: Unnecessarily complex
student_scores = {'Alice': 90, 'Bob': 85}

for name in student_scores.keys():
    score = student_scores[name]
    print(f'{name}: {score}')

# CORRECT: Use .items() directly
for name, score in student_scores.items():
    print(f'{name}: {score}')
```

### Error 5: Assuming dict order before Python 3.7
```python
# WRONG: Assuming iteration order (pre-3.7)
data = {'z': 1, 'a': 2, 'b': 3}

# In Python 3.7+, dicts maintain insertion order
# But in Python 3.6 and earlier, order was undefined

# CORRECT: If you need sorted order, sort explicitly
data = {'z': 1, 'a': 2, 'b': 3}

for key in sorted(data.keys()):
    print(f'{key}: {data[key]}')
# Output: a: 2, b: 3, z: 1
```

## Tips
- Use **`.items()`** by default when you need both key and value (most common).
- Use **`.values()`** only when you just need values (summing, finding max).
- Use **`.keys()`** rarely; `for key in dict` is more Pythonic.
- If modifying dict during iteration, iterate over a **copy**: `list(dict.items())`.
- For sorted iteration, use **`sorted(dict.keys())`** or **`sorted(dict.items())`**.

## Related Concepts
- [[Python - Dicts - Accessing Values]]
- [[Python - Dicts - Keys & Values]]
- [[Python - Loops - For Loop Basics]]
- [[Python - Loops - Enumerate & Zip]]

## MOC
- Parent: [[Python - Dicts (MOC)]]
