# TransHash: A simple script to hash a user-provided password using SHA-256.
import hashlib
import time
import os

user_input = input("What is your password?: ")  # Input from user

hash = ""

if user_input:
    hash = hashlib.sha256(user_input.encode()).hexdigest()  # Generate SHA-256 hash
    time.sleep(3)
    print("Hashing your password... Please wait")
    time.sleep(1)
    os.system("clear")
    print("Hashing your password... Please wait.")
    time.sleep(1)
    os.system("clear")
    print("Hashing your password... Please wait..")
    time.sleep(1)
    os.system("clear")
    print("Hashing your password... Please wait...")
    time.sleep(1)
    os.system("clear")

    print(f"Your password has been hashed as {hash}")
    