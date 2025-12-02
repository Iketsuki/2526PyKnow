---
tags: [python, exercises, strings, formatting]
difficulty: Beginner
---

# Python - Strings - String Formatting — Exercises

See concept: [[Python - Strings - String Formatting]]
GitHub link: [Python - Strings - String Formatting](./Python%20-%20Strings%20-%20String%20Formatting.md)

## Quick syntax fixes

1) Broken: using `+` with non-strings
```python
print('Age: ' + 5)
```
<details><summary>Answer</summary>

```python
print('Age:', 5)
```
Explanation: separate values with comma or convert to str.
</details>

2) Broken: wrong format placeholder
```python
print('Hello %d' % 'Ann')
```
<details><summary>Answer</summary>

```python
print('Hello %s' % 'Ann')
```
Explanation: `%s` works for strings.
</details>

3) Broken: missing f-string braces
```python
name = 'Ann'
print(f'Hi name')
```
<details><summary>Answer</summary>

```python
name = 'Ann'
print(f'Hi {name}')
```
Explanation: include variable inside `{}`.
</details>

---

## Easy

a) Use concatenation to print 'Hello' and a name from input.

Starter code:
```python
name = input()
# TODO: print greeting
pass
```
<details><summary>Answer</summary>

```python
name = input()
print('Hello ' + name)
```
Explanation: use `+` to join strings.
</details>

b) Use `%` formatting to print 'Score: <n>'.

Starter code:
```python
n = int(input())
# TODO: print using %
pass
```
<details><summary>Answer</summary>

```python
n = int(input())
print('Score: %d' % n)
```
Explanation: old-style `%` works for simple formatting.
</details>

---

## Medium

a) Pad a number with zeros to width 4 using format.

Starter code:
```python
n = int(input())
# TODO: print padded
pass
```
<details><summary>Answer</summary>

```python
n = int(input())
print('{:04d}'.format(n))
```
Explanation: `04d` pads with zeros to 4 digits.
</details>

b) Create a string using `.format` with named fields.

Starter code:
```python
name = input()
age = input()
# TODO: use named fields
pass
```
<details><summary>Answer</summary>

```python
name = input()
age = input()
print('Name: {n}, Age: {a}'.format(n=name, a=age))
```
Explanation: named placeholders improve clarity.
</details>

---

## Hard

Write a function that formats a price in dollars with 2 decimals and a leading `$`.

Starter code:
```python
def fmt_price(n):
    # TODO: return formatted price
    pass

print(fmt_price(3.5))
```
<details><summary>Answer</summary>

```python
def fmt_price(n):
    return '${:.2f}'.format(n)

print(fmt_price(3.5))
```
Explanation: include `$` and format to two decimals.
</details>
