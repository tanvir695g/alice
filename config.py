import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 22720167
API_HASH = "7003cbe84391ac6418a27d1a37d63576"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7174214704:AAEEq2WmkKSprhpPAGehDjCibUgg8oey__o"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://tanvir999:tanvir999@cluster0.2vpwn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002354150409

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 8152959965

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/tbpmusic999"
SUPPORT_GROUP = "https://t.me/TBP_MUSIC999"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQAf70YAuWly_rfh3Z17SE28GizYv77m4nRRuSLRtq-N-Ndf040RDGaHH4zAQFfXiMVxFBJ625Dhzg4fsbwG62SG3qXu4AmlFTN3uvB4vsDrp3VOjfqEgWe-R9dIWYBXt0E8cf2C41kUJw7x6Dvybz1qvbhi_y2utzma4l-7Sr7xIw2RolCwC3OD2K21YXyphIolL7SwEK8mCOVa2rBPN9BTtVtZmeF5ZYvuysbgCt1MxY_rbqrGhmHr4c_XXi5LmoniiEa4oDlARVtNl5vt6nZwAuT1aeTir7Om8EljuA-bdcQeru_LFsTRE1rzEfUHPkcDlT7zICIAv5MvmxfB7r2-yf9AAAAAHl9EvdAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"

PING_IMG_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"
STATS_IMG_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"
STREAM_IMG_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/9153e1dbfad7f82e653c8-b2a80d83c7ad920acd.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
