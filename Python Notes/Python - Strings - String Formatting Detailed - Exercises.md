---
tags: [python, exercises, strings, formatting]
difficulty: Beginner
---

# Python - Strings - String Formatting Detailed — Exercises

See concept: [[Python - Strings - String Formatting Detailed]]
GitHub link: [Python - Strings - String Formatting Detailed](./Python%20-%20Strings%20-%20String%20Formatting%20Detailed.md)

## Quick syntax fixes

1) Broken: using `%` with wrong types
```python
print('%d' % 'x')
```
<details><summary>Answer</summary>

```python
print('%s' % 'x')
```
Explanation: use format specifiers that match data types.
</details>

2) Broken: f-string missing braces
```python
name = 'Ann'
print(f'Hello name')
```
<details><summary>Answer</summary>

```python
name = 'Ann'
print(f'Hello {name}')
```
Explanation: include variable inside `{}` for f-strings.
</details>

3) Broken: using `.format` with wrong index
```python
print('{} {1}'.format('a'))
```
<details><summary>Answer</summary>

```python
print('{} {}'.format('a','b'))
```
Explanation: supply values for each placeholder index.
</details>

---

## Easy

a) Use an f-string to print `Name: <name>` where `<name>` is input.

Starter code:
```python
name = input()
# TODO: print using f-string
pass
```
<details><summary>Answer</summary>

```python
name = input()
print(f'Name: {name}')
```
Explanation: f-strings insert variables easily.
</details>

b) Use `.format` to print `Age: <age>` where age is input.

Starter code:
```python
age = input()
# TODO: print using format
pass
```
<details><summary>Answer</summary>

```python
age = input()
print('Age: {}'.format(age))
```
Explanation: `.format` replaces placeholders with values.
</details>

---

## Medium

a) Print a number with two decimal places using format.

Starter code:
```python
n = float(input())
# TODO: print with 2 decimals
pass
```
<details><summary>Answer</summary>

```python
n = float(input())
print('{:.2f}'.format(n))
```
Explanation: `.2f` formats float to two decimals.
</details>

b) Use f-string to pad a name to 10 characters left aligned.

Starter code:
```python
name = input()
# TODO: pad name
pass
```
<details><summary>Answer</summary>

```python
name = input()
print(f'{name:<10}')
```
Explanation: `:<10` left-aligns within width 10.
</details>

---

## Hard

Write a function that takes a list of (name,score) and prints a table with names left aligned width 10 and scores right aligned width 5.

Starter code:
```python
def print_table(rows):
    # TODO: format rows
    pass

print_table([('Ann',10),('Bob',2)])
```
<details><summary>Answer</summary>

```python
def print_table(rows):
    for name, score in rows:
        print(f'{name:<10}{score:5d}')

print_table([('Ann',10),('Bob',2)])
```
Explanation: use width specifiers to align columns.
</details>
