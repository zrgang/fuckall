import os
import sys
import random
from Config import TOKEN, SUDO, API_ID, API_HASH
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest


Riz = TelegramClient('Riz', APP_ID, API_HASH).start(bot_token=TOKEN) 

que = {}

SMEX_USERS = []
for x in SUDO: 
    SMEX_USERS.append(x)


@Riz.on(events.NewMessage(incoming=True, pattern=r"\*sbl"))
async def testing(event):
    if e.sender_id in SMEX_USERS:
  try:
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("𝗬𝗢𝗨 𝗗𝗜𝗗'𝗡𝗧 𝗛𝗔𝗩𝗘 𝗦𝗨𝗙𝗙𝗜𝗖𝗜𝗘𝗡𝗧 𝗥𝗜𝗚𝗛𝗧𝗦")
        return
    await event.edit("Carlo Ki Biwi Nache Nangi")
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("CARLO BHOSDIKA")
    


@Riz.on(events.NewMessage(incoming=True, pattern=r"\*leave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

print("\n\n")
print("🤣😂🔥 OP BOT DEPLOYED")
if len(sys.argv) not in (1, 3, 4):
    try:
        Riz.disconnect()
    except Exception as e:
        pass
