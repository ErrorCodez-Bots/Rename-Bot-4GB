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
    "<b><blockquote>ᴡɪᴛ🇭 ᴍʏ ᴘᴏᴡᴇʀꜰᴜʟ ꜰᴇᴀᴛᴜʀᴇꜱ, ʏᴏᴜ ᴄᴀɴ:-\n"
    "ᴀᴜᴛᴏʀᴇɴᴀᴍᴇ ꜰɪʟᴇꜱ 🇼ɪᴛ🇭 ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴍᴀᴛꜱ.-\n"
    "ᴀᴅᴅ ᴄᴀᴘᴛɪᴏɴꜱ ᴏʀ ꜱᴇʟᴇᴄᴛ ᴛ🇭ᴜᴍʙɴᴀɪʟꜱ.-\n"
    "ᴘʀᴏᴄᴇꜱꜱ ꜰɪʟᴇꜱ ꜱᴇǫᴜᴇɴᴛɪᴀʟʟʏ ꜰᴏʀ ꜱᴍᴏᴏᴛ🇭 🇼ᴏʀᴋꜰʟᴏ🇼.</blockquote></b>\n\n"
    "<b><blockquote>🔷 ʀᴇᴀᴅʏ ᴛᴏ ʙᴇɢɪɴ? ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ!\n"
    "🔷 ꜰᴏʀ ᴅᴇᴛᴀɪʟꜱ, ᴛᴀᴘ ᴛ🇭ᴇ 🇭ᴇʟᴘ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏ🇼.</blockquote></b>"
)

HELP_TXT = os.environ.get(
    "HELP_TXT", 
    "<b>• ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ</b>\n\n"
    "<b><blockquote>• <u>ᴛ🇭ᴜᴍʙɴᴀɪʟ ꜱᴇᴛᴛɪɴɢꜱ</u>\n"
    "• ꜱᴇɴᴅ ᴀɴʏ ᴘ🇭ᴏᴛᴏ ᴛᴏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴄᴜꜱᴛᴏᴍ ᴛ🇭ᴜᴍʙɴᴀɪʟ.\n"
    "• /vɪᴇ🇼ᴛ🇭ᴜᴍʙ - ᴠɪᴇ🇼 ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛ🇭ᴜᴍʙɴᴀɪ🇱.\n"
    "• /ᴅᴇʟᴛ🇭ᴜᴍʙ - ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛ🇭ᴜᴍʙɴᴀɪ🇱.\n\n"
    "• <u>ᴄᴀᴘᴛɪᴏɴ ꜱᴇᴛᴛɪɴɢꜱ</u>\n"
    "• /ꜱᴇᴛ_ᴄᴀᴘᴛɪᴏɴ - ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n"
    "• /ꜱᴇᴇ_ᴄᴀᴘᴛɪᴏɴ - ꜱᴇᴇ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴄᴀᴘᴛɪᴏɴ.\n"
    "• /ᴅᴇʟ_ᴄᴀᴘᴛɪᴏɴ - ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n\n"
    "• <u>ʀᴇɴᴀᴍɪɴɢ ᴍᴏᴅᴇꜱ</u>\n"
    "• /ʀᴇɴᴀᴍᴇ_ᴍᴏᴅᴇ - ꜱ🇼ɪᴛᴄ🇭 ʙᴇᴛ🇼ᴇᴇɴ ꜱɪɴɢʟᴇ ᴀɴᴅ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ.\n"
    "• /ꜰᴏʀᴍᴀᴛ - ꜱᴇᴛ ʏᴏᴜʀ ᴀᴜᴛᴏ-ʀᴇɴᴀᴍᴇ ꜰᴏʀᴍᴀᴛ.\n"
    "• /ᴍᴏᴅᴇ - ᴏᴘᴇɴ ᴛ🇭ᴇ ʀᴇɴᴀᴍᴇ ᴍᴏᴅᴇ ᴍᴇɴᴜ.\n\n"
    "• <u>ᴘʀᴇꜰɪx & ꜱᴜꜰꜰɪx</u>\n"
    "• /ꜱᴇᴛ_ᴘʀᴇꜰɪx - ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰɪx.\n"
    "• /ꜱᴇᴇ_ᴘʀᴇꜰɪx - ꜱᴇᴇ ʏᴏᴜʀ ᴘʀᴇꜰɪx.\n"
    "• /ᴅᴇʟ_ᴘʀᴇꜰɪx - ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴘʀᴇꜰɪx.\n"
    "• /ꜱᴇᴛ_ꜱᴜꜰꜰɪx - ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ꜱᴜꜰꜰɪx.\n"
    "• /ꜱᴇᴇ_ꜱᴜꜰꜰɪx - ꜱᴇᴇ ʏᴏᴜʀ ꜱᴜꜰꜰɪx.\n"
    "• /ᴅᴇʟ_ꜱᴜꜰꜰɪx - ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ꜱᴜꜰꜰɪx.\n\n"
    "• <u>ᴏᴛ🇭ᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ</u>\n"
    "• /ᴍᴇᴛᴀᴅᴀᴛᴀ - ᴄᴏɴꜰɪɢᴜʀᴇ ᴠɪᴅᴇᴏ ᴍᴇᴛᴀᴅᴀᴛᴀ.\n"
    "• /ꜱᴘᴏɪʟᴇʀ - ᴀᴅᴅ ꜱᴘᴏɪʟᴇʀ ᴇꜰꜰᴇᴄᴛ ᴏɴ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ꜰɪʟᴇꜱ.\n"
    "• /ᴅᴏɴᴀᴛᴇ - ꜱᴜᴘᴘᴏʀᴛ ᴛ🇭ᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ.</blockquote></b>\n\n"
    "<b>🔷 ᴀɴʏ ᴏᴛ🇭ᴇʀ 🇭ᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ :-\n"
    "@ꜱᴛ_ʀᴇɴᴀᴍᴇ_ᴜᴘᴅᴀᴛᴇ</b>"
)

