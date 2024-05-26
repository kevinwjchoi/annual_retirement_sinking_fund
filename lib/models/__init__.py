import sqlite3

CONN = sqlite3.connect('finance.db')
CURSOR = CONN.cursor()
