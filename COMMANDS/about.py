from MAIN import Officer
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

@Officer.on_inline_query()
async def show_info(client, inline_query):
    query = inline_query.query.strip()

    if query.lower() not in ["info", "about", "help"]:
        await inline_query.answer(
            [],
            switch_pm_text="Type 'info' to learn about the bot",
            switch_pm_parameter="start"
        )
        return

    inline_message = """
<b>🚀 THIS BOT IS USUALLY MADE FOR GROUPS.</b>
In which many users abuse and do s*x chats with girls and our sisters, etc.
We want to prevent this.

<b>PRESENTING YOU:-</b>
Our first and best robot of positive thoughts.
This bot can delete all messages, warn users, and ban them from groups to prevent bad chats.

<b>CRÉDIT 💳:</b>
• <a href="https://t.me/RaijinCodes_Ultra">@RaijinCodes_Ultra</a> - Member of 𝙲𝙾𝙳𝙴𝚂 𝙾𝙵 𝗟𝗘𝗚𝗘𝗡𝗗𝗦 | 伝説 also known as COL-X•忍者.
• <a href="https://t.me/McQueen95">@McQueen95</a> - Owner of TG Hexa Ultimate and idea contributor.

<b>[✉️ NOTICE]:</b>
If you want to create your own bots like this based on your thoughts,
Join: <a href="https://t.me/COLXproMainChannel">@COLXproMainChannel</a> and <a href="https://t.me/COL_Xpro_main">@COL_Xpro_main</a>
Authorize through @KuroAI_COLROBOT by tagging the owner @RaijinCodes_Ultra and then send your bot request.

____________________
<b>| THANK YOU ❤🌹🙏 |</b>
———————————————
"""

    result = InlineQueryResultArticle(
        title="👑 About",
        description="See 👀 what this Abuse Officer bot can do",
        input_message_content=InputTextMessageContent(inline_message, parse_mode=ParseMode.HTML)
    )

    await inline_query.answer([result], cache_time=1)
    
