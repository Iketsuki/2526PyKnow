import os
import random

def gen_case(a, d, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{a}\n{d}\n")
    with open(out_path, 'w') as fout:
        if a >= 65 or d == 'True':
            fout.write("Eligible for 2 dollar ticket\n")
        else:
            fout.write("Regular ticket\n")

def main():
    # Boundary and edge cases
    gen_case(65, 'False', '1-1')      # lower bound age
    gen_case(64, 'False', '1-2')      # just below age
    gen_case(65, 'True', '1-3')       # lower bound age, has card
    gen_case(0, 'True', '1-4')        # min age, has card
    gen_case(120, 'False', '1-5')     # max age
    gen_case(120, 'True', '1-6')      # max age, has card
    gen_case(0, 'False', '1-7')       # min age, no card
    # Random cases
    for i in range(8, 21):
        a = random.randint(0, 120)
        d = random.choice(['True', 'False'])
        gen_case(a, d, f"1-{i}")

if __name__ == "__main__":
    main()
