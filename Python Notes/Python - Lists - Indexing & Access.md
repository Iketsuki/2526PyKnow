---
tags: [python, lists, indexing]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: indexing syntax `list[i]`."
  - "Understand: lists are zero-indexed."
  - "Apply: access items by position."
---

# Python - Lists - Indexing & Access

## Concept
Access list items by position using zero-based indexing. Negative indices count from the end.

## Example Code
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])      # apple
print(fruits[1])      # banana
print(fruits[-1])     # cherry (last)
print(fruits[-2])     # banana (second-to-last)
```

## Exercises by Bloom Level
- Remember: What is the first item in `[1, 2, 3]`?
- Understand: What does a negative index do?
- Apply: Write code to access the 3rd item in a list.
- Analyze: What happens if you access an out-of-bounds index?
- Create: Build a program that accesses list items dynamically.

## Common Errors
- Off-by-one errors (forgetting 0-indexing).
- Index out of range errors.

## Related Concepts
- [[Python - Lists - Slicing]]

## MOC
- Parent: [[Python - Lists (MOC)]]
