# takes command from anywhere and returns
# cmd syntax:
# [scout, NAMES OPTIONS]

from lolpros import getPlayer

def parse_Cmd(cmd):

    if cmd[1] == "scout":

        names, elo = scoutPlayer(name=cmd[2])

        return f"Found: {names}\nElo: {elo}"



def scoutPlayer(name):
    d = getPlayer(name)
    if d is None:
        return None, None
    names, elo = [], []
    for account in d["league_player"]["accounts"]:
        names.append(account["summoner_name"])
        elo.append(account["rank"]["league_points"])
    
    return names, elo
