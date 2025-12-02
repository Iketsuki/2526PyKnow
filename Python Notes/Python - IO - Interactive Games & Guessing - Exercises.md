---
tags: [python, exercises, io, games]
difficulty: Beginner
---

# Python - IO - Interactive Games & Guessing — Exercises

See concept: [[Python - IO - Interactive Games & Guessing]]
GitHub link: [Python - IO - Interactive Games & Guessing](./Python%20-%20IO%20-%20Interactive%20Games%20%26%20Guessing.md)

## Quick syntax fixes

1) Broken: not converting guess to int
```python
guess = input('guess:')
if guess == 5:
    print('win')
```
<details><summary>Answer</summary>

```python
guess = int(input('guess:'))
if guess == 5:
    print('win')
```
Explanation: convert input to int for numeric comparison.
</details>

2) Broken: not giving user a prompt
```python
input()
```
<details><summary>Answer</summary>

```python
input('Enter guess:')
```
Explanation: prompts help the user know what to type.
</details>

3) Broken: infinite loop without break
```python
while True:
    x = input()
```
<details><summary>Answer</summary>

```python
while True:
    x = input()
    if x == '':
        break
```
Explanation: include a break condition for loops reading input.
</details>

---

## Easy

a) Ask user for a number and print 'big' if >10 else 'small'.

Starter code:
```python
# TODO: read and compare
pass
```
<details><summary>Answer</summary>

```python
n = int(input())
if n > 10:
    print('big')
else:
    print('small')
```
Explanation: simple branching in a game.
</details>

b) Simple guess: read one guess, compare to secret 7.

Starter code:
```python
# TODO: compare guess to 7
pass
```
<details><summary>Answer</summary>

```python
guess = int(input())
if guess == 7:
    print('win')
else:
    print('no')
```
Explanation: basic interactive check.
</details>

---

## Medium

a) Loop up to 3 guesses, print 'win' and stop if correct.

Starter code:
```python
# TODO: up to 3 tries
pass
```
<details><summary>Answer</summary>

```python
secret = 5
for _ in range(3):
    if int(input()) == secret:
        print('win')
        break
else:
    print('lost')
```
Explanation: for/else runs when loop not broken.
</details>

b) Give hint 'low' or 'high' when guess is wrong.

Starter code:
```python
secret = 10
# TODO: hint low/high
pass
```
<details><summary>Answer</summary>

```python
secret = 10
g = int(input())
if g < secret:
    print('low')
elif g > secret:
    print('high')
else:
    print('win')
```
Explanation: conditional hints improve play.
</details>

---

## Hard

Write a small looped game that asks for guesses until correct, count attempts and print attempts.

Starter code:
```python
def guessing_game():
    # TODO: loop until correct and return count
    pass

print(guessing_game())
```
<details><summary>Answer</summary>

```python
def guessing_game():
    secret = 3
    attempts = 0
    while True:
        attempts += 1
        if int(input()) == secret:
            return attempts

print(guessing_game())
```
Explanation: count attempts and return when correct.
</details>
