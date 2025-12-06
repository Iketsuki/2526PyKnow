import os

def gen_case(n, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{n}\n")
    with open(out_path, 'w') as fout:
        if n % 2 == 0:
            fout.write("Even\n")
        else:
            fout.write("Odd\n")

def main():
    # Sample cases
    gen_case(4, '1-1')
    gen_case(7, '1-2')
    # Random cases
    import random
    for i in range(3, 11):
        n = random.randint(-1000, 1000)
        gen_case(n, f"1-{i}")

if __name__ == "__main__":
    main()
