import os
import sys
import asyncio
from config import *
from pyrogram import filters, Client


@Client.on_message(filters.command("restart") & filters.user(ADMIN))
async def stop_button(bot, message):
    msg = await bot.send_message(
        text="<b><blockquote>🔄 ᴘʀᴏᴄᴇꜱꜱᴇꜱ ꜱᴛᴏᴘᴘᴇᴅ. ʙᴏᴛ ɪꜱ ʀᴇꜱᴛᴀʀᴛɪɴɢ...</blockquote></b>", 
        chat_id=message.chat.id
    )       
    await asyncio.sleep(3)
    await msg.edit("<b><blockquote>✅️ ʙᴏᴛ ɪꜱ ʀᴇꜱᴛᴀʀᴛᴇᴅ. ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ.</blockquote></b>")
    os.execl(sys.executable, sys.executable, *sys.argv)
