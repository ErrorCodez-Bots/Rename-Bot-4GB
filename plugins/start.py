import os, re, datetime, random, asyncio, time, humanize
from datetime import date as date_
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from helper.progress import humanbytes
from helper.database import (
    botdata, find_one, total_user, insert, 
    used_limit, uploadlimit, addpredata, total_rename, total_size
)
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from config import *

token = BOT_TOKEN
botid = token.split(':')[0]

# 4GB in Bytes
FOUR_GB = 4294967296

# Helper function for Loading Animation
async def play_loading_animation(message_or_query):
    try:
        if isinstance(message_or_query, CallbackQuery):
            msg = await message_or_query.message.reply_text("<code>ʟᴏᴀᴅɪɴɢ.</code>")
        else:
            msg = await message_or_query.reply_text("<code>ʟᴏᴀᴅɪɴɢ.</code>")
            
        await asyncio.sleep(0.4)
        await msg.edit_text("<code>ʟᴏᴀᴅɪɴɢ..</code>")
        await asyncio.sleep(0.4)
        await msg.edit_text("<code>ʟᴏᴀᴅɪɴɢ...</code>")
        await asyncio.sleep(0.4)
        return msg
    except Exception:
        return None


# Main Menu Buttons Generator
def get_main_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("• ᴄʟɪᴄᴋ ꜰᴏʀ ᴍᴏʀᴇ •", callback_data="more")],
        [
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url=UPDATE_CHANNEL)
        ],
        [InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ", callback_data='donate')]
    ])


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user_id = message.chat.id
    try:
        insert(int(user_id))
    except Exception:
        pass
    
    # 1. Run Loading Animation
    loading_msg = await play_loading_animation(message)
    
    # Clean Force Sub Channel Username
    f_sub = FORCE_SUBS.replace("@", "") if FORCE_SUBS else None

    # 2. Check Force Subscription after loading
    if f_sub:
        try:
            await client.get_chat_member(f_sub, user_id)
        except UserNotParticipant:
            if loading_msg:
                await loading_msg.delete()
            
            # Fetch Force Sub Message from config.py
            force_text = globals().get('FORCE_SUB_TEXT', "<b>ʜᴇʟʟᴏ {first_name} 👋\n\nʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ.\n\nᴋɪɴᴅʟʏ ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ʙᴇʟᴏᴡ!</b>")
            
            await message.reply_text(
                force_text.format(first_name=message.from_user.first_name),
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔺 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🔺", url=f"https://t.me/{f_sub}")],
                    [InlineKeyboardButton("🔄 ᴛʀʏ ᴀɢᴀɪɴ", callback_data="try_again")]
                ])
            )
            return
        except Exception:
            pass

    # 3. Show Start Text & Buttons
    text = START_TXT.format(mention=message.from_user.mention)
    button = get_main_buttons()
    
    if loading_msg:
        await loading_msg.delete()

    if START_PIC:
        try:
            await message.reply_photo(
                photo=START_PIC,
                caption=text,
                reply_markup=button,
                quote=True
            )
            return
        except Exception:
            pass

    await message.reply_text(
        text=text,
        reply_markup=button,
        quote=True
    )


@Client.on_callback_query(filters.regex("^(about|help|home|back|donate|more|close|cancel|try_again)$"))
async def callback_handler(client, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id
    f_sub = FORCE_SUBS.replace("@", "") if FORCE_SUBS else None
    
    # Try Again (Force Sub)
    if data == "try_again":
        await query.message.delete()
        loading_msg = await play_loading_animation(query)
        
        if f_sub:
            try:
                await client.get_chat_member(f_sub, user_id)
            except UserNotParticipant:
                if loading_msg:
                    await loading_msg.delete()
                
                # Fetch Force Sub Message from config.py
                force_text = globals().get('FORCE_SUB_TEXT', "<b>ʜᴇʟʟᴏ {first_name} 👋\n\nʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ.\n\nᴋɪɴᴅʟʏ ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ʙᴇʟᴏᴡ!</b>")

                await query.message.reply_text(
                    force_text.format(first_name=query.from_user.first_name),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🔺 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🔺", url=f"https://t.me/{f_sub}")],
                        [InlineKeyboardButton("🔄 ᴛʀʏ ᴀɢᴀɪɴ", callback_data="try_again")]
                    ])
                )
                return
            except Exception:
                pass

        if loading_msg:
            await loading_msg.delete()

        text = START_TXT.format(mention=query.from_user.mention)
        button = get_main_buttons()
        
        if START_PIC:
            try:
                await client.send_photo(
                    chat_id=query.message.chat.id,
                    photo=START_PIC,
                    caption=text,
                    reply_markup=button
                )
                return
            except Exception:
                pass

        await query.message.reply_text(text=text, reply_markup=button)

    # Home / Back
    elif data in ["home", "back"]:
        text = START_TXT.format(mention=query.from_user.mention)
        button = get_main_buttons()
        await query.message.edit_text(text=text, reply_markup=button)

    # Click For More
    elif data == "more":
        text = globals().get('MORE_TXT', "<b>• ᴄʟɪᴄᴋ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ •</b>")
        button = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("< ʙᴀᴄᴋ", callback_data="back"),
                InlineKeyboardButton("ᴄʟᴏꜱᴇ ×", callback_data="close")
            ]
        ])
        await query.message.edit_text(text=text, reply_markup=button, disable_web_page_preview=True)

    # Help Menu
    elif data == "help":
        text = HELP_TXT
        button = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("< ʙᴀᴄᴋ", callback_data="back"),
                InlineKeyboardButton("ᴄʟᴏꜱᴇ ×", callback_data="close")
            ]
        ])
        await query.message.edit_text(text=text, reply_markup=button, disable_web_page_preview=True)

    # Donate Menu (Fetches DONATE_TXT from config.py)
    elif data == "donate":
        text = DONATE_TXT
        button = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("< ʙᴀᴄᴋ", callback_data="back"),
                InlineKeyboardButton("ᴄʟᴏꜱᴇ ×", callback_data="close")
            ]
        ])
        await query.message.edit_text(text=text, reply_markup=button, disable_web_page_preview=True)

    # Close Menu
    elif data in ["close", "cancel"]:
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception:
            pass


@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    chat_id = message.chat.id
    from_user = message.from_user
    user_id = from_user.id if from_user else chat_id

    try:
        insert(int(user_id))
    except Exception:
        pass
        
    f_sub = FORCE_SUBS.replace("@", "") if FORCE_SUBS else None

    if f_sub and from_user:
        try:
            await client.get_chat_member(f_sub, user_id)
        except UserNotParticipant:
            # Fetch Force Sub Message from config.py
            force_text = globals().get('FORCE_SUB_TEXT', "<b>ʜᴇʟʟᴏ {first_name} 👋\n\nʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ.\n\nᴋɪɴᴅʟʏ ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ʙᴇʟᴏᴡ!</b>")

            await message.reply_text(
                force_text.format(first_name=message.from_user.first_name),
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔺 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🔺", url=f"https://t.me/{f_sub}")],
                    [InlineKeyboardButton("🔄 ᴛʀʏ ᴀɢᴀɪɴ", callback_data="try_again")]
                ])
            )
            return
        except Exception:
            pass

    try:
        botdata(int(botid))
        bot_data = find_one(int(botid))
        prrename = bot_data.get('total_rename', 0)
        prsize = bot_data.get('total_size', 0)
        
        user_deta = find_one(user_id)
        used_date = user_deta.get("date", 0) if user_deta else 0

        c_time = time.time()
        LIMIT = 10  # Standard flood limit
        
        if used_date and isinstance(used_date, (int, float)):
            then = used_date + LIMIT
            left = round(then - c_time)
            if left > 0:
                ltime = str(datetime.timedelta(seconds=left))
                await message.reply_text(
                    f"<b>ꜰʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ ɪꜱ ᴀᴄᴛɪᴠᴇ. ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜰᴏʀ {ltime} </b>", 
                    reply_to_message_id=message.id
                )
                return
    except Exception:
        pass

    media = await client.get_messages(chat_id, message.id)
    file = media.document or media.video or media.audio
    
    if not file:
        return

    try:
        dcid = FileId.decode(file.file_id).dc_id
    except Exception:
        dcid = "ᴜɴᴋɴᴏᴡɴ"

    filename = getattr(file, 'file_name', 'media_file')

    # 4GB Check
    if file.file_size > FOUR_GB:
        await message.reply_text("ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ꜰɪʟᴇꜱ ʟᴀʀɢᴇʀ ᴛʜᴀɴ 4ɢʙ.")
        return

    # Check for String Session for files > 2GB
    string_sess = globals().get('STRING_SESSION', None)
    if file.file_size > 2147483648 and not string_sess:
        await message.reply_text("ᴄᴀɴɴᴏᴛ ᴘʀᴏᴄᴇꜱꜱ ꜰɪʟᴇꜱ ʟᴀʀɢᴇʀ ᴛʜᴀɴ 2ɢʙ ᴡɪᴛʜᴏᴜᴛ ᴜꜱᴇʀʙᴏᴛ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴄᴏɴꜰɪɢᴜʀᴇᴅ.")
        return

    filesize = humanize.naturalsize(file.file_size)
    
    try:
        total_rename(int(botid), prrename)
        total_size(int(botid), prsize, file.file_size)
    except Exception:
        pass

    await message.reply_text(
        f"__ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪꜱ ꜰɪʟᴇ ?__\n\n"
        f"**ꜰɪʟᴇ ɴᴀᴍᴇ :** `{filename}`\n"
        f"**ꜰɪʟᴇ ꜱɪᴢᴇ :** {filesize}\n"
        f"**ᴅᴄ ɪᴅ :** {dcid}",
        reply_to_message_id=message.id,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ", callback_data="rename"),
             InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ", callback_data="cancel")]
        ])
    )
