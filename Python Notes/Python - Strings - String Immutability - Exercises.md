---
tags: [python, exercises, strings, immutability]
difficulty: Beginner
---

# Python - Strings - String Immutability — Exercises

See concept: [[Python - Strings - String Immutability]]
GitHub link: [Python - Strings - String Immutability](./Python%20-%20Strings%20-%20String%20Immutability.md)

## Quick syntax fixes

1) Broken: trying to change a character directly
```python
# Broken
word = 'dog'
word[0] = 'c'
```
<details><summary>Answer</summary>

```python
# Fixed
word = 'dog'
new_word = 'c' + word[1:]
print(new_word)
```
Explanation: Strings are immutable; build a new string.
</details>

2) Broken: using append on a string
```python
# Broken
name = 'Ada'
name.append('m')
```
<details><summary>Answer</summary>

```python
# Fixed
name = 'Ada'
name = name + 'm'
print(name)
```
Explanation: Use concatenation to create a new string.
</details>

3) Broken: slicing wrong end index
```python
# Broken
text = 'hello'
print(text[0:10])
```
<details><summary>Answer</summary>

```python
# Fixed
text = 'hello'
print(text[0:2])
```
Explanation: Slices beyond length are allowed but pick correct end index.
</details>

---

## Easy

a) Replace the first letter of 'cat' with 'b' and print.

Input example:
```text
word = cat
```
Output example:
```text
bat
```
Starter code:
```python
word = 'cat'  # word means the original word
# TODO: make new_word starting with 'b'
print(word)
```
<details><summary>Answer</summary>

```python
word = 'cat'
new_word = 'b' + word[1:]
print(new_word)
```
Explanation: Make a new string using slices.
</details>

b) Make a greeting `Hello, NAME` using concatenation and print for `NAME='Sam'`.

Starter code:
```python
name = 'Sam'
# TODO: build greeting and print
```
<details><summary>Answer</summary>

```python
name = 'Sam'
greeting = 'Hello, ' + name
print(greeting)
```
Explanation: Concatenate strings with `+`.
</details>

---

## Medium

a) Given `word='hello'`, create `h_llo` by replacing index 1 with '_' and print.

Starter code:
```python
word = 'hello'
# TODO: create new_word with '_' at index 1
print(word)
```
<details><summary>Answer</summary>

```python
word = 'hello'
new_word = word[:1] + '_' + word[2:]
print(new_word)
```
Explanation: Use slices before and after the index to build new string.
</details>

b) Turn 'abc' into 'aBc' by changing the middle letter to uppercase.

Starter code:
```python
word = 'abc'
# TODO: change middle letter to upper and print
```
<details><summary>Answer</summary>

```python
word = 'abc'
new_word = word[:1] + word[1].upper() + word[2:]
print(new_word)
```
Explanation: Use `.upper()` on the character and slice around it.
</details>

---

## Hard

Given `s = 'banana'`, create a new string with all 'a' replaced by '*' and print.

Starter code:
```python
s = 'banana'  # s means the original string
# TODO: replace all 'a' with '*'
print(s)
```
<details><summary>Answer</summary>

```python
s = 'banana'
new_s = s.replace('a', '*')
print(new_s)
```
Explanation: Use `.replace()` to create a new string with replacements.
</details>
