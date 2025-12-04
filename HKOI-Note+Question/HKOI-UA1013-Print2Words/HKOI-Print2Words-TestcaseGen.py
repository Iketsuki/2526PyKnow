# UA1013 - Testcase Generator for Print Two Words
import os

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
os.makedirs(test_dir, exist_ok=True)

def write_test(idx, word1, word2):
    in_path = os.path.join(test_dir, f"1-{idx}.in")
    out_path = os.path.join(test_dir, f"1-{idx}.out")
    with open(in_path, 'w') as fin:
        fin.write(f"{word1}\n{word2}\n")
    with open(out_path, 'w') as fout:
        fout.write(f"{word1}{word2}\n{word1} {word2}\n")

# Sample cases
write_test(1, "Hello", "world")
write_test(2, "Python", "Rocks")

# Edge cases
write_test(3, "A", "B")
write_test(4, "", "Empty")
write_test(5, "Space", " ")

# Random cases
import random
import string
for i in range(6, 11):
    w1 = ''.join(random.choices(string.ascii_letters, k=random.randint(1, 8)))
    w2 = ''.join(random.choices(string.ascii_letters, k=random.randint(1, 8)))
    write_test(i, w1, w2)
