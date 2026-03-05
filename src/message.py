import json

class Message:

    def __init__(self, in_timestamp: int, in_content: str) -> None:
        self.timestamp = in_timestamp
        self.content = in_content

    def __repr__(self) -> str:

        s = f'''
        Timestamp: {self.timestamp}
        Content: {self.content}
        '''

        return s
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Message):
            return False

    def check_malicious(self) -> int | None:

        amount_danger_words = 0
        danger_words = []

        try:
            with open("../data/dataGen/danger.json", "r") as df:
                danger_words = json.load(df)

            message_arr = self.content.split()

            for word in message_arr:
                if word in danger_words:
                    amount_danger_words += 1

            return amount_danger_words

        except FileNotFoundError as e:
            print(f"File not found; {e}.")
            return None
        except:
            print("Error.")
            return None


