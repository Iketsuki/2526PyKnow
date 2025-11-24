---
tags: [python, functions, lambda]
moc: [[Python - Functions (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: lambda syntax."
  - "Understand: when to use lambdas."
  - "Apply: use with map, filter, sort."
---

# Python - Functions - Lambda Functions

## Concept
**Lambda** — tiny unnamed function. Syntax: `lambda params: expression`. One line, one expression, returns automatically.

## Basic Lambda

```python
# Regular function
def add(a, b):
    return a + b

# Lambda equivalent
add_lambda = lambda a, b: a + b

print(add(3, 5))  # 8
print(add_lambda(3, 5))  # 8
```

## When to Use Lambda?

Usually **not** for simple cases (just use `def`). Lambda is useful when:
1. Passing function as argument
2. Simple one-liner
3. Don't need to reuse the function

## Lambda with map()

**map()** — apply function to each item in list.

```python
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Double each
doubled = list(map(lambda x: x*2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
```

## Lambda with filter()

**filter()** — keep items where function returns True.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Keep only > 5
big = list(filter(lambda x: x > 5, numbers))
print(big)  # [6, 7, 8, 9, 10]
```

## Lambda with sort()

**sort()** with `key=` parameter — sort by custom rule.

```python
students = [
    ('Alice', 90),
    ('Bob', 75),
    ('Charlie', 85)
]

# Sort by score (second element)
sorted_students = sorted(students, key=lambda s: s[1])
print(sorted_students)
# [('Bob', 75), ('Charlie', 85), ('Alice', 90)]

# Reverse sort
sorted_desc = sorted(students, key=lambda s: s[1], reverse=True)
print(sorted_desc)
# [('Alice', 90), ('Charlie', 85), ('Bob', 75)]
```

## Real-World: Sorting Names

```python
names = ['Charlie', 'Alice', 'Bob', 'David']

# Sort by length
by_length = sorted(names, key=lambda x: len(x))
print(by_length)  # ['Bob', 'Alice', 'Charlie', 'David']

# Sort by reverse alphabetical
reverse_alpha = sorted(names, key=lambda x: x[::-1])
print(reverse_alpha)
```

## Real-World: Process Data

```python
# List of prices
prices = [10.50, 5.99, 20.00, 3.25]

# Add 10% tax
with_tax = list(map(lambda p: p * 1.10, prices))
print(with_tax)  # [11.55, 6.589, 22.0, 3.575]

# Find expensive (> $15)
expensive = list(filter(lambda p: p > 15, prices))
print(expensive)  # [20.00]
```

## Lambda vs List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

# Lambda with map
result1 = list(map(lambda x: x**2, numbers))

# List comprehension (usually clearer)
result2 = [x**2 for x in numbers]

print(result1)  # [1, 4, 9, 16, 25]
print(result2)  # [1, 4, 9, 16, 25]

# List comprehension often preferred (more Pythonic)
```

## When NOT to Use Lambda

```python
# DON'T: Complex logic
numbers = [1, 2, 3, 4, 5]
# bad_result = map(lambda x: x**2 if x % 2 == 0 else x, numbers)

# DO: Use def for readability
def process(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return x

result = list(map(process, numbers))
```

## Lambda with Multiple Arguments

```python
# Lambda with 2+ arguments (rare)
multiply = lambda a, b: a * b
print(multiply(3, 4))  # 12

# Use in sorted
pairs = [(1, 2), (3, 1), (2, 2)]
by_first = sorted(pairs, key=lambda p: p[0])
by_second = sorted(pairs, key=lambda p: p[1])
print(by_first)  # [(1, 2), (2, 2), (3, 1)]
print(by_second)  # [(3, 1), (1, 2), (2, 2)]
```

## Exercises by Bloom Level
- Remember: What does `lambda` do?
- Understand: Why use lambda over def?
- Apply: Use map() with lambda to double list.
- Analyze: Compare lambda with list comprehension.
- Create: Build custom sort (e.g., by score descending).

## Common Errors with Example Code

1) Lambda with multiple statements → Can't do multi-line inside lambda (use `def` instead)

WRONG
# Trying to put 2+ statements in lambda:
# f = lambda x: x*2; print(x)  # SyntaxError!

CORRECT
def double_and_print(x):
    result = x * 2
    print(result)
    return result

double_and_print(5)  # 10

2) Forgetting `list()` with map/filter → Returns iterator, not list in Python 3

WRONG
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(squared)  # <map object at 0x...> (not a list!)
print(squared[0])  # TypeError: 'map' object is not subscriptable

CORRECT
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25] (actual list)
print(squared[0])  # 1

3) Using lambda when `def` is clearer → Reduces readability for complex logic

WRONG
# Confusing lambda with conditionals:
result = list(map(lambda x: x**2 if x % 2 == 0 else x*3, numbers))

CORRECT
def custom_transform(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return x * 3

result = list(map(custom_transform, numbers))  # Much clearer!

## Related Concepts
- [[Python - Functions - Parameters & Return Values]]
- [[Python - Lists - Common Patterns]]
- [[Python - Lists - List Comprehension]]

## MOC
- Parent: [[Python - Functions (MOC)]]
