import os
import random

def gen_case(n, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{n}\n")
    with open(out_path, 'w') as fout:
        if 10 <= n <= 20:
            fout.write("In range\n")
        else:
            fout.write("Out of range\n")

def main():
    # Sample cases
    gen_case(15, '1-1')
    gen_case(9, '1-2')
    gen_case(20, '1-3')
    # Random cases
    for i in range(4, 11):
        n = random.randint(-1000, 1000)
        gen_case(n, f"1-{i}")

if __name__ == "__main__":
    main()
