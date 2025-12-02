---
tags: [python, exercises, math, modulo]
difficulty: Beginner
---

# Python - Math - Modulo & Divisibility — Exercises

See concept: [[Python - Math - Modulo & Divisibility]]
GitHub link: [Python - Math - Modulo & Divisibility](./Python%20-%20Math%20-%20Modulo%20%26%20Divisibility.md)

## Quick syntax fixes

1) Broken: modulo by zero
```python
# Broken
print(5 % 0)
```
<details><summary>Answer</summary>

```python
# Fixed
print(5 % 2)
```
Explanation: Modulo by zero raises an error; use a non-zero divisor.
</details>

2) Broken: expecting integer remainder from float
```python
# Example
print(5.5 % 2)
```
<details><summary>Answer</summary>

```python
# prints 1.5
print(5.5 % 2)
```
Explanation: `%` works with floats and returns float remainder.
</details>

3) Broken: integer division confusion
```python
# Example
print(7 // 2)
```
<details><summary>Answer</summary>

```python
# prints 3
print(7 // 2)
```
Explanation: `//` gives integer quotient (floor division).
</details>

---

## Easy

a) Print remainder of 10 divided by 3.

Starter code:
```python
print(10 % 3)
```
<details><summary>Answer</summary>

```python
print(10 % 3)
```
Explanation: 10 % 3 equals 1.
</details>

b) Print integer division 10 // 3.

Starter code:
```python
print(10 // 3)
```
<details><summary>Answer</summary>

```python
print(10 // 3)
```
Explanation: 10 // 3 equals 3.
</details>

---

## Medium

a) Convert 125 seconds into minutes and seconds.

Starter code:
```python
seconds = 125
# TODO: compute minutes and seconds_left and print them
```
<details><summary>Answer</summary>

```python
seconds = 125
minutes = seconds // 60
seconds_left = seconds % 60
print(minutes)
print(seconds_left)
```
Explanation: Use `//` for minutes and `%` for remaining seconds.
</details>

b) Use `%` to check if a number is even or odd.

Starter code:
```python
n = 7
# TODO: print 'even' or 'odd'
```
<details><summary>Answer</summary>

```python
n = 7
if n % 2 == 0:
    print('even')
else:
    print('odd')
```
Explanation: Even numbers have remainder 0 when divided by 2.
</details>

---

## Hard

Given total seconds, print `hh:mm:ss` with zero padding.

Starter code:
```python
total_seconds = 3661
# TODO: print '01:01:01'
```
<details><summary>Answer</summary>

```python
total_seconds = 3661
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
```
Explanation: Use integer division and modulo to split time values.
</details>
