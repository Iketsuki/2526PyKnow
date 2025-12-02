---
tags: [python, exercises, lists]
difficulty: Beginner
---

# Python - Lists - Add Methods — Exercises

See concept: [[Python - Lists - Add Methods]]
GitHub link: [Python - Lists - Add Methods](./Python%20-%20Lists%20-%20Add%20Methods.md)

## Quick syntax fixes

1) Broken: using `append` with two args
```python
l = []
l.append(1,2)
```
<details><summary>Answer</summary>

```python
l = []
l.append(1)
l.append(2)
```
Explanation: `append` takes a single element.
</details>

2) Broken: using `insert` without index
```python
l = [1]
l.insert(2)
```
<details><summary>Answer</summary>

```python
l = [1]
l.insert(0, 2)
```
Explanation: `insert` needs index and value.
</details>

3) Broken: using `extend` with non-iterable
```python
l = []
l.extend(5)
```
<details><summary>Answer</summary>

```python
l = []
l.extend([5])
```
Explanation: `extend` expects an iterable like list.
</details>

---

## Easy

a) Start with empty list, append input value and print list.

Starter code:
```python
# TODO: append input value
pass
```
<details><summary>Answer</summary>

```python
v = input()
l = []
l.append(v)
print(l)
```
Explanation: use `append` to add items.
</details>

b) Extend a list `[1,2]` with `[3,4]` and print it.

Starter code:
```python
# TODO: extend list
pass
```
<details><summary>Answer</summary>

```python
l = [1,2]
l.extend([3,4])
print(l)
```
Explanation: `extend` adds multiple elements.
</details>

---

## Medium

a) Insert a value at index 1 in list `[0,2]`.

Starter code:
```python
l = [0,2]
# TODO: insert 1 at index 1
pass
```
<details><summary>Answer</summary>

```python
l = [0,2]
l.insert(1,1)
print(l)
```
Explanation: `insert` places element at given index.
</details>

b) Use `extend` to add characters of a string to a list.

Starter code:
```python
l = []
# TODO: extend with 'ab'
pass
```
<details><summary>Answer</summary>

```python
l = []
l.extend('ab')
print(l)
```
Explanation: strings are iterable and extend will add characters.
</details>

---

## Hard

Write a function that adds a value unless it already exists in the list.

Starter code:
```python
def add_once(lst, val):
    # TODO: append only if missing
    pass

print(add_once([1,2], 2))
```
<details><summary>Answer</summary>

```python
def add_once(lst, val):
    if val not in lst:
        lst.append(val)
    return lst

print(add_once([1,2], 2))
```
Explanation: check membership before append.
</details>
