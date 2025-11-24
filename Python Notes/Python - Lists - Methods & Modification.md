---
tags: [python, lists, methods]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: common list methods (`append`, `remove`, `pop`, `insert`)."
  - "Understand: each method modifies the list in-place."
  - "Apply: use methods to add, remove, and reorder items."
---

# Python - Lists - Methods & Modification

## Concept
Lists have built-in methods to modify them: `append()` adds items, `remove()` deletes, `pop()` removes by index, `insert()` adds at a position.

## Example Code
```python
items = [1, 2, 3]
items.append(4)           # [1, 2, 3, 4]
items.insert(0, 0)        # [0, 1, 2, 3, 4]
items.remove(2)           # [0, 1, 3, 4]
last = items.pop()        # Returns 4, list is [0, 1, 3]
```

## Exercises by Bloom Level
- Remember: Write a program that appends 3 items.
- Understand: What's the difference between `remove()` and `pop()`?
- Apply: Modify a list using multiple methods.
- Analyze: What happens if you remove a non-existent item?
- Create: Build a to-do list program with add/remove/display.

## Common Errors with Example Code

1) Thinking `append()` returns the list (it returns None)

WRONG
```python
my_list = [1, 2, 3]
my_list = my_list.append(4)  # append() returns None!
print(my_list)  # None (lost the list!)
```

CORRECT
```python
my_list = [1, 2, 3]
my_list.append(4)  # Don't assign the return value
print(my_list)  # [1, 2, 3, 4]
```

2) Removing an item that doesn't exist (ValueError)

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

3) Modifying list during iteration (skips items)

WRONG
```python
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # Modifying while looping
# Result: some items are skipped!
```

CORRECT
```python
items = [1, 2, 3, 4, 5]
# Create new list instead of modifying during loop
items = [item for item in items if item % 2 != 0]
print(items)  # [1, 3, 5]
```

## Related Concepts
- [[Python - Lists - Iteration & Looping]]

## MOC
- Parent: [[Python - Lists (MOC)]]
