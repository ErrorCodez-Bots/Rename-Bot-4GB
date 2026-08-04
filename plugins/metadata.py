import os
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from helper.database import *
from pyromod.exceptions import ListenerTimeout
from config import DONATE_PIC, DONATE_TXT

# ----------------- ᴍᴇᴛᴀᴅᴀᴛᴀ ʜᴀɴᴅʟᴇʀꜱ -----------------

ON = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏɴ ✅', callback_data='metadata_1')], [
    InlineKeyboardButton('ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ', callback_data='cutom_metadata')]]
OFF = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏꜰꜰ ❌', callback_data='metadata_0')], [
    InlineKeyboardButton('ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ', callback_data='cutom_metadata')]]


@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):
    ms = await message.reply_text("**ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...**", reply_to_message_id=message.id)
    bool_metadata = find(int(message.chat.id))[2]
    user_metadata = find(int(message.chat.id))[3]
    await ms.delete()
    if bool_metadata:
        return await message.reply_text(f"**ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ :-**\n\n➜ `{user_metadata}` ", quote=True, reply_markup=InlineKeyboardMarkup(ON))
    return await message.reply_text(f"**ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ :-**\n\n➜ `{user_metadata}` ", quote=True, reply_markup=InlineKeyboardMarkup(OFF))


@Client.on_callback_query(filters.regex('.*?(custom_metadata|metadata).*?'))
async def query_metadata(bot: Client, query: CallbackQuery):
    data = query.data

    if data.startswith('metadata_'):
        _bool = data.split('_')[1]
        user_metadata = find(int(query.message.chat.id))[3]

        if bool(eval(_bool)):
            setmeta(int(query.message.chat.id), bool_meta=False)
            await query.message.edit(f"**ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ :-**\n\n➜ `{user_metadata}` ", reply_markup=InlineKeyboardMarkup(OFF))

        else:
            setmeta(int(query.message.chat.id), bool_meta=True)
            await query.message.edit(f"**ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ :-**\n\n➜ `{user_metadata}` ", reply_markup=InlineKeyboardMarkup(ON))

    elif data == 'cutom_metadata':
        await query.message.delete()
        try:
            try:
                metadata = await bot.ask(text=script.METADATA_TXT, chat_id=query.from_user.id, filters=filters.text, timeout=30, disable_web_page_preview=True, reply_to_message_id=query.message.id)
            except ListenerTimeout:
                await query.message.reply_text("⚠️ ᴇʀʀᴏʀ !!\n\n**ʀᴇǫᴜᴇꜱᴛ ᴛɪᴍᴇᴅ ᴏᴜᴛ.**\n\nʀᴇꜱᴛᴀʀᴛ ʙʏ ᴜꜱɪɴɢ /metadata", reply_to_message_id=query.message.id)
                return
            print(metadata.text)
            ms = await query.message.reply_text("**ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...**", reply_to_message_id=metadata.id)
            setmetacode(int(query.message.chat.id), metadata_code=metadata.text)
            await ms.edit("**ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ ꜱᴇᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✅**")
        except Exception as e:
            print(e)


# ----------------- ᴅᴏɴᴀᴛᴇ ʜᴀɴᴅʟᴇʀꜱ -----------------

@Client.on_message(filters.private & filters.command('donate'))
async def donate_handler(bot: Client, message: Message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 ᴀᴅᴍɪɴ", url="https://t.me/ST_Rename_Update"),
         InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
    ])
    await message.reply_photo(
        photo=DONATE_PIC,
        caption=DONATE_TXT,
        reply_markup=buttons,
        quote=True
    )


@Client.on_callback_query(filters.regex('^donate$'))
async def donate_callback(bot: Client, query: CallbackQuery):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 ᴀᴅᴍɪɴ", url="https://t.me/ST_Rename_Update"),
         InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
    ])
    await query.message.edit_media(
        media=InputMediaPhoto(media=DONATE_PIC, caption=DONATE_TXT),
        reply_markup=buttons
    )


