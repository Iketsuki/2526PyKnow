---
tags: [python, exercises, io]
difficulty: Beginner
---

# Python - IO - Menu-Driven Programs — Exercises

See concept: [[Python - IO - Menu-Driven Programs]]
GitHub link: [Python - IO - Menu-Driven Programs](./Python%20-%20IO%20-%20Menu-Driven%20Programs.md)

## Quick syntax fixes

1) Broken: wrong loop to show menu once
```python
choice = input()
while choice:
    print('menu')
```
<details><summary>Answer</summary>

```python
while True:
    choice = input()
    if choice == 'q':
        break
```
Explanation: use loop and break for menu-driven programs.
</details>

2) Broken: not converting menu choice when needed
```python
choice = input()
if choice == 1:
    print('one')
```
<details><summary>Answer</summary>

```python
choice = int(input())
if choice == 1:
    print('one')
```
Explanation: convert input to int for numeric comparisons.
</details>

3) Broken: no prompt shown to user
```python
input()
```
<details><summary>Answer</summary>

```python
input('Choose option:')
```
Explanation: prompts guide the user.
</details>

---

## Easy

a) Show a menu with options 1 and q, print a message for 1.

Starter code:
```python
# TODO: read choice and act
pass
```
<details><summary>Answer</summary>

```python
choice = input('1=hi, q=quit:')
if choice == '1':
    print('hi')
```
Explanation: simple single-choice menu.
</details>

b) Loop until user enters 'q'.

Starter code:
```python
# TODO: loop until q
pass
```
<details><summary>Answer</summary>

```python
while True:
    if input('>') == 'q':
        break
```
Explanation: loop and break on quit.
</details>

---

## Medium

a) Implement a menu that adds numbers to a list and prints list on command.

Starter code:
```python
items = []
# TODO: menu add/list/quit
pass
```
<details><summary>Answer</summary>

```python
items = []
while True:
    cmd = input('a=add,l=list,q=quit:')
    if cmd == 'a':
        items.append(input('item:'))
    elif cmd == 'l':
        print(items)
    elif cmd == 'q':
        break
```
Explanation: basic menu loop with commands.
</details>

b) Use a menu to choose between adding and summing numbers.

Starter code:
```python
# TODO: add or sum numbers
pass
```
<details><summary>Answer</summary>

```python
nums = []
while True:
    cmd = input('a=add,s=sum,q=quit:')
    if cmd == 'a':
        nums.append(int(input()))
    elif cmd == 's':
        print(sum(nums))
    elif cmd == 'q':
        break
```
Explanation: combine menu with accumulation.
</details>

---

## Hard

Write a menu-driven program that saves items to `data.txt` on exit.

Starter code:
```python
items = []
# TODO: menu and write on quit
pass
```
<details><summary>Answer</summary>

```python
items = []
while True:
    cmd = input('a=add,l=list,q=quit:')
    if cmd == 'a':
        items.append(input('item:'))
    elif cmd == 'l':
        print(items)
    elif cmd == 'q':
        break
with open('data.txt','w') as f:
    for it in items:
        f.write(it + '\n')
```
Explanation: persist items on quit using file IO.
</details>
