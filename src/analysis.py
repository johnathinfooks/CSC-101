import json

from .user import *
from .utils import *



# Vincent Le
# this is the fun part of all of this; where the user and message classes get used
# basically updates and synthesizes/makes conclusions based on the data
def analysis(in_users: list[User], lower: int) -> list[User]:

    out = []

    for user in in_users:

        msg_h = user.message_history

        u = User(user.name, user.id, user.message_history)

        amount_dangerous = 0
        for msg in msg_h:
            amount_dangerous += msg.check_malicious()

        u.malicious_score = amount_dangerous

        if u.malicious_score > int(lower):
            u.malicious_flag = True

        out.append(u)

    return out



# Johnathin Fooks
# take json file. perform analysis on users. return a list of user objects
# with updated information
def populate(dataset_path: str) -> list[User]:

    try:
        out: list[User] = []

        with open(dataset_path, "r") as f, open("data/dataGen/users.json") as g:
            data = json.load(f)
            user_data = json.load(g)

        # binding id to name with dictionary
        user_lookup = {u["id"]: u["name"] for u in user_data}

        # initiating list of users
        for entry in data:
            id = entry["id"]
            if id in user_lookup:
                msg_lst = [
                    Message(m["timestamp"], m["content"])
                    for m in entry["messages"]
                ]

                u = User(user_lookup[id], id, msg_lst)
                out.append(u)

        return out

    except Exception as e:
        p_err("utils", "populate", str(e), True)
        return []



# Vincent Le
def show_flagged_users(lst:list[User]) -> list[str]:
    bad_list = []
    for user in lst:
        if user.malicious_flag:
            s = f"{user.id}  :  {user.name}"
            bad_list.append(s)
    return bad_list
