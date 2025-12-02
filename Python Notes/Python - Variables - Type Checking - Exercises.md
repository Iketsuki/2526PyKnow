---
tags: [python, exercises, variables, types]
difficulty: Beginner
---

# Python - Variables - Type Checking — Exercises

See concept: [[Python - Variables - Type Checking]]
GitHub link: [Python - Variables - Type Checking](./Python%20-%20Variables%20-%20Type%20Checking.md)

## Quick syntax fixes

1) Broken code: printing the type wrong
```python
# Broken example
value = 5
print(type(value))
```
<details><summary>Answer</summary>

```python
# Fixed (this was actually fine; explain output)
value = 5
print(type(value))  # <class 'int'> prints the type
```
Explanation: `type()` prints the type object like `<class 'int'>`.
</details>

2) Broken code: comparing type objects wrongly
```python
# Broken example
value = 'hello'
if type(value) == 'str':
    print('yes')
```
<details><summary>Answer</summary>

```python
# Fixed
value = 'hello'
if type(value) == str:
    print('yes')
```
Explanation: `str` is a type object, not the string 'str'.
</details>

3) Broken code: using isinstance the wrong way
```python
# Broken example
value = 3.5
if isinstance(value, 'float'):
    print('float')
```
<details><summary>Answer</summary>

```python
# Fixed
value = 3.5
if isinstance(value, float):
    print('float')
```
Explanation: `isinstance` takes the type object, not a string.
</details>

---

## Easy

a) Print the type of the variable `x = 10`.

Input example:
```text
None
```
Output example:
```text
<class 'int'>
```
Starter code:
```python
x = 10  # x means the number
# TODO: print the type of x
```
<details><summary>Answer</summary>

```python
x = 10
print(type(x))
```
Explanation: `type()` shows the Python type of a value.
</details>

b) Check if `y = '5'` is a string using `isinstance` and print `True` or `False`.

Starter code:
```python
y = '5'  # y means the text '5'
# TODO: print True if y is str else False
```
<details><summary>Answer</summary>

```python
y = '5'
print(isinstance(y, str))
```
Explanation: `isinstance(y, str)` returns True if y is a string.
</details>

---

## Medium

a) Read a value as text, try to convert to int. If it fails, print 'not a number'.

Input example:
```text
value = '8'
```
Output example:
```text
8
```
Starter code:
```python
value = '8'  # value means the text input
# TODO: try to convert value to int and print it; on error print 'not a number'
```
<details><summary>Answer</summary>

```python
value = '8'
try:
    number = int(value)
    print(number)
except ValueError:
    print('not a number')
```
Explanation: Use try/except to handle invalid conversions.
</details>

b) Given `items = [1, 'a', 3]`, build a new list with only the integers.

Input example:
```text
items = [1, 'a', 3]
```
Output example:
```text
[1, 3]
```
Starter code:
```python
items = [1, 'a', 3]  # items means the original list
# TODO: create ints_only with integers from items
print(items)
```
<details><summary>Answer</summary>

```python
items = [1, 'a', 3]
ints_only = []
for item in items:
    if isinstance(item, int):
        ints_only.append(item)
print(ints_only)
```
Explanation: Use isinstance to filter by type.
</details>

---

## Hard

Write a function `safe_add(a, b)` that adds a and b if both are numbers, else return None.

Input example:
```text
safe_add(2, 3)
safe_add(2, 'x')
```
Output example:
```text
5
None
```
Starter code:
```python
def safe_add(a, b):
    # a and b mean two values to add
    # TODO: return a + b if both are int or float, else return None
    pass
print(safe_add(2, 3))
print(safe_add(2, 'x'))
```
<details><summary>Answer</summary>

```python
def safe_add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    return None
print(safe_add(2, 3))
print(safe_add(2, 'x'))
```
Explanation: Use isinstance with a tuple of allowed types.
</details>
