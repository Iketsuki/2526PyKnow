import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
if n >= 10 and n <= 20:
    print("In range")
else:
    print("Out of range")

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
