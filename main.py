from src.user import *
from src.message import *
from src.utils import *
from src.operations import *
import sys

help_s = "use 'help' for help to use tool"

def main() -> int:

    try:
        # handle input initiate functionality
        handle_operations(sys.argv)

        return 0

    except:
        p_err("main", "main", "likely misinput")
        print(help_s)
        return 1

# initial

main()
