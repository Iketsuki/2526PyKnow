---
tags: [python, exercises, variables, builtins]
difficulty: Beginner
---

# Python - Variables & Types - Built-in Functions — Exercises

See concept: [[Python - Variables & Types - Built-in Functions]]
GitHub link: [Python - Variables & Types - Built-in Functions](./Python%20-%20Variables%20%26%20Types%20-%20Built-in%20Functions.md)

## Quick syntax fixes

1) Broken: using `len` wrong
```python
# Broken
print(len  ( [1,2,3] ))
```
<details><summary>Answer</summary>

```python
# Fixed
print(len([1,2,3]))
```
Explanation: Call `len()` with parentheses around the argument.
</details>

2) Broken: using `max` with no args
```python
# Broken
print(max())
```
<details><summary>Answer</summary>

```python
# Fixed
print(max([1,2,3]))
```
Explanation: Provide an iterable or multiple arguments to `max`.
</details>

3) Broken: wrong `str` use
```python
# Broken
value = str(5)
print(type(value) == 'str')
```
<details><summary>Answer</summary>

```python
# Fixed
value = str(5)
print(isinstance(value, str))
```
Explanation: Use `isinstance` to check types, not string names.
</details>

---

## Easy

a) Use `len()` to print length of list `[1,2,3]`.

Starter code:
```python
lst = [1,2,3]
# TODO: print length
```
<details><summary>Answer</summary>

```python
lst = [1,2,3]
print(len(lst))
```
Explanation: `len()` returns the number of items.
</details>

b) Use `str()` to convert `5` to text and print its type.

Starter code:
```python
n = 5
# TODO: convert to string and print type
```
<details><summary>Answer</summary>

```python
n = 5
text = str(n)
print(type(text))
```
Explanation: `str()` makes a string representation.
</details>

---

## Medium

a) Use `sum()` to add numbers in a list and print result.

Starter code:
```python
nums = [1,2,3]
# TODO: print sum
```
<details><summary>Answer</summary>

```python
nums = [1,2,3]
print(sum(nums))
```
Explanation: `sum()` returns total of iterable.
</details>

b) Use `min()` and `max()` on a list and print both values.

Starter code:
```python
vals = [4,1,7]
# TODO: print min and max
```
<details><summary>Answer</summary>

```python
vals = [4,1,7]
print(min(vals))
print(max(vals))
```
Explanation: `min` and `max` find smallest and largest items.
</details>

---

## Hard

Given `s='123'` use `int`, `sum`, and `map` to compute the sum of digits (1+2+3=6).

Starter code:
```python
s = '123'
# TODO: compute sum of digits and print 6
```
<details><summary>Answer</summary>

```python
s = '123'
digits = map(int, list(s))
print(sum(digits))
```
Explanation: Use `map(int, ...)` to convert chars to ints, then `sum`.
</details>
