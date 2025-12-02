---
tags: [python, exercises, debugging, errors]
difficulty: Beginner
---

# Python - Debugging - Common Errors — Exercises

See concept: [[Python - Debugging - Common Errors]]

GitHub link: [Python - Debugging - Common Errors](./Python%20-%20Debugging%20-%20Common%20Errors.md)

## Quick syntax fixes

1) NameError example
```python
# Broken
print(my_variable)
```
<details><summary>Answer</summary>

```python
# Fixed
my_variable = 1
print(my_variable)
```
Explanation: Define variables before use.
</details>

2) TypeError example
```python
# Broken
total = '2' + 3
```
<details><summary>Answer</summary>

```python
# Fixed
total = int('2') + 3
```
Explanation: Convert types to match before operations.
</details>

3) ValueError example
```python
# Broken
num = int('abc')
```
<details><summary>Answer</summary>

```python
# Fixed
try:
    num = int('abc')
except ValueError:
    num = None
```
Explanation: Use try/except to handle invalid conversions.
</details>

---

## Easy

a) Fix the NameError in this code and print 4.

Starter code:
```python
# TODO: make this print 4
value = 4
print(val)
```
<details><summary>Answer</summary>

```python
value = 4
print(value)
```
Explanation: Use the correct variable name.
</details>

b) Fix the TypeError: make `'4' + 1` give 5.

Starter code:
```python
# TODO: fix this to print 5
print('4' + 1)
```
<details><summary>Answer</summary>

```python
print(int('4') + 1)
```
Explanation: Convert string to int before adding.
</details>

---

## Medium

a) Handle a ValueError when converting input to int. If conversion fails, print 0.

Starter code:
```python
value = 'x'
# TODO: convert to int or print 0 if fails
```
<details><summary>Answer</summary>

```python
value = 'x'
try:
    number = int(value)
except ValueError:
    number = 0
print(number)
```
Explanation: Use try/except to provide a fallback value.
</details>

b) Fix the IndexError: remove the last item safely from a list that may be empty.

Starter code:
```python
items = []
# TODO: print and remove last item if list not empty, else print 'empty'
```
<details><summary>Answer</summary>

```python
items = []
if items:
    last = items.pop()
    print(last)
else:
    print('empty')
```
Explanation: Check for content before popping.
</details>

---

## Hard

Fix multiple errors in this function so it returns the sum of numbers in a list or 0 for non-lists.

Starter code:
```python
def sum_list(x):
    total = 0
    for i in x:
        total += i
    return total

print(sum_list([1,2,3]))
print(sum_list('no'))
```
<details><summary>Answer</summary>

```python
def sum_list(x):
    if not isinstance(x, list):
        return 0
    total = 0
    for i in x:
        total += i
    return total

print(sum_list([1,2,3]))
print(sum_list('no'))
```
Explanation: Validate the input type before iterating.
</details>
