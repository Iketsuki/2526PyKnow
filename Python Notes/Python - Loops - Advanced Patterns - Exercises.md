---
tags: [python, exercises, loops, advanced]
difficulty: Beginner
---

# Python - Loops - Advanced Patterns — Exercises

See concept: [[Python - Loops - Advanced Patterns]]
GitHub link: [Python - Loops - Advanced Patterns](./Python%20-%20Loops%20-%20Advanced%20Patterns.md)

## Quick syntax fixes

1) Broken: modifying list while iterating
```python
L = [1,2,3]
for x in L:
    if x == 2:
        L.remove(x)
```
<details><summary>Answer</summary>

```python
L = [1,2,3]
for x in L[:]:
    if x == 2:
        L.remove(x)
```
Explanation: iterate over a copy to modify safely.
</details>

2) Broken: using range(len(list)) without need
```python
for i in range(len(L)):
    print(L[i])
```
<details><summary>Answer</summary>

```python
for item in L:
    print(item)
```
Explanation: direct iteration is clearer.
</details>

3) Broken: nested loops when `any` or `all` suffice
```python
found = False
for a in A:
    for b in B:
        if a == b:
            found = True
```
<details><summary>Answer</summary>

```python
found = any(a in B for a in A)
```
Explanation: `any` can simplify nested checks.
</details>

---

## Easy

a) Use `enumerate` to print index and value for a list.

Starter code:
```python
L = ['a','b','c']
# TODO: print index and value
pass
```
<details><summary>Answer</summary>

```python
L = ['a','b','c']
for i, v in enumerate(L):
    print(i, v)
```
Explanation: `enumerate` returns index and item.
</details>

b) Use `zip` to iterate two lists together and print pairs.

Starter code:
```python
A = [1,2]
B = ['x','y']
# TODO: print pairs
pass
```
<details><summary>Answer</summary>

```python
A = [1,2]
B = ['x','y']
for a, b in zip(A, B):
    print(a, b)
```
Explanation: `zip` pairs items from both lists.
</details>

---

## Medium

a) Use `itertools.product` to loop over all pairs from two lists and count them.

Starter code:
```python
import itertools
A = [1,2]
B = ['x','y','z']
# TODO: print count of pairs
pass
```
<details><summary>Answer</summary>

```python
import itertools
A = [1,2]
B = ['x','y','z']
count = 0
for _ in itertools.product(A, B):
    count += 1
print(count)
```
Explanation: product makes the Cartesian product.
</details>

b) Flatten a list of lists with a loop and print the flat list.

Starter code:
```python
lists = [[1,2], [3,4]]
# TODO: flatten
pass
```
<details><summary>Answer</summary>

```python
lists = [[1,2], [3,4]]
flat = []
for sub in lists:
    for x in sub:
        flat.append(x)
print(flat)
```
Explanation: nested loops build flattened list.
</details>

---

## Hard

Write a function `pairwise_sum(A, B)` that returns a list of sums of matching indices (use `zip`).

Starter code:
```python
def pairwise_sum(A, B):
    # TODO
    pass

print(pairwise_sum([1,2], [3,4]))
```
<details><summary>Answer</summary>

```python
def pairwise_sum(A, B):
    return [a + b for a, b in zip(A, B)]

print(pairwise_sum([1,2], [3,4]))
```
Explanation: `zip` pairs elements and list comprehension makes sums.
</details>
