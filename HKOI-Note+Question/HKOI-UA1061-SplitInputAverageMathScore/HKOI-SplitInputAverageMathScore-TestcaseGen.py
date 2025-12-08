import os
import random

def gen_case(n, arr, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{n}\n")
        fin.write(' '.join(map(str, arr)) + '\n')
    with open(out_path, 'w') as fout:
        avg = sum(arr) / len(arr)
        fout.write(f"{avg}\n")

def main():
    # Boundary and edge cases
    gen_case(1, [100], "1-1")      # min n, max score
    gen_case(1, [1], "1-2")        # min n, min score
    gen_case(100, [100]*100, "1-3") # max n, all max
    gen_case(100, [1]*100, "1-4")   # max n, all min
    gen_case(3, [80,90,100], "1-5") # sample
    gen_case(2, [50,100], "1-6")    # sample
    # Random cases
    for i in range(7, 16):
        n = random.randint(1, 100)
        arr = [random.randint(1,100) for _ in range(n)]
        gen_case(n, arr, f"1-{i}")

if __name__ == "__main__":
    main()
