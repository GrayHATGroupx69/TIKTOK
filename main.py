import random
import string
import requests
import time

# Discord Webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1399789560589717504/dh2Nr8LdgjRcXVsfSKf7oIoY-UoKUX2P_BY4uJcoLmKrcnROuu7xg-WqWCXSONUYnU-m"


def generate_usernames(count=50):
    usernames = set()

    while len(usernames) < count:
        pattern_type = random.choice(["tri", "semi_tri", "semi_quad"])

        if pattern_type == "tri":
            name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))

        elif pattern_type == "semi_tri":
            name = random.choice([
                f"{random.choice(string.ascii_lowercase)}_{random.choice(string.ascii_lowercase)}",
                f"{random.choice(string.ascii_lowercase)}{random.choice(string.digits)}{random.choice(string.ascii_lowercase)}"
            ])

        else:  
            name = ''.join(random.choices(string.ascii_lowercase + string.digits + "_", k=4))

        usernames.add(name)

    return list(usernames)


def check_username_available(username):
    url = f"https://discord.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return True  
        elif response.status_code == 200:
            return False  
        else:
            return None   
    except:
        return None

def send_to_webhook(username):
    data = {
        "content": f"@everyone\n**new discord user available**\n`{username}`"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code in [200, 204]:
            print(f"[Webhook] Sent: {username}")
        else:
            print(f"[Webhook] Failed to send ({response.status_code})")
    except Exception as e:
        print(f"[Webhook] Error: {e}")


if __name__ == "__main__":
    generated_usernames = generate_usernames(30)
    print("🔎 Checking generated usernames...\n")

    for username in generated_usernames:
        is_available = check_username_available(username)

        if is_available is True:
            print(f"[✓] {username} is available")
            send_to_webhook(username)

        elif is_available is False:
            print(f"[X] {username} is taken")

        else:
            print(f"[?] Could not verify {username}")

        time.sleep(1) 
