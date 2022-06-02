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


con.commit()
con.close()
