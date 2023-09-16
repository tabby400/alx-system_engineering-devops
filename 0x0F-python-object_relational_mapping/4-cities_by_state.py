#!/usr/bin/python3


"""
this module lists all citiess in hbtn_0e_4_usa
database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mycursor = db.cursor()
    mycursor.execute("""SELECT cities.id, cities.name, states.name
                        FROM cities
                        JOIN states
                        ON cities.state_id = states.id
                        ORDER BY cities.id ASC""")  # cities to their states
    [print(city) for city in mycursor.fetchall()]
