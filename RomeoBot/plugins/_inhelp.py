import asyncio
import html
import os
import re
import random
import sys

from math import ceil
from re import compile

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

from RomeoBot.sql.gvar_sql import gvarstat
from . import *

hell_row = Config.BUTTONS_IN_HELP
hell_emoji = Config.EMOJI_IN_HELP
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Config.LOGGER_ID
USER_BOT_WARN_ZERO = "𝐎𝐲𝐞 𝐛𝐬𝐬𝐬 𝐤𝐚𝐫 𝐛𝐨𝐥𝐚 𝐧 𝐬𝐩𝐚𝐦 𝐧𝐡𝐢 𝐰𝐚𝐫𝐧𝐚 𝐛𝐥𝐨𝐜𝐡 𝐡𝐨𝐠𝐞"

alive_txt = """{}\n
<b><i>🌹 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🌹</b></i>
"""

def button(page, modules):
    Row = hell_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"✮ㅤ" + pair + f"ㅤ✮", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"🔥 𝐁𝐚𝐜𝐤 💥", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"• ❌ •", data="close"
            ),
            custom.Button.inline(
               f"💥 𝐍𝐞𝐱𝐭 🔥", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]


    modules = CMD_HELP
if Config.BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(InlineQuery)
    async def inline_handler(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        builder = event.builder
        result = None
        query = event.text
        auth = await clients_list()
        if event.query.user_id in auth and query == "RomeoBot_help":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            a = gvarstat("HELP_PIC")
            if a:
                help_pic = a.split(" ")[0]
            else:
                help_pic = "https://telegra.ph/file/a62b9c7d9848afde0569e.jpg"
                
                help_msg = f"🌹 **{hell_mention}**\n\n🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}"
                
                #help_msg = f"╔═══💫✨💫═══\n"
                #help_msg = f"┃**{hell_mention}**\n"
                #help_msg = f"╚═══💫✨💫═══\n"
                #help_msg = f"╔══════✣✤༻⋇༺✤✣══════╗\n"
                #help_msg = f"┣🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n"
                #help_msg = f"┣🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n"
                #help_msg = f"┣🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}`\n"
                #help_msg = f"╚══════✣✤༻⋇༺✤✣══════╝\n"""
                
            if help_pic == "DISABLE":
                result = builder.article(
                    f"Hey! Only use {hl}help please",
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic.endswith((".jpg", ".png")):
                result = builder.photo(
                    help_pic,
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic:
                result = builder.document(
                    help_pic,
                    text=help_msg,
                    title="RomeoBot Alive",
                    buttons=veriler[1],
                    link_preview=False,
                )
        elif event.query.user_id in auth and query == "alive":
            uptime = await get_time((time.time() - StartTime))
            alv_msg = gvarstat("ALIVE_MSG") or "»»» <b>𝐑𝐨𝐦𝐞𝐨 𝐨𝐧 𝐝𝐮𝐭𝐲</b> «««"
            he_ll = alive_txt.format(alv_msg, tel_ver, hell_ver, uptime, abuse_m, is_sudo)
            alv_btn = [
                [Button.url(f"{HELL_USER}", f"tg://openmessage?user_id={ForGo10God}")],
                [Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐍𝐋", f"https://t.me/{my_channel}"), 
                Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐏", f"https://t.me/{my_group}")],
            ]
            a = gvarstat("ALIVE_PIC")
            pic_list = []
            if a:
                b = a.split(" ")
                if len(b) >= 1:
                    for c in b:
                        pic_list.append(c)
                PIC = random.choice(pic_list)
            else:
                PIC = "https://telegra.ph/file/a62b9c7d9848afde0569e.jpg"
            if PIC and PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    PIC,
                    text=he_ll,
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )
            elif PIC:
                result = builder.document(
                    PIC,
                    text=he_ll,
                    title="RomeoBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )
            else:
                result = builder.article(
                    text=he_ll,
                    title="RomeoBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )

        elif event.query.user_id in auth and query == "pm_warn":
            CSTM_PMP = gvarstat("CUSTOM_PMPERMIT") or "𝐊𝐲𝐚 𝐤𝐚𝐚𝐦 𝐇"
            HELL_FIRST = "𝐇𝐞𝐥𝐥𝐨 \n   𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 {}'𝐬 𝐩𝐦\n\n 😎 𝐃𝐨𝐧𝐭'𝐧 𝐓𝐫𝐲 𝐓𝐨 𝐒𝐩𝐚𝐦 𝐇𝐞𝐫𝐞 😎".format(hell_mention, CSTM_PMP)
            a = gvarstat("PMPERMIT_PIC")
            pic_list = []
            if a:
                b = a.split(" ")
                if len(b) >= 1:
                    for c in b:
                        pic_list.append(c)
                PIC = random.choice(pic_list)
            else:
                PIC = "https://telegra.ph/file/a62b9c7d9848afde0569e.jpg"
            if PIC and PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    file=PIC,
                    text=HELL_FIRST,
                    buttons=[
                        [custom.Button.inline("📝 𝐑𝐞𝐪𝐮𝐞𝐬𝐭", data="req")],
                        [custom.Button.inline("🚫 𝐁𝐥𝐨𝐜𝐤", data="heheboi")],
                        [custom.Button.inline("❓ 𝐂𝐮𝐫𝐢𝐨𝐮𝐬", data="pmclick")],
                    ],
                    link_preview=False,
                )
            elif PIC:
                result = builder.document(
                    file=PIC,
                    text=HELL_FIRST,
                    title="𝐏𝐦 𝐏𝐞𝐫𝐦𝐢𝐭",
                    buttons=[
                        [custom.Button.inline("📝 𝐑𝐞𝐪𝐮𝐞𝐬𝐭", data="req")],
                        [custom.Button.inline("🚫 𝐁𝐥𝐨𝐜𝐤", data="heheboi")],
                        [custom.Button.inline("❓ 𝐂𝐮𝐫𝐢𝐨𝐮𝐬", data="pmclick")],
                    ],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=HELL_FIRST,
                    title="𝐏𝐦 𝐏𝐞𝐫𝐦𝐢𝐭",
                    buttons=[
                        [custom.Button.inline("📝 𝐑𝐞𝐪𝐮𝐞𝐬𝐭", data="req")],
                        [custom.Button.inline("🚫 𝐁𝐥𝐨𝐜𝐤", data="heheboi")],
                        [custom.Button.inline("❓ 𝐂𝐮𝐫𝐢𝐨𝐮𝐬", data="pmclick")],
                    ],
                    link_preview=False,
                )
                
        elif event.query.user_id in auth and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**🌹 𝐑𝐨𝐦𝐞𝐨𝐁𝐨𝐭 🌹**",
                buttons=[
                    [Button.url("🌹 𝐆𝐑𝐎𝐔𝐏 🌹", "https://t.me/ROMEOBOT_OP")],
                ],
            )

        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )

        else:
            result = builder.article(
                "@Bot_Support_Grp",
                text="""**𝐇𝐞𝐲 𝐓𝐡𝐢𝐬 𝐢𝐬 [𝐑𝐨𝐦𝐞𝐨𝐁𝐨𝐭 𝐆𝐑𝐎𝐔𝐏](https://t.me/ROMEOBOT_OP)**""",
                buttons=[
                    [
                        custom.Button.url("🌹 𝐑𝐨𝐦𝐞𝐨_𝐒𝐭𝐫𝐢𝐧𝐠 🌹", "https://t.me/Rjssgbot"),
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        auth = await clients_list()
        if event.query.user_id in auth:
            reply_pop_up_alert = "𝐓𝐡𝐢𝐬 𝐢𝐬 𝐟𝐨𝐫 𝐨𝐭𝐡𝐞𝐫 𝐮𝐬𝐞𝐫𝐬..."
        else:
            reply_pop_up_alert = "😡𝐃𝐨𝐧'𝐭 𝐬𝐩𝐚𝐦😡"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"req")))
    async def on_pm_click(event):
        auth = await clients_list()
        if event.query.user_id in auth:
            reply_pop_up_alert = "𝐓𝐡𝐢𝐬 𝐢𝐬 𝐟𝐨𝐫 𝐨𝐭𝐡𝐞𝐫 𝐮𝐬𝐞𝐫𝐬"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit("✅ **𝐑𝐞𝐪𝐮𝐞𝐬𝐭** \n\n𝐎𝐲𝐞 𝐑𝐮𝐤𝐨 𝐣𝐚𝐥𝐝𝐢 𝐤𝐲𝐚 𝐡\n😐 𝐒𝐩𝐚𝐦 𝐧𝐡𝐢 𝐛𝐨𝐥𝐚 𝐧 ")
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            await tbot.send_message(LOG_GP, f"𝐡𝐞𝐲 \n\n⚜️ 𝐘𝐨𝐮 𝐠𝐨𝐭 𝐚 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 [{first_name}](tg://user?id={event.query.user_id}) !")


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"heheboi")))
    async def on_pm_click(event):
        auth = await clients_list()
        if event.query.user_id in auth:
            reply_pop_up_alert = "𝐓𝐡𝐢𝐬 𝐢𝐬 𝐟𝐨𝐫 𝐨𝐭𝐡𝐞𝐫 𝐮𝐬𝐞𝐫𝐬"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(f"😡 **𝐁𝐥𝐨𝐜𝐤**")
            await H1(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            await tbot.send_message(LOG_GP, f"𝐇𝐨 𝐠𝐲𝐚 𝐧 𝐁𝐥𝐨𝐜𝐤 𝐛𝐨𝐥𝐚 𝐭𝐡𝐚 𝐬𝐩𝐚𝐦 𝐦𝐚𝐚𝐭 𝐤𝐚𝐫\n\n**𝐁𝐥𝐨𝐜𝐤** [{first_name}](tg://user?id={event.query.user_id}) \nℝ𝕖𝕒𝕤𝕠𝕟:- ℙ𝕄 𝕊𝕖𝕝𝕗 𝔹𝕝𝕠𝕔𝕜")


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        if event.query.user_id in auth:
            current_page_number=0
            simp = button(current_page_number, CMD_HELP)
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            await event.edit(
                         f"🌹**{hell_mention}**\n\n🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}",
                
                           #f"╔═══💫✨💫═══\n"
                           #f"┃**{hell_mention}**\n"
                           #f"╚═══💫✨💫═══\n"
                           #f"╔══════✣✤༻⋇༺✤✣══════╗\n"
                           #f"┣🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n"
                           #f"┣🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n"
                           #f"┣🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}`\n"
                           #f"╚══════✣✤༻⋇༺✤✣══════╝\n","""
                           
                buttons=simp[1],
                link_preview=False,
            )
        else:
            reply_pop_up_alert = "𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        if event.query.user_id in auth:
            veriler = custom.Button.inline(f"{hell_emoji} Re-Open Menu {hell_emoji}", data="reopen")
            await event.edit(f"**🌹 𝐁𝐨𝐭 𝐦𝐞𝐧𝐮 𝐏𝐫𝐨𝐯𝐢𝐝𝐞𝐫 𝐧𝐨𝐰 𝐜𝐥𝐨𝐬𝐞𝐝 🌹**\n\n**𝐑𝐎𝐌𝐄𝐎𝐁𝐎𝐓**  {hell_mention}\n\n        [©️𝕽𝖔𝖒𝖊𝖔𝕭𝖔𝖙 ™️]({chnl_link})", buttons=veriler, link_preview=False)   
                                #f"╔═══💫✨💫═══\n"
                                #f"┃**🌹 𝐁𝐨𝐭 𝐦𝐞𝐧𝐮 𝐏𝐫𝐨𝐯𝐢𝐝𝐞𝐫 𝐧𝐨𝐰 𝐜𝐥𝐨𝐬𝐞𝐝 🌹**\n"
                                #f"┃**𝕽𝖔𝖒𝖊𝖔𝕭𝖔𝖙 :**  {hell_mention}\n"  
                                #f"╚═══💫✨💫═══\n"
                                #[©️ ԱӀէɾօղβօէ ™️]({chnl_link})", buttons=veriler, link_preview=False)"
        else:
            reply_pop_up_alert = "𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
   

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id in auth:
            await event.edit(
                           f"🌹 **{hell_mention}**\n\n🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}",
                           #f"╔═══💫✨💫═══\n"
                           #f"┃**{hell_mention}**\n"
                           #f"╚═══💫✨💫═══\n"
                           #f"╔══════✣✤༻⋇༺✤✣══════╗\n"
                           #f"┣🌹𝐏𝐥𝐮𝐠𝐢𝐧𝐬: `{len(CMD_HELP)}` \n"
                           #f"┣🌹𝐂𝐦𝐝𝐬: `{len(apn)}`\n"
                           #f"┣🌹𝐏𝐚𝐠𝐞: 1/{veriler[0]}`\n"
                           #f"╚══════✣✤༻⋇༺✤✣══════╝\n","""
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer("𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞", cache_time=0, alert=True)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)")))
    async def Information(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline("✮ㅤ" + cmd[0] + "ㅤ✮", data=f"commands[{commands}[{page}]]({cmd[0]})")
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer("No Description is written for this plugin", cache_time=0, alert=True)

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline(f"🌹 𝐌𝐚𝐢𝐧 𝐌𝐞𝐧𝐮 🌹", data=f"page({page})")])
        if event.query.user_id in auth:
            await event.edit(
                f"**📗 File :**  `{commands}`\n**🔢 Number of commands :**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer("𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞", cache_time=0, alert=True)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)")))
    async def commands(event):
        cids = await client_id(event, event.query.user_id)
        ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**📗 File :**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ Info :**  {CMD_HELP_BOT[cmd]['info']['info']}\n"
        sextraa = CMD_HELP_BOT[cmd]["extra"]
        if sextraa:
            a = sorted(sextraa.keys())
            for b in a:
                c = b
                d = sextraa[c]["content"]
                result += f"**{c} :**  `{d}`\n"
        result += "\n"
        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 Commands :**  `{HANDLER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 Commands :**  `{HANDLER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**💬 Explanation :**  `{command['usage']}`\n\n"
        else:
            result += f"**💬 Explanation :**  `{command['usage']}`\n"
            result += f"**⌨️ For Example :**  `{HANDLER[:1]}{command['example']}`\n\n"
        if event.query.user_id in auth:
            await event.edit(
                result,
                buttons=[custom.Button.inline(f"🌹 𝐑𝐞𝐭𝐮𝐫𝐧 🌹", data=f"Information[{page}]({cmd})")],
                link_preview=False,
            )
        else:
            return await event.answer("𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐬𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞", cache_time=0, alert=True)


# RomeoBot
