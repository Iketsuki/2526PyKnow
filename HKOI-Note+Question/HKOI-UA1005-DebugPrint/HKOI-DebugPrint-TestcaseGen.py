import os
import random

if not os.path.exists('tests'):
    os.makedirs('tests')

def solve(x):
    number = x
    sum_value = number + 3
    result = sum_value / 2
    return f"{number}\n{sum_value}\n{result}"

# Constraints
MIN_X = 0.0
MAX_X = 100.0
NUM_TESTS = 10

# Test values: min, max, and random floats
test_values = [MIN_X, MAX_X, 4.0, 10.0] + [round(random.uniform(MIN_X, MAX_X), 2) for _ in range(NUM_TESTS - 4)]

for i, x in enumerate(test_values, 1):
    with open(f'tests/1-{i}.in', 'w') as fin:
        fin.write(f'{x}\n')
    with open(f'tests/1-{i}.out', 'w') as fout:
        fout.write(solve(x) + '\n')

print(f"Generated {NUM_TESTS} test cases in /tests folder.")
