---
tags: [python, exercises, conditionals]
difficulty: Beginner
---

# Exercises — Conditionals: OR Operator

See concept: [[Python - Conditionals - OR Operator]]

GitHub link: [Python - Conditionals - OR Operator](Python%20-%20Conditionals%20-%20OR%20Operator.md)

### Quick syntax fixes

1) Using `or` wrong placement:
```python
if x > 0 or < 10:
    print('ok')
```
<details><summary>Answer</summary>

```python
if x > 0 or x < 10:
    print('ok')
```
Explanation: Repeat the variable for each comparison when needed.
</details>

2) Always-true `or` misuse:
```python
if True or x>0:
    print('yes')
```
<details><summary>Answer</summary>

```python
# Avoid using True; write a meaningful condition instead.
if x > 0 or x == 0:
    print('yes')
```
Explanation: `True or ...` always runs; give real conditions.
</details>

3) Parentheses needed for combined logic:
```python
if x > 0 and y < 5 or z > 3:
    print('ok')
```
<details><summary>Answer</summary>

```python
if (x > 0 and y < 5) or z > 3:
    print('ok')
```
Explanation: Use parentheses to clarify grouping when logic mixes `and`/`or`.
</details>

---

## Easy

### a) Check if either number is zero

Input example:
```text
0
3
```

Output example:
```text
Has zero
```

Starter code:
```python
a = int(input())  # a is first number
b = int(input())  # b is second number
# TODO: print 'Has zero' if a==0 or b==0 else 'No zero'
```

<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
if a == 0 or b == 0:
    print('Has zero')
else:
    print('No zero')
```
Explanation: `or` requires only one of conditions to be true.
</details>

### b) Check word is 'yes' or 'y'

Input example:
```text
y
```

Output example:
```text
Yes
```

Starter code:
```python
w = input()  # w is word typed by user
# TODO: print 'Yes' if w is 'yes' or 'y' else 'No'
```

<details><summary>Answer</summary>

```python
w = input()
if w == 'yes' or w == 'y':
    print('Yes')
else:
    print('No')
```
Explanation: `or` checks multiple possible matches.
</details>

---

## Medium

### a) Age or name check

Input example:
```text
12
Sam
```

Output example:
```text
Allowed
```

Starter code:
```python
age = int(input())  # age in years
name = input()      # name of person
# TODO: print 'Allowed' if age>=18 or name == 'Sam' else 'Denied'
```

<details><summary>Answer</summary>

```python
age = int(input())
name = input()
if age >= 18 or name == 'Sam':
    print('Allowed')
else:
    print('Denied')
```
Explanation: `or` lets special names pass regardless of age.
</details>

### b) Either in list

Input example:
```text
apple
```

Output example:
```text
Fruit found
```

Starter code:
```python
w = input()  # a word
# TODO: print 'Fruit found' if w is 'apple' or 'banana' else 'Not found'
```

<details><summary>Answer</summary>

```python
w = input()
if w == 'apple' or w == 'banana':
    print('Fruit found')
else:
    print('Not found')
```
Explanation: Use `or` to allow multiple acceptable values.
</details>

---

## Hard

### Single: Check multiple conditions with grouping

Input example:
```text
5
2
4
```

Output example:
```text
Yes
```

Starter code:
```python
x = int(input())
y = int(input())
z = int(input())
# TODO: print 'Yes' if (x>3 and y<3) or z>3 else 'No'
```

<details><summary>Answer</summary>

```python
x = int(input())
y = int(input())
z = int(input())
if (x > 3 and y < 3) or z > 3:
    print('Yes')
else:
    print('No')
```
Explanation: Use parentheses to ensure correct logic grouping.
</details>
