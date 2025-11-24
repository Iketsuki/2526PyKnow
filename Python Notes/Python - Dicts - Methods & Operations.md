---
tags: [python, dicts, methods]
moc: [[Python - Dicts (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: common dict methods."
  - "Understand: .get(), .keys(), .values(), .items()."
  - "Apply: modify and iterate dicts safely."
---

# Python - Dicts - Methods & Operations

## Concept
**Dict methods** — Built-in operations: `.get()` (safe access), `.keys()` (get keys), `.values()` (get values), `.items()` (get pairs), `.update()` (merge dicts).

## Safe Access with .get()

```python
# Dangerous: KeyError if missing
student = {'name': 'Alice', 'age': 14}
print(student['grade'])  # KeyError!

# Safe: .get() returns None if missing
print(student.get('grade'))  # None
print(student.get('grade', 'N/A'))  # N/A (default)

# Real usage
score = data.get('score', 0)  # Default 0 if missing
```

## Extract Keys, Values, Items

```python
student = {'name': 'Alice', 'age': 14, 'grade': 'A'}

# Get all keys
keys = student.keys()
print(list(keys))  # ['name', 'age', 'grade']

# Get all values
values = student.values()
print(list(values))  # ['Alice', 14, 'A']

# Get key-value pairs
items = student.items()
print(list(items))  # [('name', 'Alice'), ('age', 14), ('grade', 'A')]

# Iterate over pairs
for key, value in student.items():
    print(f'{key}: {value}')
```

## Modify Dictionary

```python
student = {'name': 'Alice', 'age': 14}

# Add key-value
student['grade'] = 'A'
print(student)  # {'name': 'Alice', 'age': 14, 'grade': 'A'}

# Update multiple values
student.update({'age': 15, 'school': 'Central High'})
print(student)  # {..., 'age': 15, 'school': 'Central High'}

# Delete key
del student['age']
print(student)  # {'name': 'Alice', 'grade': 'A', 'school': 'Central High'}

# .pop() - delete and return value
grade = student.pop('grade')  # Returns 'A'
print(grade)  # A
print('grade' in student)  # False
```

## Increment Values

```python
votes = {'Alice': 5, 'Bob': 3}

# Increment
votes['Alice'] += 1
print(votes)  # {'Alice': 6, 'Bob': 3}

# Safe increment (if key doesn't exist)
votes['Charlie'] = votes.get('Charlie', 0) + 1
print(votes)  # {..., 'Charlie': 1}
```

## Count Occurrences

```python
# Count letters in word
word = 'hello'
letter_count = {}

for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1

print(letter_count)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Cleaner: use dict.fromkeys() to initialize
color_votes = {'red': 0, 'blue': 0, 'green': 0}
votes = ['red', 'blue', 'red', 'green']

for vote in votes:
    color_votes[vote] += 1

print(color_votes)  # {'red': 2, 'blue': 1, 'green': 1}
```

## Check Existence

```python
student = {'name': 'Alice', 'age': 14}

# Check key exists
if 'name' in student:
    print('Name is in dict')

# Check key doesn't exist
if 'grade' not in student:
    print('Grade is missing')

# .get() with default for checking
score = student.get('score', 0)
if score == 0:
    print('No score recorded')
```

## Clear and Copy

```python
# Create copy (important!)
original = {'name': 'Alice', 'score': 95}
copy = original.copy()
copy['score'] = 100

print(original['score'])  # 95 (unchanged)
print(copy['score'])  # 100 (changed only in copy)

# Clear dictionary
data = {'a': 1, 'b': 2}
data.clear()
print(data)  # {}
```

## Real-World: Grade Book

```python
grades = {
    'Alice': [85, 90, 88],
    'Bob': [92, 88, 95],
    'Charlie': [78, 82, 80]
}

# Calculate averages
averages = {}
for student, scores in grades.items():
    avg = sum(scores) / len(scores)
    averages[student] = round(avg, 2)

print(averages)
# {'Alice': 87.67, 'Bob': 91.67, 'Charlie': 80.0}

# Find best student
best_student = max(averages, key=averages.get)
print(f'Top student: {best_student}')  # Bob
```

## Real-World: Frequency Counter

```python
def count_letters(text):
    '''Count each letter frequency (case-insensitive)'''
    text = text.lower()
    counts = {}
    
    for letter in text:
        if letter.isalpha():  # Only letters
            counts[letter] = counts.get(letter, 0) + 1
    
    return counts

result = count_letters('Hello World')
print(result)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# Most common letter
most_common = max(result, key=result.get)
print(f'Most common: {most_common}')  # l
```

## Real-World: Merge Scores

```python
# Two players' scores from different games
alice_scores = {'game1': 85, 'game2': 90}
bob_scores = {'game2': 88, 'game3': 92}

# Combine scores
all_scores = {}
all_scores.update(alice_scores)
all_scores.update(bob_scores)
print(all_scores)  # {'game1': 85, 'game2': 88, 'game3': 92}

# All games where both played
shared_games = set(alice_scores.keys()) & set(bob_scores.keys())
print(shared_games)  # {'game2'}

# Who scored better in game2?
if alice_scores.get('game2', 0) > bob_scores.get('game2', 0):
    print('Alice better in game2')
else:
    print('Bob better in game2')
```

## Common Methods Reference

```python
# Access (safe)
dict.get(key, default=None)  # Safe access
key in dict  # Check existence

# Retrieve
dict.keys()  # All keys
dict.values()  # All values
dict.items()  # Key-value pairs

# Modify
dict[key] = value  # Add/update
dict.update(other)  # Merge dicts
dict.pop(key)  # Remove and return
del dict[key]  # Remove

# Clean
dict.clear()  # Delete all
dict.copy()  # Shallow copy
```

## Exercises by Bloom Level
- Remember: What does `.get()` do?
- Understand: When would you use `.items()` vs `.keys()`?
- Apply: Count letter frequencies in a string.
- Analyze: Compare `.pop()` vs `del`.
- Create: Build frequency analyzer for any text.

## Common Errors with Example Code

1) Using `dict[key]` without checking → KeyError if missing (use `.get()`)

WRONG
student = {'name': 'Alice', 'age': 14}
grade = student['grade']  # KeyError if missing!

CORRECT
student = {'name': 'Alice', 'age': 14}
grade = student.get('grade', 'N/A')  # Safely returns default

2) Forgetting `.copy()` when copying → Modifies original dict

WRONG
original = {'name': 'Alice', 'score': 95}
copy = original  # This is a reference, not a copy!
copy['score'] = 100
print(original['score'])  # 100 (oops, modified original!)

CORRECT
original = {'name': 'Alice', 'score': 95}
copy = original.copy()  # True copy
copy['score'] = 100
print(original['score'])  # 95 (original unchanged)

3) Iterating incorrectly → `.items()` for key-value pairs

WRONG
student = {'name': 'Alice', 'age': 14}
for key in student:
    print(student[key])  # Works but looks up key each time

CORRECT
student = {'name': 'Alice', 'age': 14}
for key, value in student.items():
    print(f'{key}: {value}')  # Direct access, more efficient

## Related Concepts
- [[Python - Dicts - Creation & Initialization]]
- [[Python - Dicts - Iteration]]
- [[Python - Dicts - Keys & Values]]
- [[Python - Variables & Types - Built-in Functions]]

## MOC
- Parent: [[Python - Dicts (MOC)]]
