---
tags: [python, exercises, mini-project, csv]
difficulty: Beginner
---

# Python - Mini Project - CSV Data Cleaner — Exercises

See concept: [[Python - Mini Project - CSV Data Cleaner]]
GitHub link: [Python - Mini Project - CSV Data Cleaner](./Python%20-%20Mini%20Project%20-%20CSV%20Data%20Cleaner.md)

## Quick syntax fixes

1) Broken: not closing CSV file
```python
f = open('data.csv')
data = f.read()
```
<details><summary>Answer</summary>

```python
with open('data.csv') as f:
    data = f.read()
```
Explanation: use `with` to ensure file closes.
</details>

2) Broken: splitting on comma but not stripping spaces
```python
line = 'a, b, c'
print(line.split(','))
```
<details><summary>Answer</summary>

```python
line = 'a, b, c'
print([x.strip() for x in line.split(',')])
```
Explanation: strip spaces after split.
</details>

3) Broken: not using `csv` module for quoted fields
```python
line = '"a,b",c'
print(line.split(','))
```
<details><summary>Answer</summary>

```python
import csv
for row in csv.reader(['"a,b",c']):
    print(row)
```
Explanation: `csv.reader` handles quoted commas.
</details>

---

## Easy

a) Read a CSV file with two columns (name, age) and print each name.

Starter code:
```python
import csv
with open('people.csv') as f:
    reader = csv.reader(f)
    # TODO: print names
    pass
```
<details><summary>Answer</summary>

```python
import csv
with open('people.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])
```
Explanation: first column holds the name.
</details>

b) Write cleaned lines to a new file by stripping whitespace.

Starter code:
```python
with open('raw.txt') as fin, open('clean.txt', 'w') as fout:
    for line in fin:
        # TODO: write stripped line
        pass
```
<details><summary>Answer</summary>

```python
with open('raw.txt') as fin, open('clean.txt', 'w') as fout:
    for line in fin:
        fout.write(line.strip() + '\n')
```
Explanation: `.strip()` removes leading/trailing whitespace.
</details>

---

## Medium

a) Use `csv.DictReader` to read a CSV and print `row['email']` for each row.

Starter code:
```python
import csv
with open('data.csv') as f:
    reader = csv.DictReader(f)
    # TODO: print emails
    pass
```
<details><summary>Answer</summary>

```python
import csv
with open('data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['email'])
```
Explanation: `DictReader` gives column names.
</details>

b) Remove empty rows from a CSV and write cleaned file.

Starter code:
```python
import csv
with open('in.csv') as fin, open('out.csv', 'w', newline='') as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    # TODO: skip empty rows
    pass
```
<details><summary>Answer</summary>

```python
import csv
with open('in.csv') as fin, open('out.csv', 'w', newline='') as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    for row in reader:
        if any(cell.strip() for cell in row):
            writer.writerow(row)
```
Explanation: `any(...)` finds non-empty cells.
</details>

---

## Hard

Write a function `clean_csv(infile, outfile)` that lowercases all header names and removes duplicate rows.

Starter code:
```python
import csv

def clean_csv(infile, outfile):
    # TODO: implement cleaning
    pass

clean_csv('in.csv', 'out.csv')
```
<details><summary>Answer</summary>

```python
import csv

def clean_csv(infile, outfile):
    seen = set()
    with open(infile) as fin, open(outfile, 'w', newline='') as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout)
        headers = next(reader)
        writer.writerow([h.lower() for h in headers])
        for row in reader:
            key = tuple(row)
            if key not in seen:
                seen.add(key)
                writer.writerow(row)

clean_csv('in.csv', 'out.csv')
```
Explanation: use a set to filter duplicates and lower headers.
</details>
