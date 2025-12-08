import os
import random

def gen_case(n, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{n}\n")
    with open(out_path, 'w') as fout:
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                fout.write("FizzBuzz\n")
            elif i % 3 == 0:
                fout.write("Fizz\n")
            elif i % 5 == 0:
                fout.write("Buzz\n")
            else:
                fout.write(f"{i}\n")

def main():
    # Boundary and edge cases
    gen_case(1, '1-1')      # min
    gen_case(100, '1-2')    # max
    gen_case(3, '1-3')      # first Fizz
    gen_case(5, '1-4')      # first Buzz
    gen_case(15, '1-5')     # first FizzBuzz
    gen_case(99, '1-6')     # just below max
    # Random cases
    for i in range(7, 21):
        n = random.randint(1, 100)
        gen_case(n, f"1-{i}")

if __name__ == "__main__":
    main()
