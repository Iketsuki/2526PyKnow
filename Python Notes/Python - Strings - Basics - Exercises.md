---
tags: [python, exercises, strings, basics]
difficulty: Beginner
---

# Python - Strings - Basics — Exercises

See concept: [[Python - Strings - Basics]]
GitHub link: [Python - Strings - Basics](./Python%20-%20Strings%20-%20Basics.md)

## Quick syntax fixes

1) Broken: using single quotes inside single quotes
```python
print('It's fine')
```
<details><summary>Answer</summary>

Use double quotes or escape: `print("It's fine")` or `print('It\'s fine')`.

Explanation: match quotes or escape inner quotes.
</details>

2) Broken: indexing past end
```python
s = 'hi'
print(s[5])
```
<details><summary>Answer</summary>

This raises `IndexError`; use slicing or check length first.

Explanation: strings index must be within range.
</details>

3) Broken: forgetting `str()` when concatenating
```python
age = 5
print('Age: ' + age)
```
<details><summary>Answer</summary>

Use `print('Age:', age)` or `print('Age: ' + str(age))`.

Explanation: convert non-strings or use comma in print.
</details>

---

## Easy

a) Read a name and print `Hello <name>`.

Starter code:
```python
name = input()
# TODO: print greeting
pass
```
<details><summary>Answer</summary>

```python
name = input()
print('Hello', name)
```
Explanation: use comma or concat with `+` and str.
</details>

b) Print the length of a string from input.

Starter code:
```python
s = input()
# TODO: print length
pass
```
<details><summary>Answer</summary>

```python
s = input()
print(len(s))
```
Explanation: `len()` returns string length.
</details>

---

## Medium

a) Make the input lowercase and print it.

Starter code:
```python
s = input()
# TODO: print lowercase
pass
```
<details><summary>Answer</summary>

```python
s = input()
print(s.lower())
```
Explanation: `lower()` returns a lowercase string.
</details>

b) Replace spaces in a string with dashes and print.

Starter code:
```python
s = input()
# TODO: replace spaces
pass
```
<details><summary>Answer</summary>

```python
s = input()
print(s.replace(' ', '-'))
```
Explanation: `replace` substitutes substrings.
</details>

---

## Hard

Write a function `is_palindrome(s)` that returns True for palindrome strings ignoring case and spaces.

Starter code:
```python
def is_palindrome(s):
    # TODO
    pass

print(is_palindrome('A man a plan a canal'))
```
<details><summary>Answer</summary>

```python
def is_palindrome(s):
    t = ''.join(ch.lower() for ch in s if ch != ' ')
    return t == t[::-1]

print(is_palindrome('A man a plan a canal'))
```
Explanation: normalize then compare to reversed.
</details>
