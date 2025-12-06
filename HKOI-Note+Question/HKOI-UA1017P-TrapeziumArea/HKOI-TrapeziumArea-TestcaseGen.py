import os
import random

def gen_case(a, b, h, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{a}\n{b}\n{h}\n")
    area = 0.5 * (a + b) * h
    with open(out_path, 'w') as fout:
        fout.write(f"The area of the trapezium is {area}\n")

def main():
    # Sample cases
    gen_case(10, 6, 5, '1-1')
    gen_case(3.5, 2.5, 4, '1-2')
    # Random cases
    for i in range(3, 11):
        a = round(random.uniform(0.1, 1000), 2)
        b = round(random.uniform(0.1, 1000), 2)
        h = round(random.uniform(0.1, 1000), 2)
        gen_case(a, b, h, f"1-{i}")

if __name__ == "__main__":
    main()
