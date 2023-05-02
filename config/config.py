import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "6121660804:AAGKFSo-iU7vuPNDYxVeTUrWJ5Fxz1ypq-I")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgAVg1Kf3Sx1iLpA2cZnjcDKZUSC0JT8jW6LJPAZdtSS1Sav5QVcqb-MyiQG097RR3C8_Q04At6YXz83u0MAgTA4tOa5PvCR-cK3P7y0zy_x-uU0IlDJpCiYgZoaTpL2OjbKwHVNTCxCTtuawMF-Xta5cpTu9Ot8ILfbFv-tp0vR5Qv5lxK7GAg97c66MRge8PbdfMTb7MoCFw9vfT0gcef0CSEN1MTNPPmRZxtEv5qSfPuYFBNU-zMhi6iU9mcIWGIEK2c_w6eSLSCcHCuJpKWT3grCQp77VnlWxAj6ohEe8rtaTe7XpKvd_eHEHyhYAYVWkBNhFlpMDaRC84joUG2QAAAAAXdy-zcA")
BOT_USERNAME = getenv("BOT_USERNAME", "P2_Ebot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5598607769").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5598607769").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001847569598")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "isM6s")
GROUP = getenv("GROUP", "isM6s")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


