# Copyright (C) 2021 By KennedyProject


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as kennedy
from config import SUDO_USERS

@Client.on_message(filters.command(["gmcast"]))
async def broadcast(_, message: Message):
    if message.from_user.id not in SUDO_USERS:
        return

    wtf = await message.reply("`Starting Broadcast...`")
    if not message.reply_to_message:
        await wtf.edit("Please Reply To A Message To Start Broadcast !")
        return
    lmao = message.reply_to_message.text
    sent=0
    failed=0
    async for dialog in kennedy.iter_dialogs():
        try:
            await kennedy.send_message(dialog.chat.id, lmao)
            sent += 1
            await wtf.edit(f"`Broadcasting...` \n\n**Sent To :** `{sent}` Chats \n**Failed In :** {failed} Chats")
            await asyncio.sleep(3)
        except:
            failed += 1
    await message.reply_text(f"`Gcast Succesfully` \n\n**Sent To :** `{sent}` Chats \n**Failed In :** {failed} Chats")
