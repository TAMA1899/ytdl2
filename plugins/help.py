from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.fsub import handle_force_subscribe
from config import UPDATES_CHANNEL

@Client.on_message(filters.command(["help"]))
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
    helptxt = f"**Paste Link YouTube Kesini** \n► Atau Ketik @vid (spasi) (judul lagu) \n► Lalu klik videonya"
    await message.reply_text(helptxt)
