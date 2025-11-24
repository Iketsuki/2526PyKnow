---
tags: [python, loops, patterns, iteration]
moc: [[Python - Loops (MOC)]]
difficulty: Beginner
bloom_level: Analyze
learning_objectives:
  - "Remember: common loop patterns (accumulation, filtering, searching)."
  - "Understand: when to use each pattern."
  - "Apply: implement patterns to solve problems."
  - "Analyze: combine multiple patterns effectively."
---

# Python - Loops - Loop Patterns

## Concept
**Loop patterns** — Reusable approaches to common tasks: accumulation (sum/product), filtering (select items), searching (find a value), transformation (modify items).

## Pattern 1: Accumulation (Sum/Product)

```python
# Accumulation pattern: combine values into one result
total = 0
for x in [1, 2, 3, 4]:
    total += x
print(total)  # 10

# Product accumulation
product = 1
for x in [2, 3, 4]:
    product *= x
print(product)  # 24

# String accumulation
result = ''
for word in ['hello', 'world']:
    result += word
print(result)  # 'helloworld'
```

## Pattern 2: Filtering (Select Items)

```python
# Filtering pattern: select items that match condition
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
print(evens)  # [0, 2, 4, 6, 8]

# Filter words by length
words = ['apple', 'cat', 'dog', 'elephant']
long_words = []
for word in words:
    if len(word) > 3:
        long_words.append(word)
print(long_words)  # ['apple', 'elephant']

# Filter with multiple conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for num in numbers:
    if num > 5 and num % 2 == 0:
        result.append(num)
print(result)  # [6, 8, 10]
```

## Pattern 3: Searching (Find a Value)

```python
# Searching pattern: find first occurrence
target = 5
found = False
for x in range(10):
    if x == target:
        print(f'Found {target}!')
        found = True
        break

# Search with index
items = ['apple', 'banana', 'cherry']
search_term = 'banana'
index = -1
for i in range(len(items)):
    if items[i] == search_term:
        index = i
        break
print(f'Found at index {index}')

# Count occurrences
data = [1, 2, 2, 3, 2, 4]
count = 0
for x in data:
    if x == 2:
        count += 1
print(f'Found 2 appears {count} times')
```

## Pattern 4: Transformation (Modify Items)

```python
# Transformation pattern: apply operation to each item
numbers = [1, 2, 3, 4]
squared = []
for x in numbers:
    squared.append(x ** 2)
print(squared)  # [1, 4, 9, 16]

# Transform strings
words = ['hello', 'world']
uppercase = []
for word in words:
    uppercase.append(word.upper())
print(uppercase)  # ['HELLO', 'WORLD']
```

## Pattern 5: Processing with Index

```python
# Processing with index
items = ['apple', 'banana', 'cherry']
for i in range(len(items)):
    print(f'{i}: {items[i]}')

# With enumerate (preferred)
for i, item in enumerate(items):
    print(f'{i}: {item}')
```

## Real-World Examples

```python
# Grade calculator (accumulation)
scores = [85, 92, 78, 88, 95]
total = 0
for score in scores:
    total += score
average = total / len(scores)
print(f'Average: {average}')

# Filter valid emails (filtering)
emails = ['alice@example.com', 'invalid-email', 'bob@domain.org']
valid = []
for email in emails:
    if '@' in email and '.' in email.split('@')[1]:
        valid.append(email)
print(valid)

# Find max value (searching)
numbers = [45, 23, 89, 12, 56]
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(f'Max: {max_val}')
```

## Common Errors with Example Code

### Error 1: Not initializing accumulator properly
```python
# WRONG: Not initializing total
for x in [1, 2, 3]:
    total += x  # NameError! total doesn't exist

# CORRECT: Initialize before loop
total = 0
for x in [1, 2, 3]:
    total += x
print(total)

# ALSO WRONG: Wrong initial value
product = 0  # Should be 1 for multiplication!
for x in [2, 3, 4]:
    product *= x  # Result will always be 0!

# CORRECT:
product = 1
for x in [2, 3, 4]:
    product *= x
```

### Error 2: Comparing in filtering incorrectly
```python
# WRONG: Using assignment = instead of comparison ==
evens = []
for x in range(10):
    if x = 2:  # SyntaxError!
        evens.append(x)

# CORRECT: Use ==
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
```

### Error 3: Break doesn't break outer loop when nested
```python
# WRONG: Break only breaks inner loop
found = False
for group in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    for num in group:
        if num == 5:
            break  # Only breaks inner loop!
    if found:
        break

# CORRECT: Use a flag variable
found = False
for group in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    for num in group:
        if num == 5:
            found = True
            break
    if found:
        break

# OR: Use a function
def find_number(groups, target):
    for group in groups:
        for num in group:
            if num == target:
                return True
    return False
```

### Error 4: Modifying list while iterating
```python
# WRONG: Deleting from list while iterating
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # Skip elements!

# CORRECT: Iterate over copy or create new list
items = [1, 2, 3, 4, 5]
for item in items[:]:  # [:] creates copy
    if item % 2 == 0:
        items.remove(item)

# BETTER: Create new list with filtering
items = [1, 2, 3, 4, 5]
items = [x for x in items if x % 2 != 0]
```

### Error 5: Counting/searching without proper conditions
```python
# WRONG: Count wrong element
data = ['a', 'b', 'a', 'c', 'a']
count = 0
for x in data:
    if x == 'a':
        count += 1
    print(count)  # Prints every iteration! (not what you want)

# CORRECT: Print after loop
count = 0
for x in data:
    if x == 'a':
        count += 1
print(count)  # 3

# WRONG: Not resetting accumulator in multiple searches
total = 0
for list_item in [[1, 2, 3], [4, 5, 6]]:
    for item in list_item:
        total += item
print(total)  # 21 (correct, but if you meant per-list sums, wrong!)

# CORRECT: If you want per-list totals
for list_item in [[1, 2, 3], [4, 5, 6]]:
    total = 0  # Reset for each list
    for item in list_item:
        total += item
    print(total)  # 6, then 15
```

## Exercises by Bloom Level

- **Remember**: Write a sum loop. Write a filtering loop.
- **Understand**: What's accumulation? What's filtering?
- **Apply**: Filter a list of numbers by condition.
- **Analyze**: Compare patterns for different tasks.
- **Create**: Combine multiple patterns in one program.

## Related Concepts
- [[Python - Loops - For Loop Basics]]
- [[Python - Loops - Loop Control (Break & Continue)]]
- [[Python - Loops - Enumerate & Zip]]
- [[Python - Lists - List Comprehension]]

## MOC
- Parent: [[Python - Loops (MOC)]]
