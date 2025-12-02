---
tags: [python, exercises, conditionals, nested]
difficulty: Beginner
---

# Python - Conditionals - Nested Conditions — Exercises

See concept: [[Python - Conditionals - Nested Conditions]]
GitHub link: [Python - Conditionals - Nested Conditions](./Python%20-%20Conditionals%20-%20Nested%20Conditions.md)

## Quick syntax fixes

1) Broken: bad indentation in nested if
```python
# Broken
if a > 0:
print('pos')
```
<details><summary>Answer</summary>

```python
# Fixed
if a > 0:
    print('pos')
```
Explanation: Nested blocks need indentation.
</details>

2) Broken: using else for inner if incorrectly
```python
# Broken
if x > 0:
    if x > 5:
    print('big')
    else:
        print('small')
```
<details><summary>Answer</summary>

```python
# Fixed
if x > 0:
    if x > 5:
        print('big')
    else:
        print('small')
```
Explanation: Inner blocks need consistent indentation.
</details>

3) Broken: returning from wrong scope
```python
# Broken
def f(x):
    if x>0:
        return 'pos'
    else:
        'neg'
```
<details><summary>Answer</summary>

```python
# Fixed
def f(x):
    if x>0:
        return 'pos'
    else:
        return 'neg'
```
Explanation: Use return in both branches.
</details>

---

## Easy

a) Given `x`, print 'big' if x>10 else if x>5 print 'mid' else print 'small'.

Starter code:
```python
x = 7
# TODO: nested conditions to print size
pass
```
<details><summary>Answer</summary>

```python
x = 7
if x > 10:
    print('big')
elif x > 5:
    print('mid')
else:
    print('small')
```
Explanation: Use `elif` for chained nested checks.
</details>

b) Check age and print category: child < 13, teen 13-17, adult 18+.

Starter code:
```python
age = 14
# TODO: print category
pass
```
<details><summary>Answer</summary>

```python
age = 14
if age < 13:
    print('child')
elif age <= 17:
    print('teen')
else:
    print('adult')
```
Explanation: Order checks carefully so ranges do not overlap.
</details>

---

## Medium

a) Validate username: if name is empty print 'bad', else if length<3 print 'short', else print 'ok'.

Starter code:
```python
name = 'Al'
# TODO: nested validation
pass
```
<details><summary>Answer</summary>

```python
name = 'Al'
if not name:
    print('bad')
elif len(name) < 3:
    print('short')
else:
    print('ok')
```
Explanation: Check emptiness before length.
</details>

b) Given score, print grade: A 90+, B 80-89, C 70-79, else F.

Starter code:
```python
score = 85
# TODO: nested grade logic
pass
```
<details><summary>Answer</summary>

```python
score = 85
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')
```
Explanation: Use descending thresholds in order.
</details>

---

## Hard

Write function `classify(n)` that returns 'even big' if n>10 and even, 'even small' if even and <=10, else 'odd'.

Starter code:
```python
def classify(n):
    # TODO: nested checks
    pass
print(classify(12))
print(classify(8))
print(classify(3))
```
<details><summary>Answer</summary>

```python
def classify(n):
    if n % 2 == 0:
        if n > 10:
            return 'even big'
        else:
            return 'even small'
    else:
        return 'odd'
print(classify(12))
print(classify(8))
print(classify(3))
```
Explanation: Check parity first, then size.
</details>
