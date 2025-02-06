import json
from flask import Flask, jsonify, render_template, redirect, request
import sqlite3


# init flask api
app = Flask(__name__)

# flask routes
@app.route('/')
def default():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/messenger')
def messenger():
    return render_template('messenger.html')


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# def init_db():
#     conn = get_db_connection()
#     conn.execute('''CREATE TABLE IF NOT EXISTS users (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         name TEXT,
#                         email TEXT,
#                         username TEXT NOT NULL,
#                         password TEXT NOT NULL)''')
#
#     conn.execute('''INSERT INTO users(name, email, username, password)
#                     VALUES(?, ?, ?, ?)''',
#                  ("Alan Jith", "jith@gmail.com", "ajith", "1234"))
#     conn.commit()
#     conn.close()


@app.route('/users_testbank', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    user_list = [dict(user) for user in users]

    return jsonify(user_list)


# init_db()

# run server
if __name__ == '__main__':
    print("running")
    app.run(debug=True, port=4200)