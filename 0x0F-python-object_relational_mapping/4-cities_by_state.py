#!/usr/bin/python3
"""lists cities from the database hbtn_0e_0_usa based on the state name argument and also to be able to deal with SQL injection"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    args = sys.argv

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], db=args[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.id,cities.name,states.name FROM cities\
        INNER JOIN states ON tates.id = cities.state_id ORDER BY\
            cities.id ASC;""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
