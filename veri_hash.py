# VeriHash: A simple hash comparison tool

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def vh():
    hash1 = input("Enter first hash: ")
    hash2 = input("Enter second hash: ")
    if hash1 == hash2:
        print(green("The hashes match!")) # Output if hashes match
    else:
        print(red("The hashes do not match.")) # Output if hashes do not match
