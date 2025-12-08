### Task ID: UA1061
### Task Title: Average Math Score (Split Input)

-----

### 📚 Quick Lesson

**Concept:**
You can use `split()` to read a line of numbers, convert them to integers, and calculate the average. Example:
```python
# see Split Input Calc Sum
avg = sum_score / len(arr)
print(avg)
```

-----

### 🖥️ Main Statement

**Story:**
Write a program that asks the user for the number of students $n$, then reads one line of $n$ space-separated math scores (each between 1 and 100). Print the average score as a float.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).
The second line contains $n$ space-separated integers $s$ ($1 \leq s \leq 100$).

**Output:**
Print the average score as a float.

**Sample Tests:**
Input:
```
3
80 90 100
```
Output:
```
90.0
```

Input:
```
2
50 100
```
Output:
```
75.0
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
arr = input().split()
sum_score = 0
for i in range(____):
    # TODO: add arr[i] to sum_score
    sum_score += ____
avg = sum_score / ____
print(avg)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
