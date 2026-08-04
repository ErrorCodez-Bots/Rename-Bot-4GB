import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import getid, delete
from config import ADMIN

# ==========================================
#             BROADCAST COMMAND
# ==========================================

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "<b><blockquote>⚠️ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ!</blockquote></b>"
        )
    
    ms = await message.reply_text(
        "<b><blockquote>ɢᴇᴛᴛɪɴɢ ᴀʟʟ ɪᴅꜱ ꜰʀᴏᴍ ᴅᴀᴛᴀʙᴀꜱᴇ. ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...</blockquote></b>"
    )
    
    ids = getid()
    tot = len(ids)
    success = 0
    failed = 0
    
    await ms.edit_text(
        f"<b><blockquote>ꜱᴛᴀʀᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀꜱᴛ...\n\nꜱᴇɴᴅɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ {tot} ᴜꜱᴇʀꜱ</blockquote></b>"
    )
    
    for user_id in ids:
        try:
            await asyncio.sleep(1)
            await message.reply_to_message.copy(user_id)
            success += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            try:
                await message.reply_to_message.copy(user_id)
                success += 1
            except Exception:
                failed += 1
                delete({"_id": user_id})
        except Exception:
            failed += 1
            delete({"_id": user_id})
            
        try:
            await ms.edit_text(
                f"<b><blockquote>📢 ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴘʀᴏɢʀᴇꜱꜱ:\n\n"
                f"✓ ꜱᴜᴄᴄᴇꜱꜱ :- {success}\n"
                f"✕ ꜰᴀɪʟᴇᴅ :- {failed}\n"
                f"📊 ᴛᴏᴛᴀʟ :- {tot}</blockquote></b>"
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            pass

    await ms.edit_text(
        f"<b><blockquote>📢 ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ✓\n\n"
        f"✓ ꜱᴜᴄᴄᴇꜱꜱ :- {success}\n"
        f"✕ ꜰᴀɪʟᴇᴅ :- {failed}\n"
        f"📊 ᴛᴏᴛᴀʟ :- {tot}</blockquote></b>"
    )
