---
tags: [python, exercises, io]
difficulty: Beginner
---

# Exercises — Input and Output

See concept: [[Python - IO - Input and Output]]

### Quick syntax fixes

1) Wrong order of print and input:
```python
print(input('Name: '))
```
<details><summary>Answer</summary>

```python
name = input('Name: ')
print(name)
```
Explanation: Store input if you need to use it later.
</details>

2) Using `sep` incorrectly:
```python
print('a','b', sep='')
```
<details><summary>Answer</summary>

```python
print('a','b', sep='')
```
Explanation: This is okay; the fix is to show expected use — add a clearer example: `sep='-'` prints `a-b`.
</details>

3) Forgetting `int()` for math:
```python
x = input()
print(x + 2)
```
<details><summary>Answer</summary>

```python
x = int(input())
print(x + 2)
```
Explanation: Convert input to `int` for arithmetic.
</details>

---

## Easy

### a) Echo input three times on separate lines

Input example:
```text
Hi
```

Output example:
```text
Hi
Hi
Hi
```

Starter code:
```python
s = input()
# TODO: print s three times on separate lines
```

<details><summary>Answer</summary>

```python
s = input()
print(s)
print(s)
print(s)
```
Explanation: Use three print calls.
</details>

### b) Read two numbers and print them on one line

Input example:
```text
4
9
```

Output example:
```text
4 9
```

Starter code:
```python
a = input()
b = input()
# TODO: print both on one line
```

<details><summary>Answer</summary>

```python
a = input()
b = input()
print(a, b)
```
Explanation: `print` separates by space by default.
</details>

---

## Medium

### a) Read name and three scores, print name and average

Input example:
```text
Sam
10
8
9
```

Output example:
```text
Sam 9.0
```

Starter code:
```python
name = input()
# TODO: read three scores, compute average, print name and average
```

<details><summary>Answer</summary>

```python
name = input()
s1 = int(input())
s2 = int(input())
s3 = int(input())
avg = (s1 + s2 + s3) / 3
print(name, avg)
```
Explanation: Convert inputs to `int` and compute float average.
</details>

### b) Read two words then print them joined with a dash

Input example:
```text
good
job
```

Output example:
```text
good-job
```

Starter code:
```python
w1 = input()
w2 = input()
# TODO: print them with a dash between
```

<details><summary>Answer</summary>

```python
w1 = input()
w2 = input()
print(w1 + '-' + w2)
```
Explanation: Use string concatenation to combine with `-`.
</details>

---

## Hard

### Single: Read a name and a number n, then read n words and print them as a comma list after the name

Input example:
```text
Maya
3
red
blue
green
```

Output example:
```text
Maya: red, blue, green
```

Starter code:
```python
name = input()
n = int(input())
# TODO: read n items, then print as shown
```

<details><summary>Answer</summary>

```python
name = input()
n = int(input())
items = []
for _ in range(n):
    items.append(input())
print(name + ': ' + ', '.join(items))
```
Explanation: Use a list to collect items and `join` with comma and space.
</details>
