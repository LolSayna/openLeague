# takes command from anywhere and returns
# cmd syntax:
# [scout, NAMES OPTIONS]

import logging
from lolpros import getPlayer, findPlayers
from riotAPI import findMainChampsChallenger

def parse_Cmd(cmd):

    if cmd[1] == "scout":

        names, elo = scoutPlayer(name=cmd[2])

        return f"Found: {names}\nElo: {elo}"
    
    if cmd[1] == "op":
        
        l = convertOpgg(opgg=cmd[2])
        return l

    if cmd[1] == "top":

        l = findMainChampsChallenger(playercount=int(cmd[2]), gamecount=int(cmd[3]))
        return l

    else:
        return "command not found."

def scoutPlayer(name):
    d = getPlayer(name)
    if d is None:
        return None, None
    names, elo = [], []
    for account in d["league_player"]["accounts"]:
        names.append(account["summoner_name"])
        elo.append(account["rank"]["league_points"])
    
    return names, elo


def convertOpgg(opgg):

    l = "Scouting Result:\n"
    op = opgg.split("summoners=")[1]
    
    if ",%20" in op:
        u = op.split(",%20")
    elif "," in op:
        u = op.split(",")
    else:
        u = op.split("%2C")

    for player in u:

        r = findPlayers(player)
        if r:
            playerName = r[0]["slug"]
            accName, elo = scoutPlayer(playerName)

            l += "**" + str(playerName) + "** " +str(accName)+str(elo)+"\n"
        else:
            l += "**" + str(player) + "** no account on lolpros\n"

    # removing the finale newline
    return l[:-1]