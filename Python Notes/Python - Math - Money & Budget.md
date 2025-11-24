---
tags: [python, math, money]
moc: [[Python - Practical Math (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: currency arithmetic and rounding."
  - "Understand: tracking income and expenses."
  - "Apply: build a simple budget or expense tracker."
---

# Python - Math - Money & Budget

## Concept
Track money using simple arithmetic. Store amounts as floats, round to 2 decimals, and sum income/expenses.

## Real-World Examples

**Example 1**: You have $50. You spend $12 on lunch and $8 on a game. How much left?

```python
starting_money = 50.00
lunch_cost = 12.00
game_cost = 8.00
spent = lunch_cost + game_cost
remaining = starting_money - spent
print(f'Spent: ${spent:.2f}')
print(f'Remaining: ${remaining:.2f}')
```

**Example 2**: Track weekly allowance and pocket spending.

```python
# Weekly budget
allowance = 20.00
expenses = [3.50, 5.00, 2.50, 1.99]
total_spent = sum(expenses)
remaining = allowance - total_spent
print(f'Allowance: ${allowance}')
print(f'Spent: ${total_spent:.2f}')
print(f'Saved: ${remaining:.2f}')
```

**Example 3**: Save towards a goal (e.g., $200 gaming console).

```python
goal = 200.00
current_savings = 75.00
monthly_save = 25.00
months_needed = (goal - current_savings) / monthly_save
print(f'You need {months_needed} more months to reach your goal.')
```

## Exercises by Bloom Level
- Remember: Calculate total expenses from a list.
- Understand: Why round money to 2 decimals?
- Apply: Build a simple expense tracker.
- Analyze: Compare saving $10/month vs $15/month over a year.
- Create: Build a budget app that asks income and expenses.

## Tips
- Use `.2f` for clean currency display: `f'${amount:.2f}'`.

## Related Concepts
- [[Python - Math - Calculator Basics]]
- [[Python - Lists - Iteration & Looping]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
