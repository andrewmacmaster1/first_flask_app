import sqlite3
import os

connection = sqlite3.connect('database.db')

print(os.getcwd())
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO tasks (content) VALUES (?)",
            ('Create to-do list')
            )

cur.execute("INSERT INTO tasks (content) VALUES (?)",
            ('Load database')
            )

connection.commit()
connection.close()