---
tags: [python, exercises, debugging, errors]
difficulty: Beginner
---

# Python - Debugging - Common Error Types — Exercises

See concept: [[Python - Debugging - Common Error Types]]
GitHub link: [Python - Debugging - Common Error Types](./Python%20-%20Debugging%20-%20Common%20Error%20Types.md)

## Quick syntax fixes

1) Broken: NameError
```python
# Broken
print(x)
```
<details><summary>Answer</summary>

```python
# Fixed
x = 1
print(x)
```
Explanation: Define variables before use.
</details>

2) Broken: TypeError
```python
# Broken
print(1 + '2')
```
<details><summary>Answer</summary>

```python
# Fixed
print(1 + int('2'))
```
Explanation: Convert types before operations.
</details>

3) Broken: IndexError
```python
# Broken
lst = [1]
print(lst[1])
```
<details><summary>Answer</summary>

```python
# Fixed
lst = [1]
print(lst[0])
```
Explanation: Use valid indexes (0..len-1).
</details>

---

## Easy

a) Fix a code that causes ValueError when converting 'x' to int.

Starter code:
```python
s = 'x'
# TODO: try converting and handle error by printing 'bad'
pass
```
<details><summary>Answer</summary>

```python
s = 'x'
try:
    print(int(s))
except ValueError:
    print('bad')
```
Explanation: Use try/except to catch conversion errors.
</details>

b) Show how to avoid ZeroDivisionError by checking denominator.

Starter code:
```python
a = 1
b = 0
# TODO: print a/b or 'bad'
pass
```
<details><summary>Answer</summary>

```python
a = 1
b = 0
if b == 0:
    print('bad')
else:
    print(a / b)
```
Explanation: Check denominator before dividing.
</details>

---

## Medium

a) Write code that catches KeyError when accessing missing dict key and prints 'missing'.

Starter code:
```python
d = {'a':1}
# TODO: print d['b'] or 'missing'
pass
```
<details><summary>Answer</summary>

```python
d = {'a':1}
try:
    print(d['b'])
except KeyError:
    print('missing')
```
Explanation: Use try/except for dict access.
</details>

b) Recover from FileNotFoundError when opening a file and print 'no file'.

Starter code:
```python
fname = 'nope.txt'
# TODO: try open and print 'no file' on failure
pass
```
<details><summary>Answer</summary>

```python
fname = 'nope.txt'
try:
    f = open(fname)
    f.close()
except FileNotFoundError:
    print('no file')
```
Explanation: Catch file errors to avoid crash.
</details>

---

## Hard

Write a helper that runs a function and returns (True,result) or (False,'error') on exception.

Starter code:
```python
def run_safe(fn):
    # TODO: run fn() and return (True, value) or (False, 'error')
    pass
def good():
    return 1
print(run_safe(good))
```
<details><summary>Answer</summary>

```python
def run_safe(fn):
    try:
        return (True, fn())
    except Exception:
        return (False, 'error')
def good():
    return 1
print(run_safe(good))
```
Explanation: Use try/except to convert exceptions into values.
</details>
