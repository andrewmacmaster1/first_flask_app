from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def todo():
    conn = get_db_connection()
    inctasks = conn.execute('SELECT * FROM tasks WHERE completed = 0').fetchall()
    comtasks = conn.execute('SELECT * FROM tasks WHERE completed = 1').fetchall()
    conn.close()
    return render_template('index.html', inctasks=inctasks, comtasks=comtasks)

app.run(debug=True)