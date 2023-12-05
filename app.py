from flask import Flask, render_template, flash, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkeythisisasecretkey'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=['GET'])
def load_page():
    conn = get_db_connection()
    inctasks = conn.execute('SELECT * FROM tasks WHERE completed = 0').fetchall()
    comtasks = conn.execute('SELECT * FROM tasks WHERE completed = 1').fetchall()
    conn.close()
    return render_template('index.html', inctasks=inctasks, comtasks=comtasks)

@app.route("/", methods=['POST'])
def create_task():
    conn = get_db_connection()
    task = request.form['task']
    if not task:
        flash("Cannot add empty task")
    else:
        conn.execute('INSERT INTO tasks (content) VALUES (?)',
                     (task,))

        conn.commit()    
        conn.close()
    
    return redirect(url_for('load_page'))

app.run(debug=True)