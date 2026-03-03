from user import *
from message import *

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


