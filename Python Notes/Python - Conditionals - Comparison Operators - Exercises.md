---
tags: [python, exercises, conditionals]
difficulty: Beginner
---

# Exercises — Conditionals: Comparison Operators

See concept: [[Python - Conditionals - Comparison Operators]]

GitHub link: [Python - Conditionals - Comparison Operators](Python%20-%20Conditionals%20-%20Comparison%20Operators.md)

### Quick syntax fixes

1) Using single equals by mistake:
```python
if x = 5:
    print('yes')
```
<details><summary>Answer</summary>

```python
if x == 5:
    print('yes')
```
Explanation: Use `==` to compare values.
</details>

2) Comparing wrong types without conversion:
```python
age = input()
if age > 10:
    print('old')
```
<details><summary>Answer</summary>

```python
age = int(input())
if age > 10:
    print('old')
```
Explanation: Convert input to `int()` before numeric comparisons.
</details>

3) Chained comparison mistake:
```python
if 10 < x > 5:
    print('ok')
```
<details><summary>Answer</summary>

```python
if 5 < x < 10:
    print('ok')
```
Explanation: Order the chain correctly: `5 < x < 10`.
</details>

---

## Easy

### a) Check if two numbers are equal

Input example:
```text
4
4
```

Output example:
```text
Equal
```

Starter code:
```python
first_number = int(input())  # first_number is an integer
second_number = int(input()) # second_number is an integer
# TODO: print 'Equal' if numbers are equal else 'Not equal'
```

<details><summary>Answer</summary>

```python
first_number = int(input())
second_number = int(input())
if first_number == second_number:
    print('Equal')
else:
    print('Not equal')
```
Explanation: Use `==` to test equality.
</details>

### b) Check greater than

Input example:
```text
7
3
```

Output example:
```text
First is greater
```

Starter code:
```python
a = int(input())  # a is first number
b = int(input())  # b is second number
# TODO: print 'First is greater' if a>b else 'Not greater'
```

<details><summary>Answer</summary>

```python
a = int(input())
b = int(input())
if a > b:
    print('First is greater')
else:
    print('Not greater')
```
Explanation: Use `>` for greater-than comparison.
</details>

---

## Medium

### a) Check if number is between 1 and 10 (inclusive)

Input example:
```text
5
```

Output example:
```text
Yes
```

Starter code:
```python
n = int(input())  # n is the number to test
# TODO: print 'Yes' if 1<=n<=10 else 'No'
```

<details><summary>Answer</summary>

```python
n = int(input())
if 1 <= n <= 10:
    print('Yes')
else:
    print('No')
```
Explanation: Use chained comparisons for ranges.
</details>

### b) Compare strings for alphabetical order

Input example:
```text
apple
banana
```

Output example:
```text
apple comes before banana
```

Starter code:
```python
s1 = input()  # first word
s2 = input()  # second word
# TODO: print '<s1> comes before <s2>' if s1 < s2 else '<s1> does not come before <s2>'
```

<details><summary>Answer</summary>

```python
s1 = input()
s2 = input()
if s1 < s2:
    print(f'{s1} comes before {s2}')
else:
    print(f'{s1} does not come before {s2}')
```
Explanation: String comparison uses lexicographical order.
</details>

---

## Hard

### Single: Find the larger of three numbers

Input example:
```text
3
8
5
```

Output example:
```text
8
```

Starter code:
```python
x = int(input())  # x is first number
y = int(input())  # y is second number
z = int(input())  # z is third number
# TODO: print the largest number among x,y,z
```

<details><summary>Answer</summary>

```python
x = int(input())
y = int(input())
z = int(input())
largest = x
if y > largest:
    largest = y
if z > largest:
    largest = z
print(largest)
```
Explanation: Use simple if-statements to update the largest value.
</details>
