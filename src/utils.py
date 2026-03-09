import os
import sys
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

def save_output(func, file: str = "output.txt", *args, **kwargs):

    original = sys.stdout

    try:
        with open(f"analysis_res/{file}", 'w') as f:
            sys.stdout = f
            result = func(*args, **kwargs)

    finally:
        sys.stdout = original
    print(f"Output saved to {file}")
    return result


