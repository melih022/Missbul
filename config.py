import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8431999361:AAHyc531MlXYioVSSq3-KIontgyFG7W7qTw")
    API_ID = int(os.environ.get("API_ID", "27992427"))
    API_HASH = os.environ.get("API_HASH", "07342c40853340995a492d0fc2de96cf")
    BOT_OWNER = os.environ.get("BOT_OWNER", "lreax")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Deepmusicdenemeebot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "sohbetGoogle")
    GROUP = os.environ.get("HAKKIMDA", "GoogleBilgi") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001977465611"))
