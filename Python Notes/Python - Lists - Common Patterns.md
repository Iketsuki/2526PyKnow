---
tags: [python, lists, patterns]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: common list operations (append, remove, in)."
  - "Understand: accumulation and filtering patterns."
  - "Apply: build lists from user input or calculations."
---

# Python - Lists - Common Patterns

## Concept
Most list tasks follow patterns: **accumulation** (grow a list), **filtering** (keep some items), **searching** (find an item).

## Pattern 1: Accumulation (Collect Data)

**Add Items One by One:**
```python
# Build shopping list
shopping_list = []

shopping_list.append('milk')
shopping_list.append('bread')
shopping_list.append('eggs')

print(shopping_list)  # ['milk', 'bread', 'eggs']
```

**Collect User Input:**
```python
# Get favorite colors from user
favorites = []

color1 = input('Favorite color: ')
color2 = input('Another color: ')
color3 = input('One more color: ')

favorites.append(color1)
favorites.append(color2)
favorites.append(color3)

print(f'Your favorites: {favorites}')
```

**Accumulate Calculations:**
```python
# Build list of squares
squares = []

for num in range(1, 6):
    square = num * num
    squares.append(square)

print(squares)  # [1, 4, 9, 16, 25]
```

## Pattern 2: Filtering (Keep Matching Items)

**Keep Only Passing Scores:**
```python
all_scores = [45, 78, 92, 55, 88, 60]
passing = []

for score in all_scores:
    if score >= 70:
        passing.append(score)

print(passing)  # [78, 92, 88]
```

**Find Positive Numbers:**
```python
numbers = [-5, 3, -2, 7, -1, 4]
positive = []

for num in numbers:
    if num > 0:
        positive.append(num)

print(positive)  # [3, 7, 4]
```

**Filter Even Numbers:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)  # [2, 4, 6, 8]
```

## Pattern 3: Searching (Find or Count)

**Find First Match:**
```python
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
search_name = 'Charlie'

if search_name in students:
    index = students.index(search_name)
    print(f'{search_name} is at position {index}')  # position 2
else:
    print('Not found')
```

**Count Occurrences:**
```python
responses = ['yes', 'no', 'yes', 'yes', 'no', 'maybe']

yes_count = responses.count('yes')
no_count = responses.count('no')

print(f'Yes: {yes_count}, No: {no_count}')  # Yes: 3, No: 2
```

**Find Maximum/Minimum:**
```python
scores = [85, 92, 78, 88, 95, 81]

highest = max(scores)  # 95
lowest = min(scores)   # 78

print(f'Best: {highest}, Worst: {lowest}')
```

## Combined Patterns (Real-World)

**Temperature Filter:**
```python
# Find hot days (> 25°C)
temperatures = [18, 22, 28, 15, 26, 30, 12]
hot_days = []

for temp in temperatures:
    if temp > 25:
        hot_days.append(temp)

print(f'Hot days: {hot_days}')  # [28, 26, 30]
print(f'Number of hot days: {len(hot_days)}')
```

**Quiz Score Analysis:**
```python
# Collect scores, then analyze
quiz_scores = []

# Accumulation
for i in range(1, 4):
    score = int(input(f'Quiz {i} score: '))
    quiz_scores.append(score)

# Analysis
average = sum(quiz_scores) / len(quiz_scores)
best = max(quiz_scores)
worst = min(quiz_scores)

print(f'Average: {average:.1f}')
print(f'Best: {best}, Worst: {worst}')
```

**Remove Item (Search & Delete):**
```python
to_do = ['homework', 'dishes', 'laundry', 'dishes']

# Remove first occurrence
to_do.remove('dishes')
print(to_do)  # ['homework', 'laundry', 'dishes']

# Remove by index
to_do.pop(1)
print(to_do)  # ['homework', 'dishes']
```

## Pattern 4: List Comprehension (Compact)

Shorter way to build lists:

```python
# Accumulation shorthand
squares = [num * num for num in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Filtering shorthand
evens = [num for num in range(1, 11) if num % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Transformation
names = ['alice', 'bob', 'charlie']
capitalized = [name.upper() for name in names]
print(capitalized)  # ['ALICE', 'BOB', 'CHARLIE']
```

## Quick Reference

| Task | Pattern |
|------|---------|
| Add items | `list.append()` |
| Remove item | `list.remove()` or `list.pop()` |
| Find item | `item in list` or `list.index()` |
| Count item | `list.count(item)` |
| Sort | `list.sort()` or `sorted(list)` |
| Reverse | `list.reverse()` or `list[::-1]` |

## Exercises by Bloom Level
- Remember: How to append to list?
- Understand: Why filter before counting?
- Apply: Build list from user input, filter passing scores.
- Analyze: Compare `remove()` vs `pop()`.
- Create: Build a todo list (add, remove, check off).

## Common Errors with Example Code

1) Modifying a list while looping (skips items)

WRONG
```python
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # Changes list during iteration
print(items)  # [1, 3, 5] but missed some!
```

CORRECT
```python
items = [1, 2, 3, 4, 5]
items_to_remove = [item for item in items if item % 2 == 0]
for item in items_to_remove:
    items.remove(item)
print(items)  # [1, 3, 5]

# OR: Create new list instead
items = [1, 2, 3, 4, 5]
odds = [item for item in items if item % 2 == 1]
```

2) Thinking `append()` returns the list (it returns None)

WRONG
```python
my_list = []
my_list = my_list.append(1)  # append() returns None
print(my_list)  # None
```

CORRECT
```python
my_list = []
my_list.append(1)  # Don't assign append() result
print(my_list)  # [1]
```

3) Forgetting to check if item exists before removing

WRONG
```python
items = [1, 2, 3]
items.remove(5)  # ValueError: list.remove(x): x not in list
```

CORRECT
```python
items = [1, 2, 3]
if 5 in items:
    items.remove(5)
else:
    print('Item not found')
```

## Related Concepts
- [[Python - Loops - For Loop Basics]]
- [[Python - Conditionals - If-Else Basics]]
- [[Python - Lists - Indexing & Edge Cases]]
- [[Python - Lists - Tuple vs List vs Set]]

## MOC
- Parent: [[Python - Lists (MOC)]]
