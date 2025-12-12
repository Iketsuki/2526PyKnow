# UB1002P - Testcase Generator for List Update (1-based)
import os

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
os.makedirs(test_dir, exist_ok=True)

def write_test(idx, items, i, v):
    in_path = os.path.join(test_dir, f"1-{idx}.in")
    out_path = os.path.join(test_dir, f"1-{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{len(items)}\n")
        for item in items:
            fin.write(f"{item}\n")
        fin.write(f"{i}\n{v}\n")
    items2 = items[:]
    items2[i-1] = v
    with open(out_path, 'w') as fout:
        for x in items2:
            fout.write(f"{x}\n")

# Sample cases
write_test(1, [10, 20, 30, 40], 2, 99)
write_test(2, [1, 2, 3], 1, 100)

# Edge cases
write_test(3, [5], 1, 0)
write_test(4, [7, 8], 2, -1)
write_test(5, [0, 0, 0], 3, 42)

# Random cases
import random
for idx in range(6, 11):
    n = random.randint(2, 8)
    items = [random.randint(-100, 100) for _ in range(n)]
    i = random.randint(1, n)
    v = random.randint(-100, 100)
    write_test(idx, items, i, v)
