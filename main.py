import os
import sys

from src.utils import p_err
from src.operations import handle_operations



help_s = "use 'help' for help to use tool"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))



def main() -> None:

    try:
        # handle input initiate functionality
        handle_operations(sys.argv, ROOT_DIR)

    except Exception as e:
        p_err("main", "main", str(e), False)
        print(help_s)



# initial; starts here

main()
