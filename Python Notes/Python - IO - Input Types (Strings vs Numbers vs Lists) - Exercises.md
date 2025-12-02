---
tags: [python, exercises, io, types]
difficulty: Beginner
---

# Python - IO - Input Types (Strings vs Numbers vs Lists) — Exercises

See concept: [[Python - IO - Input Types (Strings vs Numbers vs Lists)]]
GitHub link: [Python - IO - Input Types (Strings vs Numbers vs Lists)](./Python%20-%20IO%20-%20Input%20Types%20%28Strings%20vs%20Numbers%20vs%20Lists%29.md)

## Quick syntax fixes

1) Broken: input() returns string, can't add to number
```python
# Broken
v = input()
print(v + 1)
```
<details><summary>Answer</summary>

```python
# Fixed
v = input()
print(int(v) + 1)
```
Explanation: Convert input string to int when needed.
</details>

2) Broken: reading comma list but not splitting
```python
# Broken
s = input()
print(s[0])
```
<details><summary>Answer</summary>

```python
# Fixed
s = input()
parts = s.split(',')
print(parts[0])
```
Explanation: Use `split` to get list items from input text.
</details>

3) Broken: joining numbers with string without convert
```python
# Broken
n = 5
print('value: ' + n)
```
<details><summary>Answer</summary>

```python
# Fixed
n = 5
print('value: ' + str(n))
```
Explanation: Convert numbers to strings before concatenation.
</details>

---

## Easy

a) Read input '3' as string then convert to int and add 2.

Starter code:
```python
s = '3'
# TODO: convert to int and add 2
pass
```
<details><summary>Answer</summary>

```python
s = '3'
v = int(s) + 2
print(v)
```
Explanation: Use `int()` to convert numeric strings.
</details>

b) Read a comma-separated list string and print the second item.

Starter code:
```python
s = 'a,b,c'
# TODO: split and print second
pass
```
<details><summary>Answer</summary>

```python
s = 'a,b,c'
parts = s.split(',')
print(parts[1])
```
Explanation: `split` creates a list from input text.
</details>

---

## Medium

a) Safely convert input to float; if fails print 'bad'.

Starter code:
```python
user = '3.5'
# TODO: try float conversion else print 'bad'
pass
```
<details><summary>Answer</summary>

```python
user = '3.5'
try:
    v = float(user)
    print(v)
except ValueError:
    print('bad')
```
Explanation: Use try/except for conversions.
</details>

b) Read numbers separated by spaces and print their sum.

Starter code:
```python
s = '1 2 3'
# TODO: split, convert, sum, print
pass
```
<details><summary>Answer</summary>

```python
s = '1 2 3'
nums = [int(x) for x in s.split()]
print(sum(nums))
```
Explanation: Convert each piece before numeric operations.
</details>

---

## Hard

Write `parse_input(s)` that returns int if s is int, float if float, else list if contains commas.

Starter code:
```python
def parse_input(s):
    # TODO: try int, then float, then split by comma
    pass
print(parse_input('3'))
print(parse_input('3.5'))
print(parse_input('a,b'))
```
<details><summary>Answer</summary>

```python
def parse_input(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            if ',' in s:
                return s.split(',')
            return s
print(parse_input('3'))
print(parse_input('3.5'))
print(parse_input('a,b'))
```
Explanation: Try conversions in order, fallback to splitting.
</details>
