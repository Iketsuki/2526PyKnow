---
tags: [python, exercises, math]
difficulty: Beginner
---

# Python - Math - Percentages & Discounts — Exercises

See concept: [[Python - Math - Percentages & Discounts]]
GitHub link: [Python - Math - Percentages & Discounts](./Python%20-%20Math%20-%20Percentages%20%26%20Discounts.md)

## Quick syntax fixes

1) Broken: percent calculation missing divide by 100
```python
print(20 * 50)
```
<details><summary>Answer</summary>

```python
print(20/100 * 50)
```
Explanation: percent is percent/100 * base value.
</details>

2) Broken: discount applied twice
```python
price = 100
price = price - price*0.1
price = price - price*0.2
```
<details><summary>Answer</summary>

```python
price = 100
price = price * (1 - 0.1 - 0.2)
```
Explanation: combine discounts or apply sequentially as specified.
</details>

3) Broken: using int too early
```python
print(int(10/3) * 100)
```
<details><summary>Answer</summary>

```python
print((10/3) * 100)
```
Explanation: avoid int until final formatting.
</details>

---

## Easy

a) Compute 10% of a number from input.

Starter code:
```python
# TODO: read number and print 10 percent
pass
```
<details><summary>Answer</summary>

```python
n = float(input())
print(n * 0.10)
```
Explanation: multiply by 0.1 for 10%.
</details>

b) Apply a 20% discount to a price and print the new price.

Starter code:
```python
# TODO: discount price
pass
```
<details><summary>Answer</summary>

```python
price = float(input())
print(price * 0.8)
```
Explanation: 20% off means keep 80%.
</details>

---

## Medium

a) Given original and sale percent, compute sale price.

Starter code:
```python
orig = float(input())
percent = float(input())
# TODO: compute sale price
pass
```
<details><summary>Answer</summary>

```python
orig = float(input())
percent = float(input())
print(orig * (1 - percent / 100))
```
Explanation: multiply by (1 - percent/100).
</details>

b) Compute what percent one number is of another.

Starter code:
```python
a = float(input())
b = float(input())
# TODO: print percentage a is of b
pass
```
<details><summary>Answer</summary>

```python
a = float(input())
b = float(input())
print((a / b) * 100)
```
Explanation: divide then multiply by 100.
</details>

---

## Hard

Write a function that applies successive discounts from a list and returns final price.

Starter code:
```python
def apply_discounts(price, discounts):
    # discounts is list like [10,5] meaning 10% then 5%
    pass

print(apply_discounts(100, [10,5]))
```
<details><summary>Answer</summary>

```python
def apply_discounts(price, discounts):
    p = price
    for d in discounts:
        p = p * (1 - d/100)
    return p

print(apply_discounts(100, [10,5]))
```
Explanation: apply each percent in sequence.
</details>
