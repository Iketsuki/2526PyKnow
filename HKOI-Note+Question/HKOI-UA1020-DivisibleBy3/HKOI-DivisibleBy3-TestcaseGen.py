import os

def gen_case(n, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{n}\n")
    with open(out_path, 'w') as fout:
        if n % 3 == 0:
            fout.write("3\n")
        else:
            fout.write("")

def main():
    gen_case(9, '1-1')
    gen_case(8, '1-2')
    gen_case(0, '1-3')
    gen_case(-3, '1-4')
    gen_case(7, '1-5')

if __name__ == "__main__":
    main()
