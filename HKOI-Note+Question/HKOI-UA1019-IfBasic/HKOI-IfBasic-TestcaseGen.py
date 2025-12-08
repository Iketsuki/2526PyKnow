import os

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
        else:
            fout.write("")

def main():
    # Boundary and edge cases
    gen_case(0, '1-1')        # zero
    gen_case(1, '1-2')        # just above zero
    gen_case(-1, '1-3')       # just below zero
    gen_case(1000, '1-4')     # max
    gen_case(-1000, '1-5')    # min
    # Random cases
    import random
    for i in range(6, 11):
        n = random.randint(-1000, 1000)
        gen_case(n, f"1-{i}")

if __name__ == "__main__":
    main()
