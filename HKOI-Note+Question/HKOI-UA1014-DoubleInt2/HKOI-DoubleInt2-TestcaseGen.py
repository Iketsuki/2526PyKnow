# UA1014 - Testcase Generator for Double the Integer
import os

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
os.makedirs(test_dir, exist_ok=True)

def write_test(idx, x):
    in_path = os.path.join(test_dir, f"1-{idx}.in")
    out_path = os.path.join(test_dir, f"1-{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{x}\n")
    result = x * 2
    with open(out_path, 'w') as fout:
        fout.write(f"{x}*2={result}\n")

# Sample cases
write_test(1, 5)
write_test(2, -7)
write_test(3, 0)

# Edge cases
write_test(4, 1)
write_test(5, -1)
write_test(6, 99999)
write_test(7, -99999)

# Random cases
import random
for i in range(8, 11):
    x = random.randint(-100000, 100000)
    write_test(i, x)
