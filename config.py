import os

# Required Variables Config
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", ""))

# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")

# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

# Mongo DB Database Config
DATABASE_URL = os.environ.get("DB_URL", "")
DATABASE_NAME = os.environ.get("DB_NAME", "madflixbotz")

# Single Start Picture (Fallback)
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/8dd38af99889caea1cf4b-2bd9a6e6cfb04c2b95.jpg")

# 4 Random Start/Menu Pictures Config
START_PICS = os.environ.get(
    "START_PICS", 
    "https://telegra.ph/file/8dd38af99889caea1cf4b-2bd9a6e6cfb04c2b95.jpg "
    "https://telegra.ph/file/bdd491cce912cc3655cf3-df10e7c616bd15b6f1.jpg "
    "https://telegra.ph/file/4bbe2d8317dfb08f84983-8157695dd5656d2db1.jpg "
    "https://telegra.ph/file/b73ca7b6b7ae5cc29ff93-8db248b9c3262c0441.jpg"
).split()

# Updates Channel Link Config
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/ST_Rename_Update")

# Force Sub Message & Picture Config
FORCE_SUB_TXT = os.environ.get(
    "FORCE_SUB_TXT", 
    "<b>ʜᴇʟʟᴏ {first_name} 👋\n\nʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ.\n\nᴋɪɴᴅʟʏ ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ʙᴇʟᴏᴡ!</b>"
)
FORCE_SUB_PIC = os.environ.get(
    "FORCE_SUB_PIC", 
    "https://telegra.ph/file/8dd38af99889caea1cf4b-2bd9a6e6cfb04c2b95.jpg"
)

# Text Messages Config in Small Caps (SMLCAPS)
START_TXT = os.environ.get(
    "START_TXT", 
    "<b>ʜᴇʏ, {mention}! ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴍᴏꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ!</b>\n\n"
    "<blockquote><b>ᴡɪᴛʜ ᴍʏ ᴘᴏᴡᴇʀꜰᴜʟ ꜰᴇᴀᴛᴜʀᴇꜱ, ʏᴏᴜ ᴄᴀɴ:-\n"
    "ᴀᴜᴛᴏʀᴇɴᴀᴍᴇ ꜰɪʟᴇꜱ ᴡɪᴛʜ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴍᴀᴛꜱ.-\n"
    "ᴀᴅᴅ ᴄᴀᴘᴛɪᴏɴꜱ ᴏʀ ꜱᴇʟᴇᴄᴛ ᴛʜᴜᴍʙɴᴀɪʟꜱ.-\n"
    "ᴘʀᴏᴄᴇꜱꜱ ꜰɪʟᴇꜱ ꜱᴇǫᴜᴇɴᴛɪᴀʟʟʏ ꜰᴏʀ ꜱᴍᴏᴏᴛʜ ᴡᴏʀᴋꜰʟᴏᴡ.</b></blockquote>\n\n"
    "<blockquote><b>🔷 ʀᴇᴀᴅʏ ᴛᴏ ʙᴇɢɪɴ? ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ!\n"
    "🔷 ꜰᴏʀ ᴅᴇᴛᴀɪʟꜱ, ᴛᴀᴘ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ.</b></blockquote>"
)

HELP_TXT = os.environ.get(
    "HELP_TXT", 
    "<b>• ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ</b>\n\n"
    "<blockquote><b>• <u>ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴇᴛᴛɪɴɢꜱ</u>\n"
    "• ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ.\n"
    "• /viewthumb - ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.\n"
    "• /delthumb - ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.\n\n"
    "• <u>ᴄᴀᴘᴛɪᴏɴ ꜱᴇᴛᴛɪɴɢꜱ</u>\n"
    "• /set_caption - ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n"
    "• /see_caption - ꜱᴇᴇ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴄᴀᴘᴛɪᴏɴ.\n"
    "• /del_caption - ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n\n"
    "• <u>ʀᴇɴᴀᴍɪɴɢ ᴍᴏᴅᴇꜱ</u>\n"
    "• /rename_mode - ꜱᴡɪᴛᴄʜ ʙᴇᴛᴡᴇᴇɴ ꜱɪɴɢʟᴇ ᴀɴᴅ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ.\n"
    "• /format - ꜱᴇᴛ ʏᴏᴜʀ ᴀᴜᴛᴏ-ʀᴇɴᴀᴍᴇ ꜰᴏʀᴍᴀᴛ.\n"
    "• /mode - ᴏᴘᴇɴ ᴛʜᴇ ʀᴇɴᴀᴍᴇ ᴍᴏᴅᴇ ᴍᴇɴᴜ.\n\n"
    "• <u>ᴘʀᴇꜰɪx & ꜱᴜꜰꜰɪx</u>\n"
    "• /set_prefix - ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰɪx.\n"
    "• /see_prefix - ꜱᴇᴇ ʏᴏᴜʀ ᴘʀᴇꜰɪx.\n"
    "• /del_prefix - ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴘʀᴇꜰɪx.\n"
    "• /set_suffix - ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ꜱᴜꜰꜰɪx.\n"
    "• /see_suffix - ꜱᴇᴇ ʏᴏᴜʀ ꜱᴜꜰꜰɪx.\n"
    "• /del_suffix - ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ꜱᴜꜰꜰɪx.\n\n"
    "• <u>ᴏᴛʜᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ</u>\n"
    "• /metadata - ᴄᴏɴꜰɪɢᴜʀᴇ ᴠɪᴅᴇᴏ ᴍᴇᴛᴀᴅᴀᴛᴀ.\n"
    "• /spoiler - ᴀᴅᴅ ꜱᴘᴏɪʟᴇʀ ᴇꜰꜰᴇᴄᴛ ᴏɴ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ꜰɪʟᴇꜱ.\n"
    "• /donate - ꜱᴜᴘᴘᴏʀᴛ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ.</b></blockquote>\n\n"
    "<b>🔷 ᴀɴʏ ᴏᴛʜᴇʀ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ :-\n"
    "@ST_Rename_Update</b>"
)

DONATE_TXT = os.environ.get(
    "DONATE_TXT",
    "<blockquote><b>🎰 ᴛʜᴀɴᴋꜱ ꜰᴏʀ ꜱʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇꜱᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! 🍧</b></blockquote>\n\n"
    "<blockquote><b>ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛꜱ & ᴘʀᴏᴊᴇᴄᴛꜱ, ʏᴏᴜ ᴄᴀɴ\n"
    "🎁 ᴅᴏɴᴀᴛᴇ ᴜꜱ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ꜰʀᴏᴍ 10 ʀꜱ ᴜᴘᴛᴏ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ. ʏᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ ʜᴇʟᴘꜱ ᴜꜱ ᴋᴇᴇᴘ ᴛʜᴇ ꜱᴇʀᴠᴇʀꜱ ʀᴜɴɴɪɴɢ ᴀɴᴅ ᴀᴅᴅ ᴍᴏʀᴇ ᴀᴡᴇꜱᴏᴍᴇ ꜰᴇᴀᴛᴜʀᴇꜱ ꜰᴏʀ ᴇᴠᴇʀʏᴏɴᴇ ᴛᴏ ᴇɴᴊᴏʏ! ❤️</b></blockquote>\n\n"
    "<blockquote><b>🛍️ ᴜᴘɪ ɪᴅ: acxanime@upi</b></blockquote>"
)

MORE_TXT = os.environ.get(
    "MORE_TXT",
    "<b>• ᴄʟɪᴄᴋ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ •</b>\n\n"
    "ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴀɢꜱ: {filename}, {title}, {episode}, {season}, {quality}, {chapter}, {audio}"
)
