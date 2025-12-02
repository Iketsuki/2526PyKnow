---
tags: [python, exercises, lists, slicing]
difficulty: Beginner
---

# Python - Lists - Slicing — Exercises

See concept: [[Python - Lists - Slicing]]
GitHub link: [Python - Lists - Slicing](./Python%20-%20Lists%20-%20Slicing.md)

## Quick syntax fixes

1) Broken: wrong slice order
```python
L = [1,2,3,4]
print(L[3:1])
```
<details><summary>Answer</summary>

```python
L = [1,2,3,4]
print(L[1:3])
```
Explanation: start must be less than end to get expected slice.
</details>

2) Broken: negative step confusion
```python
print(L[:: -1])
```
<details><summary>Answer</summary>

```python
print(L[::-1])
```
Explanation: `[::-1]` reverses list.
</details>

3) Broken: forgetting that slices return new list
```python
L = [1,2,3]
L2 = L[:]
L2.append(4)
print(L)
```
<details><summary>Answer</summary>

L remains `[1,2,3]`, `L2` is `[1,2,3,4]` because slice copies.

Explanation: slicing without assignment makes a new list.
</details>

---

## Easy

a) Get the first three items of a list.

Starter code:
```python
L = [10,20,30,40]
# TODO: print first three
pass
```
<details><summary>Answer</summary>

```python
L = [10,20,30,40]
print(L[:3])
```
Explanation: `[:3]` takes items 0..2.
</details>

b) Reverse a list with slicing and print it.

Starter code:
```python
L = [1,2,3]
# TODO: reverse
pass
```
<details><summary>Answer</summary>

```python
L = [1,2,3]
print(L[::-1])
```
Explanation: `[::-1]` returns reversed copy.
</details>

---

## Medium

a) Skip every other item from a list and print the result.

Starter code:
```python
L = [0,1,2,3,4,5]
# TODO: print every other item
pass
```
<details><summary>Answer</summary>

```python
L = [0,1,2,3,4,5]
print(L[::2])
```
Explanation: step of 2 picks alternate items.
</details>

b) Given a string `s`, print the substring from 1 to 4 (exclusive).

Starter code:
```python
s = 'hello'
# TODO: slice and print
pass
```
<details><summary>Answer</summary>

```python
s = 'hello'
print(s[1:4])
```
Explanation: `s[1:4]` gives characters at 1,2,3.
</details>

---

## Hard

Write a function `middle(lst)` that returns the list without the first and last element.

Starter code:
```python
def middle(lst):
    # TODO
    pass

print(middle([1,2,3,4]))
```
<details><summary>Answer</summary>

```python
def middle(lst):
    return lst[1:-1]

print(middle([1,2,3,4]))
```
Explanation: `1:-1` removes first and last.
</details>
