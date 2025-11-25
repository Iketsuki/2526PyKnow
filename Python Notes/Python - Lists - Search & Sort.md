---
tags: [python, lists, methods, search, sort]
moc: [[Python - Lists (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: .index(), .count(), .sort(), .reverse(), sorted() syntax."
  - "Understand: when to use each search/sort method."
  - "Apply: safely find and organize list items."
---

# Python - Lists - Search & Sort

## Concept
Four ways to search and sort: `.index()` finds position of value, `.count()` counts occurrences, `.sort()` orders in-place, `.reverse()` reverses in-place. Built-in `sorted()` returns new sorted list.

## .index() — Find Position of Value

```python
colors = ['red', 'blue', 'green', 'red']
position = colors.index('blue')
print(position)  # 1

# Find first 'red'
position = colors.index('red')
print(position)  # 0

# Raises ValueError if not found
colors.index('yellow')  # ValueError: 'yellow' is not in list
```

With safe check:

```python
colors = ['red', 'blue', 'green']
if 'red' in colors:
    position = colors.index('red')
    print(f"Found at index {position}")
else:
    print('Not found')
```

## .count() — Count Occurrences

```python
scores = [10, 20, 10, 30, 10]
count = scores.count(10)
print(count)  # 3

# Count items without value
count = scores.count(999)
print(count)  # 0 (no error)
```

Counting with conditions:

```python
words = ['cat', 'dog', 'cat', 'bird']
cat_count = words.count('cat')
print(cat_count)  # 2
```

## .sort() — Sort In-Place

```python
scores = [30, 10, 20]
scores.sort()
print(scores)  # [10, 20, 30]

# Reverse sort
scores.sort(reverse=True)
print(scores)  # [30, 20, 10]

# Sort strings
names = ['zoe', 'alice', 'bob']
names.sort()
print(names)  # ['alice', 'bob', 'zoe']
```

Custom sort:

```python
students = [('alice', 95), ('bob', 87), ('zoe', 92)]
students.sort(key=lambda x: x[1], reverse=True)  # By score
print(students)  # [('alice', 95), ('zoe', 92), ('bob', 87)]
```

## .reverse() — Reverse In-Place

```python
items = [1, 2, 3]
items.reverse()
print(items)  # [3, 2, 1]

# Works on strings too
letters = ['a', 'b', 'c']
letters.reverse()
print(letters)  # ['c', 'b', 'a']
```

## sorted() — Return New Sorted List

Unlike `.sort()` which modifies in-place, `sorted()` returns a new list:

```python
scores = [30, 10, 20]
new_scores = sorted(scores)
print(new_scores)  # [10, 20, 30]
print(scores)  # [30, 10, 20] unchanged

# Reverse sort
new_scores = sorted(scores, reverse=True)
print(new_scores)  # [30, 20, 10]
```

Works on any iterable:

```python
string = 'python'
letters = sorted(string)
print(letters)  # ['h', 'o', 'p', 't', 'y', 'n']
```

## .sort() vs sorted()

```python
# .sort() — modifies original
numbers = [3, 1, 2]
numbers.sort()
# numbers is now [1, 2, 3]

# sorted() — creates new list
numbers = [3, 1, 2]
result = sorted(numbers)
# numbers is still [3, 1, 2]
# result is [1, 2, 3]
```

## Common Errors with Example Code

1) Using .index() on missing value without checking

WRONG
```python
items = ['a', 'b', 'c']
position = items.index('z')  # ValueError: 'z' is not in list
```

CORRECT
```python
items = ['a', 'b', 'c']
if 'z' in items:
    position = items.index('z')
else:
    print('Not found')
    position = -1
```

2) Forgetting that .sort() returns None (modifies in-place)

WRONG
```python
scores = [3, 1, 2]
sorted_scores = scores.sort()
print(sorted_scores)  # None (not [1, 2, 3])
```

CORRECT
```python
scores = [3, 1, 2]
scores.sort()  # Modify original
print(scores)  # [1, 2, 3]

# Or use sorted() for new list
sorted_scores = sorted(scores)
print(sorted_scores)  # [1, 2, 3]
```

3) Comparing different types when sorting

WRONG
```python
items = [3, 'apple', 1]
items.sort()  # TypeError: '<' not supported between instances
```

CORRECT
```python
# Convert to same type
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # [1, 2, 3]

# For mixed: convert or separate
mixed = [3, 'apple', 1]
strings = sorted([x for x in mixed if isinstance(x, str)])
numbers = sorted([x for x in mixed if isinstance(x, int)])
```

## Real-World: Leaderboard

```python
# Sort scores in descending order
leaderboard = [(100, 'alice'), (85, 'bob'), (92, 'zoe')]
leaderboard.sort(reverse=True)

for score, name in leaderboard:
    print(f"{name}: {score}")
```

## Related Concepts
- [[Python - Lists - Add Methods]]
- [[Python - Lists - Remove Methods]]
- [[Python - Lists - Common Patterns]]

## MOC
- Parent: [[Python - Lists (MOC)]]
