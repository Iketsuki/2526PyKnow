---
tags: [python, exercises, lists, search, sort]
difficulty: Beginner
---

# Python - Lists - Search & Sort — Exercises

See concept: [[Python - Lists - Search & Sort]]
GitHub link: [Python - Lists - Search & Sort](./Python%20-%20Lists%20-%20Search%20%26%20Sort.md)

## Quick syntax fixes

1) Broken: using `.index` when value not present
```python
L = [1,2]
print(L.index(3))
```
<details><summary>Answer</summary>

This raises `ValueError`; check membership first with `if 3 in L:`.

Explanation: `.index` expects the value to exist.
</details>

2) Broken: sorting in-place vs returning new list
```python
L = [3,1]
L2 = L.sort()
print(L2)
```
<details><summary>Answer</summary>

`list.sort()` sorts in place and returns `None`; use `sorted(L)` to get a new list.

Explanation: remember return behavior.
</details>

3) Broken: trying to sort list of mixed types
```python
L = [1, 'a']
L.sort()
```
<details><summary>Answer</summary>

Mixed types may not compare; convert to common type or provide `key`.

Explanation: ensure items are comparable.
</details>

---

## Easy

a) Check if 5 is in `[1,5,3]` and print `Yes` or `No`.

Starter code:
```python
L = [1,5,3]
# TODO: check membership
pass
```
<details><summary>Answer</summary>

```python
L = [1,5,3]
print('Yes' if 5 in L else 'No')
```
Explanation: `in` checks membership.
</details>

b) Sort the list `[3,1,2]` and print it.

Starter code:
```python
L = [3,1,2]
# TODO: print sorted list
pass
```
<details><summary>Answer</summary>

```python
L = [3,1,2]
print(sorted(L))
```
Explanation: `sorted` returns a new sorted list.
</details>

---

## Medium

a) Find the index of value 2 in `[0,2,4]` and print it.

Starter code:
```python
L = [0,2,4]
# TODO: print index of 2
pass
```
<details><summary>Answer</summary>

```python
L = [0,2,4]
print(L.index(2))
```
Explanation: `.index` returns the first matching index.
</details>

b) Sort a list of words by length using `sorted` with `key=len` and print.

Starter code:
```python
words = ['apple','kiwi','banana']
# TODO: sort by length and print
pass
```
<details><summary>Answer</summary>

```python
words = ['apple','kiwi','banana']
print(sorted(words, key=len))
```
Explanation: `key` customizes sort order.
</details>

---

## Hard

Write a function `binary_search(lst, target)` that returns True if `target` is in the sorted `lst` (simple loop ok).

Starter code:
```python
def binary_search(lst, target):
    # TODO: implement simple binary search
    pass

print(binary_search([1,2,3,4], 3))
```
<details><summary>Answer</summary>

```python
def binary_search(lst, target):
    lo = 0
    hi = len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return True
        if lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

print(binary_search([1,2,3,4], 3))
```
Explanation: binary search halves the search range each step.
</details>
