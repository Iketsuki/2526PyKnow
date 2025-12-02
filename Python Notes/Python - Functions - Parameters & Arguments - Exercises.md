---
tags: [python, exercises, functions]
difficulty: Beginner
---

# Exercises — Functions: Parameters & Arguments

See concept: [[Python - Functions - Parameters & Arguments]]

### Quick syntax fixes

1) Missing parameter name:
```python
def f():
    return x
```
<details><summary>Answer</summary>

```python
def f(x):
    return x
```
Explanation: Define `x` as a parameter if you use it inside.
</details>

2) Wrong call with two args for one param:
```python
def f(x):
    return x
print(f(1,2))
```
<details><summary>Answer</summary>

```python
def f(x, y):
    return x + y
print(f(1,2))
```
Explanation: Either change function or call to match parameters.
</details>

3) Default argument spacing:
```python
def greet(name='Friend'):
print('Hi', name)
```
<details><summary>Answer</summary>

```python
def greet(name='Friend'):
    print('Hi', name)
```
Explanation: Indent the function body.
</details>

---

## Easy

### a) Function that prints a number plus one

Input example:
```text
4
```

Output example:
```text
5
```

Starter code:
```python
n = int(input())
# TODO: write inc(x) that returns x+1 and print inc(n)
```

<details><summary>Answer</summary>

```python
def inc(x):
    return x + 1

n = int(input())
print(inc(n))
```
Explanation: Parameters let functions use outside values.
</details>

### b) Function with two args that prints them

Input example:
```text
Hello
World
```

Output example:
```text
Hello World
```

Starter code:
```python
a = input()
b = input()
# TODO: write show(x,y) that prints x and y with a space
```

<details><summary>Answer</summary>

```python
def show(x, y):
    print(x, y)

a = input()
b = input()
show(a, b)
```
Explanation: Pass both inputs as arguments to the function.
</details>

---

## Medium

### a) Function with default value

Input example:
```text
(no input, assume use default)
```

Output example:
```text
Hello Friend
```

Starter code:
```python
# TODO: write greet(name='Friend') that prints 'Hello <name>' and call with no args
```

<details><summary>Answer</summary>

```python
def greet(name='Friend'):
    print('Hello', name)

greet()
```
Explanation: Default parameter used when no argument is passed.
</details>

### b) Swap two numbers using a function

Input example:
```text
3
7
```

Output example:
```text
7 3
```

Starter code:
```python
a = input()
b = input()
# TODO: write swap(x,y) that returns y,x then print the swapped values
```

<details><summary>Answer</summary>

```python
def swap(x, y):
    return y, x

a = input()
b = input()
na, nb = swap(a, b)
print(na, nb)
```
Explanation: Functions can return multiple values as a tuple.
</details>

---

## Hard

### Single: Function that repeats a word n times separated by commas

Input example:
```text
hi
3
```

Output example:
```text
hi,hi,hi
```

Starter code:
```python
word = input()
n = int(input())
# TODO: write repeat(word, n) to return the repeated string, then print it
```

<details><summary>Answer</summary>

```python
def repeat(word, n):
    return ','.join([word]*n)

word = input()
n = int(input())
print(repeat(word, n))
```
Explanation: Use list multiplication and `join` to build the string.
</details>
