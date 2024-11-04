#!/usr/bin/python3
"""
Making a script in pyton that takes a table
from a SQL server and finds the ones that
matches with the given argument
"""


import MySQLdb
import sys


def main():
    """
    This function will search in a table
    for a value that matches with a given argument
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         password=password, db=database)
    sql_query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDERED BY id"
        .format(name)
    )
    cursor = db.cursor()
    cursor.execute(sql_query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__name__":
    main()
