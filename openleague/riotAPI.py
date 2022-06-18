# all with Riot api

import requests
import logging
import json
from time import time,sleep
from collections import Counter

from cred import riot_key

# generell requests
def requestsAPI(url):
    #print(f"Querrying API {url}")

    r = requests.get(url)

    if r.status_code == 403:
        logging.error("Refresh API key, returned none.")
        return None
    elif r.status_code == 429:
        logging.error("Hit API limit, returned none.")
        return None

    data = r.json()

    # to care for API limit
    sleep(1.2)
    return data

# 2 API calls
def listChallengerPlayers():

    summonerNameList = []

    d = requestsAPI(f"https://euw1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1&api_key={riot_key}")
    e = requestsAPI(f"https://euw1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=2&api_key={riot_key}")

    for player in d:
        summonerNameList.append(player["summonerName"])
    for player in e:
        summonerNameList.append(player["summonerName"])

    if len(summonerNameList) != 300:
        logging.error("Did not find 300 players.")
        return None

    # limit for testing to 5
    return summonerNameList

# 2 API calls per Name
def findGames(summonerNameList):

    gameList = {}
    for accName in summonerNameList:

        # find puuid
        d = requestsAPI(f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{accName}?api_key={riot_key}")
        puuid = d["puuid"]

        # get list of games
        # here possible to add more games by adding more pages
        d = requestsAPI(f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&start=0&count=100&api_key={riot_key}")

        gameList[accName] = d

    return gameList

# 1 API call, finds the champ which summonerName played
def findChamp(matchID, summonerName):
    d = requestsAPI(f"https://europe.api.riotgames.com/lol/match/v5/matches/{matchID}?api_key={riot_key}")

    for player in d["info"]["participants"]:
        if summonerName == player["summonerName"]:
            return player["championName"]
    
    logging.error("FindChamp failed, player was not in the game")
    return None

# Finds the mostplayed champs by each player in challenger.
# It checks "gamecount" number of games for "playercount" number of players.
# Because of the API limit takes it: 1.2s * (2 + 2*playercount + playercount*gamecount)
def findMainChampsChallenger(playercount, gamecount):

    print(f"Requests time in seconds: {1.2*(2 + 2*playercount + playercount*gamecount)}")
    print(f"Each player after ")

    summonerNameList = listChallengerPlayers()[0:playercount]
    gameList = findGames(summonerNameList)

    for summonerName, games in gameList.items():
        chamPool = []
        for match in games[0:gamecount]:
           chamPool.append(findChamp(match, summonerName))

        print(f"{summonerName} played {Counter(chamPool).most_common()}")
 

findMainChampsChallenger(3, 5)