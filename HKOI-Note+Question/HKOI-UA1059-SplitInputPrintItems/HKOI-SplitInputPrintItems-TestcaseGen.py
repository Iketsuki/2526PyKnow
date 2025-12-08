import os

def gen_case(n, arr, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{n}\n")
        fin.write(' '.join(arr) + '\n')
    with open(out_path, 'w') as fout:
        for x in arr:
            fout.write(f"{x}\n")
        fout.write(f"{len(arr)}\n")

def main():
    cases = [
        (3, ["cat", "dog", "bird"], "1-1"),
        (2, ["apple", "banana"], "1-2"),
        (1, ["fish"], "1-3"),
        (4, ["a", "b", "c", "d"], "1-4"),
        (5, ["one", "two", "three", "four", "five"], "1-5"),
    ]
    for n, arr, idx in cases:
        gen_case(n, arr, idx)

if __name__ == "__main__":
    main()
