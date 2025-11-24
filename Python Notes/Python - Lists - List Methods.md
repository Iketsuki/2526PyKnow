---
tags: [python, lists, methods]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: list methods (append, extend, insert, sort, etc.)."
  - "Understand: when to use each method."
  - "Apply: manipulate lists with methods."
---

# Python - Lists - List Methods

## Concept
**Methods** are actions on lists. Main ones: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `count()`, `index()`.

## Adding Items

**append() — Add One Item to End:**
```python
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # ['apple', 'banana', 'cherry']
```

**extend() — Add Multiple Items:**
```python
fruits = ['apple', 'banana']
more_fruits = ['cherry', 'date']

fruits.extend(more_fruits)
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

# vs append (adds whole list as one item)
fruits2 = ['apple', 'banana']
fruits2.append(more_fruits)
print(fruits2)  # ['apple', 'banana', ['cherry', 'date']]
```

**insert() — Add at Specific Position:**
```python
tasks = ['wake up', 'homework', 'sleep']

tasks.insert(1, 'breakfast')  # Position 1
print(tasks)  # ['wake up', 'breakfast', 'homework', 'sleep']

tasks.insert(0, 'alarm')  # Insert at start
print(tasks)  # ['alarm', 'wake up', 'breakfast', 'homework', 'sleep']
```

## Removing Items

**remove() — Remove by Value:**
```python
fruits = ['apple', 'banana', 'cherry', 'apple']

fruits.remove('banana')  # Remove first 'banana'
print(fruits)  # ['apple', 'cherry', 'apple']

# Removes only first occurrence
fruits.remove('apple')  # Remove first 'apple'
print(fruits)  # ['cherry', 'apple']
```

**pop() — Remove by Index (and Get Value):**
```python
tasks = ['task1', 'task2', 'task3']

removed = tasks.pop(1)  # Remove index 1, return it
print(removed)  # 'task2'
print(tasks)  # ['task1', 'task3']

# Pop last item
last = tasks.pop()
print(last)  # 'task3'
print(tasks)  # ['task1']
```

**clear() — Remove All Items:**
```python
shopping = ['milk', 'bread', 'eggs']
shopping.clear()
print(shopping)  # []
```

## Searching & Counting

**index() — Find Position of Item:**
```python
students = ['Alice', 'Bob', 'Charlie', 'David']

pos = students.index('Charlie')
print(pos)  # 2

# Error if not found
# students.index('Eve')  # ValueError!
```

**count() — Count Occurrences:**
```python
responses = ['yes', 'no', 'yes', 'maybe', 'yes']

yes_count = responses.count('yes')
print(yes_count)  # 3

no_count = responses.count('no')
print(no_count)  # 1
```

**in — Check If Item Exists:**
```python
allowed = ['Alice', 'Bob', 'Charlie']

if 'Bob' in allowed:
    print('Bob can enter')

if 'Eve' not in allowed:
    print('Eve cannot enter')
```

## Sorting & Reversing

**sort() — Sort in Place:**
```python
scores = [85, 92, 78, 88]
scores.sort()
print(scores)  # [78, 85, 88, 92]

# Reverse sort
scores.sort(reverse=True)
print(scores)  # [92, 88, 85, 78]

# Sort strings (alphabetical)
names = ['Charlie', 'Alice', 'Bob']
names.sort()
print(names)  # ['Alice', 'Bob', 'Charlie']
```

**reverse() — Reverse Order:**
```python
items = ['a', 'b', 'c', 'd']
items.reverse()
print(items)  # ['d', 'c', 'b', 'a']

# Or use slicing (doesn't modify original)
reversed_copy = items[::-1]
```

**sorted() — New Sorted List:**
```python
scores = [85, 92, 78, 88]

# Create new sorted list (don't modify original)
sorted_scores = sorted(scores)
print(scores)  # [85, 92, 78, 88] (unchanged)
print(sorted_scores)  # [78, 85, 88, 92]
```

## Real-World Examples

**To-Do List (Add & Remove):**
```python
tasks = ['homework', 'dishes']

tasks.append('laundry')  # Add task
print(tasks)

tasks.remove('dishes')  # Complete task
print(tasks)
```

**Leaderboard (Sort):**
```python
leaderboard = [('Alice', 95), ('Bob', 87), ('Charlie', 92)]

# Sort by score (second element)
leaderboard.sort(key=lambda x: x[1], reverse=True)
for name, score in leaderboard:
    print(f'{name}: {score}')
```

**Remove Duplicates (Keep Order):**
```python
numbers = [1, 2, 2, 3, 1, 4]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)  # [1, 2, 3, 4]
```

## Method Comparison

| Method | Modifies? | Returns | Use When |
|--------|-----------|---------|----------|
| `append()` | Yes | None | Add 1 item |
| `extend()` | Yes | None | Add multiple items |
| `insert()` | Yes | None | Add at position |
| `remove()` | Yes | None | Remove by value |
| `pop()` | Yes | Item | Remove by index |
| `clear()` | Yes | None | Remove all |
| `sort()` | Yes | None | Sort in place |
| `reverse()` | Yes | None | Reverse in place |
| `count()` | No | Count | Count items |
| `index()` | No | Position | Find item |

## Exercises by Bloom Level
- Remember: What does `append()` do?
- Understand: Difference between `append()` and `extend()`?
- Apply: Use `insert()` to add item at position.
- Analyze: Compare `sort()` vs `sorted()`.
- Create: Build a student rank tracker (add, sort, remove).

## Common Errors
- `append()` returns None: `x = list.append(5)` makes `x = None`.
- `insert()` doesn't return value: use it for side effect only.
- `sort()` modifies list: doesn't create new list.
- `remove()` only first occurrence: loop to remove all.

## Related Concepts
- [[Python - Lists - Common Patterns]]
- [[Python - Lists - Tuple vs List vs Set]]
- [[Python - Loops - For Loop Basics]]

## MOC
- Parent: [[Python - Lists (MOC)]]
