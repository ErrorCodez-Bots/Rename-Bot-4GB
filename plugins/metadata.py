import os
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from helper.database import *
from pyromod.exceptions import ListenerTimeout
from config import DONATE_PIC, DONATE_TXT

# ----------------- ᴍᴇᴛᴀᴅᴀᴛᴀ ʜᴀɴᴅʟᴇʀꜱ -----------------

def get_metadata_markup(bool_metadata):
    if bool_metadata:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton('ꜱᴇᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ', callback_data='custom_metadata'),
             InlineKeyboardButton('ᴀᴅᴅ ʏᴏᴜʀ ꜱɪᴛᴇ', callback_data='add_site')],
            [InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏɴ ✔', callback_data='metadata_0')]
        ])
    else:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton('ꜱᴇᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ', callback_data='custom_metadata'),
             InlineKeyboardButton('ᴀᴅᴅ ʏᴏᴜʀ ꜱɪᴛᴇ', callback_data='add_site')],
            [InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏꜰꜰ ❌', callback_data='metadata_1')]
        ])

@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):
    ms = await message.reply_text("**ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...**", reply_to_message_id=message.id)
    user_id = int(message.chat.id)
    
    user_data = find(user_id)
    bool_metadata = user_data[2] if len(user_data) > 2 else False
    user_metadata_code = user_data[3] if len(user_data) > 3 and user_data[3] else "Not Set"
    user_site = user_data[4] if len(user_data) > 4 and user_data[4] else "Not Set"
    
    await ms.delete()
    
    text = (
        f"<b>ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ :- </b> ❞\n\n"
        f"• {user_metadata_code}\n\n"
        f"<b>ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ꜱɪᴛᴇ :- </b>\n\n"
        f"• {user_site}"
    )
    
    await message.reply_text(text, quote=True, reply_markup=get_metadata_markup(bool_metadata), disable_web_page_preview=True)


@Client.on_callback_query(filters.regex('.*?(custom_metadata|metadata|add_site).*?'))
async def query_metadata(bot: Client, query: CallbackQuery):
    data = query.data
    user_id = int(query.message.chat.id)
    user_data = find(user_id)
    
    bool_metadata = user_data[2] if len(user_data) > 2 else False
    user_metadata_code = user_data[3] if len(user_data) > 3 and user_data[3] else "Not Set"
    user_site = user_data[4] if len(user_data) > 4 and user_data[4] else "Not Set"

    text = (
        f"<b>ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ :- </b> ❞\n\n"
        f"• {user_metadata_code}\n\n"
        f"<b>ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ꜱɪᴛᴇ :- </b>\n\n"
        f"• {user_site}"
    )

    if data.startswith('metadata_'):
        _bool = data.split('_')[1]

        if bool(eval(_bool)):
            setmeta(user_id, bool_meta=False)
            await query.message.edit_text(text, reply_markup=get_metadata_markup(False), disable_web_page_preview=True)
        else:
            setmeta(user_id, bool_meta=True)
            await query.message.edit_text(text, reply_markup=get_metadata_markup(True), disable_web_page_preview=True)

    elif data == 'custom_metadata':
        await query.message.delete()
        try:
            try:
                metadata = await bot.ask(
                    text="**ꜱᴇɴᴅ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ...\n\nᴇxᴀᴍᴘʟᴇ:- ʙʏ:- @ᴜɴʀᴀᴛᴇᴅ_ᴄᴏᴅᴇʀ\n\n_ᴛʏᴩᴇ /ᴄᴀɴᴄᴇʟ ᴛᴏ ꜱᴛᴏᴩ._**", 
                    chat_id=query.from_user.id, 
                    filters=filters.text, 
                    timeout=30, 
                    disable_web_page_preview=True, 
                    reply_to_message_id=query.message.id
                )
            except ListenerTimeout:
                await query.message.reply_text("⚠️ ᴇʀʀᴏʀ !!\n\n**ʀᴇǫᴜᴇꜱᴛ ᴛɪᴍᴇᴅ ᴏᴜᴛ.**\n\nʀᴇꜱᴛᴀʀᴛ ʙʏ ᴜꜱɪɴɢ /metadata", reply_to_message_id=query.message.id)
                return
            
            if metadata.text.lower() == '/cancel':
                return await metadata.reply_text("ᴘʀᴏᴄᴇꜱꜱ ᴄᴀɴᴄᴇʟʟᴇᴅ.")
                
            ms = await query.message.reply_text("**ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...**", reply_to_message_id=metadata.id)
            setmetacode(user_id, metadata_code=metadata.text)
            await ms.edit("**ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ ꜱᴇᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✅**")
        except Exception as e:
            print(e)

    elif data == 'add_site':
        await query.message.delete()
        try:
            try:
                site_msg = await bot.ask(
                    text="**ꜱᴇɴᴅ ʏᴏᴜʀ ꜱɪᴛᴇ ᴜʀʟ ᴏʀ ɴᴀᴍᴇ ᴛᴏ ꜱᴇᴛ ɪɴ ᴍᴇᴛᴀᴅᴀᴛᴀ\n\nᴇxᴀᴍᴘʟᴇ:- ʜᴛᴛᴩꜱ://ᴡᴡᴡ.ᴀɴɪʀᴇᴀʟ-ᴀɴɪᴍᴇ.ᴛᴏᴩ/\n\n_ᴛʏᴩᴇ /ᴄᴀɴᴄᴇʟ ᴛᴏ ꜱᴛᴏᴩ._**", 
                    chat_id=query.from_user.id, 
                    filters=filters.text, 
                    timeout=30, 
                    disable_web_page_preview=True, 
                    reply_to_message_id=query.message.id
                )
            except ListenerTimeout:
                await query.message.reply_text("⚠️ ᴇʀʀᴏʀ !!\n\n**ʀᴇǫᴜᴇꜱᴛ ᴛɪᴍᴇᴅ ᴏᴜᴛ.**\n\nʀᴇꜱᴛᴀʀᴛ ʙʏ ᴜꜱɪɴɢ /metadata", reply_to_message_id=query.message.id)
                return
            
            if site_msg.text.lower() == '/cancel':
                return await site_msg.reply_text("ᴘʀᴏᴄᴇꜱꜱ ᴄᴀɴᴄᴇʟʟᴇᴅ.")
                
            ms = await query.message.reply_text("**ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...**", reply_to_message_id=site_msg.id)
            await ms.edit("**ʏᴏᴜʀ ꜱɪᴛᴇ ꜱᴇᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✅**")
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
    is_spoiler = False  
    
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
