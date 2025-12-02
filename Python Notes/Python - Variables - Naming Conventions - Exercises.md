---
tags: [python, exercises, variables]
difficulty: Beginner
---

# Exercises — Variables: Naming Conventions

See concept: [[Python - Variables - Naming Conventions]]

GitHub link: [Python - Variables - Naming Conventions](./Python%20-%20Variables%20-%20Naming%20Conventions.md)

### Quick syntax fixes

1) Using a dash in name:
```python
first-name = 'Ana'
```
<details><summary>Answer</summary>

```python
first_name = 'Ana'
```
Explanation: Use underscores, not dashes, in variable names.
</details>

2) Starting name with number:
```python
1st = 5
```
<details><summary>Answer</summary>

```python
first = 5
```
Explanation: Variable names cannot start with digits.
</details>

3) Using capital letters for constants only:
```python
MyVar = 2
```
<details><summary>Answer</summary>

```python
my_var = 2
```
Explanation: Use lowercase with underscores for regular variables.
</details>

---

## Easy

### a) Make a good variable name and print it

Input example:
```text
Ana
```

Output example:
```text
Hello Ana
```

Starter code:
```python
person_name = input()  # person_name is the learner's name
# TODO: print 'Hello ' + person_name
```

<details><summary>Answer</summary>

```python
person_name = input()
print('Hello', person_name)
```
Explanation: Use clear variable names with underscore separators.
</details>

### b) Use all lowercase variable

Input example:
```text
7
```

Output example:
```text
7
```

Starter code:
```python
num_value = int(input())  # num_value represents a number
# TODO: print num_value
```

<details><summary>Answer</summary>

```python
num_value = int(input())
print(num_value)
```
Explanation: Use readable lowercase names for normal variables.
</details>

---

## Medium

### a) Rename bad variables to good ones (exercise shows mapping)

Starter code:
```python
# bad: x = 5
# bad: var1 = 'a'
# TODO: rewrite with clearer names
```

<details><summary>Answer</summary>

```python
count = 5
letter = 'a'
print(count)
print(letter)
```
Explanation: Choose names that tell what the variable holds.
</details>

### b) Avoid reserved word

Starter code:
```python
# TODO: change variable named 'list' to 'items' and print it
items = ['a', 'b']
print(items)
```

<details><summary>Answer</summary>

```python
items = ['a', 'b']
print(items)
```
Explanation: Avoid shadowing built-in names like `list`, `str`, `int`.
</details>

---

## Hard

### Single: Create three meaningful variable names and print them

Input example:
```text
(no input)
```

Output example:
```text
John
5
['a']
```

Starter code:
```python
# TODO: set variables 'student_name', 'student_age', 'student_items' and print each
```

<details><summary>Answer</summary>

```python
student_name = 'John'
student_age = 5
student_items = ['a']
print(student_name)
print(student_age)
print(student_items)
```
Explanation: Use long, descriptive variable names for clarity.
</details>
