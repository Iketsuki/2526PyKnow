import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

a = int(input())
if a < 13:
    print("Child")
elif a <= 19:
    print("Teenager")
elif a <= 64:
    print("Adult")
else:
    print("Senior")

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
