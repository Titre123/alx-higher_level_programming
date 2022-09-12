#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""


if __name__ == '__main__':
    import MySQLdb
    import sys
    args = sys.argv

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], db=args[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM"
                " cities JOIN states ON cities.state_id = states.id")
    for row in rows:
        print(row)
    cur.close()
    db.close()
