---
tags: [python, exercises, io]
difficulty: Beginner
---

# Exercises — IO: Form-Like Input Collection

See concept: [[Python - IO - Form-Like Input Collection]]

GitHub link: [Python - IO - Form-Like Input Collection](./Python%20-%20IO%20-%20Form-Like%20Input%20Collection.md)

### Quick syntax fixes

1) Using input prompts without parentheses:
```python
name = input'Name:'
```
<details><summary>Answer</summary>

```python
name = input('Name:')
```
Explanation: `input()` requires parentheses and a string argument for prompt.
</details>

2) Forgetting to strip user input:
```python
s = input()
print(s == 'yes')
```
<details><summary>Answer</summary>

```python
s = input().strip()
print(s == 'yes')
```
Explanation: `strip()` removes extra whitespace from user input.
</details>

3) Not converting numbers from input:
```python
age = input('Age:')
print(age + 1)
```
<details><summary>Answer</summary>

```python
age = int(input('Age:'))
print(age + 1)
```
Explanation: Convert to `int` for arithmetic.
</details>

---

## Easy

### a) Collect name and age, then greet

Input example:
```text
Alice
7
```

Output example:
```text
Hello Alice, you are 7
```

Starter code:
```python
name = input()   # name is the user's name
age = input()    # age is the user's age as string
# TODO: print greeting using name and age
```

<details><summary>Answer</summary>

```python
name = input()
age = input()
print(f'Hello {name}, you are {age}')
```
Explanation: Use f-string for simple formatting.
</details>

### b) Collect three answers and print them on one line

Input example:
```text
blue
green
red
```

Output example:
```text
blue, green, red
```

Starter code:
```python
a1 = input()
a2 = input()
a3 = input()
# TODO: print answers separated by comma and space
```

<details><summary>Answer</summary>

```python
a1 = input()
a2 = input()
a3 = input()
print(a1, a2, a3, sep=', ')
```
Explanation: Use `sep=', '` to join with comma and space.
</details>

---

## Medium

### a) Simple 3-question quiz that counts correct answers

Input example:
```text
red
5
yes
```

Output example:
```text
2
```

Starter code:
```python
# three answers are expected from the user
# TODO: compare them with correct answers and print the count of correct
```

<details><summary>Answer</summary>

```python
ans1 = input()
ans2 = input()
ans3 = input()
correct = 0
if ans1 == 'red':
    correct += 1
if ans2 == '5':
    correct += 1
if ans3 == 'yes':
    correct += 1
print(correct)
```
Explanation: Use simple if checks to count correct responses.
</details>

### b) Validate numeric input between 1 and 10

Input example:
```text
11
```

Output example:
```text
Out of range
```

Starter code:
```python
n = int(input())  # user number
# TODO: print 'OK' if 1<=n<=10 else 'Out of range'
```

<details><summary>Answer</summary>

```python
n = int(input())
if 1 <= n <= 10:
    print('OK')
else:
    print('Out of range')
```
Explanation: Check range using chained comparison.
</details>

---

## Hard

### Single: Read form values until a blank line and print them as a list

Input example:
```text
apple
banana

```

Output example:
```text
['apple', 'banana']
```

Starter code:
```python
# Read lines until empty line and store them in a list
# TODO: implement the loop to collect items and then print the list
```

<details><summary>Answer</summary>

```python
items = []
while True:
    line = input()
    if line == '':
        break
    items.append(line)
print(items)
```
Explanation: Loop until empty input and append each non-empty value.
</details>
