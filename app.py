from flask import Flask, render_template, flash, request, redirect, url_for, abort
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkeythisisasecretkey'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_task(task_id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?',
                        (task_id,)).fetchone()
    conn.close()
    if task is None:
        abort(404)
    return task

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

@app.route('/<int:id>/delete/', methods=['POST'])
def delete(id):
    task = get_task(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(task['content']))

    return redirect(url_for('load_page'))

@app.route('/<int:id>/move', methods=['POST'])
def move_task(id):
    task = get_task(id)
    conn = get_db_connection()
    if task['completed'] == 1:
        completed = 0
    else:
        completed = 1
    conn.execute('UPDATE tasks SET completed = ? WHERE id = ?',
                 (completed, id))
    conn.commit()
    conn.close()

    return redirect(url_for('load_page'))

@app.route('/<int:id>/edit', methods=['POST'])
def edit_task(id):
    conn = get_db_connection()
    new_task = request.form['edit_task']
    
    if not new_task:
        flash("Task cannot be empty")
    else:
        conn.execute('UPDATE tasks SET content = ?, created = CURRENT_TIMESTAMP WHERE id = ?',
                     (new_task, id))
        conn.commit()    
        conn.close()

    
    return redirect(url_for('load_page'))

@app.route('/clear', methods=['POST'])
def clear():
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE completed = 1')
    conn.commit()
    conn.close()

    return redirect(url_for('load_page'))

app.run(debug=True)