from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.private & filters.command("rename_mode"))
async def rename_workflow_cmd(bot: Client, message: Message):
    user_id = message.from_user.id
    # Fetch current mode from DB (e.g., "SINGLE", "VIDEO", "DOCUMENT")
    current_mode = "SINGLE"  # Replace with db fetch
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ꜱɪɴɢʟᴇ ʀᴇɴᴀᴍᴇ", callback_data="wf_single"),
            InlineKeyboardButton("ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ", callback_data="wf_auto")
        ]
    ])
    
    text = (
        "<b>• ʀᴇɴᴀᴍᴇ ᴡᴏʀᴋꜰʟᴏᴡ ᴍᴏᴅᴇ\n\n"
        f"ᴄᴜʀʀᴇɴᴛ ᴍᴏᴅᴇ: {current_mode}\n\n"
        "ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘʀᴇꜰᴇʀʀᴇᴅ ᴍᴏᴅᴇ ʙᴇʟᴏᴡ:</b>"
    )
    
    await message.reply_text(text, reply_markup=keyboard)


@Client.on_callback_query(filters.regex(r"^wf_"))
async def workflow_callback(bot: Client, callback_query: CallbackQuery):
    action = callback_query.data.split("_")[1]
    user_id = callback_query.from_user.id
    
    if action == "single":
        # Save SINGLE mode to DB
        # await db.set_workflow_mode(user_id, "SINGLE")
        
        await callback_query.answer("Mode set to SINGLE", show_alert=False)
        
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ꜱɪɴɢʟᴇ ʀᴇɴᴀᴍᴇ", callback_data="wf_single"),
                InlineKeyboardButton("ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ", callback_data="wf_auto")
            ]
        ])
        
        text = (
            "<b>• ʀᴇɴᴀᴍᴇ ᴡᴏʀᴋꜰʟᴏᴡ ᴍᴏᴅᴇ\n\n"
            "ᴄᴜʀʀᴇɴᴛ ᴍᴏᴅᴇ: SINGLE\n\n"
            "ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘʀᴇꜰᴇʀʀᴇᴅ ᴍᴏᴅᴇ ʙᴇʟᴏᴡ:</b>"
        )
        await callback_query.message.edit_text(text, reply_markup=keyboard)

    elif action == "auto":
        # Ask user for default format (Document / Video)
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("• ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="wf_fmt_document"),
                InlineKeyboardButton("• ᴠɪᴅᴇᴏ", callback_data="wf_fmt_video")
            ]
        ])
        
        text = (
            "<b>• ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ᴍᴏᴅᴇ ꜱᴇʟᴇᴄᴛᴇᴅ!\n\n"
            "ᴘʟᴇᴀꜱᴇ ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴅᴇꜰᴀᴜʟᴛ ᴏᴜᴛᴘᴜᴛ ꜰᴏʀᴍᴀᴛ:</b>"
        )
        await callback_query.message.edit_text(text, reply_markup=keyboard)


@Client.on_callback_query(filters.regex(r"^wf_fmt_"))
async def workflow_format_callback(bot: Client, callback_query: CallbackQuery):
    fmt = callback_query.data.split("_")[2].capitalize()  # "Video" or "Document"
    user_id = callback_query.from_user.id
    
    # Save AUTO mode & format type to DB
    # await db.set_workflow_mode(user_id, f"AUTO_{fmt.upper()}")
    
    text = (
        f"<b>✓ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ɪꜱ ɴᴏᴡ ᴀᴄᴛɪᴠᴇ!\n\n"
        f"ꜰᴏʀᴍᴀᴛ: {fmt}\n"
        f"<i>ᴀʟʟ ꜰᴜᴛᴜʀᴇ ꜰɪʟᴇꜱ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʀᴇɴᴀᴍᴇᴅ ᴀꜱ ᴛʜɪꜱ ᴛʏᴘᴇ.</i></b>"
    )
    
    await callback_query.message.edit_text(text)
