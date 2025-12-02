---
tags: [python, exercises, io]
difficulty: Beginner
---

# Python - I\O - Input & Output (Day 1) — Exercises

See concept: [[Python - I/O - Input & Output (Day 1)]]
GitHub link: [Python - I\O - Input & Output (Day 1)](./Python%20-%20I%5CO%20-%20Input%20%26%20Output%20(Day%201).md)

## Quick syntax fixes

1) Broken: missing input prompt
```python
name = input
```
<details><summary>Answer</summary>

```python
name = input()
```
Explanation: call input() to read user text.
</details>

2) Broken: printing a variable name instead of value
```python
name = input()
print('name')
```
<details><summary>Answer</summary>

```python
name = input()
print(name)
```
Explanation: print the variable, not the string 'name'.
</details>

3) Broken: reading number but not converting
```python
x = input()
print(x + 1)
```
<details><summary>Answer</summary>

```python
x = int(input())
print(x + 1)
```
Explanation: convert to int before arithmetic.
</details>

---

## Easy

a) Read a name and print "Hello <name>".

Starter code:
```python
# TODO: read and greet
pass
```
<details><summary>Answer</summary>

```python
name = input()
print('Hello', name)
```
Explanation: simple input-output.
</details>

b) Read a number and print number plus 5.

Starter code:
```python
# TODO: read number and add 5
pass
```
<details><summary>Answer</summary>

```python
n = int(input())
print(n + 5)
```
Explanation: convert input before math.
</details>

---

## Medium

a) Read two words and print them separated by a dash.

Starter code:
```python
# TODO: read two words and print with '-'
pass
```
<details><summary>Answer</summary>

```python
a = input()
b = input()
print(a + '-' + b)
```
Explanation: combine strings with operator.
</details>

b) Read a number N and then read N lines, print their count.

Starter code:
```python
# TODO: read N and then N lines
pass
```
<details><summary>Answer</summary>

```python
n = int(input())
for i in range(n):
    _ = input()
print(n)
```
Explanation: loop to consume input lines.
</details>

---

## Hard

Write a function that reads input until an empty line and returns a list of strings.

Starter code:
```python
def read_lines():
    # TODO: read until empty and return list
    pass

print(read_lines())
```
<details><summary>Answer</summary>

```python
def read_lines():
    out = []
    while True:
        line = input()
        if line == '':
            break
        out.append(line)
    return out

print(read_lines())
```
Explanation: loop reads until blank line.
</details>
