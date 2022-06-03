import sqlite3
from keys import *

con = sqlite3.connect(database)

c = con.cursor()


c.execute("""CREATE TABLE tournament (
        gameA TEXT,
        redside TEXT,
        bluwin NULL
    )""")

#c.execute("INSERT INTO tournament")


def insertTabele():
    pass

def insertElement(table, elemnt):
    pass

def extractElement(which):
    pass



con.commit()
con.close()
