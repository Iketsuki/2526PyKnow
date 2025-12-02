---
tags: [python, exercises, io, input]
difficulty: Beginner
---

# Exercises — Input Basics

See concept: [[Python - IO - Input Basics]]

### Quick syntax fixes

1) Missing parentheses for input prompt:  
```python
name = input"Your name: "
```
<details><summary>Answer</summary>

```python
name = input("Your name: ")
```
Explanation: `input()` needs parentheses and a string argument is inside them.
</details>

2) Converting input to int wrongly:
```python
age = int(input)
```
<details><summary>Answer</summary>

```python
age = int(input())
```
Explanation: Call `input()` and pass its result to `int()`.
</details>

3) Using input but forgetting to store:
```python
input("Type here")
print(text)
```
<details><summary>Answer</summary>

```python
text = input("Type here")
print(text)
```
Explanation: Save the result of `input()` into a variable.
</details>

---

## Easy

### a) Read two names and greet them on separate lines

Input example:
```text
Anna
Ben
```

Output example:
```text
Hello Anna
Hello Ben
```

Starter code:
```python
name1 = input()
name2 = input()
# TODO: print two greetings, one per line
```

<details><summary>Answer</summary>

```python
name1 = input()
name2 = input()
print('Hello', name1)
print('Hello', name2)
```
Explanation: Use two `print` calls to make separate lines.
</details>

### b) Read a number and print double

Input example:
```text
6
```

Output example:
```text
12
```

Starter code:
```python
n = input()
# TODO: convert to int and print twice the number
```

<details><summary>Answer</summary>

```python
n = int(input())
print(n * 2)
```
Explanation: Convert input to `int` before math.
</details>

---

## Medium

### a) Read name and age, then print sentence

Input example:
```text
Lina
9
```

Output example:
```text
Lina is 9 years old.
```

Starter code:
```python
name = input()
age = input()
# TODO: print the sentence exactly
```

<details><summary>Answer</summary>

```python
name = input()
age = input()
print(f"{name} is {age} years old.")
```
Explanation: f-strings make simple formatted text.
</details>

### b) Read two numbers and print their sum

Input example:
```text
3
5
```

Output example:
```text
8
```

Starter code:
```python
a = input()
b = input()
# TODO: convert to int and print sum
```

<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
print(a + b)
```
Explanation: Convert each input to `int` before adding.
</details>

---

## Hard

### Single: Read a list count and print numbers on one line

Input example:
```text
3
10
20
30
```

Output example:
```text
10 20 30
```

Starter code:
```python
n = int(input())
# TODO: read n numbers and print them on one line separated by spaces
```

<details><summary>Answer</summary>

```python
n = int(input())
nums = []
for _ in range(n):
    nums.append(input())
print(' '.join(nums))
```
Explanation: Collect strings and `join` with spaces to print on one line.
</details>
