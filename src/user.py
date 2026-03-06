from .message import *

class User:

    def __init__(self, in_name: str, in_id: int) -> None:
        self.name = in_name
        self.id = in_id
        self.message_history: list[Message] = []
        self.malicious_score = 0
        self.malicious_flag = False

    def __repr__(self):

        s = f'''
        Name: {self.name}
        ID: {self.id}
        Message History: {self.message_history}
        Malicious Score: {self.malicious_score}
        Malicious Flag: {self.malicious_flag}
        '''

        return s
    
    def check_flag(self):
        mal_sum = 0
        threshold = 50 #set threshold here
        for i in self.message_history:
            score = i.check_malicious()
            mal_sum += score if score else 0
        self.malicious_score = mal_sum
        if mal_sum >= threshold: 
            self.malicious_flag = True


def display_flagged_users(users: list[User], threshold: int) -> str:
    flagged_list = []
    for i in users:
        if i.malicious_flag == True:
            flagged_list.append(i)
    print(f"Flagged:{flagged_list}")
