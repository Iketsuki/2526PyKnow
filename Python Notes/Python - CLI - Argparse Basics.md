---
tags: [python, cli, argparse]
moc: [[Python - Mini Projects (MOC)]]
difficulty: Beginner
bloom_level: Apply
---

# Python - CLI - Argparse Basics

## Concept
`argparse` parses command-line arguments. Keep each CLI task atomic: parse args, validate, run action, return exit code.

## Example
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', default='Friend', help='Your display name')
args = parser.parse_args()
print(f'Hello {args.name}')
```

## Common Errors
1) Failing to provide useful help text

WRONG
parser.add_argument('--name')

CORRECT
parser.add_argument('--name', help='Your display name', default='Friend')

2) Not handling required arguments

WRONG
parser.add_argument('--path')  # forget to require

CORRECT
parser.add_argument('--path', required=True)

## MOC
- Parent: [[Python - Mini Projects (MOC)]]
