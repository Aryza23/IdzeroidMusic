import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Aries")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/ccdb7dd3392bc90248472.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "idzeroid_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "idzxmusic")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "idzeroidsupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "idzeroid")
OWNER_NAME = getenv("OWNER_NAME", "idzxartez") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "idzxartez")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
PMPERMIT = getenv("PMPERMIT", None)
LOG_CHANNEL = getenv("LOG_CHANNEL", None)
DATABASE_URL = os.environ.get("DATABASE_URL")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
OWNER_ID = int(os.environ.get("OWNER_ID"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/idzero23/IdzeroidMusic"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
