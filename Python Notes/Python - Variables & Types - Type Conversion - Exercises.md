---
tags: [python, exercises, variables, types]
difficulty: Beginner
---

# Python - Variables & Types - Type Conversion — Exercises

See concept: [[Python - Variables & Types - Type Conversion]]
GitHub link: [Python - Variables & Types - Type Conversion](./Python%20-%20Variables%20%26%20Types%20-%20Type%20Conversion.md)

## Quick syntax fixes

1) Broken: using float string in int()
```python
# Broken
s = '3.5'
print(int(s))
```
<details><summary>Answer</summary>

```python
# Fixed
s = '3.5'
print(float(s))
```
Explanation: Use float() for decimal strings.
</details>

2) Broken: wrong order of conversion
```python
# Broken
v = str(5) + 2
print(v)
```
<details><summary>Answer</summary>

```python
# Fixed
v = str(5) + str(2)
print(v)
```
Explanation: Convert both before concatenation.
</details>

3) Broken: converting list to int
```python
# Broken
lst = [1,2]
print(int(lst))
```
<details><summary>Answer</summary>

```python
# Fixed
lst = [1,2]
print(str(lst))
```
Explanation: Use str() to make printable representation.
</details>

---

## Easy

a) Convert a string '7' to int and print sum with 3.

Starter code:
```python
s = '7'
# TODO: convert and add 3
pass
```
<details><summary>Answer</summary>

```python
s = '7'
v = int(s) + 3
print(v)
```
Explanation: int() converts numeric strings to integers.
</details>

b) Turn number 10 into string and join with ' apples'.

Starter code:
```python
n = 10
# TODO: make message '10 apples'
pass
```
<details><summary>Answer</summary>

```python
n = 10
msg = str(n) + ' apples'
print(msg)
```
Explanation: Use str() to make numbers into text.
</details>

---

## Medium

a) Safely convert input to int; if input is decimal, convert to float then int.

Starter code:
```python
user = '3.5'
# TODO: convert to int in a safe way and print
pass
```
<details><summary>Answer</summary>

```python
user = '3.5'
try:
    v = int(user)
except ValueError:
    v = int(float(user))
print(v)
```
Explanation: Fall back to float conversion for decimals.
</details>

b) Convert list of number strings to list of ints.

Starter code:
```python
strs = ['1','2','3']
# TODO: make a list of ints
pass
```
<details><summary>Answer</summary>

```python
strs = ['1','2','3']
ints = [int(s) for s in strs]
print(ints)
```
Explanation: Use list comprehension to convert each item.
</details>

---

## Hard

Write a function that accepts a value and returns it as int if possible else returns None.

Starter code:
```python
def safe_int(v):
    # TODO: return int(v) or None
    pass
print(safe_int('5'))
print(safe_int('5.1'))
print(safe_int('x'))
```
<details><summary>Answer</summary>

```python
def safe_int(v):
    try:
        return int(v)
    except Exception:
        try:
            return int(float(v))
        except Exception:
            return None
print(safe_int('5'))    # 5
print(safe_int('5.1'))  # 5
print(safe_int('x'))    # None
```
Explanation: Try int, then float, else return None.
</details>
