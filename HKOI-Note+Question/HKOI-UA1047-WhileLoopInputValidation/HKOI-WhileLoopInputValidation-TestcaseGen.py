import os
import random

def gen_case(inputs, idx):
    case_dir = os.path.join(os.path.dirname(__file__), 'tests')
    os.makedirs(case_dir, exist_ok=True)
    in_path = os.path.join(case_dir, f"{idx}.in")
    out_path = os.path.join(case_dir, f"{idx}.out")
    with open(in_path, 'w') as fin:
        for val in inputs:
            fin.write(f"{val}\n")
    with open(out_path, 'w') as fout:
        for val in inputs:
            if 1 <= val <= 100:
                fout.write(f"Accepted: {val}\n")
                break
            else:
                fout.write("Invalid input. Try again.\n")

def main():
    # Boundary and edge cases
    gen_case([-1, 1], '1-1')      # min after invalid
    gen_case([101, 100], '1-2')   # max after invalid
    gen_case([0, 50], '1-3')      # random valid after invalid
    gen_case([100], '1-4')        # valid first try
    gen_case([1], '1-5')          # valid first try
    # Random cases
    for i in range(6, 16):
        valid = random.randint(1, 100)
        invalids = [random.randint(-100, 0), random.randint(101, 200)]
        inputs = invalids + [valid]
        random.shuffle(inputs)
        # Ensure at least one valid at end
        if not (1 <= inputs[-1] <= 100):
            inputs[-1] = valid
        gen_case(inputs, f"1-{i}")

if __name__ == "__main__":
    main()
