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

ABOUT_TXT = os.environ.get(
    "ABOUT_TXT", 
    "<b>🤖 My Name : File Renamer Bot\n📝 Language : Python 3\n📚 Framework : Pyrogram\n📡 Host Server : Render / VPS</b>"
)

HELP_TXT = os.environ.get(
    "HELP_TXT", 
    "<b><u>Help Menu</u></b>\n\n• Send Any Photo To Set Custom Thumbnail.\n• Send Any File/Video To Rename It.\n• Use /delete_thumb To Delete Saved Thumbnail."
)


# If You Need To Add Verify System Then Message Me On Telegram
# Check Demo Bots
# https://t.me/FileRenameXBot
# https://t.me/PremiumRenamerRobot
# https://t.me/FileRenamerXRobot
# Token Verification Adding Features Is Paid So If You Want Then Dm Me

# SHORTNER_URL = os.environ.get("SHORTNER_URL", "")
# SHORTNER_API = os.environ.get("SHORTNER_API", "")
# TOKEN_TIMEOUT = os.environ.get("TOKEN_TIMEOUT", "")

# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
