import asyncio
from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod

# Initialize Main Bot Client
bot = Client(
    "Renamer",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

async def main():
    if STRING_SESSION:
        # Start both Userbot (Client2) and Bot
        await Client2.start()
        await bot.start()
        
        print("Bot and Userbot Started Successfully!")
        await idle()
        
        # Stop both Clients gracefully
        await Client2.stop()
        await bot.stop()
    else:
        # Start only Bot
        await bot.start()
        print("Bot Started Successfully!")
        await idle()
        await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())


# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper
