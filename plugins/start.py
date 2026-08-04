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
            msg = await message_or_query.message.reply_text("<code>Loading.</code>")
        else:
            msg = await message_or_query.reply_text("<code>Loading.</code>")
            
        await asyncio.sleep(0.4)
        await msg.edit_text("<code>Loading..</code>")
        await asyncio.sleep(0.4)
        await msg.edit_text("<code>Loading...</code>")
        await asyncio.sleep(0.4)
        return msg
    except Exception:
        return None


# Main Menu Buttons Generator
def get_main_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("• CLICK FOR MORE •", callback_data="more")],
        [
            InlineKeyboardButton("HELP", callback_data='help'),
            InlineKeyboardButton("UPDATES", url=UPDATE_CHANNEL)
        ],
        [InlineKeyboardButton("DONATE", callback_data='donate')]
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
            await message.reply_text(
                "<b>Hello Dear \n\nYou Need To Join In My Channel To Use Me\n\nKindly Please Join Channel</b>",
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔺 Update Channel 🔺", url=f"https://t.me/{f_sub}")],
                    [InlineKeyboardButton("🔄 Try Again", callback_data="try_again")]
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
                await query.message.reply_text(
                    "<b>Hello Dear \n\nYou Need To Join In My Channel To Use Me\n\nKindly Please Join Channel</b>",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🔺 Update Channel 🔺", url=f"https://t.me/{f_sub}")],
                        [InlineKeyboardButton("🔄 Try Again", callback_data="try_again")]
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
        text = globals().get('MORE_TXT', "<b>• CLICK FOR MORE DETAILS •</b>")
        button = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("< BACK", callback_data="back"),
                InlineKeyboardButton("CLOSE ×", callback_data="close")
            ]
        ])
        await query.message.edit_text(text=text, reply_markup=button, disable_web_page_preview=True)

    # Help Menu
    elif data == "help":
        text = HELP_TXT
        button = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("< BACK", callback_data="back"),
                InlineKeyboardButton("CLOSE ×", callback_data="close")
            ]
        ])
        await query.message.edit_text(text=text, reply_markup=button, disable_web_page_preview=True)

    # Donate Menu
    elif data == "donate":
        text = globals().get('DONATE_TXT', "<b>Support the developer by donating! ❤️</b>")
        owner_link = globals().get('OWNER_LINK', 'https://t.me/ST_Rename_Update')
        button = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ADMIN 👑", url=owner_link),
                InlineKeyboardButton("CLOSE ×", callback_data="close")
            ],
            [
                InlineKeyboardButton("< BACK", callback_data="back")
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
            await message.reply_text(
                "<b>Hello Dear \n\nYou Need To Join In My Channel To Use Me\n\nKindly Please Join Channel</b>",
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔺 Update Channel 🔺", url=f"https://t.me/{f_sub}")],
                    [InlineKeyboardButton("🔄 Try Again", callback_data="try_again")]
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
                    f"<b>Flood Control Is Active. Please Wait For {ltime} </b>", 
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
        dcid = "Unknown"

    filename = getattr(file, 'file_name', 'media_file')

    # 4GB Check
    if file.file_size > FOUR_GB:
        await message.reply_text("You Can't Upload Files Larger Than 4GB.")
        return

    # Check for String Session for files > 2GB
    string_sess = globals().get('STRING_SESSION', None)
    if file.file_size > 2147483648 and not string_sess:
        await message.reply_text("Cannot Process Files Larger Than 2GB Without Userbot String Session Configured.")
        return

    filesize = humanize.naturalsize(file.file_size)
    
    try:
        total_rename(int(botid), prrename)
        total_size(int(botid), prsize, file.file_size)
    except Exception:
        pass

    await message.reply_text(
        f"__What Do You Want Me To Do With This File ?__\n\n"
        f"**File Name :** `{filename}`\n"
        f"**File Size :** {filesize}\n"
        f"**DC ID :** {dcid}",
        reply_to_message_id=message.id,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📝 Rename", callback_data="rename"),
             InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    )

