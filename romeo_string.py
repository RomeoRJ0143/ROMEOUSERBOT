import os
os.system("pip install telethon")
os.system("pip install pyrogram")
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print("•••   ROMEO SESSION  GENERATOR   •••")
print("\nHello!! Welcome to RomeoBot Session Generator\n")
okvai = input("Enter 69 to continue: ")
if okvai == "69":
    print("Choose the string session type: \n1. RomeoBot \n2. Music Bot")
    library = input("\nYour Choice: ")
    if library == "1":
        print("\nTelethon Session For RomeoBot")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with TelegramClient(StringSession(), APP_ID, API_HASH) as RomeoBot:
            print("\nYour RomeoBot Session Is sent in your Telegram Saved Messages.")
            RomeoBot.send_message("me", f"#RomeoBot #RomeoBot_SESSION \n\n`{RomeoBot.session.save()}`")
    elif library == "2":
        print("Pyrogram Session for Music Bot")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with Client(':memory:', api_id=APP_ID, api_hash=API_HASH) as UltronBot:
            print("\nYour RomeoBot Session Is sent in your Telegram Saved Messages.")
            RomeoBot.send_message("me", f"#RomeoBot_MUSIC #RomeoBot_SESSION\n\n`{RomeoBot.export_session_string()}`")
    else:
        print("Please Enter 1 or 2 only.")
else:
    print("Bhag jaa bhosdike")
