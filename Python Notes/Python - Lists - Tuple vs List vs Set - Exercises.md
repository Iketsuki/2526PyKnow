---
tags: [python, exercises, lists, tuple, set]
difficulty: Beginner
---

# Python - Lists - Tuple vs List vs Set — Exercises

See concept: [[Python - Lists - Tuple vs List vs Set]]
GitHub link: [Python - Lists - Tuple vs List vs Set](./Python%20-%20Lists%20-%20Tuple%20vs%20List%20vs%20Set.md)

## Quick syntax fixes

1) Broken: trying to append to a tuple
```python
t = (1, 2)
t.append(3)
```
<details><summary>Answer</summary>

```python
t = (1, 2)
t = t + (3,)
```
Explanation: tuples are immutable; build a new tuple.
</details>

2) Broken: using list methods on set
```python
s = {1,2}
s.insert(3)
```
<details><summary>Answer</summary>

```python
s = {1,2}
s.add(3)
```
Explanation: sets use `add`, not `insert`.
</details>

3) Broken: using set when order matters
```python
items = {1,2,3}
print(items[0])
```
<details><summary>Answer</summary>

```python
items = [1,2,3]
print(items[0])
```
Explanation: sets are unordered; use lists for indexing.
</details>

---

## Easy

a) Create a list and a tuple with the same three numbers and print the second item from both.

Starter code:
```python
my_list = [1,2,3]
my_tuple = (1,2,3)
# TODO: print second items
pass
```
<details><summary>Answer</summary>

```python
my_list = [1,2,3]
my_tuple = (1,2,3)
print(my_list[1])
print(my_tuple[1])
```
Explanation: index 1 is the second item.
</details>

b) Create a set from `[1,1,2,2,3]` and print its length.

Starter code:
```python
items = [1,1,2,2,3]
# TODO: print unique count
pass
```
<details><summary>Answer</summary>

```python
items = [1,1,2,2,3]
print(len(set(items)))
```
Explanation: `set` removes duplicates.
</details>

---

## Medium

a) Given a list, convert it to a tuple and try to change the first element; catch the error and print `Immutable`.

Starter code:
```python
L = [5,6,7]
T = tuple(L)
# TODO: try to set T[0] = 1 and handle exception
pass
```
<details><summary>Answer</summary>

```python
L = [5,6,7]
T = tuple(L)
try:
    T[0] = 1
except TypeError:
    print('Immutable')
```
Explanation: tuples raise `TypeError` on assignment.
</details>

b) Find the intersection of two sets and print it sorted as a list.

Starter code:
```python
a = {1,2,3}
b = {2,3,4}
# TODO: print sorted intersection
pass
```
<details><summary>Answer</summary>

```python
a = {1,2,3}
b = {2,3,4}
print(sorted(list(a & b)))
```
Explanation: `&` finds intersection.
</details>

---

## Hard

Write a function that takes a list and returns a tuple of unique items preserving the original order.

Starter code:
```python
def unique_tuple(lst):
    # TODO: return tuple of unique items in order
    pass

print(unique_tuple([1,2,1,3]))
```
<details><summary>Answer</summary>

```python
def unique_tuple(lst):
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return tuple(out)

print(unique_tuple([1,2,1,3]))
```
Explanation: use `seen` to keep first occurrences.
</details>
