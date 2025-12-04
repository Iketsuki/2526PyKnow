import os
import random

if not os.path.exists('tests'):
    os.makedirs('tests')

def solve(n):
    return str(abs(n))

# Constraints
MIN_N = -100
MAX_N = 100
NUM_TESTS = 10

# Test values: min, max, zero, and random
values = [MIN_N, MAX_N, 0, -7, 5] + [random.randint(MIN_N, MAX_N) for _ in range(NUM_TESTS - 5)]

for i, n in enumerate(values, 1):
    with open(f'tests/1-{i}.in', 'w') as fin:
        fin.write(f'{n}\n')
    with open(f'tests/1-{i}.out', 'w') as fout:
        fout.write(solve(n) + '\n')

print(f"Generated {NUM_TESTS} test cases in /tests folder.")
