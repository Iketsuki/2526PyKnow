---
tags: [python, exercises, debugging, tracebacks]
difficulty: Beginner
---

# Python - Debugging - Reading Tracebacks — Exercises

See concept: [[Python - Debugging - Reading Tracebacks]]

GitHub link: [Python - Debugging - Reading Tracebacks](./Python%20-%20Debugging%20-%20Reading%20Tracebacks.md)

## Quick syntax fixes

1) Broken code and traceback:
```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
Code that caused it:
```python
value = 5 + '3'
```
<details><summary>Answer</summary>

```python
# Fixed
value = 5 + int('3')
print(value)
```
Explanation: Convert the string to int before adding.
</details>

2) Broken code and traceback:
```text
IndexError: list index out of range
```
Code that caused it:
```python
lst = [1]
print(lst[1])
```
<details><summary>Answer</summary>

```python
lst = [1]
print(lst[0])
```
Explanation: Index 0 is the first item; index 1 is out of range.
</details>

3) Broken code and traceback:
```text
NameError: name 'numb' is not defined
```
Code that caused it:
```python
number = 5
print(numb)
```
<details><summary>Answer</summary>

```python
number = 5
print(number)
```
Explanation: Use the correct variable name.
</details>

---

## Easy

a) Read the traceback and fix this code: `a = 2 + '1'`.

Input example:
```text
code: a = 2 + '1'
```
Output example:
```text
3
```
Starter code:
```python
# TODO: fix the code so it prints 3
a = 2 + '1'
print(a)
```
<details><summary>Answer</summary>

```python
a = 2 + int('1')
print(a)
```
Explanation: Convert string '1' to int before adding.
</details>

b) Fix the index error: `lst = [10]; print(lst[2])` to print the last item.

Starter code:
```python
lst = [10]
# TODO: print the last item
print(lst[2])
```
<details><summary>Answer</summary>

```python
lst = [10]
print(lst[-1])
```
Explanation: Use index -1 to get the last item safely.
</details>

---

## Medium

a) Given this traceback, fix the code:
```text
TypeError: 'int' object is not iterable
```
Code:
```python
num = 5
for x in num:
    print(x)
```
Starter code:
```python
num = 5
# TODO: print numbers from 0 up to num-1
for x in num:
    print(x)
```
<details><summary>Answer</summary>

```python
num = 5
for x in range(num):
    print(x)
```
Explanation: Use `range()` to iterate a number of times.
</details>

b) Fix the NameError: `print(value)` when `value` is set inside a function but not returned.

Starter code:
```python
def set_val():
    v = 9
set_val()
print(v)
```
<details><summary>Answer</summary>

```python
def set_val():
    return 9
v = set_val()
print(v)
```
Explanation: Return values from a function to use them outside.
</details>

---

## Hard

Read the traceback and fix the code that causes `ZeroDivisionError`.

Starter code:
```python
def half(n):
    return n / 0
print(half(4))
```
Output example:
```text
2.0
```
<details><summary>Answer</summary>

```python
def half(n):
    return n / 2
print(half(4))
```
Explanation: Divide by 2, not 0.
</details>
