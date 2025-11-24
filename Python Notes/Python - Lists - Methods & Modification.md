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

## Common Errors
- `append()` returns None, not the modified list.
- Removing during iteration can skip items.

## Related Concepts
- [[Python - Lists - Iteration & Looping]]

## MOC
- Parent: [[Python - Lists (MOC)]]
