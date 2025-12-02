---
tags: [python, exercises, conditionals]
difficulty: Beginner
---

# Exercises — Conditionals: NOT Operator

See concept: [[Python - Conditionals - NOT Operator]]

GitHub link: [Python - Conditionals - NOT Operator](Python%20-%20Conditionals%20-%20NOT%20Operator.md)

### Quick syntax fixes

1) Using `not` with wrong placement:
```python
if not x == 3:
print('yes')
```
<details><summary>Answer</summary>

```python
if not x == 3:
    print('yes')
```
Explanation: Indent the body; `not x == 3` is valid but clearer as `x != 3`.
</details>

2) Using `not` with parentheses missing when needed:
```python
if not (x > 0 and y > 0):
print('no')
```
<details><summary>Answer</summary>

```python
if not (x > 0 and y > 0):
    print('no')
```
Explanation: Add parentheses to group conditions and indent.
</details>

3) Confusing `not` with `!=`:
```python
if not x != 3:
    print('ok')
```
<details><summary>Answer</summary>

```python
# Better to write explicitly:
if x == 3:
    print('ok')
```
Explanation: `not x != 3` is confusing; use `==` for clarity.
</details>

---

## Easy

### a) Check if string is not empty

Input example:
```text
hello
```

Output example:
```text
Has text
```

Starter code:
```python
s = input()  # s is the input string
# TODO: print 'Has text' if not empty else 'Empty'
```

<details><summary>Answer</summary>

```python
s = input()
if not s == '':
    print('Has text')
else:
    print('Empty')
```
Explanation: `not s == ''` checks for non-empty; `if s:` is shorter but explicit form is easier for learners.
</details>

### b) Check number is not negative

Input example:
```text
5
```

Output example:
```text
Non-negative
```

Starter code:
```python
n = int(input())  # n is the number
# TODO: print 'Non-negative' if n is not negative else 'Negative'
```

<details><summary>Answer</summary>

```python
n = int(input())
if not n < 0:
    print('Non-negative')
else:
    print('Negative')
```
Explanation: `not n < 0` means n >= 0.
</details>

---

## Medium

### a) Skip empty lines

Input example:
```text

hello
```

Output example:
```text
hello
```

Starter code:
```python
s = input()  # may be empty
# TODO: print s only if it is not empty
```

<details><summary>Answer</summary>

```python
s = input()
if not s == '':
    print(s)
```
Explanation: Use `not` to test for non-empty strings.
</details>

### b) Check value not in list

Input example:
```text
pear
```

Output example:
```text
Not found
```

Starter code:
```python
w = input()
fruits = ['apple', 'banana']
# TODO: print 'Not found' if w is not in fruits else 'Found'
```

<details><summary>Answer</summary>

```python
w = input()
fruits = ['apple', 'banana']
if w not in fruits:
    print('Not found')
else:
    print('Found')
```
Explanation: `not in` is a natural opposite to `in`.
</details>

---

## Hard

### Single: Complex negative check

Input example:
```text
4
3
```

Output example:
```text
OK
```

Starter code:
```python
x = int(input())
y = int(input())
# TODO: print 'OK' if not (x<3 or y>5) else 'Bad'
```

<details><summary>Answer</summary>

```python
x = int(input())
y = int(input())
if not (x < 3 or y > 5):
    print('OK')
else:
    print('Bad')
```
Explanation: `not` flips the grouped condition meaning both need to be false to print 'OK'.
</details>
