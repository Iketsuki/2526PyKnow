---
tags: [python, exercises, performance, big-o]
difficulty: Beginner
---

# Python - Performance - Big O basics — Exercises

See concept: [[Python - Performance - Big O basics]]
GitHub link: [Python - Performance - Big O basics](./Python%20-%20Performance%20-%20Big%20O%20basics.md)

## Quick syntax fixes

1) Broken: confusing constant-time vs linear example
```python
for i in range(5):
    print('hello')
```
<details><summary>Answer</summary>

This is O(n) where n=5, because work grows with the loop.

Explanation: the loop repeats work for each item.
</details>

2) Broken: nested loops mislabelled
```python
for i in range(n):
    for j in range(m):
        print(i, j)
```
<details><summary>Answer</summary>

This is O(n*m), often written O(n^2) if n ~ m.

Explanation: two loops multiply work.
</details>

3) Broken: counting only operations, ignoring input size
```text
# bad note: program is fast because it uses math
```
<details><summary>Answer</summary>

Performance depends on input size and algorithm, not only language features.

Explanation: algorithmic complexity matters.
</details>

---

## Easy

a) Which of these grows faster as `n` increases: `n` or `n*n`? Write the answer as `print('n*n')`.

Starter code:
```python
# TODO: print which grows faster
pass
```
<details><summary>Answer</summary>

```python
print('n*n')
```
Explanation: `n*n` (quadratic) grows faster than linear `n`.
</details>

b) For a loop `for i in range(n): print(i)`, state its complexity by printing `print('O(n)')`.

Starter code:
```python
# TODO: print complexity
pass
```
<details><summary>Answer</summary>

```python
print('O(n)')
```
Explanation: one loop over n is linear time.
</details>

---

## Medium

a) Time two small functions for n=1000 and print which is faster. Use `time.time()`.

Starter code:
```python
import time

def f1(n):
    s = 0
    for i in range(n):
        s += i
    return s

def f2(n):
    return n*(n-1)//2

# TODO: time f1 and f2 for n=1000 and print 'f2' if f2 is faster
pass
```
<details><summary>Answer</summary>

```python
import time

def f1(n):
    s = 0
    for i in range(n):
        s += i
    return s

def f2(n):
    return n*(n-1)//2

n = 1000
start1 = time.time()
f1(n)
t1 = time.time() - start1
start2 = time.time()
f2(n)
t2 = time.time() - start2
print('f2' if t2 < t1 else 'f1')
```
Explanation: arithmetic formula is faster than loop.
</details>

b) For a list of size n, is indexing list[5] O(1) or O(n)? Print the answer.

Starter code:
```python
# TODO: print 'O(1)'
pass
```
<details><summary>Answer</summary>

```python
print('O(1)')
```
Explanation: indexing by position is constant time.
</details>

---

## Hard

Explain in one sentence why reducing an algorithm from O(n^2) to O(n) matters for large `n`.

Starter prompt:
```text
# type one sentence
```
<details><summary>Answer</summary>

Reducing O(n^2) to O(n) makes the program much faster as input grows, because work changes from growing with the square of `n` to growing linearly.

Explanation: lower order of growth scales much better for large inputs.
</details>
