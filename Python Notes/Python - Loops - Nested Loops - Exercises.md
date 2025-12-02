---
tags: [python, exercises, loops]
difficulty: Beginner
---

# Python - Loops - Nested Loops — Exercises

See concept: [[Python - Loops - Nested Loops]]
GitHub link: [Python - Loops - Nested Loops](./Python%20-%20Loops%20-%20Nested%20Loops.md)

## Quick syntax fixes

1) Broken: inner loop uses wrong variable
```python
for i in range(2):
    for i in range(3):
        print(i)
```
<details><summary>Answer</summary>

```python
for i in range(2):
    for j in range(3):
        print(j)
```
Explanation: use different variables for nested loops.
</details>

2) Broken: missing indentation for inner loop
```python
for i in range(2):
for j in range(3):
    print(i,j)
```
<details><summary>Answer</summary>

```python
for i in range(2):
    for j in range(3):
        print(i,j)
```
Explanation: inner loop must be indented inside outer loop.
</details>

3) Broken: modifying list while iterating nested lists incorrectly
```python
lst = [[1],[2]]
for sub in lst:
    for x in sub:
        sub.remove(x)
```
<details><summary>Answer</summary>

```python
lst = [[1],[2]]
for sub in lst:
    for x in list(sub):
        sub.remove(x)
```
Explanation: iterate a copy when removing from inner list.
</details>

---

## Easy

a) Print pairs (i,j) for i in [1,2], j in [3,4].

Starter code:
```python
# TODO: nested loops
pass
```
<details><summary>Answer</summary>

```python
for i in [1,2]:
    for j in [3,4]:
        print(i,j)
```
Explanation: nested loops produce pairs.
</details>

b) Create a list of pairs using nested loops and append to result.

Starter code:
```python
# TODO: build pairs list
pass
```
<details><summary>Answer</summary>

```python
out = []
for i in [1,2]:
    for j in [3,4]:
        out.append((i,j))
print(out)
```
Explanation: append each pair inside inner loop.
</details>

---

## Medium

a) Multiply each element of [[1,2],[3,4]] by 2 using nested loops.

Starter code:
```python
mat = [[1,2],[3,4]]
# TODO: double values
pass
```
<details><summary>Answer</summary>

```python
mat = [[1,2],[3,4]]
for i in range(len(mat)):
    for j in range(len(mat[i])):
        mat[i][j] *= 2
print(mat)
```
Explanation: index into rows and columns to modify.
</details>

b) Flatten a 2D list using nested loops (not comprehension).

Starter code:
```python
mat = [[1,2],[3]]
# TODO: flatten
pass
```
<details><summary>Answer</summary>

```python
mat = [[1,2],[3]]
flat = []
for row in mat:
    for x in row:
        flat.append(x)
print(flat)
```
Explanation: nested loops flatten one level.
</details>

---

## Hard

Write nested loops that produce a 3x3 identity matrix as lists of lists.

Starter code:
```python
# TODO: build identity matrix
pass
```
<details><summary>Answer</summary>

```python
size = 3
mat = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(1 if i==j else 0)
    mat.append(row)
print(mat)
```
Explanation: inner loop builds each row with 1 on diagonal.
</details>
