---
tags: [python, exercises, conditionals]
difficulty: Beginner
---

# Exercises — Conditionals: AND Operator

See concept: [[Python - Conditionals - AND Operator]]

GitHub link: [Python - Conditionals - AND Operator](Python%20-%20Conditionals%20-%20AND%20Operator.md)

### Quick syntax fixes

1) Missing parentheses around input conversion:
```python
x = int(input)
if x > 0 and x < 10:
    print('ok')
```
<details><summary>Answer</summary>

```python
x = int(input())
if x > 0 and x < 10:
    print('ok')
```
Explanation: Call `input()` with parentheses before converting.
</details>

2) Using `and` with wrong operands:
```python
if x and y > 0:
    print('ok')
```
<details><summary>Answer</summary>

```python
if x > 0 and y > 0:
    print('ok')
```
Explanation: Compare each variable explicitly.
</details>

3) Indentation error in compound condition:
```python
if a > 1 and b > 2
print('yes')
```
<details><summary>Answer</summary>

```python
if a > 1 and b > 2:
    print('yes')
```
Explanation: Add colon and indent the body.
</details>

---

## Easy

### a) Check both positive

Input example:
```text
3
4
```

Output example:
```text
Both positive
```

Starter code:
```python
first_number = int(input())  # first_number is an integer
second_number = int(input()) # second_number is an integer
# TODO: print 'Both positive' if both >0 else 'Not both positive'
```

<details><summary>Answer</summary>

```python
first_number = int(input())
second_number = int(input())
if first_number > 0 and second_number > 0:
    print('Both positive')
else:
    print('Not both positive')
```
Explanation: Use `and` to require both conditions.
</details>

### b) Check in range with and

Input example:
```text
7
```

Output example:
```text
In range
```

Starter code:
```python
n = int(input())  # n is the number
# TODO: print 'In range' if n>5 and n<10 else 'Out of range'
```

<details><summary>Answer</summary>

```python
n = int(input())
if n > 5 and n < 10:
    print('In range')
else:
    print('Out of range')
```
Explanation: Two comparisons joined by `and`.
</details>

---

## Medium

### a) Check age and city

Input example:
```text
14
London
```

Output example:
```text
Teen in London
```

Starter code:
```python
age = int(input())   # age in years
city = input()       # city name
# TODO: print 'Teen in <city>' if age between 13 and 17 and city == 'London' else 'Other'
```

<details><summary>Answer</summary>

```python
age = int(input())
city = input()
if age >= 13 and age <= 17 and city == 'London':
    print(f'Teen in {city}')
else:
    print('Other')
```
Explanation: Chain multiple `and` conditions for combined checks.
</details>

### b) Both strings non-empty

Input example:
```text
hello
world
```

Output example:
```text
Good
```

Starter code:
```python
s1 = input()  # first string
s2 = input()  # second string
# TODO: print 'Good' if both strings are not empty
```

<details><summary>Answer</summary>

```python
s1 = input()
s2 = input()
if s1 != '' and s2 != '':
    print('Good')
else:
    print('Bad')
```
Explanation: Check both are non-empty strings.
</details>

---

## Hard

### Single: All numbers positive

Input example:
```text
1
2
3
```

Output example:
```text
All positive
```

Starter code:
```python
a = int(input())  # first number
b = int(input())  # second number
c = int(input())  # third number
# TODO: print 'All positive' if a,b,c all >0 else 'Some not positive'
```

<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0:
    print('All positive')
else:
    print('Some not positive')
```
Explanation: Use `and` with three comparisons to require all be true.
</details>
