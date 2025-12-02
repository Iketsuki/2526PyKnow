---
tags: [python, exercises, file-io]
difficulty: Beginner
---

# Exercises — File IO: Opening Files

See concept: [[Python - File IO - Opening Files]]

### Quick syntax fixes

1) Using open without mode when writing:
```python
f = open('a.txt', 'r')
f.write('hi')
```
<details><summary>Answer</summary>

```python
f = open('a.txt', 'w')
f.write('hi')
f.close()
```
Explanation: Use 'w' to write, or use `with`.
</details>

2) Not closing file after write:
```python
f = open('x.txt', 'w')
f.write('x')
# missing close
```
<details><summary>Answer</summary>

```python
with open('x.txt', 'w') as f:
    f.write('x')
```
Explanation: `with` closes automatically.
</details>

3) Wrong mode letters:
```python
f = open('a.txt', 'rw')
```
<details><summary>Answer</summary>

```python
f = open('a.txt', 'r')
```
Explanation: Modes are 'r', 'w', 'a' etc. 'rw' is invalid.
</details>

---

## Easy

### a) Open a file and print its first word

Input example:
```text
sample.txt
```

Suppose file `sample.txt` first line: "Hello world"

Output example:
```text
Hello
```

Starter code:
```python
fn = input()
# TODO: open the file and print the first word of the first line
```

<details><summary>Answer</summary>

```python
fn = input()
with open(fn) as f:
    first = f.readline().split()[0]
print(first)
```
Explanation: `split()` breaks the line into words; index 0 is first word.
</details>

### b) Append a line to a file

Input example:
```text
log.txt
New entry
```

Output example (no print required, but file will have new line appended)

Starter code:
```python
fn = input()
line = input()
# TODO: open file in append mode and write the line
```

<details><summary>Answer</summary>

```python
fn = input()
line = input()
with open(fn, 'a') as f:
    f.write(line + '\n')
```
Explanation: Use mode 'a' to append and add newline.
</details>

---

## Medium

### a) Read file and print first 2 lines

Input example:
```text
notes.txt
```

Output example:
```text
Line1
Line2
```

Starter code:
```python
fn = input()
# TODO: open and print first two lines
```

<details><summary>Answer</summary>

```python
fn = input()
with open(fn) as f:
    print(f.readline().strip())
    print(f.readline().strip())
```
Explanation: Call `readline()` twice to get first two lines.
</details>

### b) Create file and write three lines

Input example:
```text
out.txt
one
two
three
```

Output example (file `out.txt` created with 3 lines)

Starter code:
```python
fn = input()
# then three lines
# TODO: open fn for writing and write the next three inputs as lines
```

<details><summary>Answer</summary>

```python
fn = input()
with open(fn, 'w') as f:
    f.write(input() + '\n')
    f.write(input() + '\n')
    f.write(input() + '\n')
```
Explanation: Use 'w' mode to write and add newlines after each write.
</details>

---

## Hard

### Single: Copy first n lines from infile to outfile

Input example:
```text
in.txt
out.txt
2
```

Output example (out.txt will contain first two lines of in.txt)

Starter code:
```python
infn = input()
outfn = input()
n = int(input())
# TODO: copy first n lines from infn to outfn
```

<details><summary>Answer</summary>

```python
infn = input()
outfn = input()
n = int(input())
with open(infn) as inf, open(outfn, 'w') as outf:
    for _ in range(n):
        line = inf.readline()
        if not line:
            break
        outf.write(line)
```
Explanation: Open both files with `with` and write lines until n or EOF.
</details>
