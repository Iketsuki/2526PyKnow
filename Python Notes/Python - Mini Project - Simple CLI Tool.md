---
tags: [python, project, cli]
moc: [[Python Projects (MOC)]]
difficulty: Beginner
bloom_level: Create
learning_objectives:
  - "Remember: argparse basics."
  - "Understand: how to structure a CLI program."
  - "Apply: build a small command-line utility."
---

# Python - Mini Project - Simple CLI Tool

## Concept
Create a small CLI that accepts arguments, performs an action, and prints results. Use `argparse` for argument parsing.

## Example
```python
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='Friend')
    args = parser.parse_args()
    print(f'Hello, {args.name}!')

if __name__ == '__main__':
    main()
```

## Common Errors with Example Code

1) Parsing sys.argv manually instead of using argparse → fragile code

WRONG
import sys
name = sys.argv[1]

CORRECT
import argparse
parser = argparse.ArgumentParser()

2) Not providing helpful --help messages → poor UX

WRONG
parser.add_argument('--name')

CORRECT
parser.add_argument('--name', help='Your display name', default='Friend')

3) Not returning sensible exit codes

WRONG
# Always returns 0 even on failure

CORRECT
import sys
if error:
    sys.exit(1)

## Project steps (atomic)

Break the CLI project into atomic tasks:

1. Argument parsing basics (`argparse`) — small note: [[Python - CLI - Argparse Basics]]
2. Validation and error exit codes — tiny note with examples
3. Help and usage text — one-line note
4. Add subcommands (argparse subparsers) — separate note

Each atomic task should have its own example and a short `Common Errors with Example Code` section.

## MOC
- Parent: [[Python - Mini Projects (MOC)]]
