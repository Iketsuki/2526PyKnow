import os
import random

if not os.path.exists('tests'):
    os.makedirs('tests')

def solve(n):
    return f"{n ** 2}\n{n // 3}\n{n % 3}"

# Constraints
MIN_N = 0
MAX_N = 100
NUM_TESTS = 10

# Test values: min, max, and random
values = [MIN_N, MAX_N, 5, 9, 3] + [random.randint(MIN_N, MAX_N) for _ in range(NUM_TESTS - 5)]

for i, n in enumerate(values, 1):
    with open(f'tests/1-{i}.in', 'w') as fin:
        fin.write(f'{n}\n')
    with open(f'tests/1-{i}.out', 'w') as fout:
        fout.write(solve(n) + '\n')

print(f"Generated {NUM_TESTS} test cases in /tests folder.")
