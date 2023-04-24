import os, youtube_dl, requests, time
from config import Config
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
import yt_dlp
from telethon import TelegramClient, events
from telethon import Button
from telethon import Button
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)
import requests
import telegram


#config#

bot = Client(
    'moonBot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
client = TelegramClient('client', api_id = Config.API_ID, api_hash = Config.API_HASH).start(bot_token = Config.BOT_TOKEN )
 
#start mesajı






anlik_calisan = []

ozel_list = [5009212526]





grup_sayi = [] 

sayı_calısan = []

@client.on(events.NewMessage(pattern='^/reload ?(.*)'))

async def chatid(event):

    global grup_sayi




  


    

      

         

@client.on(events.NewMessage(pattern='^/start@deepvcbot ?(.*)'))

async def chatid(event):

    global grup_sayi

@client.on(events.NewMessage())

async def chatid(event):

  global etiketuye

  if event.is_group:

    if event.chat_id in grup_sayi:

      pass

    else:

      grup_sayi.append(event.chat_id)
@client.on(events.NewMessage())
async def mentionalladmin(event):
  global grup_sayi
  if event.is_group:
    if event.chat_id in grup_sayi:
      pass
    else:
      grup_sayi.append(event.chat_id)

@client.on(events.NewMessage(pattern='^/statik ?(.*)'))
async def son_durum(event):
    global anlik_calisan,grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**Grup sayısı 🤖**\n\nToplam Grup: `{len(grup_sayi)}`")
                        

 
@client.on(events.NewMessage(pattern='^/deep ?(.*)'))
async def destek(event):
    chat_id = event.chat_id
    photo = open('Deep.jpg', 'rb')
    caption = '**Keşfetmek İçin Derinlere Dal💫**'

    await bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, buttons=[Button.url('🧑‍💻~𝐒𝐚𝐡𝐢𝐛𝐢𝐦~🧑‍💻', f'https://t.me/DeepBotsventor'), Button.url('🧑‍💻~𝐃𝐞𝐞𝐩 𝐁𝐨𝐭𝐬~🧑‍💻', f'https://t.me/DeepBotsofficial')])

    photo.close()

    
@bot.on_message(filters.command("bul") & ~filters.edited)
def bul(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("<b>• 🔍 𝐀𝐑𝐀𝐍𝐈𝐘𝐎𝐑...</b>")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("<b>⛔ **❌ Ş𝚊𝚛𝚔ı 𝙱𝚞𝚕𝚞𝚗𝚊𝚖𝚊𝚍ı.\n\n 𝙻𝚄̈𝚃𝙵𝙴𝙽 𝙶𝙴𝙲̧𝙴𝚁𝙻𝙸̇ 𝙱𝙸̇𝚁 𝚂̧𝙰𝚁𝙺𝙸 𝙰𝙳𝙸 𝚅𝙴𝚁𝙸̇𝙽.**</b>")
        print(str(e))
        return
        m.edit("<b>•> 📥 𝙸̇𝙽𝙳𝙸̇𝚁𝙼𝙴 𝙸̇𝚂̧𝙻𝙴𝙼𝙸̇ 𝙱𝙰𝚂̧𝙻𝙰𝚃𝙸𝙻𝙳𝙸...**</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        kisi = f"@{message.from_user.username}"

        mel = f"╔═══════════════╗\nDeep Bots\n\n➤🏷Başlık :{audio_file}\n\n➤👤Talep Eden :{kisi}\n\n➤🤖Bot :@DeepVcBot\n\n╚══════════════╝"

        
        rep = f"𝙸𝚗𝚍𝚒𝚛𝚍𝚒𝚐𝚒𝚗𝚒𝚣 𝚃𝚞𝚖 𝙼𝚞𝚣𝚒𝚔𝚕𝚎𝚛 Deep Bots Music 𝙺𝚊𝚗𝚊𝚕𝚒𝚖𝚒𝚣𝚍𝚊 𝙺𝚊𝚢𝚒𝚝 𝙰𝚕𝚝𝚒𝚗𝚊 𝙰𝚕𝚒𝚗𝚖𝚊𝚔𝚝𝚊𝚍𝚒𝚛."
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("•> **Yükleniyor**...")
        
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="@VideoMuzikBot",
        reply_markup = InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton(
                        text="🎧 𝐃𝐞𝐞𝐩 𝐁𝐨𝐭𝐬 𝐊𝐚𝐲𝐢𝐭 🎧",
                        url="https://t.me/DeepBotsMusic")
                   
                ]
            ]
        )
      )
        m.delete()
        bot.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=mel, performer="@DeepVcBot", parse_mode='md', title=title, duration=dur, thumb=thumb_name,)
    except Exception as e:
        m.edit("<b>⛔ **Hatanın düzelmesini bekleyin** .</b>")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

bot.run()
