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

