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
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "madflixbotz")

# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ad48ac09b1e6f30d2dae4.jpg")

# Updates Channel Link Config
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/ST_Rename_Update")

# Force Sub Message & Picture Config
FORCE_SUB_TXT = os.environ.get(
    "FORCE_SUB_TXT", 
    "<b>Hello {first_name} 👋\n\nYou Need To Join In My Channel To Use Me.\n\nKindly Please Join Channel Below!</b>"
)
FORCE_SUB_PIC = os.environ.get(
    "FORCE_SUB_PIC", 
    "https://graph.org/file/ad48ac09b1e6f30d2dae4.jpg"
)

# Text Messages Config
START_TXT = os.environ.get(
    "START_TXT", 
    "<b>Hello {mention} 👋\n\nI Am An Advanced File Renamer Bot With 4GB Support & Custom Thumbnail Support!</b>"
)

HELP_TXT = os.environ.get(
    "HELP_TXT", 
    """<b>• AVAILABLE COMMANDS</b>

<b><blockquote>Usᴇʀ Cᴏᴍᴍᴀɴᴅs :-</blockquote></b>
<b><blockquote>• /start - ᴄʜᴇᴄᴋ ɪғ ᴛʜᴇ ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ.
• /viewthumb - ᴛᴏ ᴠɪᴇᴡ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
• /delthumb - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
• /set_caption - ᴛᴏ sᴇᴛ ᴀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
• /see_caption - sᴇᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
• /del_caption - ᴅᴇʟᴇᴛᴇ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
• /ping - ᴄʜᴇᴄᴋ ʙᴏᴛ ᴘɪɴɢ.
• /donate - sᴜᴘᴘᴏʀᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ.</blockquote></b>

<b>Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs :-</b>
<b><blockquote>• /users - sᴇᴇ ᴛᴏᴛᴀʟ ᴜsᴇʀs.
• /allids - sᴇᴇ ᴀʟʟ ᴜsᴇʀs ɪᴅ's ʟɪsᴛ.
• /broadcast - ᴍᴇssᴀɢᴇ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴍᴀɴᴅ.
• /warn - sᴇɴᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀ ᴜsᴇʀ.
• /restart - ᴄᴀɴᴄᴇʟ ᴀʟʟ ᴘʀᴏᴄᴇss ᴀɴᴅ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</blockquote></b>"""
)

DONATE_TXT = os.environ.get(
    "DONATE_TXT",
    "<b><blockquote>🪩 ᴛʜᴀɴᴋs ꜰᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! 🎐</blockquote></b>
    <b><blockquote>ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛs & ᴘʀᴏᴊᴇᴄᴛs, ʏᴏᴜ ᴄᴀɴ 🎁 ᴅᴏɴᴀᴛᴇ ᴜs ᴀɴʏ ᴀᴍᴏᴜɴᴛ ꜰʀᴏᴍ 10 ʀs ᴜᴘᴛᴏ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ. ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ ʜᴇʟᴘs ᴜs ᴋᴇᴇᴘ ᴛʜᴇ sᴇʀᴠᴇʀs ʀᴜɴɴɪɴɢ ᴀɴᴅ ᴀᴅᴅ ᴍᴏʀᴇ ᴀᴡᴇsᴏᴍᴇ ꜰᴇᴀᴛᴜʀᴇs ꜰᴏʀ ᴇᴠᴇʀʏᴏɴᴇ ᴛᴏ ᴇɴᴊᴏʏ! ❤️</blockquote></b>
    <b><blockquote>🛍 ᴜᴘɪ ɪᴅ: @upi</blockquote></b>"
)

MORE_TXT = os.environ.get(
    "MORE_TXT",
    "<b>• CLICK FOR MORE DETAILS •</b>\n\nHere you can find more information about our bot services and channel updates."
)
