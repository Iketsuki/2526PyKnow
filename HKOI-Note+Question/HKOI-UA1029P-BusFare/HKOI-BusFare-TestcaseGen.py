import os
import random

def gen_case(a, d, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{a}\n{d}\n")
    if a < 12:
        fare = d * 0.5
    elif a >= 65:
        fare = d * 0.7
    else:
        fare = d * 1.0
    with open(out_path, 'w') as fout:
        fout.write(f"{fare}\n")

def main():
    # Boundary and edge cases
    gen_case(0, 0.01, '1-1')      # min age, min distance
    gen_case(11, 100, '1-2')      # just below age threshold, max distance
    gen_case(12, 50, '1-3')       # at age threshold
    gen_case(64, 100, '1-4')      # just below senior
    gen_case(65, 100, '1-5')      # senior, max distance
    gen_case(120, 100, '1-6')     # max age, max distance
    # Random cases
    for i in range(7, 21):
        a = random.randint(0, 120)
        d = round(random.uniform(0.01, 100), 2)
        gen_case(a, d, f"1-{i}")

if __name__ == "__main__":
    main()
