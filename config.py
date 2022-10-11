import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5715936867:AAEvplFt2NR9dpsgibN0mNZeJ_dg_jPNESk")
    API_ID = int(os.environ.get("API_ID", "4723828"))
    API_HASH = os.environ.get("API_HASH", "a41aa20922b2b9ed39ecbcffcd452154")
    BOT_OWNER = os.environ.get("BOT_OWNER", "MissMuzik")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MissMuzikBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "MissMuzikKayit")
    GROUP = os.environ.get("GROUP", "SohbetMiss") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001711522921"))
