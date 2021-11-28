from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.fsub import handle_force_subscribe
from config import UPDATES_CHANNEL


@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    if UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/robotprojectx"),
        InlineKeyboardButton(
            "ᴏᴡɴᴇʀ", url="https://t.me/justthetech")]
    ])
    welcomed = f"Hello <b>{message.from_user.first_name}! \nIni adalah Bot untuk medownload lagu / video dari youtube.</b>\n\nKetik /help untuk melihat cara penggunaannya"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
