---
tags: [python, data-structures]
moc: [[Python - Data Structures (MOC)]]
difficulty: Beginner
bloom_level: Analyze
learning_objectives:
  - "Remember: differences between lists and dicts."
  - "Understand: when to choose one over the other."
  - "Apply: select the appropriate structure for tasks."
---

# Python - Data Structures - When to use lists vs dicts

## Concept
Short guide to choosing between lists and dictionaries. Lists are ordered sequences, ideal for indexed collections and simple iterations. Dicts are key-value mappings, ideal for fast lookups by key.

## Example
```python
# Use list when order matters or you have duplicates
names = ['Alice', 'Bob', 'Alice']
print(names[1])  # Bob

# Use dict for lookup by key
scores = {'Alice': 90, 'Bob': 75}
print(scores['Alice'])  # 90
```

## Common Errors with Example Code

1) Using list for fast lookup → O(n) search vs O(1) dict lookup

WRONG
names = ['alice', 'bob', 'charlie']
if 'bob' in names:
    print('found')  # O(n) scan each time

CORRECT
scores = {'alice': 1, 'bob': 2, 'charlie': 3}
if 'bob' in scores:
    print('found')  # O(1) hash lookup

2) Using dict when order matters (older Python versions) → rely on order only when needed

WRONG
# Relying on insertion order (pre-3.7) can be surprising
# Use list if you need positional access

CORRECT
# Use list for positional access and dict for keyed access

3) Using mutable types as dict keys → TypeError

WRONG
my_dict = {[1,2]: 'value'}  # TypeError: unhashable type: 'list'

CORRECT
my_dict = {(1,2): 'value'}  # use tuple as key

## Related Concepts
- [[Python - Lists - Common Patterns]]
- [[Python - Dicts - Creation & Initialization]]

## Atomic breakdown

This decision guide is intentionally short. If you want to dig deeper, read these focused notes:

- [[Python - Lists - Creation & Initialization]] — list basics and when to use them
- [[Python - Dicts - Accessing Values]] — dict lookup, .get(), and safe patterns

## MOC
- Parent: [[Python - Data Structures (MOC)]]
