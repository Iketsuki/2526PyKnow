---
tags: [python, exercises, debugging, exceptions]
difficulty: Beginner
---

# Python - Debugging - Exception Handling — Exercises

See concept: [[Python - Debugging - Exception Handling]]
GitHub link: [Python - Debugging - Exception Handling](./Python%20-%20Debugging%20-%20Exception%20Handling.md)

## Quick syntax fixes

1) Broken: catching wrong exception type
```python
# Broken
try:
    x = int('a')
except FileNotFoundError:
    print('bad')
```
<details><summary>Answer</summary>

```python
# Fixed
try:
    x = int('a')
except ValueError:
    print('bad')
```
Explanation: Catch the correct exception type.
</details>

2) Broken: broad except hides errors
```python
# Broken
try:
    x=1/0
except:
    pass
```
<details><summary>Answer</summary>

```python
# Fixed
try:
    x=1/0
except ZeroDivisionError:
    print('divide by zero')
```
Explanation: Catch specific exceptions to avoid hiding bugs.
</details>

3) Broken: forgetting finally when closing resources
```python
# Broken
f = open('f.txt')
data = f.read()
```
<details><summary>Answer</summary>

```python
# Fixed
try:
    f = open('f.txt')
    data = f.read()
finally:
    try:
        f.close()
    except Exception:
        pass
```
Explanation: Use finally to ensure cleanup.
</details>

---

## Easy

a) Use try/except to catch ValueError when converting user input.

Starter code:
```python
user = 'a'
# TODO: try int(user) and print 'bad' on ValueError
pass
```
<details><summary>Answer</summary>

```python
user = 'a'
try:
    print(int(user))
except ValueError:
    print('bad')
```
Explanation: Handle common input errors with try/except.
</details>

b) Use `else` in try/except to run code only when no exception occurred.

Starter code:
```python
try:
    v = int('5')
except ValueError:
    print('bad')
# TODO: use else to print 'ok' when conversion works
pass
```
<details><summary>Answer</summary>

```python
try:
    v = int('5')
except ValueError:
    print('bad')
else:
    print('ok')
```
Explanation: `else` runs when no exception was raised.
</details>

---

## Medium

a) Write code that catches multiple exception types: ValueError and TypeError.

Starter code:
```python
def f(x):
    return int(x) + 1
# TODO: call f in try/except to catch ValueError and TypeError
pass
```
<details><summary>Answer</summary>

```python
def f(x):
    return int(x) + 1
try:
    print(f('a'))
except (ValueError, TypeError):
    print('bad')
```
Explanation: Catch a tuple of exceptions for similar handling.
</details>

b) Re-raise an exception after logging a message.

Starter code:
```python
try:
    1/0
except ZeroDivisionError:
    # TODO: print 'error' then re-raise
    pass
```
<details><summary>Answer</summary>

```python
try:
    1/0
except ZeroDivisionError:
    print('error')
    raise
```
Explanation: Re-raise to let caller handle the error after logging.
</details>

---

## Hard

Write a function `safe_open(fname)` that returns file content or None and does not crash on errors.

Starter code:
```python
def safe_open(fname):
    # TODO: return content or None
    pass
print(safe_open('nofile.txt'))
```
<details><summary>Answer</summary>

```python
def safe_open(fname):
    try:
        with open(fname, 'r') as f:
            return f.read()
    except Exception:
        return None
print(safe_open('nofile.txt'))
```
Explanation: Use try/except and `with` to safely open files.
</details>
