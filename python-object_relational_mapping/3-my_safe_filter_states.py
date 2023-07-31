#!/usr/bin/python3
'''
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, password=passwd, db=db)

    cur = db.cursor()
    protected = (state_name,)
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", protected)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
