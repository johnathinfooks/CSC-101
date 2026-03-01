from src.message import *

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
