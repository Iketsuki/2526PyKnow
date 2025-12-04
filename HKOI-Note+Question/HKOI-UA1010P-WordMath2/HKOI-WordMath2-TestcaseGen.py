import os
import random

if not os.path.exists('tests'):
    os.makedirs('tests')

def solve(n, p):
    return str(n * p)

# Constraints
MIN_N = 1
MAX_N = 100
MIN_P = 1
MAX_P = 100
NUM_TESTS = 10

# Test values: samples and random
pairs = [(5, 2), (12, 3)] + [(random.randint(MIN_N, MAX_N), random.randint(MIN_P, MAX_P)) for _ in range(NUM_TESTS - 2)]

for i, (n, p) in enumerate(pairs, 1):
    with open(f'tests/1-{i}.in', 'w') as fin:
        fin.write(f'{n}\n{p}\n')
    with open(f'tests/1-{i}.out', 'w') as fout:
        fout.write(solve(n, p) + '\n')

print(f"Generated {NUM_TESTS} test cases in /tests folder.")
