import sqlite3
import os

connection = sqlite3.connect('database.db')

print(os.getcwd())
with open('first-flask-app\schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO tasks (content, completed) VALUES (?, ?)",
            ('Create to-do list', 1)
            )

cur.execute("INSERT INTO tasks (content) VALUES (?)",
            ('Load database',)
            )

connection.commit()
connection.close()