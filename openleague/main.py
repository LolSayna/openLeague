import logging
from cred import discord_bot_token
from discordBot import runBot

# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting container")

# starting the discord bot
#runBot(token=discord_bot_token)


runBot(token=discord_bot_token)