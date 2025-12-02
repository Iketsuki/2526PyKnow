---
tags: [python, exercises, variables]
difficulty: Beginner
---

# Exercises — Variables: Types Basics

See concept: [[Python - Variables - Types Basics]]

GitHub link: [Python - Variables - Types Basics](./Python%20-%20Variables%20-%20Types%20Basics.md)

### Quick syntax fixes

1) Using quotes for number literal:
```python
n = '5'
print(n + 1)
```
<details><summary>Answer</summary>

```python
n = 5
print(n + 1)
```
Explanation: Numbers should not be quoted when intended as numeric values.
</details>

2) Mixing types in list:
```python
lst = [1, '2', 3]
print(sum(lst))
```
<details><summary>Answer</summary>

```python
lst = [1, 2, 3]
print(sum(lst))
```
Explanation: Keep list items the same type for numeric operations.
</details>

3) Using boolean as string:
```python
b = 'True'
if b:
    print('Yes')
```
<details><summary>Answer</summary>

```python
b = True
if b:
    print('Yes')
```
Explanation: Use boolean values True/False (no quotes) for logic.
</details>

---

## Easy

### a) Identify type of input

Input example:
```text
Hello
```

Output example:
```text
str
```

Starter code:
```python
value = input()  # value is a string from input
# TODO: print the type name of value (use type() and __name__)
```

<details><summary>Answer</summary>

```python
value = input()
print(type(value).__name__)
```
Explanation: `input()` returns a string; print the type name for clarity.
</details>

### b) Convert number string to int then show type

Input example:
```text
5
```

Output example:
```text
int
```

Starter code:
```python
s = input()  # s is a string like '5'
# TODO: convert s to int and print its type name
```

<details><summary>Answer</summary>

```python
s = input()
num = int(s)
print(type(num).__name__)
```
Explanation: `int()` makes a number from a numeric string.
</details>

---

## Medium

### a) Sum three numbers and show float result

Input example:
```text
1
2
3
```

Output example:
```text
6.0
```

Starter code:
```python
# read 3 numbers as ints then print their sum as a float
```

<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
c = int(input())
print(float(a + b + c))
```
Explanation: Convert sum to float using `float()` to show decimal point.
</details>

### b) Show boolean result of empty string

Input example:
```text

```

Output example:
```text
False
```

Starter code:
```python
s = input()
# TODO: print True/False whether s is truthy (non-empty)
```

<details><summary>Answer</summary>

```python
s = input()
print(bool(s))
```
Explanation: `bool('')` is False; non-empty strings are True.
</details>

---

## Hard

### Single: Create three variables of different types and print their types

Input example:
```text
(no input)
```

Output example:
```text
int
str
list
```

Starter code:
```python
# TODO: set a number, a text, and a list; then print each type name on its own line
```

<details><summary>Answer</summary>

```python
n = 5
s = 'hello'
l = [1, 2, 3]
print(type(n).__name__)
print(type(s).__name__)
print(type(l).__name__)
```
Explanation: Use `type(...).__name__` to show the type names plainly for learners.
</details>
