import os
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command
from helpers.decorators import errors, authorized_users_only

downloads = os.path.realpath("downloads")
raw = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "deletebokep"]) & ~filters.edited)
@errors
@authorized_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("🗑️ **Delete all downloaded files**")
    else:
        await message.reply_text("😕 **The downloaded file is empty, just like your heart!**")
