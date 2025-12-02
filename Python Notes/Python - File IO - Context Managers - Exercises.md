---
tags: [python, exercises, fileio]
difficulty: Beginner
---

# Python - File IO - Context Managers — Exercises

See concept: [[Python - File IO - Context Managers]]
GitHub link: [Python - File IO - Context Managers](./Python%20-%20File%20IO%20-%20Context%20Managers.md)

## Quick syntax fixes

1) Broken: not using with
```python
f = open('x.txt')
data = f.read()
f.close()
```
<details><summary>Answer</summary>

```python
with open('x.txt') as f:
    data = f.read()
```
Explanation: `with` is clearer and safer.
</details>

2) Broken: exception stops close call
```python
f = open('x.txt')
raise Exception()
f.close()
```
<details><summary>Answer</summary>

```python
with open('x.txt') as f:
    raise Exception()
```
Explanation: `with` ensures file is closed even on exception.
</details>

3) Broken: forgetting to use mode
```python
with open('x.txt') as f:
    f.write('a')
```
<details><summary>Answer</summary>

```python
with open('x.txt','w') as f:
    f.write('a')
```
Explanation: specify correct mode for writing.
</details>

---

## Easy

a) Use `with` to write 'hello' to file.

Starter code:
```python
# TODO: write using with
pass
```
<details><summary>Answer</summary>

```python
with open('out.txt','w') as f:
    f.write('hello')
```
Explanation: `with` handles close automatically.
</details>

b) Use `with` to read and print first line.

Starter code:
```python
# TODO: read first line safely
pass
```
<details><summary>Answer</summary>

```python
with open('in.txt') as f:
    print(f.readline().strip())
```
Explanation: `with` is used for safe reads.
</details>

---

## Medium

a) Write lines from a list to a file using `with` and return number written.

Starter code:
```python
lines = ['a','b']
# TODO: write and print count
pass
```
<details><summary>Answer</summary>

```python
lines = ['a','b']
with open('out.txt','w') as f:
    for line in lines:
        f.write(line + '\n')
print(len(lines))
```
Explanation: `with` + iteration for writes.
</details>

b) Copy a file using `with` for both read and write.

Starter code:
```python
# TODO: copy in.txt to out.txt
pass
```
<details><summary>Answer</summary>

```python
with open('in.txt') as src, open('out.txt','w') as dst:
    for line in src:
        dst.write(line)
```
Explanation: `with` can open multiple files.
</details>

---

## Hard

Write a context manager using `contextlib` that times how long a block takes and prints it.

Starter code:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    # TODO: implement
    pass

with timer():
    for i in range(1000000):
        pass
```
<details><summary>Answer</summary>

```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        print('elapsed', time.time() - start)

with timer():
    for i in range(1000000):
        pass
```
Explanation: Yield inside contextmanager and use finally to report time.
</details>
