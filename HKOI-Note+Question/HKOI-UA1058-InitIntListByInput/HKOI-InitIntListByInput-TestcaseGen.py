import os

def gen_case(n, arr, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{n}\n")
        for num in arr:
            fin.write(f"{num}\n")
    with open(out_path, 'w') as fout:
        fout.write(f"{arr}\n")

def main():
    cases = [
        (3, [1, 2, 3], "1-1"),
        (2, [10, 20], "1-2"),
        (1, [42], "1-3"),
        (4, [7, 8, 9, 10], "1-4"),
        (5, [100, 200, 300, 400, 500], "1-5"),
    ]
    for n, arr, idx in cases:
        gen_case(n, arr, idx)

if __name__ == "__main__":
    main()
