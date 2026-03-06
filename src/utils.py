import os

from .user import *
from .message import *

def populate(dataset_path: str) -> dict[int, list[Message]] | None:

    out: dict[int, list[Message]] = {}

    try:
        with open(dataset_path, "r") as dataset:
            data = json.load(dataset)

            for entry in data:
                user_id = int(entry["id"])
                msg_list: list[Message] = []

                for msg in entry.get("messages", []):
                    timestamp = int(msg["timestamp"])
                    content = msg["content"]
                    msg_list.append(Message(timestamp, content))

                out[user_id] = msg_list


    except FileNotFoundError as e:
        print(f"File not found; {e}.")
        return None
    except:
        print("Error.")
        return None

    return out

def listDataSets() -> list[str]:
    data_path = "dataSet"
    files = []
    if not os.path.exists(data_path):
        print("Error: {} not found").format(data_path)
        return []
    for i in os.listdir(data_path):
        if i.endswith('.json'):
            files.append(i)
    return sorted(files)


def clear_terminal():
    # Check if the operating system is Windows ('nt') or Posix (Linux, macOS, Unix)
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls') 
    else:
        # Command for Linux, macOS, etc.
        _ = os.system('clear')
