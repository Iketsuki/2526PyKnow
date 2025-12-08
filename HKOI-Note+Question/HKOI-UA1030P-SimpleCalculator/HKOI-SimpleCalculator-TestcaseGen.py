import os
import random

def gen_case(a, b, op, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{a}\n{b}\n{op}\n")
    with open(out_path, 'w') as fout:
        if op == 'add':
            fout.write(f"{a + b}\n")
        elif op == 'sub':
            fout.write(f"{a - b}\n")
        elif op == 'mul':
            fout.write(f"{a * b}\n")
        elif op == 'div':
            fout.write(f"{a / b}\n")

def main():
    # Boundary and edge cases
    gen_case(10000, 10000, 'add', '1-1')
    gen_case(-10000, -10000, 'add', '1-2')
    gen_case(10000, -10000, 'sub', '1-3')
    gen_case(0, 10000, 'mul', '1-4')
    gen_case(10000, 1, 'div', '1-5')
    gen_case(-10000, 1, 'div', '1-6')
    gen_case(0, 1, 'div', '1-7')
    # Random cases
    ops = ['add', 'sub', 'mul', 'div']
    for i in range(8, 31):
        a = round(random.uniform(-10000, 10000), 2)
        b = round(random.uniform(-10000, 10000), 2)
        op = random.choice(ops)
        if op == 'div' and b == 0:
            b = 1  # avoid division by zero
        gen_case(a, b, op, f"1-{i}")

if __name__ == "__main__":
    main()
