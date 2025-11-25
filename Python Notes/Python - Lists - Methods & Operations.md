---
tags: [python, lists, methods]
moc: [[Python - Lists (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: common list methods."
  - "Understand: .append(), .insert(), .remove(), .sort()."
  - "Apply: modify lists safely and efficiently."
---

# Python - Lists - Methods & Operations

## Overview
This page is a parent index for list method operations. For detailed atomic notes on specific method families, see the links below.

**Core list methods** fall into three categories:
1. **Adding items** — [[Python - Lists - Add Methods]]
2. **Removing items** — [[Python - Lists - Remove Methods]]  
3. **Searching & sorting** — [[Python - Lists - Search & Sort]]

## Quick Reference

```python
# Add items
list.append(x)          # Add one item to end
list.insert(i, x)       # Add at specific index
list.extend(iterable)   # Add multiple items (unpacks)

# Remove items
list.remove(x)          # Remove first occurrence of value
list.pop(i)             # Remove at index, return value
list.clear()            # Remove all items

# Find & count
x in list               # Check if value exists
list.index(x)           # Find first index of value
list.count(x)           # Count occurrences of value

# Sort & order
list.sort()             # Sort in place
list.reverse()          # Reverse order in place
sorted(list)            # Return new sorted list
list.copy()             # Create independent copy
```

## Real-World: Integrated Example

```python
def manage_scores(scores, new_score, remove_score=None):
    '''Add new score, remove if specified, keep top 10 sorted'''
    # Add new score
    scores.append(new_score)
    
    # Remove specific score if requested
    if remove_score and remove_score in scores:
        scores.remove(remove_score)
    
    # Sort and trim
    scores.sort(reverse=True)
    if len(scores) > 10:
        scores.pop()  # Remove lowest score
    
    return scores

leaderboard = [95, 88, 92, 85]
leaderboard = manage_scores(leaderboard, 90, remove_score=85)
print(leaderboard)  # [95, 92, 90, 88]
```

## Common Errors with Example Code

1) Mutating list while iterating (skips items)

WRONG
```python
nums = [1, 2, 3, 4]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)  # Modifying during iteration
print(nums)  # [1, 3] but logic unreliable
```

CORRECT
```python
nums = [1, 2, 3, 4]
nums = [n for n in nums if n % 2 != 0]  # Use comprehension
print(nums)  # [1, 3]
```

2) Assignment creates reference, not copy (shared modification)

WRONG
```python
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)  # [1, 2, 3, 4] — modified unexpectedly!
```

CORRECT
```python
original = [1, 2, 3]
copy = original.copy()  # or original[:]
copy.append(4)
print(original)  # [1, 2, 3] — unchanged
print(copy)  # [1, 2, 3, 4]
```

3) Confusing `append()` with `extend()` (nested lists)

WRONG
```python
lst = [1, 2]
lst.append([3, 4])
print(lst)  # [1, 2, [3, 4]] — nested list!
```

CORRECT
```python
lst = [1, 2]
lst.extend([3, 4])
print(lst)  # [1, 2, 3, 4] — flat list
```

## Atomic Method Notes

For deep dives into specific operations, see:

- [[Python - Lists - Add Methods]] — .append(), .insert(), .extend()
- [[Python - Lists - Remove Methods]] — .remove(), .pop(), .clear()
- [[Python - Lists - Search & Sort]] — .index(), .count(), .sort(), .reverse(), sorted()

## Related Concepts
- [[Python - Lists - Indexing & Edge Cases]]
- [[Python - Lists - Common Patterns]]
- [[Python - Lists - List Comprehension]]
- [[Python - Variables & Types - Built-in Functions]]

## MOC
- Parent: [[Python - Lists (MOC)]]