DONATE_TXT = os.environ.get(
    "DONATE_TXT",
    "<b><blockquote>🎰 ᴛ🇭ᴀɴᴋꜱ ꜰᴏʀ ꜱ🇭ᴏ🇼ɪɴɢ ɪɴᴛᴇʀᴇꜱᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! 🍧</blockquote></b>\n\n"
    "<b><blockquote>ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛꜱ & ᴘʀᴏᴊᴇᴄᴛꜱ, ʏᴏᴜ ᴄᴀɴ\n"
    "🎁 ᴅᴏɴᴀᴛᴇ ᴜꜱ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ꜰʀᴏᴍ 10 ʀꜱ ᴜᴘᴛᴏ ʏᴏᴜʀ ᴄ🇭ᴏɪᴄᴇ. ʏᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ 🇭ᴇʟᴘꜱ ᴜꜱ ᴋᴇᴇᴘ ᴛ🇭ᴇ ꜱᴇʀᴠᴇʀꜱ ʀᴜɴɴɪɴɢ ᴀɴᴅ ᴀᴅᴅ ᴍᴏʀᴇ ᴀ🇼ᴇꜱᴏᴍᴇ ꜰᴇᴀᴛᴜʀᴇꜱ ꜰᴏʀ ᴇᴠᴇʀʏᴏɴᴇ ᴛᴏ ᴇɴᴊᴏʏ! ❤️</blockquote></b>\n\n"
    "<b><blockquote>🛍️ ᴜᴘɪ ɪᴅ: ᴀᴄxᴀɴɪᴍᴇ@ᴜᴘɪ</blockquote></b>"
)

DONATE_PIC = os.environ.get(
    "DONATE_PIC", 
    "https://telegra.ph/file/8dd38af99889caea1cf4b-2bd9a6e6cfb04c2b95.jpg"
)

MORE_TXT = os.environ.get(
    "MORE_TXT",
    "<b>• ᴄʟɪᴄᴋ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ •</b>\n\n"
    "ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴀɢꜱ: {filename}, {title}, {episode}, {season}, {quality}, {chapter}, {audio}"
)
