---
tags: [python, exercises, math]
difficulty: Beginner
---

# Python - Math - Arithmetic Operators — Exercises

See concept: [[Python - Math - Arithmetic Operators]]
GitHub link: [Python - Math - Arithmetic Operators](./Python%20-%20Math%20-%20Arithmetic%20Operators.md)

## Quick syntax fixes

1) Broken: integer division vs float
```python
print(3/2)
```
<details><summary>Answer</summary>

```python
print(3/2)
```
Explanation: in Python 3 `/` gives float; use `//` for integer division.
</details>

2) Broken: modulus of negative
```python
print(-3 % 2)
```
<details><summary>Answer</summary>

```python
print(-3 % 2)
```
Explanation: modulus works but sign rules exist; test to understand.
</details>

3) Broken: power operator typo
```python
print(pow 2 3)
```
<details><summary>Answer</summary>

```python
print(2 ** 3)
```
Explanation: use `**` for power.
</details>

---

## Easy

a) Print the sum of 4 and 5.

Starter code:
```python
# TODO: add 4 and 5
pass
```
<details><summary>Answer</summary>

```python
print(4 + 5)
```
Explanation: simple addition.
</details>

b) Print 7 divided by 2 using integer division.

Starter code:
```python
# TODO: integer division
pass
```
<details><summary>Answer</summary>

```python
print(7 // 2)
```
Explanation: `//` yields integer result.
</details>

---

## Medium

a) Read two ints and print their product.

Starter code:
```python
# TODO: read two ints and multiply
pass
```
<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
print(a * b)
```
Explanation: convert to int before arithmetic.
</details>

b) Compute `(a + b) ** 2` for input a and b.

Starter code:
```python
# TODO: compute square of sum
pass
```
<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
print((a + b) ** 2)
```
Explanation: parentheses ensure addition before power.
</details>

---

## Hard

Write a function that returns remainder and quotient when dividing a by b.

Starter code:
```python
def div_info(a, b):
    # TODO: return (quotient, remainder)
    pass

print(div_info(7,3))
```
<details><summary>Answer</summary>

```python
def div_info(a, b):
    return (a // b, a % b)

print(div_info(7,3))
```
Explanation: use floor division and modulus.
</details>
