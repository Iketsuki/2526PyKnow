import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
h = n // 3600
m = (n % 3600) // 60
s = n % 60
print(f"{h}:{m}:{s}")

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
