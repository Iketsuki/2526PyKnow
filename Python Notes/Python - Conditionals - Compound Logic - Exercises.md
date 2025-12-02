---
tags: [python, exercises, conditionals, logic]
difficulty: Beginner
---

# Python - Conditionals - Compound Logic — Exercises

See concept: [[Python - Conditionals - Compound Logic]]
GitHub link: [Python - Conditionals - Compound Logic](./Python%20-%20Conditionals%20-%20Compound%20Logic.md)

## Quick syntax fixes

1) Broken: missing parentheses in compound condition
```python
# Broken
if a > 0 and a < 10 or b > 0:
    print('ok')
```
<details><summary>Answer</summary>

```python
# Fixed
if (a > 0 and a < 10) or (b > 0):
    print('ok')
```
Explanation: Use parentheses to clarify precedence.
</details>

2) Broken: mixing comparisons incorrectly
```python
# Broken
if 1 < x < 5 and x > 10:
    print('weird')
```
<details><summary>Answer</summary>

```python
# Fixed
if 1 < x < 5 and x > 0:
    print('ok')
```
Explanation: Ensure comparisons make logical sense.
</details>

3) Broken: wrong boolean variable use
```python
# Broken
is_ok = False
if is_ok and a == 1:
    print('yes')
```
<details><summary>Answer</summary>

```python
# Fixed
is_ok = True
if is_ok and a == 1:
    print('yes')
```
Explanation: Check boolean values and conditions together.
</details>

---

## Easy

a) Check if `x` is between 1 and 10 (inclusive) and print 'in range' else 'out'.

Starter code:
```python
x = 5
# TODO: print if x is between 1 and 10
pass
```
<details><summary>Answer</summary>

```python
x = 5
if 1 <= x <= 10:
    print('in range')
else:
    print('out')
```
Explanation: Python supports chained comparisons.
</details>

b) Return True if `a` is positive and `b` is even.

Starter code:
```python
def check(a, b):
    # TODO: return True if a>0 and b%2==0
    pass
print(check(1,2))
```
<details><summary>Answer</summary>

```python
def check(a, b):
    return a > 0 and (b % 2 == 0)
print(check(1,2))
```
Explanation: Combine numeric and boolean checks with `and`.
</details>

---

## Medium

a) Combine `or` and `and` to allow action when `is_admin` or (`is_user` and `not suspended`).

Starter code:
```python
is_admin = False
is_user = True
suspended = False
# TODO: set allowed and print
pass
```
<details><summary>Answer</summary>

```python
is_admin = False
is_user = True
suspended = False
allowed = is_admin or (is_user and not suspended)
print(allowed)
```
Explanation: Use parentheses so `and` groups before `or` for clarity.
</details>

b) Prevent division by zero using compound check before dividing.

Starter code:
```python
a = 10
b = 0
# TODO: if b != 0 print a/b else print 'bad'
pass
```
<details><summary>Answer</summary>

```python
a = 10
b = 0
if b != 0 and a is not None:
    print(a / b)
else:
    print('bad')
```
Explanation: Check denominator before dividing.
</details>

---

## Hard

Write a function `valid_score(score)` that returns True if score is between 0 and 100 inclusive and not None.

Starter code:
```python
def valid_score(score):
    # TODO: return True if 0<=score<=100 and score is not None
    pass
print(valid_score(50))
print(valid_score(None))
```
<details><summary>Answer</summary>

```python
def valid_score(score):
    return (score is not None) and (0 <= score <= 100)
print(valid_score(50))
print(valid_score(None))
```
Explanation: Check for None first to avoid TypeError when comparing.
</details>
