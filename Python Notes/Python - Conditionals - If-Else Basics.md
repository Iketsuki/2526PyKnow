---
tags: [python, conditionals, if-else]
moc: [[Python - Conditionals (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `if`/`elif`/`else` syntax."
  - "Understand: how conditions branch execution."
  - "Apply: write conditional statements."
---

# Python - Conditionals - If-Else Basics

## Concept
`if` runs code if a condition is true. `elif` tests another condition. `else` runs if all previous conditions are false.

## Example Code
```python
age = 15
if age < 13:
    print('Child')
elif age < 18:
    print('Teenager')
else:
    print('Adult')
```

## Exercises by Bloom Level
- Remember: Write an `if` statement.
- Understand: What does `elif` mean?
- Apply: Check if a number is positive, negative, or zero.
- Analyze: Simplify nested if-else chains.
- Create: Build a decision tree program.

## Common Errors with Example Code

1) Using `=` instead of `==` in conditions (assignment vs comparison)

WRONG
```python
age = 15
if age = 18:  # SyntaxError: invalid syntax
    print('Adult')
```

CORRECT
```python
age = 15
if age == 18:  # Use == for comparison
    print('Adult')
else:
    print('Not 18')
```

2) Forgetting colon at the end of if/elif/else (SyntaxError)

WRONG
```python
age = 15
if age > 18
    print('Adult')
```

CORRECT
```python
age = 15
if age > 18:
    print('Adult')
elif age < 13:
    print('Child')
else:
    print('Teenager')
```

3) Indentation errors (wrong scope)

WRONG
```python
age = 15
if age > 18:
print('Adult')  # Not indented!
```

CORRECT
```python
age = 15
if age > 18:
    print('Adult')  # Indented properly
else:
    print('Teenager')
```

Short tips:
- Use `==` for comparison, `=` for assignment.
- Always end if/elif/else with a colon.
- Indent the code block after the colon (usually 4 spaces).

## Related Concepts
- [[Python - Conditionals - Boolean Logic (and-or-not)]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]
