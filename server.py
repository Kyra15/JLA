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


# run server
if __name__ == '__main__':
    print("running")
    app.run(debug=True, port=4200)