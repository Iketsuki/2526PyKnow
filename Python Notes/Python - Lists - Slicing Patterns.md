---
tags: [python, lists, slicing]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: slicing syntax `[start:stop:step]`."
  - "Understand: how slice boundaries work."
  - "Apply: use slicing to extract parts."
---

# Python - Lists - Slicing Patterns

## Concept
**Slicing** extracts a range of items. Syntax: `list[start:stop:step]`.
- **start** — where to begin (inclusive, default 0)
- **stop** — where to end (exclusive, default end)
- **step** — jump between items (default 1)

## Basic Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4] (index 2, 3, 4)
print(numbers[0:3])    # [0, 1, 2] (first 3)
print(numbers[5:8])    # [5, 6, 7]
```

## Slice Shortcuts

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[:3])     # [0, 1, 2] (start to 3)
print(numbers[5:])     # [5, 6, 7, 8, 9] (5 to end)
print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (all)
```

## Step (Skip Items)

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (odd indices)
print(numbers[::3])    # [0, 3, 6, 9] (every 3rd)

# Reverse with negative step
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## Real-World: Splitting Lists

**First Half, Second Half:**
```python
scores = [85, 92, 78, 88, 95, 81]

mid = len(scores) // 2
first_half = scores[:mid]     # [85, 92, 78]
second_half = scores[mid:]    # [88, 95, 81]

print(f'Morning: {first_half}')
print(f'Afternoon: {second_half}')
```

**Top 3, Bottom 3:**
```python
leaderboard = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']

top_3 = leaderboard[:3]        # First 3
bottom_3 = leaderboard[-3:]    # Last 3

print(f'Top: {top_3}')
print(f'Bottom: {bottom_3}')
```

**Every Nth Item (Pattern Matching):**
```python
# Every other day
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
weekdays = days[::2]  # Mon, Wed, Fri, Sun
weekends_and_mid = days[1::2]  # Tue, Thu, Sat

print(f'Pattern 1: {weekdays}')
print(f'Pattern 2: {weekends_and_mid}')
```

**Reverse List:**
```python
items = ['a', 'b', 'c', 'd']
reversed_items = items[::-1]
print(reversed_items)  # ['d', 'c', 'b', 'a']

# Without creating new list:
for item in items[::-1]:
    print(item)  # d, c, b, a
```

**Middle Section (Exclude First & Last):**
```python
grades = [78, 85, 92, 88, 95, 81, 76]

middle = grades[1:-1]  # Exclude first and last
print(middle)  # [85, 92, 88, 95, 81]
```

## Negative Step (Reverse From Position)

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[8:2:-1])  # [8, 7, 6, 5, 4] (from 8 down to 3)
print(numbers[6:1:-2])  # [6, 4, 2] (from 6 down by 2s)
```

## Safe Slicing (Never Out-of-Bounds)

```python
items = ['a', 'b', 'c']

# Slicing is always safe—won't crash even if out of bounds
print(items[0:100])     # ['a', 'b', 'c'] (not an error!)
print(items[-100:2])    # ['a', 'b'] (safe)
print(items[10:20])     # [] (empty list, not an error!)
```

## Exercises by Bloom Level
- Remember: What's `list[2:5]`?
- Understand: Why is `list[2:5]` not include 5?
- Apply: Get last 3 items with slicing.
- Analyze: Compare `list[::2]` vs `list[1::2]`.
- Create: Extract alternating items (checkerboard pattern).

## Common Errors with Example Code

1) Forgetting stop is exclusive (not inclusive)

WRONG
```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:3])  # Expecting [1, 2, 3] but got [1, 2]
# Stop index 3 is excluded!
```

CORRECT
```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # [1, 2, 3] (includes 1, 2, 3)
# Remember: start:stop includes start but excludes stop
```

2) Negative step confusion (direction not obvious)

WRONG
```python
numbers = [0, 1, 2, 3, 4, 5]
result = numbers[4:2:-1]  # Expecting [4, 3, 2] but got [4, 3]
# Stop at 2 is still exclusive!
```

CORRECT
```python
numbers = [0, 1, 2, 3, 4, 5]
result = numbers[4:0:-1]  # [4, 3, 2, 1] (stops before 0)
result2 = numbers[::-1]   # [5, 4, 3, 2, 1, 0] (full reverse)
```

3) Assuming slicing can error (it can't)

WRONG
```python
items = ['a', 'b', 'c']
# Student expects this to error
result = items[10:20]  # But it doesn't error!
```

CORRECT
```python
items = ['a', 'b', 'c']
result = items[10:20]  # Returns [] (empty list, safe)
# Slicing is always safe, even out of bounds
# (unlike indexing which raises IndexError)
```

## Related Concepts
- [[Python - Lists - Indexing & Edge Cases]]
- [[Python - Loops - Enumerate & Zip]]
- [[Python - Lists - Common Patterns]]

## MOC
- Parent: [[Python - Lists (MOC)]]
