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
dataset_menu =  '''
List of datasets
'''

flagged_users = '''
    ================================================
                    Flagged Users
    ================================================
        {list_flagged}

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

        case '1':
            print()
        case '2':
            print(dataset_menu)
        case '3':
            print(flagged_users)
        case _:
            last_command = f"Incorrect Input: {user_input}"


