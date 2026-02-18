from datetime import datetime

file_content = "test"

##############################
opt_dataSet_name = "Test"
##############################


# writes to json file
def writeFile(in_file_content: str) -> None:

    c_t = datetime.now() # current time
    timestamp = c_t.strftime("%d%b%y-%H:%M").upper()
    filename = f"dataSet-{timestamp}-[{opt_dataSet_name}].json"

    with open(filename, "w") as file:
        file.write(in_file_content)

writeFile(file_content)


