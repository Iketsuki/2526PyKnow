---
tags: [python, exercises, fileio, paths]
difficulty: Beginner
---

# Python - File IO - Working with Paths — Exercises

See concept: [[Python - File IO - Working with Paths]]
GitHub link: [Python - File IO - Working with Paths](./Python%20-%20File%20IO%20-%20Working%20with%20Paths.md)

## Quick syntax fixes

1) Broken: joining paths with +
```python
path = 'data' + '/' + 'file.txt'
```
<details><summary>Answer</summary>

```python
import os
path = os.path.join('data','file.txt')
```
Explanation: use os.path.join for cross-platform paths.
</details>

2) Broken: not using os.path.exists
```python
f = open('dir/file.txt')
```
<details><summary>Answer</summary>

```python
import os
if os.path.exists('dir/file.txt'):
    f = open('dir/file.txt')
```
Explanation: check existence before opening.
</details>

3) Broken: using backslash string on Windows without raw string
```python
path = 'C:\new\file.txt'
```
<details><summary>Answer</summary>

```python
path = r'C:\new\file.txt'
```
Explanation: raw strings avoid escape surprises.
</details>

---

## Easy

a) Build a path from folder and filename and print it.

Starter code:
```python
folder = 'data'
name = 'a.txt'
# TODO: join and print
pass
```
<details><summary>Answer</summary>

```python
import os
folder = 'data'
name = 'a.txt'
print(os.path.join(folder, name))
```
Explanation: os.path.join combines parts safely.
</details>

b) Check if `file.txt` exists and print 'yes' or 'no'.

Starter code:
```python
# TODO: check and print
pass
```
<details><summary>Answer</summary>

```python
import os
print('yes' if os.path.exists('file.txt') else 'no')
```
Explanation: os.path.exists reports presence.
</details>

---

## Medium

a) Given a path, print its directory and base name.

Starter code:
```python
path = 'a/b/c.txt'
# TODO: print dir and base
pass
```
<details><summary>Answer</summary>

```python
import os
path = 'a/b/c.txt'
print(os.path.dirname(path), os.path.basename(path))
```
Explanation: dirname and basename split paths.
</details>

b) Create a folder `out` if it does not exist.

Starter code:
```python
# TODO: make out dir if missing
pass
```
<details><summary>Answer</summary>

```python
import os
os.makedirs('out', exist_ok=True)
```
Explanation: makedirs with exist_ok avoids errors.
</details>

---

## Hard

Write a function that returns the absolute path of a filename in the current script folder.

Starter code:
```python
import os
def local_path(fname):
    # TODO: return absolute path in script folder
    pass

print(local_path('data.txt'))
```
<details><summary>Answer</summary>

```python
import os
def local_path(fname):
    base = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(base, fname))

print(local_path('data.txt'))
```
Explanation: join with script dir and abspath for full path.
</details>
