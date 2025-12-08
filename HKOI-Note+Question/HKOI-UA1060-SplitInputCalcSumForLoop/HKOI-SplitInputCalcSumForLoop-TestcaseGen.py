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
        fout.write(f"{sum(arr)}\n")

def main():
    # Boundary and edge cases
    gen_case(1, [0], "1-1")      # min n, min value
    gen_case(1, [2], "1-2")      # min n, max value
    gen_case(100, [0]*100, "1-3") # max n, all min
    gen_case(100, [2]*100, "1-4") # max n, all max
    gen_case(5, [2,2,2,2,2], "1-5") # all max small n
    gen_case(5, [0,0,0,0,0], "1-6") # all min small n
    gen_case(3, [1,2,0], "1-7") # sample
    # Random cases
    for i in range(8, 16):
        n = random.randint(1, 100)
        arr = [random.randint(0,2) for _ in range(n)]
        gen_case(n, arr, f"1-{i}")

if __name__ == "__main__":
    main()
