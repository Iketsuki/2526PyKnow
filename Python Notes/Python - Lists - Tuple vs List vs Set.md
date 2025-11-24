---
tags: [python, lists, collections]
moc: [[Python - Lists (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: syntax for list, tuple, set."
  - "Understand: when to use each collection type."
  - "Apply: choose the right collection for a task."
---

# Python - Lists - Tuple vs List vs Set

## Concept
Python has three collection types:
- **List** `[...]` — ordered, changeable, allows duplicates
- **Tuple** `(...)` — ordered, unchangeable (immutable), allows duplicates
- **Set** `{...}` — unordered, unchangeable elements, NO duplicates

## Lists (Most Common)

```python
# Create a list
fruits = ['apple', 'banana', 'cherry']

# Lists are mutable (changeable)
fruits[0] = 'orange'  # Change first item
fruits.append('grape')  # Add item
print(fruits)  # ['orange', 'banana', 'cherry', 'grape']

# Lists allow duplicates
scores = [85, 90, 85, 95]
```

## Tuples (Immutable)

```python
# Create a tuple
coordinates = (5, 10)
rgb_color = (255, 128, 64)

# Tuples cannot be changed
# coordinates[0] = 7  # ERROR!

# Use when data shouldn't change
point = (3, 4)  # Fixed coordinate
print(point[0])  # 3

# Tuples allow duplicates
measurements = (12, 12, 15, 12)
```

## Sets (Unique Values)

```python
# Create a set
unique_colors = {'red', 'green', 'blue'}
unique_scores = {85, 90, 95}

# Sets remove duplicates automatically
scores_with_dupes = {85, 90, 85, 95, 90}
print(scores_with_dupes)  # {85, 90, 95}

# Sets are unordered
favorite_numbers = {7, 3, 9}
print(favorite_numbers)  # Could print in any order
```

## Real-World: When to Use Each

**List — Ordered collection that changes:**
```python
# Shopping list (can reorder, add, remove)
shopping = ['milk', 'bread', 'eggs']
shopping.append('cheese')  # Add item

# Quiz scores (ordered by date, can update)
quiz_scores = [8, 9, 7, 10]
quiz_scores[0] = 8.5  # Correct score
```

**Tuple — Fixed, unchanging data:**
```python
# RGB color (red, green, blue always in this order)
sky_blue = (135, 206, 235)

# Coordinate pair (x, y always in this order)
home = (40.7128, -74.0060)

# Function returning multiple values
def get_user():
    return ('Alice', 15, 'NYC')
name, age, city = get_user()
```

**Set — Find unique items, check membership:**
```python
# Unique students in club
club_members = {'Alice', 'Bob', 'Charlie', 'David'}

# Remove duplicates from list
noisy_list = [1, 2, 2, 3, 3, 3, 4]
unique = set(noisy_list)
print(unique)  # {1, 2, 3, 4}

# Check if user visited page before
visited_pages = {'home', 'about', 'products'}
if 'contact' in visited_pages:
    print('Already read')
else:
    print('New page')
```

## Quick Comparison

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Ordered | ✓ | ✓ | ✗ |
| Mutable | ✓ | ✗ | ✓ (add/remove) |
| Duplicates | ✓ | ✓ | ✗ |
| Best for | Changing collections | Fixed data | Unique items |
| Speed | Medium | Fast | Fast |

## Exercises by Bloom Level
- Remember: Which uses `{}`? Which uses `[]`?
- Understand: Why use tuple for coordinates?
- Apply: Convert list with dupes to set.
- Analyze: Compare list vs set for membership check.
- Create: Design data structure for friends (use best collection).

## Common Errors
- Trying to change tuple: `tuple[0] = 5` crashes.
- Forgetting set removes dupes: `{1, 1, 1}` is `{1}`.
- Sets are unordered: don't rely on index like lists.

## Related Concepts
- [[Python - Lists - Indexing & Access]]
- [[Python - Lists - Common Patterns]]
- [[Python - Variables & Types - Type Checking]]

## MOC
- Parent: [[Python - Lists (MOC)]]
