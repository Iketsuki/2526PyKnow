---
tags: [python, exercises, fileio]
difficulty: Beginner
---

# Python - File I\O - Read & Write (Day 9) — Exercises

See concept: [[Python - File I/O - Read & Write (Day 9)]]
GitHub link: [Python - File I\O - Read & Write (Day 9)](./Python%20-%20File%20I%5CO%20-%20Read%20%26%20Write%20(Day%209).md)

## Quick syntax fixes

1) Broken: opening file in wrong mode
```python
f = open('x.txt')
f.write('a')
```
<details><summary>Answer</summary>

```python
f = open('x.txt', 'w')
f.write('a')
f.close()
```
Explanation: Use write mode to write.
</details>

2) Broken: forgetting to close file
```python
f = open('x.txt','r')
print(f.read())
```
<details><summary>Answer</summary>

```python
with open('x.txt') as f:
    print(f.read())
```
Explanation: `with` closes file automatically.
</details>

3) Broken: using append but reading later
```python
with open('x.txt','a') as f:
    f.write('x')
with open('x.txt') as f:
    print(f.read())
```
<details><summary>Answer</summary>

```python
with open('x.txt','a+') as f:
    f.seek(0)
    print(f.read())
```
Explanation: use correct mode and seek when appending then reading.
</details>

---

## Easy

a) Write 'hello' to `out.txt`.

Starter code:
```python
# TODO: write hello to file
pass
```
<details><summary>Answer</summary>

```python
with open('out.txt', 'w') as f:
    f.write('hello')
```
Explanation: open in write mode and write text.
</details>

b) Read and print all lines from `in.txt`.

Starter code:
```python
# TODO: read lines
pass
```
<details><summary>Answer</summary>

```python
with open('in.txt') as f:
    for line in f:
        print(line.strip())
```
Explanation: iterate file to read lines.
</details>

---

## Medium

a) Append a line from input to `log.txt`.

Starter code:
```python
line = input()
# TODO: append to log
pass
```
<details><summary>Answer</summary>

```python
line = input()
with open('log.txt', 'a') as f:
    f.write(line + '\n')
```
Explanation: use append mode to add lines.
</details>

b) Read numbers from a file and print their sum.

Starter code:
```python
# TODO: open numbers.txt and sum ints
pass
```
<details><summary>Answer</summary>

```python
total = 0
with open('numbers.txt') as f:
    for line in f:
        total += int(line)
print(total)
```
Explanation: convert each line to int and accumulate.
</details>

---

## Hard

Write a function that writes a list of strings to a file, one per line, and returns number written.

Starter code:
```python
def write_lines(fname, lines):
    # TODO: write and return count
    pass

print(write_lines('out.txt', ['a','b']))
```
<details><summary>Answer</summary>

```python
def write_lines(fname, lines):
    with open(fname, 'w') as f:
        for line in lines:
            f.write(line + '\n')
    return len(lines)

print(write_lines('out.txt', ['a','b']))
```
Explanation: write each string and return count.
</details>
