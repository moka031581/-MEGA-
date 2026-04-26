import requests
import os

URL = "https://www.toysrus.co.jp/ja-jp/pokemoncardgame/"
LINE_TOKEN = os.getenv("LINE_TOKEN")

def send_line(msg):
    requests.post(
        "https://notify-api.line.me/api/notify",
        headers={"Authorization": f"Bearer {LINE_TOKEN}"},
        data={"message": msg}
    )

def check():
    res = requests.get(URL)
    text = res.text

    if "MEGAドリームex" in text:
        if ("在庫あり" in text) or ("カートに入れる" in text):
            send_line("【在庫あり】MEGAドリームex")
        else:
            send_line("【掲載】MEGAドリームex（在庫不明）")

if __name__ == "__main__":
    check()
