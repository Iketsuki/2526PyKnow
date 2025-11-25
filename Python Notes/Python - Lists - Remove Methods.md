---
tags: [python, lists, methods, remove]
moc: [[Python - Lists (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: .remove(), .pop(), .clear() syntax."
  - "Understand: when to use each removal method."
  - "Apply: safely remove items from lists."
---

# Python - Lists - Remove Methods

## Concept
Three ways to remove items from a list: `.remove()` removes by value, `.pop()` removes by index and returns the value, `.clear()` empties the list.

## .remove() — Remove by Value

```python
colors = ['red', 'blue', 'red', 'green']
colors.remove('red')  # Removes first occurrence
print(colors)  # ['blue', 'red', 'green']

# Raises ValueError if value not found
items = [1, 2, 3]
items.remove(5)  # ValueError: 5 is not in list
```

Safe usage with membership check:

```python
colors = ['red', 'blue', 'green']
if 'red' in colors:
    colors.remove('red')
else:
    print('Color not found')
```

## .pop() — Remove by Index

```python
colors = ['red', 'blue', 'green']
removed = colors.pop(1)  # Remove index 1
print(removed)  # 'blue'
print(colors)  # ['red', 'green']

# pop() without index removes last item
last = colors.pop()
print(last)  # 'green'
print(colors)  # ['red']

# pop(0) removes first
colors.pop(0)
print(colors)  # []
```

Raises IndexError if index doesn't exist:

```python
items = [1, 2, 3]
items.pop(10)  # IndexError: pop index out of range
```

## .clear() — Remove All Items

```python
colors = ['red', 'blue', 'green']
colors.clear()
print(colors)  # []
```

## Comparison: remove() vs pop()

```python
# .remove() — by value
items = ['a', 'b', 'c']
items.remove('b')  # Removes first 'b' found
print(items)  # ['a', 'c']

# .pop() — by index
items = ['a', 'b', 'c']
removed = items.pop(1)  # Remove index 1, return value
print(removed)  # 'b'
print(items)  # ['a', 'c']
```

## Common Errors with Example Code

1) Using remove() without checking if value exists

WRONG
```python
items = [1, 2, 3]
items.remove(5)  # ValueError: 5 is not in list
```

CORRECT
```python
items = [1, 2, 3]
if 5 in items:
    items.remove(5)
else:
    print('Value not found')
```

2) Using pop() with invalid index

WRONG
```python
items = [1, 2, 3]
item = items.pop(10)  # IndexError: pop index out of range
```

CORRECT
```python
items = [1, 2, 3]
if len(items) > 0:
    item = items.pop()  # Remove last safely
```

3) Modifying a list while iterating — skips items

WRONG
```python
nums = [1, 2, 3, 4]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)  # Modifying during iteration
print(nums)  # [1, 3] but logic is unreliable
```

CORRECT
```python
nums = [1, 2, 3, 4]
nums = [n for n in nums if n % 2 != 0]  # Use comprehension
print(nums)  # [1, 3]
```

## Real-World: Todo List

```python
todos = ['homework', 'practice', 'read']

# Mark complete (remove)
if 'practice' in todos:
    todos.remove('practice')

# Remove by position (pop)
todos.pop(0)  # Remove first item

print(todos)
```

## Related Concepts
- [[Python - Lists - Add Methods]]
- [[Python - Lists - Common Patterns]]

## MOC
- Parent: [[Python - Lists (MOC)]]
