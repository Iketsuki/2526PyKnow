import os
import random

if not os.path.exists('tests'):
    os.makedirs('tests')

def solve(n):
    return str(n * 2)

# Constraints
MIN_N = 1
MAX_N = 100
NUM_TESTS = 10

# Test values: min, max, and random
test_values = [MIN_N, MAX_N] + [random.randint(MIN_N, MAX_N) for _ in range(NUM_TESTS - 2)]

for i, n in enumerate(test_values, 1):
    with open(f'tests/1-{i}.in', 'w') as fin:
        fin.write(f'{n}\n')
    with open(f'tests/1-{i}.out', 'w') as fout:
        fout.write(solve(n) + '\n')

print(f"Generated {NUM_TESTS} test cases in /tests folder.")
