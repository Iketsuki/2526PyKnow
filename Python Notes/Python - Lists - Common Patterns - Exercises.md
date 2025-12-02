---
tags: [python, exercises, lists]
difficulty: Beginner
---

# Python - Lists - Common Patterns — Exercises

See concept: [[Python - Lists - Common Patterns]]
GitHub link: [Python - Lists - Common Patterns](./Python%20-%20Lists%20-%20Common%20Patterns.md)

## Quick syntax fixes

1) Broken: reversing with wrong method
```python
l = [1,2]
l = l.reverse()
```
<details><summary>Answer</summary>

```python
l = [1,2]
l.reverse()
```
Explanation: `reverse()` modifies list in place and returns None.
</details>

2) Broken: using sort on immutable
```python
t = (2,1)
t.sort()
```
<details><summary>Answer</summary>

```python
t = (2,1)
lst = list(t)
lst.sort()
```
Explanation: tuples are immutable; convert to list first.
</details>

3) Broken: creating list from range incorrectly
```python
nums = range(5)
print(nums[0])
```
<details><summary>Answer</summary>

```python
nums = list(range(5))
print(nums[0])
```
Explanation: convert range to list to index.
</details>

---

## Easy

a) Reverse a list `[1,2,3]` and print it.

Starter code:
```python
# TODO: reverse and print
pass
```
<details><summary>Answer</summary>

```python
l = [1,2,3]
l.reverse()
print(l)
```
Explanation: use `reverse()` to reverse in place.
</details>

b) Sort a list of numbers and print smallest.

Starter code:
```python
# TODO: sort and print first
pass
```
<details><summary>Answer</summary>

```python
l = [3,1,2]
l.sort()
print(l[0])
```
Explanation: `sort()` arranges items; index 0 is smallest.
</details>

---

## Medium

a) Remove duplicates from a list and preserve some order.

Starter code:
```python
l = [1,2,1]
# TODO: remove duplicates
pass
```
<details><summary>Answer</summary>

```python
l = [1,2,1]
seen = []
for x in l:
    if x not in seen:
        seen.append(x)
print(seen)
```
Explanation: preserve first occurrence order.
</details>

b) Flatten a list of lists one level.

Starter code:
```python
l = [[1,2],[3]]
# TODO: flatten
pass
```
<details><summary>Answer</summary>

```python
l = [[1,2],[3]]
flat = [x for sub in l for x in sub]
print(flat)
```
Explanation: nested comprehension flattens one level.
</details>

---

## Hard

Write a function to rotate a list right by one position.

Starter code:
```python
def rotate_right(lst):
    # TODO: rotate and return
    pass

print(rotate_right([1,2,3]))
```
<details><summary>Answer</summary>

```python
def rotate_right(lst):
    return [lst[-1]] + lst[:-1]

print(rotate_right([1,2,3]))
```
Explanation: last element moves to front.
</details>
