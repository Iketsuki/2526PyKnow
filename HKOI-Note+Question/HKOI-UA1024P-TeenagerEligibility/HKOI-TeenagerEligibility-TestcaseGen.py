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
    # Boundary and edge cases
    gen_case(13, 'True', '1-1')      # lower bound, eligible
    gen_case(19, 'True', '1-2')      # upper bound, eligible
    gen_case(12, 'True', '1-3')      # just below lower, eligible
    gen_case(20, 'True', '1-4')      # just above upper, eligible
    gen_case(13, 'False', '1-5')     # lower bound, not eligible
    gen_case(19, 'False', '1-6')     # upper bound, not eligible
    gen_case(0, 'True', '1-7')       # min age, eligible
    gen_case(100, 'True', '1-8')     # max age, eligible
    # Random cases
    import random
    for i in range(9, 11):
        a = random.randint(0, 100)
        e = random.choice(['True', 'False'])
        gen_case(a, e, f"1-{i}")

if __name__ == "__main__":
    main()