# ----------------- ꜱᴘᴏɪʟᴇʀ ʜᴀɴᴅʟᴇʀꜱ -----------------

@Client.on_message(filters.private & filters.command('spoiler'))
async def spoiler_settings(bot: Client, message: Message):
    is_spoiler = False  # Replace with database function if available
    
    status_text = "ᴇɴᴀʙʟᴇᴅ" if is_spoiler else "ᴅɪꜱᴀʙʟᴇᴅ"
    btn_text = "ᴅɪꜱᴀʙʟᴇ ꜱᴘᴏɪʟᴇʀ" if is_spoiler else "ᴇɴᴀʙʟᴇ ꜱᴘᴏɪʟᴇʀ"
    callback_data = "spoiler_off" if is_spoiler else "spoiler_on"
    
    text = (
        f"<b>ᴍᴇᴅɪᴀ ꜱᴘᴏɪʟᴇʀ ꜱᴇᴛᴛɪɴɢꜱ </b>\n\n"
        f"<b>ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ: {status_text}</b>\n\n"
        f"<b>ɪꜰ ᴇɴᴀʙʟᴇᴅ, ʏᴏᴜʀ ʀᴇɴᴀᴍᴇᴅ ᴍᴇᴅɪᴀ (ᴠɪᴅᴇᴏꜱ) ᴡɪʟʟ ʙᴇ ꜱᴇɴᴛ ᴡɪᴛʜ ᴀ ꜱᴘᴏɪʟᴇʀ ᴇꜰꜰᴇᴄᴛ.</b>"
    )
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton(btn_text, callback_data=callback_data)],
        [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help"), InlineKeyboardButton("ᴄʟᴏꜱᴇ ✖", callback_data="close")]
    ])
    
    await message.reply_text(text, reply_markup=buttons, quote=True)


@Client.on_callback_query(filters.regex('^spoiler_(on|off)$'))
async def toggle_spoiler(bot: Client, query: CallbackQuery):
    action = query.data.split('_')[1]
    is_spoiler = True if action == 'on' else False
    
    status_text = "ᴇɴᴀʙʟᴇᴅ" if is_spoiler else "ᴅɪꜱᴀʙʟᴇᴅ"
    btn_text = "ᴅɪꜱᴀʙʟᴇ ꜱᴘᴏɪʟᴇʀ" if is_spoiler else "ᴇɴᴀʙʟᴇ ꜱᴘᴏɪʟᴇʀ"
    callback_data = "spoiler_off" if is_spoiler else "spoiler_on"
    
    text = (
        f"<b>ᴍᴇᴅɪᴀ ꜱᴘᴏɪʟᴇʀ ꜱᴇᴛᴛɪɴɢꜱ </b>\n\n"
        f"<b>ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ: {status_text}</b>\n\n"
        f"<b>ɪꜰ ᴇɴᴀʙʟᴇᴅ, ʏᴏᴜʀ ʀᴇɴᴀᴍᴇᴅ ᴍᴇᴅɪᴀ (ᴠɪᴅᴇᴏꜱ) ᴡɪʟʟ ʙᴇ ꜱᴇɴᴛ ᴡɪᴛʜ ᴀ ꜱᴘᴏɪʟᴇʀ ᴇꜰꜰᴇᴄᴛ.</b>"
    )
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton(btn_text, callback_data=callback_data)],
        [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="help"), InlineKeyboardButton("ᴄʟᴏꜱᴇ ✖", callback_data="close")]
    ])
    
    await query.message.edit_text(text, reply_markup=buttons)


# ----------------- ᴄʟᴏꜱᴇ ᴄᴀʟʟʙᴀᴄᴋ -----------------

@Client.on_callback_query(filters.regex('^close$'))
async def close_callback(bot: Client, query: CallbackQuery):
    await query.message.delete()
