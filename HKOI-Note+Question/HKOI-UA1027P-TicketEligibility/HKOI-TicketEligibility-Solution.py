import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

a = int(input())
d = input()  # 'True' or 'False'
if a >= 65 or d == 'True':
    print("Eligible for 2 dollar ticket")
else:
    print("Regular ticket")

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
