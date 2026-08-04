from pyrogram import Client, filters
from pyrogram.errors import StopPropagation
from config import ADMIN

# Flag to keep track of maintenance state
IS_MAINTENANCE = False


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["maintenance"]))
async def maintenance_mode(bot, message):
    """Admin command to toggle maintenance mode on and off."""
    global IS_MAINTENANCE
    IS_MAINTENANCE = not IS_MAINTENANCE
    
    if IS_MAINTENANCE:
        await message.reply_text("<b>Maintenance mode has been activated.</b>")
    else:
        await message.reply_text("<b>Maintenance mode has been deactivated.</b>")


@Client.on_message(~filters.user(ADMIN), group=-1)
async def check_maintenance(bot, message):
    """Blocks non-admin messages when maintenance mode is active."""
    if IS_MAINTENANCE:
        await message.reply_text(
            "<b>Bot is gone under maintenance.\n\n"
            "Please wait for the admin to resume the services.</b>"
        )
        raise StopPropagation
