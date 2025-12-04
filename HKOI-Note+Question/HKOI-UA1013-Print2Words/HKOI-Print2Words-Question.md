### Task ID: UA1013
### Task Title: Print Two Words Together and With Space

-----

### 📚 Quick Lesson

**Concept:**
In Python, you can join strings using the `+` operator (concatenation) or by printing multiple values separated by commas (which adds a space between them).

```python
# Concatenation (no space)
a = "Hello"
b = "world"
print(a + b)  # Output: Helloworld

# Print with space
a = "Hello"
b = "world"
print(a, b)   # Output: Hello world
```

-----

### 🖥️ Main Statement

**Story:**
Read two words from input. Print them together (no space), then print them with a space between.

**Input:**
The first line contains a word $a$.
The second line contains a word $b$.

**Output:**
Print two lines:
- First line: $a$ and $b$ joined together (no space)
- Second line: $a$ and $b$ separated by a space

**Sample Tests:**
Input:
```
Hello
world
```
Output:
```
Helloworld
Hello world
```

Input:
```
Python
Rocks
```
Output:
```
PythonRocks
Python Rocks
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read two words from input
word1 = # TODO: read first word
word2 = # TODO: read second word

# Step 2: Print them together (no space)
print(# TODO: print word1 and word2 joined)

# Step 3: Print them with a space between
print(# TODO: print word1 and word2 with space)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
