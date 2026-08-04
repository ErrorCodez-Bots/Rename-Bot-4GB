from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)
from pyrogram import Client, filters
from config import *

@Client.on_callback_query(filters.regex('^(about|help|home|back|donate|more|close|cancel|try_again)$'))
async def cb_handler(bot, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id
    f_sub = FORCE_SUBS.replace("@", "") if FORCE_SUBS else None

    # 1. HOME / BACK TO MAIN START MENU
    if data in ["home", "back"]:
        keyboard = InlineKeyboardMarkup([  
            [InlineKeyboardButton("• CLICK FOR MORE •", callback_data="more")],
            [InlineKeyboardButton("HELP", callback_data='help'),
             InlineKeyboardButton("UPDATES", url=UPDATE_CHANNEL)],
            [InlineKeyboardButton("DONATE", callback_data='donate')]
        ])
        await query.message.edit_text(text=START_TXT.format(mention=query.from_user.mention), reply_markup=keyboard)

    # 2. CLICK FOR MORE MENU
    elif data == "more":
        keyboard = InlineKeyboardMarkup([ 
            [InlineKeyboardButton("< BACK", callback_data='home'),
             InlineKeyboardButton("CLOSE ×", callback_data='close')]
        ])
        await query.message.edit_text(text=MORE_TXT, reply_markup=keyboard, disable_web_page_preview=True)

    # 3. HELP MENU
    elif data == "help":
        keyboard = InlineKeyboardMarkup([ 
            [InlineKeyboardButton("< BACK", callback_data='home'),
             InlineKeyboardButton("CLOSE ×", callback_data='close')]
        ])
        await query.message.edit_text(text=HELP_TXT, reply_markup=keyboard, disable_web_page_preview=True)

    # 4. DONATE MENU (< BACK & CLOSE ×)
    elif data == "donate":
        keyboard = InlineKeyboardMarkup([  
            [InlineKeyboardButton("< BACK", callback_data='home'),
             InlineKeyboardButton("CLOSE ×", callback_data="close")]
        ])
        await query.message.edit_text(text=DONATE_TXT, reply_markup=keyboard, disable_web_page_preview=True)

    # 5. CLOSE MENU
    elif data in ["close", "cancel"]:
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception:
            pass

    # 6. TRY AGAIN FOR FORCE SUB
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

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("• CLICK FOR MORE •", callback_data="more")],
            [InlineKeyboardButton("HELP", callback_data='help'),
             InlineKeyboardButton("UPDATES", url=UPDATE_CHANNEL)],
            [InlineKeyboardButton("DONATE", callback_data='donate')]
        ])
        await query.message.reply_text(text=START_TXT.format(mention=query.from_user.mention), reply_markup=keyboard)
