import os

from src.utils import *
from src.analysis import *



help_s = '''
    Valid input:

    help - access help information
    info - access general information
    analysis <dataset name> <max dangerous> <output file name> - show all users that are flagged as dangerous according to prompted value
    '''

info_s = '''
    ================================================
    Dangerous Activity Message Analysis Tool
    ================================================

    By Johnathin Fooks and Vincent Le
    California Polytechnic State University, CSC-101
'''



def handle_operations(argv_l: list, ROOT_DIR) -> None:

    try:
        match argv_l[1]:

            case "help":
                if len(argv_l) != 2:
                    raise Exception
                op_help()

            case "info":
                if len(argv_l) != 2:
                    raise Exception
                op_info()

            case "analysis":
                if len(argv_l) != 5:
                    raise Exception
                op_full_analysis(argv_l[2], int(argv_l[3]), argv_l[4], ROOT_DIR)

            case _:
                raise Exception

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



def op_full_analysis(dataset_name: str, amt_dng_wds_for_flag: int, filename:str, ROOT_DIR) -> None:

    try:
        data_path = os.path.join(ROOT_DIR, f"data/dataSets/{dataset_name}")
        result = analysis(populate(data_path), amt_dng_wds_for_flag)
        save_output(result, filename)

    except Exception as e:
        p_err("operations", "op_dangerous_user", str(e), False)



