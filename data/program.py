import data
import dataGen
import json


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

