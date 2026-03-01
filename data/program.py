import data
import dataGen
import json

def loadChannelData(filepath: str = "dataGen/users.json") -> dict[int, data.Users]:
        with open(filepath, 'r') as file:
             users_data = json.load(file)

        channel = {}

        for user_data in users_data:
             user_id = user_data["user_id"]
             username = user_data["username"]
             channel_id = user_data.get("channel", 1)

             user = data.User(user_id, username, channel_id)

             for msg_data in user_data["messages"]:
                  message = data.Message(
                       user_id = user_id,
                       content=msg_data["content"],
                       timestamp = msg_data["timestamp"]
                       )
                  user.addMessage(message)
        channel[user_id] = user
        return channel

def analyzeChannel(channel: dict[int, data.User], threshold: int = 50) -> list[data.User]:
     badUsers= []
     danger_words = data.loadDangerWords("dataGen/danger.json")
     for user_id, user in channel.items():
          for message in user.getMessageHistory():
               message.checkMalicious(danger_words)

          user.checkSpamming(time_window=60)
          if user.calculateMalicious(threshold):
               badUsers.append(user)
     return badUsers

def displayResults(channel: dict[int, data.User], malicious_users: list[data.User]):
    print("\n" + "="*60)
    print("MESSAGE FLAGGER ANALYSIS REPORT")
    print("="*60)

    print(f"\n Channel Statistics:")
    print(f"    Total users analyzed: {len(channel)}")
    print(f"    Flagged users: {len(malicious_users)}")
    print(f"    Clean users: {len(channel) - len(malicious_users)}")

    if malicious_users:
        print(f"\n FLAGGED USERS:")
        print("-"*60)

        #Sort function
        malicious_users.sort(key=lambda u:u.total_score, reverse=True)

        for rank, user in enumerate(malicious_users, 1):
            print(f"\n{rank} - {user.username} (ID: {user.user_id})")
            print(f"    Danger Score: {user.total_score}")
            print(f"    Total Messages: {len(user.history)}")

            flagged_msgs = [msg for msg in user.history if msg.malicious_score > 0]
            print (f"   Flagged Messages: {len(flagged_msgs)}")

            if flagged_msgs:
                print(f"    Top violations:")
                for msg in flagged_msgs[:3]: # Top 3 messages of all time
                    content_preview = msg.content[:45] + "..." if len(msg.content) > 45 else msg.content
                    print(f"        -[{msg.timestamp}] Score: {msg.malicious_score}")
                    print(f"        \"{content_preview}\"")

    else:
        print(f"\n No flagged users as malicious!")
        print(" All users are acting accordingly and are well-behaved!")
    print("\n" + "="*60)



def main():
    print("Message Flagger Program")
    print("Loading data...\n")

    try:
         channel = loadChannelData("dataGen/users.json")

         threshold = 50 # Adjustable: lower = stricter
         malicious_users = analyzeChannel(channel, threshold)

         displayResults(channel, malicious_users)
    except FileNotFoundError as e:
         print(f" Error: Could not find required data files. Make sure users.json and danger.json exist in dataGen/")
         print(f"An error has occurred: {e}")

    return None
    

if __name__ == "__main__":
     main()