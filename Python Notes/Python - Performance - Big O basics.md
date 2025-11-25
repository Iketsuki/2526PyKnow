---
tags: [python, performance]
moc: [[Python - Performance (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: common Big-O notations (O(1), O(n), O(n^2))."
  - "Understand: how algorithm complexity impacts scaling."
  - "Apply: pick simpler algorithms for small data and efficient ones for large data."
---

# Python - Performance - Big O basics

## Concept
Big O notation describes how runtime or memory grows with input size. Focus on common patterns: O(1), O(n), O(n log n), O(n^2).

## Example
```python
# O(n) example - linear scan
def contains(seq, x):
    for item in seq:
        if item == x:
            return True
    return False

# O(1) example - dict lookup
d = {'a': 1}
print(d.get('a'))  # O(1)
```

## Common Errors with Example Code

1) Assuming small constants don't matter → For large N, algorithmic complexity dominates

WRONG
# Using nested loops for large lists
for a in list1:
    for b in list2:
        process(a, b)  # O(n*m) - can be huge

CORRECT
# Use hashing or smarter algorithm to reduce complexity
s = set(list2)
for a in list1:
    if a in s:
        process(a, a)

2) Using list for membership tests repeatedly → O(n) each time

WRONG
for item in queries:
    if item in big_list:  # expensive O(n)
        pass

CORRECT
s = set(big_list)  # convert once O(n)
for item in queries:
    if item in s:  # O(1)
        pass

3) Premature optimization vs readability

WRONG
# Micro-optimized but unreadable code

CORRECT
# Prefer clear algorithms, then profile and optimize hotspots

## Profiling & Measurement (atomic)

Measure before you optimize. Use simple timing and a profiler to find hotspots. Keep profiling notes small and focused so learners can practice one tool at a time.

Example: quick timing with timeit

```python
import timeit

code = """
sum = 0
for i in range(1000):
    sum += i
"""

print(timeit.timeit(code, number=1000))
```

Example: cProfile for simple profiling

```python
import cProfile

def work(n=1000):
    s = 0
    for i in range(n):
        s += i
    return s

cProfile.run('work(10000)')
```

Atomic note: keep profiling focused — one tool per short note (timeit, cProfile, line_profiler).

## Related Concepts
- [[Python - Data Structures - When to use lists vs dicts]]
- [[Python - Performance - Profiling Basics]]

## MOC
- Parent: [[Python Fundamentals (MOC)]]
