import sqlite3
from cred import *
import logging

def createTable():
    command = f"CREATE TABLE IF NOT EXISTS games (matchID TEXT, dataset TEXT)"

    c.execute(command)

def insert(matchid, dataset):
 
    #if not extract(matchid):

    command = f"""INSERT INTO games VALUES ("{matchid}", "{dataset}")"""

    c.execute(command)
    #else:
    #    logging.warning("trying to add existing value")

def extract(matchid):
    command = f"""SELECT * FROM games WHERE matchID LIKE "{matchid}" """

    c.execute(command)
    print(len(c.fetchall()))
    print(c.fetchall())
    if len(c.fetchall()) > 0:
        return c.fetchall()[0][1]
    else:
       return []

def printALL():

    c.execute("SELECT * FROM games")
    return c.fetchall()

def endDatabase():

    logging.debug("ended database")
    c.execute("DROP TABLE games")
    con.commit()
    con.close()


# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting container")

con = sqlite3.connect(database)
c = con.cursor()
logging.debug("started database")
createTable()
    

insert("sadf", "dgd")
#insert("sadf", "dgdeee")

print(extract("sadf"))
print(extract("dfgdf"))

print(printALL())
#endDatabase()

