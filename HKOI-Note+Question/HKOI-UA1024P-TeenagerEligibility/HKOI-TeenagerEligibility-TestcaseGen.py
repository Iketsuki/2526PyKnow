import os
import random

def gen_case(a, e, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{a}\n{e}\n")
    with open(out_path, 'w') as fout:
        if 13 <= a <= 19 and e == 'True':
            fout.write("Teenager and eligible\n")
        else:
            fout.write("Not both\n")

def main():
    # Sample cases
    gen_case(15, 'True', '1-1')
    gen_case(12, 'True', '1-2')
    gen_case(17, 'False', '1-3')
    # Random cases
    for i in range(4, 11):
        a = random.randint(0, 100)
        e = random.choice(['True', 'False'])
        gen_case(a, e, f"1-{i}")

if __name__ == "__main__":
    main()
