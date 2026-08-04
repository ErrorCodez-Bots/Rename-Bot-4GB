from pyrogram import Client, filters
from pyrogram.types import Message

# Set your banner image URL or file_id here
FORMAT_BANNER = "https://graph.org/file/your_image_link.jpg"

@Client.on_message(filters.private & filters.command("format"))
async def format_cmd(bot: Client, message: Message):
    if len(message.command) < 2:
        caption_text = (
            "<b><u>ʜᴇʀᴇ'ꜱ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ɪᴛ</u> /format</b>\n"
            "<b>ꜱᴇᴛᴜᴘ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ꜰᴏʀᴍᴀᴛ\n"
            "ᴜꜱᴇ ᴛʜᴇꜱᴇ ᴋᴇʏᴡᴏʀᴅꜱ ᴛᴏ ꜱᴇᴛᴜᴘ ᴄᴜꜱᴛᴏᴍ ꜰɪʟᴇ ɴᴀᴍᴇ</b>\n\n"
            "<b><blockquote>"
            "→ {title} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴀɴɪᴍᴇ ᴏʀ ꜱᴇʀɪᴇꜱ ᴛɪᴛʟᴇ ɴᴀᴍᴇ\n"
            "→ {season} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ꜱᴇᴀꜱᴏɴ ɴᴜᴍʙᴇʀ\n"
            "→ {episode} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴇᴘɪꜱᴏᴅᴇ ɴᴜᴍʙᴇʀ\n"
            "→ {quality} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴠɪᴅᴇᴏ ʀᴇꜱᴏʟᴜᴛɪᴏɴ\n"
            "→ {chapter} :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴍᴀɴɢᴀ ᴄʜᴀᴘᴛᴇʀ ɴᴜᴍʙᴇʀ\n"
            "→ {audio} :- ᴀᴜᴛᴏ ʟᴀʙᴇʟ ꜰʀᴏᴍ ꜱᴛʀᴇᴀᴍꜱ: ꜱᴜʙ, ᴅᴜᴀʟ, ᴏʀ ᴍᴜʟᴛɪ"
            "</blockquote></b>\n\n"
            "<b><blockquote>"
            "► ᴇxᴀᴍᴘʟᴇ: /format S{season} E{episode} - {title} [{quality}] [{audio}]\n"
            "► ᴍᴀɴɢᴀ: /format {title} {chapter} @ST_Rename_Update"
            "</blockquote></b>\n\n"
            "<b><blockquote>"
            "ᴀᴜᴅɪᴏ ʟᴀʙᴇʟꜱ: 1 ᴀᴜᴅɪᴏ + ꜱᴜʙᴛɪᴛʟᴇꜱ = ꜱᴜʙ, 2 ᴀᴜᴅɪᴏ = ᴅᴜᴀʟ, 3+ ᴀᴜᴅɪᴏ = ᴍᴜʟᴛɪ.\n"
            "ɴᴏᴛᴇ: ᴅᴏɴ'ᴛ ᴘᴜᴛ .mkv ᴏʀ .mp4 ᴀᴛ ᴛʜᴇ ᴇɴᴅ."
            "</blockquote></b>"
        )
        return await message.reply_photo(photo=FORMAT_BANNER, caption=caption_text)
    
    user_format = message.text.split(None, 1)[1]
    # Save to Database
    # await db.set_format(message.from_user.id, user_format)
    
    await message.reply_text("<b><blockquote>ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ꜰᴏʀᴍᴀᴛ ꜱᴀᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓</blockquote></b>")

