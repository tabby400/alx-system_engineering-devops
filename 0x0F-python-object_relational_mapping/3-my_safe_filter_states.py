#!/usr/bin/python3


""" this module shows the values in the states table where the name matches
the arguuement safely
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()
    mycursor.execute("""SELECT * FROM states""")
    [print(state) for state in mycursor.fetchall() if state[1] == sys.argv[4]]
