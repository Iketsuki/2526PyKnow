import os

def gen_case(arr, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(' '.join(map(str, arr)) + '\n')
    with open(out_path, 'w') as fout:
        fout.write(f"{len(arr)}\n")

def main():
    cases = [
        ([1, 2, 3, 4, 5], "1-1"),
        ([10, 20, 30], "1-2"),
        ([7], "1-3"),
        ([100, 200, 300, 400, 500, 600], "1-4"),
        ([42, 43, 44, 45, 46, 47, 48, 49, 50], "1-5"),
    ]
    for arr, idx in cases:
        gen_case(arr, idx)

if __name__ == "__main__":
    main()
