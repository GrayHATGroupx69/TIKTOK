import random
import string
import requests
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1399789560589717504/dh2Nr8LdgjRcXVsfSKf7oIoY-UoKUX2P_BY4uJcoLmKrcnROuu7xg-WqWCXSONUYnU-m"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def generate_username(length):
    characters = string.ascii_lowercase + string.digits + "._"
    return ''.join(random.choices(characters, k=length))

def is_username_available(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url, headers=headers)
    return response.status_code == 404

def send_to_discord(username):
    data = {
        "content": f"@everyone\n**NEW INSTAGRAM USER !!**\n**USER:** `{username}`\n**THIS TOOL BY GRAYHATX69**"
    }
    requests.post(WEBHOOK_URL, json=data)

def main():
    while True:
        length = random.choice([3, 4, 5])
        username = generate_username(length)
        if is_username_available(username):
            print(f"[✅ AVAILABLE] {username}")
            send_to_discord(username)
        else:
            print(f"[❌ TAKEN] {username}")
        time.sleep(2) 

if __name__ == "__main__":
    main()
