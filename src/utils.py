import os
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
    print(f"[ERROR]({file})({func}): {msg} ")
    if crash:
        print("Critical error. Exiting.")
        exit()
    else:
        return


