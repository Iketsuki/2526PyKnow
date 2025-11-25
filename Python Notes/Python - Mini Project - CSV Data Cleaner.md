---
tags: [python, project, csv]
moc: [[Python Projects (MOC)]]
difficulty: Beginner
bloom_level: Create
learning_objectives:
  - "Remember: CSV reading/writing basics."
  - "Understand: data cleaning steps (trim, parse, type conversion)."
  - "Apply: build a simple CSV cleaning CLI."
---

# Python - Mini Project - CSV Data Cleaner

## Concept
Small CLI project: read a CSV, normalize headers, trim whitespace, convert numeric columns, and write cleaned CSV.

## Example (skeleton)
```python
import csv

def clean_row(row):
    return {k.strip(): v.strip() for k, v in row.items()}

with open('input.csv', newline='') as inf, open('output.csv', 'w', newline='') as outf:
    reader = csv.DictReader(inf)
    writer = csv.DictWriter(outf, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        writer.writerow(clean_row(row))
```

## Common Errors with Example Code

1) Not opening files with newline='' for CSV → Incorrect row parsing on Windows

WRONG
with open('input.csv', 'r') as f:
    reader = csv.reader(f)

CORRECT
with open('input.csv', newline='') as f:
    reader = csv.reader(f)

2) Not handling missing fields → KeyError when writing

WRONG
writer.writerow(row)  # if keys mismatch, fails

CORRECT
# Ensure consistent fieldnames or use .get() with defaults

3) Assuming everything is a string → Convert numeric fields explicitly

WRONG
value = row['amount']
print(value + 1)  # TypeError if value is '10'

CORRECT
value = int(row['amount'])
print(value + 1)

## Project structure (atomic steps)

Break this project into small, testable tasks (each becomes an atomic note or function):

1. Read CSV safely (newline='' and DictReader) — see a short note: [[Python - CSV - Reading Basics]]
2. Normalize headers (strip, lower) — small helper note
3. Clean rows (type conversions, defaults) — unit-test each helper
4. Write cleaned CSV reliably (DictWriter)
5. Add CLI wrapper (argparse) — small note: [[Python - CLI - Argparse Basics]]

Each step above should be an atomic note with a single responsibility and a `Common Errors` snippet.

## MOC
- Parent: [[Python - Mini Projects (MOC)]]
