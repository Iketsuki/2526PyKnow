import os
import random

if not os.path.exists('tests'):
    os.makedirs('tests')

def solve(a, b, c):
    return str(a - b + c)

# Constraints
MIN_A = 0
MAX_A = 100
MIN_B = 0
MAX_B = 100
MIN_C = 0
MAX_C = 100
NUM_TESTS = 10

# Test values: samples and random
triplets = [(10, 3, 5), (20, 5, 0)] + [
    (random.randint(MIN_B, MAX_A), random.randint(MIN_B, MAX_B), random.randint(MIN_C, MAX_C))
    for _ in range(NUM_TESTS - 2)
]

# Ensure B <= A for all cases
triplets = [(a, b if b <= a else a, c) for (a, b, c) in triplets]

for i, (a, b, c) in enumerate(triplets, 1):
    with open(f'tests/1-{i}.in', 'w') as fin:
        fin.write(f'{a}\n{b}\n{c}\n')
    with open(f'tests/1-{i}.out', 'w') as fout:
        fout.write(solve(a, b, c) + '\n')

print(f"Generated {NUM_TESTS} test cases in /tests folder.")
