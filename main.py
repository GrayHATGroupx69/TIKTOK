import requests
import random
import string
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1399789560589717504/dh2Nr8LdgjRcXVsfSKf7oIoY-UoKUX2P_BY4uJcoLmKrcnROuu7xg-WqWCXSONUYnU-m"

def generate_tiktok_username():
    patterns = [
        lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=3)),
        lambda: ''.join(random.choices(string.ascii_lowercase + "._", k=4)),
        lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        lambda: ''.join(random.choices(string.ascii_lowercase + "._", k=5)),
        lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)),
        lambda: ''.join(random.choices(string.ascii_lowercase + "._", k=6)),
    ]
    return random.choice(patterns)()

def generate_discord_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=2))

def check_tiktok_user_available(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response.status_code == 404
    except:
        return False

def check_discord_code_available(code):
    url = f"https://discord.com/api/v9/invites/{code}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response.status_code == 404
    except:
        return False

def send_webhook(message):
    data = {"content": message}
    try:
        requests.post(WEBHOOK_URL, json=data)
    except:
        pass

while True:
    try:
        tiktok_user = generate_tiktok_username()
        print(f"Checking TikTok username: @{tiktok_user}")
        if check_tiktok_user_available(tiktok_user):
            print(f"AVAILABLE TikTok username: @{tiktok_user}")
            send_webhook(f"**NEW TIKTOK USER FOUND !!**\nusername ( \"{tiktok_user}\" )\n\nthis tool by grayhatx69\n@everyone")

        time.sleep(1.0)

        discord_code = generate_discord_code()
        print(f"Checking Discord invite: {discord_code}")
        if check_discord_code_available(discord_code):
            print(f"AVAILABLE Discord invite: discord.gg/{discord_code}")
            send_webhook(f"**NEW DISCORD URL FOUND !!**\nurl ( \"discord.gg/{discord_code}\" )\n\nthis tool by grayhatx69\n@everyone")

        time.sleep(1.0)

    except KeyboardInterrupt:
        print("Stopped.")
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(3)
