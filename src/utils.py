import os
from .user import User
import json



def clear_terminal():
    # Check if the operating system is Windows ('nt') or Posix (Linux, macOS, Unix)
    if os.name == 'nt':
        # Command for Windows
        os.system('cls') 
    else:
        # Command for Linux, macOS, etc.
        os.system('clear')



def p_err(file: str, func: str, msg: str, crash: bool):
    print("\n[[ Use 'help' for help to use the tool ]]\n")
    print(f"[ERROR]({file})({func}): {msg} ")
    if crash:
        print("Critical error. Exiting.")
        exit()
    else:
        return



def save_output(lst:list[User], filename:str) -> None:
    with open(f"results/{filename}.txt", "w") as f:
        for obj in lst:
            f.write(repr(obj))
        f.write(f"\nList of malicious users:\n") 
        for name in show_bad_users(lst):
            f.write(name + "\n")



def show_bad_users(lst:list[User]) -> list[str]:
    bad_list = []
    for user in lst:
        if user.malicious_flag:
            bad_list.append(user.name)
    return bad_list

