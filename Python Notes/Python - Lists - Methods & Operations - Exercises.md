---
tags: [python, exercises, lists, methods]
difficulty: Beginner
---

# Python - Lists - Methods & Operations — Exercises

See concept: [[Python - Lists - Methods & Operations]]
GitHub link: [Python - Lists - Methods & Operations](./Python%20-%20Lists%20-%20Methods%20%26%20Operations.md)

## Quick syntax fixes

1) Broken: using `append` with multiple args
```python
L = []
L.append(1,2)
```
<details><summary>Answer</summary>

`append` takes one argument; use `extend` to add multiple items: `L.extend([1,2])`.

Explanation: `append` adds single element.
</details>

2) Broken: using `+` to modify list variable expecting in-place
```python
L = [1]
L + [2]
print(L)
```
<details><summary>Answer</summary>

`L + [2]` returns a new list; assign back: `L = L + [2]` or use `L.append(2)`.

Explanation: `+` does not mutate original list.
</details>

3) Broken: mixing `insert` and `remove` incorrectly
```python
L = [1,2,3]
L.insert(1, 5)
L.remove(1)
```
<details><summary>Answer</summary>

This works but be careful: `remove(1)` removes first value 1, not index. Use `del L[0]` to delete index 0.

Explanation: `remove` is by value.
</details>

---

## Easy

a) Use `append` to add 4 to `[1,2,3]` and print.

Starter code:
```python
L = [1,2,3]
# TODO: append 4 and print
pass
```
<details><summary>Answer</summary>

```python
L = [1,2,3]
L.append(4)
print(L)
```
Explanation: `append` adds one item.
</details>

b) Use `extend` to add `[4,5]` to `[1,2]` and print.

Starter code:
```python
L = [1,2]
# TODO: extend and print
pass
```
<details><summary>Answer</summary>

```python
L = [1,2]
L.extend([4,5])
print(L)
```
Explanation: `extend` concatenates lists.
</details>

---

## Medium

a) Use `insert` to put 99 at index 1 in `[1,2,3]` and print.

Starter code:
```python
L = [1,2,3]
# TODO: insert and print
pass
```
<details><summary>Answer</summary>

```python
L = [1,2,3]
L.insert(1, 99)
print(L)
```
Explanation: `insert(index, value)` adds at position.
</details>

b) Clear a list and show it's empty.

Starter code:
```python
L = [1,2]
# TODO: clear list and print length
pass
```
<details><summary>Answer</summary>

```python
L = [1,2]
L.clear()
print(len(L))
```
Explanation: `clear()` removes all items.
</details>

---

## Hard

Write a function `rotate_left(lst, n)` that moves first `n` items to the end and returns the result.

Starter code:
```python
def rotate_left(lst, n):
    # TODO
    pass

print(rotate_left([1,2,3,4], 2))
```
<details><summary>Answer</summary>

```python
def rotate_left(lst, n):
    return lst[n:] + lst[:n]

print(rotate_left([1,2,3,4], 2))
```
Explanation: slicing and concatenation rotate the list.
</details>
