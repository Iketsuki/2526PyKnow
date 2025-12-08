import os

def gen_case(i, w, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    arr = ["cat", "dog", "bird", "fish", "ant"]
    arr[i] = w
    with open(in_path, 'w') as fin:
        fin.write(f"{i}\n{w}\n")
    with open(out_path, 'w') as fout:
        fout.write(f"{arr}\n")

def main():
    cases = [
        (2, "parrot", "1-1"),
        (0, "lion", "1-2"),
        (4, "bee", "1-3"),
        (1, "wolf", "1-4"),
        (3, "shark", "1-5"),
    ]
    for i, w, idx in cases:
        gen_case(i, w, idx)

if __name__ == "__main__":
    main()
