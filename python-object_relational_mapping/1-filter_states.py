'''
In this module we are making a script
that lists all states that starts with N
'''
import MySQLdb
from sys import argv


if __name__ == "__name__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for row in rows:
        if row[1][0] == 'N':
            print(cur.fetchall())
    cur.close()
    db.close()
