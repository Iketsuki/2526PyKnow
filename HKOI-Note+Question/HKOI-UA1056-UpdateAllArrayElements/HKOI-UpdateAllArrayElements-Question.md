### Task ID: UA1056
### Task Title: Update All Array Elements

-----

### 📚 Quick Lesson

**Concept:**
You can update all elements in a list using a loop. You can also use the `*` operator to multiply each element. Example:
```python
arr = [2, 4, 6]
for i in range(len(arr)):
    # update each element by multiplying by 2 
    arr[i] = arr[i] * 2 
print(arr)  # prints [4, 8, 12]
```

-----

### 🖥️ Main Statement

**Story:**
Given a list `[1, 2, 3, 4, 5]`, write a program that updates every element by adding 3, then prints the updated list.

**Input:**
No input required.

**Output:**
Print the updated list.

**Sample Tests:**
Output:
```
[4, 5, 6, 7, 8]
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

arr = [1, 2, 3, 4, 5]
# TODO: update all elements by adding 3 and print arr

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
