from pyrogram import Client, filter
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import randam
import os

PHOTO_LINK = [
 "Photo Link",
 "photo Link"
 ]

Muhammed = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)


@Muhammed.on_message(filters.message=="text"&&filters.group) 
async def start_message(bot, message)
    await message.delete()
   




 Muhammed.run()

