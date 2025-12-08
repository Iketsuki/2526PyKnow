### Task ID: UA1038
### Task Title: Sum Up Numbers

-----

### 📚 Quick Lesson

**Concept:**
You can use a variable to keep a running total in a loop. Example:
```python
sum = 0
for i in range(1, 6):
    sum = sum + i # or sum += i
print(sum)  # prints 15
```
This adds up numbers from 1 to 5.

-----

### 🖥️ Main Statement

**Story:**
Write a program that calculates the sum of all numbers from 1 up to the number entered by the user.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).

**Output:**
Print the sum.

**Constraints:**
- $1 \leq n \leq 100$

**Sample Tests:**
Input:
```
5
```
Output:
```
15
```

Input:
```
1
```
Output:
```
1
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use a for loop to calculate the sum from 1 to n

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
