from src.utils import p_err, populate

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

def handle_operations(argv_l: list) -> int:

    match argv_l[1]:

        case "help":
            op_help()

        case "info":
            op_info()

        case "users":
            try:
                op_dangerous_users(int(argv_l[2]))
            except:
                p_err("operations", "handle_operations", "")


    return 0

def op_help() -> int:

    try:
        print(help_s)

    except:
        p_err("operations", "op_help", "")
        return 1

    return 0

def op_info() -> int:

    try:
        print(info_s)

    except:
        p_err("operations", "op_info", "")
        return 1

    return 0

def op_dangerous_users(inp: int) -> int:
    name = input("Name of dataset: ")
    data = populate()
    print(data)

