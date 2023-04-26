import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "QuranBot")

OWNER_ID = list(map(int, getenv("OWNER_ID", "1260465030").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Tepthonee/QuranBot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/T8OTT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/PPF22")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BABwBdCkTyyKhITugQfx5Ect92QxqBIfRS7mxGEnmAKLvmatcdcgAJvUDCybQSWCkdQIKgmSKp0BiSQFPL6QiHeFk1XsmZmCf1vb9lqDWhxDLx4SwqIvn0Q5GxD3mgedcQcPqazEOEQacv_2-n2A4Gk065ArgVovz5d2th6DtN3jd38hbh6BR24OyIcwS_iy2gmvvHApFG950WtwvmbPoi0hlvMdrwYewbBIsuZSbJ3rO0a1mjQiC62E49ykUBNgaz0p9IjdoMo6ttotAWTMkMorpAYtbqd49Xjl_naM0_zMS0tYfA8uM6xa574X6PRkFS9pZTVh6DqdRM5esNiKp_UvAAAAAWBktm0A")
STRING2 = getenv("STRING_SESSION2", "BABvuX1xD2VqJcIJm51CPLn1IwChGslfmn8Pe0fX7PspJXUXUxUO1es54P3_25_dOxqTEfBH76qLHOmkUmNXlBc0E2R84RZQzQVgmaYpalnWsG4RByo6ntvjuCB9iiwxfpXmbch5I_-OrA7czVnkNKZS5jPna1vQnCNL4jdc74AEsOKVsPvcmZSy9Rn_Dds3anTJsA0_tuKJaeQ1H8wcTpclvN6jfbzEk6dYBgReDKO-_corEBhWiWFHJPvIB0YC2E1orOt00s4iBapuOUXlNGNd74aXRJ102-h4n_6U2v0qVU8JCyxtm3IcwdsgiLRFItVAOzjCUx0aquhdyCAIjMFXAAAAAW2PJXYA")
STRING3 = getenv("STRING_SESSION3", "BAAp2uKQKAezBmVex5YvMrJubVHYFL_UeBCCTeIa0Snaxb_IUBieHkm_TdFrwn-SKChSRfPQrsNPmtIKrMYouaUkb3bIzTMEpbOKepnr18E05j6O43FK7gugFDUyhg5Os9kUbXkE8KDyPtrpNdJ1Rc_N80TlgdCUwFv9Z7lKrrAbSS5LdMoWSsfWGFVe2TKkOvVg_IL5xc1qMMqp4kjtKJGgu8XNNoTnTgJ7WGKPtSLQBXQrKNEJvLXvAWsKxHTpKnxRgSJSlAye_lVYPDIdAp2GWcgI3zeIEi7B9apIyO_n1MOt-uKL15_25kwilC_SVK-6V6O4WPlgLYV2BmHuB4iGAAAAAVQd7IwA")
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/e31e799f9423247350739.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/e31e799f9423247350739.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/e31e799f9423247350739.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/56d1760224589ee370186.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/56d1760224589ee370186.jpg"
