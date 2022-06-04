import requests
import logging
import json

url = "https://api.lolpros.gg"


def getPlayer(name):

    try:
        r = requests.get(f"{url}/es/players/{name}")

        return r.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"Lolpros api failed: getPlayer: {name}")
        return None

def findPlayers(name):

    try:
        r = requests.get(f"{url}/es/search?query={name}&active=true")
        
        if len(r.json()) > 1:
            logging.warning(f"Lolpros api issue: findPlayers: Found more then 1 player for: {name} ")

        return r.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"Lolpros api failed: findPlayers: {name}")
        return None