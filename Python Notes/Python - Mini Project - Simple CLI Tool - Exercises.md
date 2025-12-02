---
tags: [python, exercises, mini-project, cli]
difficulty: Beginner
---

# Python - Mini Project - Simple CLI Tool — Exercises

See concept: [[Python - Mini Project - Simple CLI Tool]]
GitHub link: [Python - Mini Project - Simple CLI Tool](./Python%20-%20Mini%20Project%20-%20Simple%20CLI%20Tool.md)

## Quick syntax fixes

1) Broken: reading `sys.argv` without importing `sys`
```python
print(sys.argv)
```
<details><summary>Answer</summary>

```python
import sys
print(sys.argv)
```
Explanation: import modules before use.
</details>

2) Broken: naive parsing of flags
```python
if '-v' in argv:
    verbose = True
```
<details><summary>Answer</summary>

```python
import sys
if '-v' in sys.argv:
    verbose = True
```
Explanation: use `sys.argv` or `argparse` for flags.
</details>

3) Broken: printing help without exit
```python
print('help')
# continue running
```
<details><summary>Answer</summary>

```python
print('help')
import sys
sys.exit(0)
```
Explanation: exit after showing help to avoid running main code.
</details>

---

## Easy

a) Write a script that prints `Hello` and the first command-line argument.

Starter code:
```python
import sys
# TODO: print greeting and first arg
pass
```
<details><summary>Answer</summary>

```python
import sys
if len(sys.argv) > 1:
    print('Hello', sys.argv[1])
else:
    print('Hello')
```
Explanation: check length before accessing `sys.argv[1]`.
</details>

b) Use `argparse` to accept `--name` and print `Hello <name>`.

Starter code:
```python
import argparse
parser = argparse.ArgumentParser()
# TODO: add --name and parse
pass
```
<details><summary>Answer</summary>

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name')
args = parser.parse_args()
print('Hello', args.name)
```
Explanation: `add_argument` creates CLI flags.
</details>

---

## Medium

a) Make a CLI that accepts `--count N` and prints `Hello` N times.

Starter code:
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--count', type=int, default=1)
args = parser.parse_args()
# TODO: print Hello args.count times
pass
```
<details><summary>Answer</summary>

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--count', type=int, default=1)
args = parser.parse_args()
for _ in range(args.count):
    print('Hello')
```
Explanation: loop using the parsed integer.
</details>

b) Add a `--verbose` flag that prints extra text when set.

Starter code:
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()
# TODO: print extra text if args.verbose
pass
```
<details><summary>Answer</summary>

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()
if args.verbose:
    print('Verbose mode on')
```
Explanation: `store_true` makes a boolean flag.
</details>

---

## Hard

Create a small CLI tool skeleton that has subcommands `clean` and `run` (use `argparse` subparsers).

Starter code:
```python
import argparse
parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest='command')
# TODO: add 'clean' and 'run' subparsers
args = parser.parse_args()
print(args)
```
<details><summary>Answer</summary>

```python
import argparse
parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest='command')
sub.add_parser('clean')
sub.add_parser('run')
args = parser.parse_args()
print(args)
```
Explanation: subparsers allow simple subcommands.
</details>
