---
tags: [python, exercises, strings]
difficulty: Beginner
---

# Exercises — String Slicing & Indexing

See concept: [[Python - Strings - Slicing]]
GitHub link: [Python - Strings - Slicing](./Python%20-%20Strings%20-%20Slicing.md)

---

## Quick syntax fixes

1) Forgetting string quotes
```python
# Broken example
greeting = Hello
```
<details><summary>Answer</summary>

```python
# Fixed example
greeting = 'Hello'
```
Explanation: Strings must be inside quotes.
</details>

2) Wrong index signs
```python
word = 'bird'
print(word[4])
```
<details><summary>Answer</summary>

```python
word = 'bird'
print(word[3])
```
Explanation: Indexes start at 0, so last index is 3 for a 4-letter word.
</details>

3) Using negative index incorrectly
```python
word = 'cat'
print(word[-4])
```
<details><summary>Answer</summary>

```python
word = 'cat'
print(word[-1])
```
Explanation: `-1` is the last character, `-len(word)` is first.
</details>

---

## Easy

### a) First and last letters

Input example:
```text
hello
```

Output example:
```text
h o
```

Starter code:
```python
text = input()  # text is the word typed by the student
# TODO: print the first and last character separated by a space
```

<details><summary>Answer</summary>

```python
text = input()
print(text[0], text[-1])
```
Explanation: Use index 0 for first and -1 for last character.
</details>

### b) Middle character (short word)

Input example:
```text
cat
```

Output example:
```text
a
```

Starter code:
```python
word = input()  # word is a short string with odd length
# TODO: print the middle character (assume odd length)
```

<details><summary>Answer</summary>

```python
word = input()
middle_index = len(word) // 2
print(word[middle_index])
```
Explanation: Use integer division to find the middle index.
</details>

---

## Medium

### a) First three letters

Input example:
```text
elephant
```

Output example:
```text
ele
```

Starter code:
```python
word = input()  # word to slice
# TODO: print the first three letters of the word
```

<details><summary>Answer</summary>

```python
word = input()
print(word[:3])
```
Explanation: Use slice `[:3]` to get characters 0,1,2.
</details>

### b) Last two letters reversed

Input example:
```text
world
```

Output example:
```text
dl
```

Starter code:
```python
word = input()  # word to process
# TODO: print the last two letters in reverse order
```

<details><summary>Answer</summary>

```python
word = input()
print(word[-1] + word[-2])
```
Explanation: Use negative indexes to select last characters and concatenate.
</details>

---

## Hard

### Single: Slice and join

Input example:
```text
python
2
```

Output example:
```text
th on
```

Starter code:
```python
word = input()         # word to slice
skip = int(input())    # skip is the integer number of characters to skip
# TODO: make two parts: letters at odd positions and letters at even positions separated by a space
```

<details><summary>Answer</summary>

```python
word = input()
skip = int(input())
part1 = word[skip::2]
part2 = word[1::2]
print(part1, part2)
```
Explanation: Use slicing with step to take every second letter starting at indexes.
</details>

---

See concept: [[Python - Strings - Slicing]]
GitHub link: [Python - Strings - Slicing](./Python%20-%20Strings%20-%20Slicing.md)
