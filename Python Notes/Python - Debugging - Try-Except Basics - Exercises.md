---
tags: [python, exercises, debugging, try-except]
difficulty: Beginner
---

# Python - Debugging - Try-Except Basics — Exercises

See concept: [[Python - Debugging - Try-Except Basics]]
GitHub link: [Python - Debugging - Try-Except Basics](./Python%20-%20Debugging%20-%20Try-Except%20Basics.md)

## Quick syntax fixes

1) Broken: wrong exception name
```python
try:
    x = 1/0
except Error:
    print('err')
```
<details><summary>Answer</summary>

```python
try:
    x = 1/0
except ZeroDivisionError:
    print('err')
```
Explanation: Use the correct exception class.
</details>

2) Broken: missing try for risky code
```python
x = int('a')
```
<details><summary>Answer</summary>

```python
try:
    x = int('a')
except ValueError:
    x = 0
```
Explanation: Use try/except around code that can fail.
</details>

3) Broken: catching too broadly
```python
try:
    x = 1/0
except Exception:
    print('oops')
```
<details><summary>Answer</summary>

```python
try:
    x = 1/0
except ZeroDivisionError:
    print('oops')
```
Explanation: Prefer specific exceptions for clarity.
</details>

---

## Easy

a) Try to convert input to int, print 0 on ValueError.

Starter code:
```python
s = input()
# TODO: convert or print 0
pass
```
<details><summary>Answer</summary>

```python
s = input()
try:
    print(int(s))
except ValueError:
    print(0)
```
Explanation: except handles conversion errors.
</details>

b) Open a file name from input and print first line or 'no file'.

Starter code:
```python
fname = input()
# TODO: open file safely
pass
```
<details><summary>Answer</summary>

```python
fname = input()
try:
    with open(fname) as f:
        print(f.readline())
except FileNotFoundError:
    print('no file')
```
Explanation: Handle missing file with except.
</details>

---

## Medium

a) Read two numbers, print division, handle ZeroDivisionError.

Starter code:
```python
a = int(input())
b = int(input())
# TODO: divide with try/except
pass
```
<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
try:
    print(a / b)
except ZeroDivisionError:
    print('cannot divide')
```
Explanation: except catches division by zero.
</details>

b) Try reading json from input and print keys or 'bad'.

Starter code:
```python
import json
s = input()
# TODO: parse json and print keys
pass
```
<details><summary>Answer</summary>

```python
import json
s = input()
try:
    data = json.loads(s)
    print(list(data.keys()))
except json.JSONDecodeError:
    print('bad')
```
Explanation: Catch JSON errors explicitly.
</details>

---

## Hard

Write a function that reads a filename and returns integer count of lines, or -1 on any error.

Starter code:
```python
def count_lines(fname):
    # TODO: open, count, handle errors
    pass

print(count_lines('data.txt'))
```
<details><summary>Answer</summary>

```python
def count_lines(fname):
    try:
        with open(fname) as f:
            return sum(1 for _ in f)
    except Exception:
        return -1

print(count_lines('data.txt'))
```
Explanation: Use except to return fallback for any IO error.
</details>
