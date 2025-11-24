---
tags: [python, math, percentages]
moc: [[Python - Practical Math (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: percentage formula (part = whole × percent/100)."
  - "Understand: real-world discount and increase scenarios."
  - "Apply: calculate discounts and tips."
---

# Python - Math - Percentages & Discounts

## Concept
Percentage = (part / whole) × 100. To find 20% of 50: `50 * 0.20`. To apply a discount: `price * (1 - discount_rate)`.

## Real-World Examples

**Example 1**: Store has 30% off a $60 hoodie. What's the sale price?

```python
original_price = 60
discount_percent = 30
discount_amount = original_price * (discount_percent / 100)
sale_price = original_price - discount_amount
print(f'Original: ${original_price}')
print(f'Discount: ${discount_amount}')
print(f'Sale price: ${sale_price}')
```

**Example 2**: Your test score is 85 out of 100. What percent is that?

```python
score = 85
total = 100
percentage = (score / total) * 100
print(f'You scored {percentage}%')
```

**Example 3**: You earned $50 and your parents gave you a 10% bonus. How much now?

```python
earnings = 50
bonus_percent = 10
bonus = earnings * (bonus_percent / 100)
total_earnings = earnings + bonus
print(f'Total: ${total_earnings}')
```

## Exercises by Bloom Level
- Remember: Write the discount formula.
- Understand: Why multiply by `(1 - rate)` instead of subtracting?
- Apply: Calculate tip on a restaurant bill (15% of $28).
- Analyze: Compare 30% off vs "pay 70%" — are they the same?
- Create: Build a discount calculator app that asks price and percentage.

## Tips
- To increase by 20%: `value * 1.20`.
- To decrease by 20%: `value * 0.80`.

## Related Concepts
- [[Python - Math - Money & Budget]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
