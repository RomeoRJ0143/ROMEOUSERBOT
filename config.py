# FILL THESE VALUES ACCORDINGLY.

from RomeoBot.config.hell_config import Config

class Development(Config):
  # get these values from my.telegram.org. 
  APP_ID = 9    # 9 is a placeholder. Fill your 6 digit api id
  API_HASH = "9"   # replace this with your api hash

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "9"
  ALIVE_NAME = "Romeo"
  # After cloning the repo and installing requirements...
  # Do `python string.py` and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  ROMEOBOT_SESSION = "9"

  # Create a bot in @BotFather
  # And fill the following values with bot token and username.
  BOT_TOKEN = "9" #token
  #FILL BOT USERNAME WITHOUT @
  BOT_USERNAME = "9"
  # Custom Command Handler. 
  HANDLER = "."
 

  # Custom Command Handler for sudo users.
  SUDO_HANDLER = "."
  # if u want to add sudo then remove #
  #SUDO_USERS = []


# end of required config
# bot
