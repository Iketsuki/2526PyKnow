---
tags: [python, exercises, math]
difficulty: Beginner
---

# Python - Math - Rounding & Precision — Exercises

See concept: [[Python - Math - Rounding & Precision]]
GitHub link: [Python - Math - Rounding & Precision](./Python%20-%20Math%20-%20Rounding%20%26%20Precision.md)

## Quick syntax fixes

1) Broken: using round without assigning
```python
round(2.345, 2)
print(2.345)
```
<details><summary>Answer</summary>

```python
print(round(2.345, 2))
```
Explanation: round returns value; print that value.
</details>

2) Broken: formatting floats with % wrong
```python
print('%.2f' % 2.3)
```
<details><summary>Answer</summary>

```python
print('%.2f' % 2.3)
```
Explanation: this is valid; prefer format or f-strings for clarity.
</details>

3) Broken: summing floats causes precision surprises
```python
print(0.1 + 0.2)
```
<details><summary>Answer</summary>

```python
print(round(0.1 + 0.2, 2))
```
Explanation: use rounding for display of floating sums.
</details>

---

## Easy

a) Print 2.345 rounded to 2 decimal places.

Starter code:
```python
# TODO: round and print
pass
```
<details><summary>Answer</summary>

```python
print(round(2.345, 2))
```
Explanation: round(number, ndigits) controls decimals.
</details>

b) Format 3.1 as '3.10' using format string.

Starter code:
```python
# TODO: format to 2 decimals
pass
```
<details><summary>Answer</summary>

```python
print('{:.2f}'.format(3.1))
```
Explanation: format ensures two decimals.
</details>

---

## Medium

a) Read a float and print it rounded to 3 decimals.

Starter code:
```python
# TODO: read and round
pass
```
<details><summary>Answer</summary>

```python
n = float(input())
print(round(n, 3))
```
Explanation: convert to float then round.
</details>

b) Sum 0.1 ten times and print rounded to 2 decimals.

Starter code:
```python
# TODO: sum and round
pass
```
<details><summary>Answer</summary>

```python
total = sum([0.1 for _ in range(10)])
print(round(total, 2))
```
Explanation: rounding for readable monetary-like sums.
</details>

---

## Hard

Write a function that formats a number with thousand separators and two decimals.

Starter code:
```python
def fmt(n):
    # TODO: return formatted string
    pass

print(fmt(12345.678))
```
<details><summary>Answer</summary>

```python
def fmt(n):
    return '{:,.2f}'.format(n)

print(fmt(12345.678))
```
Explanation: format spec `:,` adds commas and `.2f` sets decimals.
</details>
