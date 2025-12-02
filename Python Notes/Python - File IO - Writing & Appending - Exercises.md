---
tags: [python, exercises, fileio]
difficulty: Beginner
---

# Python - File IO - Writing & Appending — Exercises

See concept: [[Python - File IO - Writing & Appending]]
GitHub link: [Python - File IO - Writing & Appending](./Python%20-%20File%20IO%20-%20Writing%20%26%20Appending.md)

## Quick syntax fixes

1) Broken: using 'w' when wanting to add
```python
with open('log.txt','w') as f:
    f.write('a')
```
<details><summary>Answer</summary>

```python
with open('log.txt','a') as f:
    f.write('a')
```
Explanation: 'a' appends instead of replacing file.
</details>

2) Broken: not adding newline
```python
with open('log.txt','a') as f:
    f.write('entry')
```
<details><summary>Answer</summary>

```python
with open('log.txt','a') as f:
    f.write('entry\n')
```
Explanation: add newline after appended entries.
</details>

3) Broken: opening file multiple times for append in loop
```python
for i in range(3):
    with open('log.txt','a') as f:
        f.write(str(i))
```
<details><summary>Answer</summary>

```python
with open('log.txt','a') as f:
    for i in range(3):
        f.write(str(i) + '\n')
```
Explanation: open once and write multiple lines.
</details>

---

## Easy

a) Append the text 'x' to `log.txt`.

Starter code:
```python
# TODO: append 'x'
pass
```
<details><summary>Answer</summary>

```python
with open('log.txt','a') as f:
    f.write('x\n')
```
Explanation: use append mode and newline.
</details>

b) Write two lines to `out.txt` replacing file.

Starter code:
```python
# TODO: write two lines
pass
```
<details><summary>Answer</summary>

```python
with open('out.txt','w') as f:
    f.write('first\n')
    f.write('second\n')
```
Explanation: use write mode to replace file.
</details>

---

## Medium

a) Add a timestamp line to `log.txt` on each run.

Starter code:
```python
import time
# TODO: append timestamp
pass
```
<details><summary>Answer</summary>

```python
import time
with open('log.txt','a') as f:
    f.write(time.ctime() + '\n')
```
Explanation: append formatted time string.
</details>

b) Read last 3 lines from a file (hint: read all and slice).

Starter code:
```python
# TODO: print last 3 lines
pass
```
<details><summary>Answer</summary>

```python
with open('big.txt') as f:
    lines = f.read().splitlines()
print(lines[-3:])
```
Explanation: splitlines and slice the list.
</details>

---

## Hard

Write a function that safely appends a line only if it is not already the last line in the file.

Starter code:
```python
def append_unique(fname, line):
    # TODO: append if not duplicate last line
    pass

append_unique('log.txt','x')
```
<details><summary>Answer</summary>

```python
def append_unique(fname, line):
    lines = []
    try:
        with open(fname) as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        pass
    if not lines or lines[-1] != line:
        with open(fname,'a') as f:
            f.write(line + '\n')

append_unique('log.txt','x')
```
Explanation: read last line then append if different.
</details>
