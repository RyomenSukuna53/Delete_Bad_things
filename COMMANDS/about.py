from MAIN import Officer, HANDLERS, VERSION 
import config
from pyrogram import Client, filters 
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


@Officer.on_inline_query() 
async def show_info(client, inline_query):
  query = inline_query.query.strip() 

  inline_message = f""" 
      🚀 THIS BOT IS USUALLY MADE FOR GROUPS.
      IN WHICH MANY USERS ABUSE AND DO S*X CHATS WITH GIRLS AND OUR SISTERS ETC.
      WE WANT TO PREVENT THIS. 


      PRESENTING YOU:-
                      OUR FIRST AND BEST ROBOT OF POSITIVE THOUGHTS. 
      THIS BOT CAN DELETE ALL MSGS AND WARN USERS BAN THEM FROM GC TO PREVENT BAD CHATS. 
 
      CRÉDIT 💳:-
                 [@RaijinCodes_Ultra] MEMBER OF  𝙲𝙾𝙳𝙴𝚂 𝙾𝙵 𝗟𝗘𝗚𝗘𝗡𝗗𝗦 | 伝説 ALSO KNOWN AS [𝙲𝙾𝙻-𝙓•忍者].

                 AND 

                 [@McQueen95] OWNER OF TG HEXA ULTIMATE AND GIVE THE IDEA TO CREATE THIS BOT.


      [✉️NOTICE]:- 
                IF YOU WANT TO CREATE YOUR OWN BOTS LIKE THIS ON YOUR THOUGHTS. 

                JOIN:- @COLXproMainChannel and @COL_Xpro_main.

                AUTHORIZE YOU BY BOT @KuroAI_COLROBOT BY TAGGING OWNER @RaijinCodes_Ultra AND THEN SEND YOUR ORDER REQUEST TO CREATE IT. 

                ___________________
                |𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 ❤🌹🙏|
                ———————————————————

                 """


  
  if not query:
    await inline_query.answer([], switch_pm_text="Type info to get info...", 
                              switch_pm_parameter="start") 
    return 

  result = InlineQueryResultArticle(title="👑 About",
                                    description="See 👀 my about section  what this abuse officer can do",
                                    input_message_content=InputTextMessageContent(inline_message)
        )
    

  await inline_query.answer(results, cache_time=1)


                                    



