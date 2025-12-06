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
        if n > 0:
            fout.write("Positive\n")
        elif n < 0:
            fout.write("Negative\n")
        else:
            fout.write("Zero\n")

def main():
    # Sample cases
    gen_case(5, '1-1')
    gen_case(-3, '1-2')
    gen_case(0, '1-3')
    # Random cases
    for i in range(4, 11):
        n = random.randint(-1000, 1000)
        gen_case(n, f"1-{i}")

if __name__ == "__main__":
    main()
