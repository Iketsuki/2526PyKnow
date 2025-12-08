import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

a = float(input())
b = float(input())
op = input()
if op == 'add':
    print(a + b)
elif op == 'sub':
    print(a - b)
elif op == 'mul':
    print(a * b)
elif op == 'div':
    print(a / b)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
