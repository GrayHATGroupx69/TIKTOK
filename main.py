import random
import string
import requests
import time

# Your Discord webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1399789562745589770/n0hRBZwhZ_xeY-m9qDXJQNv4StWhueBhncbltPNj-r__z3XgKOyaf0wDEQ1WflXDHxWV"

# Generate a single username
def generate_username():
    pattern_type = random.choice(["tri", "semi_tri", "semi_quad"])

    if pattern_type == "tri":
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))

    elif pattern_type == "semi_tri":
        return random.choice([
            f"{random.choice(string.ascii_lowercase)}_{random.choice(string.ascii_lowercase)}",
            f"{random.choice(string.ascii_lowercase)}{random.choice(string.digits)}{random.choice(string.ascii_lowercase)}"
        ])

    else:  # semi_quad
        return ''.join(random.choices(string.ascii_lowercase + string.digits + "_", k=4))

# Check if a username is likely available (simulated)
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

# Send webhook with status
def send_to_webhook(username, available):
    if available is True:
        content = f"@everyone\n**new discord user available**\n`{username}`"
    elif available is False:
        content = f"**username already taken**\n`{username}`"
    else:
        content = f"**could not verify username**\n`{username}`"

    try:
        response = requests.post(WEBHOOK_URL, json={"content": content})
        if response.status_code in [200, 204]:
            print(f"[Webhook] Sent: {username} ({'available' if available else 'taken'})")
        else:
            print(f"[Webhook] Failed to send ({response.status_code})")
    except Exception as e:
        print(f"[Webhook] Error: {e}")

# Infinite loop to keep guessing usernames
if __name__ == "__main__":
    print("🚀 Username checker started (infinite loop)...\n")

    while True:
        username = generate_username()
        status = check_username_available(username)

        if status is True:
            print(f"[✓] {username} is available")
        elif status is False:
            print(f"[X] {username} is taken")
        else:
            print(f"[?] Could not verify {username}")

        send_to_webhook(username, status)

        time.sleep(1)  # avoid rate limiting
