import os
import sys

from src.utils import p_err
from src.operations import handle_operations



ROOT_DIR = os.path.dirname(os.path.abspath(__file__))



# Vincent Le
def main() -> None:

    try:
        # handle input initiate functionality
        handle_operations(sys.argv, ROOT_DIR)

    except Exception as e:
        p_err("main", "main", str(e), False)



# initial; starts here

main()
