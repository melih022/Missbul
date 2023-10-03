import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6188130506:AAF_YV9Aa2ErP6pPNHlypaSsmKthluBZ8BQ")
    API_ID = int(os.environ.get("API_ID", "20305957"))
    API_HASH = os.environ.get("API_HASH", "02f612321d53994c6a607ac2ba03206a")
    BOT_OWNER = os.environ.get("BOT_OWNER", "lreax")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "GoogleMuziksBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "GoogleMuzikKayıt")
    GROUP = os.environ.get("HAKKIMDA", "GoogleBilgi") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001711522921"))
