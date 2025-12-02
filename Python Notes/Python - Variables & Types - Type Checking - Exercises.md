---
tags: [python, exercises, variables, types]
difficulty: Beginner
---

# Python - Variables & Types - Type Checking — Exercises

See concept: [[Python - Variables & Types - Type Checking]]
GitHub link: [Python - Variables & Types - Type Checking](./Python%20-%20Variables%20%26%20Types%20-%20Type%20Checking.md)

## Quick syntax fixes

1) Broken: mixing types in addition
```python
# Broken
a = '5'
b = 3
print(a + b)
```
<details><summary>Answer</summary>

```python
# Fixed
a = '5'
b = 3
print(int(a) + b)
```
Explanation: Convert string to int before adding.
</details>

2) Broken: wrong type for loop counter
```python
# Broken
for i in range('3'):
    print(i)
```
<details><summary>Answer</summary>

```python
# Fixed
for i in range(3):
    print(i)
```
Explanation: range needs an integer.
</details>

3) Broken: expecting list but have string
```python
# Broken
name = 'Bob'
print(name.append('son'))
```
<details><summary>Answer</summary>

```python
# Fixed
name = 'Bob'
name2 = name + 'son'
print(name2)
```
Explanation: Strings do not have append; use concatenation.
</details>

---

## Easy

a) Check the type of a variable and print it.

Starter code:
```python
x = 5
# TODO: print the type of x
pass
```
<details><summary>Answer</summary>

```python
x = 5
print(type(x))
```
Explanation: type() shows the Python type of a value.
</details>

b) Convert a string number to integer and add.

Starter code:
```python
s = '10'
# TODO: convert and add 5, then print
pass
```
<details><summary>Answer</summary>

```python
s = '10'
v = int(s) + 5
print(v)
```
Explanation: Use int() to convert string to integer.
</details>

---

## Medium

a) Write code that tests if a value is a string or number and prints a message.

Starter code:
```python
value = 'hello'
# TODO: if value is str print "string" else print "not string"
pass
```
<details><summary>Answer</summary>

```python
value = 'hello'
if isinstance(value, str):
    print('string')
else:
    print('not string')
```
Explanation: Use isinstance for type checks.
</details>

b) Safely convert input to int; if fails, print error.

Starter code:
```python
user = 'abc'
# TODO: try to convert to int, print 'error' on failure
pass
```
<details><summary>Answer</summary>

```python
user = 'abc'
try:
    v = int(user)
    print(v)
except ValueError:
    print('error')
```
Explanation: Use try/except to handle bad conversions.
</details>

---

## Hard

Write a function that returns True if two values have the same type, False otherwise.

Starter code:
```python
def same_type(a, b):
    # TODO: return True if types match
    pass
print(same_type(1, 2))    # True
print(same_type(1, '1'))  # False
```
<details><summary>Answer</summary>

```python
def same_type(a, b):
    return type(a) is type(b)
print(same_type(1, 2))    # True
print(same_type(1, '1'))  # False
```
Explanation: Compare types with `type()`.
</details>
