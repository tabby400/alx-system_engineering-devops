#!/usr/bin/python3

"""
module uses name of state as arguemnt and lists
all the cities in the hbtn_0e_4_usa database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()
    mycursor.execute("""SELECT * FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    ORDER BY cities.id""")
    print(", ".join([city[2]
                     for city in mycursor.fetchall()
                     if city[4] == sys.argv[4]]))  # filter city based on state
