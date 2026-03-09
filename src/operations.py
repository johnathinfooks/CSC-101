import os

from src.utils import *
from src.analysis import *



help_s = '''
    Valid input:

    help - access help information
    info - access general information
    users - show all users that are flagged as dangerous according to prompted score
'''

info_s = '''
    ================================================
    Dangerous Activity Message Analysis Tool
    ================================================

    By Johnathin Fooks and Vincent Le
    California Polytechnic State University, CSC-101
'''



def handle_operations(argv_l: list, ROOT_DIR) -> None:

    if len(argv_l) < 2:
        print("use 'help' for help to use tool")
        exit()

    try:
        match argv_l[1]:

            case None:
                print("use 'help' for help to use tool")

            case "help":
                op_help()

            case "info":
                op_info()

            case "users":
                op_dangerous_users(argv_l[2], ROOT_DIR)

    except Exception as e:
        p_err("operations", "handle_operations", str(e), True)



def op_help() -> None:

    try:
        print(help_s)

    except:
        p_err("operations", "op_help", "", False)



def op_info() -> None:

    try:
        print(info_s)

    except:
        p_err("operations", "op_info", "", False)



def op_dangerous_users(inp: str, ROOT_DIR) -> None:
    try:
        # name = input("Name of dataset: ")
        data_path = os.path.join(ROOT_DIR, f"data/dataSets/{inp}")
        analysis(populate(data_path))

    except Exception as e:
        p_err("operations", "op_dangerous_user", str(e), False)
