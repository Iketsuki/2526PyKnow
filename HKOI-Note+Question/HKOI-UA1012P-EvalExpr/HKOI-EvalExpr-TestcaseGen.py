import os
import random

if not os.path.exists('tests'):
    os.makedirs('tests')

def solve(x):
    y = x - (x**2 + 4) / 2 + (x**3 - 3 * x + 7) / 3
    return f"{y:.3f}"

# Constraints
MIN_X = -100.0
MAX_X = 100.0
NUM_TESTS = 10

# Test values: samples and random
values = [2.0, -1.5] + [round(random.uniform(MIN_X, MAX_X), 2) for _ in range(NUM_TESTS - 2)]

for i, x in enumerate(values, 1):
    with open(f'tests/1-{i}.in', 'w') as fin:
        fin.write(f'{x}\n')
    with open(f'tests/1-{i}.out', 'w') as fout:
        fout.write(solve(x) + '\n')

print(f"Generated {NUM_TESTS} test cases in /tests folder.")
