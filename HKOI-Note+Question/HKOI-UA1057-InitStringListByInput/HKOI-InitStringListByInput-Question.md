### Task ID: UA1057
### Task Title: Initialize String List by Input

-----

### 📚 Quick Lesson

**Concept:**
You can fill a list by assigning values to each index in a loop. Example:
```python
n = 3
arr = [""] * n
for i in range(n):
    arr[i] = input()
print(arr)
```

-----

### 🖥️ Main Statement

**Story:**
Write a program that asks the user for the number of elements, then reads that many strings (one per line) and stores them in a list. Print the list at the end.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 10$).
The next $n$ lines each contain a string (no spaces).

**Output:**
Print the list of strings.

**Sample Tests:**
Input:
```
3
cat
dog
bird
```
Output:
```
['cat', 'dog', 'bird']
```

Input:
```
2
apple
banana
```
Output:
```
['apple', 'banana']
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# Step 1: create a list of n empty strings
arr = [""] * n
# Step 2: fill the list using a loop
for i in range(n):
    # TODO: read a string and store it in arr[i]
    arr[i] = ____
# Step 3: print the list
print(arr)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
