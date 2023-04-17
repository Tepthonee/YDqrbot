import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["محمد","محمد مصطفى","حمد","المطور","Mohammad","حمودة"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("PPF22")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━━𝗠𝗢𝗛𝗔𝗠𝗠𝗔𝗗 ‌♡⁩━━⩺\n\n‍ ¦dev :{name}\n ¦user :@{usr.username}\n ¦id :`{usr.id}`\n ¦bio :{usr.bio}\n\n**⩹━━𝗠𝗢𝗛𝗔𝗠𝗠𝗔𝗗 ‌♡⁩━━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
