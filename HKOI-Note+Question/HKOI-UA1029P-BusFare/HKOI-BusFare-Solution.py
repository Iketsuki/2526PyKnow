import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

a = int(input())
d = float(input())
if a < 12:
    fare = d * 0.5
elif a >= 65:
    fare = d * 0.7
else:
    fare = d * 1.0
print(fare)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
