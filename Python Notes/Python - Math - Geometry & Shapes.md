---
tags: [python, math, geometry]
moc: [[Python - Practical Math (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: formulas for area, perimeter, volume."
  - "Understand: when to use which formula."
  - "Apply: calculate sizes for rooms, objects, games."
---

# Python - Math - Geometry & Shapes

## Concept
Calculate area (2D space), perimeter (edge length), and volume (3D space) using formulas. Use `import math` for `math.pi`.

## Real-World Examples

**Example 1**: Your bedroom is 12 feet wide and 10 feet long. What's the area?

```python
width = 12
length = 10
area = width * length
print(f'Bedroom area: {area} sq ft')
```

**Example 2**: You want to fence a rectangular garden (12m × 8m). How much fencing do you need?

```python
length = 12
width = 8
perimeter = 2 * (length + width)
print(f'Fencing needed: {perimeter} meters')
```

**Example 3**: A circular pizza has radius 6 inches. What's the area?

```python
import math
radius = 6
area = math.pi * radius ** 2
print(f'Pizza area: {area:.2f} sq inches')
```

**Example 4**: Your cylindrical drink cup is 10 cm tall with radius 4 cm. How much can it hold?

```python
import math
radius = 4
height = 10
volume = math.pi * radius ** 2 * height
print(f'Cup volume: {volume:.2f} cubic cm')
```

**Example 5**: A basketball court is 94 feet long and 50 feet wide. What's the perimeter?

```python
length = 94
width = 50
perimeter = 2 * (length + width)
print(f'Court perimeter: {perimeter} feet')
```

## Formulas

- **Rectangle area**: length × width
- **Rectangle perimeter**: 2 × (length + width)
- **Circle area**: π × radius²
- **Circle circumference**: 2 × π × radius
- **Triangle area**: 0.5 × base × height
- **Cylinder volume**: π × radius² × height
- **Cube volume**: side³

## Common Errors with Example Code

### Error 1: Forgetting to import math for pi
```python
# WRONG: math.pi not available without import
area = math.pi * radius ** 2  # NameError: math is not defined

# CORRECT: Import math first
import math
radius = 6
area = math.pi * radius ** 2
print(area)  # 113.097...
```

### Error 2: Confusing diameter and radius
```python
# WRONG: Using diameter instead of radius
diameter = 10
area = math.pi * diameter ** 2  # Wrong! (diameter, not radius)

# CORRECT: Convert diameter to radius first
diameter = 10
radius = diameter / 2
area = math.pi * radius ** 2
print(area)  # 78.54...
```

### Error 3: Wrong formula for perimeter
```python
# WRONG: Using area formula for perimeter
length = 12
width = 8
perimeter = length * width  # This is AREA, not perimeter!

# CORRECT: Perimeter adds all sides
perimeter = 2 * (length + width)
print(perimeter)  # 40
```

### Error 4: Forgetting to square the radius
```python
# WRONG: Forgetting radius is squared
radius = 5
area = math.pi * radius  # Missing ** 2!

# CORRECT: Square the radius
area = math.pi * radius ** 2
print(area)  # 78.54...
```

### Error 5: Wrong operator precedence in formulas
```python
# WRONG: Missing parentheses, wrong calculation order
radius = 5
height = 10
volume = math.pi * radius ** 2 * height  # Actually correct order
# But this is wrong:
volume = math.pi * radius ** 2 + height  # Wrong! (+ instead of *)

# CORRECT: Parentheses make intent clear
volume = math.pi * (radius ** 2) * height
print(volume)  # 785.398...
```

## Exercises by Bloom Level

- **Remember**: Write the area formula for a rectangle.
- **Understand**: When use `math.pi`? What's difference between radius and diameter?
- **Apply**: Calculate the area of your room.
- **Analyze**: Compare areas of different shapes.
- **Create**: Build a shape calculator app.

## Tips
- Use `** 2` for square (e.g., `radius ** 2` instead of `radius * radius`).
- Use `math.pi` for accurate π value.
- Remember: radius is half the diameter.

## Related Concepts
- [[Python - Math - Arithmetic Operators]]
- [[Python - Math - Calculator Basics]]
- [[Python - Math - Rounding & Precision]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
