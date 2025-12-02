---
tags: [python, exercises, strings, slicing]
difficulty: Beginner
---

# Python - Strings - String Slicing & Indexing — Exercises

See concept: [[Python - Strings - String Slicing & Indexing]]
GitHub link: [Python - Strings - String Slicing & Indexing](./Python%20-%20Strings%20-%20String%20Slicing%20%26%20Indexing.md)

## Quick syntax fixes

1) Broken: wrong index
```python
# Broken
word = 'hello'
print(word[5])
```
<details><summary>Answer</summary>

```python
# Fixed
word = 'hello'
print(word[4])
```
Explanation: Last index is length-1.
</details>

2) Broken: negative index confusion
```python
# Broken
word = 'abc'
print(word[-4])
```
<details><summary>Answer</summary>

```python
# Fixed
word = 'abc'
print(word[-1])
```
Explanation: -1 is last item; -4 is out of range.
</details>

3) Broken: slice end exclusive
```python
# Broken
text = 'hello'
print(text[0:5])
```
<details><summary>Answer</summary>

```python
# Explain
text = 'hello'
print(text[0:5])  # prints 'hello' because end is exclusive
```
Explanation: Slice end index is not included in result.
</details>

---

## Easy

a) Print the first and last character of 'python'.

Starter code:
```python
word = 'python'
# TODO: print first and last characters
```
<details><summary>Answer</summary>

```python
word = 'python'
print(word[0])
print(word[-1])
```
Explanation: Use index 0 and -1 for first and last.
</details>

b) Print 'py' using slicing from 'python'.

Starter code:
```python
word = 'python'
# TODO: print 'py'
```
<details><summary>Answer</summary>

```python
word = 'python'
print(word[0:2])
```
Explanation: Slice from 0 up to but not including 2.
</details>

---

## Medium

a) Reverse the string 'abc' using slicing and print.

Starter code:
```python
word = 'abc'
# TODO: print reversed string
```
<details><summary>Answer</summary>

```python
word = 'abc'
print(word[::-1])
```
Explanation: Use step -1 to reverse.
</details>

b) Extract every second character from 'abcdef' and print 'ace'.

Starter code:
```python
s = 'abcdef'
# TODO: print every second character starting at index 0
```
<details><summary>Answer</summary>

```python
s = 'abcdef'
print(s[0::2])
```
Explanation: Slicing with step 2 picks every second character.
</details>

---

## Hard

Given `s='hello world'`, make a new string with words in reverse order -> 'world hello'.

Starter code:
```python
s = 'hello world'
# TODO: split and join reversed words and print
```
<details><summary>Answer</summary>

```python
s = 'hello world'
words = s.split()
rev = ' '.join(words[::-1])
print(rev)
```
Explanation: Use `split()` to get words, reverse list, then `join()`.
</details>
