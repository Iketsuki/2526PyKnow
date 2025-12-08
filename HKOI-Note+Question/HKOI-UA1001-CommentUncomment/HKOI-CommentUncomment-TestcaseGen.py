import os

def gen_case(idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write("")
    with open(out_path, 'w') as fout:
        fout.write("Hello\nI am anna\nI am 10 years old\n")

def main():
    gen_case('1-1')

if __name__ == "__main__":
    main()
