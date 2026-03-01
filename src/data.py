import json
import os

class Message:
    def __init__(self, user_id:int, content:str, timestamp:int):
        self.user_id = user_id
        self.content = content.lower()
        self.timestamp = timestamp
        self.malicious_score = 0
        
    def checkMalicious(self, danger_words:dict) -> bool:
        swear_words = danger_words.get("swear words", [])
        racist_words = danger_words.get("racist_derogatory_words", [])

        for word in swear_words:
            if word in self.content:
                self.malicious_score += self.content.count(word) * 2 # Points per swear word
        for word in racist_words:
            if word in self.content:
                self.malicious_score += self.content.count(word) * 5 # Points per racist word

        return self.malicious_score > 0
        
    def evaluateMessage(self):
        return self.malicious_score

class User:
    def __init__(self, user_id:int, username:str):
        self.user_id = user_id
        self.username = username
        self.history: list[Message] = []
        self.total_score = 0
        self.malicious_flag = False

    def addMessage(self, message: Message):
            self.history.append(message)
        
    
    def getMessageHistory(self):
            return self.history
        
    def getScore(self):
            self.total_score = sum(msg.malicious_score for msg in self.history)
            return self.total_score
    
    def calculateMalicious(self, threshold: int = 50) -> bool:
         self.malicious_flag = self.getScore >= threshold
         return self.malicious_flag
    
    def checkSpam(self, time_window: int = 60) -> int:
        if len(self.history) < 3:
              return 0
        spam_score = 0
        sorted_messages = sorted(self.history, key = lambda m: m.timestamp)
        for i in range(len(sorted_messages) - 2):
              if sorted_messages[i+2].timestamp - sorted_messages[i].timestamp <= time_window:
                   spam_score += 5
        self.total_score += spam_score
        return spam_score
        
    def __eq__(self, other):
        return self.user_id == other.user_id


        

        
