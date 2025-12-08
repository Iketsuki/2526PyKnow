### Task ID: UA1047
### Task Title: While Loop Input Validation

-----

### 📚 Quick Lesson

**Concept:**
A `while` loop can be used to keep asking for input until the user enters a valid value. Example:
```python
n = int(input())
while n < 1 or n > 10:
    print("Invalid input. Try again.")
    n = int(input())
```
This keeps asking until $n$ is between 1 and 10.

-----

### 🖥️ Main Statement

**Story:**
Write a program that asks the user to enter a number between 1 and 100 (inclusive). If the input is invalid, print "Invalid input. Try again." and ask again, until a valid number is entered.

**Input:**
Each line contains an integer $n$.

**Output:**
If $n$ is not between 1 and 100, print "Invalid input. Try again." and ask again. When a valid $n$ is entered, print "Accepted: n" (where n is the valid number).

**Constraints:**
- $1 \leq n \leq 100$

**Sample Tests:**
Input:
```
-5
105
50
```
Output:
```
Invalid input. Try again.
Invalid input. Try again.
Accepted: 50
```

Input:
```
101
100
```
Output:
```
Invalid input. Try again.
Accepted: 100
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# TODO: use a while loop to keep asking for input until valid

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
