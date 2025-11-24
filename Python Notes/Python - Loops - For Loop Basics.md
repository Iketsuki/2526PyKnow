---
tags: [python, loops, for, iteration]
moc: [[Python - Loops (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `for` loop syntax with sequences."
  - "Understand: how loops repeat a block for each item."
  - "Apply: use loops to process lists, strings, and ranges."
  - "Analyze: when to use for vs while loops."
---

# Python - Loops - For Loop Basics

## Concept
A **`for` loop** repeats a block of code for each item in a sequence (list, string, range, etc.). Useful for processing collections.

## Basic Syntax

```python
for variable in sequence:
    # Code runs for each item
    print(variable)
```

## Real Examples

```python
# Example 1: Loop through a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Example 2: Loop through a string
word = 'hello'
for letter in word:
    print(letter)

# Example 3: Loop through a range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Example 4: Loop with processing
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)  # 2, 4, 6, 8, 10

# Example 5: Loop with conditionals
for num in range(1, 11):
    if num % 2 == 0:
        print(f'{num} is even')
```

## Common Loop Patterns

```python
# Counting
count = 0
for item in ['a', 'b', 'c']:
    count += 1
print(count)  # 3

# Summing
total = 0
for num in [1, 2, 3, 4]:
    total += num
print(total)  # 10

# Finding
target = 'b'
found = False
for item in ['a', 'b', 'c']:
    if item == target:
        found = True
        break

# Building a new list
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(doubled)  # [2, 4, 6, 8, 10]
```

## For vs While

```python
# For loop (when you know the sequence)
for i in [1, 2, 3]:
    print(i)

# While loop (when you have a condition)
i = 1
while i <= 3:
    print(i)
    i += 1
```

## Exercises by Bloom Level

- **Remember**: Write a simple `for` loop. Loop through a list.
- **Understand**: What variable names can you use? What sequences work?
- **Apply**: Loop through a list and print each item.
- **Analyze**: Difference between `for` and `while` loops?
- **Create**: Build a program that processes list items.

## Common Errors with Example Code

### Error 1: Indentation errors
```python
# WRONG: Wrong indentation
for i in [1, 2, 3]:
print(i)  # IndentationError!

# CORRECT: Proper indentation
for i in [1, 2, 3]:
    print(i)
```

### Error 2: Using += without initialization
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

### Error 3: Assuming loop variable exists after loop
```python
# WORKS: Loop variable exists after loop
for item in ['a', 'b', 'c']:
    pass

print(item)  # 'c' (loop variable persists!)

# Be careful: This can cause bugs in some cases
```

### Error 4: Modifying list while looping
```python
# WRONG: Deleting items while iterating
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # Can skip items!

# CORRECT: Loop over a copy
items = [1, 2, 3, 4, 5]
for item in items[:]:  # [:] makes a copy
    if item % 2 == 0:
        items.remove(item)
```

### Error 5: Confusing loop variable scope
```python
# WRONG: Assuming loop variable is scoped
for i in range(3):
    x = i * 2

print(x)  # 4 (x exists! Python has function scope, not block scope)

# This is different from languages like JavaScript
# In Python, loop variables leak out of the loop
```

## Tips
- Loop variable is accessible after the loop ends.
- Use `break` to exit early.
- Use `continue` to skip to next iteration.
- Use `range()` for numeric loops.
- Use slicing `[:]` if you need to modify a list while looping.

## Related Concepts
- [[Python - Loops - Range Function]]
- [[Python - Loops - Loop Patterns]]
- [[Python - Loops - Loop Control (Break & Continue)]]

## MOC
- Parent: [[Python - Loops (MOC)]]
