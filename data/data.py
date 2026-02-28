
class Message:
    def __init__(self, user_id:int, content:str, timestamp:int):
        self.user_id = user_id
        self.content = content.lower()
        self.timestamp = timestamp
        
    def checkMalicious(self) -> bool:
        return False
        
    def evaluateMessage(self):
        pass

class User:
    def __init__(self, username:str, history:list[Message], timestamp:int, channel:int):
        
        def getMessageHistory():
            return None
        
        def getScore():
            return int
        

        