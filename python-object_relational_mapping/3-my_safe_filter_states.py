#!/usr/bin/python3
"""
Return matching states; safe from MySQL injections

Parameters given to script: username, password, database, state to match
"""

import MySQLdb
from sys import argv


def get_matching_states(username, password, database, state_to_match):
    """
    Get matching states from the states table in the database.
    """
    # Connect to the database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create cursor to execute queries using SQL; match arg given
    cursor = db.cursor()
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name=%s ORDER BY id ASC"""
    cursor.execute(sql_cmd, (state_to_match,))

    # Fetch and print the matching rows
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
    else:
        get_matching_states(argv[1], argv[2], argv[3], argv[4])
