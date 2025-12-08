import os
import random

def gen_case(n, k, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    count = sum(1 for i in range(1, n+1) if i % k == 0)
    with open(in_path, 'w') as fin:
        fin.write(f"{n}\n{k}\n")
    with open(out_path, 'w') as fout:
        fout.write(f"{count}\n")

def main():
    # Boundary and edge cases
    gen_case(1, 1, '1-1')      # min
    gen_case(100, 1, '1-2')    # max n, k=1
    gen_case(100, 100, '1-3')  # max n, k=max
    gen_case(2, 2, '1-4')      # just above min
    gen_case(99, 3, '1-5')     # just below max
    # Random cases
    for i in range(6, 21):
        n = random.randint(1, 100)
        k = random.randint(1, n)
        gen_case(n, k, f"1-{i}")

if __name__ == "__main__":
    main()
