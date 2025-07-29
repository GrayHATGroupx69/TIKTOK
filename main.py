import requests
import random
import string
import time


WEBHOOK_URL = "https://discord.com/api/webhooks/1399569154218135653/Xi_Bs7y3hKxA3TFD1iLo8eP8coiAy74Cle6rJLEqlf05LkvWCoCWiXfOo8qYXkufYMPm"

def generate_username():
    patterns = [
        lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=3)),      
        lambda: ''.join(random.choices(string.ascii_lowercase + '._', k=4)),                
        lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),      
        lambda: ''.join(random.choices(string.ascii_lowercase + '._', k=5)),                
        lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)),       
        lambda: ''.join(random.choices(string.ascii_lowercase + '._', k=6)),                
    ]
    return random.choice(patterns)()


def is_username_available(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    return response.status_code == 404


def send_to_discord(username):
    data = {
        "content": f"**FIND NEW USER !!!**\n@{username}\n\n`THIS TOOL BY GRAYHATX69`"
    }
    requests.post(WEBHOOK_URL, json=data)


while True:
    try:
        user = generate_username()
        print(f"Checking @{user}")
        if is_username_available(user):
            print(f"Available: @{user}")
            send_to_discord(user)
        else:
            print(f"Taken: @{user}")
        time.sleep(1.0)  
    except KeyboardInterrupt:
        print("STOPPED BY USER.")
        break
    except Exception as e:
        print(f"ERROR: {e}")
        time.sleep(3)
