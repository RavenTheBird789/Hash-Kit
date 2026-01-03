# Hast-Tool-Kit UI

import trans_hash 
import inverse_trans_hash 
import veri_hash 
import os
import time

def blue(text: str) -> str:
    return f"\033[94m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

def user_prompt():
    prompt = input(blue("Would you like to return to the main menu? (yes/no): "))
    if prompt.lower() in ['yes', 'y']:
        os.system('clear')
        display_menu()
    elif prompt.upper() in ['YES', 'Y']:
        os.system('clear')
        display_menu()
    elif prompt == 'Yes':
        os.system('clear')
        display_menu()
    else:
        os.system('clear')
        print(blue("Thank you for using my Hast-Tool-Kit! Goodbye!"))
        os.close(fd=0)

def display_menu():
    print(bold(blue("Hash-Tool-Kit UI")))
    print(blue("=================="))
    print(bold(red("By: RavenTheBird789")))
    print(blue("=================="))
    print(blue("1. Hash a string"))
    print(blue("2. Inverse hash a string"))
    print(blue("3. Verify a hash"))
    print(blue("4. Exit"))
    choice = input(blue("Select an option (1-4): "))
    if choice == '1':
        trans_hash.th();
        time.sleep(2);
        user_prompt();
        os.system('clear');
    elif choice == '2':
        inverse_trans_hash.ith();
        time.sleep(2);
        user_prompt();
        os.system('clear');
    elif choice == '3':
        veri_hash.vh();
        time.sleep(2);
        user_prompt();
        os.system('clear');
    elif choice == '4':
        os.system('clear');
        print(blue("Thank you for using my Hash-Tool-Kit! Goodbye!"));
        time.sleep(5)
        os.system('clear');
        os.close(fd=0);
display_menu();