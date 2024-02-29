from telethon.tl.custom import Button
from telethon import TelegramClient, events
from telegraph import Telegraph, upload_file
from DILXHACK import bot
import os

telegraph = Telegraph()


def get_file_id(msg):
    if msg.media:
        for message_type in (
                "photo",
                "animation",
                "audio",
                "document",
                "video",
                "video_note",
                "voice",
                "sticker"
        ):
            obj = getattr(msg, message_type, None)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj


@bot.on(events.NewMessage(pattern='/tgm', func=lambda e: e.is_private))
async def telegraph_upload(event):
    replied = await event.get_reply_message()
    if not replied:
        await event.reply("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝚄𝙽𝙳𝙴𝚁 𝟻𝙼𝙱.")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await event.reply("Not supported!")
        return
    text = await event.reply("𝐖𝐚𝐢𝐭 𝐁𝐫𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐭𝐨 𝐌𝐲 𝐒𝐞𝐫𝐯𝐞𝐫 ...")
    media = await replied.download_media(file='media')
    await text.edit("</>𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝. 𝐍𝐨𝐰 𝐈 𝐚𝐦 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐭𝐨 𝐭𝐞𝐥𝐞𝐠𝐫𝐚.𝐩𝐡 𝐋𝐢𝐧𝐤 ...</>")
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        await text.edit(f"Error :- {error}")
        return
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return
    await text.edit(
        text=f"ʟɪɴᴋ ʙᴇʟᴏᴡ :- \n\n `https://graph.org{response[0]}`",
        buttons =  [
                [
                    Button.url("ᴏᴘᴇɴ ʟɪɴᴋ", url=f"https://graph.org{response[0]}"),
                    Button.url("ꜱʜᴀʀᴇ ʟɪɴᴋ", url=f"https://telegram.me/share/url?url=https://graph.org{response[0]}")
                ],
            ]
        )
