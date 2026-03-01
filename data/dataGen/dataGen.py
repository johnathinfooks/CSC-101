from datetime import datetime
import json
import random

##############################
opt_dataSet_name = "Data Set One"
number_of_iterations = 7
##############################

def generateMessage(amount_malicious: int, num_words: int) -> dict:
    with open("safe.json", "r") as sf, open("danger.json", "r") as df:

        random_time = f"{random.randint(0, 2359):04d}"

        safe_words = json.load(sf)
        danger_words = json.load(df)

        message_arr = []
        # if amount_malicious is 0, every word is safe. if greater, then its every nth word is dangerous (1 is every word dangerous, 2 is every other word, etc)
        for i in range(num_words):
            if amount_malicious == 0:
                message_arr.append(random.choice(safe_words))
            elif (i + 1) % amount_malicious != 0:
                message_arr.append(random.choice(safe_words))
            else:
                message_arr.append(random.choice(danger_words))


        return {
            "timestamp": random_time,
            "content": " ".join(message_arr)
        }

def writeFileContent(max_amount_malicious: int, max_num_words: int, max_num_messages) -> dict:
    with open("users.json") as uf:


        rand_num_messages = random.randint(1, max_num_messages)

        messages_arr = []

        for _ in range(rand_num_messages):
            rand_amount_malicious = random.randint(0, max_amount_malicious)
            rand_amount_words = random.randint(1, max_num_words)

            message = generateMessage(rand_amount_malicious, rand_amount_words)
            messages_arr.append(message)

        user_data = json.load(uf)
        rand_user = random.choice(user_data)

        element = {
            "name": rand_user["name"],
            "id": rand_user["id"],
            "messages": messages_arr,
            "flagged": False,
            "malicious_score": 0
        }

    return element

# writes content to json file
def writeFile(in_file_content: list) -> None:

    c_t = datetime.now() # current time
    timestamp = c_t.strftime("%d%b%y-%H:%M").upper()
    filename = f"../dataSets/dataSet-{timestamp}-[{opt_dataSet_name}].json"

    with open(filename, "w") as f:
        json.dump(in_file_content, f, indent=4)


dataSet = []

for _ in range(number_of_iterations):
    dataSet.append(writeFileContent(5, 10, 10))

writeFile(dataSet)



