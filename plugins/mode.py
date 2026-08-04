from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

MODE_BANNER = "https://graph.org/file/your_image_link.jpg"

@Client.on_message(filters.private & filters.command("mode"))
async def mode_cmd(bot: Client, message: Message):
    user_id = message.from_user.id
    # Fetch mode from DB (default "AUTODETECT")
    current_mode = "AUTODETECT" 
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ꜰɪʟᴇ ɴᴀᴍᴇ", callback_data="mode_filename"),
            InlineKeyboardButton("ᴄᴀᴘᴛɪᴏɴ", callback_data="mode_caption"),
            InlineKeyboardButton("ᴀᴜᴛᴏ ᴅᴇᴛᴇᴄᴛ", callback_data="mode_autodetect")
        ],
        [
            InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="mode_back"),
            InlineKeyboardButton("🏠 ʜᴏᴍᴇ", callback_data="mode_home"),
            InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="mode_close")
        ]
    ])
    
    caption_text = (
        f"<b><blockquote>ʀᴇɴᴀᴍᴇ ᴍᴏᴅᴇ\n\n"
        f"ᴄᴜʀʀᴇɴᴛ ᴍᴏᴅᴇ: {current_mode}</blockquote></b>\n\n"
        "<b>ꜰɪʟᴇɴᴀᴍᴇ ᴍᴏᴅᴇ: ᴄʜᴀɴɢᴇꜱ ᴛʜᴇ ᴀᴄᴛᴜᴀʟ ꜰɪʟᴇ ɴᴀᴍᴇ.\n"
        "ᴄᴀᴘᴛɪᴏɴ ᴍᴏᴅᴇ: ᴋᴇᴇᴘꜱ ᴛʜᴇ ꜰɪʟᴇ ɴᴀᴍᴇ, ʙᴜᴛ ᴀᴅᴅꜱ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n"
        "ᴀᴜᴛᴏ ᴅᴇᴛᴇᴄᴛ ᴍᴏᴅᴇ: ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇᴛᴇᴄᴛꜱ ᴀɴᴅ ᴀᴘᴘʟɪᴇꜱ ꜱᴇᴛᴛɪɴɢꜱ.</b>"
    )
    
    await message.reply_photo(photo=MODE_BANNER, caption=caption_text, reply_markup=keyboard)


@Client.on_callback_query(filters.regex(r"^mode_"))
async def mode_callback(bot: Client, callback_query: CallbackQuery):
    action = callback_query.data.split("_")[1]
    
    if action == "close":
        return await callback_query.message.delete()
    elif action in ["filename", "caption", "autodetect"]:
        selected_mode = action.upper()
        # Save to DB
        # await db.set_rename_target(callback_query.from_user.id, selected_mode)
        
        await callback_query.answer(f"Mode changed to {selected_mode}!", show_alert=True)
        
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ꜰɪʟᴇ ɴᴀᴍᴇ", callback_data="mode_filename"),
                InlineKeyboardButton("ᴄᴀᴘᴛɪᴏɴ", callback_data="mode_caption"),
                InlineKeyboardButton("ᴀᴜᴛᴏ ᴅᴇᴛᴇᴄᴛ", callback_data="mode_autodetect")
            ],
            [
                InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="mode_back"),
                InlineKeyboardButton("🏠 ʜᴏᴍᴇ", callback_data="mode_home"),
                InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ", callback_data="mode_close")
            ]
        ])
        
        caption_text = (
            f"<b><blockquote>ʀᴇɴᴀᴍᴇ ᴍᴏᴅᴇ\n\n"
            f"ᴄᴜʀʀᴇɴᴛ ᴍᴏᴅᴇ: {selected_mode}</blockquote></b>\n\n"
            "<b>ꜰɪʟᴇɴᴀᴍᴇ ᴍᴏᴅᴇ: ᴄʜᴀɴɢᴇꜱ ᴛʜᴇ ᴀᴄᴛᴜᴀʟ ꜰɪʟᴇ ɴᴀᴍᴇ.\n"
            "ᴄᴀᴘᴛɪᴏɴ ᴍᴏᴅᴇ: ᴋᴇᴇᴘꜱ ᴛʜᴇ ꜰɪʟᴇ ɴᴀᴍᴇ, ʙᴜᴛ ᴀᴅᴅꜱ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n"
            "ᴀᴜᴛᴏ ᴅᴇᴛᴇᴄᴛ ᴍᴏᴅᴇ: ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇᴛᴇᴄᴛꜱ ᴀɴᴅ ᴀᴘᴘʟɪᴇꜱ ꜱᴇᴛᴛɪɴɢꜱ.</b>"
        )
        await callback_query.message.edit_caption(caption=caption_text, reply_markup=keyboard)

