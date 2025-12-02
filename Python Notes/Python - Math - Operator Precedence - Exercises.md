---
tags: [python, exercises, math, precedence]
difficulty: Beginner
---

# Python - Math - Operator Precedence — Exercises

See concept: [[Python - Math - Operator Precedence]]
GitHub link: [Python - Math - Operator Precedence](./Python%20-%20Math%20-%20Operator%20Precedence.md)

## Quick syntax fixes

1) Broken: wrong grouping
```python
# Broken
value = 2 + 3 * 4
print(value)
```
<details><summary>Answer</summary>

```python
# Fixed (explain)
value = 2 + 3 * 4
print(value)  # 14 because * runs before +
```
Explanation: `*` has higher precedence than `+`.
</details>

2) Broken: missing parentheses
```python
# Broken
result = (2 + 3 * (4)
```
<details><summary>Answer</summary>

```python
# Fixed
result = (2 + 3) * 4
print(result)
```
Explanation: Add closing parenthesis and group as needed.
</details>

3) Broken: mix of / and *
```python
# Example
value = 8 / 4 * 2
print(value)
```
<details><summary>Answer</summary>

```python
# Explain
value = 8 / 4 * 2
print(value)  # left-to-right -> (8/4)*2 = 4.0
```
Explanation: `/` and `*` have same precedence; evaluate left-to-right.
</details>

---

## Easy

a) Compute `2 + 3 * 4` and explain why result is 14.

Starter code:
```python
expr = 2 + 3 * 4
print(expr)
# TODO: add a short comment why
```
<details><summary>Answer</summary>

```python
expr = 2 + 3 * 4
print(expr)  # 14 because 3*4 = 12 then 2 + 12 = 14
```
Explanation: Multiplication happens before addition.
</details>

b) Use parentheses to change evaluation so result is 20.

Starter code:
```python
expr = 2 + 3 * 4
# TODO: make expression equal 20
print(expr)
```
<details><summary>Answer</summary>

```python
expr = (2 + 3) * 4
print(expr)
```
Explanation: Parentheses change order of operations.
</details>

---

## Medium

a) Evaluate `4 + 6 / 2 * 3` using Python rules and print result.

Starter code:
```python
expr = 4 + 6 / 2 * 3
print(expr)
```
<details><summary>Answer</summary>

```python
expr = 4 + 6 / 2 * 3
print(expr)  # 13.0
```
Explanation: 6/2=3.0; 3.0*3=9.0; 4+9=13.0.
</details>

b) Add parentheses to make addition happen first for the same expression.

Starter code:
```python
expr = 4 + 6 / 2 * 3
# TODO: change expression so addition runs first
print(expr)
```
<details><summary>Answer</summary>

```python
expr = (4 + 6) / 2 * 3
print(expr)
```
Explanation: Parentheses force addition first.
</details>

---

## Hard

Create an expression with `a=2,b=3,c=4,d=5` that evaluates to 45.

Starter code:
```python
a = 2
b = 3
c = 4
d = 5
# TODO: compute expression equal to 45
```
<details><summary>Answer</summary>

```python
a = 2
b = 3
c = 4
d = 5
print((a + b) * (c + d))  # 5 * 9 = 45
```
Explanation: Use parentheses to group operations.
</details>
