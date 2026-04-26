import requests
import os

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

print("Webhook:", WEBHOOK)  # ← まず確認

res = requests.post(WEBHOOK, json={"content": "🔥テスト通知"})
print("status:", res.status_code)
print("response:", res.text)
