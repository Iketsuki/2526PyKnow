---
tags: [python, exercises, performance, profiling]
difficulty: Beginner
---

# Python - Performance - Profiling Basics — Exercises

See concept: [[Python - Performance - Profiling Basics]]
GitHub link: [Python - Performance - Profiling Basics](./Python%20-%20Performance%20-%20Profiling%20Basics.md)

## Quick syntax fixes

1) Broken: using print timing without storing time
```python
start = time.time()
print('done')
print(time.time() - start)
```
<details><summary>Answer</summary>

```python
import time
start = time.time()
print('done')
print(time.time() - start)
```
Explanation: import `time` first.
</details>

2) Broken: confusing profiler output
```text
# using cProfile requires running as script
```
<details><summary>Answer</summary>

Use `python -m cProfile script.py` to get profiling output.

Explanation: run the profiler as module.
</details>

3) Broken: not closing file before timing IO
```python
f = open('data.txt')
start = time.time()
data = f.read()
```
<details><summary>Answer</summary>

```python
import time
with open('data.txt') as f:
    start = time.time()
    data = f.read()
```
Explanation: use `with` to manage file timing correctly.
</details>

---

## Easy

a) Time how long a loop of 1000 iterations takes using `time.time()` and print the seconds.

Starter code:
```python
import time
start = time.time()
for i in range(1000):
    pass
# TODO: print elapsed
pass
```
<details><summary>Answer</summary>

```python
import time
start = time.time()
for i in range(1000):
    pass
print(time.time() - start)
```
Explanation: subtract start from current time.
</details>

b) Run a small function 1000 times and print total time.

Starter code:
```python
import time
def work():
    s = 0
    for i in range(10):
        s += i
start = time.time()
for _ in range(1000):
    work()
# TODO: print time
pass
```
<details><summary>Answer</summary>

```python
import time
def work():
    s = 0
    for i in range(10):
        s += i
start = time.time()
for _ in range(1000):
    work()
print(time.time() - start)
```
Explanation: measure repeated function calls for a simple profile.
</details>

---

## Medium

a) Use `cProfile` via `python -m cProfile -s time script.py` to run a small script. (Explain how to run, one line).

Starter answer expected (one line):
```text
# example run command
```
<details><summary>Answer</summary>

Run: `python -m cProfile -s time script.py`

Explanation: `-s time` sorts output by time spent.
</details>

b) Write two functions, one slower and one faster; run each once with `time.time()` and print which is faster.

Starter code:
```python
import time
def slow(n):
    s = 0
    for i in range(n):
        for j in range(n):
            s += 1
    return s

def fast(n):
    return n*n

# TODO: time and print 'fast' or 'slow'
pass
```
<details><summary>Answer</summary>

```python
import time
def slow(n):
    s = 0
    for i in range(n):
        for j in range(n):
            s += 1
    return s

def fast(n):
    return n*n

n = 200
start = time.time(); slow(n); t1 = time.time() - start
start = time.time(); fast(n); t2 = time.time() - start
print('fast' if t2 < t1 else 'slow')
```
Explanation: compare timings to see which is quicker.
</details>

---

## Hard

Describe one simple change to make a program faster (one sentence).

Starter prompt:
```text
# write one sentence
```
<details><summary>Answer</summary>

Replace repeated work inside a loop with a precomputed value or formula.

Explanation: avoid repeated heavy work to improve speed.
</details>
