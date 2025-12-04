# UA1015 - Testcase Generator for Age 5 Years Later
import os

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
os.makedirs(test_dir, exist_ok=True)

def write_test(idx, age):
    in_path = os.path.join(test_dir, f"1-{idx}.in")
    out_path = os.path.join(test_dir, f"1-{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{age}\n")
    later = age + 5
    with open(out_path, 'w') as fout:
        fout.write(f"5 years later I will be {later} years old.\n")

# Sample cases
write_test(1, 5)
write_test(2, 12)
write_test(3, 0)

# Edge cases
write_test(4, -5)
write_test(5, 100)

# Random cases
import random
for i in range(6, 11):
    age = random.randint(-20, 120)
    write_test(i, age)
