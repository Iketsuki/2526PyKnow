---
tags: [python, exercises, lists]
difficulty: Beginner
---

# Python - Lists - Indexing & Edge Cases — Exercises

See concept: [[Python - Lists - Indexing & Edge Cases]]
GitHub link: [Python - Lists - Indexing & Edge Cases](./Python%20-%20Lists%20-%20Indexing%20%26%20Edge%20Cases.md)

## Quick syntax fixes

1) Broken: negative index typo
```python
l = [1,2]
print(l[-3])
```
<details><summary>Answer</summary>

```python
l = [1,2]
print(l[-1])
```
Explanation: use -1 for last element.
</details>

2) Broken: index out of range
```python
l = [1]
print(l[1])
```
<details><summary>Answer</summary>

```python
l = [1]
if len(l) > 1:
    print(l[1])
else:
    print('no')
```
Explanation: check length before indexing.
</details>

3) Broken: slicing wrong end index
```python
l = [1,2,3]
print(l[0:4])
```
<details><summary>Answer</summary>

```python
l = [1,2,3]
print(l[0:3])
```
Explanation: end index should be <= len(list).
</details>

---

## Easy

a) Print the first and last element of `[1,2,3]`.

Starter code:
```python
# TODO: print first and last
pass
```
<details><summary>Answer</summary>

```python
l = [1,2,3]
print(l[0], l[-1])
```
Explanation: index 0 is first, -1 is last.
</details>

b) Safely get element at index 2 or print 'none'.

Starter code:
```python
l = [1]
# TODO: safe access
pass
```
<details><summary>Answer</summary>

```python
l = [1]
print(l[2] if len(l) > 2 else 'none')
```
Explanation: check length before accessing.
</details>

---

## Medium

a) Given list, print every second item (step 2).

Starter code:
```python
l = [1,2,3,4]
# TODO: print every second
pass
```
<details><summary>Answer</summary>

```python
l = [1,2,3,4]
print(l[::2])
```
Explanation: slicing with step selects every nth item.
</details>

b) Reverse a list using slicing.

Starter code:
```python
l = [1,2,3]
# TODO: reverse via slice
pass
```
<details><summary>Answer</summary>

```python
l = [1,2,3]
print(l[::-1])
```
Explanation: slice with negative step reverses list.
</details>

---

## Hard

Write a function that returns element `k` from end (k=1 last) or None when out of range.

Starter code:
```python
def kth_from_end(lst, k):
    # TODO: return k-th from end or None
    pass

print(kth_from_end([1,2,3], 1))
```
<details><summary>Answer</summary>

```python
def kth_from_end(lst, k):
    if k <= 0 or k > len(lst):
        return None
    return lst[-k]

print(kth_from_end([1,2,3], 1))
```
Explanation: negative index -k selects k-th from end.
</details>
