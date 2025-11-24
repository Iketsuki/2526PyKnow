---
tags: [python, math, time]
moc: [[Python - Practical Math (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: time conversions (hours, minutes, seconds)."
  - "Understand: calculating durations and countdowns."
  - "Apply: track time for activities, games, or deadlines."
---

# Python - Math - Time Calculations

## Concept
Convert and calculate time: 1 hour = 60 minutes, 1 minute = 60 seconds. Use subtraction to find elapsed time.

## Real-World Examples

**Example 1**: You started homework at 4:30 PM and finished at 5:45 PM. How long did it take?

```python
start_hour = 4
start_minute = 30
end_hour = 5
end_minute = 45

# Convert to total minutes
start_total = start_hour * 60 + start_minute
end_total = end_hour * 60 + end_minute
elapsed_minutes = end_total - start_total

hours = elapsed_minutes // 60
minutes = elapsed_minutes % 60
print(f'Homework time: {hours}h {minutes}m')
```

**Example 2**: You play a video game for 2.5 hours. That's how many minutes?

```python
game_hours = 2.5
game_minutes = game_hours * 60
print(f'Gaming time: {game_minutes} minutes')
```

**Example 3**: Your favorite show is 45 minutes. You've watched 30 minutes. Time left?

```python
total_duration = 45
watched = 30
remaining = total_duration - watched
print(f'Minutes left: {remaining}')
```

**Example 4**: Movie starts at 7:00 PM, it's 45 minutes long. What time does it end?

```python
start_hour = 7
start_minute = 0
duration_minutes = 45

total_minutes = start_hour * 60 + start_minute + duration_minutes
end_hour = total_minutes // 60
end_minute = total_minutes % 60
print(f'Movie ends at {end_hour}:{end_minute:02d}')
```

## Exercises by Bloom Level
- Remember: How many minutes in 3 hours?
- Understand: Why use `//` and `%` for time conversion?
- Apply: Calculate your total screen time for the week.
- Analyze: How long to watch 5 episodes (45 min each)?
- Create: Build a countdown timer app.

## Common Errors with Example Code

### Error 1: Forgetting to convert hours to minutes
```python
# WRONG: Adding hours and minutes directly
hours = 2
minutes = 30
total = hours + minutes  # 32 (WRONG! Mixed units)

# CORRECT: Convert to same unit
total_minutes = hours * 60 + minutes  # 150 minutes
print(total_minutes)  # 150
```

### Error 2: Using single `/` instead of `//` for integer division
```python
# WRONG: Regular division leaves decimals
total_minutes = 150
hours = total_minutes / 60  # 2.5 (float, not int)

# CORRECT: Use // for integer division
hours = total_minutes // 60  # 2 (integer)
minutes = total_minutes % 60  # 30

print(f'{hours}h {minutes}m')  # 2h 30m
```

### Error 3: Forgetting to format time with leading zeros
```python
# WRONG: 7:5 instead of 7:05
hour = 7
minute = 5
print(f'{hour}:{minute}')  # 7:5 (ugly)

# CORRECT: Use :02d format specifier
print(f'{hour}:{minute:02d}')  # 7:05 (proper time format)
```

### Error 4: Not handling time overflow (e.g., 65 minutes)
```python
# WRONG: Forgetting to convert overflow
end_hour = 6
end_minute = 65  # This is 1 hour 5 minutes, not valid time!

# CORRECT: Convert to proper time
total_minutes = end_hour * 60 + end_minute  # 425 minutes
final_hour = total_minutes // 60  # 7
final_minute = total_minutes % 60  # 5
print(f'{final_hour}:{final_minute:02d}')  # 7:05
```

### Error 5: Wrong calculation for elapsed time
```python
# WRONG: Simple subtraction without unit conversion
start_time = 14  # 2 PM
end_time = 16  # 4 PM
elapsed = end_time - start_time  # 2 (hours, happens to work)

# But this FAILS with minutes:
start = 14.5  # 2:30 PM
end = 16.25  # 4:15 PM
elapsed = end - start  # 1.75 (confusing!)

# CORRECT: Convert to minutes or seconds
start_minutes = 14 * 60 + 30  # 870
end_minutes = 16 * 60 + 15  # 975
elapsed_minutes = end_minutes - start_minutes  # 105

hours = elapsed_minutes // 60  # 1
minutes = elapsed_minutes % 60  # 45
print(f'Elapsed: {hours}h {minutes}m')  # 1h 45m
```

## Tips
- Use `{minute:02d}` to format minutes with leading zero (e.g., `7:05` not `7:5`).
- Convert all times to same unit (minutes or seconds) before calculating.
- Use `//` and `%` for time conversions.

## Related Concepts
- [[Python - Math - Arithmetic Operators]]
- [[Python - Math - Calculator Basics]]
- [[Python - Math - Rounding & Precision]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
