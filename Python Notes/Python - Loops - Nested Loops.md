---
tags: [python, loops, nested]
moc: [[Python - Loops (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: nested loop syntax."
  - "Understand: outer vs inner loop."
  - "Apply: build nested structures."
---

# Python - Loops - Nested Loops

## Concept
**Nested loops** — loops inside loops. Inner loop runs completely for each outer loop iteration. Useful for 2D data (tables, grids, patterns).

## Simple Nested Loop

```python
# Outer loop 3 times
for i in range(3):
    print(f'Group {i+1}:')
    
    # Inner loop 2 times (runs for each outer iteration)
    for j in range(2):
        print(f'  Item {j+1}')

# Output:
# Group 1:
#   Item 1
#   Item 2
# Group 2:
#   Item 1
#   Item 2
# Group 3:
#   Item 1
#   Item 2
```

## Real-World: Multiplication Table

```python
# Multiplication table
print('   1  2  3  4  5')
for i in range(1, 6):
    print(f'{i}: ', end='')
    
    for j in range(1, 6):
        print(f'{i*j:3d} ', end='')
    
    print()  # New line

# Output:
#    1  2  3  4  5
# 1:   1  2  3  4  5
# 2:   2  4  6  8 10
# 3:   3  6  9 12 15
# 4:   4  8 12 16 20
# 5:   5 10 15 20 25
```

## Real-World: Star Pattern

```python
# Triangle pattern
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()

# Output:
# *
# **
# ***
# ****
# *****
```

## Real-World: Grid/Table

```python
# 3x3 grid
grid = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

for row in grid:
    for item in row:
        print(item, end=' ')
    print()

# Output:
# A B C
# D E F
# G H I
```

## Searching in 2D

```python
# Find item in table
table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

search = 5
found = False

for i, row in enumerate(table):
    for j, value in enumerate(row):
        if value == search:
            print(f'Found {search} at row {i}, col {j}')
            found = True
            break
    if found:
        break
```

## Class Schedule Example

```python
# Course schedule (days × time slots)
schedule = {
    'Monday': ['Math', 'English', 'Science'],
    'Tuesday': ['History', 'PE', 'Math'],
    'Wednesday': ['English', 'Science', 'Art']
}

for day, classes in schedule.items():
    print(f'{day}:')
    for period, class_name in enumerate(classes, 1):
        print(f'  Period {period}: {class_name}')

# Output:
# Monday:
#   Period 1: Math
#   Period 2: English
#   Period 3: Science
# ...
```

## Nested While Loops

```python
# Game rounds (outer) with multiple turns (inner)
rounds = 3
rounds_played = 0

while rounds_played < rounds:
    rounds_played += 1
    print(f'Round {rounds_played}:')
    
    turns = 0
    while turns < 2:
        turns += 1
        print(f'  Turn {turns}')

# Output:
# Round 1:
#   Turn 1
#   Turn 2
# Round 2:
#   Turn 1
#   Turn 2
# Round 3:
#   Turn 1
#   Turn 2
```

## Three-Level Nesting (Rare)

```python
# 3D structure (years → semesters → courses)
school_data = {
    'Year1': {
        'Fall': ['Math', 'English'],
        'Spring': ['Science', 'History']
    },
    'Year2': {
        'Fall': ['Physics', 'Chemistry'],
        'Spring': ['Biology', 'Art']
    }
}

for year, semesters in school_data.items():
    print(year)
    for semester, courses in semesters.items():
        print(f'  {semester}:')
        for course in courses:
            print(f'    - {course}')
```

## Breaking Nested Loops

```python
# Break inner loop only
found = False

for i in range(5):
    for j in range(5):
        if i == 2 and j == 3:
            print(f'Found at ({i}, {j})')
            found = True
            break  # Breaks inner loop
    if found:
        break  # Break outer loop
```

## Performance Warning

```python
# Nested loop: 1000 × 1000 = 1,000,000 iterations (slow!)
for i in range(1000):
    for j in range(1000):
        pass  # Slow!

# Better: use vectorization or numpy for large data
```

## Exercises by Bloom Level
- Remember: How many times runs inner loop in 3×4 nested?
- Understand: Why use nested for 2D data?
- Apply: Print 4×4 multiplication table.
- Analyze: Trace 3×3 nested loop execution.
- Create: Build checkerboard pattern (alternating X and O).

## Common Errors
- Off-by-one in both loops: leads to wrong grid size.
- Forgetting inner loop runs completely: 3×4 = 12 iterations total.
- Breaking outer from inner: only breaks inner (use flag to break both).

## Related Concepts
- [[Python - Loops - For vs While]]
- [[Python - Loops - Enumerate & Zip]]
- [[Python - Lists - Common Patterns]]

## MOC
- Parent: [[Python - Loops (MOC)]]
