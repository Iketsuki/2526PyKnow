---
tags: [python, exercises, math, functions]
difficulty: Beginner
---

# Python - Math - Simple Math Functions — Exercises

See concept: [[Python - Math - Simple Math Functions]]
GitHub link: [Python - Math - Simple Math Functions](./Python%20-%20Math%20-%20Simple%20Math%20Functions.md)

## Quick syntax fixes

1) Broken: missing return
```python
# Broken
def add(a, b):
    s = a + b
```
<details><summary>Answer</summary>

```python
# Fixed
def add(a, b):
    return a + b
```
Explanation: Functions should return values to the caller.
</details>

2) Broken: wrong function call
```python
# Broken
print(add 2, 3)
```
<details><summary>Answer</summary>

```python
# Fixed
print(add(2, 3))
```
Explanation: Call functions with parentheses.
</details>

3) Broken: wrong parameter syntax
```python
# Broken
def square(n=):
    return n * n
```
<details><summary>Answer</summary>

```python
# Fixed
def square(n):
    return n * n
```
Explanation: Use valid parameter syntax.
</details>

---

## Easy

a) Write `add_one(n)` that returns n + 1 and print `add_one(4)`.

Starter code:
```python
def add_one(n):
    # TODO: return n + 1
    pass
print(add_one(4))
```
<details><summary>Answer</summary>

```python
def add_one(n):
    return n + 1
print(add_one(4))
```
Explanation: Return the computed value from the function.
</details>

b) Write `square(n)` and print `square(3)`.

Starter code:
```python
def square(n):
    # TODO: return n * n
    pass
print(square(3))
```
<details><summary>Answer</summary>

```python
def square(n):
    return n * n
print(square(3))
```
Explanation: Multiply to get square.
</details>

---

## Medium

a) `sum_list(lst)` returns sum of numbers.

Starter code:
```python
def sum_list(lst):
    # TODO: return sum
    pass
print(sum_list([1,2,3]))
```
<details><summary>Answer</summary>

```python
def sum_list(lst):
    total = 0
    for v in lst:
        total += v
    return total
print(sum_list([1,2,3]))
```
Explanation: Loop to accumulate.
</details>

b) `max_in_list(lst)` returns the largest number.

Starter code:
```python
def max_in_list(lst):
    # TODO: return largest
    pass
print(max_in_list([2,9,4]))
```
<details><summary>Answer</summary>

```python
def max_in_list(lst):
    m = lst[0]
    for v in lst:
        if v > m:
            m = v
    return m
print(max_in_list([2,9,4]))
```
Explanation: Keep track of the maximum while iterating.
</details>

---

## Hard

Write `mean_and_count_even(lst)` returning (mean, even_count).

Starter code:
```python
def mean_and_count_even(lst):
    # TODO: return (mean, even_count)
    pass
print(mean_and_count_even([1,2,3,4]))
```
<details><summary>Answer</summary>

```python
def mean_and_count_even(lst):
    total = 0
    count_even = 0
    for v in lst:
        total += v
        if v % 2 == 0:
            count_even += 1
    mean = total / len(lst)
    return mean, count_even
print(mean_and_count_even([1,2,3,4]))
```
Explanation: Use loop to sum and count evens then compute mean.
</details>
