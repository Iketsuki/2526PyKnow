---
tags: [python, exercises, variables]
difficulty: Beginner
---

# Exercises — Variables: Assignment Basics

See concept: [[Python - Variables - Assignment Basics]]

GitHub link: [Python - Variables - Assignment Basics](./Python%20-%20Variables%20-%20Assignment%20Basics.md)

### Quick syntax fixes

1) Using = in place of == (for comparison) in prints:
```python
x = 5
if x = 5:
    print('yes')
```
<details><summary>Answer</summary>

```python
x = 5
if x == 5:
    print('yes')
```
Explanation: Use `==` to compare values; `=` assigns values.
</details>

2) Missing assignment before use:
```python
print(name)
```
<details><summary>Answer</summary>

```python
name = 'Ana'
print(name)
```
Explanation: Assign a value to the variable before printing it.
</details>

3) Wrong assignment to multiple variables:
```python
a = b = 1, 2
```
<details><summary>Answer</summary>

```python
a, b = 1, 2
```
Explanation: Use tuple unpacking for multiple assignments.
</details>

---

## Easy

### a) Assign and print a name

Input example:
```text
Ana
```

Output example:
```text
Hello Ana
```

Starter code:
```python
name = input()  # name is the learner's name
# TODO: print 'Hello ' followed by the name
```

<details><summary>Answer</summary>

```python
name = input()
print('Hello', name)
```
Explanation: Use `print` with comma to add a space between values.
</details>

### b) Assign two numbers and print their sum

Input example:
```text
3
4
```

Output example:
```text
7
```

Starter code:
```python
a = int(input())  # a is first number
b = int(input())  # b is second number
# TODO: print the sum of a and b
```

<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
print(a + b)
```
Explanation: Convert input to int before arithmetic.
</details>

---

## Medium

### a) Swap values using a temporary variable

Input example:
```text
x
y
```

Output example:
```text
y
x
```

Starter code:
```python
first = input()   # first value
second = input()  # second value
# TODO: swap values using a temp variable and print them in new order
```

<details><summary>Answer</summary>

```python
first = input()
second = input()
temp = first
first = second
second = temp
print(first)
print(second)
```
Explanation: Use a temporary variable to hold one value while swapping.
</details>

### b) Reassign to new value and print

Input example:
```text
5
```

Output example:
```text
10
```

Starter code:
```python
number = int(input())  # number is an integer
# TODO: reassign number to be number*2 then print it
```

<details><summary>Answer</summary>

```python
number = int(input())
number = number * 2
print(number)
```
Explanation: Variables can be reassigned to new values.
</details>

---

## Hard

### Single: Read three values and assign to a tuple, then print the middle one

Input example:
```text
A
B
C
```

Output example:
```text
B
```

Starter code:
```python
v1 = input()  # first value
v2 = input()  # second value
v3 = input()  # third value
# TODO: put them into a tuple and print the second item
```

<details><summary>Answer</summary>

```python
v1 = input()
v2 = input()
v3 = input()
vals = (v1, v2, v3)
print(vals[1])
```
Explanation: Tuples index like lists; index 1 is the second item.
</details>
