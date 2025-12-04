# UA1016P - Testcase Generator for Triangle Area Calculation
import os

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
os.makedirs(test_dir, exist_ok=True)

def write_test(idx, base, height):
    in_path = os.path.join(test_dir, f"1-{idx}.in")
    out_path = os.path.join(test_dir, f"1-{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{base}\n{height}\n")
    area = base * height / 2
    with open(out_path, 'w') as fout:
        fout.write("What is the base of the triangle?\n")
        fout.write("What is the height of the triangle?\n")
        fout.write(f"The area of the triangle is {area}\n")

# Sample cases
write_test(1, 10, 5)
write_test(2, 3.5, 2)

# Edge cases
write_test(3, 0.1, 0.1)
write_test(4, 1000, 1000)

# Random cases
import random
for i in range(5, 11):
    base = round(random.uniform(0.1, 1000), 2)
    height = round(random.uniform(0.1, 1000), 2)
    write_test(i, base, height)
