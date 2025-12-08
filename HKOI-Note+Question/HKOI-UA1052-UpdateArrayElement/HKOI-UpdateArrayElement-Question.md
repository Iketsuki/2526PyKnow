### Task ID: UA1052
### Task Title: Update Array Element

-----

### 📚 Quick Lesson

**Concept:**
You can update an element in a list by assigning a new value to a specific index. Example:
```python
arr = ["apple", "banana", "cherry"]
arr[1] = "orange"
print(arr)  # prints ['apple', 'orange', 'cherry']
```

-----

### 🖥️ Main Statement

**Story:**
Given a list of strings `["cat", "dog", "bird", "fish", "ant"]`, write a program that asks the user for an index and a new word, updates the element at that index with the new word, and prints the whole list.

**Input:**
The first line contains an integer $i$ ($0 \leq i \leq 4$).
The second line contains a string $w$ (no spaces).

**Output:**
Print the updated list.

**Sample Tests:**
Input:
```
2
parrot
```
Output:
```
['cat', 'dog', 'parrot', 'fish', 'ant']
```

Input:
```
0
lion
```
Output:
```
['lion', 'dog', 'bird', 'fish', 'ant']
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

arr = ["cat", "dog", "bird", "fish", "ant"]
i = int(input())
w = input()
# TODO: update arr[i] with w and print arr

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
