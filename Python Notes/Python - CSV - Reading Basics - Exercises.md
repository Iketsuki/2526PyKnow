---
tags: [python, exercises, csv]
difficulty: Beginner
---

# Exercises — CSV: Reading Basics

See concept: [[Python - CSV - Reading Basics]]

GitHub link: [Python - CSV - Reading Basics](./Python%20-%20CSV%20-%20Reading%20Basics.md)

### Quick syntax fixes

1) Splitting a line without calling strip:
```python
line = 'a,b,c\n'
print(line.split(','))
```
<details><summary>Answer</summary>

```python
line = 'a,b,c\n'
print(line.strip().split(','))
```
Explanation: `strip()` removes newline before splitting.
</details>

2) Using csv.reader but forgetting to import csv:
```python
with open('data.csv') as f:
    reader = csv.reader(f)
```
<details><summary>Answer</summary>

```python
import csv
with open('data.csv') as f:
    reader = csv.reader(f)
```
Explanation: Import the `csv` module before using it.
</details>

3) Reading whole file as one string then splitting lines incorrectly:
```python
text = open('a.csv').read()
rows = text.split(',')
```
<details><summary>Answer</summary>

```python
text = open('a.csv').read()
rows = text.splitlines()
```
Explanation: Use `splitlines()` to get lines; use `split(',')` for items on a line.
</details>

---

## Easy

### a) Read filename and print first CSV cell

Input example:
```text
sample.csv
```

Suppose `sample.csv` first line: `name,age` and second line: `Ana,7`

Output example:
```text
name
```

Starter code:
```python
filename = input()  # filename is the CSV file name
# TODO: open filename, read first line, split by comma and print first cell
```

<details><summary>Answer</summary>

```python
filename = input()
with open(filename) as f:
    first_line = f.readline().strip()
    cells = first_line.split(',')
print(cells[0])
```
Explanation: Read one line, strip newline, split by comma, access index 0.
</details>

### b) Count rows in a CSV file

Input example:
```text
data.csv
```

Output example:
```text
3
```

Starter code:
```python
filename = input()
# TODO: count how many non-empty lines are in the CSV file and print the count
```

<details><summary>Answer</summary>

```python
filename = input()
count = 0
with open(filename) as f:
    for line in f:
        if line.strip():
            count += 1
print(count)
```
Explanation: Skip empty lines using `strip()` and count real rows.
</details>

---

## Medium

### a) Print second column for each row

Input example:
```text
data.csv
```

Suppose rows:
```
name,age
Ana,7
Tom,10
```

Output example:
```text
age
7
10
```

Starter code:
```python
filename = input()
# TODO: read each non-empty line, split by ',', and print the second cell
```

<details><summary>Answer</summary>

```python
filename = input()
with open(filename) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        cells = line.split(',')
        if len(cells) >= 2:
            print(cells[1])
```
Explanation: Check line length and cell count before printing the second column.
</details>

### b) Sum numbers in second column (skip header)

Input example:
```text
scores.csv
```

Suppose file rows:
```
name,score
A,5
B,7
```

Output example:
```text
12
```

Starter code:
```python
filename = input()
# TODO: skip the header, read numeric second column and print their sum
```

<details><summary>Answer</summary>

```python
filename = input()
total = 0
with open(filename) as f:
    header = f.readline()
    for line in f:
        line = line.strip()
        if not line:
            continue
        cells = line.split(',')
        total += int(cells[1])
print(total)
```
Explanation: Read and ignore header, convert column cell to int, and accumulate.
</details>

---

## Hard

### Single: Read CSV and build list of dicts (simple)

Input example:
```text
people.csv
```

Suppose `people.csv` contains:
```
name,age
Ana,7
Tom,10
```

Output example:
```text
[{'name': 'Ana', 'age': '7'}, {'name': 'Tom', 'age': '10'}]
```

Starter code:
```python
filename = input()
# TODO: read file, use header row as keys and build a list of dicts for each row
```

<details><summary>Answer</summary>

```python
filename = input()
rows = []
with open(filename) as f:
    header = f.readline().strip().split(',')
    for line in f:
        line = line.strip()
        if not line:
            continue
        cells = line.split(',')
        d = {}
        for i in range(len(header)):
            d[header[i]] = cells[i]
        rows.append(d)
print(rows)
```
Explanation: Use the header row to map each cell into a dict for that row; simple index loop keeps it explicit for beginners.
</details>
