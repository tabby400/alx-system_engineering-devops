#!/usr/bin/python3

""" module that lists all the states from
database hbtn_0e_0_usa"""

import MySQLdb
import sys  # works with command line args

if __name__ == '__main__':

    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], database=sys.argv[3])

    mycursor = db.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"  # ascending

    cursor.execute(query)  # executed directly

    states = cursor.fetchall()  # all rows displayed

    for state in states:
        print(state)
    mycursor.close()

    db.close()
