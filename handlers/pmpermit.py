from pyrogram import Client
import asyncio
from config import SUDO_USERS, PMPERMIT, OWNER_NAME, BOT_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from pyrogram import filters
from pyrogram.types import Message
from callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE" and PMSET:
        chat_id = message.chat.id
        if chat_id in pchats:
            return
        await USER.send_message(
            message.chat.id,
        f"✨ Hello, I'm A Official **Music Assistant Of 🎧⋆ {BOT_NAME} ✘ 𝙈𝙪𝙨𝙞𝙘 ⋆🎧.**\n\n❗️ **Notes :**\n\n⫸ Don'T Spam Message.\n⫸ Don'T Send Me Anything Confidential\n\n",
        )
        return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id not in SUDO_USERS:
        return
    global PMSET
    text = message.text.split(" ", 1)
    queryy = text[1]
    if queryy == "on":
        PMSET = True
        await message.reply_text("✅ Pmpermit Turned On.")
        return
    if queryy == "off":
        PMSET = None
        await message.reply_text("❌ Pmpermit Turned Off.")
        return

@USER.on_message(filters.text & filters.private & filters.me)
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id not in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approved To Pm Due To Outgoing Messages.")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("yes", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id not in pchats:
        pchats.append(chat_id)
        await message.reply_text("✅ Approved To Pm.")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("no", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("❌ Disapproved To Pm.")
        return
    message.continue_propagation()
