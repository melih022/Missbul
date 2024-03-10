import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6188130506:AAGieqMNYDVBtsMdCI9GhEsWwGSplthmjVs")
    API_ID = int(os.environ.get("API_ID", "28167888"))
    API_HASH = os.environ.get("API_HASH", "d27cbb6932219fcf1bfd6137485c5bac")
    BOT_OWNER = os.environ.get("BOT_OWNER", "lreax")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "GoogleMuziksBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "GoogleMuzikKayıt")
    GROUP = os.environ.get("HAKKIMDA", "GoogleBilgi") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001711522921"))
