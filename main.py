from src.user import *
from src.message import *
from src.utils import *

opening_string = '''
    ================================================
    Dangerous Activity, Analysis, and Flagging Tool
    ================================================

    Input number for functionality:

    1 - Help and information
    2 - Select dataset and perform analysis
    3 - View flagged users

    0 - Exit
'''

# runtime loop

last_command = ""

while (True):

    # clear terminal interface
    clear_terminal()

    # print interface string
    print(opening_string)

    # show last command
    print(last_command + "\n")

    # listen for user input
    user_input = input()

    # switch statement matching it to handlers
    match user_input:
        case '0':
            print("Exit")
            exit()

        case _:
            last_command = f"Incorrect Input: {user_input}"


