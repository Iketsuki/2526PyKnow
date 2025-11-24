---
tags: [python, lists, methods]
moc: [[Python - Lists (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: common list methods."
  - "Understand: .append(), .insert(), .remove(), .sort()."
  - "Apply: modify lists safely and efficiently."
---

# Python - Lists - Methods & Operations

## Concept
**List methods** — Built-in operations to modify lists: `.append()` (add), `.insert()` (insert at index), `.remove()` (remove by value), `.pop()` (remove by index), `.sort()` (sort in place).

## Add Items

```python
# .append() - add to end
scores = [85, 92]
scores.append(78)
print(scores)  # [85, 92, 78]

# .insert() - add at specific index
scores.insert(1, 88)  # Insert 88 at index 1
print(scores)  # [85, 88, 92, 78]

# .extend() - add multiple items
scores.extend([95, 90])
print(scores)  # [85, 88, 92, 78, 95, 90]

# Difference: append() adds item, extend() unpacks list
items = [1, 2]
items.append([3, 4])
print(items)  # [1, 2, [3, 4]] - nested list

items2 = [1, 2]
items2.extend([3, 4])
print(items2)  # [1, 2, 3, 4] - flat list
```

## Remove Items

```python
# .remove() - remove by value (first occurrence)
colors = ['red', 'blue', 'red', 'green']
colors.remove('red')
print(colors)  # ['blue', 'red', 'green']

# .pop() - remove by index and return value
colors = ['red', 'blue', 'green']
removed = colors.pop(1)  # Remove index 1
print(removed)  # blue
print(colors)  # ['red', 'green']

# .pop() without index removes last item
last = colors.pop()
print(last)  # green

# .clear() - remove all items
colors.clear()
print(colors)  # []
```

## Find and Count

```python
# .index() - find index of value
colors = ['red', 'blue', 'green']
index = colors.index('blue')
print(index)  # 1

# Safe search: check first
if 'yellow' in colors:
    index = colors.index('yellow')
else:
    print('Not found')

# .count() - count occurrences
items = [1, 2, 2, 3, 2, 4]
print(items.count(2))  # 3
print(items.count(5))  # 0
```

## Sort and Reverse

```python
# .sort() - sorts in place (modifies original)
scores = [92, 85, 95, 78]
scores.sort()
print(scores)  # [78, 85, 92, 95]

# .sort(reverse=True) - descending
scores.sort(reverse=True)
print(scores)  # [95, 92, 85, 78]

# .reverse() - reverse order
items = [1, 2, 3]
items.reverse()
print(items)  # [3, 2, 1]

# sorted() function (doesn't modify original)
original = [92, 85, 95, 78]
sorted_scores = sorted(original)
print(sorted_scores)  # [78, 85, 92, 95]
print(original)  # [92, 85, 95, 78] - unchanged
```

## Copy Lists

```python
# WRONG: assignment creates reference
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)  # [1, 2, 3, 4] - MODIFIED!

# RIGHT: .copy() creates independent copy
original = [1, 2, 3]
copy = original.copy()
copy.append(4)
print(original)  # [1, 2, 3] - unchanged
print(copy)  # [1, 2, 3, 4]

# Also works: copy = original[:]
```

## Real-World: Leaderboard

```python
def update_leaderboard(scores, new_score):
    '''Add score to leaderboard, keep top 10'''
    scores.append(new_score)
    scores.sort(reverse=True)
    
    # Keep only top 10
    if len(scores) > 10:
        scores.pop()  # Remove lowest
    
    return scores

leaderboard = [95, 88, 92, 85]
leaderboard = update_leaderboard(leaderboard, 90)
print(leaderboard)  # [95, 92, 90, 88, 85]
```

## Real-World: Todo List

```python
todos = ['homework', 'practice', 'read']

# Add item
todos.append('exercise')
print(todos)  # [..., 'exercise']

# Complete item (remove)
if 'practice' in todos:
    todos.remove('practice')
print(todos)

# Insert urgent item
todos.insert(0, 'urgent task')
print(todos)  # ['urgent task', ...]

# Sort alphabetically
todos.sort()
print(todos)
```

## Real-World: Grade Analysis

```python
def analyze_grades(scores):
    '''Find stats for a list of grades'''
    if not scores:
        return None
    
    # Create working copy
    sorted_scores = sorted(scores)
    
    # Find median
    n = len(sorted_scores)
    if n % 2 == 0:
        median = (sorted_scores[n//2-1] + sorted_scores[n//2]) / 2
    else:
        median = sorted_scores[n//2]
    
    return {
        'min': min(scores),
        'max': max(scores),
        'avg': round(sum(scores) / len(scores), 2),
        'median': median
    }

grades = [85, 92, 88, 95, 78, 92]
stats = analyze_grades(grades)
print(stats)
# {'min': 78, 'max': 95, 'avg': 88.33, 'median': 90.0}
```

## Real-World: Filter and Clean

```python
# Remove duplicates (order-preserving)
items = [1, 2, 2, 3, 1, 4]
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
print(unique)  # [1, 2, 3, 4]

# Or use set (loses order)
unique_set = list(set(items))
print(unique_set)  # [1, 2, 3, 4] - different order

# Remove blanks
lines = ['Alice', '', 'Bob', '', 'Charlie']
lines = [line for line in lines if line]  # List comprehension
print(lines)  # ['Alice', 'Bob', 'Charlie']
```

## Common Methods Reference

```python
# Add items
list.append(x)  # Add to end
list.insert(i, x)  # Add at index
list.extend(iterable)  # Add multiple

# Remove items
list.remove(x)  # Remove by value
list.pop(i)  # Remove by index, return value
list.clear()  # Remove all

# Find
x in list  # Check existence
list.index(x)  # Find index
list.count(x)  # Count occurrences

# Order
list.sort()  # Sort in place
list.reverse()  # Reverse order
list.copy()  # Make independent copy
```

## Exercises by Bloom Level
- Remember: What does `.append()` do?
- Understand: Difference between `.append()` and `.extend()`.
- Apply: Build a todo list with add/remove functionality.
- Analyze: Compare `.sort()` (in-place) vs `sorted()` (new list).
- Create: Build grade analyzer with min/max/median.

## Common Errors with Example Code

1) Copy vs assignment (unexpected shared reference)

WRONG
```python
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)  # [1, 2, 3, 4] — original modified unexpectedly
```

CORRECT
```python
original = [1, 2, 3]
copy = original.copy()  # or copy = original[:]
copy.append(4)
print(original)  # [1, 2, 3] — unchanged
```

2) Using `remove()` when value may not exist (ValueError)

WRONG
```python
items = [1, 2, 3]
items.remove(5)  # ValueError if 5 not present
```

CORRECT
```python
items = [1, 2, 3]
if 5 in items:
    items.remove(5)
else:
    print('Value not found')
```

3) Modifying a list while iterating (skips items / bugs)

WRONG
```python
nums = [1, 2, 3, 4]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)  # Unexpected
```

CORRECT
```python
nums = [1, 2, 3, 4]
nums = [n for n in nums if n % 2 != 0]
print(nums)  # [1, 3]
```

4) Confusing `append()` with `extend()` (nested lists)

WRONG
```python
lst = [1, 2]
lst.append([3, 4])
print(lst)  # [1, 2, [3, 4]]
```

CORRECT
```python
lst = [1, 2]
lst.extend([3, 4])
print(lst)  # [1, 2, 3, 4]
```

Short tips:
- Use `.copy()` (or slicing) to clone lists.
- Check membership before `.remove()` or handle ValueError.
- Avoid mutating lists while iterating; use comprehensions.
- Use `append()` for single items, `extend()` for iterables.

## Related Concepts
- [[Python - Lists - Indexing & Edge Cases]]
- [[Python - Lists - Common Patterns]]
- [[Python - Lists - List Comprehension]]
- [[Python - Variables & Types - Built-in Functions]]

## MOC
- Parent: [[Python - Lists (MOC)]]
