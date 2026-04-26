import requests
import os

URL = "https://www.toysrus.co.jp/ja-jp/pokemoncardgame/"
WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def send_discord(msg):
    if WEBHOOK:
        requests.post(WEBHOOK, json={"content": msg})

def check():
    res = requests.get(URL)
    text = res.text

    # 一度通知したら止める用
    if os.path.exists("sent.txt"):
        return

    if "MEGAドリームex" in text:
        send_discord("🔥MEGAドリームex掲載 or 在庫あり！\nhttps://www.toysrus.co.jp/ja-jp/pokemoncardgame/")

        with open("sent.txt", "w") as f:
            f.write("sent")

if __name__ == "__main__":
    check()
