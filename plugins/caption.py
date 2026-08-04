from pyrogram import Client, filters
from pyrogram.types import Message
# Import your database helper here
# from helper.database import madflixbotz as db

# ==========================================
#              CAPTION COMMANDS
# ==========================================

@Client.on_message(filters.private & filters.command("set_caption"))
async def set_caption(bot: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b><u>ʜᴇʀᴇ'ꜱ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ɪᴛ</u> /set_caption</b>\n"
            "<b>ꜱᴇᴛᴜᴘ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ꜰᴏʀ ʏᴏᴜʀ ꜰɪʟᴇꜱ.</b>\n"
            "<b>ᴜꜱᴇ ᴛʜᴇꜱᴇ ᴋᴇʏᴡᴏʀᴅꜱ ᴛᴏ ꜱᴇᴛᴜᴘ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ:</b>\n\n"
            "<b><blockquote>"
            "→ {filename} :- ᴏʀɪɢɪɴᴀʟ ꜰɪʟᴇ ɴᴀᴍᴇ\n"
            "→ {title} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴀɴɪᴍᴇ ᴏʀ ꜱᴇʀɪᴇꜱ ᴛɪᴛʟᴇ\n"
            "→ {season} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ꜱᴇᴀꜱᴏɴ ɴᴜᴍʙᴇʀ\n"
            "→ {episode} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴇᴘɪꜱᴏᴅᴇ ɴᴜᴍʙᴇʀ\n"
            "→ {quality} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴠɪᴅᴇᴏ ʀᴇꜱᴏʟᴜᴛɪᴏɴ\n"
            "→ {filesize} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ꜰɪʟᴇ ꜱɪᴢᴇ\n"
            "→ {duration} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴠɪᴅᴇᴏ ᴅᴜʀᴀᴛɪᴏɴ"
            "</blockquote></b>\n\n"
            "<b><blockquote>"
            "• ᴇxᴀᴍᴘʟᴇ: /set_caption {filename}\n\n"
            "Size: {filesize}"
            "</blockquote></b>\n\n"
            "<b><blockquote>"
            "• ᴀʟʟ ʜᴛᴍʟ ᴛᴀɢꜱ (b, i, u, s, code, a, blockquote) ᴀʀᴇ ꜰᴜʟʟʏ ꜱᴜᴘᴘᴏʀᴛᴇᴅ."
            "</blockquote></b>"
        )
    
    caption = message.text.split(None, 1)[1]
    user_id = message.from_user.id
    
    # Save to Database
    # await db.set_caption(user_id, caption)
    
    await message.reply_text(
        "<b><blockquote>ᴄᴀᴘᴛɪᴏɴ ꜱᴀᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓</blockquote></b>"
    )


@Client.on_message(filters.private & filters.command("see_caption"))
async def see_caption(bot: Client, message: Message):
    user_id = message.from_user.id
    
    # Fetch from Database
    # caption = await db.get_caption(user_id)
    caption = None  # Replace with database fetch
    
    if caption:
        await message.reply_text(
            f"<b><blockquote>ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ :-\n\n{caption}</blockquote></b>"
        )
    else:
        await message.reply_text(
            "<b><blockquote>ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴄᴀᴘᴛɪᴏɴ ✕</blockquote></b>"
        )


@Client.on_message(filters.private & filters.command("del_caption"))
async def delete_caption(bot: Client, message: Message):
    user_id = message.from_user.id
    
    # Delete from Database
    # await db.set_caption(user_id, None)
    
    await message.reply_text(
        "<b><blockquote>ᴄᴀᴘᴛɪᴏɴ ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓</blockquote></b>"
    )
