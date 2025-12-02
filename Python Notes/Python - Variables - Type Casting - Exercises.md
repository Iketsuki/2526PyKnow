---
tags: [python, exercises, variables]
difficulty: Beginner
---

# Exercises — Variables: Type Casting

See concept: [[Python - Variables - Type Casting]]

GitHub link: [Python - Variables - Type Casting](./Python%20-%20Variables%20-%20Type%20Casting.md)

### Quick syntax fixes

1) Forgetting parentheses around int():
```python
n = int
n = n('5')
```
<details><summary>Answer</summary>

```python
n = int('5')
```
Explanation: Call `int()` directly with the string.
</details>

2) Casting non-numeric string:
```python
x = int('a')
```
<details><summary>Answer</summary>

```python
# This will raise ValueError; show correct numeric example:
x = int('5')
```
Explanation: Only numeric strings can be converted to int.
</details>

3) Using str for concatenation without cast:
```python
print('Age: ' + 5)
```
<details><summary>Answer</summary>

```python
print('Age: ' + str(5))
```
Explanation: Convert numbers to strings before concatenation.
</details>

---

## Easy

### a) Convert input to int and add 2

Input example:
```text
3
```

Output example:
```text
5
```

Starter code:
```python
s = input()  # s is a number string
# TODO: convert s to int, add 2, and print
```

<details><summary>Answer</summary>

```python
s = input()
print(int(s) + 2)
```
Explanation: Use `int()` to convert string to integer.
</details>

### b) Convert number to string and join

Input example:
```text
4
```

Output example:
```text
Number: 4
```

Starter code:
```python
n = int(input())  # n is integer
# TODO: print 'Number: ' + n using string conversion
```

<details><summary>Answer</summary>

```python
n = int(input())
print('Number: ' + str(n))
```
Explanation: Use `str()` to make a string from a number.
</details>

---

## Medium

### a) Convert three inputs to numbers and print their average as float

Input example:
```text
1
2
3
```

Output example:
```text
2.0
```

Starter code:
```python
# read three numbers as strings, convert to int, compute average and print as float
```

<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
c = int(input())
print((a + b + c) / 3)
```
Explanation: Division returns float in Python 3.
</details>

### b) Safe int conversion with default

Input example:
```text
x
```

Output example:
```text
0
```

Starter code:
```python
s = input()  # s may not be numeric
# TODO: try to convert s to int, if fail print 0
```

<details><summary>Answer</summary>

```python
s = input()
try:
    n = int(s)
except ValueError:
    n = 0
print(n)
```
Explanation: Use try/except to handle bad numeric inputs safely.
</details>

---

## Hard

### Single: Read a number, cast to float, format with two decimals

Input example:
```text
3
```

Output example:
```text
3.00
```

Starter code:
```python
s = input()  # number string
# TODO: convert to float and print with two decimal places
```

<details><summary>Answer</summary>

```python
s = input()
val = float(s)
print(f"{val:.2f}")
```
Explanation: Use f-string formatting to show two decimal places.
</details>
