import os
import random

def gen_case(a, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{a}\n")
    with open(out_path, 'w') as fout:
        if a < 13:
            fout.write("Child\n")
        elif a <= 19:
            fout.write("Teenager\n")
        elif a <= 64:
            fout.write("Adult\n")
        else:
            fout.write("Senior\n")

def main():
    # Boundary and edge cases
    gen_case(0, '1-1')      # min age
    gen_case(12, '1-2')     # just below teenager
    gen_case(13, '1-3')     # lower bound teenager
    gen_case(19, '1-4')     # upper bound teenager
    gen_case(20, '1-5')     # lower bound adult
    gen_case(64, '1-6')     # upper bound adult
    gen_case(65, '1-7')     # lower bound senior
    gen_case(120, '1-8')    # max age
    # Random cases
    for i in range(9, 11):
        a = random.randint(0, 120)
        gen_case(a, f"1-{i}")

if __name__ == "__main__":
    main()
