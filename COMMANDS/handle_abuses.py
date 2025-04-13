from MAIN import Officer, HANDLERS, VERSION, ABUSES
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from collections import defaultdict


# Abuse tracking dictionary (global for session)
abusive_limit = defaultdict(int)
SUPPORT_CHAT = -1002403025137

@Officer.on_message(filters.text & filters.group(SUPPORT_CHAT))
async def delete_abusive_msgs(client, message: Message):
    user = message.from_user
    user_id = user.id
    username = user.first_name
    text = message.text.lower()

    # Check if any abuse word is in the message
    if any(abuse.lower() in text for abuse in ABUSES):
        try:
            await message.delete()
        except:
            pass

        abusive_limit[user_id] += 1

        await message.reply(
            f"❌ [{username}](tg://user?id={user_id}), don't abuse please. This is a positive group.",
            parse_mode=ParseMode.MARKDOWN
        )

        # Warns then mute
        if abusive_limit[user_id] == 3:
            try:
                await Officer.restrict_chat_member(
                    message.chat.id,
                    user_id,
                    permissions=ChatPermissions(),
                    until_date=int(message.date.timestamp()) + 1800  # 30 minutes
                )
                await message.reply(
                    f"✅ [{username}](tg://user?id={user_id}) has been muted for 30 minutes for repeated abuse.",
                    parse_mode=ParseMode.MARKDOWN
                )
            except Exception as e:
                await message.reply("❌ Couldn't mute user, maybe I'm not admin or have no permission.")


      
