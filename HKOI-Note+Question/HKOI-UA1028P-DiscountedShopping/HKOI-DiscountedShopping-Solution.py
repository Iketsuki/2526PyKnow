import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

p = float(input())
d = int(input())
final = p * (1 - d / 100)
if final > 500:
    final = final * 0.9
    print(final)
else:
    print("No extra discount")
    print(final)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
