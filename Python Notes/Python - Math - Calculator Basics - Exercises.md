---
tags: [python, exercises, math, calculator]
difficulty: Beginner
---

# Python - Math - Calculator Basics — Exercises

See concept: [[Python - Math - Calculator Basics]]
GitHub link: [Python - Math - Calculator Basics](./Python%20-%20Math%20-%20Calculator%20Basics.md)

## Quick syntax fixes

1) Broken: not converting input
```python
# Broken
value = input('n: ')
print(value + 1)
```
<details><summary>Answer</summary>

```python
# Fixed
value = int(input('n: '))
print(value + 1)
```
Explanation: Convert input to int before arithmetic.
</details>

2) Broken: division by zero
```python
# Broken
print(5 / 0)
```
<details><summary>Answer</summary>

```python
# Fixed
den = 2
if den != 0:
    print(5 / den)
else:
    print('cannot divide by zero')
```
Explanation: Check divisor before dividing.
</details>

3) Broken: not printing result
```python
# Broken
def add(a, b):
    return a + b
add(2, 3)
```
<details><summary>Answer</summary>

```python
# Fixed
def add(a, b):
    return a + b
print(add(2, 3))
```
Explanation: Print returned value to see output.
</details>

---

## Easy

a) Read two numbers and print sum.

Starter code:
```python
# TODO: read two ints and print sum
```
<details><summary>Answer</summary>

```python
a = int(input('a: '))
b = int(input('b: '))
print(a + b)
```
Explanation: Convert inputs to integers before adding.
</details>

b) Read two numbers and print product.

Starter code:
```python
# TODO: read and multiply
```
<details><summary>Answer</summary>

```python
x = int(input('x: '))
y = int(input('y: '))
print(x * y)
```
Explanation: Multiply after converting inputs.
</details>

---

## Medium

a) Simple calculator: read a, b, and operator and print result.

Starter code:
```python
a = int(input('a: '))
b = int(input('b: '))
op = input('op: ')
# TODO: compute result
```
<details><summary>Answer</summary>

```python
a = int(input('a: '))
b = int(input('b: '))
op = input('op (+ - * /): ')
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b != 0:
        print(a / b)
    else:
        print('cannot divide by zero')
else:
    print('unknown operator')
```
Explanation: Use branching and check division by zero.
</details>

b) Add input validation: print 'bad input' on non-number.

Starter code:
```python
val = input('a: ')
# TODO: try/except convert
```
<details><summary>Answer</summary>

```python
val = input('a: ')
try:
    a = int(val)
    print(a)
except ValueError:
    print('bad input')
```
Explanation: Use try/except for validation.
</details>

---

## Hard

Compute expression string `2 + 3 * 4` and print result (educational use of `eval`).

Starter code:
```python
expr = '2 + 3 * 4'
# TODO: compute and print
```
<details><summary>Answer</summary>

```python
expr = '2 + 3 * 4'
print(eval(expr))  # careful with eval
```
Explanation: `eval` evaluates the expression string.
</details>
