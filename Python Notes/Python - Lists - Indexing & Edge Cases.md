---
tags: [python, lists, indexing]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: index syntax and positions."
  - "Understand: negative indices, out-of-bounds."
  - "Apply: safely access list items."
---

# Python - Lists - Indexing & Edge Cases

## Concept
**Indexing** accesses items by position. **Index 0** is first. **Negative indices** count from end. Out-of-bounds causes error.

## Positive Indexing (From Start)

```python
fruits = ['apple', 'banana', 'cherry', 'date']

print(fruits[0])  # 'apple' (first)
print(fruits[1])  # 'banana' (second)
print(fruits[2])  # 'cherry' (third)
print(fruits[3])  # 'date' (fourth)
```

## Negative Indexing (From End)

```python
fruits = ['apple', 'banana', 'cherry', 'date']

print(fruits[-1])  # 'date' (last)
print(fruits[-2])  # 'cherry' (second to last)
print(fruits[-3])  # 'banana' (third to last)
print(fruits[-4])  # 'apple' (fourth to last)
```

## Visual

```
Index:     0       1        2        3
Item:    'apple' 'banana' 'cherry' 'date'
Index:    -4      -3       -2      -1
```

## Real-World: Getting First & Last

**First and Last Item:**
```python
tasks = ['wake up', 'breakfast', 'homework', 'play', 'sleep']

first_task = tasks[0]  # 'wake up'
last_task = tasks[-1]  # 'sleep'

print(f'Start: {first_task}, End: {last_task}')
```

**Recently Added Item:**
```python
messages = ['Hi', 'How are you?', 'Good!', 'See you!']

latest_message = messages[-1]  # 'See you!' (most recent)
print(f'Last message: {latest_message}')
```

**Remove Last Item Safely:**
```python
scores = [85, 90, 88]
last_score = scores.pop(-1)  # Remove and get last: 88
print(scores)  # [85, 90]
```

## Out-of-Bounds (Error Cases)

```python
fruits = ['apple', 'banana', 'cherry']

# Too high index
print(fruits[5])  # ERROR: IndexError

# Too low negative index
print(fruits[-10])  # ERROR: IndexError

# Empty list
empty = []
print(empty[0])  # ERROR: IndexError
```

## Safe Access with Conditional

```python
items = ['first', 'second', 'third']

# Check length first
if len(items) > 0:
    first = items[0]
    print(first)  # 'first'

# Or use negative index on non-empty
if items:  # Non-empty?
    last = items[-1]
    print(last)  # 'third'
```

## Safe Access with `get()` (Dictionaries Only)

Note: Lists don't have `.get()`, but you can use slicing or conditionals:

```python
items = ['a', 'b', 'c']

# Slicing is always safe (returns empty if out of bounds)
print(items[0:10])  # ['a', 'b', 'c'] (won't crash)

# Or use try-except
try:
    value = items[10]
except IndexError:
    value = None
    print('Index out of range')
```

## Real-World: Leaderboard Last/First

```python
# Last (highest score)
leaderboard = ['Alice', 'Bob', 'Charlie', 'David']

winner = leaderboard[0]  # First place
last_place = leaderboard[-1]  # Last place

print(f'Winner: {winner}, Last: {last_place}')

# Or rotate using slicing
medalists = leaderboard[:3]  # Top 3
print(medalists)  # ['Alice', 'Bob', 'Charlie']
```

## Exercises by Bloom Level
- Remember: What's `fruits[-1]`?
- Understand: Why negative indices useful?
- Apply: Get last item safely from user list.
- Analyze: Compare `list[0]` vs `list[-1]`.
- Create: Build score tracker with first/last logic.

## Common Errors
- Forgetting 0-indexing: `list[1]` is second, not first.
- Forgetting list has no negative: `list[-0]` is same as `list[0]`.
- Out-of-bounds without checking: always check length first.

## Related Concepts
- [[Python - Lists - Slicing Patterns]]
- [[Python - Lists - Tuple vs List vs Set]]
- [[Python - Loops - Enumerate & Zip]]

## MOC
- Parent: [[Python - Lists (MOC)]]
