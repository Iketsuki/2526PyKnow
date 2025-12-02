---
tags: [python, exercises, io, f-strings]
difficulty: Beginner
---

# Python - IO - Formatted Strings (f-strings) — Exercises

See concept: [[Python - IO - Formatted Strings (f-strings)]]
GitHub link: [Python - IO - Formatted Strings (f-strings)](./Python%20-%20IO%20-%20Formatted%20Strings%20%28f-strings%29.md)

## Quick syntax fixes

1) Broken: f-string missing `f`
```python
# Broken
name = 'Ada'
print('Hello {name}')
```
<details><summary>Answer</summary>

```python
# Fixed
name = 'Ada'
print(f'Hello {name}')
```
Explanation: Add `f` before string to enable variable interpolation.
</details>

2) Broken: wrong braces
```python
# Broken
print(f'Value: {value')
```
<details><summary>Answer</summary>

```python
# Fixed
value = 3
print(f'Value: {value}')
```
Explanation: Use matching braces in f-strings.
</details>

3) Broken: formatting number
```python
# Broken
pi = 3.14159
print(f'pi = {pi:.2f')
```
<details><summary>Answer</summary>

```python
# Fixed
pi = 3.14159
print(f'pi = {pi:.2f}')
```
Explanation: Close the format specifier with `}`.
</details>

---

## Easy

a) Print `Hello Alice` using f-string and variable `name='Alice'`.

Starter code:
```python
name = 'Alice'
# TODO: print greeting using f-string
```
<details><summary>Answer</summary>

```python
name = 'Alice'
print(f'Hello {name}')
```
Explanation: f-strings place variables inside braces.
</details>

b) Print a formatted price `£3.50` using `price = 3.5`.

Starter code:
```python
price = 3.5
# TODO: print with two decimals and £ sign
```
<details><summary>Answer</summary>

```python
price = 3.5
print(f'£{price:.2f}')
```
Explanation: Use `:.2f` to format float to two decimals.
</details>

---

## Medium

a) Use f-string to print `Name: X, Age: Y` for tuple `('X', 10)`.

Starter code:
```python
person = ('X', 10)
# TODO: print using f-string and tuple values
```
<details><summary>Answer</summary>

```python
person = ('X', 10)
name, age = person
print(f'Name: {name}, Age: {age}')
```
Explanation: Unpack tuple then use f-string.
</details>

b) Align text with f-strings to width 10.

Starter code:
```python
word = 'hi'
# TODO: print word left aligned width 10
```
<details><summary>Answer</summary>

```python
word = 'hi'
print(f'{word:<10}')
```
Explanation: Use `<10` inside f-string for left alignment.
</details>

---

## Hard

Given values, print `Item: apple (x3) - £1.50 each - total £4.50` using f-strings and computed total.

Starter code:
```python
item = 'apple'
count = 3
price = 1.5
# TODO: compute total and print formatted sentence
```
<details><summary>Answer</summary>

```python
item = 'apple'
count = 3
price = 1.5
total = count * price
print(f'Item: {item} (x{count}) - £{price:.2f} each - total £{total:.2f}')
```
Explanation: Compute total and format floats to two decimals.
</details>
