#soon
from telethon import events
from Dasha import hbot

@hbot.on(events.NewMessage(pattern="[/]start"))
async def fuck(event):
 if event.is_private:
  try:
     await hbot.send_message(event.chat_id, '/hunt for pokemon') 
  except Exception as e:
     await event.reply("**Error:**\n`{e}`") 
