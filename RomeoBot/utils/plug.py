import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator, InputMessagesFilterDocument

from RomeoBot import *
from RomeoBot.clients import *
from RomeoBot.helpers import *
from RomeoBot.config import *
from RomeoBot.utils import *


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from RomeoBot.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import RomeoBot.utils

        path = Path(f"RomeoBot/plugins/{shortname}.py")
        name = "RomeoBot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("RomeoBot - Successfully imported " + shortname)
    else:
        import RomeoBot.utils

        path = Path(f"RomeoBot/plugins/{shortname}.py")
        name = "RomeoBot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Hell
        mod.H1 = Hell
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.Hell = Hell
        mod.RomeoBot = RomeoBot
        mod.tbot = RomeoBot
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = RomeoBot.utils
        mod.Config = Config
        mod.borg = bot
        mod.RomeoBot = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_hell = delete_hell
        mod.eod = delete_hell
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.hell_cmd = hell_cmd
        mod.sudo_cmd = sudo_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = RomeoBot.utils
        sys.modules["userbot"] = RomeoBot
        # support for paperplaneextended
        sys.modules["userbot.events"] = RomeoBot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["RomeoBot.plugins." + shortname] = mod
        LOGS.info("🇷𝐎𝐌𝐄𝐎... - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"RomeoBot.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel:
        LOGS.info("🇷𝐎𝐌𝐄𝐎... - PLUGIN CHANNEL DETECTED.")
        LOGS.info("🇷𝐎𝐌𝐄𝐎... - Starting to load extra plugins.")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"RomeoBot/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "RomeoBot/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))


# RomeoBot
