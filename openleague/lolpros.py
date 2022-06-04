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

