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
        i = 1
        while i * i <= n:
            sq = i * i
            if sq % 4 == 0:
                fout.write("clap\n")
            else:
                fout.write(f"{sq}\n")
            i += 1

def main():
    # Boundary and edge cases
    gen_case(1, '1-1')      # min
    gen_case(1000, '1-2')   # max
    gen_case(4, '1-3')      # first clap
    gen_case(16, '1-4')     # multiple claps
    gen_case(9, '1-5')      # no clap except 4
    # Random cases
    for i in range(6, 16):
        n = random.randint(1, 1000)
        gen_case(n, f"1-{i}")

if __name__ == "__main__":
    main()
