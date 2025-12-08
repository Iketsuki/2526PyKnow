import os

def gen_case(i, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    arr = [10, 20, 30, 40, 50]
    with open(in_path, 'w') as fin:
        fin.write(f"{i}\n")
    with open(out_path, 'w') as fout:
        fout.write(f"{arr[i]}\n")

def main():
    for i in range(5):
        gen_case(i, f"1-{i+1}")

if __name__ == "__main__":
    main()
