#!/usr/bin/python3
"""
Making a script that shows all the states in a database.
"""
import MySQLdb
from sys import argv


def main():
    """
    This script connects to a MySQL database and
    returns all the elements from states table
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
