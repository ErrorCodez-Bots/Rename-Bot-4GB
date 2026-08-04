from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)
from pyrogram import Client, filters
import script
from config import *

# யூசர் & அட்மின் கமாண்ட்ஸ் பிரித்து அமைக்கப்பட்ட ஹெல்ப் டெக்ஸ்ட்
HELP_TXT = """<b>• AVAILABLE COMMANDS</b>

<b>👤 USER COMMANDS :-</b>
• /start - Check If The Bot Is Running.
• /viewthumb - To View Current Thumbnail.
• /delthumb - To Delete Current Thumbnail.
• /set_caption - To Set A Custom Caption.
• /see_caption - To See Your Custom Caption.
• /del_caption - To Delete Custom Caption.
• /ping - To Check Bot Ping.
• /donate - To Support Developer.

<b>👑 ADMIN COMMANDS :-</b>
• /users - Use This Command To See Total Users.
• /allids - Use This Command To See All Users IDs List.
• /broadcast - Message Broadcast Command.
• /warn - Use This Command To Send A Message To A User.
• /restart - Use This Command To Cancel All Process And Restart The Bot."""


@Client.on_callback_query(filters.regex('^(about|help|home|back|donate|close|cancel|try_again)$'))
async def cb_handler(bot, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id
    f_sub = FORCE_SUBS.replace("@", "") if FORCE_SUBS else None

    # 1. HOME / BACK TO MAIN START MENU
    if data in ["home", "back"]:
        text = START_TXT.format(mention=query.from_user.mention)
        keyboard = InlineKeyboardMarkup([  
            [InlineKeyboardButton("• CLICK FOR MORE •", url="https://t.me/ST_Rename_Update")],
            [InlineKeyboardButton("HELP", callback_data='help'),
             InlineKeyboardButton("UPDATES", url="https://t.me/ST_Rename_Update")],
            [InlineKeyboardButton("DONATE", callback_data='donate')]
        ])
        await query.message.edit_text(text=text, reply_markup=keyboard)

    # 2. HELP MENU (User & Admin Commands + Only Back & Close Buttons)
    elif data == "help":
        keyboard = InlineKeyboardMarkup([ 
            [InlineKeyboardButton("< BACK", callback_data='home'),
             InlineKeyboardButton("CLOSE ×", callback_data='close')]
        ])
        await query.message.edit_text(text=HELP_TXT, reply_markup=keyboard, disable_web_page_preview=True)

    # 3. DONATE MENU
    elif data == "donate":
        text = getattr(script, 'DONATE_TXT', "<b>Support the developer by donating!</b>")
        keyboard = InlineKeyboardMarkup([  
            [InlineKeyboardButton("< BACK", callback_data="home"),
             InlineKeyboardButton("CLOSE ×", callback_data="close")]
        ])
        await query.message.edit_text(text=text, reply_markup=keyboard)

    # 4. CLOSE MENU
    elif data in ["close", "cancel"]:
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception:
            pass

    # 5. TRY AGAIN FOR FORCE SUB
    elif data == "try_again":
        await query.message.delete()
        if f_sub:
            try:
                await bot.get_chat_member(f_sub, user_id)
            except Exception:
                await query.message.reply_text(
                    "<b>Hello Dear \n\nYou Need To Join In My Channel To Use Me\n\nKindly Please Join Channel</b>",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🔺 Update Channel 🔺", url=f"https://t.me/{f_sub}")],
                        [InlineKeyboardButton("🔄 Try Again", callback_data="try_again")]
                    ])
                )
                return

        text = START_TXT.format(mention=query.from_user.mention)
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("• CLICK FOR MORE •", url="https://t.me/ST_Rename_Update")],
            [InlineKeyboardButton("HELP", callback_data='help'),
             InlineKeyboardButton("UPDATES", url="https://t.me/ST_Rename_Update")],
            [InlineKeyboardButton("DONATE", callback_data='donate')]
        ])
        await query.message.reply_text(text=text, reply_markup=keyboard)
