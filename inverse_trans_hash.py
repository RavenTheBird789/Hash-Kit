# InverseTransHash: A simple brute-force tool to reverse SHA-256 hashes for short alphanumeric strings.
import hashlib
import itertools
import string

target_hash = input("Enter the hash to reverse: ")

# Use lowercase letters and digits for brute force (to keep it manageable)
chars = string.ascii_lowercase + string.digits

found = False

# Try lengths from 1 to 4 (adjust as needed for longer searches)
for length in range(1, 4):
    print(f"Checking length {length}...")
    for combo in itertools.product(chars, repeat=length):
        s = ''.join(combo)
        if hashlib.sha256(s.encode()).hexdigest() == target_hash:
            print(f"Found original string: {s}")
            found = True
            break
    if found:
        break

if not found:
    print("Original string not found in the searched space (short alphanumeric strings).")