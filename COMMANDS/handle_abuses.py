from MAIN import Officer, HANDLERS, VERSION, ABUSES
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, ChatPermissions
from collections import defaultdict

abusive_limit = defaultdict(int)

@Officer.on_message(filters.text & ~filters.command)
async def delete_abusive_msgs(client, message: Message):
    user = message.from_user
    if not user:
        return

    user_id = user.id
    username = user.first_name
    text = message.text.lower()

    if any(abuse.lower() in text for abuse in ABUSES):
        try:
            await message.delete()
        except:
            pass

        abusive_limit[user_id] += 1

        try:
            await message.reply(
                f"❌ [{username}](tg://user?id={user_id}), don't abuse please. This is a positive group.",
                parse_mode=ParseMode.MARKDOWN
            )
        except:
            pass

        if abusive_limit[user_id] == 3:
            try:
                await Officer.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=user_id,
                    permissions=ChatPermissions(),
                    until_date=int(message.date.timestamp()) + 1800
                )
                await message.reply(
                    f"✅ [{username}](tg://user?id={user_id}) has been muted for 30 minutes for repeated abuse.",
                    parse_mode=ParseMode.MARKDOWN
                )
            except Exception as e:
                await message.reply(
                    "❌ Couldn't mute user. Make sure I'm an admin with restrict permissions."
                )
