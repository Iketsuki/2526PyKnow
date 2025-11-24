---
tags: [python, loops, enumerate, zip, iteration]
moc: [[Python - Loops (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: enumerate() and zip() syntax."
  - "Understand: what each function does and when to use."
  - "Apply: use in loops for cleaner, more efficient code."
  - "Analyze: when to use enumerate+zip together."
  - "Create: complex iterations with enumerate and zip."
---

# Python - Loops - Enumerate & Zip

## Concept
**enumerate()** — loop with index and value. **zip()** — loop over multiple lists together.

## Enumerate (Get Index & Value)

```python
# Regular way (needs manual index)
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(f'{i}: {fruits[i]}')

# Better way with enumerate
for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start counting from 1
for rank, fruit in enumerate(fruits, 1):
    print(f'{rank}: {fruit}')
# Output:
# 1: apple
# 2: banana
# 3: cherry
```

## Real-World: Enumerate

**Score Ranking:**
```python
scores = [95, 87, 92, 88]

for rank, score in enumerate(scores, 1):
    print(f'Rank {rank}: {score}')
# Output:
# Rank 1: 95
# Rank 2: 87
# Rank 3: 92
# Rank 4: 88
```

**Leaderboard:**
```python
students = ['Alice', 'Bob', 'Charlie']

for position, name in enumerate(students, 1):
    print(f'{position}. {name}')
# Output:
# 1. Alice
# 2. Bob
# 3. Charlie
```

**Find Position of Item:**
```python
tasks = ['homework', 'dishes', 'laundry', 'homework']

for index, task in enumerate(tasks):
    if task == 'homework':
        print(f'Homework is at position {index}')
# Output:
# Homework is at position 0
# Homework is at position 3
```

## Zip (Loop Over Multiple Lists)

```python
# Pair up two lists
names = ['Alice', 'Bob', 'Charlie']
scores = [95, 87, 92]

for name, score in zip(names, scores):
    print(f'{name}: {score}')
# Output:
# Alice: 95
# Bob: 87
# Charlie: 92
```

## Real-World: Zip

**Pair Coordinates:**
```python
x_coords = [0, 1, 2, 3]
y_coords = [0, 1, 4, 9]

for x, y in zip(x_coords, y_coords):
    print(f'({x}, {y})')
# Output:
# (0, 0)
# (1, 1)
# (2, 4)
# (3, 9)
```

**Combine Headers & Data:**
```python
headers = ['Name', 'Age', 'City']
data = ['Alice', 25, 'NYC']

for header, value in zip(headers, data):
    print(f'{header}: {value}')
# Output:
# Name: Alice
# Age: 25
# City: NYC
```

**Match Questions & Answers:**
```python
questions = ['What is 2+2?', 'What is 5*3?', 'What is 10/2?']
answers = [4, 15, 5]

for q, a in zip(questions, answers):
    print(f'{q} -> {a}')
# Output:
# What is 2+2? -> 4
# What is 5*3? -> 15
# What is 10/2? -> 5
```

## Combine Enumerate & Zip

```python
# Loop with index over paired lists
names = ['Alice', 'Bob', 'Charlie']
scores = [95, 87, 92]

for rank, (name, score) in enumerate(zip(names, scores), 1):
    print(f'{rank}. {name}: {score}')
# Output:
# 1. Alice: 95
# 2. Bob: 87
# 3. Charlie: 92
```

## Real-World: Grading

```python
students = ['Alice', 'Bob', 'Charlie', 'David']
scores = [95, 78, 92, 88]

for rank, (student, score) in enumerate(zip(students, scores), 1):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    else:
        grade = 'C'
    
    print(f'{rank}. {student}: {score} ({grade})')
# Output:
# 1. Alice: 95 (A)
# 2. Bob: 78 (C)
# 3. Charlie: 92 (A)
# 4. David: 88 (B)
```

## Zip with Different Lengths

```python
names = ['Alice', 'Bob', 'Charlie']
scores = [95, 87]  # One item missing!

for name, score in zip(names, scores):
    print(f'{name}: {score}')
# Output:
# Alice: 95
# Bob: 87
# (Charlie is skipped—no pair)

# Use zip_longest to include all
from itertools import zip_longest

for name, score in zip_longest(names, scores, fillvalue='--'):
    print(f'{name}: {score}')
# Output:
# Alice: 95
# Bob: 87
# Charlie: --
```

## Exercises by Bloom Level

- **Remember**: What does `enumerate()` give you?
- **Understand**: When to use zip() instead of nested loops?
- **Apply**: Use enumerate() to find position, zip() to pair lists.
- **Analyze**: Compare `for i in range(len(list))` vs `enumerate()`.
- **Create**: Build scorecard with ranks, names, and scores.

## Common Errors with Example Code

### Error 1: Forgetting to unpack enumerate
```python
# WRONG: Not unpacking enumerate results
fruits = ['apple', 'banana', 'cherry']
for item in enumerate(fruits):
    print(item)  # (0, 'apple'), (1, 'banana'), (1, 'cherry') - tuples!

# CORRECT: Unpack index and value
for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')  # 0: apple, 1: banana, 2: cherry
```

### Error 2: Enumerate starts at 0 by default
```python
# WRONG: Expecting 1-based indexing
scores = [85, 90, 78]
for rank, score in enumerate(scores):
    print(f'Rank {rank}: {score}')
# Output shows Rank 0, Rank 1, Rank 2 (not 1, 2, 3!)

# CORRECT: Specify start=1 for human-friendly ranking
for rank, score in enumerate(scores, 1):
    print(f'Rank {rank}: {score}')
# Output shows Rank 1, Rank 2, Rank 3
```

### Error 3: Zip stops at shortest list (silent truncation)
```python
# WRONG: Assuming all items are processed
names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [95, 87, 92]  # Missing one score!

for name, score in zip(names, scores):
    print(f'{name}: {score}')
# Output: Only shows Alice, Bob, Charlie (David is silently skipped!)

# CORRECT: Use zip_longest if all items must be processed
from itertools import zip_longest

for name, score in zip_longest(names, scores, fillvalue='N/A'):
    print(f'{name}: {score}')
# Output shows all 4 names, with David: N/A
```

### Error 4: Over-complicating with enumerate when zip is clearer
```python
# WRONG: Unnecessarily using enumerate with range
for i in range(len(names)):
    for j in range(len(scores)):
        if i == j:
            print(f'{names[i]}: {scores[j]}')

# CORRECT: Use zip directly
for name, score in zip(names, scores):
    print(f'{name}: {score}')
```

### Error 5: Incorrect unpacking in enumerate+zip
```python
# WRONG: Not unpacking the zipped pair correctly
names = ['Alice', 'Bob']
scores = [95, 87]

for i, name, score in enumerate(zip(names, scores)):
    print(f'{i}. {name}: {score}')
# Error: Too many values to unpack!

# CORRECT: Unpack the tuple from zip
for i, (name, score) in enumerate(zip(names, scores), 1):
    print(f'{i}. {name}: {score}')
# Output:
# 1. Alice: 95
# 2. Bob: 87
```

## Tips
- Use `enumerate(list)` instead of `range(len(list))` for cleaner code.
- Use `enumerate(..., 1)` for human-friendly 1-based indexing.
- Use `zip()` to pair multiple lists instead of manual indexing.
- Remember: `zip()` stops at shortest list; use `zip_longest()` if needed.
- Unpack properly: `for i, item in enumerate(list)` and `for name, score in zip(names, scores)`.

## Related Concepts
- [[Python - Loops - For Loop Basics]]
- [[Python - Loops - For vs While]]
- [[Python - Lists - Iteration & Looping]]

## MOC
- Parent: [[Python - Loops (MOC)]]
