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

## What is an If Statement?

An **if statement** makes your program choose what to do.

```python
age = 15
if age > 18:
    print('You can vote')
```

## How It Works

Think of a real-world rule:
- **IF** it is raining, **THEN** bring an umbrella.
- In Python: `IF` condition is true, `THEN` run the code.

```python
score = 85
if score > 80:
    print('Good job!')
```

## If-Else (Two Choices)

**If-else** gives two options:

```python
age = 15
if age >= 18:
    print('You are an adult')
else:
    print('You are a teenager')
```

"If the age is 18 or more, print first message. Otherwise, print second message."

## If-Elif-Else (Many Choices)

**Elif** = "else if". Use it for multiple choices:

```python
age = 15
if age < 13:
    print('You are a child')
elif age < 18:
    print('You are a teenager')
else:
    print('You are an adult')
```

Python checks each condition in order:
1. Is age less than 13? No.
2. Is age less than 18? Yes! Print "teenager" and stop.

## Real-World Examples

**Grade Check**
```python
score = 87
if score >= 90:
    print('A: Excellent!')
elif score >= 80:
    print('B: Good job!')
elif score >= 70:
    print('C: Okay')
else:
    print('F: Try again')
```

**Game Status**
```python
health = 50
if health == 0:
    print('Game over!')
elif health < 30:
    print('Low health!')
else:
    print('You are healthy')
```

**Discount Decision**
```python
age = 65
if age < 12:
    print('Kid ticket - $5')
elif age >= 65:
    print('Senior ticket - $8')
else:
    print('Adult ticket - $12')
```

## Exercises by Bloom Level

- **Remember:** Write an if statement that checks a number.
- **Understand:** What is the difference between if and elif?
- **Apply:** Check if a number is even or odd.
- **Create:** Make a program that chooses a greeting based on the time of day.

## Common Errors with Example Code

1) Using `=` instead of `==` (assignment vs comparison)

WRONG
```python
age = 15
if age = 18:  # Error!
    print('Adult')
```

CORRECT
```python
age = 15
if age == 18:  # Use == to compare
    print('Adult')
```

2) Forgetting the colon `:`

WRONG
```python
age = 15
if age > 18
    print('Adult')  # Error!
```

CORRECT
```python
age = 15
if age > 18:  # Colon here!
    print('Adult')
```

3) Indentation (spacing) error

WRONG
```python
age = 15
if age > 18:
print('Adult')  # Should be indented
```

CORRECT
```python
age = 15
if age > 18:
    print('Adult')  # Indented with spaces
```

## Tips
- Use **`==`** to compare (not `=`)
- Always add **`:`** after if/elif/else
- **Indent** the code inside the if block
- **Elif** tests another condition
- **Else** is the fallback (runs if all others are false)

## Related Concepts
- [[Python - Conditionals - Comparison Operators]]
- [[Python - Conditionals - Boolean Logic (and-or-not)]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]
