# UB1001P - Testcase Generator for List Indexing (1-based)
import os

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
os.makedirs(test_dir, exist_ok=True)

def write_test(idx, items, i):
    in_path = os.path.join(test_dir, f"1-{idx}.in")
    out_path = os.path.join(test_dir, f"1-{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{len(items)}\n")
        for item in items:
            fin.write(f"{item}\n")
        fin.write(f"{i}\n")
    with open(out_path, 'w') as fout:
        fout.write(f"{items[i-1]}\n")

# Sample cases
write_test(1, ["apple", "banana", "cherry"], 2)
write_test(2, ["one", "two", "three", "four", "five"], 5)

# Edge cases
write_test(3, ["a"], 1)
write_test(4, ["x", "y"], 1)
write_test(5, ["x", "y"], 2)

# Random cases
import random
import string
for idx in range(6, 11):
    n = random.randint(2, 8)
    items = [''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 6))) for _ in range(n)]
    i = random.randint(1, n)
    write_test(idx, items, i)
