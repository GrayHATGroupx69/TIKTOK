import random
import string
import requests
import time
from bs4 import BeautifulSoup

WEBHOOK_URL = "https://discord.com/api/webhooks/1399789560589717504/dh2Nr8LdgjRcXVsfSKf7oIoY-UoKUX2P_BY4uJcoLmKrcnROuu7xg-WqWCXSONUYnU-m"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# -------- Instagram --------

def generate_insta_username(length):
    chars = string.ascii_lowercase + string.digits + "._"
    return ''.join(random.choices(chars, k=length))

def is_insta_available(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url, headers=HEADERS)
    return response.status_code == 404

def send_insta_to_webhook(username):
    data = {
        "content": f"@everyone\n**NEW INSTAGRAM USER !!**\n**USER:** `{username}`\n**THIS TOOL BY GRAYHATX69**"
    }
    requests.post(WEBHOOK_URL, json=data)

# -------- Discord --------

def generate_discord_username(length):
    chars = string.ascii_lowercase + string.digits + "_"
    return ''.join(random.choices(chars, k=length))

def is_discord_available(username):
    try:
        url = "https://discordgate.com/tools/username-lookup"
        data = {"username": username}
        response = requests.post(url, headers=HEADERS, data=data)
        soup = BeautifulSoup(response.text, "html.parser")
        alert_div = soup.find("div", class_="alert")
        if alert_div:
            result = alert_div.text.strip()
            return "available" in result.lower()
        else:
            return False
    except Exception as e:
        print(f"[Error Checking Discord Username] {e}")
        return False

def send_discord_to_webhook(username):
    data = {
        "content": f"@everyone\n**NEW DISCORD USER !!**\n**USER:** `{username}`\n**THIS TOOL BY GRAYHATX69**"
    }
    requests.post(WEBHOOK_URL, json=data)

# -------- Main Loop --------

def main():
    while True:
        try:
            # --- Instagram ---
            insta_length = random.choice([3, 4, 5])
            insta_user = generate_insta_username(insta_length)
            if is_insta_available(insta_user):
                print(f"[✅ INSTAGRAM AVAILABLE] {insta_user}")
                send_insta_to_webhook(insta_user)
            else:
                print(f"[❌ INSTAGRAM TAKEN] {insta_user}")

            # --- Discord ---
            discord_length = random.choice([3, 4])
            discord_user = generate_discord_username(discord_length)
            if is_discord_available(discord_user):
                print(f"[✅ DISCORD AVAILABLE] {discord_user}")
                send_discord_to_webhook(discord_user)
            else:
                print(f"[❌ DISCORD TAKEN] {discord_user}")

            time.sleep(2)  # Delay to avoid rate limiting

        except KeyboardInterrupt:
            print("🛑 Stopped by user.")
            break
        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()
