---
tags: [python, exercises, debugging, finally]
difficulty: Beginner
---

# Python - Debugging - Finally Blocks — Exercises

See concept: [[Python - Debugging - Finally Blocks]]
GitHub link: [Python - Debugging - Finally Blocks](./Python%20-%20Debugging%20-%20Finally%20Blocks.md)

## Quick syntax fixes

1) Broken: resource not closed on error
```python
f = open('x.txt')
data = f.read()
```
<details><summary>Answer</summary>

```python
try:
    f = open('x.txt')
    data = f.read()
finally:
    f.close()
```
Explanation: `finally` always runs to close resources.
</details>

2) Broken: using finally but not catching errors
```python
try:
    x = 1/0
finally:
    print('done')
```
<details><summary>Answer</summary>

```python
try:
    x = 1/0
except ZeroDivisionError:
    print('error')
finally:
    print('done')
```
Explanation: `except` handles error, `finally` always runs.
</details>

3) Broken: forgetting finally when opening file
```python
f = open('x.txt')
data = f.read()
# later error
```
<details><summary>Answer</summary>

```python
try:
    f = open('x.txt')
    data = f.read()
finally:
    f.close()
```
Explanation: Put cleanup in `finally` so it runs even on error.
</details>

---

## Easy

a) Run a try/finally where finally prints 'done'.

Starter code:
```python
# TODO: use try and finally
pass
```
<details><summary>Answer</summary>

```python
try:
    x = 1
finally:
    print('done')
```
Explanation: `finally` runs after try block.
</details>

b) Open a file, read first line, ensure it closes in finally.

Starter code:
```python
# TODO: open file and close in finally
pass
```
<details><summary>Answer</summary>

```python
try:
    f = open('test.txt')
    line = f.readline()
finally:
    f.close()
```
Explanation: Closing file in finally prevents leaks.
</details>

---

## Medium

a) Show finally runs even if exception occurs; print 'ok' in except and 'done' in finally.

Starter code:
```python
# TODO: add try/except/finally
pass
```
<details><summary>Answer</summary>

```python
try:
    x = 1/0
except ZeroDivisionError:
    print('ok')
finally:
    print('done')
```
Explanation: except handles, finally still runs.
</details>

b) Use finally to ensure a variable `closed = True` after try.

Starter code:
```python
closed = False
# TODO: set closed True in finally
pass
```
<details><summary>Answer</summary>

```python
closed = False
try:
    x = 1
finally:
    closed = True
print(closed)
```
Explanation: finally can update state even on error.
</details>

---

## Hard

Write code that opens a file, tries to convert first line to int, returns 0 on error, and always closes file.

Starter code:
```python
def safe_first_int(fname):
    # TODO: open, try convert, finally close
    pass

print(safe_first_int('data.txt'))
```
<details><summary>Answer</summary>

```python
def safe_first_int(fname):
    f = open(fname)
    try:
        line = f.readline()
        return int(line)
    except Exception:
        return 0
    finally:
        f.close()

print(safe_first_int('data.txt'))
```
Explanation: finally ensures close, except returns fallback.
</details>
