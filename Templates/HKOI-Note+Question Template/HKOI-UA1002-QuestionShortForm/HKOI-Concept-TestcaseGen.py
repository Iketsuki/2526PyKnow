import random
import os
import string

if not os.path.exists('tests'):
    os.makedirs('tests')

def generate_word(length):
    """Generates a random word with specified length."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def solve(w):
    """The simple solution is to return the word itself."""
    return w

# Constraints
MIN_LEN = 1
MAX_LEN = 10
NUM_TESTS = 10

# List of words to use for testing
test_words = [
    # Boundary Case 1: Minimum length (1)
    generate_word(MIN_LEN),
    # Boundary Case 2: Maximum length (10)
    generate_word(MAX_LEN),
    # Case 3-10: Random lengths
    generate_word(random.randint(MIN_LEN + 1, MAX_LEN - 1)),
    generate_word(random.randint(MIN_LEN, MAX_LEN)),
    generate_word(random.randint(MIN_LEN, MAX_LEN)),
    generate_word(random.randint(MIN_LEN + 1, MAX_LEN - 1)),
    generate_word(random.randint(MIN_LEN, MAX_LEN)),
    generate_word(random.randint(MIN_LEN, MAX_LEN)),
    generate_word(random.randint(MIN_LEN + 1, MAX_LEN - 1)),
    generate_word(random.randint(MIN_LEN, MAX_LEN)),
]

for i in range(1, NUM_TESTS + 1):
    w = test_words[i-1]
    
    input_str = w
    output_str = solve(w)
    
    # Write input to 1-i.in
    # [cite_start]Note: No trailing whitespace, and the line contains the end-of-line character [cite: 97, 131]
    with open(f'tests/1-{i}.in', 'w') as f:
        f.write(input_str + '\n')
    
    # Write output to 1-i.out
    with open(f'tests/1-{i}.out', 'w') as f:
        f.write(output_str + '\n')

print(f"Generated {NUM_TESTS} test cases in /tests folder.")
