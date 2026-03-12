import json



# Johnathin Fooks
class Message:

    def __init__(self, in_timestamp: int, in_content: str) -> None:
        self.timestamp = in_timestamp
        self.content = in_content

    def __repr__(self) -> str:

        s = f"{self.timestamp}: '{self.content}'"

        return s



    def check_malicious(self) -> int:

        amount_danger_words = 0
        danger_words = []

        try:
            with open("data/dataGen/danger.json", "r") as df:
                danger_words = json.load(df)

            message_arr = self.content.split()

            for word in message_arr:
                if word in danger_words:
                    amount_danger_words += 1

            return amount_danger_words

        except Exception as e:
            print(e)
            return 0
