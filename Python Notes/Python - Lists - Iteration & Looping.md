---
tags: [python, lists, iteration, loops]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `for item in list` syntax."
  - "Understand: iteration processes each item in order."
  - "Apply: use loops to process lists and extract data."
  - "Analyze: when to use different iteration patterns."
---

# Python - Lists - Iteration & Looping

## Concept
**Iterate** over list items using `for item in list`. Each loop cycle processes one item in order.

## Basic Iteration

```python
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(f'Hello, {name}!')

# Iteration with processing
scores = [85, 90, 78, 92]
for score in scores:
    print(f'Score: {score}')
```

## Iteration with Index

```python
names = ['Alice', 'Bob', 'Charlie']

# Method 1: range(len())
for i in range(len(names)):
    print(f'{i}: {names[i]}')

# Method 2: enumerate() - cleaner!
for i, name in enumerate(names):
    print(f'{i}: {name}')
```

## Real Examples

```python
# Example 1: Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)  # 15

# Example 2: Find maximum
numbers = [3, 7, 2, 9, 1]
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(max_val)  # 9

# Example 3: Filter items
scores = [85, 92, 78, 88, 95]
passing = []
for score in scores:
    if score >= 80:
        passing.append(score)
print(passing)  # [85, 92, 88, 95]

# Example 4: Transform items
words = ['apple', 'banana', 'cherry']
lengths = []
for word in words:
    lengths.append(len(word))
print(lengths)  # [5, 6, 6]
```

## Exercises by Bloom Level

- **Remember**: Write a simple `for` loop over a list.
- **Understand**: What happens after each iteration?
- **Apply**: Loop through a list and sum all numbers.
- **Analyze**: When do you need `range(len(list))` vs direct iteration?
- **Create**: Build a program that filters and displays items from a list.

## Common Errors with Example Code

### Error 1: Modifying list while iterating
```python
# WRONG: Deleting items while iterating (skips items)
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # Skips some items!

# CORRECT: Iterate over a copy
items = [1, 2, 3, 4, 5]
for item in items[:]:  # [:] creates copy
    if item % 2 == 0:
        items.remove(item)

# BETTER: Create new list
items = [1, 2, 3, 4, 5]
items = [x for x in items if x % 2 != 0]
```

### Error 2: Forgetting that loop variable persists
```python
# After loop, variable still exists
for item in [1, 2, 3]:
    pass

print(item)  # 3 (loop variable persists!)

# Be careful: This can cause unexpected behavior in some cases
```

### Error 3: Using loop variable outside valid scope
```python
# WRONG: Assuming nested loop variable exists outside
for i in range(3):
    for j in range(2):
        value = i + j

# This works (j = 1 after loop), but be aware variables persist

# BETTER: Use descriptive names to track which loop var is which
```

### Error 4: Not initializing accumulator before loop
```python
# WRONG: sum doesn't exist before loop
for num in [1, 2, 3]:
    sum += num  # NameError: sum is not defined

# CORRECT: Initialize before loop
sum = 0
for num in [1, 2, 3]:
    sum += num
print(sum)  # 6
```

### Error 5: Confusing enumerate with multiple unpacking
```python
# WRONG: Not unpacking enumerate correctly
names = ['Alice', 'Bob']
for name in enumerate(names):
    print(name)  # (0, 'Alice'), (1, 'Bob') - tuples!

# CORRECT: Unpack properly
for index, name in enumerate(names):
    print(f'{index}: {name}')

# OR if you just need the index or name
for i in range(len(names)):
    print(f'{i}: {names[i]}')
```

## Tips
- Use `enumerate(list)` to get both index and item.
- Use direct `for item in list` when you don't need the index.
- Use `range(len(list))` when you need to modify items by index.
- Iterate over a copy `[:]` if you need to modify the original list.

## Related Concepts
- [[Python - Lists - Indexing & Edge Cases]]
- [[Python - Loops - For Loop Basics]]
- [[Python - Loops - Enumerate & Zip]]

## MOC
- Parent: [[Python - Lists (MOC)]]
