import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6151655209:AAEuzgAAaq_MR47U8wYrCh9bKRBgUVrn1-g")
    API_ID = int(os.environ.get("API_ID", "20305957"))
    API_HASH = os.environ.get("API_HASH", "02f612321d53994c6a607ac2ba03206a)
    BOT_OWNER = os.environ.get("BOT_OWNER", "DeepBotsventor")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "DeepVcBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "DeepBotsMusic")
    GROUP = os.environ.get("HAKKIMDA", "DeepBotsOfficial") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001948617476"))
