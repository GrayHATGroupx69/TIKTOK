import requests
import random
import string
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1399569154218135653/Xi_Bs7y3hKxA3TFD1iLo8eP8coiAy74Cle6rJLEqlf05LkvWCoCWiXfOo8qYXkufYMPm"


def generate_tiktok_username():
    patterns = [
        lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=3)),     
        lambda: ''.join(random.choices(string.ascii_lowercase + '._', k=4)),               
        lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),      
        lambda: ''.join(random.choices(string.ascii_lowercase + '._', k=5)),              
        lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)),       
        lambda: ''.join(random.choices(string.ascii_lowercase + '._', k=6)),                
    ]
    return random.choice(patterns)()


def generate_discord_code():
    patterns = [
        lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=2)),  
        lambda: ''.join(random.choices(string.ascii_letters + string.digits + "_-", k=3)),  
        lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=3)),  
        lambda: ''.join(random.choices(string.ascii_letters + string.digits + "_-", k=4)),  
    ]
    return random.choice(patterns)()


def is_tiktok_user_available(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.status_code == 404


def is_discord_invite_valid(code):
    url = f"https://discord.com/api/v9/invites/{code}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.status_code == 200


def send_to_discord(content):
    data = {"content": content}
    requests.post(WEBHOOK_URL, json=data)


while True:
    try:
   
        user = generate_tiktok_username()
        print(f"[TIKTOK] Checking @{user}")
        if is_tiktok_user_available(user):
            print(f"[TIKTOK] FOUND AVAILABLE USER: @{user}")
            send_to_discord(f"**FIND NEW USER !!!**\n@{user}\n\n`THIS TOOL BY GRAYHATX69`")
        time.sleep(1.2)

     
        code = generate_discord_code()
        print(f"[DISCORD] Checking invite: {code}")
        if is_discord_invite_valid(code):
            print(f"[DISCORD] VALID INVITE FOUND: discord.gg/{code}")
            send_to_discord(f"**NEW DISCORD URL FOUND**\ndiscord.gg/{code}\n\n`THIS TOOL BY GRAYHATX69` @everyone")
        time.sleep(1.2)

    except KeyboardInterrupt:
        print("end by user.")
        break
    except Exception as e:
        print(f"[ERROR] {e}")
        time.sleep(3)
