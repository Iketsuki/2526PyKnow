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

## Common Errors
- Integer division `5 // 2` gives `2` (not `2.5`).

## Related Concepts
- [[Python - Variables - Types Basics]]
- [[Python - Math - Money & Budget]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
