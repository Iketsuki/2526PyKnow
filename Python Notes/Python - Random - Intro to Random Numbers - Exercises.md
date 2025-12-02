---
tags: [python, exercises, random]
difficulty: Beginner
---

# Python - Random - Intro to Random Numbers — Exercises

See concept: [[Python - Random - Intro to Random Numbers]]
GitHub link: [Python - Random - Intro to Random Numbers](./Python%20-%20Random%20-%20Intro%20to%20Random%20Numbers.md)

## Quick syntax fixes

1) Broken: forgetting to import module
```python
# Broken
print(random.randint(1, 6))
```
<details><summary>Answer</summary>

```python
# Fixed
import random
print(random.randint(1, 6))
```
Explanation: Import `random` before using it.
</details>

2) Broken: using wrong function name
```python
# Broken
import random
print(random.randomint(1,6))
```
<details><summary>Answer</summary>

```python
# Fixed
import random
print(random.randint(1, 6))
```
Explanation: The correct function is `randint`.
</details>

3) Broken: expecting float from randint
```python
# Example
import random
print(random.randint(1, 3))
```
<details><summary>Answer</summary>

```python
# prints integer 1,2,or3
import random
print(random.randint(1, 3))
```
Explanation: `randint` returns an integer in the inclusive range.
</details>

---

## Easy

a) Print a random integer between 1 and 10.

Starter code:
```python
# TODO: print random int 1-10
```
<details><summary>Answer</summary>

```python
import random
print(random.randint(1, 10))
```
Explanation: Use `randint` from `random` module.
</details>

b) Choose a random item from a list `['red','green','blue']` and print it.

Starter code:
```python
colors = ['red','green','blue']
# TODO: pick and print random color
```
<details><summary>Answer</summary>

```python
import random
colors = ['red','green','blue']
print(random.choice(colors))
```
Explanation: Use `random.choice` to pick an item.
</details>

---

## Medium

a) Simulate rolling two dice and print their sum.

Starter code:
```python
# TODO: roll two dice and print sum
```
<details><summary>Answer</summary>

```python
import random
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
print(d1 + d2)
```
Explanation: Roll with `randint` and add results.
</details>

b) Shuffle a list and print result.

Starter code:
```python
items = [1,2,3,4]
# TODO: shuffle and print items
```
<details><summary>Answer</summary>

```python
import random
items = [1,2,3,4]
random.shuffle(items)
print(items)
```
Explanation: `random.shuffle` reorders list in place.
</details>

---

## Hard

Write a program that picks a random secret number 1-10 and asks the user to guess until correct, printing number of tries.

Starter code:
```python
# TODO: implement guess loop and count tries
```
<details><summary>Answer</summary>

```python
import random
secret = random.randint(1, 10)
tries = 0
while True:
    try:
        guess = int(input('guess: '))
        tries += 1
        if guess == secret:
            print('correct', tries)
            break
        elif guess < secret:
            print('too low')
        else:
            print('too high')
    except ValueError:
        print('enter a number')
```
Explanation: Use randint for secret and loop until guessed.
</details>
