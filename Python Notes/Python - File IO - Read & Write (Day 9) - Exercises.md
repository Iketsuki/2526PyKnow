---
tags: [python, exercises, fileio]
difficulty: Beginner
---

# Python - File IO - Read & Write (Day 9) — Exercises

See concept: [[Python - File IO - Read & Write (Day 9)]]
GitHub link: [Python - File IO - Read & Write (Day 9)](./Python%20-%20File%20IO%20-%20Read%20%26%20Write%20(Day%209).md)

## Quick syntax fixes

1) Broken: reading before writing expected content
```python
with open('x.txt') as f:
    print(f.read())
with open('x.txt','w') as f:
    f.write('hi')
```
<details><summary>Answer</summary>

```python
with open('x.txt','w') as f:
    f.write('hi')
with open('x.txt') as f:
    print(f.read())
```
Explanation: write before read if expecting content.
</details>

2) Broken: using read() then iterating file
```python
with open('x.txt') as f:
    data = f.read()
    for line in f:
        print(line)
```
<details><summary>Answer</summary>

```python
with open('x.txt') as f:
    for line in f:
        print(line)
```
Explanation: reading moves file pointer; iterate directly instead.
</details>

3) Broken: writing without newline when needed
```python
with open('x.txt','a') as f:
    f.write('x')
with open('x.txt') as f:
    print(f.read())
```
<details><summary>Answer</summary>

```python
with open('x.txt','a') as f:
    f.write('x\n')
with open('x.txt') as f:
    print(f.read())
```
Explanation: add newline to separate appended entries.
</details>

---

## Easy

a) Create a file `a.txt` and write '1' then close.

Starter code:
```python
# TODO: write '1' to a.txt
pass
```
<details><summary>Answer</summary>

```python
with open('a.txt','w') as f:
    f.write('1')
```
Explanation: open in write mode and write text.
</details>

b) Read file `a.txt` and print its contents.

Starter code:
```python
# TODO: read a.txt and print
pass
```
<details><summary>Answer</summary>

```python
with open('a.txt') as f:
    print(f.read())
```
Explanation: use `with` for safe reading.
</details>

---

## Medium

a) Read lines of `nums.txt` and print their sum.

Starter code:
```python
# TODO: sum numbers in file
pass
```
<details><summary>Answer</summary>

```python
total = 0
with open('nums.txt') as f:
    for line in f:
        total += int(line)
print(total)
```
Explanation: convert lines to int and add.
</details>

b) Write a list of names to `names.txt`, one per line.

Starter code:
```python
names = ['Ann','Ben']
# TODO: write names
pass
```
<details><summary>Answer</summary>

```python
names = ['Ann','Ben']
with open('names.txt','w') as f:
    for n in names:
        f.write(n + '\n')
```
Explanation: write each name with newline.
</details>

---

## Hard

Write a function that reads a file and returns number of non-empty lines.

Starter code:
```python
def count_nonempty(fname):
    # TODO: count lines that are not blank
    pass

print(count_nonempty('data.txt'))
```
<details><summary>Answer</summary>

```python
def count_nonempty(fname):
    count = 0
    with open(fname) as f:
        for line in f:
            if line.strip():
                count += 1
    return count

print(count_nonempty('data.txt'))
```
Explanation: strip blanks and count.
</details>
