from Dasha import ubot, tbot
from Dasha.events import dasha
from . import get_user

@dasha(pattern="^/kick ?(.*)")
async def kick(event):
 if event.is_private:
   return await event.edit("Please use this in groups.")
 try:
  user, extra = await get_user(event)
 except TypeError:
  pass
 if not user:
  await event.edit("Failed to fetch user.")
 if not event.chat.admin_rights.ban_users:
   return await event.edit("Failed to Kick, No CanBanUsers Right.")
 try:
  await ubot.kick_participant(event.chat_id, user.id)
  await event.edit(f"Kicked **[{user.first_name}](tg://user?id={user.id})** from [{event.chat.title}](http://t.me/{event.chat.username})!")
 except:
  await event.edit("Can't kick admins.")

@dasha(pattern="^/pin$")
async def pin(event):
     fuck = await event.edit('`Processing...`')
     lol = await event.get_reply_message()
     await event.client.pin_message(event.chat_id, lol, notify=True)
     await fuck.edit(f'**Sᴜᴄᴄᴇssғᴜʟʟʏ Pɪɴɴᴇᴅ [Tʜɪs](http://t.me/c/{lol.chat.id}/{lol.id}) ᴍᴇssᴀɢᴇ**')
  
@dasha(pattern='^/kickme')
async def lmao(event):
        await event.edit(f'My Master is leaving from **{event.chat.title}**')
        await event.client.kick_participant(event.chat_id, 'me')
        
@dasha(pattern='^/del')    
async def bruh(event):
        x = await event.get_reply_message()
        await x.delete()
        await event.delete()
        
@dasha(pattern="^/ban  ?(.*)")
async def ban(event):
 if event.is_private:
   return await event.edit("Please use this in groups.")
 try:
  user, extra = await get_user(event)
 except TypeError:
  pass
 if not user:
  await event.edit("Failed to fetch user.")
 if not event.chat.admin_rights.ban_users:
   return await event.edit("Dont have enough ryts")
 try:
  await ubot.edit_permissions(event.chat_id, user.id, view_messages=False)
  await event.edit(f"Banned **[{user.first_name}](tg://user?id={user.id})** from [{event.chat.title}](http://t.me/{event.chat.username})!")
 except:
  await event.edit("Can't ban admins.")
  
  
@dasha(pattern="^/dban ?(.*)")
async def dban(event):
 if event.is_private:
   return await event.edit("Please use this in groups.")
 try:
  user, extra = await get_user(event)
 except TypeError:
  pass
 if not user:
  await event.edit("Failed to fetch user.")
 if not event.chat.admin_rights.ban_users:
   return await event.edit("Failed to Kick, No CanBanUsers Right.")
 try:
  lol=await event.get_reply_message()
  await ubot.edit_permissions(event.chat_id, lol.sender.id, view_messages=False)
  await lol.delete()
  await event.edit(f"banned **[{user.first_name}](tg://user?id={user.id})** from [{event.chat.title}](http://t.me/{event.chat.username})!")
 except:
  await event.edit("Can't ban admins.")