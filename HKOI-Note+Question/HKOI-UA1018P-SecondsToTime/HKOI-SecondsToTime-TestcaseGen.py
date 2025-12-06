import os
import random

def gen_case(n, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{n}\n")
    h = n // 3600
    m = (n % 3600) // 60
    s = n % 60
    with open(out_path, 'w') as fout:
        fout.write(f"{h}:{m}:{s}\n")

def main():
    # Sample cases
    gen_case(3661, '1-1')
    gen_case(59, '1-2')
    # Random cases
    for i in range(3, 11):
        n = random.randint(0, 100000)
        gen_case(n, f"1-{i}")

if __name__ == "__main__":
    main()
