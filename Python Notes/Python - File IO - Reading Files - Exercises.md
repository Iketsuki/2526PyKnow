---
tags: [python, exercises, file-io]
difficulty: Beginner
---

# Exercises — File IO: Reading Files

See concept: [[Python - File IO - Reading Files]]

### Quick syntax fixes

1) Forgetting to open file:
```python
text = f.read()
```
<details><summary>Answer</summary>

```python
f = open('file.txt')
text = f.read()
f.close()
```
Explanation: Open the file before reading.
</details>

2) Using read without parentheses:
```python
text = f.read
```
<details><summary>Answer</summary>

```python
text = f.read()
```
Explanation: Call `read()` to get contents.
</details>

3) Not using with when asked:
```python
f = open('a.txt')
print(f.read())
```
<details><summary>Answer</summary>

```python
with open('a.txt') as f:
    print(f.read())
```
Explanation: `with` ensures file closes automatically.
</details>

---

## Easy

### a) Read a filename and print its first line

Starter file example (assume file contains lines):

Input example:
```text
sample.txt
```

Output example:
```text
Hello world
```

Starter code:
```python
fn = input()
# TODO: open the file and print the first line (strip newline)
```

<details><summary>Answer</summary>

```python
fn = input()
with open(fn) as f:
    print(f.readline().strip())
```
Explanation: `readline()` reads one line; `strip()` removes newline.
</details>

### b) Print number of lines in a file

Input example:
```text
data.txt
```

Output example:
```text
3
```

Starter code:
```python
fn = input()
# TODO: count lines
```

<details><summary>Answer</summary>

```python
fn = input()
count = 0
with open(fn) as f:
    for _ in f:
        count += 1
print(count)
```
Explanation: Loop over file object yields lines.
</details>

---

## Medium

### a) Print the last line of a file

Input example:
```text
lines.txt
```

Output example:
```text
Goodbye
```

Starter code:
```python
fn = input()
# TODO: read all lines and print the last one
```

<details><summary>Answer</summary>

```python
fn = input()
with open(fn) as f:
    lines = f.readlines()
print(lines[-1].strip())
```
Explanation: Use `readlines()` to get list of lines, then index -1.
</details>

### b) Check if a word is in file

Input example:
```text
story.txt
apple
```

Output example:
```text
Found
```

Starter code:
```python
fn = input()
word = input()
# TODO: print 'Found' if word appears in file text
```

<details><summary>Answer</summary>

```python
fn = input()
word = input()
with open(fn) as f:
    text = f.read()
if word in text:
    print('Found')
else:
    print('Not found')
```
Explanation: Read file as a string and use `in`.
</details>

---

## Hard

### Single: Count how many times a word appears (case-sensitive)

Input example:
```text
poem.txt
fish
```

Output example:
```text
2
```

Starter code:
```python
fn = input()
word = input()
# TODO: count occurrences of the word in the file
```

<details><summary>Answer</summary>

```python
fn = input()
word = input()
count = 0
with open(fn) as f:
    for line in f:
        count += line.count(word)
print(count)
```
Explanation: Use `str.count()` on each line and add up counts.
</details>
