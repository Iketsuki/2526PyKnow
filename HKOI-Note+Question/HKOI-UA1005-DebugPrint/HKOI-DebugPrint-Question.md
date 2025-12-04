### Task ID: UA1005
### Task Title: Debug with Print

-----

### 📚 Quick Lesson

**Concept:**
You can use the `print()` function to check the value of a variable at any step in your program. This helps you find mistakes and understand how your code works.

**Example:**
```python
number = 4.0
print(number)  # Shows: 4.0
sum_value = number + 3
print(sum_value)  # Shows: 7.0
result = sum_value / 2
print(result)  # Shows: 3.5
```

-----

### 🖥️ Main Statement

**Story:**
Read a decimal number, add 3, divide by 2, and print the value of each variable after you change it. Use `print()` to show the value of `number`, `sum_value`, and `result` after each step.

**Input:**
The first line contains a decimal number $X$.

**Output:**
Print the value of each variable after it changes, each on its own line.

**Constraints:**
$0.0 \leq X \leq 100.0$

## **Sample Tests:** 
| Input | Output | 
|---|---|
| 4.0 | 4.0\n7.0\n3.5 |
| 10.0 | 10.0\n13.0\n6.5 |

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

number = float(input())
# TODO: print the value of number

sum_value = number + 3
# TODO: print the value of sum_value

result = sum_value / 2
# TODO: print the value of result

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
