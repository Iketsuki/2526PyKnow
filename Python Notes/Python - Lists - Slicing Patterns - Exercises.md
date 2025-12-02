---
tags: [python, exercises, lists, slicing]
difficulty: Beginner
---

# Python - Lists - Slicing Patterns — Exercises

See concept: [[Python - Lists - Slicing Patterns]]
GitHub link: [Python - Lists - Slicing Patterns](./Python%20-%20Lists%20-%20Slicing%20Patterns.md)

## Quick syntax fixes

1) Broken: off-by-one slice
```python
L = [1,2,3,4]
print(L[:4])
```
<details><summary>Answer</summary>

`L[:4]` returns all items; use `L[:3]` to get first three.

Explanation: slice end is exclusive.
</details>

2) Broken: using negative step incorrectly
```python
print(L[1:-1:-1])
```
<details><summary>Answer</summary>

Negative step reverses direction; choose correct indices or use `[::-1]`.

Explanation: mixing positive bounds with negative step often gives empty result.
</details>

3) Broken: assuming slice modifies list
```python
L = [1,2,3]
L[1:2] = [9]
```
<details><summary>Answer</summary>

This does modify `L` in-place; careful with assignment slices to reshape list.

Explanation: slice assignment can insert or remove elements.
</details>

---

## Easy

a) Take every second element from `[0,1,2,3,4]` and print.

Starter code:
```python
L = [0,1,2,3,4]
# TODO: print every second element
pass
```
<details><summary>Answer</summary>

```python
L = [0,1,2,3,4]
print(L[::2])
```
Explanation: step selects stride.
</details>

b) Show how to replace the middle slice `L[1:3]` with `[9,9]`.

Starter code:
```python
L = [1,2,3,4]
# TODO: replace middle
pass
```
<details><summary>Answer</summary>

```python
L = [1,2,3,4]
L[1:3] = [9,9]
print(L)
```
Explanation: slice assignment changes list content.
</details>

---

## Medium

a) Given `L`, return every third item starting from index 2.

Starter code:
```python
L = list(range(10))
# TODO: print items start=2 step=3
pass
```
<details><summary>Answer</summary>

```python
L = list(range(10))
print(L[2::3])
```
Explanation: `start: :step` form controls start and step.
</details>

b) Remove the first and last two items using slicing.

Starter code:
```python
L = [0,1,2,3,4,5]
# TODO: remove first and last two
pass
```
<details><summary>Answer</summary>

```python
L = [0,1,2,3,4,5]
print(L[2:-2])
```
Explanation: `2:-2` removes 2 from front and back.
</details>

---

## Hard

Write a function `every_n(lst, n, start=0)` that returns every `n`th item starting at `start`.

Starter code:
```python
def every_n(lst, n, start=0):
    # TODO
    pass

print(every_n(list(range(10)), 3, 1))
```
<details><summary>Answer</summary>

```python
def every_n(lst, n, start=0):
    return lst[start::n]

print(every_n(list(range(10)), 3, 1))
```
Explanation: slicing handles start and step.
</details>
