---
tags: [python, csv]
moc: [[Python - Mini Projects (MOC)]]
difficulty: Beginner
bloom_level: Apply
---

# Python - CSV - Reading Basics

## Concept
Read CSV files safely using `csv.reader` or `csv.DictReader`. On Windows, open files with `newline=''` to avoid extra blank lines.

## Example
```python
import csv
with open('data.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

## Common Errors with Example Code
1) Not using `newline=''` on Windows

WRONG
with open('data.csv', 'r') as f:
    reader = csv.reader(f)  # may give extra blank rows on Windows

CORRECT
with open('data.csv', newline='') as f:
    reader = csv.reader(f)

## MOC
- Parent: [[Python - Mini Projects (MOC)]]
