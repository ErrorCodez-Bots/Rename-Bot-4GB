from config import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.database import botdata, find_one, total_user, getid
from helper.progress import humanbytes

token = BOT_TOKEN
botid = token.split(':')[0]


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def users(client, message):
    botdata(int(botid))
    data = find_one(int(botid))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    
    await message.reply_text(
        f"<b><blockquote>⚡️ ᴛᴏᴛᴀʟ ᴜꜱᴇʀ :- {total_user()}\n"
        f"⚡️ ᴛᴏᴛᴀʟ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ :- {total_rename}\n"
        f"⚡️ ᴛᴏᴛᴀʟ ꜱɪᴢᴇ ʀᴇɴᴀᴍᴇᴅ :- {humanbytes(int(total_size))}</blockquote></b>",
        quote=True,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="cancel")]
        ])
    )


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["allids"]))
async def allids(client, message):
    botdata(int(botid))
    data = find_one(int(botid))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    id = str(getid())
    ids = id.split(',')
    
    await message.reply_text(
        f"<b><blockquote>⚡️ ᴀʟʟ ɪᴅꜱ :- {ids}\n\n"
        f"⚡️ ᴛᴏᴛᴀʟ ᴜꜱᴇʀ :- {total_user()}\n"
        f"⚡️ ᴛᴏᴛᴀʟ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ :- {total_rename}\n"
        f"⚡️ ᴛᴏᴛᴀʟ ꜱɪᴢᴇ ʀᴇɴᴀᴍᴇᴅ :- {humanbytes(int(total_size))}</blockquote></b>",
        quote=True,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="cancel")]
        ])
    )
