---
tags: [python, exercises, variables, mutability]
difficulty: Beginner
---

# Python - Variables - Mutability & Immutability — Exercises

See concept: [[Python - Variables - Mutability & Immutability]]
GitHub link: [Python - Variables - Mutability & Immutability](./Python%20-%20Variables%20-%20Mutability%20%26%20Immutability.md)

## Quick syntax fixes

1) Broken code: trying to change a character in a string
```python
# Broken example
word = 'cat'
word[0] = 'b'
print(word)
```
<details><summary>Answer</summary>

```python
# Fixed
word = 'cat'
new_word = 'b' + word[1:]
print(new_word)
```
Explanation: Strings are immutable. Make a new string instead.
</details>

2) Broken code: modifying a list item but printing the wrong variable
```python
# Broken example
my_list = [1, 2, 3]
my_list[0] = 9
print(list)
```
<details><summary>Answer</summary>

```python
# Fixed
my_list = [1, 2, 3]
my_list[0] = 9
print(my_list)
```
Explanation: `list` is a type name; use the variable `my_list`.
</details>

3) Broken code: trying to append to a string
```python
# Broken example
name = 'Ada'
name.append('m')
print(name)
```
<details><summary>Answer</summary>

```python
# Fixed
name = 'Ada'
name = name + 'm'
print(name)
```
Explanation: Use concatenation to make a new string.
</details>

---

## Easy

a) Replace the first item in a list with a new number.

Input example:
```text
Start list: [10, 20, 30]
Replace with: 5
```
Output example:
```text
[5, 20, 30]
```
Starter code:
```python
start_list = [10, 20, 30]  # start_list means the numbers
new_first = 5  # new_first means the new first number
# TODO: change the first item in start_list to new_first
print(start_list)
```
<details><summary>Answer</summary>

```python
start_list = [10, 20, 30]
new_first = 5
start_list[0] = new_first
print(start_list)
```
Explanation: Lists are mutable; assign to index 0.
</details>

b) Make a new string by changing the first letter.

Input example:
```text
word = cat
first letter = b
```
Output example:
```text
bat
```
Starter code:
```python
word = 'cat'  # word means the original word
first_letter = 'b'  # first_letter means the new first character
# TODO: build a new string that starts with first_letter
print(word)
```
<details><summary>Answer</summary>

```python
word = 'cat'
first_letter = 'b'
new_word = first_letter + word[1:]
print(new_word)
```
Explanation: Strings are immutable so we make a new string.
</details>

---

## Medium

a) Given a list of names, change the last name to 'Sam' and print the list.

Input example:
```text
names = ['Ana', 'Ben', 'Cara']
```
Output example:
```text
['Ana', 'Ben', 'Sam']
```
Starter code:
```python
names = ['Ana', 'Ben', 'Cara']  # names means the list of names
# TODO: set the last name to 'Sam'
print(names)
```
<details><summary>Answer</summary>

```python
names = ['Ana', 'Ben', 'Cara']
names[-1] = 'Sam'
print(names)
```
Explanation: Use index -1 to set the last item in a list.
</details>

b) Replace a character in the middle of a word with 'x'.

Input example:
```text
word = 'hello'
index = 1
```
Output example:
```text
hxllo
```
Starter code:
```python
word = 'hello'  # word means the original word
index = 1  # index means the position to replace (0 is first)
# TODO: create new_word with character at index replaced by 'x'
print(word)
```
<details><summary>Answer</summary>

```python
word = 'hello'
index = 1
new_word = word[:index] + 'x' + word[index+1:]
print(new_word)
```
Explanation: Slices build a new string around the changed character.
</details>

---

## Hard

Replace every even number in a list with 0 and print the new list.

Input example:
```text
numbers = [1, 2, 3, 4, 5]
```
Output example:
```text
[1, 0, 3, 0, 5]
```
Starter code:
```python
numbers = [1, 2, 3, 4, 5]  # numbers means the list of numbers
# TODO: change each even number to 0
print(numbers)
```
<details><summary>Answer</summary>

```python
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = 0
print(numbers)
```
Explanation: Lists are mutable, loop and set items by index.
</details>
