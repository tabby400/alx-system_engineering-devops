#!/usr/bin/python3


"""this module is whereby the name matches the
arguement"""

from sys import argv
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], database=argv[3])
    mycursor = db.cursor()  # method by  MySQLdb library
    mycursor.execute(
            "SELECT * FROM states WHERE name like BINARY"
            "'{:s}' ORDER BY id ASC".format(argv[4]))
    states = mycursor.fetchall()  # all rows
    for state in states:
        print(state)

    mycursor.close()
    db.close()
