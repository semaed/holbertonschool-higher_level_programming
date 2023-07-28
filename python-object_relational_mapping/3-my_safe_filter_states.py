#!/usr/bin/python3
"""
Get matching states from the states table in the database.
Safe from MySQL injections.

Parameters:
    1. MySQL username
    2. MySQL password
    3. Database name
    4. State name to match

Usage:
    ./script.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys


def get_matching_states(username, password, database, state_name):
    """
    Fetch and display matching states from the states table.
    """
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor to execute queries using SQL; match the state name given
    cursor = db.cursor()
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name=%s ORDER BY id ASC"""
    cursor.execute(sql_cmd, (state_name,))

    # Fetch and print the matching rows
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username, password, database, state_name = sys.argv[1:]

    get_matching_states(username, password, database, state_name)
