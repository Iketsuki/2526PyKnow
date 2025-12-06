### Task ID: UA1024P
### Task Title: Teenager or Not?

-----

### 📚 Quick Lesson

**Concept:**
You can convert values to boolean using `bool()`. For example:
- `bool(0)` is `False`
- `bool(1)` is `True`
- `bool('False')` is `True` (non-empty string)
- `bool('')` is `False` (empty string)

For user input, you often need to compare strings directly, e.g.:
```python
e = input()  # 'True' or 'False'
if e == 'True':
    print('Eligible!')
```

-----

### 🖥️ Main Statement

**Story:**
Given two inputs: age (integer) and eligibility (either `True` or `False` as a string), print `Teenager and eligible` if age is between 13 and 19 (inclusive) and eligibility is `True`. Otherwise, print `Not both`.

**Input:**
The first line contains an integer $a$ ($0 \leq a \leq 100$), the age.
The second line contains a string $e$ (`True` or `False`).

**Output:**
Print `Teenager and eligible` if $13 \leq a \leq 19$ and $e$ is `True`, otherwise print `Not both`.

**Constraints:**
- $0 \leq a \leq 100$
- $e$ is either `True` or `False`

**Sample Tests:**
Input:
```
15
True
```
Output:
```
Teenager and eligible
```

Input:
```
12
True
```
Output:
```
Not both
```

Input:
```
17
False
```
Output:
```
Not both
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

a = int(input())
e = input()  # 'True' or 'False'
# TODO: check if a is teenager and e is True

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
