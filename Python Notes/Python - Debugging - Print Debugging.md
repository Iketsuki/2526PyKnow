---
tags: [python, debugging, print]
moc: [[Python - Debugging (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: inserting debug print statements."
  - "Understand: when to add prints."
  - "Apply: use print to inspect values."
---

# Python - Debugging - Print Debugging

## Concept
Insert `print()` statements to inspect variables and trace execution flow.

## Example Code
```python
x = 5
print(f'x before loop: {x}')
for i in range(3):
    x += i
    print(f'x in loop: {x}')
print(f'x after loop: {x}')
```

## Exercises by Bloom Level
- Remember: Add a debug print.
- Understand: What to print?
- Apply: Debug a broken loop.
- Analyze: Too many prints vs too few?
- Create: Use print to trace function calls.

## Tips
- Use descriptive labels in print statements.
 
## Common Errors with Example Code

### Error 1: Printing too little information
```python
# WRONG: Prints a value without context
value = compute()
print(value)  # Hard to know what this is

# CORRECT: Add descriptive label
value = compute()
print(f'DEBUG: compute() returned {value}')
```

### Error 2: Leaving debug prints in production logic
```python
# WRONG: Many prints left in final code
for i in range(1000000):
  process(i)
  print(i)  # Slows program and pollutes output

# CORRECT: Use logging with levels or remove prints
import logging
logging.basicConfig(level=logging.INFO)
for i in range(1000000):
  process(i)
  logging.debug(f'Processed {i}')
```

### Error 3: Not showing variable context (ambiguous output)
```python
# WRONG: Repeated prints that are ambiguous
print(x)
print(y)

# CORRECT: Show labels
print(f'x={x}, y={y}')
```

### Error 4: Printing large objects directly
```python
# WRONG: Dumping huge structures makes logs unreadable
print(huge_list)

# CORRECT: Print lengths or summaries
print(f'huge_list length={len(huge_list)}')
print('First 5 items:', huge_list[:5])
```

### Error 5: Relying on prints instead of assertions/tests
```python
# WRONG: Using prints as only verification
print('result is', result)  # Not an automated check

# CORRECT: Add simple assertion or unit test
assert result == expected, f'Expected {expected}, got {result}'
```

## MOC
- Parent: [[Python - Debugging (MOC)]]
