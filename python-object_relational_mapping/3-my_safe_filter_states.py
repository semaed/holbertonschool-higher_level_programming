#!/usr/bin/python3

""" import required"""

import MySQLdb
import sys


def display_states(username, password, database, state_name):
    """
    Display states from the MySQL database based on the given state_name.

    Args:
        username (str): MySQL username for database connection.
        password (str): MySQL password for database connection.
        database (str): Name of the MySQL database to connect to.
        state_name (str): The name of the state to search for in the database.

    Returns:
        None: The function prints the results directly to the console.
    """
    # Establish a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Use a parameterized query to avoid MySQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Script entry point. Takes command-line arguments and calls display_states function.
    """
    # Ensure the script is called with the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get the arguments and call the display_states function
    username, password, database, state_name = sys.argv[1:5]
    display_states(username, password, database, state_name)
