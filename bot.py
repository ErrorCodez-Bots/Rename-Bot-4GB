import asyncio
import logging
import logging.config
import os
import sys
from flask import Flask
from threading import Thread
from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod

# 1. Setup Logging Config
logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)

# 2. Flask App Setup (For Web Server / Healthy Checks)
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return '@JishuDeveloper'

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host='0.0.0.0', port=port)

# 3. Initialize Main Bot Client
bot = Client(
    "Renamer",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

async def main():
    # Web சர்வரை தனியாக Background Thread-ல் இயக்குகிறது
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    logger.info("Web Server Started Successfully!")

    if STRING_SESSION:
        # Userbot மற்றும் Bot இரண்டையும் துவக்குகிறது
        await Client2.start()
        await bot.start()
        
        logger.info("Bot and Userbot Started Successfully!")
        await idle()
        
        await Client2.stop()
        await bot.stop()
    else:
        # Bot மட்டும் துவக்குகிறது
        await bot.start()
        logger.info("Bot Started Successfully!")
        await idle()
        await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())


# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper
