from Dasha.events import dasha
from Dasha import StartTime
import time, datetime
from . import get_readable_time
from telethon import Button, version

@dasha(pattern="^/ping")
async def _(event):
    start_time = datetime.datetime.now()
    message = await event.edit("`Pinging..`")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b>『 ☛ Pᴏɴɢ :</b> <code>{}</code>\n"
        "<b>     ☛ Uᴘᴛɪᴍᴇ :</b> <code>{}</code>』".format(telegram_ping, uptime),
        parse_mode="html",
    )
'''      
@dasha(pattern="^/repo$")
async def repo(event):
      await event.client.send_file(event.chat_id, file='Dasha/resources/Dasha.jpg', caption='click - **[Rᴇᴘᴏ](http://github.com/tamilvip007/dasha)**')
'''
@dasha(pattern="^/alive$")
async def alive(event):
 try:
    chat = await event.get_chat()
    await event.delete()
    uptime = get_readable_time((time.time() - StartTime))
    x = "**               【  𝙳𝙰𝚂𝙷𝙰 𝙸𝚂 𝙰𝙻𝙸𝚅𝙴 】 **\n\n"
    x += "**Sʏsᴛᴇᴍs ᴀʀᴇ ᴡᴏʀᴋɪɴɢ ᴘᴇʀғᴇᴄᴛʟʏ...**\n\n"
    x += "**✘** 🄰🄱🄾🅄🅃 🄼🅈 🅂🅈🅂🅃🄴🄼🅂 **✘**\n\n"
    x +=f'**=============================**\n'
    x += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ `{version.__version__}`\n"

    x += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ `{uptime}`\n"
    x +=f'**=============================**\n\n'
    x += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ **『 [Iɴᴅʀᴀᴊɪᴛʜ](tg://user?id=1633375527) 』** \n\n"
    lol = await event.client.send_file(event.chat_id, file='Dasha/resources/lol.mp4', caption=x)
 except Exception as v:
   await event.respond(str(v))
