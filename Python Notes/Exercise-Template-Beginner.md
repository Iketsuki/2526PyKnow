---
tags: [python, exercises, template]
difficulty: Beginner
---

# Exercise File Template — Beginner (Use as copy for new exercise files)

Purpose: Copy this file and replace the placeholders to create a new exercise file that matches the project's format.

See concept: [[REPLACE_WITH_CONCEPT_FILENAME]]  # e.g. [[Python - Lists - Creation & Initialization]]
GitHub link: [REPLACE_WITH_CONCEPT_FILENAME](./REPLACE_WITH_CONCEPT_FILENAME.md)  # e.g. [Python - Lists - Creation & Initialization](./Python%20-%20Lists%20-%20Creation%20%26%20Initialization.md)

Notes for authors (short):
- Use clear, full variable names in starter code. Avoid short forms like `fn` — use `filename` and add a short inline comment, e.g. `filename = input()  # filename means the file name to open`.
- For GitHub compatibility: include both the wiki-style link `[[Note Name]]` and a relative link that uses URL-encoding for special characters (spaces -> `%20`, `&` -> `%26`). Example:
	- `See concept: [[Python - Lists - Creation & Initialization]]`
	- `GitHub link: [Python - Lists - Creation & Initialization](./Python%20-%20Lists%20-%20Creation%20%26%20Initialization.md)`
- Keep language simple and sentences short (suitable for young ESL learners).
- Each exercise file must include: 3 quick syntax-fix problems, Easy a/b, Medium a/b, Hard single. Each problem must include two separate code blocks: Input example and Output example, a starter code block with `# TODO`, and an answer inside a hidden toggle (`<details><summary>Answer</summary>...</details>`). Add a concise or even one-line explanation after the answer.
- Do not require advanced functions or concepts in the blanks. Starter code can use simple `# TODO` comments for the student. Avoid requiring list comprehensions, lambda, generator expressions, or advanced parameters in starter blanks unless the concept page explicitly teaches them. Answers may show a clear, simple solution; prefer explicit loops and simple statements so learners can follow.

---

## Header metadata
- `tags`: keep `python, exercises` plus topic tag
- `difficulty`: Beginner

---

## Quick syntax fixes

1) Short description of the syntax problem (one-line).  Show the broken code in a fenced python block.
```python
# Broken example (student sees this)
print'Hello'
```
<details><summary>Answer</summary>

```python
# Fixed example (author writes full working code)
print('Hello')
```
Explanation: Use parentheses for `print` in Python 3.
</details>

2) Another small syntax fix
```python
# Broken example
name = input
print(name)
```
<details><summary>Answer</summary>

```python
# Fixed
name = input()
print(name)
```
Explanation: `input()` must be called with parentheses and its result stored.
</details>

3) Third small syntax fix
```python
# Broken example
items = [1 2 3]
```
<details><summary>Answer</summary>

```python
# Fixed
items = [1, 2, 3]
```
Explanation: Use commas between list items.
</details>

---

## Easy

### a) Short title (one line)

Input example:
```text
# Input block (plain text) — show exact inputs the student would type
alice
7
```

Output example:
```text
# Output block (plain text) — show expected printed output
Name: alice, Age: 7
```

Starter code:
```python
name = input()  # name means the person's name
age = input()   # age means the person's age (string is fine)
# TODO: print the text exactly as the output example
```

<details><summary>Answer</summary>

```python
name = input()
age = input()
print('Name:', name + ',', 'Age:', age)
```
Explanation: Use `print` with commas to match spacing and punctuation.
</details>

### b) Short title (one line)

Input example:
```text
3
4
5
```

Output example:
```text
3-4-5
```

Starter code:
```python
first_number = input()   # first_number is the first value
second_number = input()  # second_number is the second value
third_number = input()   # third_number is the third value
# TODO: print these three numbers with '-' between them
```

<details><summary>Answer</summary>

```python
first_number = input()
second_number = input()
third_number = input()
print(first_number, second_number, third_number, sep='-')
```
Explanation: `print(..., sep='-')` sets the separator to a dash.
</details>

---

## Medium

### a) Short title

Input example:
```text
Tom
10
```

Output example:
```text
Hello Tom! You are 10 years old.
```

Starter code:
```python
name = input()   # name means the learner's name
age = input()    # age means the learner's age
# TODO: print the greeting exactly like the output example
```

<details><summary>Answer</summary>

```python
name = input()
age = input()
print(f'Hello {name}! You are {age} years old.')
```
Explanation: Use an f-string for clear insertion of variables.
</details>

### b) Short title

Input example:
```text
apple
banana
cherry
```

Output example:
```text
apple, banana, cherry
```

Starter code:
```python
item1 = input()  # item1 is the first word
item2 = input()  # item2 is the second word
item3 = input()  # item3 is the third word
# TODO: print items on one line separated by comma and space
```

<details><summary>Answer</summary>

```python
item1 = input()
item2 = input()
item3 = input()
print(item1, item2, item3, sep=', ')
```
Explanation: Use `sep=', '` to place a comma and space between items.
</details>

---

## Hard

### Single: Short title

Input example:
```text
Day
Sunny
25
```

Output example:
```text
Day | Sunny | 25°C
```

Starter code:
```python
label = input()    # label means the first word to show
weather = input()  # weather means weather word (Sunny/Cloudy)
temperature = input()  # temperature as string (e.g. '25')
# TODO: format and print exactly like the output example
```

<details><summary>Answer</summary>

```python
label = input()
weather = input()
temperature = input()
print(label, '|', weather, '|', temperature + '°C')
```
Explanation: Concatenate the degree symbol and use `print` separators.
</details>

---

## Authoring checklist (copy into new exercise file and fill fields):
- Replace the `See concept` link with the exact note file name in double brackets.
- Update the file front-matter tags if needed.
- Verify all starter code variables use full names and include short inline `# comments` explaining them (for children).
- Keep hidden answers inside `<details>` toggles and include a 1-2 sentence explanation below each answer.
- Confirm no advanced constructs are required to complete the blanks (no list comprehensions, no lambda, no args/kwargs) unless the concept file explicitly teaches them.

---

End of template. Copy this file and edit its content when creating new exercise pages.
