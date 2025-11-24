---
tags: [python, math, calculator]
moc: [[Python - Practical Math (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: basic arithmetic operations (+, -, *, /, //, %)."
  - "Understand: order of operations (PEMDAS)."
  - "Apply: build a simple calculator."
---

# Python - Math - Calculator Basics

## Concept
Use `+`, `-`, `*`, `/` for basic math. `/` gives decimals; `//` gives whole numbers. `%` gives remainder (useful for checking if even/odd).

## Real-World Example
**Scenario**: You buy 3 energy drinks at $2.50 each. How much do you spend?

```python
price_per_drink = 2.50
num_drinks = 3
total = price_per_drink * num_drinks
print(f'You spent: ${total}')

# With tax (8%)
tax = total * 0.08
final_cost = total + tax
print(f'With tax: ${final_cost:.2f}')
```

## Exercises by Bloom Level
- Remember: What does `//` do?
- Understand: Why use `*` for repeated addition?
- Apply: Calculate total cost of 5 items at $7.99 each.
- Analyze: How to round to 2 decimal places for currency?
- Create: Build a calculator for multiple items with tax.

## Common Errors with Example Code

1) Using `/` instead of `//` when you need whole numbers

WRONG
```python
cookies = 7
kids = 2
per_kid = cookies / kids
print(per_kid)  # 3.5
# But you might want whole cookies: 3
```

CORRECT
```python
cookies = 7
kids = 2
per_kid = cookies // kids  # 3
print(f'Each kid gets {per_kid} cookies')
```

2) Not handling division by zero in calculations

WRONG
```python
total = 50
num_people = 0
per_person = total / num_people  # ZeroDivisionError
```

CORRECT
```python
total = 50
num_people = 0
if num_people > 0:
    per_person = total / num_people
    print(f'Per person: ${per_person:.2f}')
else:
    print('Need at least 1 person')
```

3) Forgetting to round money values

WRONG
```python
item1 = 10.99
item2 = 15.50
item3 = 23.51
total = item1 + item2 + item3
print(total)  # May have floating-point error
```

CORRECT
```python
item1 = 10.99
item2 = 15.50
item3 = 23.51
total = item1 + item2 + item3
total = round(total, 2)
print(f'Total: ${total:.2f}')
```

## Related Concepts
- [[Python - Variables - Types Basics]]
- [[Python - Math - Money & Budget]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
