---
tags: [python, exercises, loops, enumerate, zip]
difficulty: Beginner
---

# Python - Loops - Enumerate & Zip — Exercises

See concept: [[Python - Loops - Enumerate & Zip]]
GitHub link: [Python - Loops - Enumerate & Zip](./Python%20-%20Loops%20-%20Enumerate%20%26%20Zip.md)

## Quick syntax fixes

1) Broken: using `enumerate` but forgetting to unpack
```python
for i in enumerate(L):
    print(i)
```
<details><summary>Answer</summary>

```python
for i, v in enumerate(L):
    print(i, v)
```
Explanation: `enumerate` yields (index, value).
</details>

2) Broken: using `zip` and assuming it returns list in Python 3
```python
z = zip(A, B)
print(z[0])
```
<details><summary>Answer</summary>

```python
z = list(zip(A, B))
print(z[0])
```
Explanation: `zip` returns iterator; convert to list to index.
</details>

3) Broken: mismatched lengths, expecting error
```python
for a, b in zip([1], [2,3]):
    print(a+b)
```
<details><summary>Answer</summary>

It will only iterate the shortest list length; no error.

Explanation: `zip` stops at the shortest input.
</details>

---

## Easy

a) Use `enumerate` to print index:value pairs for list `['x','y']`.

Starter code:
```python
L = ['x','y']
# TODO: print index and value
pass
```
<details><summary>Answer</summary>

```python
L = ['x','y']
for i, v in enumerate(L):
    print(i, v)
```
Explanation: `enumerate` is simple for index and value.
</details>

b) Use `zip` to pair `[1,2]` and `['a','b']` and print pairs.

Starter code:
```python
A = [1,2]
B = ['a','b']
# TODO: zip and print
pass
```
<details><summary>Answer</summary>

```python
A = [1,2]
B = ['a','b']
for a, b in zip(A, B):
    print(a, b)
```
Explanation: `zip` pairs items one-to-one.
</details>

---

## Medium

a) Use `enumerate` starting at 1 to print numbering for a list.

Starter code:
```python
L = ['a','b']
# TODO: enumerate start=1
pass
```
<details><summary>Answer</summary>

```python
L = ['a','b']
for i, v in enumerate(L, start=1):
    print(i, v)
```
Explanation: `start=` sets the first index.
</details>

b) Zip three lists and print triplets.

Starter code:
```python
A = [1]
B = [2]
C = [3]
# TODO: zip three lists
pass
```
<details><summary>Answer</summary>

```python
A = [1]
B = [2]
C = [3]
for x, y, z in zip(A, B, C):
    print(x, y, z)
```
Explanation: `zip` accepts multiple iterables.
</details>

---

## Hard

Write a function `indexed_pairs(A, B)` that returns a list of strings "i: a-b" for each zipped pair using enumerate.

Starter code:
```python
def indexed_pairs(A, B):
    # TODO
    pass

print(indexed_pairs([1,2], ['x','y']))
```
<details><summary>Answer</summary>

```python
def indexed_pairs(A, B):
    out = []
    for i, (a, b) in enumerate(zip(A, B)):
        out.append(f"{i}: {a}-{b}")
    return out

print(indexed_pairs([1,2], ['x','y']))
```
Explanation: combine `enumerate` with `zip` and f-strings.
</details>
