import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5807124690:AAFxwdMtdp3GWWWMafj510QHl0QmHd2mKr0")
    API_ID = int(os.environ.get("API_ID", "4723828"))
    API_HASH = os.environ.get("API_HASH", "a41aa20922b2b9ed39ecbcffcd452154")
    BOT_OWNER = os.environ.get("BOT_OWNER", "MissSahip")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "VideoMuzikAsistan")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "VideoMuzikKayit")
    GROUP = os.environ.get("GROUP", "SohbetMavi") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001711522921"))
