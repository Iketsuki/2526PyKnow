---
tags: [python, exercises, loops]
difficulty: Beginner
---

# Exercises — Loops: For Loop Basics

See concept: [[Python - Loops - For Loop Basics]]

### Quick syntax fixes

1) Missing colon:
```python
for i in [1,2,3]
    print(i)
```
<details><summary>Answer</summary>

```python
for i in [1,2,3]:
    print(i)
```
Explanation: Add `:` after the `for` header.
</details>

2) Indentation for body:
```python
for i in range(2):
print(i)
```
<details><summary>Answer</summary>

```python
for i in range(2):
    print(i)
```
Explanation: Indent the loop body.
</details>

3) Using wrong variable in loop:
```python
for x in [1,2]:
    print(i)
```
<details><summary>Answer</summary>

```python
for x in [1,2]:
    print(x)
```
Explanation: Use the same loop variable inside the body.
</details>

---

## Easy

### a) Print numbers 1 to 3 each on a new line

Output example:
```text
1
2
3
```

Starter code:
```python
# TODO: use a for loop and range to print 1 to 3
```

<details><summary>Answer</summary>

```python
for i in range(1, 4):
    print(i)
```
Explanation: `range(1,4)` gives 1,2,3.
</details>

### b) Print each letter of the word

Input example:
```text
cat
```

Output example:
```text
c
a
t
```

Starter code:
```python
s = input()
# TODO: print each character on its own line
```

<details><summary>Answer</summary>

```python
s = input()
for ch in s:
    print(ch)
```
Explanation: Strings are iterable; loop over characters.
</details>

---

## Medium

### a) Sum numbers from 1 to n

Input example:
```text
5
```

Output example:
```text
15
```

Starter code:
```python
n = int(input())
# TODO: use a for loop to sum numbers 1..n
```

<details><summary>Answer</summary>

```python
n = int(input())
s = 0
for i in range(1, n+1):
    s += i
print(s)
```
Explanation: Loop and accumulate sum.
</details>

### b) Print squares of numbers in a list

Input example:
```text
2
3
4
```

Output example:
```text
4
9
16
```

Starter code:
```python
nums = [int(input()), int(input()), int(input())]
# TODO: print square of each number
```

<details><summary>Answer</summary>

```python
nums = [int(input()), int(input()), int(input())]
for n in nums:
    print(n*n)
```
Explanation: Multiply the number by itself.
</details>

---

## Hard

### Single: Build comma-separated numbers from 1..n

Input example:
```text
4
```

Output example:
```text
1,2,3,4
```

Starter code:
```python
n = int(input())
# TODO: create the string and print it
```

<details><summary>Answer</summary>

```python
n = int(input())
print(','.join(str(i) for i in range(1, n+1)))
```
Explanation: Convert numbers to strings and join with commas.
</details>
