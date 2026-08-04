from pyrogram import Client, filters
from pyrogram.types import Message
# Import your database helper here
# from helper.database import db

# ==========================================
#             THUMBNAIL COMMANDS
# ==========================================

@Client.on_message(filters.private & filters.command("set_thumb"))
async def set_thumb(bot: Client, message: Message):
    # Check if message is a reply or contains a photo
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply_text(
            "<b><blockquote>ɢɪᴠᴇ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ\n\n"
            "ᴇxᴀᴍᴘʟᴇ :- ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴘʜᴏᴛᴏ ᴡɪᴛʜ /set_thumb</blockquote></b>"
        )
    
    photo_id = message.reply_to_message.photo.file_id
    user_id = message.from_user.id
    
    # Save photo_id to Database
    # await db.set_thumbnail(user_id, photo_id)
    
    await message.reply_text(
        "<b><blockquote>ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓</blockquote></b>"
    )


@Client.on_message(filters.private & filters.command(["see_thumb", "view_thumb"]))
async def see_thumb(bot: Client, message: Message):
    user_id = message.from_user.id
    
    # Fetch thumbnail file_id from Database
    # thumb_id = await db.get_thumbnail(user_id)
    thumb_id = None  # Replace with actual DB call
    
    if thumb_id:
        await message.reply_photo(
            photo=thumb_id,
            caption="<b><blockquote>ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ 📌</blockquote></b>"
        )
    else:
        await message.reply_text(
            "<b><blockquote>ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴛʜᴜᴍʙɴᴀɪʟ ✕</blockquote></b>"
        )


@Client.on_message(filters.private & filters.command(["del_thumb", "delete_thumb"]))
async def delete_thumb(bot: Client, message: Message):
    user_id = message.from_user.id
    
    # Delete thumbnail from Database
    # await db.set_thumbnail(user_id, None)
    
    await message.reply_text(
        "<b><blockquote>ᴛʜᴜᴍʙɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓</blockquote></b>"
    )
