---
tags: [python, exercises, conditionals]
difficulty: Beginner
---

# Exercises — Conditionals: If-Else Basics

See concept: [[Python - Conditionals - If-Else Basics]]

### Quick syntax fixes

1) Missing colon after if:
```python
if x > 0
    print('pos')
```
<details><summary>Answer</summary>

```python
if x > 0:
    print('pos')
```
Explanation: Add `:` after the `if` header.
</details>

2) Using = instead of ==:
```python
if x = 3:
    print('yes')
```
<details><summary>Answer</summary>

```python
if x == 3:
    print('yes')
```
Explanation: Use `==` to compare values.
</details>

3) Indentation for else:
```python
if x>0:
    print('a')
else
print('b')
```
<details><summary>Answer</summary>

```python
if x>0:
    print('a')
else:
    print('b')
```
Explanation: `else` needs colon and body indented.
</details>

---

## Easy

### a) Check if a number is positive

Input example:
```text
5
```

Output example:
```text
Positive
```

Starter code:
```python
n = int(input())
# TODO: print 'Positive' if n>0 else 'Not positive'
```

<details><summary>Answer</summary>

```python
n = int(input())
if n > 0:
    print('Positive')
else:
    print('Not positive')
```
Explanation: Simple if-else checks the sign.
</details>

### b) Check even or odd

Input example:
```text
4
```

Output example:
```text
Even
```

Starter code:
```python
n = int(input())
# TODO: print 'Even' or 'Odd'
```

<details><summary>Answer</summary>

```python
n = int(input())
if n % 2 == 0:
    print('Even')
else:
    print('Odd')
```
Explanation: Use modulo to test evenness.
</details>

---

## Medium

### a) Check grade letter from score

Input example:
```text
85
```

Output example:
```text
B
```

Starter code:
```python
score = int(input())
# TODO: print A for >=90, B for 80-89, C for 70-79, else F
```

<details><summary>Answer</summary>

```python
score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')
```
Explanation: Use `elif` for ranges.
</details>

### b) Check name length and print short/long

Input example:
```text
Eve
```

Output example:
```text
Short
```

Starter code:
```python
name = input()
# TODO: print 'Short' if len(name)<5 else 'Long'
```

<details><summary>Answer</summary>

```python
name = input()
if len(name) < 5:
    print('Short')
else:
    print('Long')
```
Explanation: Use `len()` to check string length.
</details>

---

## Hard

### Single: Category from age

Input example:
```text
12
```

Output example:
```text
Child
```

Starter code:
```python
age = int(input())
# TODO: print Child for age<13, Teen for 13-17, Adult for 18+
```

<details><summary>Answer</summary>

```python
age = int(input())
if age < 13:
    print('Child')
elif age <= 17:
    print('Teen')
else:
    print('Adult')
```
Explanation: Combine comparisons with `elif` for ranges.
</details>
