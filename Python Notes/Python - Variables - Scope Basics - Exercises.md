---
tags: [python, exercises, variables, scope]
difficulty: Beginner
---

# Python - Variables - Scope Basics — Exercises

See concept: [[Python - Variables - Scope Basics]]
GitHub link: [Python - Variables - Scope Basics](./Python%20-%20Variables%20-%20Scope%20Basics.md)

## Quick syntax fixes

1) Broken code: using a function variable outside the function
```python
# Broken example
def make_number():
    number = 5
    return
print(number)
```
<details><summary>Answer</summary>

```python
# Fixed
def make_number():
    number = 5
    return number
number = make_number()
print(number)
```
Explanation: Variables inside a function are local; return them to use outside.
</details>

2) Broken code: forgetting to call the function that sets a value
```python
# Broken example
count = 0
def set_count():
    count = 3
set_count
print(count)
```
<details><summary>Answer</summary>

```python
# Fixed
count = 0
def set_count():
    return 3
count = set_count()
print(count)
```
Explanation: Call the function and assign its returned value.
</details>

3) Broken code: using global without intent
```python
# Broken example
value = 1
def change():
    value = value + 1
change()
print(value)
```
<details><summary>Answer</summary>

```python
# Fixed (explicit local assignment)
value = 1
def change():
    local_value = value + 1
    return local_value
value = change()
print(value)
```
Explanation: Do not modify globals inside functions; return new values instead.
</details>

---

## Easy

a) Make a function that sets a number and returns it. Print the returned number.

Input example:
```text
None (use code)
```
Output example:
```text
7
```
Starter code:
```python
# Starter
def give_number():
    # TODO: make this function return the number 7
    pass
value = give_number()  # value means the result from the function
print(value)
```
<details><summary>Answer</summary>

```python
def give_number():
    return 7
value = give_number()
print(value)
```
Explanation: Return values make data available outside the function.
</details>

b) Create a function that adds 2 to its input and return the result. Print the result.

Input example:
```text
input_number = 3
```
Output example:
```text
5
```
Starter code:
```python
def add_two(n):
    # n means the number to add to
    # TODO: return n plus 2
    pass
result = add_two(3)  # result means the returned number
print(result)
```
<details><summary>Answer</summary>

```python
def add_two(n):
    return n + 2
result = add_two(3)
print(result)
```
Explanation: The function returns the new number to the caller.
</details>

---

## Medium

a) Inside a function, create a list and return it. Outside, print the list.

Input example:
```text
None
```
Output example:
```text
[1, 2, 3]
```
Starter code:
```python
def make_list():
    # TODO: create a list [1,2,3] and return it
    pass
my_list = make_list()
print(my_list)
```
<details><summary>Answer</summary>

```python
def make_list():
    return [1, 2, 3]
my_list = make_list()
print(my_list)
```
Explanation: Return the list to use it outside the function.
</details>

b) Fix this code so the global `count` is updated by the function (do not use the `global` keyword).

Input example:
```text
count = 0
def add1(c):
    c = c + 1
    return c
count = add1(count)
print(count)
```
Output example:
```text
1
```
Starter code:
```python
count = 0
def add1(c):
    # TODO: return c + 1
    pass
count = add1(count)
print(count)
```
<details><summary>Answer</summary>

```python
count = 0
def add1(c):
    return c + 1
count = add1(count)
print(count)
```
Explanation: Return the new value and assign it to the global variable.
</details>

---

## Hard

Write a function that takes a list and returns a new list with each item increased by 2. Do not change the original list.

Input example:
```text
[1, 2, 3]
```
Output example:
```text
[3, 4, 5]
```
Starter code:
```python
def add_two_to_list(in_list):
    # in_list means the original list
    # TODO: return a new list where each item is in_list item + 2
    pass
original = [1, 2, 3]
new = add_two_to_list(original)
print(new)
print(original)
```
<details><summary>Answer</summary>

```python
def add_two_to_list(in_list):
    result = []
    for item in in_list:
        result.append(item + 2)
    return result
original = [1, 2, 3]
new = add_two_to_list(original)
print(new)
print(original)
```
Explanation: Build a new list to avoid changing the original (no in-place mutation).
</details>
