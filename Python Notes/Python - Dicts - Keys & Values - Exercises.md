---
tags: [python, exercises, dicts]
difficulty: Beginner
---

# Exercises — Dicts: Keys & Values

See concept: [[Python - Dicts - Keys & Values]]

GitHub link: [Python - Dicts - Keys & Values](./Python%20-%20Dicts%20-%20Keys%20%26%20Values.md)

### Quick syntax fixes

1) Missing colon between key and value:
```python
d = {'a' 1}
```
<details><summary>Answer</summary>

```python
d = {'a': 1}
```
Explanation: Use `:` between key and value.
</details>

2) Using list instead of dict:
```python
x = ['k','v']
print(x['k'])
```
<details><summary>Answer</summary>

```python
x = {'k': 'v'}
print(x['k'])
```
Explanation: Use `{}` for dicts and square brackets with the key to access.
</details>

3) Key access wrong type:
```python
d = {'a':1}
print(d[a])
```
<details><summary>Answer</summary>

```python
d = {'a':1}
print(d['a'])
```
Explanation: Keys that are strings must be quoted when used as literals.
</details>

---

## Easy

### a) Create a dict from two inputs and print the value

Input example:
```text
color
blue
```

Output example:
```text
blue
```

Starter code:
```python
key_name = input()    # key_name is the key to add
value_text = input()   # value_text is the value for that key
# TODO: create a dictionary with this pair and print the value for key_name
```

<details><summary>Answer</summary>

```python
key_name = input()
value_text = input()
my_dict = {key_name: value_text}
print(my_dict[key_name])
```
Explanation: Create a dict and retrieve the value with the key.
</details>

### b) Print keys of a fixed dict

Output example:
```text
['name', 'age']
```

Starter code:
```python
person = {'name': 'Ana', 'age': '7'}  # person is a sample dictionary
# TODO: print the list of keys
```

<details><summary>Answer</summary>

```python
person = {'name': 'Ana', 'age': '7'}
print(list(person.keys()))
```
Explanation: `keys()` returns the dict keys; `list()` shows them plainly.
</details>

---

## Medium

### a) Read 3 key/value pairs and print dict

Input example:
```text
a
1
b
2
c
3
```

Output example:
```text
{'a': '1', 'b': '2', 'c': '3'}
```

Starter code:
```python
my_dict = {}  # start with empty dictionary
# TODO: read three key/value pairs and store them into my_dict
```

<details><summary>Answer</summary>

```python
my_dict = {}
for _ in range(3):
    k = input()
    v = input()
    my_dict[k] = v
print(my_dict)
```
Explanation: Assign `my_dict[key] = value` for each pair.
</details>

### b) Print number of keys

Input example:
```text
(no input)
```

Output example:
```text
2
```

Starter code:
```python
sample = {'name': 'Ana', 'age': '7'}
# TODO: print number of keys in sample
```

<details><summary>Answer</summary>

```python
sample = {'name': 'Ana', 'age': '7'}
print(len(sample.keys()))
```
Explanation: `len(dict.keys())` gives the count of keys.
</details>

---

## Hard

### Single: Swap two values in a dict

Input example:
```text
apple
banana
```

Output example:
```text
{'a': 'banana', 'b': 'apple'}
```

Starter code:
```python
a = input()  # first value
b = input()  # second value
d = {'a': a, 'b': b}
# TODO: swap the values of keys 'a' and 'b' and print d
```

<details><summary>Answer</summary>

```python
a = input()
b = input()
d = {'a': a, 'b': b}
d['a'], d['b'] = d['b'], d['a']
print(d)
```
Explanation: Use tuple assignment to swap dict values simply.
</details>
