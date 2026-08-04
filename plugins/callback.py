import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from database.database import get_user_settings, update_user_setting
from config import *

@Client.on_message(filters.private & filters.command('donate'))
async def donate_message_handler(bot, message):
    admin_val = globals().get('ADMIN', '')
    admin_url = f"tg://openmessage?user_id={admin_val}" if str(admin_val).isdigit() else f"https://t.me/{str(admin_val).replace('@', '')}"
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 ᴀᴅᴍɪɴ", url=admin_url)],
        [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="home"),
         InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
    ])
    if 'DONATE_PIC' in globals() and DONATE_PIC:
        await message.reply_photo(
            photo=DONATE_PIC,
            caption=DONATE_TXT,
            reply_markup=keyboard,
            quote=True
        )
    else:
        await message.reply_text(
            text=DONATE_TXT,
            reply_markup=keyboard,
            disable_web_page_preview=True,
            quote=True
        )

@Client.on_message(filters.private & filters.command('spoiler'))
async def spoiler_message_handler(bot, message):
    is_spoiler = False  # Replace with database query if available, e.g., settings['is_spoiler']
    
    status_text = "ᴇɴᴀʙʟᴇᴅ" if is_spoiler else "ᴅɪꜱᴀʙʟᴇᴅ"
    btn_text = "ᴅɪꜱᴀʙʟᴇ ꜱᴘᴏɪʟᴇʀ" if is_spoiler else "ᴇɴᴀʙʟᴇ ꜱᴘᴏɪʟᴇʀ"
    callback_data = "spoiler_off" if is_spoiler else "spoiler_on"
    
    text = (
        f"<b>ᴍᴇᴅɪᴀ ꜱᴘᴏɪʟᴇʀ ꜱᴇᴛᴛɪɴɢꜱ </b>\n\n"
        f"<b>ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ: {status_text}</b>\n\n"
        f"<b>ɪꜰ ᴇɴᴀʙʟᴇᴅ, ʏᴏᴜʀ ʀᴇɴᴀᴍᴇᴅ ᴍᴇᴅɪᴀ (ᴠɪᴅᴇᴏꜱ) ᴡɪʟʟ ʙᴇ ꜱᴇɴᴛ ᴡɪᴛʜ ᴀ ꜱᴘᴏɪʟᴇʀ ᴇꜰꜰᴇᴄᴛ.</b>"
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(btn_text, callback_data=callback_data)],
        [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="home"), InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
    ])
    
    await message.reply_text(text, reply_markup=keyboard, quote=True)

