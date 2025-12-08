### Task ID: UA1048P
### Task Title: Sum Odd Numbers with Input Validation

-----

### 📚 Quick Lesson

**Concepts Combined:**
- Input validation with a while loop
- Summing odd numbers with a while loop

-----

### 🖥️ Main Statement

**Story:**
Write a program that asks the user to enter a number between 1 and 100 (inclusive). If the input is invalid, print "Invalid input. Try again." and ask again, until a valid number is entered. Then, print the sum of all odd numbers from 1 up to that number (inclusive).

**Input:**
Each line contains an integer $n$.

**Output:**
If $n$ is not between 1 and 100, print "Invalid input. Try again." and ask again. When a valid $n$ is entered, print the sum of all odd numbers from 1 to $n$.

**Constraints:**
- $1 \leq n \leq 100$

**Sample Tests:**
Input:
```
-5
105
7
```
Output:
```
Invalid input. Try again.
Invalid input. Try again.
16
```

Input:
```
100
```
Output:
```
2500
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# TODO: input validation and sum odd numbers

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
