import random
import string
import requests
import time


WEBHOOK_URL = "https://discord.com/api/webhooks/1399789560589717504/dh2Nr8LdgjRcXVsfSKf7oIoY-UoKUX2P_BY4uJcoLmKrcnROuu7xg-WqWCXSONUYnU-m"


def generate_usernames(count=50):
    usernames = set()

    while len(usernames) < count:
        choice = random.choice(["tri", "semi_tri", "semi_quad"])
        if choice == "tri":
            name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        elif choice == "semi_tri":
            pattern = random.choice([
                f"{random.choice(string.ascii_lowercase)}_{random.choice(string.ascii_lowercase)}",
                f"{random.choice(string.ascii_lowercase)}{random.choice(string.digits)}{random.choice(string.ascii_lowercase)}"
            ])
            name = pattern
        else:  
            name = ''.join(random.choices(string.ascii_lowercase + string.digits + "_", k=4))

        usernames.add(name)
    
    return list(usernames)


def check_username_available(username):
    url = f"https://discord.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 404:
        return True  
    elif response.status_code == 200:
        return False  
    else:
        return None   


def send_to_webhook(username):
    data = {
        "content": f"@everyone\n**new discord user available**\n`{username}`"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204 or response.status_code == 200:
            print(f"[Webhook] أُرسل بنجاح: {username}")
        else:
            print(f"[Webhook] فشل الإرسال: {response.status_code}")
    except Exception as e:
        print(f"[Webhook] خطأ أثناء الإرسال: {e}")


if __name__ == "__main__":
    generated = generate_usernames(30)
    print("🔍 جاري التحقق من اليوزرات...\n")

    for user in generated:
        available = check_username_available(user)
        if available is True:
            print(f"[✓] {user} يبدو أنه متاح")
            send_to_webhook(user)
        elif available is False:
            print(f"[×] {user} مستخدم بالفعل")
        else:
            print(f"[?] {user} لا يمكن التحقق (غير معروف)")

        time.sleep(1)  
