import os, youtube_dl, requests, time
import re
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
import json
import telegram
from datetime import datetime
from pyrogram.types import CallbackQuery


# Botu oluşturun
deep = TelegramClient('bot', api_id = Config.API_ID,api_hash = Config.API_HASH).start(bot_token=Config.BOT_TOKEN)

#config#

bot = Client(
    'moonBot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
client = TelegramClient('client', api_id = Config.API_ID, api_hash = Config.API_HASH).start(bot_token = Config.BOT_TOKEN )
LOG_GROUP_ID = -1001931419270
anlik_calisan = []
ozel_list = [5009212526]
grup_sayi = [] 
sayı_calısan = []
# Botu kötüye kullanarak "oynat" komutunu çalıştıran kullanıcıları takip edin
PLAY_THRESHOLD = 8
PLAY_TIME_WINDOW = 5
play_counts = {}






# Telegram Bot API anahtarını buraya girin
bot_token = "6188130506:AAF_YV9Aa2ErP6pPNHlypaSsmKthluBZ8BQ"

# Telegram Bot API'nin temel URL'si
bot_url = f"https://api.telegram.org/bot6188130506:AAF_YV9Aa2ErP6pPNHlypaSsmKthluBZ8BQ/"

# Bot sahibinin ID'si
owner_id = "5009212526"

# "/stats" komutunu işleyen fonksiyon
def handle_stats_command(chat_id):
    # Botunuzun kullanıldığı grupları ve kanalları saymak için kullanacağımız değişkenler
    small_groups = 0
    large_groups = 0
    channels = 0

    # Botunuzun bulunduğu grupları ve yetkili olduğunuz grupları saymak için kullanacağımız değişkenler
    total_groups = 0
    admin_groups = 0

    # Botunuzun kullanıldığı tüm grupları ve kanalları alın
    get_updates_url = f"{bot_url}getUpdates"
    response = requests.get(get_updates_url)
    data = json.loads(response.content)

    # Her grup ve kanal için gerekli bilgileri alın
    for update in data["result"]:
        chat_type = update["message"]["chat"]["type"]
        if chat_type == "group":
            members_count = update["message"]["chat"]["members_count"]
            if members_count < 100:
                small_groups += 1
            else:
                large_groups += 1
            total_groups += 1
            # Eğer bot yetkili ise, admin_groups değişkenini arttırın
            if "entities" in update["message"] and update["message"]["entities"][0]["type"] == "bot_command":
                admin_groups += 1
        elif chat_type == "channel":
            channels += 1

    # Mesajı oluşturun
    message = f"Bot {small_groups} üyesi 100 altındaki gruplarda ve {large_groups} üyesi 100 üstündeki gruplarda kullanılıyor. Toplamda {total_groups} grupta bulunuyor ve bunların {admin_groups} tanesinde yetkili olarak çalışıyor."

    # Mesajı gönderin
    send_message_url = f"{bot_url}sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(send_message_url)

# Botunuzun mesajları almak için kullanacağı URL
get_updates_url = f"{bot_url}getUpdates"

# Botunuzun mesajları sürekli olarak kontrol edin
while True:
    # Botunuzun mesajları alın
    response = requests.get(get_updates_url)
    data = json.loads(response.content)

    # Her mesaj için gerekli işlemleri yapın
    for update in data["result"]:
    # Eğer mesajın "message" anahtarı yoksa, bir sonraki mesaja geçin
       if "message" in update and "text" in update["message"]:
       message_text = update["message"]["text"]
    # Devam eden işlemler
       else:
    print("Geçerli bir metin mesajı bulunamadı.")

           

    # Mesajın metnini alın
       message_text = update["message"]["text"]

    # Mesajın gönderildiği chat'in ID'sini alın
       chat_id = update["message"]["chat"]["id"]

    # Eğer mesaj "/stats" ise, handle_stats_command fonksiyonunu çağırın
       if message_text == "/stats" and str(chat_id) == owner_id:
           handle_stats_command(chat_id)
# "oynat" veya "voynat" komutunu takip eden filtre
@bot.on_message(filters.command(["oynat", "voynat"]))
def play_command_handler(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.from_user.username
    nickname = message.from_user.first_name or "bilinmiyor"
    if username is None:
        mention = f"<a href='tg://user?id={user_id}'>{nickname}</a>"
    else:
        mention = f"@{username}"
    group_id = message.chat.id
    group_name = message.chat.title
    

    current_time = int(time.time())

    # Kullanıcının "oynat" veya "voynat" komutunu çalıştırma sayısını izleyin
    if user_id not in play_counts:
        play_counts[user_id] = []

    play_counts[user_id].append(current_time)

    # Son 10 saniye içinde kaç kez "oynat" veya "voynat" komutu çalıştırıldı
    count_in_window = len([
        t for t in play_counts[user_id]
        if current_time - t <= PLAY_TIME_WINDOW
    ])

    # Uyarı mesajı gönderin ve günlüğe kaydedin
    if count_in_window >= PLAY_THRESHOLD:
        # Uyarı mesajı
        log_message = (
            f"Grup: {group_name}\n [{group_id}]\n\n"
            f"Kullanıcı Nick : {mention}\n\n"
            f"Kullanıcı ismi: {nickname}\n\n"
            f"ID: {user_id}\n\n"
            
            "'oynat' veya 'voynat' komutunu çok sık kullandı. \n@GooglemuzikSahip\n @lReax\n@AtomFast"
        )
        client.send_message(LOG_GROUP_ID, log_message)

        # Kullanıcıya özel uyarı mesajı
       
        user_message = "\n❌Bota Spam Atmayın❌\nGruptan Ayrılıyorum.\nTekrar Spam Atarsanız Botu Artık Kullanamayacaksınız...\nDestek İçin:@lReax"
        client.send_message(chat_id, f"{mention}: {user_message}")
        client.leave_chat(chat_id)        
        
@client.on(events.NewMessage(pattern='^/reload ?(.*)'))

async def chatid(event):

    global grup_sayi

@client.on(events.NewMessage(pattern='^/start@GoogleMüzikBot ?(.*)'))

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
    global anlik_calisan, grup_sayi, ozel_list
    sender = await event.get_sender()
    if sender.id in ozel_list:
        await event.respond(f"**Grup sayısı 🤖**\n\nToplam Grup: `{len(grup_sayi)}`")
    else:
        await event.respond("Bu Komutu Sadece Sahibim Kullanabilir")

                        

# "/statik" komutu işleyici
# "/statik" komutu işleyici
# "/statik" komutu işleyici
@bot.on_message(filters.command("statik") & ~filters.edited)
async def grup_bilgileri(event):
    global grup_sayi, ozel_list
    user_id = event.sender_id
    
    if user_id in ozel_list:
        args = event.pattern_match.group(1)
        
        if not args:
            total_group_count = len(grup_sayi)
            await event.reply(f"Toplam grup sayısı: `{total_group_count}`")
        elif args.isdigit():
            member_count = int(args)
            less_than = 0
            more_than = 0
            for group in grup_sayi:
                if group['member_count'] < member_count:
                    less_than += 1
                else:
                    more_than += 1
            await event.reply(f"{less_than} grupta {member_count}'ten az üye var. {more_than} grupta ise daha fazla.")
        else:
            await event.reply("Geçerli bir sayı belirtiniz.")
    else:
        await event.reply("Bu komutu kullanma izniniz yok.")
    
#@client.on(events.NewMessage(pattern='^/statik (\d+)'))
#async def grup_bilgileri_uyeler(event):
    #global anlik_calisan,grup_sayi,ozel_list
    #sender = await event.get_sender()
    #if sender.id not in ozel_list:
       # member_count = int(event.pattern_match.group(1))
       # less_than = 0 
        #more_than = 0
        #async for dialog in client.iter_dialogs():
            #if dialog.is_group and dialog.entity.members_count < member_count:
                #less_than += 1
            #elif dialog.is_group:
                #more_than += 1
        #await event.reply(f"{less_than} grupta {member_count}'ten az üye var. {more_than} grupta ise daha fazla.")
    #else:
        #await event.reply("Bu komutu kullanma izniniz yok.")

#@client.on(events.NewMessage(pattern='^/ayrıl (\d+)'))
#async def grup_cik(event):
    #global anlik_calisan,grup_sayi,ozel_list
    #sender = await event.get_sender()
    #if sender.id not in ozel_list:
        #member_limit = int(event.pattern_match.group(1))
        #count = 0
        #async for dialog in client.iter_dialogs():
            #if dialog.is_group and dialog.entity.members_count == member_limit:
                #count += 1
                # Burada grupu çıkarmak için gerekli işlemleri gerçekleştirin
        #await event.reply(f"{count} gruptan çıkıldı.")
    #else:
        #await event.reply("Bu komutu kullanma izniniz yok.")
    # buraya kadar
 
@client.on(events.NewMessage(pattern='^/destek ?(.*)'))
async def destek(event):
    chat_id = event.chat_id
    talep_mesaji = event.pattern_match.group(1)
    
    # Mesajın gönderildiği grup bilgileri
    group_title = event.chat.title
    group_link = event.chat_id
    
    # Mesajı gönderen kullanıcının bilgileri
    user_id = event.from_id.user_id
    
    user_name = event.sender.first_name
    user_surname = event.sender.username
    # Mesajı log grubuna gönder
    log_message = (
    f"**Google~Bot~İnfo**\n\n"
    f"💬 𝙶𝚛𝚞𝚙 𝙱𝚒𝚕𝚐𝚒 💬\n"
    f"Grup İsmi: [{group_title}]\n"
    f"Grup ID'si: {chat_id}\n\n"
    f"👤 𝙺𝚞𝚕𝚕𝚊𝚗𝚒𝚌𝚒 𝙱𝚒𝚕𝚐𝚒 👤\n"
    f"İsim: {user_name}\n"
    f"Kullanıcı adı: @{user_surname}\n"
    f"ID: {user_id}\n\n"
    f"Mesaj:\n{talep_mesaji}\n\n"
    f"@lReax\n"
    
    
)

    
    
    # Slogan ve fotoğraf mesajı
    photo = open('Deep.jpg', 'rb')
    if talep_mesaji:
        slogan = "**Mesajınız Bot Yetkililerine İletilmiştir. Kısa Sürede Geri Dönüş Sağlanacaktır. İyi Günler💫**"
        await bot.send_message(LOG_GROUP_ID, log_message)
    else:
        slogan = "**Keşfetmek İçin Derinlere Dal 💫**"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("👨‍💻~𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫~🧑‍💻", url=f"https://t.me/GoogleMuzikSahip"),
                InlineKeyboardButton("📜 𝙆𝙤𝙢𝙪𝙩𝙡𝙖𝙧 📜", url=f"https://t.me/GoogleMuziksBot?start=help")
            ]
        ]
    )
    await bot.send_photo(
        chat_id=chat_id, photo=photo, caption=slogan,
        reply_markup=keyboard
    )
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

        mel = f"╔═══════════════╗\nGoogle Müzik\n\n➤🏷Başlık :{audio_file}\n\n➤👤Talep Eden :{kisi}\n\n➤🤖Bot :@GoogleMüzikBot\n\n╚══════════════╝"

        
        rep = f"𝙸𝚗𝚍𝚒𝚛𝚍𝚒𝚐𝚒𝚗𝚒𝚣 𝚃𝚞𝚖 𝙼𝚞𝚣𝚒𝚔𝚕𝚎𝚛 𝙂𝙤𝙤𝙜𝙡𝙚 𝙈𝙪𝙯𝙞𝙠 Music 𝙺𝚊𝚗𝚊𝚕𝚒𝚖𝚒𝚣𝚍𝚊 𝙺𝚊𝚢𝚒𝚝 𝙰𝚕𝚝𝚒𝚗𝚊 𝙰𝚕𝚒𝚗𝚖𝚊𝚔𝚝𝚊𝚍𝚒𝚛."
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("•> **Yükleniyor**...")
        
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="@GoogleMüzikBot",
        reply_markup = InlineKeyboardMarkup(
           [
                [
                    InlineKeyboardButton(
                        text="🎧 𝙂𝙤𝙤𝙜𝙡𝙚 𝙈𝙪𝙯𝙞𝙠 🎧",
                        url="https://t.me/GoogleMuzikKayit")
                   
                ]
            ]
        )
      )
        m.delete()
        bot.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, performer="@GoogleMüzikBot", parse_mode='md', title=title, duration=dur, thumb=thumb_name,)
    except Exception as e:
        m.edit("<b>⛔ **Hatanın düzelmesini bekleyin** .</b>")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        
        

bot.run()
