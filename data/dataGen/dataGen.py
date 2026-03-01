from datetime import datetime
import json
import random


##############################
opt_dataSet_name = "Test"
##############################

file_content = ""

def writeFileContent(percent_malicious: int, num_words: int):

    with open("data/words.json") as sf:
        safe_data = json.load(sf)

    with open("data/danger.json") as df:
        danger_data = json.load(df)

    i = 0
    while i < num_words:
        file_content = " ".join(random.choice(safe_data))



        i += 1


# writes to json file
def writeFile(in_file_content: str) -> None:

    c_t = datetime.now() # current time
    timestamp = c_t.strftime("%d%b%y-%H:%M").upper()
    filename = f"dataSets/dataSet-{timestamp}-[{opt_dataSet_name}].json"

    with open(filename, "w") as file:
        file.write(in_file_content)

writeFile(file_content)


