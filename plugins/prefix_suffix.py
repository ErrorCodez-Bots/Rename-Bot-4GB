from pyrogram import Client, filters
from pyrogram.types import Message
# Import your database helper here
# from helper.database import madflixbotz as db

# ==========================================
#              PREFIX COMMANDS
# ==========================================

@Client.on_message(filters.private & filters.command("set_prefix"))
async def set_prefix(bot: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b><blockquote>ɢɪᴠᴇ ᴛʜᴇ ᴘʀᴇꜰɪx\n\n"
            "ᴇxᴀᴍᴘʟᴇ :- /set_prefix @Unrated_Coder</blockquote></b>"
        )
    
    prefix = message.text.split(None, 1)[1]
    user_id = message.from_user.id
    
    # Save to Database
    # await db.set_prefix(user_id, prefix)
    
    await message.reply_text(
        "<b><blockquote>ᴘʀᴇꜰɪx ꜱᴀᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓</blockquote></b>"
    )

@Client.on_message(filters.private & filters.command("see_prefix"))
async def see_prefix(bot: Client, message: Message):
    user_id = message.from_user.id
    
    # Fetch from Database
    # prefix = await db.get_prefix(user_id)
    prefix = None  # Replace with database fetch
    
    if prefix:
        await message.reply_text(
            f"<b><blockquote>ʏᴏᴜʀ ᴘʀᴇꜰɪx :- {prefix}</blockquote></b>"
        )
    else:
        await message.reply_text(
            "<b><blockquote>ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴇꜰɪx ✕</blockquote></b>"
        )

@Client.on_message(filters.private & filters.command("del_prefix"))
async def delete_prefix(bot: Client, message: Message):
    user_id = message.from_user.id
    
    # Delete from Database
    # await db.set_prefix(user_id, None)
    
    await message.reply_text(
        "<b><blockquote>ᴘʀᴇꜰɪx ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓</blockquote></b>"
    )


# ==========================================
#              SUFFIX COMMANDS
# ==========================================

@Client.on_message(filters.private & filters.command("set_suffix"))
async def set_suffix(bot: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b><blockquote>ɢɪᴠᴇ ᴛʜᴇ ꜱᴜꜰꜰɪx\n\n"
            "ᴇxᴀᴍᴘʟᴇ :- /set_suffix @Unrated_Coder</blockquote></b>"
        )
    
    suffix = message.text.split(None, 1)[1]
    user_id = message.from_user.id
    
    # Save to Database
    # await db.set_suffix(user_id, suffix)
    
    await message.reply_text(
        "<b><blockquote>ꜱᴜꜰꜰɪx ꜱᴀᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓</blockquote></b>"
    )

@Client.on_message(filters.private & filters.command("see_suffix"))
async def see_suffix(bot: Client, message: Message):
    user_id = message.from_user.id
    
    # Fetch from Database
    # suffix = await db.get_suffix(user_id)
    suffix = None  # Replace with database fetch
    
    if suffix:
        await message.reply_text(
            f"<b><blockquote>ʏᴏᴜʀ ꜱᴜꜰꜰɪx :- {suffix}</blockquote></b>"
        )
    else:
        await message.reply_text(
            "<b><blockquote>ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ꜱᴜꜰꜰɪx ✕</blockquote></b>"
        )

@Client.on_message(filters.private & filters.command("del_suffix"))
async def delete_suffix(bot: Client, message: Message):
    user_id = message.from_user.id
    
    # Delete from Database
    # await db.set_suffix(user_id, None)
    
    await message.reply_text(
        "<b><blockquote>ꜱᴜꜰꜰɪx ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓</blockquote></b>"
    )

