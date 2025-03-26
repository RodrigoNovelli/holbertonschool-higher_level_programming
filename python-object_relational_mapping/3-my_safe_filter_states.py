'''
This module is for making a script that
is the same as the last one but safe
from MySQL injections
'''


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=[2], db=argv[3])
    cur = db.cursor()
    exe = "SELECT * FROM states WHERE name=%s ORDER BY states.id"
    rows = cur.execute(exe, (argv[4], ))
    for row in rows:
        print(cur.fetchone())
