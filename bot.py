import asyncio
import logging
import os
import sys
from flask import Flask
from threading import Thread
from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod

# 1. Direct Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(name)s - %(module)s - %(levelname)s - %(message)s",
    datefmt="%I:%M:%S %p",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("TelegramBot.log", mode="w")
    ]
)
logger = logging.getLogger(__name__)

# 2. Flask App Setup (For Koyeb Health Check)
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return '@JishuDeveloper'

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host='0.0.0.0', port=port)

# 3. Initialize Main Bot Client with in_memory=True (Clears Peer Cache)
bot = Client(
    "Renamer",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins'),
    in_memory=True
)

async def main():
    # Web Server Thread
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    logger.info("Web Server Started Successfully!")

    if STRING_SESSION:
        # Userbot Client Cache reset
        Client2.in_memory = True
        
        await Client2.start()
        await bot.start()
        
        logger.info("Bot and Userbot Started Successfully!")
        await idle()
        
        await Client2.stop()
        await bot.stop()
    else:
        await bot.start()
        logger.info("Bot Started Successfully!")
        await idle()
        await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())
