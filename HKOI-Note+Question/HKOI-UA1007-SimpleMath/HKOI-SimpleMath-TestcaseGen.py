import os
import random

if not os.path.exists('tests'):
    os.makedirs('tests')

def solve(a, b):
    return f"{a + b}\n{a - b}\n{a * b}\n{a / b}"

# Constraints
MIN_N = 1
MAX_N = 100
NUM_TESTS = 10

# Test values: samples and random
pairs = [(7, 3), (12, 4)] + [(random.randint(MIN_N, MAX_N), random.randint(MIN_N, MAX_N)) for _ in range(NUM_TESTS - 2)]

for i, (a, b) in enumerate(pairs, 1):
    with open(f'tests/1-{i}.in', 'w') as fin:
        fin.write(f'{a}\n{b}\n')
    with open(f'tests/1-{i}.out', 'w') as fout:
        fout.write(solve(a, b) + '\n')

print(f"Generated {NUM_TESTS} test cases in /tests folder.")
