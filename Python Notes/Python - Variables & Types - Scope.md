---
tags: [python, variables, scope]
moc: [[Python - Variables & Types (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: local vs global scope."
  - "Understand: where variable exists."
  - "Apply: use scope correctly in functions."
---

# Python - Variables & Types - Scope

## Concept
**Scope** — where a variable exists and is accessible. **Local** — inside function. **Global** — outside function.

## Local Scope (Inside Function)

```python
def greet():
    name = 'Alice'  # Local variable
    print(name)

greet()  # Alice (works inside function)
print(name)  # Error! name doesn't exist here
```

## Global Scope (Outside Function)

```python
name = 'Bob'  # Global variable

def greet():
    print(name)  # Can read global variable

greet()  # Bob
print(name)  # Bob (works outside function)
```

## Local Hides Global

```python
message = 'Hello'

def test():
    message = 'Hi'  # Local variable (different from global)
    print(message)

test()  # Hi (prints local)
print(message)  # Hello (global unchanged)
```

## Reading vs Modifying Global

```python
counter = 0

def increment():
    global counter  # Must declare to modify global
    counter += 1

increment()
print(counter)  # 1

increment()
print(counter)  # 2
```

## Real-World: Score Tracker

```python
# Global score
total_score = 0

def add_points(points):
    global total_score
    total_score += points
    return total_score

print(add_points(10))  # 10
print(add_points(5))  # 15
print(total_score)  # 15
```

## Real-World: Game Settings

```python
difficulty = 'normal'  # Global setting

def create_enemy(enemy_type):
    if difficulty == 'hard':  # Read global
        health = 100
    else:
        health = 50
    return {'type': enemy_type, 'health': health}

print(create_enemy('goblin'))  # {'type': 'goblin', 'health': 50}
```

## Function Parameters (Local)

```python
def add(a, b):  # a, b are local to this function
    result = a + b  # result is local
    return result

print(add(3, 5))  # 8
print(a)  # Error! a doesn't exist outside
print(result)  # Error! result is local to function
```

## Scope Chain (Nested Functions)

```python
x = 'global'

def outer():
    x = 'outer'
    
    def inner():
        x = 'inner'
        print(x)
    
    inner()
    print(x)

outer()
# Output:
# inner
# outer

print(x)  # global
```

## Common Mistake: Forgetting global

```python
# WRONG: trying to modify global without declaration
counter = 0

def increment():
    counter += 1  # Error! UnboundLocalError
    # Python thinks counter is local, but hasn't been assigned yet

# RIGHT:
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1
```

## Best Practice: Avoid Global Modification

```python
# LESS GOOD: global modification
score = 0

def add_points(points):
    global score
    score += points

# BETTER: return new value
def add_points_better(current_score, points):
    return current_score + points

score = 0
score = add_points_better(score, 10)
print(score)  # 10
```

## Local Variables in Loops

```python
for i in range(3):
    name = 'Alice'  # Created each iteration

print(name)  # 'Alice' still exists (Python keeps it!)
# This is different from some languages
```

## Function Scope Example

```python
def create_student(name, grade):
    # name, grade are local parameters
    school = 'Lincoln High'  # local variable
    
    def get_info():
        # Can access outer function's variables
        return f'{name} in {grade} at {school}'
    
    return get_info()

print(create_student('Bob', 10))
# Bob in 10 at Lincoln High

print(school)  # Error! school is local to create_student
```

## Exercises by Bloom Level
- Remember: What's the difference between local and global?
- Understand: Why does local hide global?
- Apply: Use `global` to modify global variable.
- Analyze: Trace scope in nested functions.
- Create: Build function that uses global settings safely.

## Common Errors with Example Code

1) Accessing a variable defined inside a function (NameError)

WRONG
```python
def greet():
    message = 'Hello'

print(message)  # NameError: name 'message' is not defined
```

CORRECT
```python
def greet():
    message = 'Hello'
    return message

msg = greet()
print(msg)  # 'Hello'
```

2) Modifying a global variable without declaring `global` (UnboundLocalError)

WRONG
```python
count = 0
def inc():
    count += 1  # UnboundLocalError: local variable 'count' referenced before assignment

inc()
```

CORRECT
```python
count = 0
def inc():
    global count
    count += 1

inc()
print(count)  # 1
```

3) Expecting local changes to modify caller's variables for immutables

WRONG
```python
def set_to_zero(x):
    x = 0

value = 5
set_to_zero(value)
print(value)  # still 5
```

CORRECT
```python
def set_to_zero(x):
    return 0

value = 5
value = set_to_zero(value)
print(value)  # 0
```

## Related Concepts
- [[Python - Functions - Parameters & Return Values]]
- [[Python - Functions - Default Parameters & Keywords]]
- [[Python - Variables & Types - Type Checking]]

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
