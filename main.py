import random
import string
import requests
import time

# Your updated Discord Webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1399789562745589770/n0hRBZwhZ_xeY-m9qDXJQNv4StWhueBhncbltPNj-r__z3XgKOyaf0wDEQ1WflXDHxWV"

# Generate semi-quad or quad username (4 chars only)
def generate_username():
    pattern_type = random.choice(["semi_quad", "quad"])
    
    if pattern_type == "semi_quad":
        return ''.join(random.choices(string.ascii_lowercase + string.digits + "_", k=4))
    else:  # quad
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))

# Check if the username is available (not guaranteed, just simulated)
def check_username_available(username):
    url = f"https://discord.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return True   # Likely available
        elif response.status_code == 200:
            return False  # Taken
        else:
            return None   # Unclear
    except:
        return None

# Send result to Discord Webhook
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

# Main infinite loop
if __name__ == "__main__":
    print("🔁 Starting infinite Discord username checker (semi-quad & quad)...\n")

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
        time.sleep(1)  # Avoid rate limiting
