import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6157942511:AAEn-TCf4vOam72acFdg4_fM4U6NxejeToY")
    API_ID = int(os.environ.get("API_ID", "20305957"))
    API_HASH = os.environ.get("API_HASH", "02f612321d53994c6a607ac2ba03206a")
    BOT_OWNER = os.environ.get("BOT_OWNER", "lreax")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "GoogleMuzikBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "GoogleMuzikKayıt")
    GROUP = os.environ.get("HAKKIMDA", "GoogleBilgi") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001711522921"))
