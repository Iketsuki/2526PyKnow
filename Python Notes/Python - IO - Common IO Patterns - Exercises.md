---
tags: [python, exercises, io]
difficulty: Beginner
---

# Exercises — IO: Common IO Patterns

See concept: [[Python - IO - Common IO Patterns]]

GitHub link: [Python - IO - Common IO Patterns](./Python%20-%20IO%20-%20Common%20IO%20Patterns.md)

### Quick syntax fixes

1) Using read without parentheses:
```python
text = f.read
```
<details><summary>Answer</summary>

```python
text = f.read()
```
Explanation: Call `read()` to get file contents.
</details>

2) Printing without newline control confusion:
```python
print('a', end='')
```
<details><summary>Answer</summary>

```python
print('a', end='')
```
Explanation: This is valid; demonstrates controlling end character to avoid extra newline.
</details>

3) Not closing file after write:
```python
f = open('x.txt', 'w')
f.write('x')
```
<details><summary>Answer</summary>

```python
with open('x.txt', 'w') as f:
    f.write('x')
```
Explanation: `with` ensures file is properly closed.
</details>

---

## Easy

### a) Read one line and print it

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
filename = input()  # filename is the file to open
# TODO: open filename and print its first line (strip newline)
```

<details><summary>Answer</summary>

```python
filename = input()
with open(filename) as f:
    print(f.readline().strip())
```
Explanation: Use `with` and `strip()` to clean the line.
</details>

### b) Write a line into a file

Input example:
```text
out.txt
Hello
```

Output example:
```text
# file out.txt will have 'Hello' as a line
```

Starter code:
```python
filename = input()  # filename to write into
line = input()      # line to write
# TODO: open filename in write mode and write the line, adding newline
```

<details><summary>Answer</summary>

```python
filename = input()
line = input()
with open(filename, 'w') as f:
    f.write(line + '\n')
```
Explanation: Use 'w' mode and add '\n' to end the line.
</details>

---

## Medium

### a) Read whole file and print length of text

Input example:
```text
file.txt
```

Output example:
```text
42
```

Starter code:
```python
filename = input()
# TODO: open filename, read all text and print its length (number of characters)
```

<details><summary>Answer</summary>

```python
filename = input()
with open(filename) as f:
    text = f.read()
print(len(text))
```
Explanation: Use `read()` and `len()` to measure text size.
</details>

### b) Copy file contents to another file

Input example:
```text
in.txt
out.txt
```

Output example:
```text
# out.txt will have same contents as in.txt
```

Starter code:
```python
in_filename = input()   # source file
out_filename = input()  # destination file
# TODO: copy contents from in_filename to out_filename
```

<details><summary>Answer</summary>

```python
in_filename = input()
out_filename = input()
with open(in_filename) as inf, open(out_filename, 'w') as outf:
    for line in inf:
        outf.write(line)
```
Explanation: Open both files and write line-by-line.
</details>

---

## Hard

### Single: Replace lines that contain a word and write to new file

Input example:
```text
in.txt
out.txt
apple
```

Output example:
```text
# out.txt will have lines with 'apple' replaced by 'X'
```

Starter code:
```python
in_filename = input()
out_filename = input()
word = input()  # word to replace
# TODO: write a new file replacing word with 'X' in each line
```

<details><summary>Answer</summary>

```python
in_filename = input()
out_filename = input()
word = input()
with open(in_filename) as inf, open(out_filename, 'w') as outf:
    for line in inf:
        outf.write(line.replace(word, 'X'))
```
Explanation: Use `str.replace()` to substitute words in each line.
</details>
