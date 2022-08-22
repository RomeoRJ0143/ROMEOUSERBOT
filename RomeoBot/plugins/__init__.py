import datetime
import time

from RomeoBot import *
from RomeoBot.clients import *
from RomeoBot.config import Config
from RomeoBot.helpers import *
from RomeoBot.utils import *
from RomeoBot.random_strings import *
from RomeoBot.version import __hell__
from RomeoBot.sql.gvar_sql import gvarstat
from telethon import version

hell_logo = "./RomeoBot/resources/pics/hellbot_logo.jpg"
cjb = "./RomeoBot/resources/pics/cjb.jpg"
restlo = "./RomeoBot/resources/pics/rest.jpeg"
shuru = "./RomeoBot/resources/pics/shuru.jpg"
shhh = "./RomeoBot/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hell_ver = __hell__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

is_sudo = "True" if gvarstat("SUDO_USERS") else "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "@Bot_Updates_Chnl"
my_group = Config.MY_GROUP or "@Bot_Support_Grp"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/Bot_Updates_Chnl"
hell_channel = f"[✨𝕽𝖔𝖒𝖊𝖔𝕭𝖔𝖙✨]({chnl_link})"
grp_link = "https://t.me/Bot_Support_Grp"
hell_grp = f"[✨𝕽𝖔𝖒𝖊𝖔𝕭𝖔𝖙✨]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# RomeoBot
