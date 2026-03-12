import os
from .user import User


# Johnathin Fooks
def clear_terminal():
    # Check if the operating system is Windows ('nt') or Posix (Linux, macOS, Unix)
    if os.name == 'nt':
        # Command for Windows
        os.system('cls') 
    else:
        # Command for Linux, macOS, etc.
        os.system('clear')



# Johnathin Fooks
def p_err(file: str, func: str, msg: str, crash: bool):
    print("\n[[ Use 'help' for help to use the tool ]]\n")
    print(f"[ERROR]({file})({func}): {msg} ")
    if crash:
        print("Critical error. Exiting.")
        exit()
    else:
        return



# Vincent Le
def save_output(lst:list[User], filename:str) -> None:
    with open(f"results/{filename}.txt", "w") as f:
        for obj in lst:
            f.write(repr(obj))
        f.write(f"\n===== FLAGGED USERS =====\n") 
        for name in show_flagged_users(lst):
            f.write(name + "\n")
        if len(show_flagged_users(lst)) < 1:
            f.write("NO FLAGGED USERS\n")

# Vincent Le
def show_flagged_users(lst:list[User]) -> list[str]:
    bad_list = []
    for user in lst:
        if user.malicious_flag:
            s = f"{user.id}  :  {user.name}"
            bad_list.append(s)
    return bad_list
