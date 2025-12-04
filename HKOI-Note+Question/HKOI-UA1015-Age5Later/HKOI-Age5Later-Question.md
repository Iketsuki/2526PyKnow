### Task ID: UA1015
### Task Title: Age 5 Years Later

-----

### 📚 Quick Lesson

**Concept:**
You can print multiple values in Python using commas in the `print()` function. This automatically adds spaces between the values and works for both strings and numbers, without needing to convert numbers to strings.

```python
# Example: Add 7 to age
age = int(input())
later = age + 7
print("7 years later I will be", later, "years old.")
```

-----

### 🖥️ Main Statement

**Story:**
Read your age as an integer. Print what your age will be in 5 years in the format:

`5 years later I will be 10 years old.`

**Input:**
The first line contains an integer $age$.

**Output:**
Print one line: `5 years later I will be y years old.`, where $y$ is $age + 5$.

**Sample Tests:**
Input:
```
5
```
Output:
```
5 years later I will be 10 years old.
```

Input:
```
12
```
Output:
```
5 years later I will be 17 years old.
```

Input:
```
0
```
Output:
```
5 years later I will be 5 years old.
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read your age as an integer
age = # TODO: read integer

# Step 2: Calculate age 5 years later
later = # TODO: add 5 to age

# Step 3: Print the result using commas
print(# TODO: print using commas)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
