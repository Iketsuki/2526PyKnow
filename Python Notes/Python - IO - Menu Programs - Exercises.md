---
tags: [python, exercises, io, menu]
difficulty: Beginner
---

# Python - IO - Menu Programs — Exercises

See concept: [[Python - IO - Menu Programs]]
GitHub link: [Python - IO - Menu Programs](./Python%20-%20IO%20-%20Menu%20Programs.md)

## Quick syntax fixes

1) Broken: using `input` but not converting
```python
# Broken
choice = input('1 or 2: ')
if choice == 1:
    print('one')
```
<details><summary>Answer</summary>

```python
# Fixed
choice = input('1 or 2: ')
if choice == '1':
    print('one')
```
Explanation: `input` returns a string; compare with string.
</details>

2) Broken: menu without loop
```python
# Broken
print('1. Say hi')
print('2. Quit')
choice = input()
# program ends
```
<details><summary>Answer</summary>

```python
# Fixed simple loop
while True:
    print('1. Say hi')
    print('2. Quit')
    choice = input()
    if choice == '2':
        break
```
Explanation: Use a loop to keep showing the menu.
</details>

3) Broken: invalid choice handling
```python
# Broken
choice = input('1 or 2: ')
if choice == '3':
    print('not valid')
```
<details><summary>Answer</summary>

```python
# Fixed
choice = input('1 or 2: ')
if choice not in ('1', '2'):
    print('not valid')
```
Explanation: Check for allowed options.
</details>

---

## Easy

a) Show a menu with 1) Hello 2) Quit. If 1, print Hello. If 2, exit.

Starter code:
```python
# TODO: write simple menu
```
<details><summary>Answer</summary>

```python
while True:
    print('1. Hello')
    print('2. Quit')
    choice = input('> ')
    if choice == '1':
        print('Hello')
    elif choice == '2':
        break
```
Explanation: Loop until user chooses Quit.
</details>

b) Add a menu option that asks for a number and prints its square.

Starter code:
```python
# TODO: add option 2 to square a number
```
<details><summary>Answer</summary>

```python
while True:
    print('1. Hello')
    print('2. Square a number')
    print('3. Quit')
    choice = input('> ')
    if choice == '1':
        print('Hello')
    elif choice == '2':
        try:
            n = int(input('n: '))
            print(n * n)
        except ValueError:
            print('bad input')
    elif choice == '3':
        break
```
Explanation: Convert input and handle bad input.
</details>

---

## Medium

a) Add input validation so non-numbers do not crash the menu.

Starter code:
```python
# TODO: wrap int conversion in try/except
```
<details><summary>Answer</summary>

```python
while True:
    print('1. Square')
    print('2. Quit')
    choice = input('> ')
    if choice == '1':
        try:
            n = int(input('n: '))
            print(n * n)
        except ValueError:
            print('bad input')
    elif choice == '2':
        break
```
Explanation: Use try/except to handle bad user input.
</details>

b) Track how many times each option was used and print counts on exit.

Starter code:
```python
# TODO: implement counters and print on exit
```
<details><summary>Answer</summary>

```python
count_hello = 0
count_square = 0
while True:
    print('1. Hello')
    print('2. Square')
    print('3. Quit')
    choice = input('> ')
    if choice == '1':
        print('Hello')
        count_hello += 1
    elif choice == '2':
        try:
            n = int(input('n: '))
            print(n * n)
            count_square += 1
        except ValueError:
            print('bad input')
    elif choice == '3':
        print('hello used', count_hello)
        print('square used', count_square)
        break
```
Explanation: Use counters to track usage.
</details>

---

## Hard

Store entered names in a list and print them when user chooses 'show names'.

Starter code:
```python
# TODO: implement add name, show names, quit
```
<details><summary>Answer</summary>

```python
names = []
while True:
    print('1. Add name')
    print('2. Show names')
    print('3. Quit')
    c = input('> ')
    if c == '1':
        n = input('name: ')
        names.append(n)
    elif c == '2':
        print(names)
    elif c == '3':
        break
```
Explanation: Use a list to collect names and show when requested.
</details>
