---
tags: [python, exercises, io, errors]
difficulty: Beginner
---

# Python - IO - Error Handling in Input-Output — Exercises

See concept: [[Python - IO - Error Handling in Input-Output]]
GitHub link: [Python - IO - Error Handling in Input-Output](./Python%20-%20IO%20-%20Error%20Handling%20in%20Input-Output.md)

## Quick syntax fixes

1) Broken: not closing file
```python
# Broken
f = open('x.txt')
data = f.read()
```
<details><summary>Answer</summary>

```python
# Fixed
with open('x.txt') as f:
    data = f.read()
```
Explanation: Use `with` to ensure file is closed.
</details>

2) Broken: not handling FileNotFoundError
```python
# Broken
f = open('no.txt')
```
<details><summary>Answer</summary>

```python
# Fixed
try:
    with open('no.txt') as f:
        pass
except FileNotFoundError:
    print('no file')
```
Explanation: Catch file errors to avoid crash.
</details>

3) Broken: reading binary as text
```python
# Broken
with open('img.png', 'r') as f:
    data = f.read()
```
<details><summary>Answer</summary>

```python
# Fixed
with open('img.png', 'rb') as f:
    data = f.read()
```
Explanation: Use correct mode for binary files.
</details>

---

## Easy

a) Try to open a file and print 'missing' if not found.

Starter code:
```python
fname = 'nofile.txt'
# TODO: try open and print 'missing' on failure
pass
```
<details><summary>Answer</summary>

```python
fname = 'nofile.txt'
try:
    with open(fname) as f:
        pass
except FileNotFoundError:
    print('missing')
```
Explanation: Use try/except for file operations.
</details>

b) Read lines safely and print number of lines.

Starter code:
```python
fname = 'x.txt'
# TODO: read lines and print count or 'no file'
pass
```
<details><summary>Answer</summary>

```python
fname = 'x.txt'
try:
    with open(fname) as f:
        lines = f.readlines()
    print(len(lines))
except FileNotFoundError:
    print('no file')
```
Explanation: Protect file reading with try/except.
</details>

---

## Medium

a) Write function `read_int(fname)` that reads a file with one number and returns int or None on error.

Starter code:
```python
def read_int(fname):
    # TODO: read file and convert to int safely
    pass
print(read_int('x.txt'))
```
<details><summary>Answer</summary>

```python
def read_int(fname):
    try:
        with open(fname) as f:
            s = f.read().strip()
        return int(s)
    except Exception:
        return None
print(read_int('x.txt'))
```
Explanation: Combine file IO and conversion error handling.
</details>

b) Append a line to a file and handle errors.

Starter code:
```python
def append_line(fname, text):
    # TODO: append text or print 'err'
    pass
append_line('x.txt', 'hello')
```
<details><summary>Answer</summary>

```python
def append_line(fname, text):
    try:
        with open(fname, 'a') as f:
            f.write(text + '\n')
    except Exception:
        print('err')
append_line('x.txt', 'hello')
```
Explanation: Use append mode and catch write errors.
</details>

---

## Hard

Write a function that copies content from `src` to `dst` and returns True on success else False.

Starter code:
```python
def copy_file(src, dst):
    # TODO: return True on success else False
    pass
print(copy_file('a.txt','b.txt'))
```
<details><summary>Answer</summary>

```python
def copy_file(src, dst):
    try:
        with open(src, 'rb') as fsrc:
            data = fsrc.read()
        with open(dst, 'wb') as fdst:
            fdst.write(data)
        return True
    except Exception:
        return False
print(copy_file('a.txt','b.txt'))
```
Explanation: Read/write in binary for reliable copying; return status.
</details>
