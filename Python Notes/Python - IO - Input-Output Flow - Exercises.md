---
tags: [python, exercises, io, flow]
difficulty: Beginner
---

# Python - IO - Input-Output Flow — Exercises

See concept: [[Python - IO - Input-Output Flow]]
GitHub link: [Python - IO - Input-Output Flow](./Python%20-%20IO%20-%20Input-Output%20Flow.md)

## Quick syntax fixes

1) Broken: forgetting to close file after write
```python
# Broken
f = open('x.txt','w')
f.write('hi')
```
<details><summary>Answer</summary>

```python
# Fixed
with open('x.txt','w') as f:
    f.write('hi')
```
Explanation: `with` closes file automatically.
</details>

2) Broken: reading before writing when order matters
```python
# Broken
with open('x.txt') as f:
    print(f.read())
with open('x.txt','w') as f:
    f.write('hi')
```
<details><summary>Answer</summary>

```python
# Fixed
with open('x.txt','w') as f:
    f.write('hi')
with open('x.txt') as f:
    print(f.read())
```
Explanation: Write data before reading it if you expect content.
</details>

3) Broken: ignoring IO order in programs that interact with user
```python
# Broken
name = input('name:')
print('hello')
```
<details><summary>Answer</summary>

```python
# Fixed
name = input('name:')
print('hello', name)
```
Explanation: Use input values in output to complete IO flow.
</details>

---

## Easy

a) Read a name from input and print 'Hello <name>'.

Starter code:
```python
# TODO: read name and greet
pass
```
<details><summary>Answer</summary>

```python
name = input()
print('Hello', name)
```
Explanation: Simple input then output flow.
</details>

b) Read two numbers and print their sum.

Starter code:
```python
# TODO: read two numbers and print sum
pass
```
<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
print(a + b)
```
Explanation: Convert input strings to numbers before math.
</details>

---

## Medium

a) Read comma-separated numbers, sum them and print.

Starter code:
```python
s = input()
# TODO: parse and sum numbers
pass
```
<details><summary>Answer</summary>

```python
s = input()
nums = [int(x) for x in s.split(',')]
print(sum(nums))
```
Explanation: Split input then convert each piece.
</details>

b) Read a filename, try to open and print 'ok' or 'no file'.

Starter code:
```python
fname = input()
# TODO: open and print status
pass
```
<details><summary>Answer</summary>

```python
fname = input()
try:
    with open(fname) as f:
        print('ok')
except FileNotFoundError:
    print('no file')
```
Explanation: Connect input and file IO with error handling.
</details>

---

## Hard

Write a function that asks user for numbers until empty line, then returns their sum.

Starter code:
```python
def sum_until_empty():
    # TODO: read lines until empty and sum
    pass
print(sum_until_empty())
```
<details><summary>Answer</summary>

```python
def sum_until_empty():
    total = 0
    while True:
        line = input()
        if line == '':
            break
        total += int(line)
    return total
print(sum_until_empty())
```
Explanation: Loop with input until break condition, then return accumulated value.
</details>
