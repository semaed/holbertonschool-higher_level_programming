#!/usr/bin/python3

import MySQLdb
import sys


def filter_states():
    """
    Connects to the MySQL server and lists all states with names starting with 'N'.

    Arguments:
        None (takes arguments from the command line)

    Returns:
        None
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".
              format(sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        """" Connect to the MySQL server """
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database_name)

        """ Create a cursor object to execute queries """
        cursor = db.cursor()

        """ Execute the SELECT query """
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        """ Fetch all the rows """
        rows = cursor.fetchall()

        """ Display the results """
        for row in rows:
            print(row)

        """ Close the cursor and connection """
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))


if __name__ == "__main__":
    filter_states()
