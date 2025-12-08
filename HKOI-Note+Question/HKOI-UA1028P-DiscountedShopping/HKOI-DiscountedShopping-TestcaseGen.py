import os
import random

def gen_case(p, d, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{p}\n{d}\n")
    final = p * (1 - d / 100)
    with open(out_path, 'w') as fout:
        if final > 500:
            final = final * 0.9
            fout.write(f"{final}\n")
        else:
            fout.write("No extra discount\n")
            fout.write(f"{final}\n")

def main():
    # Boundary and edge cases
    gen_case(10000, 0, '1-1')      # max price, no discount
    gen_case(10000, 99, '1-2')     # max price, max discount
    gen_case(0.01, 0, '1-3')       # min price, no discount
    gen_case(0.01, 98, '1-4')      # min price, high discount
    gen_case(500, 0, '1-5')        # price at threshold
    gen_case(500, 1, '1-6')        # just above threshold
    gen_case(499.99, 0, '1-7')     # just below threshold
    # Random cases
    for i in range(8, 21):
        p = round(random.uniform(0.01, 10000), 2)
        d = random.randint(0, 99)
        gen_case(p, d, f"1-{i}")

if __name__ == "__main__":
    main()
