"""
Create and read/write to Sqlite database
https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
http://www.sqlitetutorial.net/sqlite-python/create-tables/
https://www.pythoncentral.io/advanced-sqlite-usage-in-python/
"""

import datetime
import sqlite3
from sqlite3 import Error

class Lane_DB():
    def __init__(self):
        """ Initialize the lane database """
        self.DB = sqlite3.connect('lane_closures.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

        self.cursor = self.DB.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS lanes(
                            id INTEGER PRIMARY KEY,
                            closure_id INTEGER,
                            primary_street TEXT,
                            date_closed_from TIMESTAMP,
                            date_closed_to TIMESTAMP,
                            boundaries TEXT,
                            traffic_effect TEXT,
                            published INTEGER
                            )''')

    def write(self, lane_data):
        """ lane_data (array):
            [0] closure_id
            [1] primary_street
            [2] date_closed_from
            [3] date_closed_to
            [4] boundaries
            [5] traffic_effect
            [6] published (0/1)"""

        if len(lane_data) == 6:
            try:
                self.cursor.execute('INSERT INTO lanes(closure_id, primary_street, date_closed_from, date_closed_to, boundaries, traffic_effect, published) VALUES (?)', lane_data)
            except sqlite3.Error as error:
                print(error)
            finally:
                self.DB.commit()