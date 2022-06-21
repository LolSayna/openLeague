import logging
from cred import discord_bot_token
from discordBot import runBot
from interpreter import convertOpgg
from riotAPI import findMainChampsChallenger



# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting container")

# starting the discord bot
#runBot(token=discord_bot_token)


#runBot(token=discord_bot_token)

opgg = "https://euw.op.gg/multisearch/euw?summoners=brokenblade19,G2%20BOOMER,Ca%C3%9Es,Enter%20The%20East1,Targamas"
#convertOpgg(opgg)

res = findMainChampsChallenger(10, 25)
#runBot(token=discord_bot_token)

print(res)