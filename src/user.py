from .message import Message

class User:

    def __init__(self, in_name: str, in_id: int, in_msg_h: list[Message]) -> None:
        self.name = in_name
        self.id = in_id
        self.message_history = in_msg_h
        self.malicious_score = 0
        self.malicious_flag = False

    def __repr__(self):

        s = f'''
ID: {self.id}
Name: {self.name}
Message History: {self.message_history}
Malicious Score: {self.malicious_score}
Malicious Flag: {self.malicious_flag}
'''

        return s

