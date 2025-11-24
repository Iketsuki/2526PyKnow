---
tags: [python, loops, patterns]
moc: [[Python - Loops (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: enumerate(), zip(), range()."
  - "Understand: loop control (break, continue)."
  - "Apply: iterate multiple sequences together."
---

# Python - Loops - Advanced Patterns

## Concept
**Advanced loop patterns** — Use `enumerate()` to get index, `zip()` to combine lists, `break` to exit early, `continue` to skip items.

## Enumerate: Index + Value

```python
# Without enumerate (tedious)
colors = ['red', 'blue', 'green']
for i in range(len(colors)):
    print(f'{i}: {colors[i]}')

# With enumerate (clean)
for index, color in enumerate(colors):
    print(f'{index}: {color}')
# Output:
# 0: red
# 1: blue
# 2: green

# Custom start index
for index, color in enumerate(colors, start=1):
    print(f'{index}. {color}')
# Output:
# 1. red
# 2. blue
# 3. green
```

## Zip: Combine Multiple Lists

```python
# Iterate two lists together
names = ['Alice', 'Bob', 'Charlie']
ages = [14, 15, 16]

for name, age in zip(names, ages):
    print(f'{name} is {age}')
# Output:
# Alice is 14
# Bob is 15
# Charlie is 16

# Zip stops at shortest list
scores = [85, 92]
for name, age, score in zip(names, ages, scores):
    print(f'{name}: {score}')
# Output:
# Alice: 85
# Bob: 92
# (Charlie is skipped - no score)
```

## Break: Exit Early

```python
# Find first even number
numbers = [1, 3, 5, 7, 2, 4]
for num in numbers:
    if num % 2 == 0:
        print(f'Found even: {num}')
        break
# Output: Found even: 2

# Search and stop
items = ['apple', 'banana', 'cherry', 'date']
search = 'cherry'
for index, item in enumerate(items):
    if item == search:
        print(f'Found at index {index}')
        break
```

## Continue: Skip to Next

```python
# Skip odd numbers
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 1:  # Odd
        continue
    print(num)
# Output: 2, 4, 6

# Skip missing data
scores = [85, None, 92, None, 88]
total = 0
count = 0
for score in scores:
    if score is None:
        continue
    total += score
    count += 1

average = total / count if count > 0 else 0
print(f'Average: {average}')  # 88.33
```

## Loop with Else

```python
# else runs if loop completes (no break)
search = 'mango'
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    if fruit == search:
        print(f'Found {search}')
        break
else:
    print(f'{search} not found')
# Output: mango not found

# With break (else doesn't run)
search = 'banana'
for fruit in fruits:
    if fruit == search:
        print(f'Found {search}')
        break
else:
    print(f'{search} not found')
# Output: Found banana
```

## Range with Enumerate

```python
# Number sequence with index
for index, num in enumerate(range(5)):
    print(f'{index}: {num}')
# Output:
# 0: 0
# 1: 1
# 2: 2
# 3: 3
# 4: 4
```

## Real-World: Grade Check

```python
def check_grades(grades):
    '''Find first failing grade'''
    for index, grade in enumerate(grades, start=1):
        if grade < 70:
            print(f'Student {index} is failing: {grade}')
            return index
    print('All students passing')
    return None

grades = [85, 92, 65, 88]
result = check_grades(grades)  # Student 3 is failing: 65
```

## Real-World: Match Pairs

```python
def pair_students(names, skills):
    '''Pair students with matching skills'''
    pairs = []
    for name, skill in zip(names, skills):
        pairs.append(f'{name}: {skill}')
    return pairs

names = ['Alice', 'Bob', 'Charlie']
skills = ['coding', 'art', 'music']

for pair in pair_students(names, skills):
    print(pair)
# Output:
# Alice: coding
# Bob: art
# Charlie: music
```

## Real-World: Find Duplicate

```python
def find_duplicate(items):
    '''Find first item that appears twice'''
    seen = []
    for index, item in enumerate(items):
        if item in seen:
            return f'Duplicate: {item} at index {index}'
        seen.append(item)
    return 'No duplicates'

data = ['a', 'b', 'c', 'b', 'd']
print(find_duplicate(data))  # Duplicate: b at index 3
```

## Real-World: Progress Tracker

```python
def track_progress(tasks):
    '''Track which tasks are done'''
    for index, task in enumerate(tasks, start=1):
        status = '✓' if task['done'] else '✗'
        print(f'{index}. {status} {task["name"]}')

tasks = [
    {'name': 'Homework', 'done': True},
    {'name': 'Practice', 'done': False},
    {'name': 'Read', 'done': True}
]

track_progress(tasks)
# Output:
# 1. ✓ Homework
# 2. ✗ Practice
# 3. ✓ Read
```

## Common Patterns Reference

```python
# Get index and value
for i, item in enumerate(items):
    print(i, item)

# Iterate multiple lists together
for a, b in zip(list1, list2):
    print(a, b)

# Exit loop early
for item in items:
    if condition:
        break

# Skip to next iteration
for item in items:
    if condition:
        continue
    # process item

# Run code if loop didn't break
for item in items:
    if item == target:
        break
else:
    # Only runs if break never happened
    print('Not found')
```

## Exercises by Bloom Level
- Remember: What does `enumerate()` do?
- Understand: When would you use `break` vs `continue`?
- Apply: Find first item matching a condition.
- Analyze: Compare `break` with `loop-else`.
- Create: Build searcher that finds duplicates.

## Common Errors
- Forgetting `enumerate()` returns (index, value) tuple.
- Using `break` in nested loop → Only exits inner loop.
- `loop-else` confused with `if-else`.
- `zip()` stops at shortest list → Need to handle carefully.

## Related Concepts
- [[Python - Loops - For vs While]]
- [[Python - Loops - Range Function]]
- [[Python - Lists - Iteration & Looping]]
- [[Python - Functions - Lambda Functions]]

## MOC
- Parent: [[Python - Loops (MOC)]]
