---
tags: [python, exercises, conditionals, boolean]
difficulty: Beginner
---

# Python - Conditionals - Boolean Logic (and-or-not) — Exercises

See concept: [[Python - Conditionals - Boolean Logic (and-or-not)]]
GitHub link: [Python - Conditionals - Boolean Logic (and-or-not)](./Python%20-%20Conditionals%20-%20Boolean%20Logic%20%28and-or-not%29.md)

## Quick syntax fixes

1) Broken: using `and` with non-boolean values incorrectly
```python
# Broken
if 1 and 0:
    print('yes')
```
<details><summary>Answer</summary>

```python
# Fixed
if bool(1) and bool(0):
    print('yes')
```
Explanation: Convert to booleans when mixing numeric truthy/falsy values.
</details>

2) Broken: `or` ordering mistake
```python
# Broken
name = ''
print(name or None)
```
<details><summary>Answer</summary>

```python
# Fixed
name = ''
print(name or 'unknown')
```
Explanation: `or` returns first truthy value; give a readable default.
</details>

3) Broken: using `not` wrong place
```python
# Broken
is_ok = False
if not is_ok == True:
    print('bad')
```
<details><summary>Answer</summary>

```python
# Fixed
is_ok = False
if not is_ok:
    print('bad')
```
Explanation: Use `not` directly with the boolean variable.
</details>

---

## Easy

a) Check if both `a` and `b` are True and print 'both' else 'no'.

Starter code:
```python
a = True
b = False
# TODO: print 'both' if both True else 'no'
pass
```
<details><summary>Answer</summary>

```python
a = True
b = False
if a and b:
    print('both')
else:
    print('no')
```
Explanation: `and` requires both sides to be True.
</details>

b) Use `or` to choose a non-empty string between `s1` and `s2` and print it.

Starter code:
```python
s1 = ''
s2 = 'hello'
# TODO: print non-empty string
pass
```
<details><summary>Answer</summary>

```python
s1 = ''
s2 = 'hello'
print(s1 or s2)
```
Explanation: `or` returns first truthy value.
</details>

---

## Medium

a) Use `and`, `or`, and `not` to implement simple permission checks: `can_edit = is_owner or (is_member and not is_banned)`.

Starter code:
```python
is_owner = False
is_member = True
is_banned = False
# TODO: set can_edit and print it
pass
```
<details><summary>Answer</summary>

```python
is_owner = False
is_member = True
is_banned = False
can_edit = is_owner or (is_member and not is_banned)
print(can_edit)
```
Explanation: Combine boolean operators for rules.
</details>

b) Show short-circuit behavior: write code that prints 1 and does not call function when left side is True.

Starter code:
```python
def f():
    print('called')
    return True
# TODO: use or/and to avoid calling f when not needed
pass
```
<details><summary>Answer</summary>

```python
def f():
    print('called')
    return True
print(True or f())  # f() is not called because True short-circuits
```
Explanation: `or` short-circuits when left side is truthy.
</details>

---

## Hard

Write a function `both_positive(a,b)` that returns True only if both numbers are > 0 using boolean operators.

Starter code:
```python
def both_positive(a, b):
    # TODO: return True if both > 0
    pass
print(both_positive(1,2))
print(both_positive(0,2))
```
<details><summary>Answer</summary>

```python
def both_positive(a, b):
    return (a > 0) and (b > 0)
print(both_positive(1,2))
print(both_positive(0,2))
```
Explanation: Use comparison and `and` to combine checks.
</details>
