---
tags: [python, exercises, lists, methods]
difficulty: Beginner
---

# Python - Lists - List Methods — Exercises

See concept: [[Python - Lists - List Methods]]
GitHub link: [Python - Lists - List Methods](./Python%20-%20Lists%20-%20List%20Methods.md)

## Quick syntax fixes

1) Broken: using `append` wrong
```python
L.append([1,2])
```
<details><summary>Answer</summary>

This appends the list as a single element; use `extend` to add items individually.

Explanation: `append` adds one element, `extend` concatenates.
</details>

2) Broken: expecting `sort` to return list
```python
L2 = L.sort()
```
<details><summary>Answer</summary>

`L.sort()` modifies in place and returns `None`; use `sorted(L)` for a new sorted list.

Explanation: difference between in-place and functional APIs.
</details>

3) Broken: pop and index confusion
```python
L.pop(5)
```
<details><summary>Answer</summary>

If index out of range, `pop` raises `IndexError`; ensure index valid.

Explanation: check bounds before popping.
</details>

---

## Easy

a) Use `append` to add `10` to `[1,2,3]`.

Starter code:
```python
L = [1,2,3]
# TODO: append 10
pass
```
<details><summary>Answer</summary>

```python
L = [1,2,3]
L.append(10)
print(L)
```
Explanation: simple append example.
</details>

b) Use `count` to print how many times `1` appears in `[1,2,1]`.

Starter code:
```python
L = [1,2,1]
# TODO: print count
pass
```
<details><summary>Answer</summary>

```python
L = [1,2,1]
print(L.count(1))
```
Explanation: `count` returns occurrences.
</details>

---

## Medium

a) Use `index` to find where `3` appears in `[1,3,5]`.

Starter code:
```python
L = [1,3,5]
# TODO: print index of 3
pass
```
<details><summary>Answer</summary>

```python
L = [1,3,5]
print(L.index(3))
```
Explanation: `index` returns first matching position.
</details>

b) Use `reverse()` to reverse a list in place and print.

Starter code:
```python
L = [1,2,3]
# TODO: reverse and print
pass
```
<details><summary>Answer</summary>

```python
L = [1,2,3]
L.reverse()
print(L)
```
Explanation: `reverse()` mutates the list.
</details>

---

## Hard

Write a function `replace_all(lst, old, new)` that replaces all occurrences of `old` with `new`.

Starter code:
```python
def replace_all(lst, old, new):
    # TODO
    pass

print(replace_all([1,2,1], 1, 9))
```
<details><summary>Answer</summary>

```python
def replace_all(lst, old, new):
    return [new if x == old else x for x in lst]

print(replace_all([1,2,1], 1, 9))
```
Explanation: use list comprehension to build new list.
</details>
