# UA1011 - Testcase Generator for Round to Thousandths
import random
import os

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
os.makedirs(test_dir, exist_ok=True)

def write_test(idx, value):
    in_path = os.path.join(test_dir, f"1-{idx}.in")
    out_path = os.path.join(test_dir, f"1-{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{value}\n")
    rounded = round(float(value), 3)
    with open(out_path, 'w') as fout:
        fout.write(f"{rounded:.3f}\n")

# Sample cases
write_test(1, 3.1415926)
write_test(2, 2.0)
write_test(3, -0.12345)

# Min/max cases
write_test(4, -1000.0)
write_test(5, 1000.0)

# Random cases
for i in range(6, 11):
    value = random.uniform(-1000.0, 1000.0)
    write_test(i, value)
