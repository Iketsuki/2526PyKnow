# UA1013 - Print Two Words Together and With Space
# Solution

import time
start_time = time.time()

# Step 1: Read two words from input
word1 = input()
word2 = input()

# Step 2: Print them together (no space)
print(word1 + word2)

# Step 3: Print them with a space between
print(word1, word2)

end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
