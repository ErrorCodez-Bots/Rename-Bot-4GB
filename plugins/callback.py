import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from database.database import get_user_settings, update_user_setting
from config import *

@Client.on_callback_query(filters.regex('^(home|more|panel|meta_config|rename_mode|thumbnails|caption|format|set_rename_|set_thumb_|help|donate|close)$'))
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
            "<b><blockquote>META CONFIG\n\n"
            "Control the rename setup users change most often.\n"
            f"• Custom format: {settings['format']}\n"
            f"• Caption template: {settings['caption']}\n"
            f"• Rename mode: <b>{settings['rename_mode']}</b>\n"
            f"• Main thumbnail: <b>{settings['main_thumb']}</b>\n"
            f"• Quality thumbs: <b>{settings['quality_thumbs']}</b>\n"
            f"• Copy source file thumb: <b>{settings['copy_source_thumb']}</b>\n\n"
            "Use buttons for quick setup.</blockquote></b>"
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
            "<b><blockquote>📝 RENAME MODE\n\n"
            f"Current mode: <b>{settings['rename_mode']}</b>\n\n"
            "• FILENAME MODE: Changes the actual file name.\n"
            "• CAPTION MODE: Keeps the file name, but adds a custom caption.\n"
            "• AUTO DETECT MODE: Automatically detects and applies settings.</blockquote></b>"
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("ꜰɪʟᴇ ɴᴀᴍᴇ", callback_data="set_rename_FILENAME"),
             InlineKeyboardButton("ᴄᴀᴘᴛɪᴏɴ", callback_data="set_rename_CAPTION"),
             InlineKeyboardButton("ᴀᴜᴛᴏ ᴅᴇᴛᴇᴄᴛ", callback_data="set_rename_AUTODETECT")],
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="meta_config"),
             InlineKeyboardButton("🏠 ʜᴏᴍᴇ", callback_data="home"),
             InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
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
            "<b><blockquote>🖼️ THUMBNAIL SETTINGS\n\n"
            f"• Main thumb: <b>{settings['main_thumb']}</b>\n"
            f"• Quality thumbs: <b>{settings['quality_thumbs']}</b>\n"
            f"• Copy source thumb: <b>{settings['copy_source_thumb']}</b>\n\n"
            "Configure your thumbnails below.</blockquote></b>"
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("ꜱᴇᴛ ᴍᴀɪɴ", callback_data="set_thumb_main"),
             InlineKeyboardButton("ᴄᴏᴘʏ ᴛʜᴜᴍʙ", callback_data="set_thumb_copy")],
            [InlineKeyboardButton("ᴠɪᴇᴡ ᴍᴀɪɴ", callback_data="view_main"),
             InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ ᴍᴀɪɴ", callback_data="delete_main")],
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="meta_config"),
             InlineKeyboardButton("🏠 ʜᴏᴍᴇ", callback_data="home"),
             InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
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
            f"<b><blockquote>💬 CAPTION SETTINGS\n\n"
            f"Current caption: <b>{settings['caption']}</b></blockquote></b>\n\n"
            "<b><blockquote>To set a new caption, use the command:\n"
            "<code>/set_caption Your caption here</code>\n\n"
            "Available tags: {filename}, {title}, {episode}, {season}, {quality}, {chapter}, {audio}</blockquote></b>"
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
            f"<b><blockquote>⚙️ FORMAT SETTINGS\n\n"
            f"Current format: <b>{settings['format']}</b></blockquote></b>\n\n"
            "<b><blockquote>To set a new format, use the command:\n"
            "<code>/set_format Your format here</code>\n\n"
            "Available tags: {filename}, {title}, {episode}, {season}, {quality}, {chapter}, {audio}</blockquote></b>"
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
        # Dynamic admin link generation using the ADMIN ID or Username configured in config.py
        admin_val = globals().get('ADMIN', '')
        admin_url = f"tg://openmessage?user_id={admin_val}" if str(admin_val).isdigit() else f"https://t.me/{str(admin_val).replace('@', '')}"
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🦋 ᴀᴅᴍɪɴ", url=admin_url)],
            [InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="home"),
             InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="close")]
        ])
        await query.message.edit_text(
            text=DONATE_TXT,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

    # 11. CLOSE
    elif data == "close":
        await query.message.delete()
