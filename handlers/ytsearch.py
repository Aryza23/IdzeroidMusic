import logging
from pyrogram.types import Message
from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch
from pyrogram import Client as app, filters
from helpers.filters import command
from config import BOT_USERNAME

BOT_USERNAME : "idzeroid_bot"


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)


@app.on_message(command(["search", f"search@{BOT_USERNAME}"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**/Search Give Video Name !!**")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("🔎 **Searching Video**")
        results = YoutubeSearch(query, max_results=4).to_dict()
        text = ""
        for i in range(4):
            text += f"**Title :** `{results[i]['title']}`\n"
            text += f"**Duration :** {results[i]['duration']}\n"
            text += f"**Views :** {results[i]['views']}\n"
            text += f"**Channel :** {results[i]['channel']}\n"
            text += f"https://www.youtube.com{results[i]['url_suffix']}\n\n"
            text += "**Powered By :** __@IdzXartez__\\n"
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
