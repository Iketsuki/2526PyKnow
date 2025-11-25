---
tags: [python, performance]
moc: [[Python - Performance (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: basic profiling tools (timeit, cProfile)."
  - "Understand: how to measure hotspots." 
  - "Apply: run a profiler and interpret simple output."
---

# Python - Performance - Profiling Basics

## Concept
Profiling measures where your program spends time. Start with small, focused measurements: `timeit` for micro-benchmarks and `cProfile` for whole-program hotspots.

## timeit (micro-benchmarks)
```python
import timeit
print(timeit.timeit("sum([i for i in range(100)])", number=10000))
```
Use `timeit` for tight snippets where function call overhead and constants matter.

## cProfile (whole-program)
```python
import cProfile

def work(n=10000):
    s = 0
    for i in range(n):
        s += i
    return s

cProfile.run('work(10000)')
```
Run cProfile to get function-by-function timings; focus on the top offenders.

## Atomic guidance
- Create one short note per tool (this file is one).
- For line-level detail, use `line_profiler` (separate atomic note).
- Always measure on realistic input sizes.

## Common Errors with Example Code
1) Measuring too small inputs → noisy results

WRONG
import timeit
print(timeit.timeit('sum(range(10))', number=1))  # too small

CORRECT
print(timeit.timeit('sum(range(10000))', number=1000))  # more stable

2) Profiling without isolating other work → background tasks skew results

WRONG
# Run profiler while other heavy apps are running

CORRECT
# Close other heavy processes or run multiple trials

## Related Concepts
- [[Python - Performance - Big O basics]]
- [[Python - Performance - Profiling Basics]]

## MOC
- Parent: [[Python - Performance (MOC)]]
