import requests
import logging
import json

url = "https://api.lolpros.gg"


def getPlayer(name):

    try:
        r = requests.get(f"{url}/es/players/{name}")

        return r.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"Lolpros api request failed")
        return None

def parsePlayer(dict):
    if dict is None:
        return None, None
    names, elo = [], []
    for account in dict["league_player"]["accounts"]:
        names.append(account["summoner_name"])
        elo.append(account["rank"]["league_points"])
    
    return names, elo


def parsing(name):

    return parsePlayer(getPlayer(name))