---
tags: [python, debugging, strategies]
moc: [[Python - Debugging (MOC)]]
difficulty: Beginner
bloom_level: Analyze
learning_objectives:
  - "Remember: debugging steps."
  - "Understand: systematic debugging."
  - "Apply: find and fix bugs."
---

# Python - Debugging - Debugging Strategies

## Concept
A systematic approach: reproduce the bug, isolate the problem, form a hypothesis, test it.

## Example Code
```python
# Strategy: test each piece
def broken_function(x):
    result = x * 2
    print(f'After multiply: {result}')
    result = result + 10
    print(f'After add: {result}')
    return result
```

## Exercises by Bloom Level
- Remember: Steps to debug a program.
- Understand: Why isolate code?
- Apply: Debug a multi-step function.
- Analyze: Root cause analysis.
- Create: Fix complex bugs.

## Common Errors with Example Code

### Error 1: Debugging only symptoms, not root cause
```python
# WRONG: Fixing the immediate error, not the cause
def calculate(items):
    return items[0] + items[1]  # IndexError if fewer than 2 items

# Symptom fix:
if len(items) >= 2:
    return items[0] + items[1]
else:
    return 0  # Works, but maybe not the intent

# CORRECT: Understand what should happen
def calculate(items):
    if len(items) < 2:
        print('Error: need at least 2 items')
        return None
    return items[0] + items[1]
```

### Error 2: Not reproducing the bug reliably
```python
# WRONG: Vague debugging
# "It crashes sometimes"
# Hard to debug what you can't reliably trigger

# CORRECT: Reproduce consistently
# "It crashes when I input negative numbers"
# Test with: calculate(-5, 10)
```

### Error 3: Adding too many print statements at once
```python
# WRONG: Scattered debug output
def process(x):
    print('Step 1')
    print(x)
    y = x * 2
    print('Step 2')
    print(y)
    # Hard to trace output

# BETTER: Organized debugging
def process(x):
    print(f'DEBUG: input x={x}')
    y = x * 2
    print(f'DEBUG: after multiply, y={y}')
    return y
```

### Error 4: Not checking assumptions
```python
# WRONG: Assuming data is what you think
def get_average(scores):
    return sum(scores) / len(scores)

# Crashes if scores is empty!

# CORRECT: Validate assumptions
def get_average(scores):
    if not scores:
        print('Error: scores list is empty')
        return None
    return sum(scores) / len(scores)
```

### Error 5: Changing too much at once when debugging
```python
# WRONG: Multiple changes, can't tell what helped
# Change variable name, reorder lines, modify logic all at once

# CORRECT: One change at a time
# 1. Fix the first issue, test
# 2. If still broken, fix next issue, test
# 3. Keep track of what fixed what
```

## MOC
- Parent: [[Python - Debugging (MOC)]]
