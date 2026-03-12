import os

from src.utils import *
from src.analysis import *



help_s = '''
    Valid input:

    help - access help information
    info - access general information
    list - list datasets
    analysis <dataset name> <output file name> <max dangerous> - show all users that are flagged as dangerous according to prompted value
    '''

info_s = '''
    ================================================
    Dangerous Activity Message Analysis Tool
    ================================================

    By Johnathin Fooks and Vincent Le
    California Polytechnic State University, CSC-101
'''



# Johnathin Fooks
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

            case "list":
                if len(argv_l) != 2:
                    raise Exception
                op_list_datasets()

            case "analysis":
                if len(argv_l) != 5:
                    raise Exception
                op_full_analysis(argv_l[2], argv_l[3], int(argv_l[4]), ROOT_DIR)

            case _:
                raise Exception

    except Exception as e:
        p_err("operations", "handle_operations", str(e), True)



# Vincent Le
def op_help() -> None:

    try:
        print(help_s)

    except Exception as e:
        p_err("operations", "op_help", str(e), False)



# Vincent Le
def op_info() -> None:

    try:
        print(info_s)

    except Exception as e:
        p_err("operations", "op_info", str(e), False)



# Vincent Le
def op_list_datasets():
    
    try:
        files = os.listdir("data/dataSets/")
        print("\n    Valid Datasets:")
        print()
        for f in files:
            print('    ' + f)
        print()


    except Exception as e:
        p_err("operations", "op_list_datasets", str(e), False)



# Vincent Le
def op_full_analysis(dataset_name: str, out_filename: str, amt_dng_wds_for_flag: int, ROOT_DIR) -> None:

    try:
        data_path = os.path.join(ROOT_DIR, f"data/dataSets/{dataset_name}")
        result = analysis(populate(data_path), amt_dng_wds_for_flag)
        save_output(result, out_filename)

    except Exception as e:
        p_err("operations", "op_full_analysis", str(e), False)



