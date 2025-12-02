---
tags: [python, exercises, strings]
difficulty: Beginner
---

# Exercises — Strings: Basics

See concept: [[Python - Strings - String Basics]]

### Quick syntax fixes

1) Missing quotes:
```python
s = Hello
```
<details><summary>Answer</summary>

```python
s = 'Hello'
```
Explanation: Strings need quotes.
</details>

2) Concatenate numbers as strings:
```python
print('1' + 2)
```
<details><summary>Answer</summary>

```python
print('1' + str(2))
```
Explanation: Convert number to string before concatenation.
</details>

3) Wrong index type:
```python
s = 'abc'
print(s['0'])
```
<details><summary>Answer</summary>

```python
s = 'abc'
print(s[0])
```
Explanation: Indices are integers, not strings.
</details>

---

## Easy

### a) Print first letter of a word

Input example:
```text
apple
```

Output example:
```text
a
```

Starter code:
```python
w = input()
# TODO: print the first letter
```

<details><summary>Answer</summary>

```python
w = input()
print(w[0])
```
Explanation: Use index 0 for first character.
</details>

### b) Make word uppercase

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
w = input()
# TODO: print the uppercase word
```

<details><summary>Answer</summary>

```python
w = input()
print(w.upper())
```
Explanation: Use `.upper()` to convert to uppercase.
</details>

---

## Medium

### a) Replace spaces with dashes

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
Explanation: `.replace()` swaps substrings.
</details>

### b) Count letter 'a'

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
# TODO: count 'a' letters and print number
```

<details><summary>Answer</summary>

```python
s = input()
print(s.count('a'))
```
Explanation: Use `.count()` to count occurrences.
</details>

---

## Hard

### Single: Join words with comma

Input example:
```text
red
blue
green
```

Output example:
```text
red,blue,green
```

Starter code:
```python
w1 = input()
w2 = input()
w3 = input()
# TODO: print words joined by commas
```

<details><summary>Answer</summary>

```python
w1 = input()
w2 = input()
w3 = input()
print(','.join([w1, w2, w3]))
```
Explanation: `join` combines strings with a separator.
</details>
