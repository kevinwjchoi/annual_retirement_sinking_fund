import sqlite3

CONN = sqlite3.connect('investment_tracker.db')
CURSOR = CONN.cursor()
