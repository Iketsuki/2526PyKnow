---
tags: [python, exercises, conditionals]
difficulty: Beginner
---

# Exercises — Conditionals: Truthiness

See concept: [[Python - Conditionals - Truthiness]]

GitHub link: [Python - Conditionals - Truthiness](Python%20-%20Conditionals%20-%20Truthiness.md)

### Quick syntax fixes

1) Checking empty list incorrectly:
```python
l = []
if l == True:
    print('yes')
```
<details><summary>Answer</summary>

```python
l = []
if l:
    print('yes')
else:
    print('no')
```
Explanation: Empty lists are false-y; use `if l:` to test non-empty.
</details>

2) Using `not` vs `==` confusion:
```python
s = ''
if not s:
print('empty')
```
<details><summary>Answer</summary>

```python
s = ''
if not s:
    print('empty')
```
Explanation: `not s` is true for empty strings; ensure indentation.
</details>

3) Wrong numeric truth test:
```python
n = 0
if n:
    print('yes')
```
<details><summary>Answer</summary>

```python
n = 0
if n:
    print('yes')
else:
    print('no')
```
Explanation: 0 is false-y; show both branches to clarify behavior.
</details>

---

## Easy

### a) Print 'Has text' if input not empty

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
text = input()  # text from user
# TODO: print 'Has text' if text is not empty else 'No text'
```

<details><summary>Answer</summary>

```python
text = input()
if text:
    print('Has text')
else:
    print('No text')
```
Explanation: Non-empty strings are true in conditions.
</details>

### b) Check list truthiness

Input example:
```text
a
```

Output example:
```text
Not empty
```

Starter code:
```python
items = [input()]  # simple list with one input
# TODO: print 'Not empty' if items is non-empty else 'Empty'
```

<details><summary>Answer</summary>

```python
items = [input()]
if items:
    print('Not empty')
else:
    print('Empty')
```
Explanation: Any non-empty list is truthy.
</details>

---

## Medium

### a) Treat '0' as text vs number

Input example:
```text
0
```

Output example:
```text
Has text
```

Starter code:
```python
s = input()  # s is a string even if it looks like a number
# TODO: print 'Has text' if s is non-empty
```

<details><summary>Answer</summary>

```python
s = input()
if s:
    print('Has text')
else:
    print('No text')
```
Explanation: Even '0' is a non-empty string and therefore truthy.
</details>

### b) Check 0 vs non-zero number

Input example:
```text
0
```

Output example:
```text
Zero
```

Starter code:
```python
n = int(input())  # convert to number
# TODO: print 'Zero' if n==0 else 'Non-zero'
```

<details><summary>Answer</summary>

```python
n = int(input())
if n:
    print('Non-zero')
else:
    print('Zero')
```
Explanation: 0 is false-y, so `if n:` is false for zero.
</details>

---

## Hard

### Single: Combine truthiness and not

Input example:
```text

hello
```

Output example:
```text
Printed
```

Starter code:
```python
a = input()  # may be empty
b = input()  # may be non-empty
# TODO: print 'Printed' if not a and b else 'Skipped'
```

<details><summary>Answer</summary>

```python
a = input()
b = input()
if (not a) and b:
    print('Printed')
else:
    print('Skipped')
```
Explanation: `not a` is true when a is empty; use parentheses to be clear.
</details>
