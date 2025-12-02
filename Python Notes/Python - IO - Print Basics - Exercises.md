---
tags: [python, exercises, io, print]
difficulty: Beginner
---

# Exercises — Print Basics

See concept: [[Python - IO - Print Basics]]

### Quick syntax fixes

1) Fix the syntax to print:  
```python
print'Hello'
```
<details><summary>Answer</summary>

```python
print('Hello')
```
Explanation: `print` needs parentheses in Python 3.
</details>

2) Fix missing comma between values:  
```python
print('Name' 'Alice')
```
<details><summary>Answer</summary>

```python
print('Name', 'Alice')
```
Explanation: Use a comma to separate values for `print`.
</details>

3) Fix string quotes:  
```python
print("She said: 'Hi)
```
<details><summary>Answer</summary>

```python
print("She said: 'Hi'")
```
Explanation: Close the quotes properly.
</details>

---

## Easy

### a) Print name and age on one line

Input example:
```text
Alice
7
```

Output example:
```text
Name: Alice, Age: 7
```

Starter code:
```python
name = input()
age = input()
# TODO: print the text exactly as the output example
```

<details><summary>Answer</summary>

```python
name = input()
age = input()
print('Name:', name + ',', 'Age:', age)
```
Explanation: Use `print` with commas and simple string concatenation for clarity.
</details>

### b) Print numbers with dash separator

Input example:
```text
3
4
5
```

Output example:
```text
3-4-5
```

Starter code:
```python
a = input()
b = input()
c = input()
# TODO: print the numbers with '-' between them
```

<details><summary>Answer</summary>

```python
a = input()
b = input()
c = input()
print(a, b, c, sep='-')
```
Explanation: `print(..., sep='-')` sets the separator.
</details>

---

## Medium

### a) Print a greeting using variables

Input example:
```text
Tom
10
```

Output example:
```text
Hello Tom! You are 10 years old.
```

Starter code:
```python
name = input()
age = input()
# TODO: print greeting exactly like the output example
```

<details><summary>Answer</summary>

```python
name = input()
age = input()
print(f'Hello {name}! You are {age} years old.')
```
Explanation: Use f-strings to insert variables simply.
</details>

### b) Show items on one line with commas

Input example:
```text
apple
banana
cherry
```

Output example:
```text
apple, banana, cherry
```

Starter code:
```python
x = input()
y = input()
z = input()
# TODO: print items on one line separated by commas and space
```

<details><summary>Answer</summary>

```python
x = input()
y = input()
z = input()
print(x, y, z, sep=', ')
```
Explanation: `sep=', '` inserts a comma and a space between values.
</details>

---

## Hard

### Single: Format a table row

Input example:
```text
Day
Sunny
25
```

Output example:
```text
Day | Sunny | 25°C
```

Starter code:
```python
label = input()
weather = input()
temp = input()
# TODO: print exactly like the output example, with degree symbol after temp
```

<details><summary>Answer</summary>

```python
label = input()
weather = input()
temp = input()
print(label, '|', weather, '|', temp + '°C')
```
Explanation: Concatenate the degree symbol to the temperature and use `print` separators.
</details>
