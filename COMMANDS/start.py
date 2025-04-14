from MAIN import Officer, HANDLERS, VERSION
from pyrogram import Client, filters 
from pyrogram.enums import ParseMode 



@Officer.on_message(filters.command("start", prefixes=HANDLERS)) 
async def start_the_bot(client, message):
  user = message.from_user
  user_id = user.id 
  username = user.first_name 

  welcome_text = f"""
    Welcome [{username}](tg://user?id={user_id}) to Abuse Prevention Bot! 🚫

    This bot is designed to help reduce abusive language and ensure a respectful environment in your chats.

    Here are some things this bot will do:
    - Automatically delete abusive messages
    - Warn users if they use inappropriate language
    - Ban users after repeated offenses

    Let's keep the chat clean and respectful! 😇

    Type any abusive or harmful word in you chat i will remove the Message 📩.
    """
  await message.reply_text(welcome_text, parse_mode=ParseMode.MARKDOWN)





  
