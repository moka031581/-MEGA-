import requests
import os

URL = "https://www.toysrus.co.jp/ja-jp/pokemoncardgame/"
WEBHOOK = os.getenv("DISCORD_WEBHOOK")
STATE_FILE = "status.txt"

def send_discord(msg):
    if WEBHOOK:
        requests.post(WEBHOOK, json={"content": msg})

def get_current_status(text):
    if "MEGAドリームex" in text:
        if ("在庫あり" in text) or ("カートに入れる" in text):
            return "in_stock"
        return "listed"
    return "none"

def read_previous():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return f.read()
    return "none"

def write_current(status):
    with open(STATE_FILE, "w") as f:
        f.write(status)

def check():
    res = requests.get(URL)
    text = res.text

    current = get_current_status(text)
    previous = read_previous()

    print("前回:", previous, "今回:", current)

    # 状態が変わったときだけ通知
    if current != previous:
        if current == "in_stock":
            send_discord("🔥【在庫復活】MEGAドリームex")
        elif current == "listed":
            send_discord("👀【掲載】MEGAドリームex")

    write_current(current)

if __name__ == "__main__":
    check()
