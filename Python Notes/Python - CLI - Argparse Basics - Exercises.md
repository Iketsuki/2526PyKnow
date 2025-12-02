---
tags: [python, exercises, cli, argparse]
difficulty: Beginner
---

# Python - CLI - Argparse Basics — Exercises

See concept: [[Python - CLI - Argparse Basics]]
GitHub link: [Python - CLI - Argparse Basics](./Python%20-%20CLI%20-%20Argparse%20Basics.md)

## Quick syntax fixes

1) Broken: missing import
```python
# Broken
parser = argparse.ArgumentParser()
```
<details><summary>Answer</summary>

```python
# Fixed
import argparse
parser = argparse.ArgumentParser()
```
Explanation: Import modules before use.
</details>

2) Broken: wrong method name
```python
# Broken
parser = argparse.ArgumentParser()
parser.addArg('--name')
```
<details><summary>Answer</summary>

```python
# Fixed
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name')
```
Explanation: Use `add_argument` to add CLI options.
</details>

3) Broken: forgetting parse_args
```python
# Broken
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name')
print(name)
```
<details><summary>Answer</summary>

```python
# Fixed
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name')
args = parser.parse_args([])
print(args.name)
```
Explanation: Call `parse_args()` to get arguments.
</details>

---

## Easy

a) Make a parser that accepts `--count` and print the parsed value (use `parse_args([])` for examples).

Starter code:
```python
import argparse
parser = argparse.ArgumentParser()
# TODO: add --count as int
args = parser.parse_args([])
print(args.count)
```
<details><summary>Answer</summary>

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--count', type=int, default=0)
args = parser.parse_args([])
print(args.count)
```
Explanation: `add_argument` defines flags; `type=int` makes values integers.
</details>

b) Add a `--name` argument and print a greeting using the parsed value.

Starter code:
```python
import argparse
parser = argparse.ArgumentParser()
# TODO: add --name
args = parser.parse_args([])
print('Hello', args.name)
```
<details><summary>Answer</summary>

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name', default='friend')
args = parser.parse_args([])
print('Hello', args.name)
```
Explanation: Use default so code prints even without CLI input.
</details>

---

## Medium

a) Make a parser that accepts `--repeat N` and prints 'hi' N times.

Starter code:
```python
import argparse
parser = argparse.ArgumentParser()
# TODO: add --repeat as int
args = parser.parse_args([])
for i in range(args.repeat):
    print('hi')
```
<details><summary>Answer</summary>

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--repeat', type=int, default=1)
args = parser.parse_args([])
for i in range(args.repeat):
    print('hi')
```
Explanation: Convert values to int for use in range().
</details>

b) Add a boolean flag `--shout` that, when present, prints greeting in upper-case.

Starter code:
```python
import argparse
parser = argparse.ArgumentParser()
# TODO: add --shout as store_true flag
args = parser.parse_args([])
msg = 'hello'
if args.shout:
    msg = msg.upper()
print(msg)
```
<details><summary>Answer</summary>

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--shout', action='store_true')
args = parser.parse_args([])
msg = 'hello'
if args.shout:
    msg = msg.upper()
print(msg)
```
Explanation: `action='store_true'` makes a boolean flag.
</details>

---

## Hard

Create a parser with a required `--file` parameter. Print the file name or an error message.

Starter code:
```python
import argparse
parser = argparse.ArgumentParser()
# TODO: add required --file
args = parser.parse_args([])
print('file:', args.file)
```
<details><summary>Answer</summary>

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True)
try:
    args = parser.parse_args([])
    print('file:', args.file)
except SystemExit:
    print('error: file is required')
```
Explanation: `required=True` makes an argument mandatory; `parse_args` exits on missing required args.
</details>
