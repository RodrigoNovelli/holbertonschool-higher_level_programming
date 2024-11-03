#!/usr/bin/python3
"""
Making a script in pyhton that gets values from
a table and filters the results
"""


import MySQLdb
import sys


def main():
    """
    Main function to searh and return all the
    tates with the letter N
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port='3306',
                         user=username, password=password, db=database)
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id"
        )
    states = cursor.fetchall()
    for state in states:
        print(state)
        cursor.close
        db.close()


if __name__ == "__main__":
    main()
