---
tags: [python, exercises, lists, remove]
difficulty: Beginner
---

# Python - Lists - Remove Methods — Exercises

See concept: [[Python - Lists - Remove Methods]]
GitHub link: [Python - Lists - Remove Methods](./Python%20-%20Lists%20-%20Remove%20Methods.md)

## Quick syntax fixes

1) Broken: using `remove` with wrong value
```python
L = [1,2,3]
L.remove(4)
```
<details><summary>Answer</summary>

This raises `ValueError` because 4 is not in list.

Explanation: ensure value exists before `remove`.
</details>

2) Broken: calling `pop` without index when list empty
```python
L = []
L.pop()
```
<details><summary>Answer</summary>

This raises `IndexError`; check list length before `pop`.

Explanation: `pop()` needs an item to remove.
</details>

3) Broken: confusing `del` and `remove`
```python
del L[2]
L.remove(2)
```
<details><summary>Answer</summary>

`del L[2]` removes by index; `remove(2)` removes by value.

Explanation: use correct method for index vs value.
</details>

---

## Easy

a) Remove the value 3 from `[1,2,3,4]` and print the list.

Starter code:
```python
L = [1,2,3,4]
# TODO: remove 3 and print
pass
```
<details><summary>Answer</summary>

```python
L = [1,2,3,4]
L.remove(3)
print(L)
```
Explanation: `remove` deletes first matching value.
</details>

b) Pop the last item from a list and print it.

Starter code:
```python
L = [5,6,7]
# TODO: pop and print
pass
```
<details><summary>Answer</summary>

```python
L = [5,6,7]
print(L.pop())
```
Explanation: `pop()` returns the removed item.
</details>

---

## Medium

a) Remove duplicates from a list while preserving order using a loop and `remove` or set helper.

Starter code:
```python
L = [1,2,1,3]
# TODO: remove duplicates keeping order
pass
```
<details><summary>Answer</summary>

```python
L = [1,2,1,3]
seen = set()
out = []
for x in L:
    if x not in seen:
        seen.add(x)
        out.append(x)
print(out)
```
Explanation: use `seen` to avoid repeated values.
</details>

b) Safely pop an item from a list if it exists (print 'empty' otherwise).

Starter code:
```python
L = []
# TODO: pop safely
pass
```
<details><summary>Answer</summary>

```python
L = []
if L:
    print(L.pop())
else:
    print('empty')
```
Explanation: check truthiness of list before popping.
</details>

---

## Hard

Write a function `remove_all(lst, val)` that removes all occurrences of `val` from `lst` and returns the new list.

Starter code:
```python
def remove_all(lst, val):
    # TODO
    pass

print(remove_all([1,2,1,3], 1))
```
<details><summary>Answer</summary>

```python
def remove_all(lst, val):
    return [x for x in lst if x != val]

print(remove_all([1,2,1,3], 1))
```
Explanation: list comprehension filters items.
</details>
