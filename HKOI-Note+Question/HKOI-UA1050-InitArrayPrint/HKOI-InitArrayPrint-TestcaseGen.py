import os

def gen_case(idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write("")  # No input
    with open(out_path, 'w') as fout:
        fout.write("[1, 2, 3, 4, 5]\n")

def main():
    for i in range(1, 6):
        gen_case(f"1-{i}")

if __name__ == "__main__":
    main()
