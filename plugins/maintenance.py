from pyrogram import Client, filters
from config import ADMIN

# Flag to keep track of maintenance state
IS_MAINTENANCE = False


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["maintenance"]))
async def maintenance_mode(bot, message):
    """Admin command to toggle maintenance mode on and off."""
    global IS_MAINTENANCE
    IS_MAINTENANCE = not IS_MAINTENANCE
    
    if IS_MAINTENANCE:
        await message.reply_text("<b><blockquote>ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ.</blockquote></b>")
    else:
        await message.reply_text("<b><blockquote>ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ʜᴀꜱ ʙᴇᴇɴ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ.</blockquote></b>")


@Client.on_message(~filters.user(ADMIN), group=-1)
async def check_maintenance(bot, message):
    """Blocks non-admin messages when maintenance mode is active."""
    if IS_MAINTENANCE:
        await message.reply_text(
            "<b><blockquote>ʙᴏᴛ ɪꜱ ɢᴏɴᴇ ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ.\n\n"
            "ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜰᴏʀ ᴛʜᴇ ᴀᴅᴍɪɴ ᴛᴏ ʀᴇꜱᴜᴍᴇ ᴛʜᴇ ꜱᴇʀᴠɪᴄᴇꜱ.</blockquote></b>"
        )
        return  # Replaces StopPropagation to halt further handler execution in this group
