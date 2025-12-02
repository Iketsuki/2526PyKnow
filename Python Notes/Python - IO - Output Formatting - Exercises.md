---
tags: [python, exercises, io, formatting]
difficulty: Beginner
---

# Python - IO - Output Formatting — Exercises

See concept: [[Python - IO - Output Formatting]]
GitHub link: [Python - IO - Output Formatting](./Python%20-%20IO%20-%20Output%20Formatting.md)

## Quick syntax fixes

1) Broken: missing space in string concatenation
```python
# Broken
name = 'Ada'
print('Hello' + name)
```
<details><summary>Answer</summary>

```python
# Fixed
name = 'Ada'
print('Hello ' + name)
```
Explanation: Add a space when concatenating strings.
</details>

2) Broken: incorrect format placeholder
```python
# Broken
score = 90
print('Score: %')
```
<details><summary>Answer</summary>

```python
# Fixed
score = 90
print(f'Score: {score}')
```
Explanation: Use f-string or format to insert variables.
</details>

3) Broken: float formatting
```python
# Broken
value = 3.14159
print('value=', value)
```
<details><summary>Answer</summary>

```python
# Better
value = 3.14159
print(f'value={value:.2f}')
```
Explanation: Use format specifier `:.2f` to show two decimals.
</details>

---

## Easy

a) Print `Name: Alice, Age: 10` using f-string.

Starter code:
```python
name = 'Alice'
age = 10
# TODO: print formatted string
```
<details><summary>Answer</summary>

```python
name = 'Alice'
age = 10
print(f'Name: {name}, Age: {age}')
```
Explanation: f-strings insert variables into text.
</details>

b) Print number 3.14159 as `3.14`.

Starter code:
```python
value = 3.14159
# TODO: print with two decimals
```
<details><summary>Answer</summary>

```python
value = 3.14159
print(f'{value:.2f}')
```
Explanation: Use `:.2f` to format float to two decimals.
</details>

---

## Medium

a) Print a table of names and scores aligned in two columns.

Starter code:
```python
rows = [('Ana', 90), ('Ben', 85)]
# TODO: print each name left-aligned width 10 and score right-aligned width 3
```
<details><summary>Answer</summary>

```python
rows = [('Ana', 90), ('Ben', 85)]
for name, score in rows:
    print(f'{name:<10}{score:>3}')
```
Explanation: Use alignment specifiers `<` and `>` with widths.
</details>

b) Print a number padded with zeros to width 4 (e.g., 7 -> 0007).

Starter code:
```python
n = 7
# TODO: print 0007
```
<details><summary>Answer</summary>

```python
n = 7
print(f'{n:04d}')
```
Explanation: `04d` formats integer with leading zeros.
</details>

---

## Hard

Format `{'a':1,'b':2}` into `a=1, b=2`.

Starter code:
```python
data = {'a':1,'b':2}
# TODO: build and print 'a=1, b=2'
```
<details><summary>Answer</summary>

```python
data = {'a':1,'b':2}
out = ', '.join([f"{k}={v}" for k,v in data.items()])
print(out)
```
Explanation: Use join and f-strings to build the formatted string.
</details>
