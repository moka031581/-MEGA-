import requests
import os
import time

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

PACKS = [
    "スタートデッキ100",
    "ニンジャスピナー",
    "アビスアイ",
    "メガドリーム",
    "インフェルノＸ",
    "ストームエメラルダ",
]

SITES = [
    ("トイザらス", "https://www.toysrus.co.jp/ja-jp/pokemoncardgame/"),
    ("エディオン", "https://www.edion.com/item_list.html?keyword=%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%82%AB%E3%83%BC%E3%83%89"),
    ("イオン", "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%82%AB%E3%83%BC%E3%83%89%E3%82%AB%E3%83%BC%E3%83%89&psc=0")
]

def send(msg):
    if WEBHOOK:
        requests.post(WEBHOOK, json={"content": msg})

def check():
    for name, url in SITES:
        try:
            text = requests.get(url, timeout=10).text

            for pack in PACKS:
                if pack in text:
                    if "在庫あり" in text or "カートに入れる" in text:
                        send(f"🔥【{name}】在庫あり！{pack}")

        except:
            print(f"{name} エラー")

# 1回の実行で3回チェック（高速化）
for _ in range(3):
    check()
    time.sleep(20)
