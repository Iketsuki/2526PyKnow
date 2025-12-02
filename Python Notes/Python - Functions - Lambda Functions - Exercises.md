---
tags: [python, exercises, functions, lambda]
difficulty: Beginner
---

# Python - Functions - Lambda Functions — Exercises

See concept: [[Python - Functions - Lambda Functions]]
GitHub link: [Python - Functions - Lambda Functions](./Python%20-%20Functions%20-%20Lambda%20Functions.md)

## Quick syntax fixes

1) Broken: using `lambda` without assignment
```python
# Broken
lambda x: x+1
```
<details><summary>Answer</summary>

```python
# Fixed
f = lambda x: x + 1
print(f(2))
```
Explanation: Assign lambda to a name to call it.
</details>

2) Broken: missing argument in lambda
```python
# Broken
f = lambda: x+1
print(f(2))
```
<details><summary>Answer</summary>

```python
# Fixed
f = lambda x: x + 1
print(f(2))
```
Explanation: Lambda parameters must match how you call it.
</details>

3) Broken: using lambda for multi-line body
```python
# Broken
f = lambda x:
    y = x+1
    return y
```
<details><summary>Answer</summary>

```python
# Fixed
def f(x):
    y = x + 1
    return y
print(f(2))
```
Explanation: Lambdas must be single expressions; use def for longer code.
</details>

---

## Easy

a) Create a lambda that adds 2 and use it.

Starter code:
```python
# TODO: make lambda add2 and print add2(3)
pass
```
<details><summary>Answer</summary>

```python
add2 = lambda x: x + 2
print(add2(3))
```
Explanation: Simple lambdas are short functions.
</details>

b) Use lambda with `map` to double numbers in a list.

Starter code:
```python
nums = [1,2,3]
# TODO: use map + lambda to double and print list
pass
```
<details><summary>Answer</summary>

```python
nums = [1,2,3]
doubled = list(map(lambda x: x*2, nums))
print(doubled)
```
Explanation: `map` applies function to each item.
</details>

---

## Medium

a) Use lambda with `sorted` key to sort words by length.

Starter code:
```python
words = ['a','abc','ab']
# TODO: sort by len using lambda and print
pass
```
<details><summary>Answer</summary>

```python
words = ['a','abc','ab']
words_sorted = sorted(words, key=lambda w: len(w))
print(words_sorted)
```
Explanation: `key` receives a function to compute sort key.
</details>

b) Replace a small function with an equivalent lambda in a call.

Starter code:
```python
def inc(x):
    return x+1
print(inc(4))
# TODO: call with lambda instead and print
pass
```
<details><summary>Answer</summary>

```python
def inc(x):
    return x+1
print((lambda x: x+1)(4))
```
Explanation: You can call a lambda immediately in an expression.
</details>

---

## Hard

Write a function `make_adder(n)` that returns a lambda adding `n` to its input.

Starter code:
```python
def make_adder(n):
    # TODO: return lambda x: x + n
    pass
add5 = make_adder(5)
print(add5(2))  # expect 7
```
<details><summary>Answer</summary>

```python
def make_adder(n):
    return lambda x: x + n
add5 = make_adder(5)
print(add5(2))  # 7
```
Explanation: Lambdas can close over outer variables.
</details>
