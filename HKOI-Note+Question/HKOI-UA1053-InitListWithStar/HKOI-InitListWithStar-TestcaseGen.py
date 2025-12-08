import os

def gen_case(n, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{n}\n")
    with open(out_path, 'w') as fout:
        fout.write(f"{[0]*n}\n")

def main():
    for n, idx in [(1, "1-1"), (5, "1-2"), (10, "1-3"), (100, "1-4")]:
        gen_case(n, idx)

if __name__ == "__main__":
    main()
