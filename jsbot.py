import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Jsbot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jsbot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jsbot.send_message(
               chat_id=message.chat.id,
               text="""<b>Hey There, I'm Telegraph Bot

👻 This is a Telegraph uploader bot
for telegram.You can upload below types
to telegraph easily by using this bot

👇 You can upload 👇

📽️ Short Videos (Must be less than 5MB).
🎬 Round Videos.
🖼️ Pictures.
💥 Animations.
💟 Stickers.
📜 Text Posts.
📩 Inbox Supported.
👥 Group Supported.
🚀 Fast Uploading.

✍️ඔයාට අවශ්‍ය උඩ තියෙන ඕනෑම Media
එකක් මේ BOT ගෙන් Telegraph එකට Upload
කරල එකේ direct link එක ගන්න පුලුවන්😝

Hit help button to find out more about how to use me</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                               [[
                                        InlineKeyboardButton(
                                            "🌷Help", callback_data="help"),
                                        InlineKeyboardButton(
                                            "✨Channel", url="https://t.me/janithsbots"),
                                         InlineKeyboardButton(

                                            "Youtube Channel", url="www.youtube.com/Janithsadanuwan")
                                  [[
                                     
                                   reply_markup=InlineKeyboardMarkup(
                               [[
                                         InlineKeyboardButton(
 
                                            "➕ Add Me To Your Group ➕", url="http://t.me/The_Thelegraph_Uploader_Bot?startgroup=botstart")
                                    ]]
                            ),
            disable_web_page_preview=True,        
            parse_mode="html")

@Jsbot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jsbot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help🙈

Just send a photo or video less than 5mb file size, I'll upload it to telegraph.🎉

☘️ Dҽᐯҽ𝘭๏pҽᏒ : @janith_sadanuwan

@janithsbots</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "👻About", callback_data="about"),
                                  ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jsbot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jsbot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>

<b>☘️ Dҽᐯҽ𝘭๏pҽᏒ :</b> <a href="https://t.me/janith_sadanuwan">Janith sadanuwan🇱🇰</a>

<b>🔆Language:</b> <a href="https://www.python.org/">Python 3</a>

<b>♻️Library:</b> <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>

<b>@janithsbots</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "❌Close", callback_data="close")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jsbot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Your File Is Successfully Uploaded To Telegraph!\n\n👻https://telegra.ph{response[0]}\n\nJoin @janithsbots**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Jsbot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Your File Is Successfully Uploaded To Telegraph!\n\n👻https://telegra.ph{response[0]}\n\nJoin @janithsbots**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Jsbot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Your File Is Successfully Uploaded To Telegraph!\n\n👻https://telegra.ph{response[0]}\n\nJoin @FZBOTS**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Jsbot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
Join @janithsbots
"""
)

Jsbot.run()
