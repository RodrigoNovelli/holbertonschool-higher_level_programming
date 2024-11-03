#!/usr/bin/python3
'''
Making a script that shows all the states in a database.
'''


import MySQLdb
from sys import argv

params = {
    'host': 'localhost',
    'port': 3306,
    'user': argv[1],
    'passwd': argv[2],
    'db': argv[3],
}

if __name__ == "__main__":
    db = MySQLdb.connect(**params)
    num_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(num_rows):
        print(cur.fetchone())
