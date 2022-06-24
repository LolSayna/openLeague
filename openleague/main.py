import logging
from cred import discord_bot_token
from discordBot import runBot
from interpreter import convertOpgg
from riotAPI import findMainChampsChallenger
from sqlTest import *


# logging in sqlTest


#opgg = "https://euw.op.gg/multisearch/euw?summoners=brokenblade19,G2%20BOOMER,Ca%C3%9Es,Enter%20The%20East1,Targamas"
#convertOpgg(opgg)


res = findMainChampsChallenger(playercount=2, gamecount=3)
print(res)




# runBot(token=discord_bot_token)

print(printALL())
endDatabase()