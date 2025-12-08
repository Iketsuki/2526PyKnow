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
        for _ in range(n):
            fout.write("Hello World\n")

def main():
    # Boundary and edge cases
    gen_case(1, '1-1')      # min
    gen_case(100, '1-2')    # max
    gen_case(2, '1-3')      # just above min
    gen_case(99, '1-4')     # just below max
    # Random cases
    for i in range(5, 16):
        n = random.randint(1, 100)
        gen_case(n, f"1-{i}")

if __name__ == "__main__":
    main()
