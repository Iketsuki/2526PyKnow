---
tags: [python, debugging, try-except, finally, cleanup, context-managers]
moc: [[Python - Debugging (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: `finally` block always executes."
  - "Understand: when to use `finally` for cleanup."
  - "Apply: safe resource management with `with` statement."
---

# Python - Debugging - Finally Blocks

## Concept
`finally` block runs **no matter what** — after normal execution or exception. Use for cleanup: closing files, releasing connections, resetting state.

## Finally Always Runs

```python
try:
    print('Try block')
    result = 10 / 0
except ZeroDivisionError:
    print('Except block')
finally:
    print('Finally block')

# Output:
# Try block
# Except block
# Finally block
```

Finally runs even if no exception:

```python
try:
    print('Try block')
    result = 10 / 2
except ZeroDivisionError:
    print('Except block')
finally:
    print('Finally block')

# Output:
# Try block
# Finally block
```

## File Cleanup with Finally

Without `finally` — file might stay open if error occurs:

```python
# RISKY: File stays open if error in processing
file = open('data.txt', 'r')
content = file.read()
file.close()  # Skipped if error happens above
```

With `finally` — file always closes:

```python
file = None
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('File not found')
finally:
    if file:
        file.close()  # Always runs
```

## Context Managers: Better Alternative

**Use `with` statement instead of finally for files:**

```python
try:
    with open('data.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found')
# File closes automatically, no finally needed
```

Benefits of `with`:
- Automatic cleanup (even if exception)
- Cleaner code
- Works with files, connections, locks, etc.

## Resource Cleanup Examples

### Database Connection

```python
connection = None
try:
    connection = create_database_connection()
    data = connection.query('SELECT * FROM users')
except ConnectionError as e:
    print(f'Connection failed: {e}')
finally:
    if connection:
        connection.close()  # Always close
```

### File Writing

```python
file = None
try:
    file = open('output.txt', 'w')
    file.write('Important data')
except IOError as e:
    print(f'Write failed: {e}')
finally:
    if file:
        file.close()
```

### Lock Release (Threading)

```python
lock = threading.Lock()

try:
    lock.acquire()
    # Critical section
    modify_shared_resource()
finally:
    lock.release()  # Always release, even if error
```

## Finally with Else

Combines success path (`else`) and cleanup (`finally`):

```python
try:
    age = int(input('Age: '))
except ValueError:
    print('Invalid input')
else:
    print(f'You are {age} years old')
finally:
    print('Input complete')

# If invalid: "Invalid input" → "Input complete"
# If valid: "You are X years old" → "Input complete"
```

## Real-World: Transaction Rollback

```python
transaction = None
try:
    transaction = db.begin_transaction()
    transaction.insert('users', {'name': 'Alice'})
    transaction.insert('logs', {'action': 'insert'})
    transaction.commit()  # Success
except Exception as e:
    print(f'Error: {e}')
    if transaction:
        transaction.rollback()  # Undo if error
finally:
    if transaction:
        transaction.close()  # Always close
```

## Real-World: Temporary File Cleanup

```python
import tempfile
import os

temp_file = None
try:
    # Create temporary file
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    temp_file.write('temporary data')
    temp_file.flush()
    
    # Use temporary file
    process_file(temp_file.name)
except Exception as e:
    print(f'Process failed: {e}')
finally:
    if temp_file:
        temp_file.close()
        os.remove(temp_file.name)  # Clean up
```

## Real-World: Timer Reset

```python
timer_running = False

try:
    timer = start_timer()
    timer_running = True
    
    long_operation()
finally:
    if timer_running:
        timer.stop()  # Always stop
        timer_running = False
```

## Common Errors with Example Code

1) Forgetting cleanup — using finally would fix this

WRONG
```python
file = open('data.txt', 'r')
content = file.read()
# If exception happens, file never closes
# File descriptor leaked
```

CORRECT
```python
file = None
try:
    file = open('data.txt', 'r')
    content = file.read()
finally:
    if file:
        file.close()

# Or better: use 'with'
with open('data.txt', 'r') as file:
    content = file.read()
```

2) Not checking if resource exists before cleanup

WRONG
```python
try:
    connection = create_connection()
    data = query(connection)
except ConnectionError:
    pass
finally:
    connection.close()  # NameError if create_connection() failed
```

CORRECT
```python
connection = None
try:
    connection = create_connection()
    data = query(connection)
except ConnectionError:
    pass
finally:
    if connection:  # Check before cleanup
        connection.close()
```

3) Using finally when context manager is better

WRONG
```python
file = None
try:
    file = open('data.txt', 'r')
    data = file.read()
finally:
    if file:
        file.close()
```

CORRECT
```python
with open('data.txt', 'r') as file:
    data = file.read()
# File closes automatically
```

## Tips
- **Always clean up** resources (files, connections, locks)
- **Prefer `with`** for file operations
- **Check before cleanup** in finally — resource might not exist
- **Finally + else** = error path + success path + cleanup
- **Use finally** for non-file resources (sockets, locks, connections)

## Related Concepts
- [[Python - Debugging - Try-Except Syntax]]
- [[Python - Debugging - Exception Info]]
- [[Python - File IO - Context Managers]]

## MOC
- Parent: [[Python - Debugging (MOC)]]
