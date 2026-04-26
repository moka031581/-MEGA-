import requests
import os

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

requests.post(WEBHOOK, json={"content": "✅テスト成功！"})
