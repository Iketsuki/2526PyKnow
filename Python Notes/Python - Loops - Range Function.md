---
tags: [python, loops, range]
moc: [[Python - Loops (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `range()` syntax."
  - "Understand: range generates sequences."
  - "Apply: use range for numeric loops."
---

# Python - Loops - Range Function

## Concept
`range()` generates a sequence of numbers. Use it with `for` loops to repeat a fixed number of times.

## Example Code
```python
for i in range(5):
    print(i)                    # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)                    # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)                    # 0, 2, 4, 6, 8
```

## Exercises by Bloom Level
- Remember: Write `range(5)`.
- Understand: What does `range(1, 6)` produce?
- Apply: Loop from 10 down to 1.
- Analyze: Compare `range(5)` with `[0, 1, 2, 3, 4]`.
- Create: Print a multiplication table using range.

## Common Errors
- Forgetting the range is 0-indexed.

## Related Concepts
- [[Python - Loops - For Loop Basics]]

## MOC
- Parent: [[Python - Loops (MOC)]]
