# all with Riot api

import requests
import logging
import json
from time import time,sleep
from collections import Counter

from sqlTest import extract,insert

from cred import riot_key

# generell requests
def requestsAPI(url, retries=0):
    #print(f"Querrying API {url}")

    try:
        r = requests.get(url)

        if r.status_code == 403:
            logging.error("Refresh API key, returned none.")
            quit()
        elif r.status_code == 429:
            logging.error("Hit API limit, returned none.")
            return None

        elif r.status_code == 500 or r.status_code == 503:
            if retries > 3:
                logging.error("Service unavailable, already tried 3 times.")
                quit()
            logging.error(f"Service unavailable, retry in 5s.{retries}")
            sleep(5)
            return requestsAPI(url, retries+1)

        data = r.json()
    except Exception as e:
        print(f"FATAL ERROR with API. Retires: {retries}\n\n\nErrorMessage: {e}\n\n\nurl: {url}")
        if retries > 3:
            logging.error("Error 3 times, quitting.")
            quit()
        sleep(10)
        return requestsAPI(url, retries+1)


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

# 2 API calls
def findGames(summonerName):

    # find puuid
    d = requestsAPI(f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={riot_key}")
    puuid = d["puuid"]

    # get list of games
    # here possible to add more games by adding more pages
    games = requestsAPI(f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&start=0&count=100&api_key={riot_key}")

    return games, puuid

# 1 API call, finds the champ which summonerName played
def findChamp(matchID, puuid):

    if extract("games", matchID):
        logging.info("Found in Table")
        d = extract("games", matchID)[0][1]
    else:
        d = requestsAPI(f"https://europe.api.riotgames.com/lol/match/v5/matches/{matchID}?api_key={riot_key}")
        insert("games", matchID, d)


    try:
        d["info"]
    except KeyError as e:
        logging.error(f"Keyerror: {e}\n d:{d}")
        quit()

    for player in d["info"]["participants"]:
        if puuid == player["puuid"]:
            return player["championName"], d
    
    logging.error(f"FindChamp failed, player was not in the game.\nd: {d}\nmatchId: {matchID}\npuuid: {puuid}")
    return None

# Finds the mostplayed champs by each player in challenger.
# It checks "gamecount" number of games for "playercount" number of players.
# Because of the API limit takes it: 1.2s * (2 + 2*playercount + playercount*gamecount)
def findMainChampsChallenger(playercount, gamecount):

    toplist = ""
    identifyer = 0

    starttime = time()
    delayTime = 1.2*(2 + 2*playercount + playercount*gamecount)
    #firstPlayerDelay = 1.2*(2 + 2 + gamecount)
    logging.info(f"Lower Boundary for time: {delayTime:.1f}")
    #print(f"Lower Boundary for first player: {firstPlayerDelay:.1f}\n")

    summonerNameList = listChallengerPlayers()[0:playercount]

    know_matches = {}
    for summonerName in summonerNameList:

        gamesList, puuid = findGames(summonerName)

        chamPool = []
        for match in gamesList[0:gamecount]:
            if match in know_matches:
                logging.info("used caching")
                d = know_matches[match]
                
                for player in d["info"]["participants"]:
                    if puuid == player["puuid"]:
                        chamPool.append(player["championName"])
            else:    
                res, answer = findChamp(match, puuid)
                know_matches[match] = answer
                chamPool.append(res)


        identifyer += 1
        champsSummed = Counter(chamPool).most_common()
        toplist += f"{identifyer}\t{summonerName}\t{len(gamesList[0:gamecount])}"

        if len(champsSummed) == 1:

            toplist += f"\t{champsSummed[0][0]}\t{champsSummed[0][1]}\n" 
            
        if len(champsSummed) == 2:

            toplist += f"\t{champsSummed[0][0]}\t{champsSummed[0][1]}\t{champsSummed[1][0]}\t{champsSummed[1][1]}\n" 
        
        if len(champsSummed) > 2:

            toplist += f"\t{champsSummed[0][0]}\t{champsSummed[0][1]}\t{champsSummed[1][0]}\t{champsSummed[1][1]}\t{champsSummed[2][0]}\t{champsSummed[2][1]}\n" 

    logging.info(f"\nTotal time was: {time()-starttime:.2f}, so calculation time was: {(time()-starttime) - delayTime:.2f}")

    return toplist[:-1]

