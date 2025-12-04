### Task ID: UA1016P
### Task Title: Triangle Area Calculation

-----

### 📚 Quick Lesson

**Concept:**
You can ask questions in `input()` to make your program interactive. For example, to calculate the area of a square:

```python
# Example: Area of a square
side = float(input("What is the side length of the square? "))
area = side * side
print("The area of the square is", area)
```

-----

### 🖥️ Main Statement

**Story:**
You want to find the area of a triangle. Ask the user for the base and height using questions in `input()`. Then, calculate and print the area.

**Input:**
The first line contains the base of the triangle (a real number).
The second line contains the height of the triangle (a real number).

**Output:**
- First, print: `What is the base of the triangle?`
- Second, print: `What is the height of the triangle?`
- Third, print: `The area of the triangle is <area>`

**Constraints:**
- $0 < \text{base} \leq 1000$
- $0 < \text{height} \leq 1000$

**Sample Tests:**
Input:
```
10
5
```
Output:
```
What is the base of the triangle?
What is the height of the triangle?
The area of the triangle is 25.0
```

Input:
```
3.5
2
```
Output:
```
What is the base of the triangle?
What is the height of the triangle?
The area of the triangle is 3.5
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Ask for the base
base = # TODO: ask for base with input()

# Step 2: Ask for the height
height = # TODO: ask for height with input()

# Step 3: Calculate the area
area = # TODO: calculate area

# Step 4: Print the area
print(# TODO: print area)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
