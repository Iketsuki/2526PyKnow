### Task ID: UB1002P
### Task Title: List Update (1-based)

-----

### 🖥️ Main Statement

**Story:**
You are given a list of numbers. Your task is to update one of the numbers and print the updated list.

**Input:**
- The first line contains an integer $n$, the number of items.
- The next $n$ lines each contain an integer (the list elements).
- The next line contains an integer $i$ (1-based index).
- The next line contains an integer $v$ (the new value).

**Output:**
Print the updated list, one number per line.

**Sample Input:**
```
4
10
20
30
40
2
99
```
**Sample Output:**
```
10
99
30
40
```

**Starter Code:**
```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read n
n = # TODO

# Step 2: Read n numbers into a list
# TODO: read and append

# Step 3: Read i and v
i = # TODO
v = # TODO

# Step 4: Update the i-th element (1-based)
# TODO: update lst[i-1]

# Step 5: Print the updated list
for x in lst:
    print(x)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
