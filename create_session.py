import os
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("TG_API_ID"))
api_hash = os.getenv("TG_API_HASH")
phone = os.getenv("TG_PHONE")
session = os.getenv("SESSION_FILE", "samostroi.session")

print("===============================================")
print("  Telethon: Создание сессии")
print("  Номер:", phone)
print("===============================================")

client = TelegramClient(session, api_id, api_hash)

async def main():
    print("Авторизация...")
    await client.start(phone=phone)
    print("===============================================")
    print("СЕССИЯ УСПЕШНО СОЗДАНА!")
    print("Файл:", session)
    print("===============================================")

with client:
    client.loop.run_until_complete(main())