@Client.on_callback_query(filters.regex('^(home|more|panel|meta_config|rename_mode|thumbnails|caption|format|set_rename_|set_thumb_|help|donate|spoiler_on|spoiler_off|close)$'))
async def cb_handler(bot, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id
    settings = await get_user_settings(user_id)

    # 1. HOME / START MENU
    if data == "home":
        keyboard = InlineKeyboardMarkup([  
            [InlineKeyboardButton("• ᴄʟɪᴄᴋ ꜰᴏʀ ᴍᴏʀᴇ •", callback_data="more")],
            [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
             InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url=UPDATE_CHANNEL)],
            [InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ", callback_data='donate')]
        ])
        await query.message.edit_text(
            text=START_TXT.format(mention=query.from_user.mention), 
            reply_markup=keyboard
        )

    # 2. CLICK FOR MORE MENU
    elif data == "more":
        text = (
            "<b><blockquote>💬 ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ\n\n"
            "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʙᴏᴛ - ʏᴏᴜʀ ᴜʟᴛɪᴍᴀᴛᴇ ꜱᴏʟᴜᴛɪᴏɴ ꜰᴏʀ ʀᴇɴᴀᴍɪɴɢ ᴀɴᴅ ᴏʀɢᴀɴɪᴢɪɴɢ ꜰɪʟᴇꜱ ᴇꜰꜰᴏʀᴛʟᴇꜱꜱʟʏ.\n\n"
            "ᴋᴇʏ ꜰᴇᴀᴛᴜʀᴇꜱ:-\n"
            "• ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴍᴀᴛꜱ: ꜱᴇᴛ ᴘᴇʀꜱᴏɴᴀʟɪᴢᴇᴅ ʀᴇɴᴀᴍɪɴɢ ꜰᴏʀᴍᴀᴛꜱ.\n"
            "• ᴍᴇᴛᴀᴅᴀᴛᴀ ꜱᴜᴘᴘᴏʀᴛ: ᴀᴅᴅ ᴏʀ ᴍᴏᴅɪꜰʏ ᴍᴇᴛᴀᴅᴀᴛᴀ.\n"
            "• ᴄᴀᴘᴛɪᴏɴ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ: ꜱᴇᴛ, ᴄʜᴇᴄᴋ, ᴏʀ ᴅᴇʟᴇᴛᴇ ᴄᴀᴘᴛɪᴏɴꜱ.\n"
            "• ᴛʜᴜᴍʙɴᴀɪʟꜱ: ꜱᴀᴠᴇ, ᴠɪᴇᴡ, ᴏʀ ʀᴇᴘʟᴀᴄᴇ ᴛʜᴜᴍʙɴᴀɪʟꜱ.\n"
            "• ᴅᴜᴍᴘ ᴄʜᴀɴɴᴇʟ: ᴅɪʀᴇᴄᴛʟʏ ꜱᴛᴏʀᴇ ꜰɪʟᴇꜱ ɪɴ A ᴄᴜꜱᴛᴏᴍ ᴄʜᴀɴɴᴇʟ.</blockquote></b>"
        )
        keyboard = InlineKeyboardMarkup([ 
            [InlineKeyboardButton("⚙️ ᴘᴀɴᴇʟ", callback_data='panel'),
             InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data='home')]
        ])
        await query.message.edit_text(text=text, reply_markup=keyboard, disable_web_page_preview=True)

    # 3. USER PANEL
    elif data == "panel":
        text = (
            "<b><blockquote>👤 ᴜꜱᴇʀ ᴘᴀɴᴇʟ\n"
            "ᴜꜱᴇʀ ᴘʟᴀɴ ᴛʏᴘᴇ: [ᴘᴜʙʟɪᴄ ᴜꜱᴇʀ]\n\n"
            f"ᴄᴜʀʀᴇɴᴛ ꜱᴇᴛᴜᴘ:\n"
            f"• ʀᴇɴᴀᴍᴇ ᴍᴏᴅᴇ: {settings['rename_mode']}\n"
            "• ᴍᴇᴅɪᴀ ᴛʏᴘᴇ: ᴀᴜᴛᴏ/ᴘᴇʀ ꜰɪʟᴇ\n"
            "• ᴍᴇᴛᴀᴅᴀᴛᴀ: ᴏꜰꜰ\n"
            f"• ᴍᴀɪɴ ᴛʜᴜᴍʙɴᴀɪʟ: {settings['main_thumb']}\n"
            "• ᴅᴜᴍᴘ ᴄʜᴀɴɴᴇʟ: ɴᴏᴛ ꜱᴇᴛ</blockquote></b>"
        )
        keyboard = InlineKeyboardMarkup([ 
            [InlineKeyboardButton("⚙️ ᴍᴇᴛᴀ ᴄᴏɴꜰɪɢ", callback_data='meta_config')],
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data='more')]
        ])
        await query.message.edit_text(text=text, reply_markup=keyboard)

    # 4. META CONFIG MENU
    elif data == "meta_config":
        text = (
            "<b><blockquote>ᴍᴇᴛᴀ ᴄᴏɴꜰɪɢ\n\n"
            "ᴄᴏɴᴛʀᴏʟ ᴛʜᴇ ʀᴇɴᴀᴍᴇ ꜱᴇᴛᴜᴘ ᴜꜱᴇʀꜱ ᴄʜᴀɴɢᴇ ᴍᴏꜱᴛ ᴏꜰᴛᴇɴ.\n"
            f"• ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴍᴀᴛ: {settings['format']}\n"
            f"• ᴄᴀᴘᴛɪᴏɴ ᴛᴇᴍᴘʟᴀᴛᴇ: {settings['caption']}\n"
            f"• ʀᴇɴᴀᴍᴇ ᴍᴏᴅᴇ: <b>{settings['rename_mode']}</b>\n"
            f"• ᴍᴀɪɴ ᴛʜᴜᴍʙɴᴀɪʟ: <b>{settings['main_thumb']}</b>\n"
            f"• ǫᴜᴀʟɪᴛʏ ᴛʜᴜᴍʙꜱ: <b>{settings['quality_thumbs']}</b>\n"
            f"• ᴄᴏᴘʏ ꜱᴏᴜʀᴄᴇ ꜰɪʟᴇ ᴛʜᴜᴍʙ: <b>{settings['copy_source_thumb']}</b>\n\n"
            "ᴜꜱᴇ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ǫᴜɪᴄᴋ ꜱᴇᴛᴜᴘ.</blockquote></b>"
        )
        keyboard = InlineKeyboardMarkup([ 
            [InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ ᴍᴏᴅᴇ", callback_data='rename_mode'),
             InlineKeyboardButton("🖼️ ᴛʜᴜᴍʙɴᴀɪʟꜱ", callback_data='thumbnails')],
            [InlineKeyboardButton("✍️ ᴄᴀᴘᴛɪᴏɴ", callback_data='caption'),
             InlineKeyboardButton("⚙️ ꜰᴏʀᴍᴀᴛ", callback_data='format')],
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data='panel'),
             InlineKeyboardButton("🏠 ʜᴏᴍᴇ", callback_data='home'),
             InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data='close')]
        ])
        await query.message.edit_text(text=text, reply_markup=keyboard)

    # 5. RENAME MODE MENU & ACTIONS
    elif data == "rename_mode":
        text = (
            "<b><blockquote>📝 ʀᴇɴᴀᴍᴇ ᴍᴏᴅᴇ\n\n"
            f"ᴄᴜʀʀᴇɴᴛ ᴍᴏᴅᴇ: <b>{settings['rename_mode']}</b>\n\n"
            "• ꜰɪʟᴇɴᴀᴍᴇ ᴍᴏᴅᴇ: ᴄʜᴀɴɢᴇꜱ ᴛʜᴇ ᴀᴄᴛᴜᴀʟ ꜰɪʟᴇ ɴᴀᴍᴇ.\n"
            "• ᴄᴀᴘᴛɪᴏɴ ᴍᴏᴅᴇ: ᴋᴇᴇᴘꜱ ᴛʜᴇ ꜰɪʟᴇ ɴᴀᴍᴇ, ʙᴜᴛ ᴀᴅᴅꜱ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n"
            "• ᴀᴜᴛᴏ ᴅᴇᴛᴇᴄᴛ ᴍᴏᴅᴇ: ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇᴛᴇᴄᴛꜱ ᴀɴᴅ ᴀᴘᴘʟɪᴇꜱ ꜱᴇᴛᴛɪɴɢꜱ.</blockquote></b>"
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("ꜰɪʟᴇ ɴᴀᴍᴇ", callback_data="set_rename_FILENAME"),
             InlineKeyboardButton("ᴄᴀᴘᴛɪᴏɴ", callback_data="set_rename_CAPTION"),
             InlineKeyboardButton("ᴀᴜᴛᴏ ᴅᴇᴛᴇᴄᴛ", callback_data="set_rename_AUTODETECT")],
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data='meta_config'),
             InlineKeyboardButton("🏠 ʜᴏᴍᴇ", callback_data='home'),
             InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data='close')]
        ])
        await query.message.edit_text(text=text, reply_markup=keyboard)

    elif data.startswith("set_rename_"):
        new_mode = data.split("_")[2]
        await update_user_setting(user_id, "rename_mode", new_mode)
        await query.answer(f"Rename Mode set to {new_mode}!")
        query.data = "rename_mode"
        await cb_handler(bot, query)

    # 6. THUMBNAILS MENU & ACTIONS
    elif data == "thumbnails":
        text = (
            "<b><blockquote>🖼️ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴇᴛᴛɪɴɢꜱ\n\n"
            f"• ᴍᴀɪɴ ᴛʜᴜᴍʙ: <b>{settings['main_thumb']}</b>\n"
            f"• ǫᴜᴀʟɪᴛʏ ᴛʜᴜᴍʙꜱ: <b>{settings['quality_thumbs']}</b>\n"
            f"• ᴄᴏᴘʏ ꜱᴏᴜʀᴄᴇ ᴛʜᴜᴍʙ: <b>{settings['copy_source_thumb']}</b>\n\n"
            "ᴄᴏɴꜰɪɢᴜʀᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟꜱ ʙᴇʟᴏᴡ.</blockquote></b>"
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("ꜱᴇᴛ ᴍᴀɪɴ", callback_data="set_thumb_main"),
             InlineKeyboardButton("ᴄᴏᴘʏ ᴛʜᴜᴍʙ", callback_data="set_thumb_copy")],
            [InlineKeyboardButton("ᴠɪᴇᴡ ᴍᴀɪɴ", callback_data="view_main"),
             InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ ᴍᴀɪɴ", callback_data="delete_main")],
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data='meta_config'),
             InlineKeyboardButton("🏠 ʜᴏᴍᴇ", callback_data='home'),
             InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data='close')]
        ])
        await query.message.edit_text(text=text, reply_markup=keyboard)

    elif data == "set_thumb_main":
        new_val = not settings['main_thumb']
        await update_user_setting(user_id, "main_thumb", new_val)
        await query.answer(f"Main Thumb set to {new_val}!")
        query.data = "thumbnails"
        await cb_handler(bot, query)

    # 7. CAPTION MENU
    elif data == "caption":
        text = (
            f"<b><blockquote>💬 ᴄᴀᴘᴛɪᴏɴ ꜱᴇᴛᴛɪɴɢꜱ\n\n"
            f"ᴄᴜʀʀᴇɴᴛ ᴄᴀᴘᴛɪᴏɴ: <b>{settings['caption']}</b></blockquote></b>\n\n"
            "<b><blockquote>ᴛᴏ ꜱᴇᴛ ᴀ ɴᴇᴡ ᴄᴀᴘᴛɪᴏɴ, ᴜꜱᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ:\n"
            "<code>/set_caption Your caption here</code>\n\n"
            "ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴀɢꜱ: {filename}, {title}, {episode}, {season}, {quality}, {chapter}, {audio}</blockquote></b>"
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="meta_config"),
             InlineKeyboardButton("🏠 ʜᴏᴍᴇ", callback_data="home"),
             InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
        ])
        await query.message.edit_text(text=text, reply_markup=keyboard)

    # 8. FORMAT MENU
    elif data == "format":
        text = (
            f"<b><blockquote>⚙️ ꜰᴏʀᴍᴀᴛ ꜱᴇᴛᴛɪɴɢꜱ\n\n"
            f"ᴄᴜʀʀᴇɴᴛ ꜰᴏʀᴍᴀᴛ: <b>{settings['format']}</b></blockquote></b>\n\n"
            "<b><blockquote>ᴛᴏ ꜱᴇᴛ ᴀ ɴᴇᴡ ꜰᴏʀᴍᴀᴛ, ᴜꜱᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ:\n"
            "<code>/set_format Your format here</code>\n\n"
            "ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴀɢꜱ: {filename}, {title}, {episode}, {season}, {quality}, {chapter}, {audio}</blockquote></b>"
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="meta_config"),
             InlineKeyboardButton("🏠 ʜᴏᴍᴇ", callback_data="home"),
             InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
        ])
        await query.message.edit_text(text=text, reply_markup=keyboard)

    # 9. HELP MENU
    elif data == "help":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="home"),
             InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
        ])
        await query.message.edit_text(
            text=HELP_TXT,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

    # 10. DONATE MENU
    elif data == "donate":
        admin_val = globals().get('ADMIN', '')
        admin_url = f"tg://openmessage?user_id={admin_val}" if str(admin_val).isdigit() else f"https://t.me/{str(admin_val).replace('@', '')}"
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🦋 ᴀᴅᴍɪɴ", url=admin_url)],
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="home"),
             InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
        ])
        if 'DONATE_PIC' in globals() and DONATE_PIC:
            try:
                await query.message.edit_media(
                    media=InputMediaPhoto(media=DONATE_PIC, caption=DONATE_TXT),
                    reply_markup=keyboard
                )
            except Exception:
                await query.message.edit_text(
                    text=DONATE_TXT,
                    reply_markup=keyboard,
                    disable_web_page_preview=True
                )
        else:
            await query.message.edit_text(
                text=DONATE_TXT,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )

    # 11. SPOILER TOGGLE HANDLERS
    elif data in ["spoiler_on", "spoiler_off"]:
        is_spoiler = True if data == "spoiler_on" else False
        
        status_text = "ᴇɴᴀʙʟᴇᴅ" if is_spoiler else "ᴅɪꜱᴀʙʟᴇᴅ"
        btn_text = "ᴅɪꜱᴀʙʟᴇ ꜱᴘᴏɪʟᴇʀ" if is_spoiler else "ᴇɴᴀʙʟᴇ ꜱᴘᴏɪʟᴇʀ"
        callback_data = "spoiler_off" if is_spoiler else "spoiler_on"
        
        text = (
            f"<b>ᴍᴇᴅɪᴀ ꜱᴘᴏɪʟᴇʀ ꜱᴇᴛᴛɪɴɢꜱ </b>\n\n"
            f"<b>ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ: {status_text}</b>\n\n"
            f"<b>ɪꜰ ᴇɴᴀʙʟᴇᴅ, ʏᴏᴜʀ ʀᴇɴᴀᴍᴇᴅ ᴍᴇᴅɪᴀ (ᴠɪᴅᴇᴏꜱ) ᴡɪʟʟ ʙᴇ ꜱᴇɴᴛ ᴡɪᴛʜ ᴀ ꜱᴘᴏɪʟᴇʀ ᴇꜰꜰᴇᴄᴛ.</b>"
        )
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(btn_text, callback_data=callback_data)],
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="home"), InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
        ])
        
        await query.message.edit_text(text, reply_markup=keyboard)

    # 12. CLOSE
    elif data == "close":
        await query.message.delete()
