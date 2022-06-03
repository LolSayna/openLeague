import requests
import logging
from discordBot import runBot
from cred import discord_bot_token

# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting container")

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
if r.status_code != 200:
    logging.debug("Requests check failed")


runBot(token=discord_bot_token)