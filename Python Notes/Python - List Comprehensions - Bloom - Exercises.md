---
tags: [python, exercises, lists, comprehensions]
difficulty: Beginner
---

# Python - List Comprehensions - Bloom — Exercises

See concept: [[Python - List Comprehensions - Bloom]]
GitHub link: [Python - List Comprehensions - Bloom](./Python%20-%20List%20Comprehensions%20-%20Bloom.md)

## Quick syntax fixes

1) Broken: comprehension missing brackets
```python
for x in [1,2]: x*2
```
<details><summary>Answer</summary>

```python
[x*2 for x in [1,2]]
```
Explanation: list comprehensions use bracket notation.
</details>

2) Broken: using comprehension for side effects
```python
[print(x) for x in [1,2]]
```
<details><summary>Answer</summary>

```python
for x in [1,2]:
    print(x)
```
Explanation: use loops for side effects, comprehensions for building lists.
</details>

3) Broken: comprehension with wrong variable name
```python
[y for x in [1,2]]
```
<details><summary>Answer</summary>

```python
[x for x in [1,2]]
```
Explanation: use the same loop variable inside expression.
</details>

---

## Easy

a) Make a list of squares from [1,2,3].

Starter code:
```python
# TODO: list comprehension for squares
pass
```
<details><summary>Answer</summary>

```python
squares = [x*x for x in [1,2,3]]
print(squares)
```
Explanation: comprehension maps each x to x*x.
</details>

b) Make a list of strings from numbers: '1','2'.

Starter code:
```python
# TODO: convert to strings
pass
```
<details><summary>Answer</summary>

```python
strings = [str(x) for x in [1,2]]
print(strings)
```
Explanation: use str() in comprehension.
</details>

---

## Medium

a) Filter even numbers from 1..6 using comprehension.

Starter code:
```python
# TODO: even numbers comprehension
pass
```
<details><summary>Answer</summary>

```python
evens = [x for x in range(1,7) if x%2==0]
print(evens)
```
Explanation: add if condition in comprehension.
</details>

b) Create pairs (x,y) for x in [1,2] and y in [3,4].

Starter code:
```python
# TODO: list of pairs
pass
```
<details><summary>Answer</summary>

```python
pairs = [(x,y) for x in [1,2] for y in [3,4]]
print(pairs)
```
Explanation: nested loops in comprehension generate pairs.
</details>

---

## Hard

Use comprehension to make a dict mapping numbers to their squares for 1..3.

Starter code:
```python
# TODO: dict comprehension
pass
```
<details><summary>Answer</summary>

```python
d = {x: x*x for x in range(1,4)}
print(d)
```
Explanation: use brace form for dict comprehensions.
</details>
