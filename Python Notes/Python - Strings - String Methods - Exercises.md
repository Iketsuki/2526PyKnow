---
tags: [python, exercises, strings]
difficulty: Beginner
---

# Exercises — Strings: String Methods

See concept: [[Python - Strings - String Methods]]

GitHub link: [Python - Strings - String Methods](./Python%20-%20Strings%20-%20String%20Methods.md)

### Quick syntax fixes

1) Calling method without parentheses:
```python
s = 'hi'
print(s.upper)
```
<details><summary>Answer</summary>

```python
s = 'hi'
print(s.upper())
```
Explanation: Methods need `()` to call them.
</details>

2) Using replace incorrectly:
```python
s = 'a b'
print(s.replace(' ', '-'))
```
<details><summary>Answer</summary>

```python
s = 'a b'
print(s.replace(' ', '-'))
```
Explanation: This example is correct; show expected use. `replace` swaps substrings.
</details>

3) Mistaken strip usage:
```python
s = ' hi '
print(s.strip)
```
<details><summary>Answer</summary>

```python
s = ' hi '
print(s.strip())
```
Explanation: `strip()` removes leading/trailing whitespace when called.
</details>

---

## Easy

### a) Make word uppercase

Input example:
```text
hello
```

Output example:
```text
HELLO
```

Starter code:
```python
word = input()  # word to transform
# TODO: print the uppercase version of word
```

<details><summary>Answer</summary>

```python
word = input()
print(word.upper())
```
Explanation: `.upper()` converts letters to uppercase.
</details>

### b) Remove spaces from ends

Input example:
```text
  hi  
```

Output example:
```text
hi
```

Starter code:
```python
s = input()  # string may have spaces around it
# TODO: print the stripped string
```

<details><summary>Answer</summary>

```python
s = input()
print(s.strip())
```
Explanation: `strip()` removes leading and trailing whitespace.
</details>

---

## Medium

### a) Replace spaces with dash

Input example:
```text
hello world
```

Output example:
```text
hello-world
```

Starter code:
```python
s = input()
# TODO: replace spaces with '-' and print
```

<details><summary>Answer</summary>

```python
s = input()
print(s.replace(' ', '-'))
```
Explanation: `replace(old, new)` swaps all occurrences.
</details>

### b) Count letter occurrences

Input example:
```text
banana
```

Output example:
```text
3
```

Starter code:
```python
s = input()
# TODO: count how many times 'a' appears and print number
```

<details><summary>Answer</summary>

```python
s = input()
print(s.count('a'))
```
Explanation: `.count(char)` returns number of occurrences.
</details>

---

## Hard

### Single: Join three words with comma

Input example:
```text
one
two
three
```

Output example:
```text
one,two,three
```

Starter code:
```python
w1 = input()
w2 = input()
w3 = input()
# TODO: print the words joined by commas
```

<details><summary>Answer</summary>

```python
w1 = input()
w2 = input()
w3 = input()
print(','.join([w1, w2, w3]))
```
Explanation: `join` combines items from a list with the separator string.
</details>
