---
tags: [python, exercises, lists, comprehensions]
difficulty: Beginner
---

# Python - List Comprehensions — Exercises

See concept: [[Python - List Comprehensions]]
GitHub link: [Python - List Comprehensions](./Python%20-%20List%20Comprehensions.md)

## Quick syntax fixes

1) Broken: forgetting brackets
```python
for x in [1,2]: x*2
```
<details><summary>Answer</summary>

```python
[x*2 for x in [1,2]]
```
Explanation: wrap comprehension in brackets.
</details>

2) Broken: using comprehension to print values
```python
[print(x) for x in [1,2]]
```
<details><summary>Answer</summary>

```python
for x in [1,2]:
    print(x)
```
Explanation: use loops for side effects.
</details>

3) Broken: comprehension with wrong variable
```python
[y for x in [1,2]]
```
<details><summary>Answer</summary>

```python
[x for x in [1,2]]
```
Explanation: use same variable inside expression.
</details>

---

## Easy

a) Create a list of doubled numbers from [1,2,3].

Starter code:
```python
# TODO: doubled list
pass
```
<details><summary>Answer</summary>

```python
doubled = [x*2 for x in [1,2,3]]
print(doubled)
```
Explanation: comprehension applies expression to each item.
</details>

b) Convert words to uppercase using comprehension.

Starter code:
```python
words = ['a','b']
# TODO: uppercase
pass
```
<details><summary>Answer</summary>

```python
words = ['a','b']
upper = [w.upper() for w in words]
print(upper)
```
Explanation: call method inside comprehension.
</details>

---

## Medium

a) Use comprehension to filter odd numbers from 1..5.

Starter code:
```python
# TODO: odd numbers
pass
```
<details><summary>Answer</summary>

```python
odds = [x for x in range(1,6) if x%2==1]
print(odds)
```
Explanation: include an if condition.
</details>

b) Make a list of squares only for numbers >2.

Starter code:
```python
# TODO: squares >2
pass
```
<details><summary>Answer</summary>

```python
s = [x*x for x in range(1,6) if x>2]
print(s)
```
Explanation: combine expression and filter.
</details>

---

## Hard

Create a list of unique characters from a string using comprehension.

Starter code:
```python
s = 'aba'
# TODO: unique chars
pass
```
<details><summary>Answer</summary>

```python
s = 'aba'
unique = list({c for c in s})
print(unique)
```
Explanation: set comprehension gives unique chars, convert to list.
</details>
