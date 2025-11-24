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

## Common Errors with Example Code

1) Forgetting `range()` is 0-indexed and exclusive of the end (off-by-one)

WRONG
```python
for i in range(5):
    print(i)
# Prints 0, 1, 2, 3, 4 (not 1-5!)

for i in range(1, 5):  # Should be range(1, 6) to include 5
    print(i)
# Prints 1, 2, 3, 4 (missing 5)
```

CORRECT
```python
for i in range(1, 6):  # Includes 1 through 5
    print(i)  # 1, 2, 3, 4, 5
```

2) Not understanding the step parameter (default step is 1)

WRONG
```python
for i in range(0, 10, 2):
    print(i)
# Prints 0, 2, 4, 6, 8 (expected this)

# But if you want to go backwards, negative step needed:
for i in range(5, 0, 1):  # Wrong: doesn't print anything
    print(i)
```

CORRECT
```python
for i in range(5, 0, -1):  # Use negative step to go backwards
    print(i)  # 5, 4, 3, 2, 1
```

3) Forgetting that `range()` returns an iterator, not a list

WRONG
```python
r = range(5)
print(r[2])  # Might work but confusing
total = r + range(5, 10)  # TypeError: can't concatenate range to range
```

CORRECT
```python
r = range(5)
print(list(r)[2])  # Convert to list if needed: 2

# Or iterate directly:
for i in r:
    print(i)

# Combine ranges (convert to list first if needed)
combined = list(range(5)) + list(range(5, 10))
```

Short tips:
- `range(n)` is 0 to n-1 (end is exclusive).
- Use `range(start, end, step)` for custom ranges.
- Use negative step to count backwards.
- `range()` doesn't create a list, it's an iterator.

## Related Concepts
- [[Python - Loops - For Loop Basics]]

## MOC
- Parent: [[Python - Loops (MOC)]]
