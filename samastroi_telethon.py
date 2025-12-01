import os
import logging
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("TG_API_ID", "0"))
API_HASH = os.getenv("TG_API_HASH", "")
SESSION_FILE = os.getenv("SESSION_FILE", "samostroi.session")

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("samastroi_bot")

client = TelegramClient(SESSION_FILE, API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r"/start"))
async def handler_start(event):
    await event.reply("Самострой-бот запущен. Здесь должен быть твой основной код бота.")

if __name__ == "__main__":
    log.info("Starting Samostroi Telethon bot...")
    client.start()
    client.run_until_disconnected()
