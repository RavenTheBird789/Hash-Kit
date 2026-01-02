# InverseTransHash: A simple brute-force tool to reverse SHA-256 hashes for short alphanumeric strings.
import hashlib
import itertools
import string

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def ith():
    target_hash = input("Enter the hash to reverse: ")
    # Use letters and digits for brute force
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits 

    found = False
    # Try lengths from 1 to 4 (adjust as needed for longer searches)
    for length in range(1, 4):
        print(f"Checking length {length}...")
        for combo in itertools.product(chars, repeat=length):
            s = ''.join(combo)
            if hashlib.sha256(s.encode()).hexdigest() == target_hash:
                print(green(f"Found original string: {s}")) # Output the found string
                found = True
                break
        if found:
            break

    if not found:
        print(red("Original string not found in the searched space (short alphanumeric strings).")) # Output if not found
