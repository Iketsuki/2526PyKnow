---
tags: [python, exercises, debugging, strategies]
difficulty: Beginner
---

# Python - Debugging - Debugging Strategies — Exercises

See concept: [[Python - Debugging - Debugging Strategies]]
GitHub link: [Python - Debugging - Debugging Strategies](./Python%20-%20Debugging%20-%20Debugging%20Strategies.md)

## Quick syntax fixes

1) Broken: forgot print to check value
```python
# Broken
value = 5
value
```
<details><summary>Answer</summary>

```python
# Fixed
value = 5
print(value)
```
Explanation: Use print() to see values while debugging.
</details>

2) Broken: too large function, hard to read
```python
# Broken
def f():
    a=1;b=2;c=3;d=4
```
<details><summary>Answer</summary>

```python
# Fixed (refactor example)
def f():
    a = 1
    b = 2
    c = 3
    d = 4
```
Explanation: Break code into small lines/functions for clarity.
</details>

3) Broken: no error handling
```python
# Broken
open('nofile.txt').read()
```
<details><summary>Answer</summary>

```python
# Fixed
try:
    open('nofile.txt').read()
except FileNotFoundError:
    print('file missing')
```
Explanation: Add small try/except when reading files while debugging.
</details>

---

## Easy

a) Insert a `print` to show variable `x` inside a function to debug its value.

Starter code:
```python
def f(x):
    # TODO: print x, then return x*2
    pass
print(f(3))
```
<details><summary>Answer</summary>

```python
def f(x):
    print('x=', x)
    return x * 2
print(f(3))
```
Explanation: Print helps see values during execution.
</details>

b) Use small test calls at bottom of file to run a function and check output.

Starter code:
```python
def add(a,b):
    return a+b
# TODO: add a test call that prints add(1,2)
pass
```
<details><summary>Answer</summary>

```python
def add(a,b):
    return a+b
print(add(1,2))
```
Explanation: Simple test calls help verify behavior.
</details>

---

## Medium

a) Use try/except to catch an error and print the stack trace using `traceback` module.

Starter code:
```python
import traceback
def bad():
    1/0
# TODO: call bad and print traceback on error
pass
```
<details><summary>Answer</summary>

```python
import traceback
def bad():
    1/0
try:
    bad()
except Exception:
    traceback.print_exc()
```
Explanation: Use traceback to see full error info.
</details>

b) Break a long function into two smaller functions to make debugging easier (fill in TODOs).

Starter code:
```python
def step1(x):
    return x+1
def step2(x):
    return x*2
def process(x):
    # TODO: call step1 then step2
    pass
print(process(3))
```
<details><summary>Answer</summary>

```python
def step1(x):
    return x+1
def step2(x):
    return x*2
def process(x):
    a = step1(x)
    return step2(a)
print(process(3))
```
Explanation: Smaller functions are simpler to test.
</details>

---

## Hard

Write a small test that asserts `f(2)==4` and prints 'ok' or 'fail'.

Starter code:
```python
def f(x):
    return x*2
# TODO: write simple assert test and print result
pass
```
<details><summary>Answer</summary>

```python
def f(x):
    return x*2
try:
    assert f(2) == 4
    print('ok')
except AssertionError:
    print('fail')
```
Explanation: Simple assertions help catch wrong outputs.
</details>
