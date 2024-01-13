#!/usr/bin/python3
"""
5-filter_cities module
"""
import MySQLdb
import sys

"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database
"""

if __name__ == "__main__":
    argv = sys.argv[1:]
    username = argv[0]
    password = argv[1]
    db_name = argv[2]
    state_name = argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
            )
    cur = db.cursor()

    query = """
    SELECT cities.name
    FROM cities, states
    WHERE cities.state_id LIKE BINARY states.id
    AND states.name LIKE BINARY %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name, ))
    rows = cur.fetchall()
    for index, row in enumerate(rows):
        if index > 0:
            print(", ", end="")
        print(row[0], end="")
    print()

    cur.close()
    db.close()
