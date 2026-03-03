import user
import message


# initial program

dataSet = []

print("== CREATE DATASET ==")
s = '''
Name: Name of dataset; included in file name.
Max Amount Messages: The max number of messages each user object can have. Random between 0 and max.
Max Amount Words: The max number of words each message object can have. Random between 0 and max.
Max Amount Dangerous: Random number between 0 and max that represents amount dangerous. 0 = no danger. After 0, every nth word is dangerous.
Iterations: The number of user objects included in dataset.
'''
print(s)
dataSetName = input("Name of dataset: ")
max_amount_messages = int(input("Max Amount Messages: "))
max_amount_words = int(input("Max Amount Words: "))
max_amount_dangerous = int(input("Max Amount Dangerous: "))
dataSetIterations = int(input("Number of iterations: "))

for _ in range(dataSetIterations):
    dataSet.append(writeFileContent(max_amount_dangerous, max_amount_words, max_amount_messages))

writeFile(dataSet, dataSetName)



