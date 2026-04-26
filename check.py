import requests
import os

URL = "https://www.toysrus.co.jp/ja-jp/pokemoncardgame/"
WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def send_discord(msg):
    if WEBHOOK:
        res = requests.post(WEBHOOK, json={"content": msg})
        print("status:", res.status_code)
    else:
        print("Webhook is None")

def check():
    res = requests.get(URL)
    text = res.text

    if "MEGAドリームex" in text:
        if ("在庫あり" in text) or ("カートに入れる" in text):
            send_discord("🔥【在庫あり】MEGAドリームex")
        else:
            send_discord("👀【掲載】MEGAドリームex（在庫不明）")

if __name__ == "__main__":
    check(send_discord("🔥テスト通知"))
