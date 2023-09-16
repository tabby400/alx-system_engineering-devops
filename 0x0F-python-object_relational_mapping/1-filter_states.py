#!/usr/bin/python3


""" this module only filters states which begin
with capital N"""

from sys import argv
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], database=argv[3])
    mycursor = db.cursor()

    mycursor.execute(
            "SELECT * FROM states WHERE name like BINARY 'N%' ORDER BY id ASC")

    states = mycursor.fetchall()  # all rows

    for state in states:
        print(state)
    mycursor.close()
    db.close()
