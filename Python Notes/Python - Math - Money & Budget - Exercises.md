---
tags: [python, exercises, math, money]
difficulty: Beginner
---

# Python - Math - Money & Budget — Exercises

See concept: [[Python - Math - Money & Budget]]
GitHub link: [Python - Math - Money & Budget](./Python%20-%20Math%20-%20Money%20%26%20Budget.md)

## Quick syntax fixes

1) Broken: forgetting cents to dollars conversion
```python
price = 150
print(price)
```
<details><summary>Answer</summary>

```python
price = 150
print(price / 100)
```
Explanation: convert cents to dollars by dividing by 100.
</details>

2) Broken: rounding money with integer division
```python
total = 10/3
print(int(total))
```
<details><summary>Answer</summary>

```python
total = 10/3
print(round(total,2))
```
Explanation: use round for monetary formatting.
</details>

3) Broken: adding strings instead of numbers
```python
print('10' + '5')
```
<details><summary>Answer</summary>

```python
print(int('10') + int('5'))
```
Explanation: convert numeric strings before arithmetic.
</details>

---

## Easy

a) Read price in cents and print dollars (float with 2 decimals).

Starter code:
```python
# TODO: read cents and print dollars
pass
```
<details><summary>Answer</summary>

```python
cents = int(input())
print('{:.2f}'.format(cents / 100))
```
Explanation: divide by 100 and format to 2 decimals.
</details>

b) Add two prices in cents and print total dollars.

Starter code:
```python
# TODO: sum cents and print dollars
pass
```
<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
print('{:.2f}'.format((a + b) / 100))
```
Explanation: sum cents then convert.
</details>

---

## Medium

a) Calculate change given cost and paid amount (both in dollars).

Starter code:
```python
# TODO: read cost and paid, print change
pass
```
<details><summary>Answer</summary>

```python
cost = float(input())
paid = float(input())
print(round(paid - cost, 2))
```
Explanation: subtract and round to 2 decimals.
</details>

b) Compute monthly budget left after expenses list.

Starter code:
```python
income = float(input())
# TODO: read three expenses and print remainder
pass
```
<details><summary>Answer</summary>

```python
income = float(input())
e1 = float(input())
e2 = float(input())
e3 = float(input())
print(round(income - (e1+e2+e3),2))
```
Explanation: subtract expenses from income.
</details>

---

## Hard

Write a function that splits a bill amount among n people and returns per-person amount rounded up to cents.

Starter code:
```python
import math
def split_bill(amount, n):
    # TODO: split and round up to cents
    pass

print(split_bill(10.00, 3))
```
<details><summary>Answer</summary>

```python
import math
def split_bill(amount, n):
    cents = math.ceil((amount / n) * 100)
    return cents / 100.0

print(split_bill(10.00, 3))
```
Explanation: round up per-person cents then convert.
</details>
