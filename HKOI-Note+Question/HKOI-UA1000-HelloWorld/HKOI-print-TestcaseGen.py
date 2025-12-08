import os

if not os.path.exists('tests'):
    os.makedirs('tests')

def solve():
    """The solution is to return "Hello World"."""
    return "Hello World"

# Generate 10 identical test cases (since there is no input variation)
NUM_TESTS = 10

for i in range(1, NUM_TESTS + 1):
    output_str = solve()
    
    # Write empty input (no input needed for this task)
    with open(f'tests/1-{i}.in', 'w') as f:
        f.write('')
    
    # Write output "Hello World" with newline
    with open(f'tests/1-{i}.out', 'w') as f:
        f.write(output_str + '\n')

print(f"Generated {NUM_TESTS} test cases in /tests folder.")
