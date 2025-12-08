### Task ID: UA1059
### Task Title: Split Input and Print Items

-----

### 📚 Quick Lesson

**Concept:**
You can split a line of input into a list using `split()`. You can print each item using a for loop, and use `len()` to get the number of items. Example:
```python
arr = input().split()
for x in arr:
    print(x)
print(len(arr))
```
Or:
```python
for i in range(len(arr)):
    print(arr[i])
```

-----

### 🖥️ Main Statement

**Story:**
Write a program that asks the user for the number of items $n$, then reads one line of $n$ space-separated strings. Print each item on a new line using a for loop, and print the number of items at the end.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 10$).
The second line contains $n$ space-separated strings.

**Output:**
Print each item on a new line, then print the number of items.

**Sample Tests:**
Input:
```
3
cat dog bird
```
Output:
```
cat
dog
bird
3
```

Input:
```
2
apple banana
```
Output:
```
apple
banana
2
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
arr = input()____
# TODO: print each item using a for loop
for i in range(len(arr)):
    print(____)
# Alternative:
# for x in arr:
#     print(x)
# TODO: print the number of items
print(____)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
