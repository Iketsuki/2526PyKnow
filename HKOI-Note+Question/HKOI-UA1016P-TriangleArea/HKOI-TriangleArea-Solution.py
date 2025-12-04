# UA1016P - Triangle Area Calculation
# Solution

import time
start_time = time.time()

# Step 1: Ask for the base
print("What is the base of the triangle?")
base = float(input())

# Step 2: Ask for the height
print("What is the height of the triangle?")
height = float(input())

# Step 3: Calculate the area
area = base * height / 2

# Step 4: Print the area
print("The area of the triangle is", area)

end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
