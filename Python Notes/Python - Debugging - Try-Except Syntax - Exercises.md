---
tags: [python, exercises, debugging, try-except]
difficulty: Beginner
---

# Python - Debugging - Try-Except Syntax — Exercises

See concept: [[Python - Debugging - Try-Except Syntax]]
GitHub link: [Python - Debugging - Try-Except Syntax](./Python%20-%20Debugging%20-%20Try-Except%20Syntax.md)

## Quick syntax fixes

1) Broken: except without colon
```python
try:
    x = 1
except
    print('e')
```
<details><summary>Answer</summary>

```python
try:
    x = 1
except Exception:
    print('e')
```
Explanation: `except` needs a colon and an optional exception.
</details>

2) Broken: wrong try/except order
```python
except ValueError:
    pass
try:
    x = int('a')
```
<details><summary>Answer</summary>

```python
try:
    x = int('a')
except ValueError:
    pass
```
Explanation: try must come before except.
</details>

3) Broken: using else but syntax wrong
```python
try:
    x = 1
else:
    print('ok')
```
<details><summary>Answer</summary>

```python
try:
    x = 1
except Exception:
    pass
else:
    print('ok')
```
Explanation: `else` must follow except blocks.
</details>

---

## Easy

a) Write try/except to catch ValueError when converting input to int.

Starter code:
```python
s = input()
# TODO: convert safely
pass
```
<details><summary>Answer</summary>

```python
s = input()
try:
    print(int(s))
except ValueError:
    print('bad')
```
Explanation: Correct try/except syntax for conversion.
</details>

b) Use try/except/else: print 'ok' in else when no error.

Starter code:
```python
try:
    x = int(input())
# TODO: add except and else
pass
```
<details><summary>Answer</summary>

```python
try:
    x = int(input())
except ValueError:
    print('bad')
else:
    print('ok')
```
Explanation: else runs when no exception occurs.
</details>

---

## Medium

a) Use try/except/finally to open and always close a file; print 'closed' in finally.

Starter code:
```python
# TODO: open, read, finally close
pass
```
<details><summary>Answer</summary>

```python
f = open('x.txt')
try:
    data = f.read()
except Exception:
    data = ''
finally:
    f.close()
    print('closed')
```
Explanation: finally always executes.
</details>

b) Use multiple except blocks for different errors.

Starter code:
```python
# TODO: handle ValueError and TypeError separately
pass
```
<details><summary>Answer</summary>

```python
try:
    x = int(input())
    y = x + 'a'
except ValueError:
    print('bad int')
except TypeError:
    print('type error')
```
Explanation: multiple except blocks handle specific errors.
</details>

---

## Hard

Write a function that divides two inputs and returns None on any error, use try/except with specific exceptions.

Starter code:
```python
def safe_div(a, b):
    # TODO: divide and handle errors
    pass

print(safe_div(4, 2))
```
<details><summary>Answer</summary>

```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None

print(safe_div(4, 2))
```
Explanation: handle expected exceptions explicitly.
</details>
