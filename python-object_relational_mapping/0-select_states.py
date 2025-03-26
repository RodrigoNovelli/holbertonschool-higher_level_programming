'''
In this module we are making a script that
gets information from a database
'''
import MySQLdb


def list_states(username, password, database):
    '''
    Function that lists allthe
    states from the database
    '''
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database
    )

    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
