import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21740783")
API_HASH = os.environ.get("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "")

CHANNEL = os.environ.get("CHANNEL", "Anime_Warrior_Tamil") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","Utsxititz_bot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","Anime_warrior_chat") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","Anime_Warrior_Tamil") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","speedwolf1")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","Speedwolf1")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://telegra.ph/file/60cc8a0f42af417fbefdb.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6299192020').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002134913785"))
